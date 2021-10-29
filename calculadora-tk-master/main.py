# -*- coding: utf-8 -*-

# @author: Ayan Khan
# @github: github.com/Zakk242K
# @Created: 17-oct-2018

# Builtin
import tkinter as tk

# Módulo próprio
from app.calculadora import Calculadora

if __name__ == '__main__':
    master = tk.Tk()
    main = Calculadora(master)
    main.start()
