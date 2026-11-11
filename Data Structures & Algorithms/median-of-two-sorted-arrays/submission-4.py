class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #the median is the middle numbers divided by 2 


        newArr = nums1 + nums2 

        newArr.sort()

        total = len(newArr)

        if total % 2 == 0:

            index1 = total // 2 
            index2 = (total // 2) - 1

            return (newArr[index1] + newArr[index2]) / 2
        
        else:
            return newArr[total // 2] 
        


           
        



        


