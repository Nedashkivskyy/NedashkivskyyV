with open('Probne.txt') as file:
    words=0
    characters=0
    
    for line in file:
        wordslist=line.split()
        words=words+len(wordslist)
        characters += sum(len(word) for word in wordslist)

print(words)
print(characters)

