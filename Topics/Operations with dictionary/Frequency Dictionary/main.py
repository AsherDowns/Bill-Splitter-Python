sentence = input()
words = sentence.lower().split()
word_count = {word: words.count(word) for word in words}
for k,v in word_count.items():
    print(k, v)