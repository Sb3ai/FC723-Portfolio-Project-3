#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:53:24 2026

@author: bu3li
"""
import math
# This file contains the basic calculator operations.


# Function to add two numbers
def add(a, b):
    return a + b

# Funcion to subtract
def subtract(a, b):
    return a - b

# Function to multiply
def multiply(a, b):
    return a * b

# Function to divide
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Function to square
def square(a):
    return a ** 2

# Function to square root
def square_root(a):
    if a < 0:
        raise ValueError("Cannot square root a negative number")
    return math.sqrt(a)
# Functio to give power
def power(a, b):
    return a ** b

# FUnction for convert to percentage
def percentage(a):
    return a / 100