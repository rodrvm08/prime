x = int(input("Digite o numero: "))
mult = 0
for count in range(2,x):
  if x % count == 0:
    mult = mult + 1
if mult == 0:
  print("É primo")
else:
  print("Não é primo")


j = int(input("digite o número: "))
kino = 1
seto = 0
while kino == 1:
  kino = kino + 1
  if j % kino == 0:
    seto = seto +1
if seto == 0:
  print("É primo")
else:
  print("Não é primo")