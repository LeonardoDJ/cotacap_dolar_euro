valor = float(input("Qual valor você deseja converter? "))

def converter(valor):
    dolar = valor * 5.44
    euro = valor * 6.07
    return dolar, euro

dolar, euro = converter(valor)

print("\nO valor do seu dinheiro em dólar: " + str(round(dolar, 2)))
print("O valor em euro: " + str(round(euro, 2)))
