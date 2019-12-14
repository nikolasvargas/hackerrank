#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nested_lists.py
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
# CHALLENGE: https://www.hackerrank.com/challenges/nested-list/problem


def main(args):
    sorted_grade = sorted(list({i[1] for i in args}))
    names = "\n".join(sorted([i[0] for i in args if i[1] == sorted_grade[1]]))
    print(names)
    return 0


if __name__ == '__main__':
    n = int(input())
    grades = [[input(), float(input())] for _ in range(n)]
    main(grades)
