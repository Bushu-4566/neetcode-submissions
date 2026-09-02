class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            current = 0

            for w in weights:
                if current + w > cap:
                    ships += 1
                    current = 0

                current += w

            return ships <= days

        while l <= r:
            mid = l + (r - l) // 2

            if canShip(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

        