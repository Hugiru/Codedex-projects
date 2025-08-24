
colo=float(input("Input amount left in colombian pesos: "))
peru=float(input("Input amount left in peruvian soles: "))
braz=float(input("Input amount left in brazilian reais: "))

colo=colo*0.28
peru=peru*0.29
braz=braz*0.18

bal_usd=(colo+peru+braz)

print("Your balance in USD is: ", bal_usd)
