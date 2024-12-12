import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk  # For loading and displaying images

# Token classes
class TokenType:
    KEYWORD = 'KEYWORD'
    UNKNOWN = 'UNKNOWN'

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

# Lexer logic
class TransitionLexer:
    def __init__(self):
        self.final_states = {
            5: 'Base',
            11: 'Bubble',
            15: 'Build',
            20: 'Broke',
            27: 'Change',
            30: 'Con',
            33: 'Const',
            39: 'Create',
            43: 'Def',
            49: 'Destroy',
            56: 'Display',
            58: 'Do',
            63: 'Flip',
            70: 'Ifsnap',
            75: 'Link',
            80: 'Pane',
            85: 'Piece',
            88: 'Put',
            96: 'Rebrick',
            101: 'Revoid',
            108: 'Stable',
            111: 'Set',
            115: 'Snap',
            121: 'Snapif',
            125: 'Subs',
            131: 'While',
            138: 'Wobble'
        }

    def analyze(self, input_string):
        state = 0
        token_value = ""
        tokens = []
        errors = []
        first_token_checked = False

        for char in input_string:
            if char in {' ', '\n', '\t'}:
                if state in self.final_states:
                    if not first_token_checked:
                        if self.final_states[state] != 'Build':
                            errors.append("Lexical Error: The code must start with 'Build'")
                        first_token_checked = True
                    tokens.append(Token(TokenType.KEYWORD, self.final_states[state]))
                    token_value = ""
                    state = 0
                elif token_value.strip():
                    errors.append(f"Lexical Error: '{token_value.strip()}' is not recognized")
                    tokens.append(Token(TokenType.UNKNOWN, token_value.strip()))
                    token_value = ""
                    state = 0
                continue

            token_value += char

            match state:
                case 0:
                    if char == 'B':
                        state = 1
                    elif char == 'C':
                        state = 21
                    elif char == 'D':
                        state = 40
                    elif char == 'F':
                        state = 59
                    elif char == 'I':
                        state = 64
                    elif char == 'L':
                        state = 71
                    elif char == 'P':
                        state = 76
                    elif char == 'R':
                        state = 89
                    elif char == 'S':
                        state = 102
                    elif char == 'W':
                        state = 126
                    else:
                        state = -1

                # Transitions for "Base"
                case 1:
                    if char == 'a':
                        state = 2
                case 2:
                    if char == 's':
                        state = 3
                case 3:
                    if char == 'e':
                        state = 4
                case 4:
                    if char in {' ', '\n', '\t'}:
                        state = 5

                # Transitions for "Bubble"
                case 6:
                    if char == 'u':
                        state = 7
                case 7:
                    if char == 'b':
                        state = 8
                case 8:
                    if char == 'b':
                        state = 9
                case 9:
                    if char == 'l':
                        state = 10
                case 10:
                    if char == 'e':
                        state = 11

                # Transitions for "Build"
                case 1:
                    if char == 'u':
                        state = 12
                case 12:
                    if char == 'i':
                        state = 13
                case 13:
                    if char == 'l':
                        state = 14
                case 14:
                    if char == 'd':
                        state = 15

                # Transitions for "Link"
                case 71:
                    if char == 'i':
                        state = 72
                case 72:
                    if char == 'n':
                        state = 73
                case 73:
                    if char == 'k':
                        state = 75

                # Transitions for "Pane"
                case 76:
                    if char == 'a':
                        state = 77
                case 77:
                    if char == 'n':
                        state = 78
                case 78:
                    if char == 'e':
                        state = 80

                # Transitions for "Piece"
                case 81:
                    if char == 'i':
                        state = 82
                case 82:
                    if char == 'e':
                        state = 83
                case 83:
                    if char == 'c':
                        state = 84
                case 84:
                    if char == 'e':
                        state = 85

                # Transitions for "Put"
                case 86:
                    if char == 'u':
                        state = 87
                case 87:
                    if char == 't':
                        state = 88

                # Transitions for "Rebrick"
                case 89:
                    if char == 'e':
                        state = 90
                case 90:
                    if char == 'b':
                        state = 91
                case 91:
                    if char == 'r':
                        state = 92
                case 92:
                    if char == 'i':
                        state = 93
                case 93:
                    if char == 'c':
                        state = 94
                case 94:
                    if char == 'k':
                        state = 96

                # Transitions for "Revoid"
                case 97:
                    if char == 'o':
                        state = 98
                case 98:
                    if char == 'i':
                        state = 99
                case 99:
                    if char == 'd':
                        state = 101

                # Transitions for "Stable"
                case 102:
                    if char == 't':
                        state = 103
                case 103:
                    if char == 'a':
                        state = 104
                case 104:
                    if char == 'b':
                        state = 105
                case 105:
                    if char == 'l':
                        state = 106
                case 106:
                    if char == 'e':
                        state = 108

                # Transitions for "Set"
                case 111:
                    if char == 'e':
                        state = 112
                case 112:
                    if char == 't':
                        state = 111

                # Transitions for "Snap"
                case 113:
                    if char == 'n':
                        state = 114
                case 114:
                    if char == 'a':
                        state = 115
                case 115:
                    if char == 'p':
                        state = 115

                # Transitions for "Snapif"
                case 116:
                    if char == 'i':
                        state = 117
                case 117:
                    if char == 'f':
                        state = 121

                # Transitions for "Subs"
                case 122:
                    if char == 'b':
                        state = 123
                case 123:
                    if char == 's':
                        state = 125

                # Transitions for "While"
                case 126:
                    if char == 'h':
                        state = 127
                case 127:
                    if char == 'i':
                        state = 128
                case 128:
                    if char == 'l':
                        state = 129
                case 129:
                    if char == 'e':
                        state = 131

                # Transitions for "Wobble"
                case 132:
                    if char == 'o':
                        state = 133
                case 133:
                    if char == 'b':
                        state = 134
                case 134:
                    if char == 'b':
                        state = 135
                case 135:
                    if char == 'l':
                        state = 136
                case 136:
                    if char == 'e':
                        state = 138

                case _:
                    state = -1

        if state in self.final_states and token_value.strip():
            tokens.append(Token(TokenType.KEYWORD, self.final_states[state]))
            token_value = ""
            state = 0
        elif token_value.strip() and state == -1:
            errors.append(f"Lexical Error: '{token_value.strip()}' is not recognized")
            tokens.append(Token(TokenType.UNKNOWN, token_value.strip()))
            token_value = ""
            state = 0

        return tokens, errors

def validate_syntax(tokens):
    errors = []
    for token in tokens:
        if token.type == TokenType.UNKNOWN:
            errors.append(f"Lexical Error: '{token.value}' is not recognized")
    return errors

def update_analysis(event=None):
    source_code = text_with_line_numbers.text.get("1.0", "end-1c")
    lexer = TransitionLexer()
    tokens, errors = lexer.analyze(source_code)

    lexeme_text.delete("1.0", "end")
    token_text.delete("1.0", "end")
    error_text.delete("1.0", "end")

    for token in tokens:
        lexeme_text.insert(tk.END, f"{token.value}\n")
        token_text.insert(tk.END, f"{token.type}\n")

    lexical_errors = validate_syntax(tokens)
    errors.extend(lexical_errors)

    if errors:
        for error in errors:
            error_text.insert(tk.END, error + "\n")
    else:
        error_text.insert(tk.END, "No errors detected.\n")

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

# Main GUI setup
root = tk.Tk()
root.title("Transition-Based Code Analyzer")
root.state("zoomed")  # Start maximized

# Load the background image
bg_image = Image.open("lego-city.jpg")  # Replace with your image file path
bg_image = bg_image.resize((1920, 1080))  # Resize to match window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas to hold the background image
canvas = tk.Canvas(root, width=1920, height=1080)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")  # Display the image

# User Input Section (Top-Left)
input_frame = tk.Frame(canvas, bg="white")
input_frame.place(relx=0.02, rely=0.05, anchor="nw", width=700, height=400)

label = tk.Label(input_frame, text="Enter Lego-C code:", bg="white", anchor="w")
label.pack(side="top", anchor="w", padx=10, pady=5)

text_with_line_numbers = TextWithLineNumbers(input_frame, bg="#ffffff")
text_with_line_numbers.pack(side="top", fill="both", expand=True, padx=10, pady=5)
text_with_line_numbers.text.bind("<KeyRelease>", update_analysis)

# Errors Section (Bottom-Left)
error_frame = tk.Frame(canvas, bg="white")
error_frame.place(relx=0.02, rely=0.6, anchor="nw", width=700, height=300)

error_label = tk.Label(error_frame, text="Errors:", bg="white", anchor="w")
error_label.pack(padx=5, pady=5)

error_text = tk.Text(error_frame, width=85, height=15, bg="#ffffff")
error_text.pack(padx=5, pady=5)

# Output Section (Right: Top to Bottom)
output_frame = tk.Frame(canvas, bg="white")
output_frame.place(relx=0.75, rely=0.05, anchor="nw", width=600, height=800)

lexeme_label = tk.Label(output_frame, text="Lexemes:", bg="white", anchor="w")
lexeme_label.pack(padx=5, pady=5)

lexeme_text = tk.Text(output_frame, width=40, height=15, bg="#ffffff")
lexeme_text.pack(padx=5, pady=5)

token_label = tk.Label(output_frame, text="Tokens:", bg="white", anchor="w")
token_label.pack(padx=5, pady=5)

token_text = tk.Text(output_frame, width=40, height=15, bg="#ffffff")
token_text.pack(padx=5, pady=5)

root.mainloop()