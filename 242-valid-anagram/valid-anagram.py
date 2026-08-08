class Solution(object):
    def isAnagram(self, s, t):
        mapping=[0]*26

        for ch in s:
            index = ord(ch)-97
            mapping[index]+= 1

        for ch in t:
            index = ord(ch)-97
            mapping[index]-= 1
        return all(m==0 for m in mapping)