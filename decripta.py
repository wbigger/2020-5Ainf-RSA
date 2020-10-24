from rsa import decrypt
import ast


message = ast.literal_eval(input("inserisci il messaggio da decriptare: "))

key = ast.literal_eval(input("inserisci la chiave per decriptare: "))

messaggio_in_chiaro = decrypt(key, message)
print(messaggio_in_chiaro)
