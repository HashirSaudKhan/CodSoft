import random
import string as str
print("\nWELCOME TO THE PASSWORD GENERATOR :) ")
x = 0
s = input("If you want to generate password enter 'y' or want to quit enter 'q' :")
while ( x >=  0 ):
    
    if (s == "y" or s == "Y"):
        Password_lenght = int(input("\nEnter the lenght:"))
        lower_letters = str.ascii_lowercase
        upper_letters = str.ascii_uppercase
        numbers = str.digits
        symbols = str.punctuation
        All = lower_letters + upper_letters + numbers + symbols

        temporary = random.sample(All, Password_lenght)
        password = "".join(temporary)
        print("Your Password is : " + password)
        t = input("\nGenerate password again enter 'y' or want to quit enter 'q' :")
        if (t == "q" or t == "Q"):
          print("you quit ;)")
          break
        else:
            x = x + 1

    elif (s == "q" or s == "Q"):
        print("you quit ;)")
        break
