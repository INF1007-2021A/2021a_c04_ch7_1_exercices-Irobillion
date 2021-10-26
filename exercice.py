#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle


# TODO: Définissez vos fonction ici
def trouver_volume(a=2, b=3, c=1, p=5):
    volume = (4 / 3) * math.pi * a * b * c
    masse = p * volume

    return str(masse) + ' kg', str(volume) + ' m^3'


def frequence_lettres(phrase):
    frequences = {}
    for lettre in phrase:
        frequences.update({lettre: phrase.count(lettre)})
    t = {}
    print(frequences)
    g = sorted(frequences, key=lambda x: frequences[x], reverse=True)
    return g[0]


turtle.speed('fastest')

# turning the turtle to face upwards
turtle.rt(-90)

# the acute angle between
# the base and branch of the Y
angle = 30


def draw_tree(taille, niveau):
    if niveau > 0:
        turtle.colormode(255)
        turtle.pencolor(0, 255 // niveau, 0)
        turtle.fd(taille)

        turtle.rt(angle)
        draw_tree(0.8 * taille, niveau - 1)

        turtle.pencolor(0, 255 // niveau, 0)

        turtle.lt(2 * angle)
        draw_tree(0.8 * taille, niveau - 1)

        turtle.pencolor(0, 255 // niveau, 0)

        turtle.rt(angle)
        turtle.fd(-taille)


def valide_adn(adn) -> bool:
    result = True
    for letter in adn:
        if letter not in ['a', 't', 'g', 'c']:
            result = False
    # liste = [1 for letter in list(adn) if letter not in ['a', 't', 'g', 'c']]
    return result


def saisie():
    chaine_adn = input('Donnez une chaine ADN valide: ')

    while True:
        if not valide_adn(chaine_adn):
            chaine_adn = input('Donnez une chaine ADN valide: ')
        else:
            break

    return chaine_adn


def proportions(chaine, sequence):
    prop = (chaine.count(sequence) / len(chaine)) * 100
    print(f'chaine: {chaine}\n' + f'sequence: {sequence}\n' + f'il ya {round(prop, 2)} % de "ca"')


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(print(trouver_volume()))
    frequence_lettres('aaujhjhjkghgksz')
    print(valide_adn("atgklmmatagccaca"))
    # print(saisie())
    proportions('attgcaatggtggtacatg', 'ca')
    draw_tree(80, 7)
    pass
