def countWordsFromFile():
    filename = input("ENTER FILE NAME")
    numberOfSpaces = 0
    file = open(filename,"r")
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("number of words")
    print(numberOfWords)

countWordsFromFile