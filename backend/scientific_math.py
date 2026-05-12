#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:08:49 2026

@author: bu3li
"""

# Importing math libary
import math

# Function to calculate sine
def sine(degrees):
    return math.sin(math.radians(degrees))

# Function to calculate cosine
def cosine(degrees):
    return math.cos(math.radians(degrees))

# Function to calculate tangent
def tangent(degrees):
    return math.tan(math.radians(degrees))

# Function to calculate arcsine
def arcsine(value):
    # Check if value is between -1 and 1
    if value < -1 or value > 1:
        raise ValueError("Arcsin input must be between -1 and 1")
    return math.degrees(math.asin(value))

# Function to calculate arccosine
def arccosine(value):
    if value < -1 or value > 1:
        raise ValueError("Arccos input must be between -1 and 1")
    return math.degrees(math.acos(value))

# Function to calculate arctangent
def arctangent(value):
    return math.degrees(math.atan(value))

# Function to calculate logarithm base 10
def log(a):
    # Prevent log of zero or negative numbers
    if a <= 0:
        raise ValueError("Log input must be greater than 0")
    return math.log10(a)

# Function to calculate natural logarithm
def ln(a):
    # Prevent ln of zero or negative numbers
    if a <= 0:
        raise ValueError("Ln input must be greater than 0")
    return math.log(a)

# Function to calculate factorial

def factorial(a):
    if a < 0:# Prevent negative factorial values
        raise ValueError("Factorial input cannot be negative")
    if int(a) != a:# Prevent decimal factorial values
        raise ValueError("Factorial input must be a whole number")
    return math.factorial(int(a))