class Solution:
    def decodeString(self, s: str) -> str:
        """
        do it layer by layer: use stack or recursive(dfs)
        stack = [] we append every element, and whenever we encounter "]", stop and trace back to the nearest "]"
        """

        stack = []
        idx = 0
        
        while idx < len(s):
            if s[idx] != "]":
                stack.append(s[idx])
                idx += 1
                continue
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # pop the "["

                # number - edge case two digit
                k = ""
                while stack and stack[-1].isdigit(): ## EDGE CASE: when we pop and stack becomes empty
                    k = stack.pop() + k
                    continue
                
                # final substr
                stack.append(substr * int(k))

                idx += 1
        
        return "".join(stack)

            

        