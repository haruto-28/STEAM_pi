import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Raspberry Pi Button")

# ボタンがクリックされた時の動作を定義
def on_button_click():
    print("Button clicked!")

# ボタンの作成
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)

# メインループの開始
root.mainloop()