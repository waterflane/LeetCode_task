def longestPrefix(text: str) -> str:
    res = [0]*len(text)
    j = 0

    for i in range(1, len(text)):
        while j > 0 and text[i] != text[j]: j = res[j-1]
        if text[i] == text[j]: j += 1
        
        res[i] = j
        
    return text[:res[-1]]

print(longestPrefix("level"))
