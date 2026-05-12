#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:51:45 2026

@author: bu3li
"""

from backend.basic_logic import add
from backend.scientific_math import sine
import gui

def test_backend():
    print("Backend test started...\n")

    print("5 + 5 =", add(5, 5))
    print("sin(90) =", sine(90))

    print("\nBackend working successfully.")


if __name__ == "__main__":
    test_backend()