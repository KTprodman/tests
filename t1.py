import pandas as pd
import numpy as np


class Stack(object):

    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def push(self, element):
        self._stack.append(element)
        
    def pop(self):
        try:
            element = self._stack.pop()
        except:
            element = None
        return element
    
    def empty(self):
        self._stack = []
