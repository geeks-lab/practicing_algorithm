import re

doc = input()
searching_word = re.compile(input())
print(len(searching_word.findall(doc)))