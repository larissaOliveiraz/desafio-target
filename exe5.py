# 5-)

palavra = str(input("Digite uma palavra: "))
letras = []

for i in palavra:
    letras = [i] + letras

print (''.join(letras))