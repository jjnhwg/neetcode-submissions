class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        input given is a 2d matrix and the first of each row represents a number and the output
        is to see if we can find an integer in this 2d matrix

        """

        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

        # l = mid + 1 bc l might be in the middle array check if the array at the end is greater then the target
        # if not then we know we are in the right row to then look at the column t

        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            start = matrix[mid][0]

            if target < start:
                r = mid - 1

            elif target > start and target > matrix[mid][-1]:
                l = mid + 1

            else:
                i, j = 0, len(matrix[mid]) - 1

                while i <= j:
                    
                    mid_2 = (i + j) // 2

                    if matrix[mid][mid_2] > target:
                        j = mid_2 - 1

                    elif matrix[mid][mid_2] < target:
                        i = mid_2 + 1

                    else:
                        return True
                return False

        return False
