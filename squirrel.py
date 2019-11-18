def squirrel(x):
  diamonds = 0
  def fact(x):
    if(x == 1):
      return 1
    else:
      return x * fact(x-1)
  
  diamonds = str(fact(x))[0]
  return(diamonds)
