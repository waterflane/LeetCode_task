def removeAnagrams(words: list[str]) -> list[str]:
    def decomposition(word):
        decomposition = {}
        for letter in word:
            if letter not in decomposition: decomposition[letter] = 1
            else: decomposition[letter] += 1
        return decomposition


    i = 1
    while True:
        if i == len(words): break

        if decomposition(words[i]) == decomposition(words[i-1]): words.pop(i)
        else: i+=1
    return words



print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))
