import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

def to_bool(x):
    if x in [1, "1", "true", "True", "TRUE", True]:
        return True
    elif x in [0, -1, "-1", "0", "False", False, "FALSE"]:
        return False

class app:
    def __init__(self, master):
        self.master = master
        self.alpha_frame = tk.Frame(self.master, bg="black")
        self.getfile = tk.Button(text='Select a File', width=30, command=self.new_window, fg="white", bg="grey", activebackground="black", activeforeground="white", bd="0")

        self.fullvar = tk.StringVar(self.master)
        self.bordervar = tk.StringVar(self.master)
        self.fullvar.set(0)
        self.bordervar.set(0)
        self.fullscreen = tk.Checkbutton(variable=self.fullvar, text="Set Window To Full Screen", width=25, height=2,
                                         bg="black", activeforeground="white", activebackground="black", fg="white", bd=0, command=lambda: self.on_check(self.fullvar, self.fullscreen))
        self.border = tk.Checkbutton(variable=self.bordervar, text="Window Without border", width=25, height=2,
                                         bg="black", activeforeground="white", activebackground="black", fg="white",
                                         bd=0, command=lambda: self.on_check(self.bordervar, self.border))
        self.alpha = tk.Scale(self.alpha_frame, width=25, fg="white", bg="black", activebackground="black", bd=0, from_=10, to=100)
        self.lable = tk.Label(self.alpha_frame, text="Alpha Value: ", fg="white", bg="black", activebackground="black", activeforeground="white")
        self.getfile.grid(row=1, column=1, columnspan=2)
        self.fullscreen.grid(row=2, column=1)
        self.border.grid(row=3, column=1)
        self.alpha.grid(row=1, column=2)
        self.lable.grid(row=1, column=1)
        self.alpha_frame.grid(row=4, column=1, columnspan=2)

    def on_check(self, var, obj):
        if var.get() == "1":
            obj["fg"] = "green"
        else:
            obj["fg"] = "white"

    def new_window(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select a Image",
                                          filetypes=[("image files", "*.png"), ("image files", "*.jpg"),
                                                     ("image files", "*.jpeg")])
        if len(path) > 0:
            alpha_val = self.alpha.get() / 100
            image_window = tk.Toplevel(self.master)
            image_window.iconbitmap("mc@H.ico")
            image_window.configure(background="#fff123")
            image_window.attributes("-transparentcolor", "#fff123", "-alpha", alpha_val, "-fullscreen", self.fullvar.get())
            image_window.overrideredirect(self.bordervar.get())
            new_window(image_window, path)
        else:
            x = 1
            for i in range(x):
                wr = tk.Tk()
                wr.title("Image overlay By DON'T#9171 for Minecraft@Home")
                wr.configure(background="red")
                wr.iconbitmap("mc@H.ico")
                error(wr, "There is No File Selected", self.master).window()
                if len(path) > 0:
                    break
                else:
                    x += 1

class error:
    def __init__(self, master, msg, app_master):
        self.master = master
        self.msg = msg
        self.app_master = app_master

    def window(self):
        error_frame = tk.Frame(self.master, bg="red")
        warning = tk.Button(error_frame, text=self.msg + " Click here to reload", bg="red", fg="white", width=35, height=2, command=self.close_reload)
        warning.grid(row=1, column=1)
        error_frame.grid(row=1, column=1)

    def close_reload(self):
        self.master.destroy()
        app(self.app_master).new_window()

class new_window:
    def __init__(self, master, filepath):
        self.master = master
        self.filepath = filepath
        vis = tk.StringVar(self.master)
        vis.set(1)

        def change():
            # print("[DEBUG] Vis: ", vis.get(), type(vis.get()), " Bool: ", to_bool(vis.get()))
            if not to_bool(vis.get()):
                self.visible["bg"] = "white"
                self.visible["fg"] = "Black"
                self.visible["text"] = "Visibility [OFF]"
                self.canvas.pack_forget()
            else:
                self.visible["bg"] = "black"
                self.visible["fg"] = "grey"
                self.visible["text"] = "Visibility [ON]"
                self.canvas.pack()

        if self.filepath.find(".png") != -1:
            self.img_int = tk.PhotoImage(file=self.filepath)
        else:
            self.img_int = ImageTk.PhotoImage(Image.open(self.filepath))

        width, height = Image.open(self.filepath).size
        self.canvas = tk.Canvas(self.master, bg="black", highlightthickness=0, bd=0, width=width, height=height)
        self.canvas.pack()
        self.canvas.create_image(width/2, height/2, image=self.img_int)
        self.quit_button = tk.Button(self.master, text="Quit", command=self.close_windows, anchor="w", width=5, activebackground="red", bd=0, bg="black", fg="white")
        self.visible = tk.Checkbutton(self.master, variable=vis, text="Visiblility [ON]", fg="grey", bg="black", width=12, activebackground="black", bd=0, command=lambda: change())
        attributes = self.master.attributes()

        if attributes[7]:
            self.visible.place(x=self.master.winfo_width(), y=0, anchor="ne")
        else:
            self.visible.place(x=self.master.winfo_width() - 25, y=0, anchor="ne")
        # self.visible_wind = self.canvas.create_window(width, 0, anchor="ne", window=self.visible)
        self.quit_button_window = self.canvas.create_window(0, 0, anchor='nw', window=self.quit_button)

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("Image overlay By DON'T#9171 for Minecraft@Home")
    root.iconbitmap("mc@H.ico")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("215x225+%d+%d" % (screen_width / 2 - 275, screen_height / 2 - 125))
    root.configure(background="black")
    app(root)
    root.mainloop()


if __name__ == '__main__':
    main()
