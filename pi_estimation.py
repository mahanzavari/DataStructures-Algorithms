import random
import numpy as np
import matplotlib.pyplot as plt


"Estimating the value of Pi using the formula pi / 4 == circle / square"

def estimate_pi(num_samples):
    """Estimates the value of pi using the Monte Carlo method."""

    points_inside_circle = 0
    total_points = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_samples):
        # Generate random x and y coordinates within a square (side length 2)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Calculate the distance from the origin
        distance = x**2 + y**2

        # Check if the point is inside the unit circle (radius 1)
        if distance <= 1:
            points_inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

        total_points += 1

    # Estimate pi: (Area of Circle) / (Area of Square) = pi/4
    pi_estimate = 4 * (points_inside_circle / total_points)
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

# Run the simulation
num_samples = 10000
pi_estimate, x_inside, y_inside, x_outside, y_outside = estimate_pi(num_samples)

print(f"Estimated value of pi with {num_samples} samples: {pi_estimate}")

# Visualization
plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')

# Draw the circle
circle = plt.Circle((0, 0), 1, color='green', fill=False)
plt.gca().add_patch(circle)

plt.title(f'Monte Carlo Estimation of Pi (N={num_samples})')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.gca().set_aspect('equal', adjustable='box')  # Ensure circle looks like a circle
plt.legend()
plt.show()

# Convergence analysis
sample_sizes = [100, 1000, 10000, 100000, 1000000]
pi_estimates = []
for n in sample_sizes:
    pi_estimates.append(estimate_pi(n)[0])

plt.figure(figsize=(8, 6))
plt.plot(sample_sizes, pi_estimates, marker='o')
plt.axhline(y=np.pi, color='r', linestyle='--', label='True Pi')
plt.xscale('log')
plt.title('Convergence of Pi Estimate with Increasing Sample Size')
plt.xlabel('Number of Samples (log scale)')
plt.ylabel('Estimated Pi')
plt.legend()
plt.grid(True)
plt.show()