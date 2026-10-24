# DS: Array
# ALGO: Binary Search. Boundary Search.
# Time: O(nlogm). Space: O(1). n = len(weights), m = sum(weights) - max(weights)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity: int) -> bool:
            daysSpent = 1
            shipmentWeight = 0
            for w in weights:
                shipmentWeight += w

                if shipmentWeight > capacity:
                    # wait for new shipment next day
                    daysSpent += 1
                    shipmentWeight = w

                    if daysSpent > days:
                        return False

            return True

        # binary search for capacity
        # capacity must be at least the max weight to avoid splitting a weight into two shipments
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                # keep mid. push left
                right = mid
            else:
                # discard mid. push right
                left = mid + 1
        return left
