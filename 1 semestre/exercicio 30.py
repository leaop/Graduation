import re


txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque convallis dolor vel bibendum dictum. Curabitur a egestas enim. Nullam porta dictum turpis et congue. Integer non arcu nec dolor imperdiet gravida. Donec quis justo ac est aliquam sollicitudin a at ligula. Mauris consequat felis quis maximus condimentum. Cras posuere ligula."

# Verifica se a string começa com Sabe
x = re.findall("virgula$", txt)
if x:
  print("Sim, termina com 'ligula'")
else:
  print("Não tem com 'virgula'")