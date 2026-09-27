# NumPy Discrete Difference (`np.diff`)

`np.diff(arr)` computes differences between adjacent array entries ($a[i+1] - a[i]$). It measures rates of change and step deltas rather than static values.

```python
import numpy as np

sales = np.array([10, 15, 25, 40, 38])
delta = np.diff(sales)

print("Raw Data:    ", sales)
print("Step Deltas: ", delta)  # Output: [ 5 10 15 -2]
```

*Note: Output length is $N - 1$ because the final element has no subsequent pair.*

---

## 1. Axis & Higher-Order Options (`n` & `axis`)

### A. 2D Array Axis Operations
By default, `np.diff()` operates along columns (`axis=-1`). Pass `axis=0` to difference vertically across rows.

```python
import numpy as np

matrix = np.array([[1, 4, 10],
                   [2, 8, 20]])

print("Column Differences (axis=1):\n", np.diff(matrix, axis=1))
print("Row Differences    (axis=0):\n", np.diff(matrix, axis=0))
```
Output:-
```plaintext
Column Differences (axis=1):
 [[ 3  6]
 [ 6 12]]
Row Differences    (axis=0):
 [[ 1  4 10]]
```

### B. Higher-Order Differences (`n=2`)
`n=2` calculates the second-order difference (the difference of differences, or acceleration).

```python
arr = np.array([10, 15, 25, 40, 42])
#                \ / \ / \ / \ / 
# n=1:            [5, 10, 15, 2]
#                   \ / \ / \ /
# n=2:               [5, 5, -13]   <-- [10-5, 15-10, 2-15]
print("2nd Order Diff:", np.diff(arr, n=2))  # Output: [ 5  5 -13]
```

---

## 2. Practical Data Science Applications

### 1. Time-Series Stationarity
Time series modeling algorithms (e.g., ARIMA) require stationary input data (stable mean and variance). Applying `np.diff()` removes baseline linear trends.

### 2. De-cumulating Aggregated Data
Recovering periodic intervals from cumulative metrics (e.g., step counters or total monthly revenues).

### 3. Anomaly & Outlier Spike Detection
Identifying sudden physical crashes or rapid telemetry changes by screening for excessive threshold shifts: $\Delta x > \text{threshold}$.

```python
import numpy as np

server_latency = np.array([45, 48, 50, 49, 420, 52])
spikes = np.where(np.abs(np.diff(server_latency)) > 100)[0]

print("Latency anomaly detected after index:", spikes)  # Output: [3 4]
```