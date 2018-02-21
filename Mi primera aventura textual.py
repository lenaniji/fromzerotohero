personaje = {"vidas":5, "fuerza":10, "dinero": 10}

def parada ():
    print("Llegais a la parada de autobús pero veis como la carretera está cortada por la gente ardiendo.")
    print("Recibís una llamada de Grumpy explicandoos que el coche está arreglado.")
    print("No tenéis más remedio que volver al coche para llegar a la bolera.")
    roomESP ()

def lootbox ():
    vida = 5
    
    print("¡Una cavalgata se os viene encima!")
    accion = input("atacar o escapar:")
    if accion == "atacar":
        vida = vida - personaje["fuerza"]
        if vida <= 0:
            print("¡le has prendido fuego a la gente!")
            print("¡Has ganado dos monedas!")
            personaje["dinero"] = personaje["dinero"] + 2
            parada()
    if accion == "escapar":
            print("Escapaste")
            room4()
    
    
def room4 ():
    print("No podéis llegar hasta la parada y no hay otro camino. Podéis intentar prenderle fuego a la cavalgata o volver con Kinoli y Grumpy.")
    direc = input("¿opcion 1/opcion 2?")
    if direc == "opcion 1":
        lootbox ()
    elif direc == "opcion 2":
        roomESP() 
        
def roomESP ():
    print("Volveis con Grumpy y Piña, os subis al coche y llegáis a los alrededores de la bolera.")
    print("Entre pitos y flautas, es la hora de cenar y estáis todos cansados.")
    print("Coméis algo y os vais a casa sin jugar a los bolos")
    print("=================================================================================")
    print("FIN DEL JUEGO")
    

def room2 ():
    print("Piña llama a un profesional y os quedáis charlando junto a Grumpy mientras esperáis.")
    print("Tras 30 minutos de espera, llega el POFESIONAL y cambia la rueda.")
    roomESP ()

def room3 ():
    print("Te vas junto a Cuqui y Trash a la parada de bus más cercana, a unos 20 minutos a pie.")
    print("En el barrio se oye música y la gente va disfraza, ya que son las fiestas del barrio.")
    lootbox ()
    
def room1 ():
    print("Tras 30 minutos observando como Grumpy y Piña intentan cambiar la rueda, Cuqui y Trash deciden ir a una parada de autobús cercana y subirse a uno para reunirse con Melocotón y Solaire.")
    print("Grumpy y Piña deciden que la mejor solución es llamar a un profesional para ayudarles.")
    print("¿Te quedas?")
    direc = input("(si/no)")
    if direc == "si":
        room2()    
    elif direc == "no":
        room3()    

def entrada ():
    print("Has llegado al coche y ves que tiene una rueda pinchada")
    print("Estás a tiempo de dar la vuelta e ir en metro.")
    print("¿Sigues queriendo ir en coche?")
    direc = input("(si/no)")
    if direc == "si":
        room1 ()    
    else:
        print("Consigues llegar a los alrededores de la bolera y disfrutas con Melocotón y Solaire de unas croquetas")



print("Los bolos que jamás se tiraron")
print("===============================")
print("")
print("Seis amigos se disponian a ir a jugar a bolos y pasar una agradable tarde.")
print("Al no haber sitio para todos en el coche, Melocotón y Solaire cogieron el metro.")
print("Grumpy, Piña, Cuqui y Trash se dirigen hacia el coche.")
print("¿Les acompañas al coche?")

respuesta = input("(si/no)")

if respuesta == "si":
    entrada()
else:
    print("Consigues llegar a los alrededores de la bolera y disfrutas con Melocotón y Solaire de unas croquetas")

