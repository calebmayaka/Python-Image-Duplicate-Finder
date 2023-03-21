import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Duplicate Image Finder")
        self.pack()

        # create widgets
        self.dir_label = tk.Label(self, text="Directory:")
        self.dir_label.grid(row=0, column=0)

        self.dir_entry = tk.Entry(self)
        self.dir_entry.grid(row=0, column=1)

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2)

        self.run_button = tk.Button(self, text="Find Duplicates", command=self.find_duplicates)
        self.run_button.grid(row=1, column=1)

        self.delete_var = tk.BooleanVar(value=False)
        self.delete_checkbox = tk.Checkbutton(self, text="Delete duplicates", variable=self.delete_var)
        self.delete_checkbox.grid(row=2, column=1)

        self.quit_button = tk.Button(self, text="Quit", command=self.master.quit)
        self.quit_button.grid(row=3, column=1)

        # initialize variables
        self.directory = None

    def browse_directory(self):
        self.directory = filedialog.askdirectory()
        self.dir_entry.delete(0, tk.END)
        self.dir_entry.insert(0, self.directory)

    def find_duplicates(self):
        if not self.directory:
            messagebox.showerror("Error", "Please select a directory")
            return

        # create a dictionary to store file hashes and paths
        hashes = {}

        # loop through all files in the directory
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)

            # check if the file is an image
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):

                # open the file and calculate its hash
                with open(filepath, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()

                # if the hash is already in the dictionary, we've found a duplicate
                if file_hash in hashes:
                    messagebox.showinfo("Duplicate found", f"Duplicate found: {filename}")
                    if self.delete_var.get():
                        os.remove(filepath)
                        messagebox.showinfo("Duplicate deleted", f"Duplicate deleted: {filename}")
                else:
                    hashes[file_hash] = filepath

        messagebox.showinfo("Complete", "Duplicate search complete")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
