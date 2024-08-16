# Python program to check
# whether permutation of two
# arrays satisfy the condition
# a[i] + b[i] >= k.

# Check whether any
# permutation exists which
# satisfy the condition.


def isPossible(a, b, n, k):

    # Sort the array a[]
    # in decreasing order.
    a.sort(reverse=True)

    # Sort the array b[]
    # in increasing order.
    b.sort()

    # Checking condition
    # on each index.
    for i in range(n):
        if (a[i] + b[i] < k):
            return False

    return True


# Driver code

a = [2, 1, 3]
b = [7, 8, 9]
k = 10
n = len(a)

if(isPossible(a, b, n, k)):
    print("Yes")
else:
    print("No")