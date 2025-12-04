class Trie:
    def __init__(self, words: list[str] = [], now: str='*'):
        self.now = now
        self.next_lists: list[Trie] = []
        self.word = ''
        self.next_words = []

        if words != []: self._create_trie(words)

    def _create_trie(self, words):
        for word in words:
            now = self
            for i in word:
                def search_in_next():
                    for nt in now.next_lists:
                        if nt.now == i: return nt
                    return False
                
                now.next_words.append(word)
                s = search_in_next()
                if s: 
                    s
                    now = s
                else: 
                    new = Trie(now=i)
                    now.next_lists.append(new)
                    now = new
            now.word = word
    
    def get_next_chars(self):
        res = []
        for i in range(len(self.next_lists)):
            res.append(self.next_lists[i].now)
        return res
    
    def get_to_target_word(self, word):
        for i in self.next_lists:
            if word in i.next_words:
                return i
        return 0

    def get_next(self, char):
        for i in range(len(self.next_lists)):
            if self.next_lists[i].now == char: return self.next_lists[i]

    def del_word_from_memory(self, word):
        now = self
        while 1:
            if now == 0: return True
            now.next_words.remove(word)

            now = now.get_to_target_word(word)
        

def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    words_trie = Trie(words)

    occurrences = [i.now for i in words_trie.next_lists]
    stack = []

    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] in occurrences:
                stack.append([y,x, [[y, x]],words_trie.get_next(board[y][x])])

    res = []

    while stack:
        y,x,visited,now = stack.pop()

        if now.word != '' and now.word not in res: 
            res.append(now.word)
            words_trie.del_word_from_memory(now.word)
        if now.next_words == []: continue


        for i in [[-1,0],[1,0], [0,-1], [0,1]]:
            new_y, new_x = y+i[0], x+i[1]
            if (new_y < len(board) and new_y >= 0) and (new_x < len(board[0]) and new_x >= 0) and [new_y, new_x] not in visited:
                nexts = now.get_next_chars()
                if board[new_y][new_x] in nexts:
                    new_viseted = visited.copy()
                    new_viseted.append([new_y, new_x])
                    stack.append([new_y,new_x, new_viseted, now.get_next(board[new_y][new_x])])
    return res

print(findWords([["o","a","a","n"],
                 ["e","t","a","e"],
                 ["i","h","k","r"],
                 ["i","f","l","v"]], 

                 ["oath","pea","eat","rain", "oat"]))
