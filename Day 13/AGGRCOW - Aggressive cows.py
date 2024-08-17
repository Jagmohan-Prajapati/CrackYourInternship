"""Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1 ... xN (0 <= xi <= 1,000,000,000).
His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Input
t – the number of test cases, then t test cases follows.
* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi

Output
For each test case output one integer: the largest minimum distance.

Example
Input:
1
5 3
1
2
8
4
9
Output:
3"""

def largest_minimum_distance(N, C, stalls):
    stalls.sort()

    def can_place_cows(min_dist):
        count = 1
        last_position = stalls[0]
        
        for i in range(1, N):
            if stalls[i] - last_position >= min_dist:
                count += 1
                last_position = stalls[i]
                if count == C:
                    return True
        return False

    low, high = 1, stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result