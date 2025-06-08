import tkinter as tk
from tkinter import messagebox


class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Todo List Application")
        self.geometry("400x300")

        self.todo_list = []
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self, width=380, height=280, bg="white")
        main_frame.pack(pady=10, padx=10, fill="both", expand=True)
        self.title = tk.Label(main_frame, text="Todo List", font=("Arial", 16), bg="white")
        self.title.pack(pady=10)
        self.todo_entry = tk.Entry(main_frame)
        self.todo_entry.pack(pady=10, padx=10, fill="x")
        self.add_button = tk.Button(main_frame, text="Add Todo", command=self.add_todo)
        self.add_button.pack(pady=10, padx=10)
        self.todo_listbox = tk.Listbox(main_frame)
        self.todo_listbox.pack(pady=10, padx=10, expand=False )
        self.todo_listbox.bind("<Double-Button-1>", self.remove_todo)
        self.todo_listbox.bind("<Delete>", self.remove_todo)
        self.todo_listbox.bind("<Return>", self.remove_todo)
        self.todo_listbox.bind("<BackSpace>", self.remove_todo)
        self.todo_listbox.bind("<Button-3>", self.show_context_menu)
        self.context_menu = tk.Menu(self.todo_listbox, tearoff=0)
        self.context_menu.add_command(label="Remove Todo", command=self.remove_todo)
        self.context_menu.add_command(label="Clear All Todos", command=self.clear_todos)
    def add_todo(self):
        todo_text = self.todo_entry.get().strip()
        if todo_text:
            self.todo_list.append(todo_text)
            self.todo_listbox.insert(tk.END, todo_text)
            self.todo_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Todo cannot be empty!")
    def remove_todo(self, event=None):
        selected_indices = self.todo_listbox.curselection()
        if selected_indices:
            for index in reversed(selected_indices):
                self.todo_listbox.delete(index)
                del self.todo_list[index]
        else:
            messagebox.showwarning("Warning", "No todo selected!")
    def clear_todos(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all todos?"):
            self.todo_listbox.delete(0,tk.END)
            self.todo_list.clear()
    def show_context_menu(self, event):
        try:
            self.todo_listbox.selection_set(self.todo_listbox.nearest(event.y))
            self.context_menu.post(event.x_root, event.y_root)
        except Exception as e:
            print(f"Error showing context menu: {e}")
if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()