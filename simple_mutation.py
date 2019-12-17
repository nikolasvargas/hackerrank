#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simple_mutation.py
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
#  https://www.hackerrank.com/challenges/python-mutations/problem
"""
- Task
    Read a given string, change the character at a given index and then print the modified string.

- Sample Input
    abracadabra
    5 k

- Sample Output
    abrackdabra
"""

def mutate_string(string, position, character):
    ret = list(string)
    ret[position] = character
    return "".join(ret)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
