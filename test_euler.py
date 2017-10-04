from euler import eulerien







def test_sommet():
    for s in


def test_eulerien():
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



    assert eulerien(g)
    assert not eulerien(g2)

