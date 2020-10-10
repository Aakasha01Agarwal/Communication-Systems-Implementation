# Imports

import numpy as np                              ## pip install numpy
import matplotlib.pyplot as plt                 ## pip install matplotlib
import tkinter as tk
from tkinter import simpledialog

pi=3.14                                         ## can use np.pi instead
t=np.linspace(0,2*pi, 10000)

class DSB_SC:
    def __init__(self):
        #inputs from the GUI
        self.application_window = tk.Tk()
        self.application_window.withdraw()
        self.ac=simpledialog.askfloat("Input", "Ac?", parent=self.application_window)
        self.am=simpledialog.askfloat("Input", "Am?", parent=self.application_window)
        self.fm=simpledialog.askfloat("Input", "fm?", parent=self.application_window)
        self.fc=simpledialog.askfloat("Input", "fc?", parent=self.application_window)
        self.plot_all()

    def carrier(self):
        var = 2 * pi * self.fc * t
        signal = self.ac* np.cos(var)
        return signal

    def message(self):
        var = 2 * pi * self.fm * t
        signal = self.am * np.cos(var)
        return signal

    def dsb_sc(self):
        x = np.multiply(self.carrier(), self.message())
        return x

    def plot_carrier(self):
        plt.plot(t, self.carrier())
        plt.show()

    def plot_message(self):
        plt.plot(t, self.message())
        plt.show()

    def plot_dsb_sc(self):
        plt.plot(t, self.dsb_sc())
        plt.show()

    def plot_all(self):
        fig, axes= plt.subplots(3)
        fig.suptitle('Plots')
        axes[0].set_title("Carrier Signal")
        axes[0].plot(t, self.carrier())
        axes[1].set_title("Message Signal")
        axes[1].plot(t, self.message())
        axes[2].set_title("DSB_SC Signal")
        axes[2].plot(t, self.dsb_sc())
        plt.show()



dsb=DSB_SC()

