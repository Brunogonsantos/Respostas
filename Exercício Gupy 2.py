a = 0
fib = 1
valor = int(input("Digite um valor maior que 0, para saber se ele pertence ou não a sequência de Fibonacci "))
while (fib <= valor):
  a += fib
  fib += a
  if(a == valor) or (fib == valor):
    print("Pertence")
    break
  elif (a > valor) or (fib > valor):
    print("Não Pertence")