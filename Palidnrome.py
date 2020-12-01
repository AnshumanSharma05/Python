#Palidnrome
word=input("Enter the word")
word=word.replace(" ","")
word=word.casefold()
new_word=word[::-1]
if(word==new_word):
    print("Yes, the String is a palindrome")
else:
    print("No, the String is not a palindrome")
