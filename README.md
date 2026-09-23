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