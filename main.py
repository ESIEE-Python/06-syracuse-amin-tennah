""" Fonctions secondaires###"""


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """ Fonctions secondaires###"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')

#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # votre code ici

    n = len(l)
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    initial_value = l[0]
    for k in range(1, len(l)):
        if l[k] < initial_value:
            return k
    return -1


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici

    n = max(l)
    return n


#### Fonction principale


def main():
    """le main"""

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print("Temps de vol:", temps_de_vol(lsyr))
    print("Temps de vol en altitude:", temps_de_vol_en_altitude(lsyr))
    print("Altitude maximale:", altitude_maximale(lsyr))

    # Autres exemples
    lsyr2 = syracuse_l(27)
    syr_plot(lsyr2)
    print("Temps de vol pour n=27:", temps_de_vol(lsyr2))
    print("Temps de vol en altitude pour n=27:", temps_de_vol_en_altitude(lsyr2))
    print("Altitude maximale pour n=27:", altitude_maximale(lsyr2))

    lsyr3 = syracuse_l(5)
    syr_plot(lsyr3)
    print("Temps de vol pour n=5:", temps_de_vol(lsyr3))
    print("Temps de vol en altitude pour n=5:", temps_de_vol_en_altitude(lsyr3))
    print("Altitude maximale pour n=5:", altitude_maximale(lsyr3))


if __name__ == "__main__":
    main()
