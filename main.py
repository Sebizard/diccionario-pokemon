terminos_pokemon = {"pokeball":"objeto que se usa para atrapar pokemon","tipo":"tipo elemental al que pertenese un pokemon y el cual le da sus poderes ejemplo tipo fuego","evolucion":"un pokemon el cual evoluciono y mejoro su poder a la ves que aumenta su  tamaño y cambia de forma y nombre de especie","movimiento":"poder utilizado por un pokemon en batalla ya sea para cubrirse o para atacar"}
busqueda = input("que desea buscar")

if busqueda in terminos_pokemon:
    print(busqueda, terminos_pokemon[busqueda])
else:
    print('Esta palabra no esta en la base de datos')
