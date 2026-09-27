# NumPy Percentiles (`np.percentile`) & Percentile Rank Calculation

Percentiles are fundamental tools in data analysis used to understand the distribution, spread, and relative standing of values within a dataset.

---
## 1. Finding Values at a Percentile (`np.percentile`)

`np.percentile(a, q)` calculates the $q$-th percentile value of an array. It answers the question: *"What numeric value cuts off the lower $q\%$ of the dataset?"*

```python
import numpy as np

data = np.array([10, 20, 35, 40, 50])

# Find the 50th percentile (Median)
p50 = np.percentile(data, 50)

# Find the 90th percentile
p90 = np.percentile(data, 90)

print(f"50th Percentile (Median): {p50}") # Output: 35.0
print(f"90th Percentile:          {p90}") # Output: 46.0
```

### Key Parameters:
- **`method` / `interpolation`**: Specifies how NumPy handles values when the percentile falls between two data points (e.g., `'linear'`, `'lower'`, `'higher'`, `'nearest'`, `'midpoint'`). The default is `'linear'`.
- **`axis`**: Computes percentiles across rows (`axis=1`) or columns (`axis=0`) for multi-dimensional arrays.

```python
# Compute multiple percentiles at once
p25_75 = np.percentile(data, [25, 75])
print(f"IQR boundaries (25th & 75th): {p25_75}") # Output: [20. 40.]
```

---
## 2. NumPy Percentile Rank Calculation

Calculating a percentile rank is the inverse of `np.percentile()`. Instead of asking *"what value represents the 90th percentile?"*, calculating rank answers *"what percentile position does a value $x$ occupy within a given dataset?"*

### 2.1. Mathematical Formula

To account for duplicate ties, the standard percentile rank formula is:

$$\text{Percentile Rank} = \left( \frac{L + 0.5 \times E}{N} \right) \times 100$$

Where:
- $L$ = Number of elements strictly less than $x$
- $E$ = Number of elements equal to $x$
- $N$ = Total number of observations

### 2.2. Practical Implementations

#### Method A: Pure Vectorized NumPy (Fast & Lightweight)
```python
import numpy as np

def calculate_percentile_rank(arr, val):
    count_less = np.sum(arr < val)
    count_equal = np.sum(arr == val)
    return ((count_less + 0.5 * count_equal) / len(arr)) * 100

data = np.array([10, 20, 35, 40, 50])
score = 35

rank = calculate_percentile_rank(data, score)
print(f"Percentile rank of {score}: {rank:.1f}%")  # Output: 50.0%
```

#### Method B: Using `scipy.stats.percentileofscore`
```python
import numpy as np
from scipy import stats

data = np.array([10, 20, 35, 40, 50])
score = 35

# kind='mean' implements the (L + 0.5*E) / N formulation
rank = stats.percentileofscore(data, score, kind='mean')
print(f"SciPy Rank: {rank:.1f}%")  # Output: 50.0%
```

### 2.3. Worked Example

Given dataset: `arr = [10, 20, 35, 40, 50]` ($N = 5$), Target Value: `35`

1. Count strictly lower values ($10, 20$): $L = 2$
2. Count equal values ($35$): $E = 1$
3. Evaluate formula:

$$\text{Percentile Rank} = \left( \frac{2 + 0.5 \times 1}{5} \right) \times 100 = \left( \frac{2.5}{5} \right) \times 100 = 50.0\%$$

### 2.4. Analytical Applications

- **Customer Segmentation:** Assigning users to engagement tiers (e.g., top 10% highly active users).
- **Normalized Benchmarking:** Comparing test performance across varied scale distributions.