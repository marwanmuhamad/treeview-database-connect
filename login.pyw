import tkinter as tk 
from tkinter import messagebox
import tkinter_oop


class Login:
    username = 'marwan'
    password = 'marwan' 
    width = 320
    height = 150
    background = "#313131"
    hdr_color = "#050505"
    fg_color = "#fffa12"

    def __init__(self):
        self.root = tk.Tk()
        self.x = int(0.5*(self.root.winfo_screenwidth() - Login.width))
        self.y = int(0.5*(self.root.winfo_screenheight() - Login.height))
        self.root.title('Login Form')
        self.root.geometry("{}x{}+{}+{}".format(Login.width, Login.height, self.x, self.y))
        self.root.configure(bg = Login.background)
        self.root.overrideredirect(True)
        
        # Labels
        self.user_lbl = tk.Label(self.root, text = 'Username', fg = Login.fg_color, bg = Login.background,
                                font = ("Roboto", 13, "bold"))
        self.user_lbl.grid(row=0, column=0, padx=5, pady=15)
        self.pass_lbl = tk.Label(self.root, text = 'Password', fg = Login.fg_color, bg = Login.background,
                                font = ("Roboto", 13, "bold"))
        self.pass_lbl.grid(row=1, column=0, padx=5, pady=0)
        
        #Variables:
        self.user_txt = tk.StringVar()
        self.pass_txt = tk.StringVar()
        # Entry Forms
        self.user_box = tk.Entry(self.root, width = 25, relief = "flat", textvariable= self.user_txt)
        self.user_box.grid(row=0, column=1, padx=4, pady=15)
        self.user_box.config(font = ("Roboto", 11))
        self.user_box.focus_set()

        self.pass_box = tk.Entry(self.root, width = 25, show= "\u2022", relief = "flat",
                                textvariable= self.pass_txt)
        self.pass_box.grid(row=1, column=1, padx=4, pady=0)
        self.pass_box.config(font = ("Roboto", 11))

        # Buttons 
        self.login_btn = tk.Button(self.root, text = "LOG IN", bg = Login.fg_color, fg = Login.hdr_color, 
                                   relief = "flat", border= 0, activebackground = "#050505",
                                   activeforeground = "#fffa12", font = ("Roboto", 11, "bold"),  
                                   command = self.call_main_form)
        self.login_btn.grid(row = 2, column=0, columnspan= 2, pady = 10, padx = 20, ipadx = 30, ipady = 1)


        self.root.mainloop()
    # FUnctions
    def call_main_form(self):
        if self.user_box.get() == Login.username and self.pass_box.get() == Login.password:
            self.root.destroy()
            tkinter_oop.myApp()
            
        else:
            messagebox.showerror("Error", "Incorrect username or password")
            self.user_box.delete(0, 'end')
            self.pass_box.delete(0, 'end')
            self.user_box.focus_set()
            
if __name__ == '__main__':
    Login()