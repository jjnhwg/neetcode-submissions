class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''
        input array of temp 
        output an array where how many days until there is a warmer temp 

        walkthrough: 



        '''

        stack = [] # the stack will keep track of days that havent found a warmer temperature 

        res = len(temperatures) * [0]

        #the top of the stack will not be popped until there is a warmer temp and then you can minus the diff 
        #bewteen the days to get ther esult

        for temp in range(len(temperatures)):

            while stack and temperatures[temp] > stack[-1][0]:
                val = stack.pop()
                res[val[1]] = temp - val[1]

            stack.append([temperatures[temp], temp])
        
        
        return res

        




        
        