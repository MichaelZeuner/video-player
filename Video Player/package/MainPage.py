import tkinter as tk   


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.mainFrame = tk.Frame(self.canvas)
        self.canvas.pack(side="left",fill="both",expand=True)
        self.canvas.create_window((4,4), window=self.mainFrame, anchor="nw", tags="self.mainFrame")