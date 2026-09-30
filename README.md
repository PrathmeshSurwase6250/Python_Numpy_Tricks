# NumPy Tricks & Practice 🚀

This repository contains my **NumPy practice code**, focusing on useful NumPy functions and tricks that are commonly used in **Data Science, Machine Learning, and Python interviews**.

The examples cover array creation, sorting, reshaping, concatenation, searching, statistical operations, and array manipulation.

---

## 🧰 Technologies Used

* Python 🐍
* NumPy

Install NumPy:

```bash
pip install numpy
```

Import NumPy:

```python
import numpy as np
```

---

# 📚 NumPy Tricks Covered

## 1. Random Integer Array

Generate random integers between a given range.

```python
rand = np.random.randint(1, 101, 15)

print(rand)
```

`np.random.randint(start, stop, size)`

Example:

```text
1 to 100 → 15 random numbers
```

> Note: The upper limit `101` is excluded, so numbers are generated from `1` to `100`.

---

## 2. Sorting an Array

Sort a 1D array:

```python
print(np.sort(rand))
```

Example:

```text
Before:
[45 12 89 23]

After:
[12 23 45 89]
```

---

# 3. Creating a 2D Random Array

```python
b = np.random.randint(1, 100, 24).reshape(6, 4)

print(b)
```

Creates:

```text
6 rows × 4 columns
```

---

# 4. Sorting a 2D Array

### Sort each row

```python
print(np.sort(b))
```

By default:

```python
axis=-1
```

So NumPy sorts each row independently.

---

## 5. Sort Columns

```python
print(np.sort(b, axis=0))
```

`axis=0` means sorting happens **vertically down each column**.

### Remember:

```text
axis=0 → columns
axis=1 → rows
```

---

# 6. Adding a Column Using `np.append()`

```python
print(
    np.append(
        b,
        np.ones((b.shape[0], 1)),
        axis=1
    )
)
```

This adds a column containing `1`s.

If:

```text
b.shape = (6, 4)
```

Then:

```python
b.shape[0]
```

gives:

```text
6
```

Therefore:

```python
np.ones((6, 1))
```

creates:

```text
[[1]
 [1]
 [1]
 [1]
 [1]
 [1]]
```

After appending:

```text
Original → 6 × 4
New      → 6 × 5
```

### Important

When using:

```python
axis=1
```

the number of rows must match.

---

# 7. `np.concatenate()`

Create two arrays:

```python
a = np.arange(6).reshape(2, 3)

b = np.arange(6, 12).reshape(2, 3)
```

### Concatenate Row-Wise

```python
c = np.concatenate((a, b), axis=0)

print(c)
```

Result:

```text
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
```

Shape:

```text
(4, 3)
```

---

### Concatenate Column-Wise

```python
c = np.concatenate((a, b), axis=1)

print(c)
```

Result:

```text
[[ 0  1  2  6  7  8]
 [ 3  4  5  9 10 11]]
```

Shape:

```text
(2, 6)
```

### Easy Rule

```text
axis=0 → add rows
axis=1 → add columns
```

---

# 8. Finding Unique Values

```python
e = np.array([
    1,1,1,2,2,3,3,4,
    4,5,6,7,7,4
])

print(np.unique(e))
```

Output:

```text
[1 2 3 4 5 6 7]
```

`np.unique()` removes duplicate values.

---

# 9. `np.expand_dims()`

Create an array:

```python
a = np.random.randint(1, 101, 30)
```

Initially:

```text
shape = (30,)
```

Convert it into a column:

```python
a = np.expand_dims(a, axis=1)

print(a)
```

Now:

```text
shape = (30, 1)
```

### Think of it as:

```text
1D array
   ↓
Add a dimension
   ↓
Column vector
```

---

# 10. `np.where()` – Find Positions

```python
print(np.where(rand > 50))
```

This returns the **indices** where the condition is true.

Example:

```python
a = np.array([10, 60, 30, 80])

np.where(a > 50)
```

Output:

```text
(array([1, 3]),)
```

Because:

```text
60 → index 1
80 → index 3
```

---

# 11. `np.where()` – Replace Values

```python
print(np.where(a > 50, 0, a))
```

Meaning:

```text
If value > 50 → replace with 0
Otherwise     → keep original value
```

Example:

```text
[10 60 30 80]

↓

[10  0 30  0]
```

This is extremely useful in **data preprocessing**.

---

# 12. Finding Maximum Index — `argmax()`

```python
print(np.argmax(rand))
```

`np.argmax()` returns the **index of the maximum value**.

Example:

```python
a = np.array([10, 50, 30, 90])

np.argmax(a)
```

Output:

```text
3
```

Because `90` is at index `3`.

> `argmax()` returns the index, not the maximum value itself.

---

# 13. `argmax()` with Axis

```python
b = np.random.randint(1, 101, 24).reshape(6, 4)

print(np.argmax(b, axis=0))
```

This finds the index of the maximum value **in each column**.

```text
axis=0 → column-wise
```

---

# 14. `argmin()`

```python
print(np.argmin(b, axis=1))
```

Finds the index of the minimum value in each row.

```text
axis=1 → row-wise
```

---

# 15. Cumulative Sum — `cumsum()`

```python
print(np.cumsum(b))
```

`np.cumsum()` calculates the running/cumulative sum.

Example:

```python
a = np.array([1, 2, 3, 4])
```

Result:

```text
[1 3 6 10]
```

Calculation:

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

---

# 16. Cumulative Product — `cumprod()`

```python
print(np.cumprod(b))
```

Calculates the running product.

Example:

```python
a = np.array([1, 2, 3, 4])
```

Result:

```text
[1 2 6 24]
```

Calculation:

```text
1
1 × 2 = 2
1 × 2 × 3 = 6
1 × 2 × 3 × 4 = 24
```

---

# 17. Percentile

```python
print(np.percentile(b, 50))
```

`50th percentile` is equivalent to the **median**.

Common percentiles:

```text
25th percentile → Q1
50th percentile → Median
75th percentile → Q3
```

Example:

```python
np.percentile(data, 50)
```

---

# 18. Histogram

```python
print(np.histogram(b, bins=[0, 50, 100]))
```

A histogram counts how many values fall inside specified ranges.

Here:

```python
bins=[0, 50, 100]
```

creates ranges approximately representing:

```text
0–50
50–100
```

`np.histogram()` returns:

```text
(counts, bin_edges)
```

---

# 19. Correlation Coefficient

```python
salary = np.array([20000, 40000, 60000, 100000])

exp = np.array([1, 2, 3, 4])

c = np.corrcoef(salary, exp)

print(c)
```

`np.corrcoef()` calculates the **correlation coefficient**.

Correlation generally ranges from:

```text
-1 → strong negative relationship
 0 → no linear relationship
+1 → strong positive relationship
```

In this example, salary and experience increase together, so the correlation is positive.

---

# 20. `np.isin()`

```python
items = np.array([10,20,30,40,50,60,70,80,90])

print(np.isin(b, items))
```

Checks whether each element of `b` exists inside `items`.

It returns a Boolean array:

```text
True
False
True
...
```

### Example

```python
a = np.array([10, 20, 30, 40])

items = np.array([20, 40])

np.isin(a, items)
```

Output:

```text
[False  True False  True]
```

---

# 21. Reverse an Array — `np.flip()`

```python
print(np.flip(items))
```

Reverses the array.

Example:

```text
[10 20 30 40]

↓

[40 30 20 10]
```

---

# 22. Replace Values Using `np.put()`

```python
np.put(items, [0, 1], [200000, 500000])

print(items)
```

`np.put()` replaces values at specified indexes.

Example:

```python
a = np.array([10, 20, 30, 40])

np.put(a, [0, 2], [100, 300])
```

Result:

```text
[100  20 300  40]
```

---

# 23. Delete Elements — `np.delete()`

```python
print(np.delete(items, [0, 1]))
```

Deletes elements at the specified indexes.

Example:

```python
a = np.array([10, 20, 30, 40])

np.delete(a, [0, 2])
```

Result:

```text
[20 40]
```

---

# 🧠 Quick NumPy Trick Cheat Sheet

| Function              | Purpose                          |
| --------------------- | -------------------------------- |
| `np.random.randint()` | Generate random integers         |
| `np.sort()`           | Sort array                       |
| `np.append()`         | Add values                       |
| `np.ones()`           | Create array of ones             |
| `np.concatenate()`    | Join arrays                      |
| `np.unique()`         | Remove duplicates                |
| `np.expand_dims()`    | Add a dimension                  |
| `np.where()`          | Find/replace based on condition  |
| `np.argmax()`         | Index of maximum                 |
| `np.argmin()`         | Index of minimum                 |
| `np.cumsum()`         | Cumulative sum                   |
| `np.cumprod()`        | Cumulative product               |
| `np.percentile()`     | Calculate percentile             |
| `np.histogram()`      | Calculate frequency distribution |
| `np.corrcoef()`       | Calculate correlation            |
| `np.isin()`           | Check membership                 |
| `np.flip()`           | Reverse array                    |
| `np.put()`            | Replace values by index          |
| `np.delete()`         | Delete values by index           |

---

# 🎯 Important Axis Concept

One of the most important NumPy concepts is `axis`.

For a 2D array:

```text
        Column
          ↓
     1   2   3
     4   5   6
     7   8   9
     ↓
```

### `axis=0`

Works **down the rows / column-wise**:

```text
1 → 4 → 7
2 → 5 → 8
3 → 6 → 9
```

### `axis=1`

Works **across columns / row-wise**:

```text
1 → 2 → 3
4 → 5 → 6
7 → 8 → 9
```

Remember:

```text
axis=0 → down
axis=1 → across
```

---

# 💼 Why These NumPy Tricks Matter

These functions are frequently useful in:

* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Machine Learning
* Statistics
* Data Science
* Feature Engineering
* Numerical Computing

The goal of this practice is not just to memorize NumPy functions, but to understand **how arrays behave with shapes, axes, conditions, and mathematical operations**.

---

## 🚀 Next Practice

After completing these NumPy tricks, practice:

1. Broadcasting
2. Boolean indexing
3. Fancy indexing
4. Matrix operations
5. `axis` in detail
6. Statistical functions
7. Linear algebra
8. Random distributions
9. Missing-value handling
10. NumPy-based data preprocessing

**NumPy → Pandas → Matplotlib/Seaborn → Statistics → Machine Learning**
