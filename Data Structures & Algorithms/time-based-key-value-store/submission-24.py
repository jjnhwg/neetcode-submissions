class TimeMap:

    '''
    mp1 = { alice: [happy, 1], [sad, 2]}
    '''

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

      


        '''
        bug: lets say the timestamp we are looking for is 4 
        we need to find the largest timestamp < = 4
        if mid is 
        mp1 = { alice: [happy, 1], [sad, 2], [sad, 3], [sad, 4], [sad, 5] }

        r = mid - 1 happens when mid is greater than the target 

        if mid is less than or equal to the target 

        '''

        mood = self.map[key]


        l, r = 0, len(mood) - 1 

        while l <= r:

            mid = (l + r) // 2 

            if mood[mid][1] > timestamp:
                r = mid - 1 
            else:
                res = mood[mid][0]
                l = mid + 1 
        
        return res 





        '''
        the target is the largest timestamp before the actual time stamp or is the time 
        stamp 

        if the value time stamp is bigger than the actual timestamp then we 
        move to the left of the array 
        '''
