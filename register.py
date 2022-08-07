name=input("Enter your name : ")
gender=input("Enter your Gender M/F: ")
email=input("Enter your email: ")
password=input("Enter your password: ")
cnpassword=input("Confirm your password: ")

if len(name)>4 and len(name)<25:
    if '@' in email:
        if password == cnpassword:
            print("Registration Successful. ")
        else:
            print("Password does not match with confirm password! ")
    else:
        print("Please Enter Valid Email! ")
else:
    print("Enter Valid username! ")
