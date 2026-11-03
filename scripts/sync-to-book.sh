#!/bin/bash
# sync-to-book.sh — push canonical scripts & recipes from this (source) repo into
# a target book repo, per SOURCE-MANIFEST.md.
#   CANONICAL → overwrite   |   SEED → copy if missing   |   PROTECTED → never touch
# SEED files come from templates/seed/ (blank per-book templates), never from this
# repo's root, whose copies are the AI1 CLI book's own filled-in files.
#
#   scripts/sync-to-book.sh [--dry-run] <target-book-dir>
set -e

DRY=0
[ "$1" = "--dry-run" ] && { DRY=1; shift; }
TARGET="$1"
[ -z "$TARGET" ] && { echo "usage: scripts/sync-to-book.sh [--dry-run] <target-book-dir>"; exit 1; }

SRC="$(cd "$(dirname "$0")/.." && pwd)"     # the ai1-cli (source) repo
MANIFEST="$SRC/SOURCE-MANIFEST.md"
SEED_SRC="$SRC/templates/seed"              # blank templates SEED copies from
[ -d "$TARGET" ] || { echo "target not found: $TARGET"; exit 1; }
[ -f "$MANIFEST" ] || { echo "manifest not found: $MANIFEST"; exit 1; }
TARGET="$(cd "$TARGET" && pwd)"
[ "$TARGET" = "$SRC" ] && { echo "refusing to sync a repo into itself"; exit 1; }

# extract a marked block from the manifest
block() { sed -n "/<!-- sync:$1 -->/,/<!-- \/sync:$1 -->/p" "$MANIFEST" | grep -vE '^<!--' | grep -vE '^\s*$'; }

# read each block into an array (while-read, not mapfile: macOS /bin/bash is 3.2)
CANON=(); while IFS= read -r line; do CANON+=("$line"); done < <(block canonical)
SEED=();  while IFS= read -r line; do SEED+=("$line");  done < <(block seed)

copied=0; seeded=0; skipped=0

copy_path() {   # $1 = relative path (file or dir/), $2 = canon | SEED
  local rel="$1" mode="$2" src="$SRC/$1" dst="$TARGET/$1"
  [ "$mode" = "SEED" ] && src="$SEED_SRC/$rel"
  if [[ "$rel" == */ ]]; then                      # whole directory (canonical only)
    [ -d "$src" ] || return 0
    echo "  [$mode dir] $rel"
    [ "$DRY" -eq 1 ] || { mkdir -p "$dst"; cp -R "$src." "$dst" 2>/dev/null || cp -R "$src"* "$dst" 2>/dev/null || true; }
    copied=$((copied+1)); return
  fi
  if [ ! -f "$src" ]; then                         # bare `return` here would exit 1 and trip set -e
    [ "$mode" = "SEED" ] && echo "  [SEED] $rel — no template at templates/seed/$rel, skipped" >&2
    return 0
  fi
  if [ "$mode" = "SEED" ] && [ -e "$dst" ]; then
    skipped=$((skipped+1)); return                 # seed: don't clobber existing
  fi
  echo "  [$mode] $rel"
  [ "$DRY" -eq 1 ] || { mkdir -p "$(dirname "$dst")"; cp "$src" "$dst"; }
  [ "$mode" = "SEED" ] && seeded=$((seeded+1)) || copied=$((copied+1))
}

echo "SYNC  $SRC  →  $TARGET   $([ $DRY -eq 1 ] && echo '(dry run)')"
echo "CANONICAL (overwrite):"
for p in "${CANON[@]}"; do copy_path "$p" "canon"; done
echo "SEED (if missing):"
for p in "${SEED[@]}";  do copy_path "$p" "SEED"; done
echo "PROTECTED: never touched (chapters/, output/, .env, *.verified.json, generated outputs, fact data)"
echo "----"
echo "done: $copied canonical copied, $seeded seeded, $skipped seed-skipped (already present)$([ $DRY -eq 1 ] && echo '  [dry run — nothing written]')"
