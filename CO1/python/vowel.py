word=str(input("Enter the word: "))
print("The original string is: ",word)
print("The vowels are: ",end="")
for i in word:
    if i in 'aeiouAEIOU':
        print([i],end="")
