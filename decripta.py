from rsa import decrypt

message = eval(input("inserisci il messaggio da decriptare: "))

# Noi andremo a leggere chiave pubblica e privata da codice a barre
# ora lo scriviamo direttamente dentro il codice
private = (3285731,2316427)
public = (962571,2316427)

key = public

messaggio_in_chiaro = decrypt(key, message)
print(messaggio_in_chiaro)
