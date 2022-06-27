contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
sub = lambda a, b: a - b

print(soma(5, 10))
print(sub(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}
print(type(calculadora))
soma = calculadora['soma']
#soma = lambda a, b: a + b,
mult = calculadora['mult']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicacao é: {}'.format(mult(10,2)))
