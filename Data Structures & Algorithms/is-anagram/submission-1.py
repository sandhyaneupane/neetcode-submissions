class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s={}
        map_t={}
        for n in s:
            map_s[n]= 1+ map_s.get(n,0)
        for n in t:
            map_t[n]= 1+ map_t.get(n,0)

        return map_s==map_t

        