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
    return g


def creer_graph2():
    g2 = dict()
    g2[1] = set([2, 4])
    g2[2] = set([1, 4, 3])
    g2[3] = set([2, 4])
    g2[4] = set([1, 2, 3])
    return g2

def test_voisins():
    g = creer_graph1()
    assert g["a"] == {"b", "c"}
    assert g["b"] == {"a", "c"}


def test_non_voisins():
    g = creer_graph2()
    assert 1 not in g[3]


def test_longeur():
    g = creer_graph1()
    assert len(g["a"]) == 2