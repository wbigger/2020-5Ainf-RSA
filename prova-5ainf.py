from rsa import encrypt,decrypt

if __name__ == '__main__':
    message = "yo"
    print message
    private = (3285731, 2316427)
    public = (962571, 2316427)
    encrypted_msg = encrypt(private, message)
    print encrypted_msg
    print decrypt(public, encrypted_msg)
