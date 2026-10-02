# PW2 — Lab A: Motion from Tracking Data

## Goal

The goal of this lab was to recover the velocity and acceleration of a falling object from noisy position measurements and then integrate the acceleration back to recover velocity and position.

## Results

The mean acceleration obtained from the data was approximately:

**-9.81 m/s²**

This is close to the expected gravitational acceleration.

The standard deviation of the acceleration was:

**[PUT YOUR VALUE HERE] m/s²**

The acceleration is much noisier than the position because differentiation amplifies small measurement errors in the data. Since acceleration is obtained after differentiating twice, the noise becomes even larger.

After integrating the acceleration back to velocity and then to position, the recovered position was close to the original position.

The largest difference between the original and recovered position was:

**[PUT YOUR VALUE HERE] m**

Integration reduces the effect of random noise because positive and negative errors partially cancel when the values are accumulated.

## Plot

The figure `motion.png` contains three panels:

1. Position vs time
2. Velocity vs time
3. Acceleration vs time

The acceleration plot also contains the theoretical gravitational acceleration line at **-9.81 m/s²**.

Overall, the position data is smooth, the velocity is slightly noisy, and the acceleration is much noisier.