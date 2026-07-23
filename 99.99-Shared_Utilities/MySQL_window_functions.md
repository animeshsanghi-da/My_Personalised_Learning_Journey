# Comprehensive Guide to MySQL Window Functions

Window functions in MySQL (introduced in version 8.0) perform calculations across a set of table rows that are somehow related to the current row. Unlike aggregate functions that group multiple rows into a single output row, window functions evaluate and return a value for each row in the result set.

## The `OVER()` Clause
The `OVER()` clause defines the window (the set of rows) on which the function operates. It has three optional components:
1. **PARTITION BY**: Divides the result set into partitions (groups) to which the window function is applied.
2. **ORDER BY**: Specifies the logical order of the rows within each partition.
3. **Frame Clause**: Further restricts the rows within the partition (e.g., `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`).

---

## Sample Data for Examples
Assume we have the following `employee_sales` table for the examples below:

``` sql
CREATE TABLE employee_sales (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    sales_amount DECIMAL(10,2)
);
```

---

## 1. Ranking Window Functions

### ROW_NUMBER()
**Definition:** Assigns a unique, sequential integer to each row within a partition, starting at 1 for the first row. If values are tied, it still assigns distinct, consecutive numbers.
**Syntax:** 
``` sql
ROW_NUMBER() OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Assign a row number to employees based on their sales amount from highest to lowest.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    ROW_NUMBER() OVER (ORDER BY sales_amount DESC) AS row_num
FROM employee_sales;
```

### RANK()
**Definition:** Assigns a rank to each row within a partition. If there are ties, the tied rows get the same rank, and the next rank skips the tied number (e.g., 1, 2, 2, 4).
**Syntax:** 
``` sql
RANK() OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Rank employees within each department by sales.
``` sql
SELECT 
    emp_name, 
    department, 
    sales_amount,
    RANK() OVER (PARTITION BY department ORDER BY sales_amount DESC) AS sales_rank
FROM employee_sales;
```

### DENSE_RANK()
**Definition:** Similar to `RANK()`, but it does not skip rank numbers when there are ties (e.g., 1, 2, 2, 3).
**Syntax:** 
``` sql
DENSE_RANK() OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Find the dense rank of employees by sales.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    DENSE_RANK() OVER (ORDER BY sales_amount DESC) AS dense_sales_rank
FROM employee_sales;
```

### PERCENT_RANK()
**Definition:** Calculates the percentile rank of a row within a partition. The formula is `(rank - 1) / (total_rows - 1)`. The return value ranges from 0 to 1.
**Syntax:** 
``` sql
PERCENT_RANK() OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Calculate the percentile rank of sales amounts.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    PERCENT_RANK() OVER (ORDER BY sales_amount) AS pct_rank
FROM employee_sales;
```

### CUME_DIST()
**Definition:** Calculates the cumulative distribution of a value within a group. It represents the proportion of rows with a value less than or equal to the current row's value. Return value ranges from >0 to 1.
**Syntax:** 
``` sql
CUME_DIST() OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Find the cumulative distribution of sales.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    CUME_DIST() OVER (ORDER BY sales_amount) AS cumulative_dist
FROM employee_sales;
```

### NTILE()
**Definition:** Divides the rows in a sorted partition into a specified number of roughly equal groups (or "buckets"), and assigns a bucket number to each row.
**Syntax:** 
``` sql
NTILE(number_of_buckets) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Divide employees into 4 quartiles based on their sales.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    NTILE(4) OVER (ORDER BY sales_amount DESC) AS quartile
FROM employee_sales;
```

---

## 2. Value Window Functions

### LEAD()
**Definition:** Provides access to a row at a specified physical offset *after* the current row within the partition. Useful for comparing a current row's value with the next row's value. (It returns the **next row**)
**Syntax:** 
``` sql
LEAD(expression [, offset [, default_value]]) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Compare an employee's sales with the next employee's sales in the ranked list.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    LEAD(sales_amount, 1, 0) OVER (ORDER BY sales_amount DESC) AS next_lower_sales
FROM employee_sales;
```

### LAG()
**Definition:** Provides access to a row at a specified physical offset *before* the current row within the partition. (It returns the **previous row**)
**Syntax:** 
``` sql
LAG(expression [, offset [, default_value]]) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
)
```
**Example:** Compare an employee's sales with the previous employee's sales in the ranked list.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    LAG(sales_amount, 1, 0) OVER (ORDER BY sales_amount DESC) AS next_higher_sales
FROM employee_sales;
```

### FIRST_VALUE()
**Definition:** Returns the value of the specified expression from the first row of the window frame.
**Syntax:** 
``` sql
FIRST_VALUE(expression) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
    [frame_clause]
)
```
**Example:** Compare each employee's sales against the top seller in their department.
``` sql
SELECT 
    emp_name, 
    department, 
    sales_amount,
    FIRST_VALUE(sales_amount) OVER (PARTITION BY department ORDER BY sales_amount DESC) AS highest_dept_sales
FROM employee_sales;
```

### LAST_VALUE()
**Definition:** Returns the value of the specified expression from the last row of the window frame. *Note: The default frame is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, so to get the true last value of a partition, you usually need to explicitly define the frame.*
**Syntax:** 
``` sql
LAST_VALUE(expression) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
    [frame_clause]
)
```
**Example:** Compare each employee's sales against the lowest seller in the entire company.
``` sql
SELECT 
    emp_name, 
    sales_amount,
    LAST_VALUE(sales_amount) OVER (
        ORDER BY sales_amount DESC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS lowest_company_sales
FROM employee_sales;
```

### NTH_VALUE()
**Definition:** Returns the value of the expression from the *N*-th row of the window frame. If that row does not exist, it returns NULL.
**Syntax:** 
``` sql
NTH_VALUE(expression, N) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
    [frame_clause]
)
```
**Example:** Find the sales amount of the 2nd highest seller in each department.
``` sql
SELECT 
    emp_name, 
    department, 
    sales_amount,
    NTH_VALUE(sales_amount, 2) OVER (PARTITION BY department ORDER BY sales_amount DESC) AS second_highest_sales
FROM employee_sales;
```

---

## 3. Aggregate Functions as Window Functions

Standard aggregate functions (`SUM`, `AVG`, `MIN`, `MAX`, `COUNT`) can also act as window functions when paired with the `OVER()` clause. Instead of collapsing rows, they return the aggregated value alongside the original rows.

### SUM()
**Definition:** Calculates the total sum of a numeric expression across the rows within the window frame. When paired with an `ORDER BY` clause, it is highly useful for calculating running totals.
**Syntax:** 
``` sql
SUM(expression) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
    [frame_clause]
)
```

**Example:** Calculate a running total of sales amounts from highest to lowest.
``` sql
SELECT 
    emp_name,
    sales_amount,
    SUM(sales_amount) OVER (ORDER BY sales_amount DESC) AS running_total
FROM employee_sales;
```

### AVG()
**Definition:** Calculates the average value of a numeric expression across the rows within a specific window frame or partition.
**Syntax:** 
``` sql
AVG(expression) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
    [frame_clause]
)
```

**Example:** Calculate the average sales for each department alongside the individual employee records.
``` sql
SELECT 
    emp_name,
    department,
    sales_amount,
    AVG(sales_amount) OVER (PARTITION BY department) AS dept_avg_sales
FROM employee_sales;
```

### MIN() and MAX()
**Definition:** Returns the minimum or maximum value of the expression within the window frame. Useful for finding the highest or lowest value in a rolling window or partition without collapsing the rows into a single output.
**Syntax:** 
``` sql
MIN(expression) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
    [frame_clause]
)
```

**Example:** Find the maximum and minimum sales achieved so far in each department (a running max/min ordered sequentially by employee ID).
``` sql
SELECT 
    emp_name,
    department,
    sales_amount,
    MAX(sales_amount) OVER (PARTITION BY department ORDER BY emp_id) AS rolling_max_sales,
    MIN(sales_amount) OVER (PARTITION BY department ORDER BY emp_id) AS rolling_min_sales
FROM employee_sales;
```

### COUNT()
**Definition:** Counts the number of rows within the window frame or partition.
**Syntax:** 
``` sql
COUNT(expression) OVER (
    [PARTITION BY expression]
    [ORDER BY expression]
    [frame_clause]
)
```

**Example:** Count how many employees are in each department alongside their individual data.
``` sql
SELECT 
    emp_name,
    department,
    sales_amount,
    COUNT(emp_id) OVER (PARTITION BY department) AS dept_headcount
FROM employee_sales;
```

---

## 4. Deep Dive: The Frame Clause (`ROWS` vs `RANGE`)

To make this guide truly comprehensive, you must understand the **Frame Clause**, which dictates exactly which rows within a partition are evaluated by the window function. 

*Note: If you use `ORDER BY` without specifying a frame, MySQL applies a default frame:* `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. 

### Syntax
``` sql
{ROWS | RANGE} BETWEEN frame_start AND frame_end
```

**Keywords for `frame_start` and `frame_end`:**
* `UNBOUNDED PRECEDING`: The frame starts at the very first row of the partition.
* `[N] PRECEDING`: The frame starts/ends `N` rows before the current row.
* `CURRENT ROW`: The frame starts/ends exactly at the current row.
* `[N] FOLLOWING`: The frame starts/ends `N` rows after the current row.
* `UNBOUNDED FOLLOWING`: The frame ends at the very last row of the partition.

### `ROWS` vs `RANGE`
* **`ROWS`**: Treats rows as physical entities. For example, `1 PRECEDING` means exactly one literal row above the current one.
* **`RANGE`**: Treats rows as logical values based on the `ORDER BY` clause. If multiple rows have the exact same value in the `ORDER BY` column (a tie), they are evaluated together as a single logical block.

### Advanced Examples

**Example 1: 3-Period Moving Average (using `ROWS`)**
This calculates the average of the previous row, the current row, and the next row (useful for smoothing out time-series data).
``` sql
SELECT 
    emp_name,
    sales_amount,
    AVG(sales_amount) OVER (
        ORDER BY emp_id 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) AS moving_avg
FROM employee_sales;
```

**Example 2: Total Sum for the Entire Partition (Overriding the default frame)**
If you use `ORDER BY` but want the sum of the *entire* partition on every single row (not just a running cumulative total), you must explicitly redefine the frame to include all following rows.
``` sql
SELECT 
    emp_name,
    department,
    sales_amount,
    SUM(sales_amount) OVER (
        PARTITION BY department 
        ORDER BY sales_amount 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS total_dept_sales_repeated
FROM employee_sales;
```