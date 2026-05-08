import sys
import math

def cross(o, a, b):
    """
    Returns cross product of OA and OB.
    Positive  -> counter-clockwise turn
    Negative  -> clockwise turn
    Zero      -> collinear
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def distance(p1, p2):
    """
    Returns Euclidean distance between two points.
    """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def convex_hull(points):
    """
    Computes convex hull using Andrew's Monotone Chain Algorithm.
    Returns hull points in order.
    """

    # Remove duplicate points and sort
    points = sorted(set(points))

    # If only one point exists, hull is that point
    if len(points) <= 1:
        return points

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Remove last point of each half because it is repeated
    hull = lower[:-1] + upper[:-1]

    return hull


def calculate_perimeter(hull):
    """
    Calculates perimeter of convex hull.
    """
    if len(hull) <= 1:
        return 0.0

    perimeter = 0.0
    n = len(hull)

    for i in range(n):
        perimeter += distance(hull[i], hull[(i + 1) % n])

    return perimeter


def main():
    input_data = sys.stdin.read().strip().split()

    if not input_data:
        return

    N = int(input_data[0])
    points = []

    index = 1

    for _ in range(N):
        x1 = float(input_data[index])
        y1 = float(input_data[index + 1])
        x2 = float(input_data[index + 2])
        y2 = float(input_data[index + 3])
        index += 4

        # Add the four corners of the rectangle
        points.append((x1, y1))
        points.append((x1, y2))
        points.append((x2, y1))
        points.append((x2, y2))

    hull = convex_hull(points)
    perimeter = calculate_perimeter(hull)

    print(f"{perimeter:.10f}")


if __name__ == "__main__":
    main()