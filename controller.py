# -*- coding: utf-8 -*-

import logging
import tkinter as tk

import model
import view

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

class Controller(object):
    def __init__(self):    
        self.root = tk.Tk()

        self.model = model.TemperatureConverter()
        self.view = view.Frame(self)

    def mainloop(self):
        self.view.mainloop()
        # Disabled reference to destroy because it triggers this exception on
        # Windows:
        #
        # _tkinter.TclError: can't invoke "destroy" command: application has
        #                    been destroyed
        #
        # Christian: Try enabling it on Linux and see if you get a different
        # result.
        #
        #self.root.destroy()

    
    def genInputUpdatedFunc(self, celsius_var, fahrenheit_var):
        # After a new calculation, the .set() invocation triggers an additional
        # unwanted update of the originally submitted value.
        #
        # Use a variable to ignore updates triggered by our .set() call.
        #
        # Use a dict variable to be able to mutate in this outer scope without
        # needing to declare a (dirty, in this case) global.
        d = {'ignore': False}

        def handler(var_name, *args):
            """Note: *args is ignored for our purposes."""
            if d['ignore']:
                return

            logger.info('handler invoked, var_name=%s, args=%s' % (var_name, args))

            if var_name == "celsius":
                tF = self.model.forC(celsius_var.get())
                d['ignore'] = True
                fahrenheit_var.set(tF)
                d['ignore'] = False
            elif var_name == "fahrenheit":
                tC = self.model.forF(fahrenheit_var.get())
                d['ignore'] = True
                celsius_var.set(tC)
                d['ignore'] = False

        return handler
