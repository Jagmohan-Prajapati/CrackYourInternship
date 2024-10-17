"""Given two empty jugs of m and n litres respectively. The jugs don’t have markings to allow measuring smaller quantities. You have to use the jugs to measure d litres of water. The task is to find the minimum number of operations to be performed to obtain d litres of water in one of the jugs. In case of no solution exist, return -1.

The operations you can perform are:

Empty a Jug
Fill a Jug
Pour water from one jug to the other until one of the jugs is either empty or full.
Example:

Input: m = 3, n = 5, d = 4
Output: 6
Explanation: Operations are as follow:


Initially, both jugs are empty (jug1 = 0, jug2 = 0).
Step 1: Fill the 5 liter jug -> (0, 5).
Step 2: Pour from the 5 liter jug to the 3 liter jug -> (3, 2).
Step 3: Empty the 3 liter jug -> (0, 2).
Step 4: Pour the 2 liters from the 5-liter jug to the 3 liter jug -> (2, 0).
Step 5: Fill the 5 liter jug again -> (2, 5).
Step 6: Pour 1 liter from the 5 liter jug into the 3 liter jug -> (3, 4).
Now, the 5 liter jug contains exactly 4 liters, so we stop and return 6 steps.


Input: m = 8, n = 56, d = 46
Output: -1
Explanation: Not possible to fill any one of the jug with 46 litre of water."""


def min_steps(m, n, d):
    if d > max(m, n):
        return -1 

    # Queue for BFS: (jug1, jug2, steps)
    q = deque([(0, 0, 0)])
    
    # For tracking the visited states
    visited = [[False] * (n + 1) for _ in range(m + 1)]  
    visited[0][0] = True

    while q:
        jug1, jug2, steps = q.popleft()

        if jug1 == d or jug2 == d:
            return steps

        # 1: Fill jug1
        if not visited[m][jug2]:
            visited[m][jug2] = True
            q.append((m, jug2, steps + 1))

        # 2: Fill jug2
        if not visited[jug1][n]:
            visited[jug1][n] = True
            q.append((jug1, n, steps + 1))

        # 3: Empty jug1
        if not visited[0][jug2]:
            visited[0][jug2] = True
            q.append((0, jug2, steps + 1))

        # 4: Empty jug2
        if not visited[jug1][0]:
            visited[jug1][0] = True
            q.append((jug1, 0, steps + 1))

        # 5: Pour jug1 into jug2
        pour1to2 = min(jug1, n - jug2)
        if not visited[jug1 - pour1to2][jug2 + pour1to2]:
            visited[jug1 - pour1to2][jug2 + pour1to2] = True
            q.append((jug1 - pour1to2, jug2 + pour1to2, steps + 1))

        # 6: Pour jug2 into jug1
        pour2to1 = min(jug2, m - jug1)
        if not visited[jug1 + pour2to1][jug2 - pour2to1]:
            visited[jug1 + pour2to1][jug2 - pour2to1] = True
            q.append((jug1 + pour2to1, jug2 - pour2to1, steps + 1))

    return -1 