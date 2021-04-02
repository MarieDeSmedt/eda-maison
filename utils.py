def reg_linear(df,encoding = 0,regression = 0):

   if encoding == 0:
       print("ceci utilise le label encoding")
   else:
       print("ceci utilise le one oht encoding")


   if regression == 0:
       print("ceci utilise la regression de lasso")
   else:
       print("ceci utilise la regression de ridge")

   values = []
   return values