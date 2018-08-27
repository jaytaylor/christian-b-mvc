# -*- coding: utf-8 -*-

import re

class TemperatureConverter(object):
    def __init__(self):
        pass

    @staticmethod
    def forC(tC):
        tC = TemperatureConverter.number(tC)
        if tC is None:
            return 0

        tF = ((9 / 5) * tC) + 32
        return tF

    @staticmethod
    def forF(tF):
        tF = TemperatureConverter.number(tF)
        if tF is None:
            return 0

        tC = (5 / 9) * (tF - 32)
        return tC

    @staticmethod
    def number(value):
        try:
            return float(value)
        except ValueError:
            # If conversion to a float fails, then the input was invalid.
            return None
