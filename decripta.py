from rsa import decrypt
# import ast


message = eval(input("inserisci il messaggio da decriptare: "))

key = eval(input("inserisci la chiave per decriptare: "))

messaggio_in_chiaro = decrypt(key, message)
print(messaggio_in_chiaro)
