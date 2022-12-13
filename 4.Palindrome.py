word=input("Enter a String:")
l=len(word)-1
count=0
for i in range(l):
    if(word[i]!=word[l-i]):
        break
    count=1
if(count==1):
    print("Palindrome")
else:
    print("Not Palindrome")
