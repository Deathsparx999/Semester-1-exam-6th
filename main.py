#Q1
##
a=int(input("please enter 1st number: "))
b=int(input("now the second: "))
c=int(input("the third one please: "))
d=int(input("fourth: "))
e=int(input("and your final number: "))
numList=[a,b,c,d,e]
print(numList)
numList.sort
print(numList)
###########################################
namList=[]
petList=[]
name=input("please insert your name: ")
pets=int(input("how many pets do you have?: "))
namList.append(name)
petList.append(pets)
#####################################################
#Q3
def isAnagram(w1, w2):
  if sorted(w1) == sorted(w2):
    print(w1,"Is an anagram of",w2) 
    return True
  else:
    print(w1,"Is not an anagram of",w2)
    return False
    
word1=input("enter first word: ")
word2=input("enter second word: ")


word1=word1.lower()
word2=word2.lower()


word1=word1.replace(" ","")
word2=word2.replace(" ","")


if(sorted(word1) == sorted(word2)):
  print(word1,"Is an anagram of",word2) 
else:
  print(word1,"Is not an anagram of",word2)

isAnagram(word1,word2)

phrase=input("please enter a phrase: ")
phrase=phrase.lower()
phrase=phrase.replace(" ","")
isAnagram(word1,phrase)
isAnagram(word2,phrase)