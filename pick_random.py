import random

names = [
    'Alejandra Blanco',
    'Erika Garcia',
    'Francisco Orozco',
    'Luz Carillo',
    'Nery Diaz',
    'Sandra Gutierrez',
    'Valentin Alcaraz'
]

tabs = [
    'Vuelos Sencillo',
    'Vuelos Redondo',
    'Vuelos Varios Destinos',
    'Renta de autos',
    'Traslado Aeropuerto',
    'Paquetes',
    'Actividades',
]

while len(names) and len(tabs):
    name = random.choice(names)
    tab = random.choice(tabs)
    print(f'{name}: {tab}')
    names.remove(name)
    tabs.remove(tab)

