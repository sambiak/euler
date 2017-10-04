
def eulerien(graphe):
    for sommet in graphe :
        if len(graphe[sommet])%2 != 0 or len(graphe[sommet]) < 2 :
            return False
    return True

