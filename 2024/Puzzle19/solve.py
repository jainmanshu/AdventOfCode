with open('input_1.txt') as f:
    lines = f.read().split('\n\n')

towels = lines[0].split(', ')
patterns = lines[1].split('\n')

# Thinking about solving throught trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
    
    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]
        return True
    
def part1():
    trie = Trie()

    for towel in towels:
        trie.insert(towel)
        
    def dfs(pattern, start, memo):
        if start == len(pattern):  # Successfully matched the entire pattern
            return True
        if start in memo:  # Check if result for this start index is already computed
            return memo[start]
        
        for end in range(start + 1, len(pattern) + 1):
            if trie.search(pattern[start:end]):  # If substring matches a towel
                if dfs(pattern, end, memo):  # Recur for the remaining pattern
                    memo[start] = True
                    return True
        
        memo[start] = False  # Store the result for this start index
        return False
    
    count = 0
    for pattern in patterns:
        memo = {}  # Memoization dictionary for each pattern
        if dfs(pattern, 0, memo):  # Start matching from the beginning of the pattern
            count += 1
    
    return count

print("Part 1:", part1())        
        


