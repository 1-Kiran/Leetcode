class Solution(object):
    def checkInclusion(self, s1, s2):
        count_s1={}
        count_s2={}
        for i in s1:
            count_s1[i]=count_s1.get(i,0)+1

        for i in range(len(s2)-len(s1)+1):

            for j in s2[i:len(s1)+i]:
                count_s2[j]=count_s2.get(j,0)+1
            if count_s1==count_s2:
                return True
            count_s2={}
            
        return False