import random
import string


CHAR_MAP = { 
    'uppercase': string.ascii_uppercase,
    'lowercase': string.ascii_lowercase,
    'numbers': string.digits,   #this is a hashmap
    'special_characters': string.punctuation,
} 


def generate_0(length):
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(chars) #generates and puts it in "password"



def generate_1(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    password = []
    chars = ''

    if uppercase:
        chars += string.ascii_uppercase
        password += random.choice(string.ascii_uppercase) #handles the generation of uppercase

    if lowercase:
        chars += string.ascii_lowercase
        password += random.choice(string.ascii_lowercase) #handles the generation of lowercase

    if numbers:
        chars += string.digits
        password += random.choice(string.digits) #handles the generation of nums
    
    if special_characters:
        chars += string.punctuation
        password += random.choice(string.punctuation) #handles the generation of special chars.

    for _ in range(length - len(password)):
        password += random.choice(chars)
    
    random.shuffle(password) #it shuffles everything
    password = ''.join(password) #if you put stuff inbetween '' it will put it inbetween text 

    print(password)


    #"length" is an example of an arguement | kwargs are the arguements with an equal sign
def generate_2(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    password = []
    chars = ''

    for key, value in CHAR_MAP.items():
        if locals()[key]: #key is one of the char_map | dont use "locals() = bad practice"
            chars += value
            password += random.choice(value)

    for _ in range(length - len(password)):
        password += random.choice(chars)
    
    random.shuffle(password)
    password = ''.join(password) 
    
    print(password)



def generate(length, **kwargs): #putting "pass" means don't do anything | **kwargs upacks things, also means keyword arguements | *args means arguements
    password = []
    chars = ''

    if not any(kwargs.values()):
        return 'Please provide password requirement' #error handling

    for item in kwargs:
        if kwargs[item] and CHAR_MAP.get(item):
            chars += CHAR_MAP[item]
            password += random.choice(CHAR_MAP[item]) #doing the 1st "if" statements above

    for _ in range(length - len(password)):
        password += random.choice(chars)
    
    random.shuffle(password)
    return ''.join(password) 
    

if __name__ == '__main__':
    print(generate(25, uppercase=True, lowercase=True, numbers=True, special_characters=True))
