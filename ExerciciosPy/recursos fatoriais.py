def fatorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n*fatorial(n-1) # como podemos ver nesse exemplo
print(fatorial(4))

# pode se usar o while tambem,ou fazer dessa forma.