def gemiddelde(sentence):
    words = sentence.split()
    return sum(len(word) for word in words) / len(words)


print(gemiddelde(input('Random zin: ')))
