# NumPy Exponential Function (`np.exp`)

`np.exp(x)` computes the element-wise exponential ($e^x$) for every entry in an array, where $e \approx 2.71828$ (Euler's number).

```python
import numpy as np

arr = np.array([1, 2, 3])
print(np.exp(arr))
# Output: [ 2.71828183  7.3890561  20.08553692]
```

---
## 1. Mathematical Breakdown

Under the hood, $e^x$ is approximated using the **Taylor Series expansion**:
$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots$$

**Step-by-step for $x = 1$:**
$$\begin{aligned} e^1 &\approx 1 + 1 + \frac{1^2}{2} + \frac{1^3}{6} + \frac{1^4}{24} \\     &= 1 + 1 + 0.5 + 0.1666 + 0.0416 \approx 2.7082 \quad (\to 2.71828) \end{aligned}$$

---

## 2. Analytics & Machine Learning Applications

### A. Reversing Log Transformations (Inverting Log Scaling)
When training models on right-skewed targets (e.g., house prices or sales revenue), we often apply `np.log()` during preprocessing. `np.exp()` converts predictions back to actual monetary units.

```python
log_pred = 11.512925
actual_price = np.exp(log_pred)
print(f"Predicted Price: ${actual_price:,.2f}")  # Output: $100,000.00
```

### B. Activation Functions & Probability Mapping
ML models output raw numeric scores (logits). `np.exp()` transforms these into probabilities because $e^x$ maps any real number to a strictly positive value:

- **Sigmoid (Binary Classification):** 
$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

- **Softmax (Multi-class Classification):** 
$$P(i) = \frac{e^{z_i}}{\sum e^{z_j}}$$

---

## 3. Practical Workflow Example

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Simulated dataset: skewed revenue
np.random.seed(42)
ad_spend = np.random.uniform(10, 100, 100)
revenue = np.exp(3.0 + 0.03 * ad_spend + np.random.normal(0, 0.1, 100))

# 1. Transform target using np.log to handle skewness
y_log = np.log(revenue)
X = ad_spend.reshape(-1, 1)

# 2. Fit model
model = LinearRegression().fit(X, y_log)

# 3. Predict & convert back to original scale using np.exp
log_preds = model.predict([[50]])
actual_pred = np.exp(log_preds[0])

print(f"Predicted Revenue for $50 Ad Spend: ${actual_pred:,.2f}")
```

> **Pro Tip:** If your target column contains zeros, use `np.log1p(x)` ($\log(1+x)$) to avoid infinity errors, and reverse it with `np.expm1(x)` ($e^x - 1$).