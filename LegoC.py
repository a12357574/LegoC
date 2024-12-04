import tkinter as tk
from tkinter import scrolledtext


# Enum-like class for Token Types
class TokenType:
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    INTEGER_LITERAL = 'INTEGER_LITERAL'
    FLOAT_LITERAL = 'FLOAT_LITERAL'
    STRING_LITERAL = 'STRING_LITERAL'
    OPERATOR = 'OPERATOR'
    PUNCTUATOR = 'PUNCTUATOR'
    ERROR = 'ERROR'


# Token class to hold the token type and value
class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value


# LexicalAnalyzer class to tokenize the input source code
class LexicalAnalyzer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.length = len(source_code)
        self.keywords = {
            "Build", "Destroy", "Pane", "Link", "Display", "Rebrick", "Broke", "Change", "Con",
            "Const", "Create", "Def", "Do", "Flip", "Ifsnap", "Piece", "Put", "Revoid", "Stable",
            "Set", "Snap", "Snapif", "Subs", "While", "Wobble"
        }
        self.single_operators = {'+', '-', '*', '/', '%', '=', '<', '>', '!', '~'}
        self.punctuators = {';', ',', '(', ')', '{', '}'}

    def is_whitespace(self, c):
        return c in ' \t\n\r'

    def is_alpha(self, c):
        return c.isalpha()

    def is_digit(self, c):
        return c.isdigit()

    def is_alphanumeric(self, c):
        return c.isalnum()

    def tokenize(self):
        tokens = []
        errors = []

        while self.position < self.length:
            current_char = self.source_code[self.position]

            # Skip whitespaces
            if self.is_whitespace(current_char):
                self.position += 1
                continue

            # Handle keywords and identifiers
            if self.is_alpha(current_char):
                start = self.position
                while (self.position < self.length and
                       (self.is_alphanumeric(self.source_code[self.position]) or self.source_code[self.position] == '_')):
                    self.position += 1
                word = self.source_code[start:self.position]
                if word in self.keywords:
                    tokens.append(Token(TokenType.KEYWORD, word))
                elif len(word) > 20 or not word[0].islower():
                    errors.append(f"Invalid identifier '{word}' at position {start}.")
                    tokens.append(Token(TokenType.ERROR, word))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, word))
                continue

            # Handle numeric literals
            if self.is_digit(current_char):
                start = self.position
                while self.position < self.length and self.is_digit(self.source_code[self.position]):
                    self.position += 1
                tokens.append(Token(TokenType.INTEGER_LITERAL, self.source_code[start:self.position]))
                continue

            # Handle operators
            if current_char in self.single_operators:
                next_char = self.source_code[self.position + 1] if self.position + 1 < self.length else ''
                if next_char == current_char:
                    errors.append(f"Invalid operator sequence '{current_char}{next_char}' at position {self.position}.")
                    tokens.append(Token(TokenType.ERROR, current_char + next_char))
                    self.position += 2
                else:
                    tokens.append(Token(TokenType.OPERATOR, current_char))
                    self.position += 1
                continue

            # Handle punctuators
            if current_char in self.punctuators:
                tokens.append(Token(TokenType.PUNCTUATOR, current_char))
                self.position += 1
                continue

            # Handle unknown characters
            errors.append(f"Unrecognized character '{current_char}' at position {self.position}.")
            tokens.append(Token(TokenType.ERROR, current_char))
            self.position += 1

        return tokens, errors


# GUI components and functions
class TextWithLineNumbers(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.line_numbers = tk.Text(self, width=4, padx=3, takefocus=0, border=0, background="lightgray", state="disabled", wrap="none")
        self.line_numbers.pack(side="left", fill="y")

        self.text = scrolledtext.ScrolledText(self, wrap="none")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<KeyPress>", self._update_line_numbers)
        self.text.bind("<MouseWheel>", self._update_line_numbers)
        self.text.bind("<ButtonRelease>", self._update_line_numbers)
        self.text.bind("<Configure>", self._update_line_numbers)

    def _update_line_numbers(self, event=None):
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", "end")

        lines = self.text.index("end-1c").split(".")[0]
        line_numbers = "\n".join(str(i) for i in range(1, int(lines) + 1))
        self.line_numbers.insert("1.0", line_numbers)

        self.line_numbers.config(state="disabled")
        self.line_numbers.yview_moveto(self.text.yview()[0])


def update_analysis(event=None):
    source_code = text_with_line_numbers.text.get("1.0", "end-1c")
    lexer = LexicalAnalyzer(source_code)
    tokens, errors = lexer.tokenize()

    lexeme_text.delete("1.0", "end")
    token_text.delete("1.0", "end")
    error_text.delete("1.0", "end")

    for token in tokens:
        lexeme_text.insert(tk.END, f"{token.value}\n")
        token_text.insert(tk.END, f"{token.type}\n")

    if errors:
        for error in errors:
            error_text.insert(tk.END, error + "\n")
    else:
        error_text.insert(tk.END, "No errors detected.\n")


root = tk.Tk()
root.title("Lego-C Code Analyzer")

input_frame = tk.Frame(root)
input_frame.pack(fill=tk.BOTH, pady=5)

label = tk.Label(input_frame, text="Enter Lego-C code:")
label.pack(side="top", anchor="w")

text_with_line_numbers = TextWithLineNumbers(input_frame)
text_with_line_numbers.pack(side="top", fill="both", expand=True, padx=5, pady=5)

output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, pady=5)

lexeme_label = tk.Label(output_frame, text="Lexemes:")
lexeme_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

lexeme_text = tk.Text(output_frame, width=25, height=10)
lexeme_text.grid(row=1, column=0, padx=5, pady=5)

token_label = tk.Label(output_frame, text="Tokens:")
token_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

token_text = tk.Text(output_frame, width=25, height=10)
token_text.grid(row=1, column=1, padx=5, pady=5)

error_label = tk.Label(output_frame, text="Errors:")
error_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

error_text = tk.Text(output_frame, width=35, height=10)
error_text.grid(row=1, column=2, padx=5, pady=5)

text_with_line_numbers.text.bind("<KeyRelease>", update_analysis)

root.mainloop()
