# Optimal Patrol Path Around Machines

## Problem Summary
A factory has several rectangular machines. A security robot must patrol around all machines using the shortest possible closed path. The path must enclose all rectangles and must not pass through the interior of any rectangle.

## Key Idea
Each rectangle can be represented by its four corner points. The shortest path enclosing all rectangles is the convex hull of all rectangle corners.

## Algorithm
1. Read N rectangles.
2. Convert each rectangle into 4 corner points.
3. Sort all points by x-coordinate, then y-coordinate.
4. Build the lower hull using cross product orientation.
5. Build the upper hull using cross product orientation.
6. Combine lower and upper hulls.
7. Calculate the perimeter of the convex hull.

## Mathematical Formulas

### Cross Product
cross(O, A, B) = (Ax - Ox)(By - Oy) - (Ay - Oy)(Bx - Ox)

If cross > 0, the turn is counter-clockwise.
If cross < 0, the turn is clockwise.
If cross = 0, the points are collinear.

### Distance Between Two Points
distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

### Perimeter
The perimeter is the sum of distances between consecutive convex hull points, including the distance from the last point back to the first point.

## Time Complexity
Creating all corner points: O(N)

Sorting points: O(N log N)

Building convex hull: O(N)

Total complexity: O(N log N)

## How to Run

```bash
python3 solution.py < sample_input.txt