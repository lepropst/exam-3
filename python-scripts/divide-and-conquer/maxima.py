from typing import List, Tuple


def find_maxima(S: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Finds the maximal points in a set of 2D points using a divide-and-conquer approach.

    Args:
      S: A list of tuples representing 2D points (x, y).

    Returns:
      A list of tuples representing the maximal points.
    """

    # Base case: If there's only one point, it's the maximum
    if len(S) == 1:
        return S

    # Divide: Find the median x-value to split the set
    S.sort(key=lambda point: point[0])  # Sort by x-coordinate
    mid = len(S) // 2
    L = S[mid][0]  # The dividing line's x-coordinate

    S_left = [point for point in S if point[0] < L]
    S_right = [point for point in S if point[0] >= L]

    # Conquer: Recursively find maxima in the left and right subsets
    maxima_left = find_maxima(S_left)
    maxima_right = find_maxima(S_right)

    # Combine: Find the largest y-value in the right subset
    y_right = max(point[1] for point in maxima_right)

    # Filter out points in the left subset with y-values less than y_right
    maxima_left = [point for point in maxima_left if point[1] >= y_right]

    # Combine the remaining maxima from both subsets
    return maxima_left + maxima_right


def main():
    points = [(0, 1), (3, 4), (5, 6), (2, 4), (6, 9), (7, 9), (8, 9)]
    print(find_maxima(points))


if __name__ == "__main__":
    main()
