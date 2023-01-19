from fastapi import FastAPI
import requests
import bcrypt
import random
import string
import hashlib

app = FastAPI()


# test case for the leaked passwords
@app.get('/check_leak')
def checkLeakedPasswords(password): 
    hash=hashlib.md5(password.encode())
    url="https://api.pwnedpasswords.com/range/{}".format(hash.hexdigest()[:5])
    response=requests.get(url).content
    if response:
        return True
    else:
        return False   


@app.get('/check_length')
def PasswordLength(password):
    min_length = 8
    max_length = 50
    if len(password) > min_length and len(password) < max_length:
        return "ok"
    else:
        return "Characters should be between 8 and 50"

@app.get('/createAccount')
def createAccount(user,password):
    if SpecialCharacters(password) == "ok":
        if not checkLeakedPasswords(password):
            return "Account Created"
        else:
            return "Leaked Password"
    else:
        return "Password doesnot contain special characters"            

@app.get('/check_specialcharacters')
def SpecialCharacters(password):
    passwordLst = ["!","@","$","&"]
    for char in password:
        if char in passwordLst:
            return "ok"
    return "Password must contain at least one special character"

@app.get('/update_policy')
def updatePolicy(policyName,policyValue):
    polices_dct={"minLength":8,"maxLength":50,"specialCharacters":1,"upperCase":1,"lowerCase":1}
    if policyName in polices_dct:
        polices_dct[policyName]=policyValue
        return "Update Success" 
    else:
        return "Policy Not Found" 

@app.get('/generatePassword')           
def generateRandomPassword():
    MAX_LENGTH=50
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabets_lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 
                            'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

    alphabets_upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

    special_characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
                               '~', '>','*', '(', ')', '<']

    all_combined = numbers + alphabets_lowerCase + alphabets_upperCase + special_characters

    # Get Random characters from number, uppercase alphabets, lowercase alphabets, special charcters
    random_numbers = random.choice(numbers)
    random_upper = random.choice(alphabets_upperCase)
    random_lower = random.choice(alphabets_lowerCase)
    random_special_char = random.choice(special_characters)

    temp = random_numbers + random_upper + random_lower + random_special_char

    psswd_lst=[]

    for x in range(MAX_LENGTH - 4):
        temp = temp + random.choice(all_combined)

    psswd_lst.extend(temp)

    #Shuffle psswd_lst to avoid predictable nature of the password
    random.shuffle(psswd_lst)

    return "".join(psswd_lst)



    