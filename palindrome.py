
def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def is_prime(number: int) -> bool:
    result_list = [x for x in range(2,number) if number % x ==0]
    return len(result_list) == 0

def run():
    print('Es un palindromo:',is_palindrome(321)) #Error has incompatible type "int"; expected "str"
    print('Es un palindromo:',is_palindrome('ana')) #True
    print('2 Es un numero primo :',is_prime(2)) # True
    print('14 Es un numero primo :',is_prime(14)) # False

if __name__ == '__main__':
    run()
