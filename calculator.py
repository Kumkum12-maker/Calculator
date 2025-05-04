import tkinter as tk

#Calculatoe Logic
def press(key):
    if display.get() in ["Error", "Error: Divide by 0"]:
        display.delete(0, tk.END)
    display.insert(tk.END, key)

def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def evaluate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Divide by 0")
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

#GUI Setup
root = tk.Tk()
root.title("Calculator")
root.geometry("340x500")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10, sticky="nsew")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+']
]

all_buttons = []

for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        btn = tk.Button(root, text=char, font=("Arial", 18),
                        command=lambda ch=char: press(ch))
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
        all_buttons.append(btn)

# Clear button
clear_btn = tk.Button(root, text='C', font=("Arial", 18), command=clear)
clear_btn.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

# Backspace button
backspace_btn = tk.Button(root, text='⌫', font=("Arial", 18), command=backspace)
backspace_btn.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

# Equal button
equal_btn = tk.Button(root, text='=', font=("Arial", 18), command=evaluate)
equal_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Theme toggle button
toggle_theme_btn = tk.Button(root, text='🌗 Theme', font=("Arial", 14), command=lambda: toggle_theme())
toggle_theme_btn.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Theme Settings
light_theme = {
    "bg": "#ffffff",
    "fg": "#000000",
    "btn_bg": "#f0f0f0",
    "btn_fg": "#000000",
    "special_btn_bg": "#ff9500",
    "equal_btn_bg": "#34c759",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000"
}

dark_theme = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "btn_bg": "#333333",
    "btn_fg": "#ffffff",
    "special_btn_bg": "#ff9500",
    "equal_btn_bg": "#30d158",
    "entry_bg": "#2c2c2e",
    "entry_fg": "#ffffff"
}

theme = dark_theme  # Default start theme

def toggle_theme():
    global theme
    theme = dark_theme if theme == light_theme else light_theme
    apply_theme()

def apply_theme():
    root.configure(bg=theme["bg"])
    display.configure(bg=theme["entry_bg"], fg=theme["entry_fg"])
    for btn in all_buttons:
        btn.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])
    clear_btn.configure(bg=theme["special_btn_bg"], fg="white")
    equal_btn.configure(bg=theme["equal_btn_bg"], fg="white")
    backspace_btn.configure(bg=theme["special_btn_bg"], fg="white")
    toggle_theme_btn.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])

# Final Layout Setup
for i in range(7):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

apply_theme()
root.mainloop()
