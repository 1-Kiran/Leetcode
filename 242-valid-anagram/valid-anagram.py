class Solution(object):
    def isAnagram(self, s, t):
        s_data={}
        t_data={}
        for i in s:
            s_data[i]=s_data.get(i,0)+1
        for i in t:
            t_data[i]=t_data.get(i,0)+1
        if s_data==t_data:
            return True
        return False
        