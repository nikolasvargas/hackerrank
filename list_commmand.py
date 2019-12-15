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

if __name__ == '__main__':
    N = int(input())
    lista = []

    inplace_command = {
        "sort": lista.sort,
        "pop": lista.pop,
        "reverse": lista.reverse
    }

    for i in range(0, N):
        command_name, *params = input().split()

        if command_name == "print":
            print(lista)

        if command_name in ["insert", "remove", "append"]:
            getattr(lista, command_name)(*(map(int, params)))

        if not params and command_name != "print":
            inplace_command[command_name]()
