import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)

#Generate more characters here
#....
lowercaseLetter3=chr(random.randint(97,122))
lowercaseLetter4=chr(random.randint(97,122))
lowercaseLetter5=chr(random.randint(97,122))
randomcharacter6=chr(random.randint(33,38))
randomcharacter7=chr(random.randint(33,38))
lowercaseLetter8=chr(random.randint(97,122))
lowercaseLetter9=chr(random.randint(97,122))
lowercaseLetter10=chr(random.randint(97,122))
randomcharacter11=chr(random.randint(33,38))
randomcharacter12=chr(random.randint(33,38))
#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + randomcharacter6 + randomcharacter7 + lowercaseLetter8 + lowercaseLetter9 + lowercaseLetter10 + randomcharacter11 + randomcharacter12 # + ....
password = shuffle(password)

#Ouput
print(password)