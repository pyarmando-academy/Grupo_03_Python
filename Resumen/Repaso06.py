tipo_pizza = ["Vegetariana", "No Vegetarina"]
ingred_vegetarianos = ["Pimiento", "Tofu"]
ingred_no_vegetarianos = ["Peperoni", "Jamon", "Salmón"]


def imprime_tipo_pizza(tipo_pizzas):
    contador = 1
    for pixa in tipo_pizza:
        print(f'\t{contador}.- {pixa}')
        contador += 1


def elige_pizza(tipo_pizza, usuario_elige_pizza):
    if usuario_elige_pizza == 1:
        pizza = tipo_pizza[0]
        print(f'\n\tEl Tipo de pizza seleccionada es {pizza}\n')
    else:
        pizza = tipo_pizza[1]
        print(f'\n\tEl Tipo de pizza seleccionada es {pizza}\n')
    return pizza


def seleccione_ingredientes(pizza):
    print(f'\t** Todas Nuestras pizzas incluyen Mozarella y Salsa Pomodoro')
    if pizza == "Vegetariana":
        print("\n\tElije un Ingrediente para completar tu pedido")
        contador = 1
        for i in ingred_vegetarianos:
            print(f'\t{contador} - {i}')
            contador += 1
        usuario_eliege_ingrediente = int(input("\n\tElige un Ingrediente (1/2)"))
        ingrediente = ingred_vegetarianos[usuario_eliege_ingrediente - 1]
        print(f'\n\t El Ingrediente seleccionado es {ingrediente}\n')

    else:

        print("\n\tElije un Ingrediente para completar tu pedido")
        contador = 1
        for i in ingred_no_vegetarianos:
            print(f'\t{contador} - {i}')
            contador += 1
        usuario_eliege_ingrediente = int(input("\n\tElige un Ingrediente (1/2/3)"))
        ingrediente = ingred_no_vegetarianos[usuario_eliege_ingrediente - 1]
        print(f'\n\t El Ingrediente seleccionado es {ingrediente}\n')
    return ingrediente


def orden(ingrediente, pizza):
    print(f'\tTu Orden es la siguiente \n\t >> Pizza {pizza} con {ingrediente}')


imprime_tipo_pizza(tipo_pizza)  # todo Ver los tipos de Pizza que Hay
usuario_elige_pizza = int(input("\n\t¿Que tipo de pizza desea (1/2)?:"))
pizza = elige_pizza(tipo_pizza, usuario_elige_pizza)
ingrediente = seleccione_ingredientes(pizza)
orden(ingrediente, pizza)

# elige_pizza(tipo_pizza,1)
# imprime_tipo_pizza('Vegetariana')
