def check_multiple (number):
    return number % 3 == 0 and number % 5 == 0

def check_password (input_string):
    secret_word = "Python123"
    if input_string = secret_word:
        return "access granted"
    else:
        return "access denied"

def calculate_federal_tax(salary):
    """calculate federal tax based on salary brackets"""
    if salary <= 1100:
        tax_rate = 0.10
        
    elif salary <= 44725:
        tax_rate = 0.12
    elif salary <= 93575:
        tax_rate = 0.22
    elif salary <= 182100:
        tax_rate = 0.24
    else:
        tax_rate = 0.32
    
    return salary * tax_rate







#for password us Python123

