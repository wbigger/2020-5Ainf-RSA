from rsa import encrypt
import ast

message = input("inserisci il messaggio da criptare: ")

# Noi andremo a leggere chiave pubblica e privata da codice a barre
# ora lo scriviamo direttamente dentro il codice
# private = (3285731,2316427)
# public = (962571,2316427)

key = ast.literal_eval(input("inserisci la chiave per criptare: "))

# print(key)
# p,q = key
# print(p)
# print(q)
messaggio_criptato = encrypt(key, message)
print(messaggio_criptato)
