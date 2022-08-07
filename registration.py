name=input("Enter your name : ")
gender=input("Enter your Gender M/F: ")
email=input("Enter your email: ")
password=input("Enter your password: ")
cnpassword=input("Confirm your password: ")
msz=''
if len(name)< 4 or len(name)>25:
    msz+='User name invalid\n'
if '@' not in email:
    msz+='Invaild Email\n'
if password != cnpassword:
    msz+="Password does not match"
if len(msz)>0:
    print("Error\n",msz)
else:
    print("Registration succesful.")


