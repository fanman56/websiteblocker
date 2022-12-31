import customtkinter as ct
import tkinter as tk
from pathlib import Path


# main class
class Website():
    def __init__(self, site) -> None:
        self.orignalfile = Path("c:/Windows/System32/Drivers/etc/hosts")

        self.site = site

    # blocking site method
    def block(self):
        newvar = self.orignalfile.read_text() + "\n" + "0.0.0.0 " + self.site
        self.orignalfile.write_text(newvar)

    # unblocking site method
    def unblock(self):
        if self.site in self.orignalfile.read_text():
            newvar = self.orignalfile.read_text()
            out = newvar.replace("0.0.0.0 " + self.site, "")
            self.orignalfile.write_text(out)

    # list reading
    def readlist(self):
        weblist = self.orignalfile.read_text().rstrip()
        return weblist


class MyGUI():

    def __init__(self) -> None:
        self.root = ct.CTk()
        self.lable = ct.CTkLabel(self.root, text="Website_Blocker", font=("Arial", 18))
        self.lable.pack(padx=10, pady=12)
        self.root.geometry("500x550")
        self.root.title("Web_V0.1")

        self.textbox = ct.CTkTextbox(self.root, height=8)
        self.textbox.pack(padx=10, pady=12)

        self.checkstate = ct.IntVar()
        self.check = ct.CTkCheckBox(self.root, text="Unblock all", variable=self.checkstate)
        self.check.pack(padx=10, pady=10)

        self.blockbtn = ct.CTkButton(self.root, text="Block", command=self.block)
        self.blockbtn.pack(padx=10, pady=10)

        self.unblockbtn = ct.CTkButton(self.root, text="Unblock", command=self.unblock)
        self.unblockbtn.pack(padx=10, pady=10)

        self.list0btn = ct.CTkButton(self.root, text="BlockList", command=self.list0)
        self.list0btn.pack(padx=10, pady=10)

        self.labler = ct.CTkLabel(self.root, text="", height=20)
        self.labler.pack(padx=10, pady=12)

        self.textbox1 = tk.Text(bg="Black", fg="blue", )
        self.textbox1.pack(padx=10, pady=10, expand=True)

        self.root.mainloop()

    def block(self):
        user_input = self.textbox.get('1.0', ct.END)
        web = Website(user_input)
        web.block()
        self.labler.configure(text=f"{user_input} Blocked")

    def unblock(self):
        user_input = self.textbox.get('1.0', ct.END)
        web = Website(user_input)
        web.unblock()
        self.labler.configure(text=f"{user_input} Unblocked")

    def list0(self):
        self.textbox1.delete('1.0', tk.END)
        self.textbox1.insert(tk.END, Website("").orignalfile.read_text().strip())


MyGUI()