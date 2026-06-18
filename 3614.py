from collections import deque

class Solution:
    def processStr(self, s: str, k: int) -> str:
        tot_lenght = 0
        for char in s:
            if char == "#": tot_lenght *=2
            if char.isalpha(): tot_lenght+=1
            if char == '*': tot_lenght -=1

            if tot_lenght < 0: tot_lenght = 0

        if tot_lenght-1 < k: return '.'

        for i in range(len(s)-1, -1, -1):
            char = s[i]

            if char == "#":
                if k > (tot_lenght//2)-1: k-=tot_lenght//2
                tot_lenght = tot_lenght//2
            elif char.isalpha(): 
                if k == tot_lenght-1: return char
                tot_lenght-=1
            elif char == '%':
                k = tot_lenght-1-k
            elif char == '*':
                tot_lenght+=1

            


a = Solution()
print(a.processStr("a#b%*", 1))
print(a.processStr("cd%#*#", 3))
print(a.processStr("%#*gm#xib", 2))
