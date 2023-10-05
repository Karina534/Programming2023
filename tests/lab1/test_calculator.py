import pytest
from src.lab1 import calculator
from tkinter import messagebox
def test_calculat_sqrt():
    assert calculator.sqrt(4) == 2
    #with ValueError as error:
        #assert messagebox.showinfo('Ты лох', "На ноль делить нельзя!")
