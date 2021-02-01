import string

f = open('tmp/text.txt', 'r')

text = f.read()

f.close()

text = text.lower()

print (text)

print(string.punctuation)

spec_chars = string.punctuation + '\n\xa0«»\t—…'

text = "".join([ch for ch in text if ch not in spec_chars])

print (text)


