from tkinter import Button, Frame, Label, StringVar, Tk

from calculator_engine import CalculatorError, calculate


COLORS = {
    "background": "#121212",
    "display": "#1F6F78",
    "button": "#F4F4F2",
    "button_text": "#111111",
    "operator": "#76ABAE",
    "operator_text": "#FFFFFF",
    "accent": "#FF9D3D",
    "accent_text": "#FFFFFF",
}


class CalculatorApp:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Calculadora")
        self.window.geometry("350x470")
        self.window.resizable(False, False)
        self.window.configure(background=COLORS["background"])

        self.expression = ""
        self.display_value = StringVar()

        self._build_layout()
        self._bind_keyboard()

    def run(self) -> None:
        self.window.mainloop()

    def _build_layout(self) -> None:
        display_frame = Frame(self.window, width=350, height=110, bg=COLORS["display"])
        display_frame.grid(row=0, column=0)
        display_frame.grid_propagate(False)

        body_frame = Frame(self.window, width=350, height=360, bg=COLORS["background"])
        body_frame.grid(row=1, column=0)
        body_frame.grid_propagate(False)

        display = Label(
            display_frame,
            textvariable=self.display_value,
            anchor="e",
            padx=24,
            font=("Arial", 28, "bold"),
            bg=COLORS["display"],
            fg="#FFFFFF",
        )
        display.place(x=0, y=0, width=350, height=110)

        buttons = [
            ("C", 0, 0, 1, self.clear, "accent"),
            ("⌫", 0, 1, 1, self.backspace, "accent"),
            ("%", 0, 2, 1, lambda: self.add_value("%"), "operator"),
            ("/", 0, 3, 1, lambda: self.add_value("/"), "operator"),
            ("7", 1, 0, 1, lambda: self.add_value("7"), "button"),
            ("8", 1, 1, 1, lambda: self.add_value("8"), "button"),
            ("9", 1, 2, 1, lambda: self.add_value("9"), "button"),
            ("*", 1, 3, 1, lambda: self.add_value("*"), "operator"),
            ("4", 2, 0, 1, lambda: self.add_value("4"), "button"),
            ("5", 2, 1, 1, lambda: self.add_value("5"), "button"),
            ("6", 2, 2, 1, lambda: self.add_value("6"), "button"),
            ("-", 2, 3, 1, lambda: self.add_value("-"), "operator"),
            ("1", 3, 0, 1, lambda: self.add_value("1"), "button"),
            ("2", 3, 1, 1, lambda: self.add_value("2"), "button"),
            ("3", 3, 2, 1, lambda: self.add_value("3"), "button"),
            ("+", 3, 3, 1, lambda: self.add_value("+"), "operator"),
            ("0", 4, 0, 2, lambda: self.add_value("0"), "button"),
            (".", 4, 2, 1, lambda: self.add_value("."), "button"),
            ("=", 4, 3, 1, self.calculate_result, "accent"),
        ]

        for text, row, column, colspan, command, style in buttons:
            self._create_button(body_frame, text, row, column, colspan, command, style)

    def _create_button(self, parent, text, row, column, colspan, command, style) -> None:
        width = 87.5 * colspan
        x_position = column * 87.5
        y_position = row * 72

        background = COLORS[style]
        foreground = COLORS.get(f"{style}_text", COLORS["button_text"])

        Button(
            parent,
            text=text,
            bg=background,
            fg=foreground,
            activebackground=background,
            activeforeground=foreground,
            font=("Arial", 18, "bold"),
            relief="flat",
            bd=0,
            command=command,
        ).place(x=x_position, y=y_position, width=width, height=72)

    def _bind_keyboard(self) -> None:
        self.window.bind("<Return>", lambda _event: self.calculate_result())
        self.window.bind("<BackSpace>", lambda _event: self.backspace())
        self.window.bind("<Escape>", lambda _event: self.clear())
        self.window.bind("<Key>", self._handle_keypress)

    def _handle_keypress(self, event) -> None:
        if event.char in "0123456789+-*/%.":
            self.add_value(event.char)

    def add_value(self, value: str) -> None:
        if self.display_value.get() == "Erro":
            self.expression = ""

        self.expression += value
        self.display_value.set(self.expression)

    def calculate_result(self) -> None:
        try:
            result = calculate(self.expression)
        except CalculatorError:
            self.display_value.set("Erro")
            self.expression = ""
            return

        self.expression = str(result)
        self.display_value.set(self.expression)

    def clear(self) -> None:
        self.expression = ""
        self.display_value.set("")

    def backspace(self) -> None:
        self.expression = self.expression[:-1]
        self.display_value.set(self.expression)


if __name__ == "__main__":
    CalculatorApp().run()
