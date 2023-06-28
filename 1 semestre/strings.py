"""frase = "minha terra tem palmeiras onde canta o sabia"
print(frase)
print(type(frase))
for letra in frase:
    print(letra)
"""
frase = "avaliação de estudio R"
"""for letra in "avaliação...":
    print(letra)
print(type(len(frase)))
"""
"""print(frase[2])
print("de" in frase)
print("outra" in frase)"""

"""
f = "True"
print(type(f))
print("T" in f)
if "Onde" in f:
    print("Sim, \'test\', frase existe no texto")
# O '\' é uma ferramenta de scape, ou seja, um epdido para o interpretador ignonar o caracter especial no contexto geral. Ele ainda vai aparecer, mas na leitura do codigo vai ser ignorado
else:
    print("não existe")
    numero = 3
    number = 5
    print("não desista pq a soma é:")
    print(numero + number)

"""

def dividir(textoparadividir):
    return textoparadividir.split()
texto = "vamos dividir o texto"
print(dividir(texto))
print(type(dividir(texto)))
print(dividir(texto)[3])
print(texto[0:7])
print(texto[0:-3])
print(texto[-3:9])
print(texto[-3:-6])