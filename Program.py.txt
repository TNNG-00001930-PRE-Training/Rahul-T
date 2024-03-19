#Given a string. The task is to print all words
#with even length in the given string.
word=input("your word is :")
for i in range(len(word)):
    print(i)
    if (i+1)%2==0:
        print(word[i])