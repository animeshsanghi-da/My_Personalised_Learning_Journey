# NumPy Standard Deviation (`np.std`)

`np.std()` measures the dispersion or spread of values relative to their mean. By default, it computes the **population standard deviation**:
$$\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N - \text{ddof}}}$$

Where $\mu$ is the array mean, $N$ is total elements, and `ddof` (Degrees of Freedom) defaults to **0**.
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Standard Deviation:", np.std(arr))  # Output: 14.142135623730951
```

---

## 1. Why Use Standard Deviation? (Practical Example)

The mean alone can be misleading because two datasets with the **exact same average** can have vastly different risk, consistency, and distribution. Standard deviation measures consistency and risk.

### Scenario: Comparing Two Investments
Imagine analyzing daily returns for two stocks over 5 days:
```python
import numpy as np

# Both stocks have an average return of $100 per day
stock_a = np.array([98, 102, 100, 99, 101])  # Highly stable
stock_b = np.array([10, 200, 50, 190, 50])   # Highly volatile

print("Stock A Mean:", np.mean(stock_a))  # Output: 100.0
print("Stock B Mean:", np.mean(stock_b))  # Output: 100.0

print("Stock A Std: ", np.std(stock_a))   # Output: ~1.41 (Low Risk / Predictable)
print("Stock B Std: ", np.std(stock_b))   # Output: ~76.42 (High Risk / Volatile)
```

**Key Takeaway:** Looking only at the mean suggests both stocks perform identically. Calculating the standard deviation reveals that **Stock A** offers consistent performance, whereas **Stock B** carries significant volatility and risk.

---

## 2. Worked Step-by-Step Calculation

For `arr = [10, 20, 30, 40, 50]`:

1. **Mean ($\mu$):** $(10 + 20 + 30 + 40 + 50) / 5 = 30.0$
2. **Squared Deviations:** $(10-30)^2 = 400$, $(20-30)^2 = 100$, $(30-30)^2 = 0$, $(40-30)^2 = 100$, $(50-30)^2 = 400$
3. **Variance ($\sigma^2$):** $(400 + 100 + 0 + 100 + 400) / 5 = 200.0$
4. **Standard Deviation ($\sigma$):** $\sqrt{200.0} \approx 14.1421$

---

## 3. Crucial Trap: NumPy (`ddof=0`) vs. Pandas / Excel (`ddof=1`)

- **NumPy default (`ddof=0`):** Population SD (divides by $N$). Use when analyzing an entire dataset population.
- **Pandas / Excel default (`ddof=1`):** Sample SD (divides by $N - 1$). Use when calculating metrics from a sample drawn from a larger population (Bessel's correction).

```python
import pandas as pd
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Pandas defaults to sample standard deviation (ddof=1)
print("Pandas default:", pd.Series(arr).std())  # 15.811388

# Match Pandas output in NumPy by passing ddof=1
print("NumPy (ddof=1):", np.std(arr, ddof=1))    # 15.811388
```

---

## 4. Axis-wise Computations & Data Science Applications

In 2D matrices (features vs. samples), calculate standard deviation across rows or columns:

```python
import numpy as np

matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

# Feature-wise SD (down columns): axis=0
print("Column SD:", np.std(matrix, axis=0))  # Output: [15. 15. 15.]

# Observation-wise SD (across rows): axis=1
print("Row SD:   ", np.std(matrix, axis=1))  # Output: [8.16496581 8.16496581]
```

### Key Use Cases in Analytics:
1. **Feature Scaling (Z-Score Standardization):** Centering data via $z = \frac{x - \mu}{\sigma}$ (used in `StandardScaler`).
2. **Anomaly Detection:** Outliers are typically identified as points exceeding $\pm 2\sigma$ or $\pm 3\sigma$ from the mean.
3. **Volatility Analysis:** Measuring financial risk and performance consistency.