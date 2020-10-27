from cryptography.fernet import Fernet

def authenticate_user(environ):
    cipher_term_cd = environ['HTTP_TOKEN']
    byte_cipher_term_cd = cipher_term_cd.encode()
    secret_key = b'G5mX1vlxKVaQkdg3CfhH6pVQIctECVw3MN6uCXbJpGo='
    f = Fernet(secret_key)
    encoded_term_cd = f.decrypt(byte_cipher_term_cd)
    term_cd = encoded_term_cd.decode()
    print(term_cd)
    if term_cd == '12345':
        username = term_cd
        print('User identified and shall be named', username)
        return username
    else:
        print('User anauthorized and shall be casted out ')
        return None
