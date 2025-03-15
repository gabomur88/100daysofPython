diccionario_normal = ["a","b","c","d","ch","e","f","g","h","i","j","k","l","m","n","ñ", \
                      "o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
diccionario_morse = [".-", "-...","-.-.","----","-..",".","..-.","--.","....","..",".---","-.-",".-..",
                     "--","-.","--.--","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
                     "-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..",
                     "----."]
print(diccionario_normal)

print(diccionario_morse)

print(len(diccionario_normal))
print(len(diccionario_morse))

palabra_normal = input("Que Palabra quieres traducir a morse?\n").lower()
print(f"La Palabra a Traducir es {palabra_normal}")

palabra_normal_dividida = list(palabra_normal)

print(f"la palabra dividida es {palabra_normal_dividida}")

palabra_morse_final=[]
for n in palabra_normal_dividida:
    if n in diccionario_normal:

        indice = diccionario_normal.index(n)
        morse = diccionario_morse[indice]
        palabra_morse_final.append(morse)
palabra_sacramentada_morse = ' '.join(palabra_morse_final)
print(f"La Palabra Final en Morse es: {palabra_sacramentada_morse}")

