#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def czy_puste(self, game, poz):
        """Czy podana pozycja jest pusta?"""
        if ('normal' in rg.loc_types(poz)) and not ('obstacle' in rg.loc_types(poz)):
            if game.robots.get(poz) == None:
                return True
        return False


    def wrogowie_obok23(self, game):
        """Lista wrogów oddalonych o 2-3 pozycje"""
        lista = []
        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) == 2 or rg.dist(poz, self.location) == 3:
                    lista.append(poz)
        return lista


    def czy_wejscie(self, poz):
        """Czy podana pozycja jest punktem wejścia?"""
        if 'spawn' in rg.loc_types(poz):
            return True
        return False


    def czy_wrog(self, game, poz):
        """Czy na podanej pozycji jest wróg?"""
        if game.robots.get(poz) != None:
            if game.robots[poz].player_id != self.player_id:
                return True
        return False

    def wrogowie(self, game):
        """Lista wrogów wokół robota"""
        wrogowie_obok = []  # pusta lista
        for poz, robot in game.robots.iteritems():
            for poz in rg.locs_around(self.location):
                if self.czy_wrog(game, poz) and poz not in wrogowie_obok:
                    wrogowie_obok.append(poz)
        return wrogowie_obok;

    def bezpieczne(self, game):
        """Funkcja zwraca listę bezpiecznych miejsc wokół robota
        o podanej pozycji"""
        lista = []  # pusta lista
        for poz in rg.locs_around(self.location):
            if self.czy_puste(game, poz):
                lista.append(poz)
        return lista


    def act(self, game):

        bezpieczne = self.bezpieczne(game)
        wrogowie = self.wrogowie(game)
        #self.bezpieczne(game) = doopa
        """
        if self.czy_wejscie:
            return ['move', rg.toward(self.location, bezpieczne[0])]
        if wrogowie:
            for poz, robot in game.robots.iteritems():
                if robot.player_id != self.player_id:
                    if rg.dist(poz, self.location) <= 1:
                        return ['attack', poz]
        """
        for poz, robot in game.robots.iteritems():
                if robot.player_id != self.player_id:
                    if rg.dist(poz, self.location) <= 1:
                        return ['attack', poz]

        if self.czy_wejscie:
            return ['move', rg.toward(self.location, bezpieczne[1])]
        if not self.wrogowie_obok23 >0 :
            return ['guard']
        else:
            return ['suicide']

