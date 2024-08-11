def find_latest_non_conflict(jobs, i):
    """
    Finds the index of the latest job (before index i) that doesn't conflict with job i.

    Args:
        jobs: A list of tuples representing jobs, where each tuple has the format (start_time, finish_time, weight).
        i: The index of the current job.

    Returns:
        The index of the latest non-conflicting job, or -1 if no such job exists.
    """

    for j in range(i - 1, -1, -1):
        if jobs[j][1] <= jobs[i][0]:
            return j
    return -1


def weighted_interval_scheduling(jobs):
    """
    Finds the maximum weight subset of mutually compatible jobs.

    Args:
        jobs: A list of tuples representing jobs, where each tuple has the format (start_time, finish_time, weight).

    Returns:
        The maximum total weight achievable by scheduling a compatible subset of jobs.
    """

    # Sort jobs by finish time in ascending order
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    dp = [0] * (
        n + 1
    )  # dp[i] stores the maximum weight achievable using the first i jobs

    # Base case: dp[0] = 0 (no jobs selected)

    for i in range(1, n + 1):
        print("scheduling", jobs[i - 1])
        # Option 1: Include the current job
        incl_profit = jobs[i - 1][2]  # Weight of the current job
        latest_non_conflict = find_latest_non_conflict(jobs, i - 1)
        if latest_non_conflict != -1:
            print("FOUND NEW MACHINE", latest_non_conflict)
            incl_profit += dp[latest_non_conflict + 1]

        # Option 2: Exclude the current job
        excl_profit = dp[i - 1]

        # Choose the option with maximum profit
        dp[i] = max(incl_profit, excl_profit)
        print(
            "CHOOSING CURRENT OR NEXT",
            incl_profit,
            excl_profit,
            max(incl_profit, excl_profit),
        )

    return dp[n]


jobs = [(1, 3, 5), (2, 5, 6), (4, 7, 3), (6, 9, 4), (8, 11, 2)]
print(weighted_interval_scheduling(jobs))
