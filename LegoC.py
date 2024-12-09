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
    UNKNOWN = 'UNKNOWN'

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

class LexicalAnalyzer:
    def __init__(self, source_code):
        self.input = source_code
        self.position = 0

        # Keywords with their delimiters
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

        # Operators and symbols with their delimiters
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
            "<=": "delim13",
            ">": "delim11",
            ">=": "delim13",
            "&&": "delim12",
            "||": "delim12",
            "{": "delim14",
            "}": "delim14",
            "(": "delim14",
            ")": "delim14",
            "[": "delim14",
            "]": "delim14",
            ";": "delim3",
            ",": "delim3",
           
        }

        # Updated delimiters
        self.delimiters = {
            "delim1": [" ", "\n", "\t"],
            "delim2": [None],
            "delim3": [" "],
            "delim4": [" ", '"'],
            "delim5": [" ", "("],
            "delim6": [" ", "{"],
            "delim7": [" ", ":", "\n", "\t"],
            "delim8": [";"],
            "delim9": [":"],
            "delim10": [";", " "],
            "delim11": [" ", "<", ">", "=", "!", "&", "|"],
            "delim12": [" ", "+", "-", "*", "/", "%", "("],
            "delim13": [" ", "=", "<", ">", "!"],
            "delim14": [" ", "\n", "{", "(", "["],
            "iden_delim": [" ", "=", ";", ",", "{", "}", "(", ")"]
        }

    def is_whitespace(self, c):
        return c in self.delimiters["delim1"]

    def is_symbol(self, s):
        return s in self.symbols

    def get_next_symbol(self):
        start = self.position
        # Detect if we are encountering symbols directly, and return that symbol
        if self.is_symbol(self.input[self.position]):
            self.position += 1  # Move position forward to avoid infinite loop
            symbol = self.input[start:self.position]
            # Check for consecutive delimiters
            if self.position < len(self.input) and self.is_symbol(self.input[self.position]):
                raise SyntaxError(f"Unexpected consecutive delimiters: '{symbol}{self.input[self.position]}'")
            return symbol
        else:
            # If not a symbol, get the next valid identifier
            while self.position < len(self.input) and not self.is_whitespace(self.input[self.position]) and not self.is_symbol(self.input[self.position]):
                self.position += 1
            return self.input[start:self.position]

    def is_valid_identifier(self, word):
        # Length check (optional)
        if len(word) == 0:
            return False
        if len(word) > 20:  # Exceeds maximum length
            return False

        # Check if it starts with a lowercase letter
        if not word[0].islower():  # Must start with a lowercase letter
            return False

        # Remove any trailing delimiters from the identifier
        word = word.rstrip("".join(self.delimiters["iden_delim"]))

        # Check if there are any multiple delimiters at the end
        if any(delim * 2 in word for delim in self.delimiters["iden_delim"]):
            return False  # Multiple delimiters found

        # Check if all characters are valid (alphanumeric or underscores)
        for char in word:
            if not (char.isalnum() or char == "_"):  # Allow letters, digits, and underscores
                return False

        return True

    def tokenize(self):
        tokens = []
        lexemes = []
        self.position = 0  # Reset position for each analysis

        while self.position < len(self.input):
            current_char = self.input[self.position]

            # Check for whitespace (spaces) explicitly
            if self.is_whitespace(current_char):
                tokens.append(Token(TokenType.PUNCTUATOR, "SPACE"))
                
                self.position += 1
                continue

            # Check for keywords
            word = self.get_next_symbol()
            if word in self.keywords:
                tokens.append(Token(TokenType.KEYWORD, word))
                lexemes.append(word)

            # Check for symbols
            elif word in self.symbols:
                tokens.append(Token(TokenType.OPERATOR, word))
                lexemes.append(word)

            # Check for identifiers
            elif word.isalnum() or "_" in word:
                if self.is_valid_identifier(word):
                    tokens.append(Token(TokenType.IDENTIFIER, word))
                else:
                    tokens.append(Token(TokenType.UNKNOWN, word))
                lexemes.append(word)

            # Unknown or other characters
            else:
                tokens.append(Token(TokenType.UNKNOWN, word))
                lexemes.append(word)

        return tokens, lexemes

def validate_syntax(tokens, keywords):
    errors = []

    for token in tokens:
        if token.type == TokenType.UNKNOWN:
            if len(token.value) > 20:
                errors.append(f"Identifier Error: '{token.value}' exceeds 20 characters")
            else:
                errors.append(f"Lexical Error: '{token.value}' is not a valid identifier")

    return errors

def update_analysis(event=None):
    source_code = text_with_line_numbers.text.get("1.0", "end-1c")
    lexer = LexicalAnalyzer(source_code)
    try:
        tokens, lexemes = lexer.tokenize()

        lexeme_text.delete("1.0", "end")
        token_text.delete("1.0", "end")
        error_text.delete("1.0", "end")

        # Display lexemes and tokens
        for lexeme in lexemes:
            lexeme_text.insert(tk.END, f"{lexeme}\n")

        for token in tokens:
            if token.type == TokenType.IDENTIFIER:
                token_text.insert(tk.END, f"IDENTIFIER\n")
            else:
                token_text.insert(tk.END, f"{token.value}\n")

        # Validate syntax
        errors = validate_syntax(tokens, lexer.keywords)
        if errors:
            for error in errors:
                error_text.insert(tk.END, error + "\n")
        else:
            error_text.insert(tk.END, "No errors detected.\n")

    except SyntaxError as e:
        error_text.delete("1.0", "end")  # Clear previous errors
        error_text.insert(tk.END, str(e) + "\n")

class TextWithLineNumbers(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.line_numbers = tk.Text(self, width=4, padx=3, takefocus=0, border=0, background="lightgray", state="disabled", wrap="none")
        self.line_numbers.pack(side="left", fill="y")

        self.text = scrolledtext.ScrolledText(self, wrap="none")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<KeyRelease>", self._update_line_numbers)
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
