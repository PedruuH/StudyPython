a=float(input("Qual a velocidade do carro? "))
if a<=80:
    print ("Muito bem")
else:
    a=(a-80)*5
    print ("Multa de: R${val:.2f}" .format(val=a))
    
