# Optimal Patrol Path Around Machines

## Problem Summary
Given N axis-aligned rectangles on a factory floor, find the shortest
closed polygonal loop that encloses all rectangles.

---

## 1. Mathematical Explanation

### (a) Transforming Rectangles into Points
Each axis-aligned rectangle defined by opposite corners (x1, y1) and
(x2, y2) has exactly four corners:

- (x1, y1)
- (x1, y2)
- (x2, y1)
- (x2, y2)

We extract all four corners from every rectangle, producing a set of
up to 4N points. The patrol path problem then reduces to finding the
shortest closed loop enclosing all these points.

### (b) Why the Convex Hull is the Optimal Path
- Any valid patrol path must enclose all rectangles.
- Among all enclosing closed loops, the shortest one is always **convex**
  — a non-convex loop can be "shortcut" at any inward bend to reduce
  its length without losing coverage.
- The **convex hull** is the smallest convex polygon containing all
  the corner points.
- Since rectangles are convex and axis-aligned, enclosing all their
  corners guarantees enclosing the full rectangles.

Therefore, the perimeter of the convex hull of all rectangle corners
is the minimum possible patrol path length.

### (c) Algorithm: Andrew's Monotone Chain

**Why sorting is needed:**
The algorithm makes two linear passes — one left-to-right (lower hull)
and one right-to-left (upper hull). Sorting by (x, y) guarantees a
consistent geometric order so the passes produce a valid hull.

**How cross products are used:**
For three consecutive points O, A, B on the candidate hull, we compute:

```
cross(O, A, B) = (Ax − Ox)(By − Oy) − (Ay − Oy)(Bx − Ox)
```

- If cross > 0 → counter-clockwise turn → keep A
- If cross ≤ 0 → clockwise turn or collinear → remove A (not on hull)

**Time complexity:**
- Sorting 4N points: O(N log N)
- Two linear passes: O(N)
- **Overall: O(N log N)**

---

## 2. Mathematical Formulas

### Cross Product / Orientation Test
For three points O, A, B:
```
cross(O, A, B) = (Ax − Ox)(By − Oy) − (Ay − Oy)(Bx − Ox)
```

### Euclidean Distance
```
d(P, Q) = √( (Qx − Px)² + (Qy − Py)² )
```

### Perimeter of Convex Hull
If the hull has k vertices H₀, H₁, …, H_{k−1}:
```
L = Σ d(Hᵢ, H₍ᵢ₊₁₎ mod k)   for i = 0, 1, …, k−1
```

---

## 3. Code Solution

See `solution.py`

### Time Complexity: O(N log N)
### Space Complexity: O(N)

---

## Example

**Input:**
```
2
0 0 2 1
1 0 3 2
```

**Output:**
```
8.4721359550
```

---

## How to Run

```bash
python solution.py < input.txt
```

Or type input manually:
```bash
python solution.py
2
0 0 2 1
1 0 3 2
```