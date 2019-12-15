#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minion_game.py
#
#  Copyright 2019 Níkolas Vargas <vargasnikolass@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#  https://www.hackerrank.com/challenges/the-minion-game/


# def minion_game(string: str) -> int:
#     vowels, length = 'AEIOU', len(string)
#     for i in range
#     return 0


if __name__ == '__main__':
    s = input()
    vowels = 'AEIOU'
    K = sum([len(s)-i for i, letter in enumerate(s) if letter in vowels])
    S = sum([len(s)-i for i, letter in enumerate(s) if letter not in vowels])
    print(['Stuart '+str(S), ['Kevin '+str(K), 'Draw'][K == S]][K >= S])
