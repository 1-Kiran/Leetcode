class Solution(object):
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        count_s1 = {}
        count_s2 = {}

        for ch in s1:
            count_s1[ch] = count_s1.get(ch, 0) + 1

        for ch in s2[:len(s1)]:
            count_s2[ch] = count_s2.get(ch, 0) + 1

        if count_s1 == count_s2:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            old = s2[left]
            count_s2[old] -= 1
            if count_s2[old] == 0:
                del count_s2[old]
            left += 1
            new = s2[right]
            count_s2[new] = count_s2.get(new, 0) + 1
            if count_s1 == count_s2:
                return True

        return False