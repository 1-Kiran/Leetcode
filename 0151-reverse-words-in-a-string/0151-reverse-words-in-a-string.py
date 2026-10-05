class Solution(object):
    def reverseWords(self, s):
        s_list=s.split()
        l=0
        r=len(s_list)-1
        while l<r:
            s_list[l],s_list[r]=s_list[r],s_list[l]
            l+=1
            r-=1
        return " ".join(s_list)