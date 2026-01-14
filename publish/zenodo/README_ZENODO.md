# Deterministic Lattice Simulation Artifact — Spectrum v0.2.0

## Description

Spectrum is a deterministic, non-learning measurement infrastructure designed for audit-grade reproducibility. This artifact provides bit-identical lattice simulations with guaranteed deterministic replay capabilities. Every execution produces exact, verifiable outputs through canonical serialization and SHA-256 hash verification. The system eliminates all sources of non-determinism: no randomness, no time dependence, no environment variables, no floating-point arithmetic. All computations use exact rational arithmetic with immutable state transitions and canonical ordering, ensuring perfect reproducibility across platforms, Python versions, and execution environments.

## How to Verify

### Prerequisites
- Python 3.10 or later
- Install pytest: `pip install pytest`
- Set PYTHONPATH: `export PYTHONPATH=/path/to/spectrum:$PYTHONPATH`

### Verification Steps

1. **Run the deterministic test suite:**
   ```bash
   cd /path/to/spectrum
   export PYTHONPATH=$PWD:$PYTHONPATH
   pytest tests/test_determinism.py -v
   pytest tests/test_boundary_determinism.py -v
   ```

2. **Verify hash stability and canonical serialization:**
   ```bash
   pytest tests/test_canonical_serialization.py -v
   ```
   
   This confirms that lattice node serialization produces identical hashes across multiple runs.

3. **Compare against reference hashes:**
   ```bash
   sha256sum -c release/file_hashes.sha256
   ```
   
   This verifies that core source files match the release manifest (some files like README.md may differ between versions).

4. **Run all determinism validation tests:**
   ```bash
   pytest tests/test_determinism.py tests/test_canonical_serialization.py tests/test_boundary_determinism.py -v
   ```
   
   All tests should pass with zero failures, confirming bit-identical behavior.

### Expected Results

- All tests pass with zero failures
- Hash comparisons show identical values across runs
- File integrity check completes successfully
- No warnings about non-deterministic behavior

## License

Copyright 2026 AttraQtor-Labs LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Citation

To cite this artifact in publications, please use:

```bibtex
@software{spectrum_v0_2_0,
  author       = {{AttraQtor-Labs LLC}},
  title        = {Deterministic Lattice Simulation Artifact — Spectrum v0.2.0},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {0.2.0},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

**Note:** Replace `XXXXXXX` with the actual DOI assigned by Zenodo upon publication.

## Additional Information

- **Repository:** https://github.com/AttraQter-Labs/spectrum
- **Documentation:** See `README.md` and `VERIFICATION.md` in the repository root
- **Release Manifest:** `release/RELEASE_MANIFEST.json`
- **Determinism Contract:** `INTERFACE.md` and `contracts/CONTRACT.md`
