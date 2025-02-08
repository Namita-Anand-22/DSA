def min_lifter_capacity(A, B):
    """
    Binary search approach to find the minimum capacity M required 
    to transport all boxes within B days.
    """
    def can_transport(M):
        days_used = 1
        current_load = 0

        for weight in A:
            if current_load + weight > M:
                days_used += 1
                current_load = 0
            current_load += weight

            if days_used > B:
                return False
        return True

    # Binary search range between max(A) and sum(A)
    left, right = max(A), sum(A)

    while left < right:
        mid = (left + right) // 2
        if can_transport(mid):
            right = mid  # Try smaller M
        else:
            left = mid + 1  # Increase M

    return left  # The minimum M found

# Example Input
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = 5

# Compute and print result
print("Minimum required capacity M:", min_lifter_capacity(A, B))
