import tkinter as tk
from tkinter import ttk 
import db
from datetime import datetime
from tkinter.messagebox import showinfo
from tkinter import messagebox
import re
# from login import Login

myDB = db.Database('classicmodels')
data = myDB.fetchData('orderdetails')
column = myDB.fetchColumns()

today = datetime.now()
hari = today.strftime("%A, %d-%m-%Y")
# print(hari)

# login_form = Login()
class myApp:
    width = 800 
    height = 600
    background = "#313131"
    hdr_color = "#050505"
    fg_color = "#fffa12"
    
    # main window:
    def __init__(self):
        self.price = 0
        self.root = tk.Tk()
        self.x = int(0.5*(self.root.winfo_screenwidth() - myApp.width))
        self.y = int(0.5*(self.root.winfo_screenheight() - myApp.height))
        self.root.title('my Object Oriented Application')
        self.root.geometry("{}x{}+{}+{}".format(myApp.width, myApp.height, self.x, self.y))
        self.root.configure(bg = myApp.background)
        # self.root.resizable(0,0)
        self.root.overrideredirect(True)
        
        self.lbl_title = tk.Label(self.root, text = 'TOKO MARWAH BERKAH', font = ("Lato", 10, "bold"), bg = myApp.hdr_color, 
                                  fg = myApp.fg_color, width = 96)
        self.lbl_title.grid(row = 0, column = 0, sticky='nw', columnspan= 8)
        self.lbl_title.bind("<B1-Motion>", self.move)

        self.cls_btn = tk.Button(self.root, text="\u274c", fg=myApp.fg_color, bg = myApp.hdr_color, 
                                font = ("Lato", 9), command = self.close_win,
                                bd=0, activebackground="#fffa12", activeforeground="#000000", highlightbackground = "#fffa12", 
                                highlightcolor = "#000000")
        self.cls_btn.grid(row=0, column=8, sticky='ne', ipadx=0, ipady=0, padx=1, pady=0, columnspan =1)

        # self.min_btn = tk.Button(self.root, text="\u25bc", fg=myApp.fg_color, bg = myApp.hdr_color, 
        #                         font = ("Lato", 9), command = self.minimize_win,
        #                         bd=0)
        # self.min_btn.grid(row=0, column=9, sticky='e', ipadx=2, ipady=0, padx=0, pady=0)

        # Labels
        self.lblAdmin = tk.Label(self.root, text = "Admin : "+str('marwan').title(), 
                                font = ('Lato', 9), bg = myApp.background, fg = myApp.fg_color)
        self.lblAdmin.grid(row = 1, column=0,pady=5, sticky = "w", padx=5)
        
        self.dateVar = tk.StringVar()
        self.dateVar.set("Hari,Tanggal : " + hari)
        self.lblTgl = tk.Label(self.root, textvariable=self.dateVar, font = ('Lato', 9),
                                bg = myApp.background, fg = myApp.fg_color)
        self.lblTgl.grid(row = 1, column=7, sticky = "ne", padx=5)
        self.lblTgl.after(1000)
        
        self.lbl0 = tk.Label(text = " ", bg = myApp.background, fg = myApp.background)
        self.lbl0.grid(row = 2)
        self.lbl1 = tk.Label(self.root, text = 'Kode Pesanan/', font = ('Lato', 12), bg = myApp.background, fg = myApp.fg_color)
        self.lbl1.grid(row=3, column = 0, pady = 2, sticky = 'w', ipadx = 3)
        self.lbl2 = tk.Label(self.root, text = 'Kode Barang', font = ('Lato', 12), bg = myApp.background, fg = myApp.fg_color)
        self.lbl2.grid(row=4, column = 0, sticky = 'w', ipadx = 3)
        self.lbl3 = tk.Label(self.root, text = "HARGA", fg = myApp.fg_color, bg = myApp.background, font = ("Lato", 20, "bold"))
        self.lbl3.grid(row=3, column = 2, rowspan=2, sticky= 'nw')

        # Variables:
        self.code_var = tk.StringVar()
        self.priceVar = tk.StringVar()
        # self.code_var2 = tk.StringVar()
        # Entry forms
        self.txt1 = tk.Entry(self.root, width = 20, bd = 0, textvariable=self.code_var)
        self.txt1.grid(row=3, column = 1, pady = 5, sticky = 'w', ipadx = 3)
        self.txt1.configure(font= ("Lato", 13))
        self.txt1.focus_set()
        self.txt1.bind('<Return>', self.searchItemEvent)

        # Treeview:
        self.tree = ttk.Treeview(self.root, selectmode= "browse")
        self.tree['columns'] = tuple(column)

        #treeview columns
        self.tree.column("#0", width = 0, stretch = False)
        self.tree.column("orderNumber", width = 140, anchor="w")
        self.tree.column("productCode", width = 140, anchor="w")
        self.tree.column("quantityOrdered", width = 130, anchor= "e")
        self.tree.column("priceEach", width = 130, anchor="e")
        self.tree.column("orderLineNumber", width = 150, anchor="e")

        # treeview headings
        self.tree.heading("#0", text = "", anchor = "w")
        self.tree.heading("orderNumber", text = "Kode Pesanan", anchor="center")
        self.tree.heading("productCode", text = "Kode Barang", anchor="center")
        self.tree.heading("quantityOrdered", text = "Jumlah", anchor="center")
        self.tree.heading("priceEach", text = "Harga", anchor="center")
        self.tree.heading("orderLineNumber", text = "No. Urut Pesanan", anchor="center")

        self.tree.tag_configure("oddrow", background= "#BEBEBE", foreground= "#313131")
        self.tree.tag_configure("evenrow", background= "#313131", foreground="#BEBEBE")
        #insert values into Treeview
        for i in range(len(data)):
            if i%2 == 0:
                self.tree.insert(parent="", index = 'end', iid = i, text = "", 
                                values = (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]),
                                tags= ('evenrow',))
            else:
                self.tree.insert(parent="", index = 'end', iid = i, text = "", 
                                values = (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]),
                                tags= ('oddrow',))
        self.tree.grid(row = 6, column = 0, pady = 20, columnspan = 10, padx = 10, sticky = "nsew")
        self.tree.bind('<<TreeviewSelect>>', self.viewPrice)
        
        # add style to Treeview
        self.style = ttk.Style(self.root)
        # self.style.theme_use("default")

        self.style.configure("Treeview",
            background = "#ABABAB",
            foreground= "#000000",
            rowheight = 30,
            borderwidth = 0,
            font = ("Lato", 11),
            fieldbackground = "#ABABAB"
        )
        self.style.configure('Treeview.Heading', 
            foreground='#313131', 
            background = "#fffa12",
            rowheight = 60,
            font = ("Lato", 12, "bold"))

        self.style.map("Treeview",
            background=[("selected", "#fffa12")],
            foreground=[('selected', "#000000")])
        
        # Buttons
        self.search_btn = tk.Button(self.root, text = "Search Item", bg = myApp.fg_color, font = ("Lato",11), 
                                    fg = "#313131",bd = 0, relief = 'flat', activebackground= "#000000",
                                    activeforeground="#fffa12",command = self.searchItem)
        self.search_btn.grid(row = 5, column = 0, padx = 5, ipadx = 3, pady = 10, ipady = 3, sticky= "w")                 
        
        self.root.mainloop()
    # Functions:
    def close_win(self):
        self.ask = messagebox.askyesno("Quit?", "Are you sure want to quit?")
        if self.ask:
            # self.root.quit
            self.root.destroy()
        else:
            return None
    
    def move(self, event):
        self.root.geometry(f"+{event.x_root}+{event.y_root}")
    
    def minimize_win(self):
        # self.root.overrideredirect(False)
        self.root.iconify()
        # self.root.deiconify()
        # self.root.overrideredirect(True)
    def searchItem(self, table = 'orderdetails', x1 = None): 
        self.priceVar.set("")
        x1 = self.txt1.get()
        if x1:
            data = myDB.searchItems(table = table, x = x1)

        else:
            data = myDB.fetchData(table)
        for children in self.tree.get_children():
            self.tree.delete(children)
        
        for i in range(len(data)):
            if i%2 == 0:
                self.tree.insert(parent="", index = 'end', iid = i, text = "", 
                                values = (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]),
                                tags= ('evenrow',))
            else:
                self.tree.insert(parent="", index = 'end', iid = i, text = "", 
                                values = (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]),
                                tags= ('oddrow',))
    def searchItemEvent(self, event): 
        self.priceVar.set("")
        x1 = self.txt1.get()
        if x1:
            data = myDB.searchItems(table = 'orderdetails', x = x1)

        else:
            data = myDB.fetchData('orderdetails')
        for children in self.tree.get_children():
            self.tree.delete(children)
        
        for i in range(len(data)):
            if i%2 == 0:
                self.tree.insert(parent="", index = 'end', iid = i, text = "", 
                                values = (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]),
                                tags= ('evenrow',))
            else:
                self.tree.insert(parent="", index = 'end', iid = i, text = "", 
                                values = (data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]),
                                tags= ('oddrow',))
    
    def viewPrice(self, event):
        self.priceVar.set("")
        
        x = self.tree.focus()
        y = self.tree.item(x)['values'][3]
        self.priceVar.set('$'+str(y))
        # z = self.tree.item(x)
        # w = self.tree.index(self.tree.focus())
        # print(w)
        # print(z)
        # print(x, y)
        # print(self.tree.item(x))
        # print(type(y))
        # print(dir(self.tree))

        self.lbl4 = tk.Label(self.root, textvariable=self.priceVar, fg = myApp.fg_color, bg = myApp.background, font = ("Lato", 20, "bold"))
        self.lbl4.grid(row=4, column = 2, rowspan=2, sticky= 'nw')

if __name__ == '__main__':
    
    myApp() #myApp.width, myApp.height
    # print("This is working well")