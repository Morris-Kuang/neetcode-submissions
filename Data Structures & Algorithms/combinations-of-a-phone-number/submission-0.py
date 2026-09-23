class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        dictionary: to store digit and its chars (key: digit, value = [a, b, c])
        decision tree
        [d, e, f] [g, h, i]
        each layer represents a digit's combination to try -- backtracking 
        base: layers = num
        decision, add first, second, or third / fourth element (for loop)

        "567" -> ['j', 'k', 'l'] ['m', 'n', 'o'] ['p', 'q', 'r', 's']
        """

        num = len(digits)
        if num == 0:
            return []

        dic = {
            '2':['a', 'b', 'c'], 
            '3':['d', 'e', 'f'], 
            '4':['g', 'h', 'i'], 
            '5':['j', 'k', 'l'], 
            '6':['m', 'n', 'o'], 
            '7':['p', 'q', 'r', 's'], 
            '8':['t', 'u', 'v'], 
            '9':['w', 'x', 'y', 'z'], 
            '0':[' ']
        }
        res = []
        letter = [] #should turn to "" in the end

        def backtrack(layer):
            if layer == num:
                res.append("".join(letter))
                return
            
            chars = dic.get(digits[layer])
            for i in chars:
                letter.append(i)
                backtrack(layer+1)
                letter.pop()
        
        backtrack(0)
        return res




            