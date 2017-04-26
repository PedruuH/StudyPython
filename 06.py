a=float(input("Qual distancia deseja percorrer: "))
if a<=200:
    print("Preço a pagar: R${val:.2f}" .format(val=(a*0.50)))
else:
    print("Preço a pagar: R${val:.2f}" .format(val=(a*0.45)))
