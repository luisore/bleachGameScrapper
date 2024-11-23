import requests
from bs4 import BeautifulSoup
import random

charactersCreados = []

# Super Classe
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
    
    tipo = ""
    descripcion = ""
        
    def conTipo(self,tipo):
        self.tipo = tipo
        
    def conDescripcion(self,descripcion):
        self.descripcion = descripcion
        
    def __str__(self):
        
        return(f'Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}')
    
    def atacar(self,personajeObjetivo):
        print(f'{self.nombre} ataca a {personajeObjetivo.nombre}')
    

# Classe Figlia
class Shinigami(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre
        
    zanpakuto = ""
    bankai = ""
        
    def conZanpakuto(self,zanpakuto):
        self.zanpakuto = zanpakuto
        
    def conBankai(self,bankai):
        self.bankai = bankai    
        
    def atacar(self,personajeObjetivo):
        
        sn = input('Desea activar Bankai antes de atacar? (s/n): ')
        
        while(True):
            if sn == "s":
                print(f'{self.nombre} activa su Bankai: {self.bankai}')
                print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con el poderoso Bankai {self.bankai}')  
                return 0
            elif sn == "n":
                print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con su zanpakuto {self.zanpakuto}')
                return 0
            else:
                sn = input('Seleccione una opcion correcta (s/n): ')
        
    def __str__(self):
        
        return(f'Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}\nZanpakuto: {self.zanpakuto}\nBankai: {self.bankai}')
        

class Hollow(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre     
    
    tecnicasHollow = []
    
    def conTecnicasHollow(self,tecnicasHollow):
        self.tecnicasHollow = tecnicasHollow
        
    
    def atacar(self,personajeObjetivo):
        print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con el poderoso {random.choice(self.tecnicasHollow)}')  
        
        
    def __str__(self):
        return(f'Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}\nTecnicas Hollow: {self.tecnicasHollow}')
    

class MenosGrande(Hollow):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre
        

class Adjucha(Hollow):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre


class Vasto_Lorde(Hollow):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre


class Arrancar(Hollow):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre


class Visored(Shinigami,Hollow):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre        
        
    def atacar(self,personajeObjetivo):
        
        sn = input('Desea activar Bankai antes de atacar? (s/n): ')
        
        while(True):
            if sn == "s":
                print(f'{self.nombre} activa su Bankai: {self.bankai}')
                print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con el poderoso Bankai {self.bankai}')     
                print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con el poderoso {random.choice(self.tecnicasHollow)}') 
                return 0
            elif sn == "n":
                print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con su zanpakuto {self.zanpakuto}')
                print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con el poderoso {random.choice(self.tecnicasHollow)}') 
                return 0
            else:
                sn = input('Seleccione una opcion correcta (s/n): ')
            
    def __str__(self):
        return(f'Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}\nZanpakuto: {self.zanpakuto}\nBankai: {self.bankai}\ntecnicasHollow: {self.tecnicasHollow}')
        
        
class Quincy(Personaje):    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = nombre        
        
    def conTecnicaQuincy(self,tecnicaQuincy):
        self.tecnicaQuincy = tecnicaQuincy
        
    def atacar(self,personajeObjetivo):
        print(f'{self.nombre} ataca a {personajeObjetivo.nombre} con la tecnica Quincy {self.tecnicaQuincy}')  
        
    def __str__(self): 
        return(f'Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}\nTecnica Quincy: {self.tecnicaQuincy}')        


class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance



class Scrapper(metaclass=Singleton):

    url_base = "https://bleach.fandom.com/es/wiki/"
    url_armas = "https://bleach.fandom.com/es/wiki/Lista_de_Armas"
    url_hollows = "https://bleach.fandom.com/es/wiki/Hollow#Menos"
    url_tecnicas_hollow = 'https://bleach.fandom.com/es/wiki/T%C3%A9cnicas_Hollow'
    url_quincy = "https://bleach.fandom.com/es/wiki/Lista_de_Quincy"

    shiningamis = []    
    hollows = []
    hollowsTecnicas = []
    quincys = []


    def get_all_shiningamis(self):
        respuesta = requests.get(Scrapper.url_armas)
        if respuesta.status_code != 200:
                raise ValueError("No se pudo obtener la información de la página")
        soup = BeautifulSoup(respuesta.text, "html.parser")
    
        h3 = soup.find('span', {'id': 'Zanpaku-t.C5.8D_de_Shinigamis_y_Visored'})
        tabla = h3.find_next('table')
    
        for fila in tabla.find_all('tr')[2:]:
            columnas = fila.find_all('td')
            if len(columnas) >=3:
                nombre = columnas[1].text.strip()
                zanpakuto = columnas[0].text.strip()
                bankai = columnas[2].text.strip()
                Scrapper.shiningamis.append((nombre, zanpakuto, bankai))
            
        return Scrapper.shiningamis
    
    def get_character_description(self,nombreCharacter):
        
        #url del shinigami seleccionado
        url_character = Scrapper.url_base + nombreCharacter.replace(" ","_")
        #print(url_character)

        respuesta = requests.get(url_character)
        if respuesta.status_code != 200:
                raise ValueError("No se pudo obtener la información de la página")
        soup = BeautifulSoup(respuesta.text, "html.parser")

        sumario = soup.find('div', {'id': 'toc'})
        descripcion = sumario.find_previous('p').text.strip("\n")

        #print(descripcion)
        
        return descripcion
            

    def get_shinigami_data(self, numero_shinigami):
        shinigami_seleccionado = Scrapper.shiningamis[numero_shinigami]
        #print(shinigami_seleccionado)
        return shinigami_seleccionado
    
    def print_all_shinigamis_con_armas(self):
        print('Nombre de las armas y sus shinigamis: ')
        for shinigami in Scrapper.shiningamis:
            #numero de shinigamis para menu        
            print(f'{Scrapper.shiningamis.index(shinigami)+1}.{shinigami[0]}')
            print(f'Zanpakuto: {shinigami[1]}')
            print(f'Bankai: {shinigami[2]}')
            print('')
            
            
    def get_all_hollows(self):
        respuesta = requests.get(Scrapper.url_hollows)
        if respuesta.status_code != 200:
                raise ValueError("No se pudo obtener la información de la página")
        soup = BeautifulSoup(respuesta.text, "html.parser")
    
        h3 = soup.find('span', {'id': 'Menos_Grande'})
        Scrapper.hollows.append(h3.text.strip())
        
        h3 = soup.find('span', {'id': 'Adjucha'})
        Scrapper.hollows.append(h3.text.strip())
        
        h3 = soup.find('span', {'id': 'Vasto_Lorde'})
        Scrapper.hollows.append(h3.text.strip())
        
        h3 = soup.find('span', {'id': 'Arrancar'})
        Scrapper.hollows.append(h3.text.strip())
        
        h3 = soup.find('span', {'id': 'Visored'})
        Scrapper.hollows.append(h3.text.strip())
        
        return Scrapper.hollows
        
       
    def get_hollows_description(self,nombreHollow):
        nombreHollowGuionBajo = nombreHollow.replace(" ","_")
        
        #print(nombreHollowGuionBajo)
        #url del shinigami seleccionado
        url_hollow = Scrapper.url_hollows + nombreHollowGuionBajo
        #print(url_shinigami)

        respuesta = requests.get(url_hollow)
        if respuesta.status_code != 200:
                raise ValueError("No se pudo obtener la información de la página")
        soup = BeautifulSoup(respuesta.text, "html.parser")

        sumario = soup.find('span', {'id': nombreHollowGuionBajo})
        #print(sumario)
        descripcion = sumario.find_next('p').find_next('p').text.strip()

        #print(descripcion)
        
        return descripcion
    
    
    def get_all_tecnicasHollow(self):
        if not Scrapper().hollowsTecnicas:
            respuesta = requests.get(Scrapper.url_tecnicas_hollow)
            if respuesta.status_code != 200:
                    raise ValueError("No se pudo obtener la información de la página")
            soup = BeautifulSoup(respuesta.text, "html.parser")
        
            span = soup.find('h2', {'id': 'mw-toc-heading'})
            span = span.find_next('span').find_next('span').find_next('span')
            tecnicaHollow = span.text.strip()
            Scrapper().hollowsTecnicas.append(tecnicaHollow)
            
            while (True):   
                span = span.find_next('span').find_next('span')
                if (span.text.strip() != "" and span.text.strip() != "Navegación"):
                    Scrapper().hollowsTecnicas.append(span.text.strip())
                else:
                    Scrapper().hollowsTecnicas.append('Navegación')
                    return Scrapper.hollowsTecnicas
        else: return Scrapper().hollowsTecnicas

    
    def get_all_quincy(self):
        respuesta = requests.get(Scrapper.url_quincy)
        if respuesta.status_code != 200:
                raise ValueError("No se pudo obtener la información de la página")
        soup = BeautifulSoup(respuesta.text, "html.parser")
    
        span = soup.find('span', {'id': 'Miembros_de_Wandenreich'})
        li = span.find_next('a').find_next('a').text.strip()
        
        Scrapper().quincys.append(li)    
    
        a = soup.find('span',{'id':'Sternritter'}).find_next('a').find_next('a').find_next('a')
        
        
        Scrapper().quincys.append(a.text.strip())
        
        
        while (a.text.strip() != 'Ichigo Kurosaki' ):
            a = a.find_next('a')
            if (a.text.strip() != "" and a.text.strip() != "Jagdarmee" ):
                Scrapper().quincys.append(a.text.strip())
            
        #print(Scrapper().quincys)
        return Scrapper.quincys
    
    
    def print_all_quincy(self):
        print('Nombre de Quincys: ')
        
        #print(Scrapper.quincys)
        for quincy in Scrapper.quincys:
            #numero de shinigamis para menu        
            
            print(f'{Scrapper.quincys.index(quincy)+1}.{quincy}')
            
            
    def get_tecnica_quincy(self, nombreCharacter):
        
        #url del shinigami seleccionado
        url_character = Scrapper.url_base + nombreCharacter.replace(" ","_")
        #print(url_character)
           
        respuesta = requests.get(url_character)
        if respuesta.status_code != 200:
                raise ValueError("No se pudo obtener la información de la página")
        soup = BeautifulSoup(respuesta.text, "html.parser")
        try:
            sumario = soup.find('span', {'id': 'Armas_Espirituales'})
            tecnicaQuincy = sumario.find_next('b').text.strip()            
        except:
            print("no hay tecnica Quincy a aplicar")
            return ""
        else:
            return tecnicaQuincy

    def get_quincy_data(self, numero_quincy):
        quincy_seleccionado = Scrapper.quincys[numero_quincy]
        #print(shinigami_seleccionado)
        return quincy_seleccionado


def mostrar_menu(nombre, opciones):  # incorporamos el parámetro para mostrar el nombre del menú
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida):  # incorporamos el parámetro para mostrar el nombre del menú
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Crear Personaje', crearPersonajeSubMenu),
        '2': ('Ver Personajes Creados', verPersonajesCreados),  # la acción es una llamada a submenu que genera un nuevo menú
        '3': ('Ver detalles de un Personaje', verDetallesDeUnPersonaje),
        '4': ('Activar Habilidad o Atacar', activarHabilidadOAtacar),
        '5': ('Salir', salir)
    }

    generar_menu('Menú principal', opciones, '5')  # indicamos el nombre del menú


def crearPersonajeSubMenu():
    print('Has elegido la opción Crear Personaje: ')
    opciones = {
        '1': ('Shinigami', crearShinigami),
        '2': ('Hollow', crearHollowSubMenu),
        '3': ('Quincy', crearQuincy),
        '4': ('Visored (Shinigami con poderes Hollow)', crearVisored),
        '5': ('Volver al menú principal', salir)
    }

    generar_menu('Personajes', opciones, '5')  # indicamos el nombre del submenú

def crearHollowSubMenu():
    Scrapper().get_all_hollows()
    #print(Scrapper.hollows)

    opciones = {
        '1': (Scrapper.hollows[0], crearMenosGrande),
        '2': (Scrapper.hollows[1], crearAdjucha),
        '3': (Scrapper.hollows[2], crearVastoLorde),
        '4': (Scrapper.hollows[3], crearArrancar),
        '5': (Scrapper.hollows[4] + '(Shinigami con poderes Hollow)', crearVisored),
        '6': ('Volver al menú Personajes', salir)
    }

    generar_menu('Tipo de Hollows', opciones, '6')  

# A partir de aquí creamos las funciones que ejecutan las acciones de los menús


def verPersonajesCreados():
    
    print('Nombre de los Personajes: ')
    for character in charactersCreados:
        #numero de shinigamis para menu        
        print(f'{charactersCreados.index(character)+1}.{character.nombre}')
        print('')
        

def verDetallesDeUnPersonaje():
    verPersonajesCreados()
    numeroPersonaje = int(input('Ingrese el numero de personaje que desea ver: ')) - 1
    
    print(charactersCreados[numeroPersonaje])
    
    
def activarHabilidadOAtacar():
    print('Seleccione el personaje que va a activar la habilidad o atacar:\n')
    verPersonajesCreados()
    numeroPersonaje = int(input('Seleccione el personaje: \n')) - 1
    personaje = charactersCreados[numeroPersonaje]
    print('¿Quien sera el objetivo del ataque?')
    charactersObjetivos = charactersCreados.copy()
    charactersObjetivos.remove(personaje)
    
    for character in charactersObjetivos:
        #numero de shinigamis para menu        
        print(f'{charactersObjetivos.index(character)+1}.{character.nombre}')
        print('')
    numeroPersonajeObjetivo = int(input('Seleccione el Objetivo: \n')) - 1
    personajeObjetivo = charactersObjetivos[numeroPersonajeObjetivo]
        
    personaje.atacar(personajeObjetivo)

def crearShinigami():
    
    m1 = Scrapper()
    m1.get_all_shiningamis()
    m1.print_all_shinigamis_con_armas()
    
    numero_shinigami = int(input('Ingrese el numero de shinigmi que desea crear: ')) - 1
    shinigamiData = Scrapper.get_shinigami_data(Scrapper,numero_shinigami)
    
    #Nombre
    nombre = shinigamiData[0]
    shinigamiCreado = Shinigami(nombre)
    #Tipo
    shinigamiCreado.conTipo("Shinigami")
    #Descripcion
    descripcion = Scrapper.get_character_description(Scrapper,nombre)
    shinigamiCreado.conDescripcion(descripcion)
    #Zanpakuto
    zanpakuto = shinigamiData[1]
    shinigamiCreado.conZanpakuto(zanpakuto)
    #bankai
    bankai = shinigamiData[2]
    shinigamiCreado.conBankai(bankai)
    
    charactersCreados.append(shinigamiCreado)
    print(f'\nEL Shinigami creado es: \n\n{shinigamiCreado}')   


def crearMenosGrande():
    
    nombre = "Menos Grande"
    menosGrandeCreado = MenosGrande(nombre)
    
    menosGrandeCreado.conTipo("Hollow")
    
    descripcion = Scrapper.get_hollows_description(Scrapper,nombre)
    menosGrandeCreado.conDescripcion(descripcion)
    
    tecnicasHollow = Scrapper().get_all_tecnicasHollow()
    menosGrandeCreado.conTecnicasHollow(tecnicasHollow)
    
    charactersCreados.append(menosGrandeCreado)
    print(f'\nEL Menos Grande creado es: \n\n{menosGrandeCreado}')  


def crearAdjucha():
    
    nombre = "Adjucha"
    adjuchaCreada = Adjucha(nombre)
    
    adjuchaCreada.conTipo("Hollow")
    
    descripcion = Scrapper.get_hollows_description(Scrapper,nombre)
    adjuchaCreada.conDescripcion(descripcion)
    
    tecnicasHollow = Scrapper().get_all_tecnicasHollow()
    adjuchaCreada.conTecnicasHollow(tecnicasHollow)
    
    charactersCreados.append(adjuchaCreada)
    print(f'\nEL Adjucha creado es: \n\n{adjuchaCreada}')  


def crearVastoLorde():
    
    nombre = "Vasto Lorde"
    vastoLordeCreada = Vasto_Lorde(nombre)
    
    vastoLordeCreada.conTipo("Hollow")
    
    descripcion = Scrapper.get_hollows_description(Scrapper,nombre)
    vastoLordeCreada.conDescripcion(descripcion)
    
    tecnicasHollow = Scrapper().get_all_tecnicasHollow()
    vastoLordeCreada.conTecnicasHollow(tecnicasHollow)
    
    charactersCreados.append(vastoLordeCreada)
    print(f'\nEL Vasto Lorde creado es: \n\n{vastoLordeCreada}')  


def crearArrancar():
    
    nombre = "Arrancar"
    arrancarCreado = Arrancar(nombre)
    
    arrancarCreado.conTipo("Hollow")
    
    descripcion = Scrapper.get_hollows_description(Scrapper,nombre)
    arrancarCreado.conDescripcion(descripcion)
    
    tecnicasHollow = Scrapper().get_all_tecnicasHollow()
    arrancarCreado.conTecnicasHollow(tecnicasHollow)
    
    charactersCreados.append(arrancarCreado)
    print(f'\nEL Arrancar creado es: \n\n{arrancarCreado}')  


def crearQuincy():
    
    m1 = Scrapper()
    m1.get_all_quincy()
    m1.print_all_quincy()
    
    
    numero_quincy = int(input('Ingrese el numero de quincy que desea crear: ')) - 1
    quincyData = Scrapper.get_quincy_data(Scrapper,numero_quincy)
    
    
    #Nombre
    nombre = quincyData
    quincy_Creado = Quincy(nombre)
    #Tipo
    quincy_Creado.conTipo("Quincy")
    #Descripcion
    descripcion = Scrapper.get_character_description(Scrapper,nombre)
    quincy_Creado.conDescripcion(descripcion)
    
    #Tecnica Quincy
    tecnicaQuincy = Scrapper().get_tecnica_quincy(nombre)
    quincy_Creado.conTecnicaQuincy(tecnicaQuincy)
    
    charactersCreados.append(quincy_Creado)
    print(f'\nEL Quincy creado es: \n\n{quincy_Creado}')   
   
    
def crearVisored():
    
    m1 = Scrapper()
    m1.get_all_shiningamis()
    m1.print_all_shinigamis_con_armas()
    
    numero_shinigami = int(input('Ingrese el numero de shinigmi que desea crear el Hollow: ')) - 1
    shinigamiData = Scrapper.get_shinigami_data(Scrapper,numero_shinigami)
    
    #Nombre
    nombre = shinigamiData[0]
    visoredCreado = Visored(nombre)
    #Tipo
    visoredCreado.conTipo("Visored")
    #Descripcion
    descripcion = Scrapper.get_character_description(Scrapper,nombre)
    visoredCreado.conDescripcion(descripcion)
    #Zanpakuto
    zanpakuto = shinigamiData[1]
    visoredCreado.conZanpakuto(zanpakuto)
    #bankai
    bankai = shinigamiData[2]
    visoredCreado.conBankai(bankai)
    
    tecnicasHollow = Scrapper().get_all_tecnicasHollow()
    visoredCreado.conTecnicasHollow(tecnicasHollow)
    
    charactersCreados.append(visoredCreado)
    print(f'\nEL Visored creado es: \n\n{visoredCreado}')   


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal() # iniciamos el programa mostrando el menú principal