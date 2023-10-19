import tkinter as tk
from tkinter import ttk

class LoginWindow:
    def __init__(self):
        # 创建图形窗口
        self.root = tk.Tk()
        self.root.title("登录窗口")
        self.root.geometry("300x240")

        # 添加用户名标签和文本框（垂直布局）
        username_label = tk.Label(self.root, text="用户名：", font=("Arial", 12))
        username_label.grid(row=0, column=0, padx=5, pady=10)
        self.username_entry = tk.Entry(self.root, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1, padx=5, pady=10)

        # 添加密码标签和文本框（垂直布局）
        password_label = tk.Label(self.root, text="密码：", font=("Arial", 12))
        password_label.grid(row=1, column=0, padx=5, pady=10)
        self.password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, padx=5, pady=10)

        # 添加下拉列表（垂直布局）
        key_label = tk.Label(self.root, text="快捷键：", font=("Arial", 12))
        key_label.grid(row=2, column=0, padx=5, pady=10)
        shortcut_var = tk.StringVar(self.root)
        shortcut_var.set("Alt+Ctrl+E")
        shortcut_options = ["Alt+Ctrl+E", "Alt+Shift+A", "Ctrl+Shift+Z", "Alt+Space", "Ctrl+Alt+Space"]
        self.shortcut_dropdown = ttk.Combobox(self.root, textvariable=shortcut_var, values=shortcut_options, font=("Arial", 12))
        self.shortcut_dropdown.grid(row=2, column=1, padx=5, pady=10)

        # 添加单选按钮和文本框（垂直布局）
        self.radio_var = tk.StringVar(self.root, value="text_input")
        radio_label = tk.Label(self.root, text="选择输入类型：", font=("Arial", 12))
        radio_label.grid(row=3, column=0, padx=5, pady=10)
        text_radio = tk.Radiobutton(self.root, text="文字输入", variable=self.radio_var, value="text_input", font=("Arial", 12), command=self.enable_text_input)
        text_radio.grid(row=3, column=1, padx=2, pady=5, sticky=tk.W)
        file_radio = tk.Radiobutton(self.root, text="文件输入", variable=self.radio_var, value="file_input", font=("Arial", 12), command=self.enable_file_input)
        file_radio.grid(row=3, column=2, padx=2, pady=5, sticky=tk.W)

        self.text_entry = tk.Entry(self.root, font=("Arial", 12), state="normal")
        self.text_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=10)
        self.text_entry.insert(0, "请输入服务器URL")
        self.text_entry.bind("<FocusIn>", self.on_file_entry2_focus_in)
        self.text_entry.bind("<FocusOut>", self.on_file_entry2_focus_out)

        self.file_entry = tk.Entry(self.root, font=("Arial", 12), state="disabled")
        self.file_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=10)


        self.file_entry2 = tk.Entry(self.root, font=("Arial", 12), state="disabled")
        self.file_entry2.grid(row=7, column=0, columnspan=2, padx=5, pady=10)


        # 添加提交按钮
        submit_button = tk.Button(self.root, text="提交", command=self.on_submit, font=("Arial", 12))
        submit_button.grid(row=8, column=0, columnspan=2, pady=10)

        # 设置窗口背景颜色
        self.root.configure(bg="white")

        # 运行图形窗口主循环
        self.root.mainloop()

    def enable_text_input(self):
        self.text_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        self.text_entry.config(state="normal")
        self.file_entry.grid_forget()
        self.file_entry2.grid_forget()
        self.file_entry.config(state="disabled")
        self.file_entry2.config(state="disabled")

    def enable_file_input(self):
        self.text_entry.grid_forget()
        self.text_entry.config(state="disabled")
        self.file_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=10)
        self.file_entry.config(state="normal")
        self.file_entry2.grid(row=7, column=0, columnspan=2, padx=5, pady=10)
        self.file_entry2.config(state="normal")

        self.file_entry2.insert(0, "请输入accessKeySecret")
        self.file_entry.insert(0, "请输入accessKeyId")
        self.file_entry2.bind("<FocusIn>", self.on_file_entry2_focus_in)
        self.file_entry2.bind("<FocusOut>", self.on_file_entry2_focus_out)
        self.file_entry.bind("<FocusIn>", self.on_file_entry_focus_in)
        self.file_entry.bind("<FocusOut>", self.on_file_entry_focus_out)
    def on_text_entry_focus_in(self, event):
        if self.text_entry.get() == "请输入文字":
            self.text_entry.delete(0, tk.END)

    def on_text_entry_focus_out(self, event):
        if self.text_entry.get() == "":
            self.text_entry.insert(0, "请输入文字")

    def on_file_entry_focus_in(self, event):
        if self.file_entry.get() == "请输入文件路径":
            self.file_entry.delete(0, tk.END)

    def on_file_entry_focus_out(self, event):
        if self.file_entry.get() == "":
            self.file_entry.insert(0, "请输入文件路径")

    def on_file_entry2_focus_in(self, event):
        if self.file_entry2.get() == "请输入文件路径":
            self.file_entry2.delete(0, tk.END)

    def on_file_entry2_focus_out(self, event):
        if self.file_entry2.get() == "":
            self.file_entry2.insert(0, "请输入文件路径")
    def on_submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        shortcut = self.shortcut_dropdown.get()
        input_type = self.radio_var.get()
        text_input = self.text_entry.get()
        file_input = self.file_entry.get()

        print("Username:", username)
        print("Password:", password)
        print("Shortcut:", shortcut)
        print("Input Type:", input_type)
        print("Text Input:", text_input)
        print("File Input:", file_input)