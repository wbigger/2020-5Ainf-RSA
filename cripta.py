from rsa import encrypt

message = input("inserisci il messaggio da criptare: ")


key = eval(input("inserisci la chiave per criptare: "))

messaggio_criptato = encrypt(key, message)
print(messaggio_criptato)
