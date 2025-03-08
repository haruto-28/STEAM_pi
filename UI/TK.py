import tkinter as tk
from tkinter import messagebox

class NumericInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Numeric Input Checker")
        self.root.geometry("900x500")

        self.input_value = tk.StringVar()

        # エントリーボックスの作成
        entry_label = tk.Label(root, text="Enter numbers:", font=("Helvetica", 18))
        entry_label.pack(pady=10)
        entry = tk.Entry(root, textvariable=self.input_value, font=("Helvetica", 18), justify='center')
        entry.pack(pady=10)

        # 数字ボタンの作成
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        for i in range(10):
            button = tk.Button(button_frame, text=str(i), font=("Helvetica", 18), width=4, height=2, 
                               command=lambda num=i: self.append_number(num))
            button.grid(row=i//3, column=i%3, padx=5, pady=5)

        # チェックボタンの作成
        check_button = tk.Button(root, text="Check", command=self.check_input, font=("Helvetica", 18))
        check_button.pack(pady=20)

    def append_number(self, num):
        current_value = self.input_value.get()
        self.input_value.set(current_value + str(num))

    def check_input(self):
        entered_text = self.input_value.get()
        if entered_text == "2012":
            messagebox.showinfo("Result", "ok")
            self.root.quit()  # プログラムを終了させる
        else:
            messagebox.showerror("Result", "Incorrect input")

# メインウィンドウの作成
root = tk.Tk()
app = NumericInputApp(root)

# メインループの実行
root.mainloop()