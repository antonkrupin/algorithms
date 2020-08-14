words = []
wordsBigger = []
def BiggerGreater(word):
    listWord = list(word)
    
    for x in range(len(listWord)):
        for y in range(len(listWord)):
            wordCopy = listWord.copy()
            changedWord = ''
            if(x != y):
                changedWord += listWord[x] + listWord[y]
                wordCopy[x] = ''
                wordCopy[y] = ''
                for m in range(len(wordCopy)):
                    if(wordCopy[m] != ''):
                        changedWord += wordCopy[m]
                words.append(changedWord)
                
    for x in range(len(listWord)):
        for y in range(len(listWord)):
            wordCopy = listWord.copy()
            changedWord = ''
            if(x != y):
                if(word[x] < word[y]):
                    test = ''
                    changedWord += word[y] + word[x]
                    wordCopy[x] = ''
                    wordCopy[y] = ''
                    for m in range(len(wordCopy)):
                        if(wordCopy[m] != ''):
                            test += wordCopy[m]
                    words.append(test + changedWord)

    for x in range(len(words)):
        if(words[x] > word):
            wordsBigger.append(words[x])
    
    if(wordsBigger == []):
        test = ''
        return test
    else:
        for x in range(len(wordsBigger)):
            smallWord = wordsBigger[x]
            for i in range(len(wordsBigger)):
                if(x != i):
                    if(smallWord > wordsBigger[i]):
                        smallWord = wordsBigger[i]
                    
        return smallWord
