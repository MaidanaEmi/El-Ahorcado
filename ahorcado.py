import random
# Variables generales
words = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

IMÁGENES_AHORCADO = [
'''
  +---+
  |   |

      |

      |

      |

      |

=========''',
'''
  +---+
  |   |
  0
      |

      |

      |

      |

=========
''',
'''
  +---+
  |   |
  0
  |   |

      |

      |

      |

=========
''',
'''
  +---+
  |   |
  0
 /|   |

      |

      |

      |

=========
''',
'''
  +---+
  |   |
  0
 /|\  |

      |

      |

      |

=========
''',
'''
  +---+
  |   |
  0
 /|\  |
 /
      |

      |

      |

=========
''',
'''
  +---+
  |   |
  0
 /|\  |
 / \  |
      |

      |

      |

=========
'''
]

#Inicio juego
def jugar():
    print("¡Inicia el juego!")
    word_list = generateWord(words)
    print("Adivina que palabra es! Tiene: ",len(word_list), "letras.")
    print(word_list)
    juegoTerminado = False
    letraProbadas = []
    correctas = []
    incorrectas = []
    sum_ocurrences = 0
    while juegoTerminado == False :
        l = obtenerIntento(letraProbadas)
        if l in word_list:
            correctas.append(l)
            letraProbadas.append(l)
            sum_ocurrences += word_list.count(l)
            showBoard(correctas,word_list)
        else:
            incorrectas.append(l)
            letraProbadas.append(l)
            showImageAhorcado(incorrectas)
        if len(correctas) == len(word_list) or sum_ocurrences == len(word_list):
            word_str = convertListToStr(word_list)
            print("La palabra es: ",word_str,"Adivinaste!")
            juegoTerminado = True
        elif len(incorrectas)==len(IMÁGENES_AHORCADO)-1:
            print("Se te acabaron las oportunidades. Perdiste!")
            juegoTerminado = True
    else:
        return True
        

# Validar input
def obtenerIntento(letraProbadas):    
    l = input("Prueba con una letra: ")
    l = l.lower()
    if len(l)!=1:
        print("Por favor ingrese una sola letra")
    elif l in letraProbadas:
        print("Ya has probado con esa letra. Elige otra.")
    elif l not in 'abcdefghijklmnñopqrstuvwxyz':
        print("Por favor ingresa una LETRA")
    else:
        return l

# Generar palabra aleatoria
def generateRandom(l):
    rand = random.randrange(0, len(l)-1)
    return rand

def selectWord(l,r):
    w = l[r]
    return w

def convertWordToList(w):
    word_list = [str(i) for i in w]
    return word_list

def generateWord(wl):
    random_number = generateRandom(wl)
    select_word = selectWord(wl,random_number)
    word_list = convertWordToList(select_word)
    return word_list

# Mostrar avance de juego
def showBoard(correct_list,word_list):
    board = []
    for i in word_list:
        if i in correct_list:
            board.append(i)
        else:
            board.append('_')
    print(board)

def showImageAhorcado(incorrect_list):
    print(IMÁGENES_AHORCADO[len(incorrect_list)])

# Funciones utilitarias
def convertListToStr(word_list):
    word_str = ''.join(word_list)
    return word_str

# Bloque principal
# print("¡Inicia el juego!")
# word_list = generateWord(words)
# print("Adivina que palabra es! Tiene: ",len(word_list), "letras.")
# print(word_list)
# juegoTerminado = False
# letraProbadas = []
# correctas = []
# incorrectas = []
# sum_ocurrences = 0
# while juegoTerminado == False :
#     l = obtenerIntento(letraProbadas)
#     if l in word_list:
#         correctas.append(l)
#         letraProbadas.append(l)
#         sum_ocurrences += word_list.count(l)
#         showBoard(correctas)
#     else:
#         incorrectas.append(l)
#         letraProbadas.append(l)
#         showImageAhorcado(incorrectas)
#     if len(correctas) == len(word_list) or sum_ocurrences == len(word_list):
#         print("La palabra es: ",word_list,"Adivinaste!")
#         juegoTerminado = True
#     elif len(incorrectas)==len(IMÁGENES_AHORCADO)-1:
#         print("Se te acabaron las oportunidades. Perdiste!")
#         juegoTerminado = True

juego = jugar()
if juego == True:
    juego_nuevo = input("¡Quieres jugar de nuevo? ")
    if juego_nuevo == 's':
        jugar()
    # else:
    #     break



