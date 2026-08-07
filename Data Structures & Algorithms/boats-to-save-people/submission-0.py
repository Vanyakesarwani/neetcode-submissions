class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        i, j = 0, len(people)-1
        people.sort()
        while i <= j:
            if people[i] + people[j] <= limit:
                boat += 1
                i += 1
                j -= 1
            else:
                boat += 1
                j -= 1
        return boat