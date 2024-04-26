class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        bool_array = []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                bool_array.append(True)
            else:
                bool_array.append(False)
        return bool_array


        