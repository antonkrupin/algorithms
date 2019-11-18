def squirrel(x):
  diamonds = 0
  if x == 0:
        return 1
  else:
    def fact(x):
      if(x == 1):
        return 1
      else:
        return x * fact(x-1)
    diamonds = str(fact(x))[0]
    return(int(diamonds))
  
