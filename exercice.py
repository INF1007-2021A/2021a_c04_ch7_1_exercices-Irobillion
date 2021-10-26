#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


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


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(print(trouver_volume()))
    frequence_lettres('aaujhjhjkghgksz')
    pass
