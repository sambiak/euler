from cycle import sommet_a_des_voisins
from cycle import sommet_avec_voisins
from cycle import cycle
from cycle import cycles_egaux
from cycle import euler
from cycle import a_des_aretes

def creer_graph1():
    g = dict()
    g["a"] = set()
    g["a"].add("b")
    g["a"].add("c")
    g["b"] = set()
    g["b"].add("a")
    g["b"].add("c")
    g["c"] = set()
    g["c"].add("a")
    g["c"].add("b")
    g["d"] = set()
    return g

def creer_graph2():
    g = dict()
    g["a"] = set()
    return g


def test_sommet_a_des_voisin():
    g = creer_graph1()
    assert sommet_a_des_voisins("a",g)


def test_sommet_a_des_voisins_False():
    g = creer_graph1()
    assert not sommet_a_des_voisins("d", g)


def test_sommet_avec_voisins():
    g = creer_graph2()
    assert sommet_avec_voisins(g) == None


def test_sommet_avec_voisins2():
    g = creer_graph1()
    assert sommet_avec_voisins(g) != None


def test_cycles_egaux():
    c1 = [1, 2, 3, 4]
    c2 = [3, 4, 1, 2]
    assert cycles_egaux(c1,c2)


def test_cycles_egaux2():
    c1 = [1, 2, 3, 4]
    c2 = [3, 2, 1, 4]
    assert cycles_egaux(c1, c2)


def test_cycles_egaux_false():
    c1 = [1, 2, 3, 4]
    c2 = [3, 1, 2, 4]
    assert not cycles_egaux(c1, c2)


def test_cycles():
    g = {1: {2, 4}, 2: {1, 3}, 3: {2, 4}, 4: {1, 3}}
    assert cycles_egaux(cycle(g, sommet_avec_voisins(g)), [1, 2, 3, 4])


def test_cycles2():
    g  = {1: {2, 3}, 2: {1, 3}, 3: {1, 2, 4, 5}, 4: {3, 5}, 5: {3, 4}}
    assert cycles_egaux(cycle(g, sommet_avec_voisins(g)), [1, 2, 3]) or cycles_egaux(cycle(g, sommet_avec_voisins(g)), [3, 4, 5]) or cycles_egaux(cycle(g, sommet_avec_voisins(g)), [1, 2, 3, 4, 5])


def test_euler():
    g = {1: {2, 4}, 2: {1, 3}, 3: {2, 4}, 4: {1, 3}}
    assert cycles_egaux(euler(g), [1, 2, 3, 4])


def test_euler2():
    g  = {1: {2, 3}, 2: {1, 3}, 3: {1, 2, 4, 5}, 4: {3, 5}, 5: {3, 4}}
    assert cycles_egaux(euler(g), [1, 2, 3, 4, 5]) or cycles_egaux(euler(g), [1, 2, 3, 5, 4]) or cycles_egaux(euler(g), [2, 1, 3, 4, 5]) or cycles_egaux(euler(g), [2, 1, 3, 5, 4])


def test_a_des_aretes():
    g = {1: {}, 2: {}}
    assert not a_des_aretes(g)


def test_a_des_aretes2():
    g = {1: {2}, 2: {1}}
    assert a_des_aretes(g)