import tkinter as tk
from tkinter import *

class InstructionEntry(tk.Entry):
    def __init__(self, master=None, instrText="", instrColor="gray", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.instrText = instrText
        self.instrColor = instrColor
        self.insert(0, instrText)
        self.configure(foreground=instrColor)
        self.bind("<FocusIn>", self.clearInstrText)
        self.bind("<FocusOut>", self.addInstrText)

    def clearInstrText(self, event):
        if self.get() == self.instrText:
            self.delete(0, tk.END)
            self.configure(foreground="black")

    def addInstrText(self, event):
        if not self.get():
            self.insert(0, self.instrText)
            self.configure(foreground=self.instrColor)

class InstructionText(tk.Text):
    def __init__(self, master=None, instrText="", instrColor="gray", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.instrText = instrText
        self.instrColor = instrColor
        self.insert("1.0", instrText)
        self.configure(foreground=instrColor)
        self.bind("<FocusIn>", self.clearInstrText)

    def clearInstrText(self, event):
        if self.get("1.0", "end-1c") == self.instrText:
            self.delete("1.0", tk.END)
            self.configure(foreground="black")


    