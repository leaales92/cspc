"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0
 
def k_imbalance(x):
    return (2*x)**2 / ((1-x)*(1-x)) - K

# 1) Newton method
x_newton = newton(k_imbalance, x0=0.5)

print("Newton x =", x_newton)

# 2) SLSQP method
def objective(x):
    return k_imbalance(x[0])**2

result = minimize(
    objective,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 0.999)]
)

x_slsqp = result.x[0]

print("SLSQP x =", x_slsqp)

# Equilibrium amounts
n_H2 = 1 - x_newton
n_I2 = 1 - x_newton
n_HI = 2 * x_newton

print("H2 =", n_H2)
print("I2 =", n_I2)
print("HI =", n_HI)

# Plot
x_values = np.linspace(0, x_newton, 100)

H2 = 1 - x_values
I2 = 1 - x_values
HI = 2 * x_values

plt.plot(x_values, H2, label="H2")
plt.plot(x_values, I2, label="I2")
plt.plot(x_values, HI, label="HI")

plt.axvline(x_newton, linestyle="--", label="Equilibrium")

plt.xlabel("Reaction extent x")
plt.ylabel("Amount (mol)")
plt.legend()

plt.savefig("equilibrium.png")
plt.show()
# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
