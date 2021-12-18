import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class main_:
    def __init__(self, master):
        self.master = master
        self.alpha_frame = tk.Frame(self.master, bg="black")
        self.getfile = tk.Button(text='Select a File', width=30, command=self.new_window, fg="white", bg="grey", activebackground="black", activeforeground="white", bd="0")
        on_color = "green"
        off_color = "white"

        def on_check():
            self.full_val = cbvar.get()
            if cbvar.get() == "1":
                self.fullscreen["fg"] = on_color  # if (get current checkbutton state) is "1" then....
            else:
                self.fullscreen["fg"] = off_color

        cbvar = tk.StringVar(self.master)
        cbvar.set(0)
        self.full_val = 0
        self.fullscreen = tk.Checkbutton(variable=cbvar, text="Set Window To Full Screen", width=25, height=2,
                                         bg="black", activeforeground="white", activebackground="black", fg="white", bd="0", command=on_check)
        self.alpha = tk.Scale(self.alpha_frame, width=25, fg="white", bg="black", activebackground="black", bd="0", from_=10, to=100)
        self.lable = tk.Label(self.alpha_frame, text="Alpha Value: ", fg="white", bg="black", activebackground="black", activeforeground="white")
        self.getfile.grid(row=1, column=1, columnspan=2)
        self.fullscreen.grid(row=2, column=1)
        self.alpha.grid(row=1, column=2)
        self.lable.grid(row=1, column=1)
        self.alpha_frame.grid(row=3, column=1, columnspan=2)

    def new_window(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select a Image",
                                          filetypes=[("image files", "*.png"), ("image files", "*.jpg"),
                                                     ("image files", "*.jpeg")])
        if len(path) > 0:
            if self.full_val == 1 or self.full_val:
                self.full_val = True
            else:
                self.full_val = False

            self.alpha_val = self.alpha.get() / 100
            image_window = tk.Toplevel(self.master)
            image_window.iconbitmap("mc@H.ico")
            image_window.attributes("-alpha", self.alpha_val, "-fullscreen", self.full_val)
            image_window.configure(background="black")
            new_window(image_window, path)
        else:
            x = 1
            for i in range(x):
                wr = tk.Tk()
                wr.title("Image overlay By DON'T#7191 for Minecraft@Home")
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
        self.error_frame = tk.Frame(self.master, bg="red")
        self.warning = tk.Button(self.error_frame, text=self.msg + " Click here to reload", bg="red", fg="white", width=35, height=2, command=self.close_reload)
        self.warning.grid(row=1, column=1)
        self.error_frame.grid(row=1, column=1)

    def close_reload(self):
        self.master.destroy()
        main_(self.app_master).new_window()

class new_window:
    def __init__(self, master, filepath):
        self.master = master
        self.image_frame = tk.Frame(self.master, bg="black")
        self.filepath = filepath
        self.quit = tk.Button(self.image_frame, text="Quit", command=self.close_windows)

        if self.filepath.find(".png") != -1:
            self.img_int = tk.PhotoImage(file=self.filepath)
        else:
            self.img_int = ImageTk.PhotoImage(Image.open(self.filepath))

        self.image = tk.Label(self.image_frame, image=self.img_int)
        self.image.pack()
        self.image_frame.grid(row=1, column=1)

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("Image overlay By DON'T#7191 for Minecraft@Home")
    root.iconbitmap("mc@H.ico")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("215x225+%d+%d" % (screen_width / 2 - 275, screen_height / 2 - 125))
    root.configure(background="black")
    main_(root)
    root.mainloop()


if __name__ == '__main__':
    main()

