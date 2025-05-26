# Longest word with all prefixes

# Given a string array nums of length n. A string is called a complete string if every prefix of this string is also present in the array nums. Find the longest complete string in the array nums.

# If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None" (without quotes).


# Examples:
# Input : nums = [ "n", "ni", "nin", "ninj" , "ninja" , "nil" ]

# Output : ninja

# Explanation : The word "ninja" is the longest word which has all its prefixes present in the array.

# Input : nums = [ "ninja" , "night" , "nil" ]

# Output : None

# Explanation : There is no string that has all its prefix present in array. So we return None.

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def check_all_prefixes_exist(self,word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node or not node.is_end:
                return False
        return True

    def longest_complete_string(nums):
        trie = Trie()
        for word in nums:
            trie.insert(word)
            
        best = ""
        for word in nums:
            if trie.check_all_prefixes_exist(word):
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best if best else "None"