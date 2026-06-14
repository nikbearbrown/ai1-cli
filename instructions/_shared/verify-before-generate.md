## Generation is the fallback, not the default (P2)

**Before generating any artifact, check it isn't already verified:** run `python scripts/verify.py check <artifact>`. If verified (exit 0), **use the existing file — do not regenerate.** If unverified, stop and say so. If absent, generate it, run `python scripts/verify.py stub <artifact> --phase <phase>`, and **STOP** for human sign-off. Only a human runs `python scripts/verify.py sign`. The sidecar (`<name>.verified.json`) is the artifact's passport. See `conductor/VERIFICATION.md`.
