# -*- coding: utf-8 -*-

import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, controller):
        tk.Frame.__init__(self)
        self.pack()

        self.controller = controller

        self.createLayout()

    def createLayout(self):
        """
        Creates and wires up the application page view handlers.
        """
        # Celsius portion.
        self.label_celsius = tk.Label(self, text="Celsius")
        self.label_celsius.grid(row=0, sticky=tk.W)

        self.celsius_var = tk.StringVar(name="celsius")
        self.celsius_var.set(32)

        self.celsius = tk.Entry(self, textvariable=self.celsius_var)
        self.celsius.grid(row=0, column=1)

        # Activate the celsius widget.
        self.celsius.focus()

        # Highlight the celsius input field text so the user doesn't have to
        # press TAB or click anything get started converting.
        self.celsius.select_range(0, 'end')

        # Move cursor to right.
        self.celsius.icursor(2)

        # Fahrenheit portion.
        self.label_fahrenheit = tk.Label(self, text="Fahrenheit")
        self.label_fahrenheit.grid(row=1, sticky=tk.W)

        self.fahrenheit_var = tk.StringVar(name="fahrenheit")
        self.fahrenheit_var.set(0)

        # Attach event handlers.
        handler = self.controller.genInputUpdatedFunc(celsius_var=self.celsius_var, fahrenheit_var=self.fahrenheit_var)
        self.celsius_var.trace("w", handler)
        self.fahrenheit_var.trace("w", handler)

        self.fahrenheit = tk.Entry(self, textvariable=self.fahrenheit_var)
        self.fahrenheit.grid(row=1, column=1)

        # Quit button.

        self.quit_button = tk.Button(self)
        self.quit_button["text"] = "Quit"
        self.quit_button["command"] =  self.quit
        self.quit_button.grid(row=2, column=3)
