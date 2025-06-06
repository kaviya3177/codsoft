import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
       
        title = tk.Label(self.root, text="To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        self.task_entry = tk.Entry(self.root, font=("Arial", 14))
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)

        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=5)

        add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)

        del_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=self.delete_task)
        del_btn.grid(row=0, column=1, padx=5)

        mark_btn = tk.Button(btn_frame, text="Mark as Done", width=12, command=self.mark_done)
        mark_btn.grid(row=0, column=2, padx=5)

        self.task_listbox = tk.Listbox(self.root, font=("Arial", 12), height=15, selectbackground="#a6a6a6")
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Input Error", "Task cannot be empty.")
        else:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            if not task.startswith("[Done] "):
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, "[Done] " + task)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
