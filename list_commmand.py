#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  list_command.py
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
#  https://www.hackerrank.com/challenges/python-lists/problem
"""
Input (stdin)
-------------
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Expected Output
---------------
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
if __name__ == '__main__':
    N = int(input())
    lista = []

    for i in range(0, N):
        command_name, *params = input().split()
        try:
            getattr(lista, command_name)(*(map(int, params)))
        except AttributeError:
            print(lista)
