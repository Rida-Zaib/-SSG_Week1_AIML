# Task 1.3 — Math for ML Practice Set

## Overview
Applied problems in statistics, probability, linear algebra, and calculus, the kind
of math that shows up constantly in machine learning algorithms. Each problem is
solved and verified with code, not just worked out by hand.

## What the notebook covers

1. **Statistics** — computes mean, variance, and standard deviation of a set of
   exam scores using NumPy.
2. **Probability** — simulates 10,000 coin flips to estimate the probability of
   heads, then computes the exact probability of getting 5 heads in 10 flips
   using the binomial formula.
3. **Linear Algebra** — multiplies two matrices, and finds the determinant and
   inverse of a matrix, the same operations used in solving linear regression.
4. **Calculus** — finds the derivative of f(x) = 3x² + 2x - 5 using SymPy, and
   evaluates the slope at x = 4, the same idea used in gradient descent.

## Files
- `math_for_ml.ipynb` — the full notebook, code + outputs + explanations

## How to run
```bash
pip install numpy sympy
jupyter notebook math_for_ml.ipynb
```
Then Run All Cells.

## Key takeaways
- Variance and standard deviation describe how spread out data is around the mean.
- The simulated coin flip probability converges toward the exact value as the number
  of trials grows — the law of large numbers in action.
- Matrix multiplication and inversion are the backbone of how linear models solve
  for their weights.
- A derivative gives the slope of a function at a point, which is exactly what
  gradient descent uses to update model weights during training.

## Deliverable
PDF/notebook of worked solutions, as required by the Skill Set Go EduTech AI/ML
track, Week 1, Task 1.3.
