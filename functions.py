from fastapi import FastAPI
import requests
import random
import hashlib

app = FastAPI()


# test case for the leaked passwords
@app.get('/check_leak')
def check_leaked_passwords(password): 
    hash=hashlib.md5(password.encode())
    url="https://api.pwnedpasswords.com/range/{}".format(hash.hexdigest()[:5])
    response=requests.get(url).content
    if response:
        return True
    else:
        return False   


@app.get('/check_length')
def password_length(password):
    min_length = 8
    max_length = 50
    if len(password) > min_length and len(password) < max_length:
        return "ok"
    else:
        return "Characters should be between 8 and 50"

@app.get('/createAccount')
def create_account(user,password):
    if special_characters(password) == "ok":
        if not check_leaked_passwords(password):
            return "Account Created"
        else:
            return "Leaked Password"
    else:
        return "Password doesnot contain special characters"            

@app.get('/check_specialcharacters')
def special_characters(password):
    password_lst = ["!","@","$","&"]
    for char in password:
        if char in password_lst:
            return "ok"
    return "Password must contain at least one special character"

@app.get('/update_policy')
def update_policy(policy_name,policy_value):
    polices_dct={"minLength":8,"maxLength":50,"specialCharacters":1,"upperCase":1,"lowerCase":1}
    if policy_name in polices_dct:
        polices_dct[policy_name]=policy_value
        return "Update Success" 
    else:
        return "Policy Not Found" 

@app.get('/generatePassword')           
def generate_random_password():
    max_length=50
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabets_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 
                            'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

    alphabets_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 
                              'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

    special_characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
                               '~', '>','*', '(', ')', '<']

    all_combined = numbers + alphabets_lowercase + alphabets_uppercase + special_characters

    # Get Random characters from number, uppercase alphabets, lowercase alphabets, special charcters
    random_numbers = random.choice(numbers)
    random_upper = random.choice(alphabets_uppercase)
    random_lower = random.choice(alphabets_lowercase)
    random_special_char = random.choice(special_characters)

    temp = random_numbers + random_upper + random_lower + random_special_char

    psswd_lst=[]

    for char in range(max_length - 4):
        temp = temp + random.choice(all_combined)

    psswd_lst.extend(temp)

    #Shuffle psswd_lst to avoid predictable nature of the password
    random.shuffle(psswd_lst)

    return "".join(psswd_lst)



    