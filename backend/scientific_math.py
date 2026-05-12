#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:08:49 2026

@author: bu3li
"""


import math


def sine(degrees):
    return math.sin(math.radians(degrees))


def cosine(degrees):
    return math.cos(math.radians(degrees))


def tangent(degrees):
    return math.tan(math.radians(degrees))


def arcsine(value):
    if value < -1 or value > 1:
        raise ValueError("Arcsin input must be between -1 and 1")
    return math.degrees(math.asin(value))


def arccosine(value):
    if value < -1 or value > 1:
        raise ValueError("Arccos input must be between -1 and 1")
    return math.degrees(math.acos(value))


def arctangent(value):
    return math.degrees(math.atan(value))