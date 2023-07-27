# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:57:34 2023

@author: Sandeep
"""

# test_hello.py
from hello import say_hello

def test_say_hello():
    name = "John"
    assert say_hello(name) == f"Hello, {name}!"
