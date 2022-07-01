real = float(input('Quanto você tem na carteira? '))
dolar = real / 5.33
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))