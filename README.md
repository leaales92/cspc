# CSPC Lab A
## PW1 — Lab A

### Tests
All three tests passed successfully:
- simulation starts at N0
- negative decay rate raises ValueError
- average simulation result agrees with the analytical decay law

### Speed comparison
- Pure Python time: 2.793 s
- NumPy time: 0.000331 s
- Speed-up: approximately 8444x

### Conclusion
The NumPy implementation is much faster than the pure Python loop because NumPy performs the calculations in a vectorized and optimized way. All three tests passed, so the simulation behaves as expected.

## PW1 — Lab B

The observed count decreases over time and follows the same overall exponential decay trend as the analytical curve. The observed data match the analytical law reasonably well, although there are small differences between the observed points and the smooth theoretical curve.

The Snakemake pipeline automatically generates `figure.png` from `decay_observed.csv` by running `plot.py`, and it only reruns the rule when the required files have changed.
