import tkinter as tk
from tkinter import scrolledtext
import re

# Enum-like class for Token Types
class TokenType:
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    INTEGER_LITERAL = 'Linklit'
    FLOAT_LITERAL = 'Bubblelit'
    STRING_LITERAL = 'Piecelit'
    OPERATOR = 'OPERATOR'
    PUNCTUATOR = 'PUNCTUATOR'
    UNKNOWN = 'UNKNOWN'

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value


class LexicalAnalyzer:
    def __init__(self, source_code):
        self.input = source_code
        self.position = 0
        self.keywords = {
            "Base": "delim7",
            "Bubble": "delim3",
            "Build": "delim1",
            "Broke": "delim8",
            "Change": "delim5",
            "Con": "delim8",
            "Const": "delim2",
            "Create": "delim5",
            "Def": "delim9",
            "Destroy": "delim2",
            "Display": "delim4",
            "Do": "delim6",
            "Flip": "delim8",
            "Ifsnap": "delim6",
            "Link": "delim3",
            "Pane": "delim5",
            "Piece": "delim3",
            "Put": "delim5",
            "Rebrick": "delim10",
            "Revoid": "delim8",
            "Stable": "delim8",
            "Set": "delim6",
            "Snap": "delim6",
            "Snapif": "delim5",
            "Subs": "delim3",
            "While": "delim5",
            "Wobble": "delim8",
        }

        self.symbols = {
            "=": "delim11",
            "==": "delim13",
            "+": "delim12",
            "+=": "delim12",
            "-": "delim12",
            "-=": "delim12",
            "*": "delim12",
            "*=": "delim12",
            "/": "delim12",
            "/=": "delim12",
            "%": "delim12",
            "%=": "delim12",
            "!!": "delim12",
            "!=": "delim11",
            "<": "delim11",
            "<=": "delim11",
            ">": "delim11",
            ">=": "delim11",
            "&&": "delim12",
            "||": "delim12",
            "{": "delim14",
            "}": "delim14",
            "(": "delim14",
            ")": "delim14",
            "[": "delim14",
            "]": "delim14",
            ";": "delim3",
        }

        self.delimiters = {
            "delim1": [" ", "\n", "\t"],
            "delim2": [None],
            "delim3": [" "],
            "delim4": [" ", '"'],
            "delim5": [" ", "("],
            "delim6": [" ", "{"],
            "delim7": [" ", ":", "\n", "+"],
            "delim8": [";"],
            "delim9": [":"],
            "delim10": [";", " "],
            "delim11": [" ", *list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")],
            "delim12": [" ", *list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), "("],
            "delim13": [" ", *list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")],
            "delim14": [" ", "\n", "{", *list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")],
            "identifier_delim": [" ", "=", ";", ",", "{", "}", "(", ")"],
            "piece_delim": ["}", ";", ")", "~", "=", " "],
        }


    def is_whitespace(self, c):
        return c in self.delimiters["delim1"]

    def is_identifier_boundary(self, c):
        return c in self.delimiters["identifier_delim"]

    def is_piece_boundary(self, c):
        return c in self.delimiters["piece_delim"]

    def get_next_word(self):
        start = self.position
        while self.position < len(self.input) and self.input[self.position].isalnum():
            self.position += 1
        return self.input[start:self.position]

    def tokenize(self):
        tokens = []
        lexemes = []
        self.position = 0  # Reset position for each analysis

        while self.position < len(self.input):
            current_char = self.input[self.position]

            if self.is_whitespace(current_char):
                tokens.append(Token(TokenType.UNKNOWN, "space"))
                lexemes.append("space")
                self.position += 1
                continue

            # Check for keywords
            word = self.get_next_word()
            if word in self.keywords:
                tokens.append(Token(TokenType.KEYWORD, word))
                lexemes.append(word)

            # Check for symbols
            elif word in self.symbols:
                tokens.append(Token(TokenType.OPERATOR, word))
                lexemes.append(word)

            # Check for identifiers
            if current_char.isalpha():
                start = self.position
                while self.position < len(self.input) and not self.is_identifier_boundary(self.input[self.position]):
                    self.position += 1
                identifier = self.input[start:self.position]
                tokens.append(Token(TokenType.IDENTIFIER, identifier))
                lexemes.append(identifier)
                continue

            # Check for integers or floats
            if current_char.isdigit() or (current_char == '.' and self.input[self.position + 1].isdigit()):
                start = self.position
                is_float = False
                while self.position < len(self.input) and (self.input[self.position].isdigit() or self.input[self.position] == '.'):
                    if self.input[self.position] == '.':
                        is_float = True
                    self.position += 1
                literal = self.input[start:self.position]
                token_type = TokenType.FLOAT_LITERAL if is_float else TokenType.INTEGER_LITERAL
                tokens.append(Token(token_type, literal))
                lexemes.append(literal)
                continue

            # Check for string literals (Piecelit)
            if current_char == '"':  # Piecelit starts with a double quote
                start = self.position
                self.position += 1
                while self.position < len(self.input) and not self.is_piece_boundary(self.input[self.position]):
                    self.position += 1
                if self.position >= len(self.input):  # Missing closing
                    tokens.append(Token(TokenType.UNKNOWN, self.input[start:]))
                    lexemes.append(self.input[start:])
                else:
                    self.position += 1  # Include the boundary
                    piecelit = self.input[start:self.position]
                    tokens.append(Token(TokenType.STRING_LITERAL, piecelit))
                    lexemes.append(piecelit)
                continue

            # Unknown or other characters
            else:
                tokens.append(Token(TokenType.UNKNOWN, current_char))
                lexemes.append(current_char)
                self.position += 1

        return tokens, lexemes


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


def validate_syntax(tokens):
    errors = []
    if not tokens:
        errors.append("No code provided.")
        return errors
    if tokens[0].value != "Build":
        errors.append("Program must start with 'Build'.")
    if tokens[-1].value != "Destroy":
        errors.append("Program must end with 'Destroy'.")
    return errors


def update_analysis(event=None):
    source_code = text_with_line_numbers.text.get("1.0", "end-1c")
    lexer = LexicalAnalyzer(source_code)
    tokens, lexemes = lexer.tokenize()

    lexeme_text.delete("1.0", "end")
    token_text.delete("1.0", "end")
    error_text.delete("1.0", "end")

    for lexeme in lexemes:
        lexeme_text.insert(tk.END, f"{lexeme}\n")

    for token in tokens:
        token_text.insert(tk.END, f"{token.value}\n")

    errors = validate_syntax(tokens)
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
text_with_line_numbers.pack(side="top", fill="both", expand=True)
text_with_line_numbers.text.bind("<KeyRelease>", update_analysis)

output_frame = tk.Frame(root)
output_frame.pack(fill=tk.BOTH, pady=5)

lexeme_label = tk.Label(output_frame, text="Lexemes:")
lexeme_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

lexeme_text = tk.Text(output_frame, width=35, height=10)
lexeme_text.grid(row=1, column=0, padx=5, pady=5)

token_label = tk.Label(output_frame, text="Tokens:")
token_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

token_text = tk.Text(output_frame, width=35, height=10)
token_text.grid(row=1, column=1, padx=5, pady=5)

error_label = tk.Label(output_frame, text="Errors:")
error_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")

error_text = tk.Text(output_frame, width=35, height=10)
error_text.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
