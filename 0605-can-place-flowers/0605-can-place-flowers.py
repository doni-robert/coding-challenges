class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        indices = len(flowerbed) - 1
        for i in range(indices + 1): 
                # empty_prev = True or False
                empty_prev = (i == 0) or (flowerbed[i - 1] == 0)
                # empty_next = True or False
                empty_next = (i == indices) or (flowerbed[i + 1] == 0)
            
                if empty_prev and empty_next and flowerbed[i] == 0:
                    # Plant a flower here
                    flowerbed[i] = 1
                    n -= 1
    
        return n <= 0
        