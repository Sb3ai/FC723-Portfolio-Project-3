#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:53:22 2026

@author: nasserali
"""
# This part is coded by nasser / My partner
import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)

display = tk.Entry(
    root,
    font=("Arial", 30),
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)

display.pack(fill="both", ipadx=8, pady=20, padx=10)

root.mainloop()