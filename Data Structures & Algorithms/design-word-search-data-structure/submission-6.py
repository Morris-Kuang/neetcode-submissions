class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        # let all char go in dfs -- HARD!
        def dfs(trie, i):
            # base
            if i == len(word):
                return trie.isEnd

            c = word[i]
            if c == ".":
                for child in trie.children.values():
                    if dfs(child, i + 1):  # cannot directly return the dfs boolean, since this is only one route testing, might still have another that work
                        return True
                    else:
                        continue
                return False  # if all routes don't work
            else:
                if c not in trie.children:
                    return False
                else:
                    trie = trie.children[c]
                    return dfs(trie, i + 1)   # return the dfs boolean!
            
        return dfs(curr, 0)


