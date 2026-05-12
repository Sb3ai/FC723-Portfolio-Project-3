#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:53:24 2026

@author: bu3li
"""
import math
# This file contains the basic calculator operations.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square(a):
    return a ** 2


def square_root(a):
    if a < 0:
        raise ValueError("Cannot square root a negative number")
    return math.sqrt(a)