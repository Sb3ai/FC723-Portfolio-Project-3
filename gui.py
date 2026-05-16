#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:53:22 2026

@author: nasserali
"""
# This part is coded by nasser / My partner



# I have finished the gui - Nasser
import re
import tkinter as tk
import math 
import ast

# Import basic operations from the backend logic file.
from backend.basic_logic import (
    add,
    divide,
    multiply,
    percentage,
    power,
    square,
    square_root,
    subtract,
)

# Import scientific operations from the scientific backend file.
from backend.scientific_math import (
    arccosine,
    arcsine,
    arctangent,
    cosine,
    factorial,
    ln,
    log,
    sine,
    tangent,
)
# Import validation functions so input is checked before calculations.
from backend.validate import validate_one_number, validate_two_numbers


class RoundButton(tk.Canvas):
    """A rounded calculator button drawn on a Tkinter canvas."""

    def __init__(self, parent, text, bg_color, fg_color, command):
        super().__init__(
            parent,
            width=76,
            height=62,
            bg="#000000",
            highlightthickness=0,
            bd=0,
        )

        self.text = text
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.command = command

        # Draw the button and connect mouse events to it.
        self.draw_button(bg_color)
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def draw_button(self, color):
        """Draw the rounded rectangle and the button text."""
        self.delete("all")
        self.create_round_rectangle(4, 4, 72, 58, radius=28, fill=color, outline=color)
        self.create_text(
            38,
            31,
            text=self.text,
            fill=self.fg_color,
            font=("Arial", 15, "bold"),
        )

    def create_round_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        """Create a rounded rectangle shape using canvas points."""
        points = [
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_click(self, event):
        """Run the button command when the button is clicked."""
        self.command()

    def on_enter(self, event):
        """Lighten the button when the mouse moves over it."""
        self.draw_button(self.lighten_color(self.bg_color))

    def on_leave(self, event):
        """Return the button to its normal colour."""
        self.draw_button(self.bg_color)

    def lighten_color(self, color):
        """Lighten a hex colour for a simple hover effect."""
        red = min(int(color[1:3], 16) + 22, 255)
        green = min(int(color[3:5], 16) + 22, 255)
        blue = min(int(color[5:7], 16) + 22, 255)
        return f"#{red:02x}{green:02x}{blue:02x}"


class CalculatorGUI:
    """Main calculator window and all user interaction."""

    def __init__(self):
        # Main window settings
        self.root = tk.Tk()
        self.root.title("FC723 Scientific Calculator")
        self.root.geometry("440x760")
        self.root.minsize(420, 720)
        self.root.configure(bg="#000000")

        # Variables used by the calculator
        self.display_text = tk.StringVar(value="0")
        self.previous_answer = ""
        self.history = []
        self.angle_mode = "DEG"
        self.mode_text = tk.StringVar(value="Mode: Degree")

        self.create_display()
        self.create_buttons()
        self.create_history()
        self.bind_keyboard()

    def create_display(self):
        """Create the read-only calculator display."""
        display_frame = tk.Frame(self.root, bg="#000000")
        display_frame.pack(fill="x", padx=20, pady=(24, 8))

        title_label = tk.Label(
            display_frame,
            text="Advanced Scientific Calculator",
            font=("Arial", 13),
            bg="#000000",
            fg="#8e8e93",
            anchor="w",
        )
        title_label.pack(fill="x", pady=(0, 14))
        self.mode_label = tk.Label(
            display_frame,
            textvariable=self.mode_text,
            font=("Arial", 11),
            bg="#000000",
            fg="#ff9f0a",
            anchor="w",
        )
        self.mode_label.pack(fill="x", pady=(0, 8))

        self.display = tk.Label(
            display_frame,
            textvariable=self.display_text,
            font=("Arial", 46),
            bg="#000000",
            fg="white",
            anchor="e",
            padx=4,
            pady=8,
            relief="flat",
        )
        self.display.pack(fill="x")
    
    def add_function_to_display(self,function_name):
        current = self.display_text.get()
        
        if current == "0" or current == "Error":
            self.display_text.set(function_name + "(")
        else:
            self.display_text.set(current + function_name + "(")
    

    def set_angle_mode(self, mode):
        """Change between degree mode and radian mode."""
        self.angle_mode = mode
    
        if mode == "DEG":
            self.mode_text.set("Mode: Degree")
        else:
            self.mode_text.set("Mode: Radian")
    
    def evaluate_expression(self, expression):

        """Safely evaluate a calculator expression without using Python eval."""
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("xʸ", "**")
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("√", "sqrt")

    
        tree = ast.parse(expression, mode="eval")
        return self.evaluate_node(tree.body)
    

    def evaluate_node(self, node):
        """Evaluate only the math syntax allowed in this calculator."""
        if isinstance(node, ast.Constant):
            return float(node.value)
    
        if isinstance(node, ast.BinOp):
            left = self.evaluate_node(node.left)
            right = self.evaluate_node(node.right)
    
            if isinstance(node.op, ast.Add):
                return add(left, right)
            if isinstance(node.op, ast.Sub):
                return subtract(left, right)
            if isinstance(node.op, ast.Mult):
                return multiply(left, right)
            if isinstance(node.op, ast.Div):
                return divide(left, right)
            if isinstance(node.op, ast.Pow):
                return power(left, right)
    
        if isinstance(node, ast.UnaryOp):
            value = self.evaluate_node(node.operand)
    
            if isinstance(node.op, ast.UAdd):
                return value
            if isinstance(node.op, ast.USub):
                return -value
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Invalid function")
        
            function_name = node.func.id
            value = self.evaluate_node(node.args[0])
        
            functions = self.get_scientific_functions()
        
            if function_name in functions:
                return functions[function_name](value)
        
            raise ValueError("Invalid expression")
            
    def get_scientific_functions(self):
        """Return scientific functions depending on degree or radian mode."""
        if self.angle_mode == "RAD":
            return {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "asin": math.asin,
                "acos": math.acos,
                "atan": math.atan,
                "log": log,
                "ln": ln,
                "sqrt": square_root,
            }
        
        return {
            "sin": sine,
            "cos": cosine,
            "tan": tangent,
            "asin": arcsine,
            "acos": arccosine,
            "atan": arctangent,
            "log": log,
            "ln": ln,
            "sqrt": square_root,
        }

    def create_buttons(self):
        """Create all number, operation, and scientific buttons."""
        button_frame = tk.Frame(self.root, bg="#000000")
        button_frame.pack(fill="x", padx=18, pady=(4, 6))


        # Buttons are stored in a list of rows to make the layout easier to read.
        buttons = [
            ["C", "⌫", "DEG", "RAD", "÷"],
            ["sin", "cos", "tan", "π", "×"],
            ["asin", "acos", "atan", "(", "-"],
            ["log", "ln", "√", ")", "+"],
            ["7", "8", "9", "x²", "="],
            ["4", "5", "6", "xʸ", "Ans"],
            ["1", "2", "3", ".", "Hist"],
            ["0", "+/-", "%", "n!", "Exit"],
        ]

        for row_number, row in enumerate(buttons):
            button_frame.rowconfigure(row_number, weight=1)
            for column_number, button_text in enumerate(row):
                button_frame.columnconfigure(column_number, weight=1)

                button = RoundButton(
                    button_frame,
                    text=button_text,
                    command=lambda value=button_text: self.button_click(value),
                    bg_color=self.get_button_color(button_text),
                    fg_color=self.get_text_color(button_text),
                )
                button.grid(
                    row=row_number,
                    column=column_number,
                    padx=5,
                    pady=5,
                    sticky="nsew",
                )
    
    def create_history(self):
        """Create the calculation history area."""
        history_frame = tk.Frame(self.root, bg="#000000")
        history_frame.pack(fill="both", expand=True, padx=20, pady=(8, 18))

        history_title = tk.Label(
            history_frame,
            text="Calculation History",
            font=("Arial", 12),
            bg="#000000",
            fg="#8e8e93",
            anchor="w",
        )
        history_title.pack(fill="x", pady=(0, 5))

        self.history_box = tk.Listbox(
            history_frame,
            font=("Arial", 11),
            bg="#1c1c1e",
            fg="#f2f2f7",
            bd=0,
            height=7,
            activestyle="none",
            highlightthickness=0,
            selectbackground="#ff9f0a",
            selectforeground="white",
        )
    
        # Double-clicking a previous calculation puts its answer on the display.
        self.history_box.pack(side="left", fill="both", expand=True)
        self.history_box.bind("<Double-Button-1>", self.use_history_answer)

    def get_button_color(self, button_text):
        """Choose button colours to make the GUI look like a real calculator."""
        orange_buttons = {
            "+",
            "-",
            "×",
            "÷",
            "=",
        }

        grey_buttons = {
            "C",
            "⌫",
            "+/-",
            "%",
        }

        scientific_buttons = {
            "√",
            "x²",
            "xʸ",
            "n!",
            "sin",
            "cos",
            "tan",
            "asin",
            "acos",
            "atan",
            "log",
            "ln",
            "π",
            "DEG",
            "RAD",
            "(",
            ")",
            "Ans",
            "Hist",
            "Exit",
        }

        if button_text in orange_buttons:
            return "#ff9f0a"
        if button_text in grey_buttons:
            return "#a5a5a5"
        if button_text in scientific_buttons:
            return "#505050"
        return "#333333"

    def get_text_color(self, button_text):
        """Choose text colours that contrast with each button colour."""
        if self.get_button_color(button_text) == "#a5a5a5":
            return "#000000"
        return "white"
    
    def bind_keyboard(self):
        """Allow the calculator to be controlled by the keyboard."""
        self.root.bind("<Key>", self.keyboard_input)
        self.root.bind("<Return>", lambda event: self.calculate_result())
        self.root.bind("<KP_Enter>", lambda event: self.calculate_result())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Escape>", lambda event: self.clear_display())

    def keyboard_input(self, event):
        """Handle keyboard numbers and operators."""
        key = event.char

        if key in "0123456789.":
            
            self.add_to_display(key)
        elif key in "+-*/^":
            # Keyboard symbols are converted later to the display symbols.
            self.add_operator(key)
        elif key in "()":
            self.add_to_display(key)
        elif key == "=":
            self.calculate_result()

    def button_click(self, value):
        """Send each button to the correct calculator action."""
        # This if/elif structure connects every visible button to a function.
        if value == "C":
            self.clear_display()
        elif value == "⌫":
            self.backspace()
        elif value == "=":
            self.calculate_result()
        elif value == "Exit":
            self.root.destroy()
        elif value == "Hist":
            self.clear_history()
        elif value == "Ans":
            self.add_to_display(self.previous_answer)
        elif value == "+/-":
            self.change_sign()
        elif value in ["+", "-", "×", "÷", "xʸ"]:
            self.add_operator(value)
        elif value == "%":
            self.calculate_percentage()
        elif value == "√":
            self.add_function_to_display("√")
        elif value == "x²":
            self.calculate_single_input("x²", square)
        elif value == "n!":
            self.calculate_single_input("!", factorial)
        elif value in ["sin", "cos", "tan", "asin", "acos", "atan", "log", "ln"]:
            self.add_function_to_display(value)
        elif value == "DEG":
            self.set_angle_mode("DEG")
        elif value == "RAD":
            self.set_angle_mode("RAD")
        elif value == "π":
            self.add_to_display("π")
        elif value in ["(",")"]:
            self.add_to_display(value)
        else:
            self.add_to_display(value)

    def add_to_display(self, value):
        """Add a number or decimal point to the display."""
        
        current = self.display_text.get()

        if current == "Error":
            self.display_text.set("")
            current = ""

        if current == "0" and value != ".":
            self.display_text.set(value)
        elif current == "0" and value == ".":
            self.display_text.set("0.")
        else:
            self.display_text.set(current + value)

    def add_operator(self, operator):
        """Add an operator while preventing two operators in a row."""
        # Convert keyboard operators to the symbols used on the GUI.
        operator = operator.replace("*", "×").replace("/", "÷").replace("^", "xʸ")
        current = self.display_text.get()

        if current == "" and operator == "-":
            self.display_text.set("-")
            return

        if current == "" or current == "Error":
            return
        # If the user presses two operators, replace the old one with the new one.
        if self.ends_with_operator(current):
            current = self.remove_last_operator(current)
            self.display_text.set(current + operator)
        else:
            self.display_text.set(current + operator)

    def ends_with_operator(self, text):
        """Check if the display already ends with an operator."""
        return text.endswith(("+", "-", "×", "÷", "xʸ"))

    def remove_last_operator(self, text):
        """Remove the final operator before replacing it with another one."""
        if text.endswith("xʸ"):
            return text[:-2]
        return text[:-1]

    def backspace(self):
        """Remove the last character from the display."""
        current = self.display_text.get()
        if current != "Error":
            new_value = current[:-1]
            if new_value == "":
                new_value = "0"
            self.display_text.set(new_value)

    def clear_display(self):
        """Clear only the current display."""
        self.display_text.set("0")

    def clear_history(self):
        """Clear the history list."""
        self.history.clear()
        self.history_box.delete(0, tk.END)

    def change_sign(self):
        """Change the current number from positive to negative or back again."""
        current = self.display_text.get()
        if current.startswith("-"):
            self.display_text.set(current[1:])
        elif current not in ["", "0", "Error"]:
            self.display_text.set("-" + current)

    def calculate_result(self):
        """Calculate expressions such as 6+2, 9×3, 10÷2, and 2xʸ3."""
        expression = self.display_text.get()

        try:
            result = self.evaluate_expression(expression)
            self.show_result(expression, result)

        except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
            self.display_text.set("Error")

    def split_expression(self, expression):
        """
        Split a two-number calculation into number, operator, number.

        A regular expression is used so negative numbers like -5+2 still work.
        """
        number = r"-?(?:\d+(?:\.\d*)?|\.\d+)"
        pattern = rf"^\s*({number})\s*(\+|-|×|÷|xʸ)\s*({number})\s*$"
        match = re.match(pattern, expression)

        if not match:
            raise ValueError("Invalid expression")

        return match.group(1), match.group(2), match.group(3)

    def calculate_single_input(self, symbol, operation):
        """Calculate operations that only need one number."""
        expression = self.display_text.get()

        try:
            value = validate_one_number(expression)
            result = operation(value)

            if symbol == "!":
                history_text = f"{self.format_number(value)}! = {self.format_number(result)}"
            else:
                history_text = f"{symbol}({self.format_number(value)}) = {self.format_number(result)}"

            self.display_result(result)
            self.add_history(history_text)

        except (ValueError, OverflowError):
            self.display_text.set("Error")

    def calculate_percentage(self):
        """Convert the current number into a percentage."""
        expression = self.display_text.get()

        try:
            value = validate_one_number(expression)
            result = percentage(value)
            self.display_result(result)
            self.add_history(f"{self.format_number(value)}% = {self.format_number(result)}")

        except (ValueError, OverflowError):
            self.display_text.set("Error")

    def calculate_scientific(self, operation_name):
        """Calculate scientific operations using the scientific backend file."""
        expression = self.display_text.get()

        operations = {
            # Dictionary links button names to the matching backend functions.
            "sin": sine,
            "cos": cosine,
            "tan": tangent,
            "asin": arcsine,
            "acos": arccosine,
            "atan": arctangent,
            "log": log,
            "ln": ln,
        }

        try:
            value = validate_one_number(expression)
            result = operations[operation_name](value)
            self.display_result(result)
            self.add_history(
                f"{operation_name}({self.format_number(value)}) = {self.format_number(result)}"
            )

        except (ValueError, OverflowError):
            self.display_text.set("Error")

    def display_result(self, result):
        """Show the result and store it as the previous answer."""
        result_text = self.format_number(result)
        self.display_text.set(result_text)
        self.previous_answer = result_text

    def show_result(self, expression, result):
        """Show a two-number calculation result and add it to history."""
        self.display_result(result)
        self.add_history(f"{expression} = {self.format_number(result)}")

    def add_history(self, history_text):
        """Save a calculation in the on-screen history box."""
        self.history.append(history_text)
        self.history_box.insert(tk.END, history_text)
        self.history_box.see(tk.END)

    def use_history_answer(self, event):
        """Double-clicking a history item puts its answer back on the display."""
        selected = self.history_box.curselection()

        if selected:
            history_text = self.history_box.get(selected[0])
            # The answer is always after the equals sign in the history text.
            answer = history_text.split("=")[-1].strip()
            self.display_text.set(answer)

    def format_number(self, value):
        """Format results and show common radian answers using π."""
        if self.angle_mode == "RAD":
            pi_text = self.format_pi_result(value)
            if pi_text is not None:
                return pi_text
    
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
    
        return str(round(value, 10))
    def format_pi_result(self, value):
        """Convert common radian answers into π format."""
        pi = math.pi
    
        common_values = {
            0: "0",
            pi / 6: "π/6",
            pi / 4: "π/4",
            pi / 3: "π/3",
            pi / 2: "π/2",
            pi: "π",
            2 * pi: "2π",
            -pi / 6: "-π/6",
            -pi / 4: "-π/4",
            -pi / 3: "-π/3",
            -pi / 2: "-π/2",
            -pi: "-π",
            -2 * pi: "-2π",
        }
    
        for number, text in common_values.items():
            if abs(value - number) < 0.000001:
                return text
    
        return None

    def run(self):
        """Start the Tkinter event loop."""
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()