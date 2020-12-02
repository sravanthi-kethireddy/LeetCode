import collections
class TimeMap(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myDs = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.myDs[key].append((value, timestamp))
        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.myDs:
            print( "null")
        arr = self.myDs[key]
        i = len(arr)-1
        while i>=0 and arr[i][1]>timestamp:
            i-=1

        if i >= 0:
            print( arr[i][0])
        else:
            print( "null")
        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
key = ["set","get","get","set","get","get"]
kvPair = [["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
inout = list(zip(key, kvPair))
# for each in inout:
obj.set('foo', 'bar', 1)
obj.get('foo', 1)
obj.get('foo', 3)
obj.set('foo', 'bar2', 4)
obj.get('foo', 4)
obj.get('foo', 5)
    
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)