import tkinter as tk
from package.MainPage import MainPage

class GUISetUp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, defualt="") must be ico file, 16x16
        tk.Tk.wm_title(self, "What to Eat")
        
        self.container = tk.Frame(self)
        self.container.pack(side="top",fill="both", expand= True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.resizable(width=False, height=False)

        menubar = tk.Menu(self.container)
        filemenu = tk.Menu(menubar, tearoff=0)
        #filemenu.add_command(label="New Recipe", command = lambda: showRecipeWindow(self.sql))
        #filemenu.add_command(label="New Item", command = lambda: showItemWindow(self.sql))
        #filemenu.add_command(label="New Leftover", command = lambda: showLeftoverWindow(self.sql))
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=quit)

        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)
        
        frame = MainPage(self.container, self)
        frame.grid(row=0,column=0,sticky="nsew")
        frame.tkraise()

app = GUISetUp()
app.geometry("900x600")
app.mainloop()