class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_plot = (i == 0) or (flowerbed[i-1] == 0)
                right_plot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if right_plot and left_plot:
                    flowerbed[i] = 1
                    count +=1
        return count >=n
        