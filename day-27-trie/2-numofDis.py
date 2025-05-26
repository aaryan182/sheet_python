# Number of distinct substrings in a string

# Given a string s, determine the number of distinct substrings (including the empty substring) of the given string.

# A string B is a substring of a string A if B can be obtained by deleting several characters (possibly none) from the start of A and several characters (possibly none) from the end of A. Two strings X and Y are considered different if there is at least one index i such that the character of X at index i is different from the character of Y at index i (X[i] != Y[i]).


# Examples:
# Input : s = "aba"

# Output : 6

# Explanation : The distinct substrings are "a", "ab", "ba", "b", "aba", "".

# Input : s = "abc"

# Output : 7

# Explanation : The distinct substrings are "a", "ab", "abc", "b", "bc", "c", "".

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.count = 0

    def insert_suffixes(self, s):
        for i in range(len(s)):
            node = self.root
            for j in range(i,len(s)):
                ch = s[j]
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                    self.count += 1
                node = node.children[ch]
                
    def count_distinct_substrings(s):
        trie = Trie()
        trie.insert_suffixes(s)
        return trie.count + 1