from euler import eulerien
from copy import deepcopy
def sommet_a_des_voisins(s,g):
    return len(g[s]) != 0

def sommet_avec_voisins(g):
    for sommet in g :
        if sommet_a_des_voisins(sommet,g):
            return sommet
    return None


def cycle(g, x):

    c = [x]
    while sommet_a_des_voisins(x, g):
        y = g[x].pop()
        c.append(y)
        g[y].remove(x)
        x = y
    return c[c.index(x):len(c) - 1]


def cycles_egaux(c1,c2):
    cr = list(reversed(c1))
    if len(c1) != len(c2):
        return False
    for i in range (len(c1)):
        if c1 == c2 or cr == c2 :
            return True
        c1 = [c1[-1]] + c1[:len(c1)-1]
        cr = [cr[-1]] + cr[:len(cr)-1]


def a_des_aretes(g):
    for s in g:
        if len(g[s]) > 0:
            return True
    return False


def euler(graph):
    assert eulerien(graph)
    g = deepcopy(graph)
    c = cycle(g, sommet_avec_voisins(g))
    while a_des_aretes(g):
        for i, s in enumerate(c):
            if sommet_a_des_voisins(s, g):
                c2 = cycle(g, s)
                c = c[:i] + c2 + c[i:]
    print(c)
    return c
