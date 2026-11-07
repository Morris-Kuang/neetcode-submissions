class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        hashset and l, r ptrs
        update res if greater
        """
        if not s:
            return 0

        seen = set()
        l, r = 0, 0
        res = 1

        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            else:
                seen.add(s[r])
            
            
            if (r - l + 1) > res:
                res = r - l + 1
            
            r += 1

        return res