from personaje import Personaje #mal escrito personaje
import random #mal escrito random

print("¡Bienvenido a Gran Fantasía!") #gran realidad 
nombre = input(
    "Por favor indique el nombre de su personaje:\n" #nombre del personaje 
)

p = Personaje(nombre)
print(p.estado)

print(
    "\n¡Oh no!, ¡Ha aparecido un Orco!" #orco
)

o = Personaje("Orco")
probabilidad_ganar = Personaje.get_probabilidad_ganar(
    p, o
) #falta valor o en el par de datos al llamar metodo get_probabilidad_ganar

opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

while opcion_orco == 1:
    resultado = (
        "Gana" if random.uniform(0, 1) > probabilidad_ganar else "Pierde" #falta comilla y completar palabras
    )

    if resultado == "Gana":
        print(
            "\n¡Le has ganado al orco, felicidades!\n"
            "¡Recibirás 50 puntos de experiencia!\n"
        )
        p.estado = 50 #valores cambiados
        o.estado = -30
        

    elif resultado == "Pierde":
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n"
            "¡Has perdido 30 puntos de experiencia!\n"
        )
        p.estado = -30
        o.estado =50

    print(p.estado)
    print(o.estado) #primt
    
    probabilidad_ganar = p.get_probabilidad_ganar(p) #reemplazo el 0 por p
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar) #provabilidad

else:
    print("\n El orco ha quedado atrás.")
    
   
