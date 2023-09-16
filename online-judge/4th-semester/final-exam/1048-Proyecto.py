"""
dd/mm/aaaa
12/06/2021

Autor: Jhoan Manuel Buitrago Chávez
Código Estudiantil: 8953846

Código de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.

Problema 1048 Low Cost Air Travel
https://onlinejudge.org/external/10/1048.pdf

Video explicativo:
https://youtu.be/p7s18gH2dBg
"""


from heapq import heappush, heappop
from sys import stdin



class State:
    """
    Clase que representa los estados del problema

    Atributos:
        cost : int
            Costo total del recorrido en este estado

        ticket : int 
            Tiquete que se está usando en el estado actual

        iTicket : int
            Indice de la ciudad del tiquete que se esta usando en el estado.

        iQuery : int 
            Indice del Query que corresponde a la ciudad que estoy tratando de
            visitar.

        used : list 
            Lista de tiquetes usados en el recorrido del estado.
        
    Métodos:
        __lt__ : bool
            Definir la comparación "menor que" entre estados, dicha comparación
            esta dada por el menor costo. Si los costos son iguales entonces se busca
            el menor iQuery
        
        __str__ : str
            Definir la forma de imprimir los estados. Solo tiene utilidad de debug.
    """
    def __init__(self, cost = 0, ticket = 0, iTicket = 0, iQuery = 0, used = []):
        self.cost = cost
        self.iTicket = iTicket
        self.ticket = ticket
        self.iQuery = iQuery
        self.used = used
    
    def __lt__(self, other):
        if self.cost == other.cost:
            return self.iQuery > other.iQuery
        return self.cost < other.cost
    
    def __str__(self):
        return f"({self.cost}, {self.ticket}, {self.iTicket}, {self.iQuery}, {self.used})"



def solve(ticketList : list, query : list):
    """
    Función encargada de resolver el problema. Consiste en un Dijkstra por estados
    que usa un heap como cola de prioridad para organizar los estados que tienen que ser
    procesados. Debido a que en el problema se específica que debe haber una solución
    el algoritmo no se detiene hasta encontrarlo.

    Se usa un set de visitados que guarda una tupla de 3 valores:
        ticket: indice del tiquete en la matriz ticketList
        city_index: indice de la ciudad en el tiquete
        query_index: siguiente posición del query que necesita ser visitado.

    Este set de visitados permite no procesar un estado similar dos veces.

    Argumentos:
        ticketList : list
            Lista donde cada elemento es una lista que contiene la información de un tiquete,
            el indice del elemento es el incide del tiquete.
        
        query : list
            Lista que contiene las ciudades a visitar en orden.

    Retorna
        ans : State
            Estado final donde ya se recorrieron todas las ciudades, este estado contiene
            toda la información necesaria para dar el output del problema.
    """
    pQueue = []
    start = query[0]

    #set de los estados ya recorridos.
    visited = set()

    # Buscar tickets en los que pueda empezar desde la primera ciudad del query
    for i in range(len(ticketList)):
        if ticketList[i][1] == start:
            heappush(pQueue, State(ticketList[i][0], i, 1, 1, [i + 1]))
            visited.add((i, 1, 1))
    
    found = False
    ans = State()

    while not found:
        state : State = heappop(pQueue)
        currTicket = state.ticket
        
        # si el index del query es igual al tamaño del query se encontró la solución
        if state.iQuery == len(query):
            found = True
            ans = state

        else:
            # Si quedan vuelos que usar en el ticket actual
            if state.iTicket + 1 < len(ticketList[currTicket]):
                state.iTicket += 1
                
                # Si el siguiente vuelo me lleva a la ciudad que necesito
                if ticketList[state.ticket][state.iTicket] == query[state.iQuery]:
                    state.iQuery += 1

                # Revisar que este nuevo estado no haya sido recorrido antes
                # Si ya fue recorrido es que existe un camino hasta este estado con menor costo
                if (state.ticket, state.iTicket, state.iQuery) not in visited:
                    visited.add((state.ticket, state.iTicket, state.iQuery))
                    heappush(pQueue, state)
                
                    currCity = ticketList[currTicket][state.iTicket]
                    # Revisar los demás tickets a ver si puedo cambiar desde la ciudad en la que estoy
                    for i in range(len(ticketList)):
                        if ticketList[i][1] == currCity:
                            # Creo un nuevo estado aumentando el costo total y añado el ticket al orden
                            used = list(state.used)
                            used.append(i + 1)
                            newState = State(state.cost + ticketList[i][0], i, 1, state.iQuery, used)
                            heappush(pQueue, newState)

    return ans

"""
Procedimiento encargado de recibir el input y dar la salida del problema
"""
def main():
    cases = 1
    tickets = int(stdin.readline())
    while tickets != 0:
        ticketList = []
        for i in range(tickets):
            cost, number, *cities = map(int, stdin.readline().split())
            ticketList.append([cost, *cities])
        
        trips = int(stdin.readline())
        for i in range(trips):
            query = list(map(int, stdin.readline().split()))[1:]
            ans = solve(ticketList, query)
            print(f"Case {cases}, Trip {i + 1}: Cost = {ans.cost}")
            print("  Tickets used:", *ans.used)

        cases += 1
        tickets = int(stdin.readline())

main()
