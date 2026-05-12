#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:00:44 2026

@author: bu3li
"""

def convert_to_number(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Invalid input. Please enter a number.")


def check_empty(value):
    if value == "":
        raise ValueError("Input cannot be empty")
    return True


def validate_two_numbers(value1, value2):
    check_empty(value1)
    check_empty(value2)

    num1 = convert_to_number(value1)
    num2 = convert_to_number(value2)

    return num1, num2


def validate_one_number(value):
    check_empty(value)
    return convert_to_number(value)