def puiss(a, b):

    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")

    if a == 0 and b < 0:
        raise ValueError("Une puissance négative de 0 est indéfinie")

    resultat = 1

    for i in range(abs(b)):
        resultat = resultat * a

    if b < 0:
        resultat = 1 / resultat

    return resultat