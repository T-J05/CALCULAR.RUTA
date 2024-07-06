import networkx
import random as rd
import math 


#creamos el grafo
G = networkx.grid_2d_graph(10,10) 

obst = set() # conjunto que recolecta los obstaculos

def heuristica(x,y): #heuristica con distancia manhathan
    
    return abs(x[0]- y[0]) + abs (x[1]-y[1])


def crear_tabla(G):
    filas , columnas = 10,10
    tablero = [["." for _ in range(columnas)]for _ in range(filas)]
    for (i,j) in G.nodes(): #ponemos inicialmente todas las casillas en .
        tablero[i][j]= "."

    print ('0 1 2 3 4 5 6 7 8 9')
    for fila in tablero:
            print(" ".join(fila))

    
    for _ in range (6):
            print("ingrese las coordenadas de x e y para poner obstaculos(max7) ")
            
            ox = int(input("ingrese la coordenada de x para obstaculo: "))

            oy = int(input("ingrese la coordenada de y para obstaculo: "))
           
            
           
            if  ox < 0 or oy < 0 or ox > 10 or oy > 10:
                print ('fuera de los limites') 
            else:
                obst.add((ox,oy)) #anhadimos los obstaculos
                continua = (input('si desea mas obstaculos ingrese si en caso contrario escriba no: '))
                if continua == 'no':
                   break


           
               

    obs= rd.randint(7,15) #nr random de obstaculos que se incluyen
    
    
    for _ in range (obs): #en un rango de los obstaculos elegidos se hace un for
         obx = rd.randint(0,9)
         oby = rd.randint(0,9)
         obstaculos = (obx,oby)
         obst.add(obstaculos)

    print("tablero con obstaculos")

    for nd in obst: #agregamos los obstaculos en el tablero de acuerdo al conjunto obstaculos
        f , c = nd
        tablero[f][c] = "o"
    for filax in tablero:
         print(" ".join(filax))
    

    print("ingrese las coordenadas x e y de tu punto de inicio")

    ix = int(input("ingrese la coordenada x: "))
    iy = int(input("ingrese la coordenada y: "))

    print("ingrese las coordenadas x e y de tu punto de destino")

    dx = int(input("ingrese la coordenada x: "))
    dy = int(input("ingrese la coordenada y: "))

    
    
    
    inicio= (ix,iy) #redefinimos el inicio 
    
    fin = (dx,dy) #redefinimos el fin
    
   
    if fin in obst :

        print ("ERROR tu destino esta en un obstaculo")
        print("ingrese las coordenadas x e y de tu punto de destino")

        dx = int(input("ingrese la coordenada x: "))
        dy = int(input("ingrese la coordenada y: ")) 

    if inicio in obst:
        print ("ERROR tu destino esta en un obstaculo")
        print(" ingrese las coordenadas x e y de tu punto de inicio")
        ix = int(input("ingrese la coordenada x: "))
        iy = int(input("ingrese la coordenada y: "))

    if dx < 0 or dy < 0 or dx > 10 or dy > 10:
            print('fuera de rango')
   
    inicio= (ix,iy) #definimos el inicio 

    fin = (dx,dy) #definimos el fin

    #definimos el peso de las aristas
    for (u,v) in G.edges(): 
        G.edges()[u,v]['peso'] = 1

    for (u,v) in G.edges():
        if u in obst or v in obst:
            G.edges()[u,v]['peso'] = math.inf
    #inicializamos el a star
    ruta = networkx.astar_path(G,inicio,fin,heuristic=heuristica,weight='peso') #inicializacion de a star

    continuar = input("ingrese 'ver' si desea ver la ruta: ")

    if continuar.lower() == 'ver':
            
        for nudo in ruta: #imprimimos la ruta 
            print('\n')
            if nudo in obst: 
                 print('NO HAY CAMINO')
                 tablero[ix][iy] = 'I'
                 tablero[dx][dy] = 'F'
                 for fil in tablero:
                      print(' '.join(fil))
                 break
            
            tablero[nudo[0]][nudo[1]]= 'x'
            tablero[ix][iy] = 'I'
            tablero[dx][dy] = 'F'
            for fil in tablero:
                print(' '.join(fil))

crear_tabla(G)



