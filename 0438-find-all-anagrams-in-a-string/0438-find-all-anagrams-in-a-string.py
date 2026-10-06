class Solution(object):
    def findAnagrams(self, s, p):
        count_p = {}
        count_s = {}
        l=[]

        for ch in p:
            count_p[ch] = count_p.get(ch, 0) + 1

        for ch in s[:len(p)]:
            count_s[ch] = count_s.get(ch, 0) + 1

        if count_p == count_s:
            l.append(0)

        left = 0

        for right in range(len(p), len(s)):
            old = s[left]
            count_s[old] -= 1
            if count_s[old] == 0:
                del count_s[old]
            left += 1
            new = s[right]
            count_s[new] = count_s.get(new, 0) + 1
            if count_p == count_s:
                l.append(left)

        return l