# leetcode 421

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        for num in nums:
            self.insert(root,num)
        
        max_xor = 0

        for num in nums:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit
                if toggled in node.children:
                    curr_xor |= (1 << i) 
                    node = node.children[toggled]
                else:
                    node = node.children[bit] 
            max_xor = max(max_xor, curr_xor)

        return max_xor