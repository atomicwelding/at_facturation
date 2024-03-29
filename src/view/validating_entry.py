""" Fredrik Lundh, " June 30, 1998 " @ http://effbot.org/zone/tkinter-entry-validate.htm
"""

from tkinter import *

class ValidatingEntry(Entry):
    # base class for validating entry widgets

    def __init__(self, master, value="", **kw):
        # apply(Entry.__init__, (self, master), kw)
        Entry.__init__(*(self, master), kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set("") # corrected the original code version, because it was prefilling Entry widgets with braces
        self.__variable.trace("w", self.__callback)
        self.config(textvariable=self.__variable)

    def __callback(self, *dummy):
        value = self.__variable.get()
        newvalue = self.validate(value)
        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(self.newvalue)
        else:
            self.__value = value

    def validate(self, value):
        # override: return value, new value, or None if invalid
        return value

class MaxLengthEntry(ValidatingEntry):

    def __init__(self, master, value="", maxlength=None, **kw):
        self.maxlength = maxlength
        # apply(ValidatingEntry.__init__, (self, master), kw)
        ValidatingEntry.__init__(*(self, master), kw)

    def validate(self, value):
        if self.maxlength is None or len(value) <= self.maxlength:
            return value
        return None # new value too long