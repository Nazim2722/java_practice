def GST(amt,tax=5):
  return (amt*tax*0.01)+amt

def TotalTax(fn,amt,tax=8):
  
  x = (tax*0.01*amt)+amt
  final_amount = fn(x)
  return "amount spend "+str(amt)+" tax 8% total= "+str(x)+" GST 5%==>"+str(final_amount)


TotalTax(fn = GST,amt = 1000)