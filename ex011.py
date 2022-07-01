alt = float(input('Qual a altura da sua parede? '))
larg = float(input('Digite a largura da sua parede? '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(larg, alt, area))
tinta = area / 2 
print('Para pintar essa parede, você precisara de {}l de tinta.'.format(tinta))