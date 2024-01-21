#password generator
# Requirements 
'''  Create a Python script that generates random passwords.
 Ensure the passwords are a mix of uppercase and lowercase letters, numbers, and special characters.
 Allow users to specify the length and number of passwords to generate.
'''
import random
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2="abcdefghijklmnopqrstuvwxyz"
s3="0123456789"
s4="~!@#$%^&*()_+-=`[];{}./,:?><"
print("At least one letter should be Upper case, one should be Lower case, one should be Number, one should be Special character")
print('Minimum length should be 4 and non -ve')
length=int(input("Enter the length"))
number=int(input("Enter the number of password you want to generate"))
def printing():
    s=''
    for j in range(number):
        for i in range(length):
            if(i%4==0):
                rand=random.choice(s1)
            elif(i%4==1):
                rand=random.choice(s2)
            elif(i%4==2):
                rand=random.choice(s3)
            elif(i%4==3):
                rand=random.choice(s4)   
            s=s+rand
        print(s)
        s=''
printing()
