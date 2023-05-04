import tkinter as tk
from tkinter import filedialog
import other
class SkipIDE:
    def __init__(self, master):
        self.master = master
        self.master.title("SkipIDE 0.1")
        self.text_area = tk.Text(self.master)
        self.text_area.pack(fill="both", expand=True)

        # Menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # File options
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Other options
        other_menu = tk.Menu(menu_bar, tearoff=0)
        other_menu.add_command(label="Check for Updates", command=other.check_for_updates)
        menu_bar.add_cascade(label="Others", menu=other_menu)

        # Keyboard shortcuts
        self.master.bind('<Control-o>', self.open_file)
        self.master.bind('<Control-s>', self.save_file)
        self.master.bind('<Control-Shift-s>', self.save_file_as)

        # Open file indicator
        self.file_path = None
        self.update_title()

    def update_title(self):
        if self.file_path:
            self.master.title(f"SkipIDE 0.1 - {self.file_path}")
        else:
            self.master.title("SkipIDE 0.1")

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(defaultextension=".sk",
                                               filetypes=[("SK files", "*.sk"),
                                                          ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", content)
            self.file_path = file_path
            self.update_title()
    
    def save_file(self, event=None):
        if self.file_path:
            with open(self.file_path, "w") as file:
                content = self.text_area.get("1.0", "end-1c")
                file.write(content)
            self.update_title()
        else:
            self.save_file_as()

    def save_file_as(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".sk",
                                                 filetypes=[("SK files", "*.sk"),
                                                            ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", "end-1c")
                file.write(content)
            self.file_path = file_path
            self.update_title()

    def quit(self):
        self.master.quit()

if __name__ == '__main__':
    root = tk.Tk()
    app = SkipIDE(root)
    root.mainloop()
