import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False , False)


display = tk.Entry (
    root,
    font=("Arial", 30 ), 
    bd=10,
    relief=tk.RIDGE,
    justify="right"
)

display.pack(fill="both", ipadx=8 , pady=20 , padx=10)



buttons_frame = tk.Frame(root)
buttons_frame.pack()

button_7 = tk.Button(
    buttons_frame,
    text="7",
    font=("Arial", 20),
    width=5,
    height=2
)
button_7.grid(row=0, column=0, padx=5, pady=5)



button_8 = tk.Button(
    buttons_frame,
    text="8",
    font=("Arial", 20),
    width=5,
    height=2
)
button_8.grid(row=0, column=1, padx=5, pady=5)

button_9 = tk.Button(
    buttons_frame,
    text="9",
    font=("Arial", 20),
    width=5,
    height=2
)
button_9.grid(row=0, column=2, padx=5, pady=5)

button_divide = tk.Button(
    buttons_frame,
    text="/",
    font=("Arial", 20),
    width=5,
    height=2
)
button_divide.grid(row=0, column=3, padx=5, pady=5)



button_4 = tk.Button(
    buttons_frame,
    text="4",
    font=("Arial", 20),
    width=5,
    height=2
)
button_4.grid(row=1, column=0, padx=5, pady=5)


button_5 = tk.Button(
    buttons_frame,
    text="5",
    font=("Arial", 20),
    width=5,
    height=2
)
button_5.grid(row=1, column=1, padx=5, pady=5)


button_6 = tk.Button(
    buttons_frame,
    text="6",
    font=("Arial", 20),
    width=5,
    height=2
)
button_6.grid(row=1, column=2, padx=5, pady=5)

button_multiply = tk.Button(
    buttons_frame,
    text="*",
    font=("Arial", 20),
    width=5,
    height=2
)
button_multiply.grid(row=1, column=3, padx=5, pady=5)


button_1 = tk.Button(
    buttons_frame,
    text="1",
    font=("Arial", 20),
    width=5,
    height=2
)
button_1.grid(row=2, column=0, padx=5, pady=5)


button_2 = tk.Button(
    buttons_frame,
    text="2",
    font=("Arial", 20),
    width=5,
    height=2
)
button_2.grid(row=2, column=1, padx=5, pady=5)


button_3 = tk.Button(
    buttons_frame,
    text="3",
    font=("Arial", 20),
    width=5,
    height=2
)
button_3.grid(row=2, column=2, padx=5, pady=5)


button_minus = tk.Button(
    buttons_frame,
    text="-",
    font=("Arial", 20),
    width=5,
    height=2
)
button_minus.grid(row=2, column=3, padx=5, pady=5)


button_0 = tk.Button(
    buttons_frame,
    text="0",
    font=("Arial", 20),
    width=5,
    height=2
)
button_0.grid(row=3, column=0, padx=5, pady=5)


button_clear = tk.Button(
    buttons_frame,
    text="C",
    font=("Arial", 20),
    width=5,
    height=2
)
button_clear.grid(row=3, column=1, padx=5, pady=5)


button_equals = tk.Button(
    buttons_frame,
    text="=",
    font=("Arial", 20),
    width=5,
    height=2
)
button_equals.grid(row=3, column=2, padx=5, pady=5)




button_plus = tk.Button(
    buttons_frame,
    text="+",
    font=("Arial", 20),
    width=5,
    height=2
)
button_plus.grid(row=3, column=3, padx=5, pady=5)



root.mainloop()