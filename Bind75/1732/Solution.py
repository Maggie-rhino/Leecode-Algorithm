class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude =0
        current =0
        for i in range(len(gain)):
            current = current + gain[i]
            highest_altitude = max(current,highest_altitude)
        return highest_altitude