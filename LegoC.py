import tkinter as tk

def process_input(event=None):
    input_text = input_entry.get("1.0", "end-1c")  # Get input text
    lexeme_output.delete("1.0", tk.END)  # Clear previous output
    token_output.delete("1.0", tk.END)   # Clear token output
    output_text.delete("1.0", tk.END)    # Clear lexical error output

    target_words = {"Build": "\n", "Bubble": " ", "Base": [" ", ":", "\n", "\t"]}
    quotation = '"'
    # Split input into lines
    lines = input_text.split("\n")
    if not lines or all(not line.strip() for line in lines):
        output_text.insert(tk.END, "Input is empty. Please provide some input.\n")
        return

    for line_number, line in enumerate(lines):
        state = 0  # Reset state for each line
        word = ""
        target_word = None
        for index, char in enumerate(line + "\n"): # Include newline for final state check
            if state == 0:  # Start state
                if char == "B":
                    state = 1
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "C":
                    state = 25
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "D":
                    state = 40
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "F":
                    state = 55
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "I":
                    state = 59
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "L":
                    state = 65
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "P":
                    state = 69
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "R":
                    state = 79
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "S":
                    state = 90
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "W":
                    state = 106
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "=": # Equal
                    state = 116
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "+": # Positive / add
                    state = 118
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "-": # Minus 
                    state = 120
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "*": # Multiply (asterisk)
                    state = 122
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "/": # Division (slash)
                    state = 124
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "%": # Percentage
                    state = 126
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "!": # Not (exclamation point)
                    state = 128
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "<": # Greater than
                    state = 131
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == ">": # Less than
                    state = 133
                    word = ""
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "&": # Ampersand
                    state = 135
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "|": # 
                    state = 137
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "{": # Open curly brace
                    state = 139
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "}": # Closed curly brace
                    state = 140
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "(": # Open parenthesis
                    state = 141
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == ")": # Closed parenthesis
                    state = 142
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "[": # Open brace
                    state = 143
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "]": # Closed brace
                    state = 144
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == ";": # Semicolon
                    state = 145
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "\0":
                    state = 146
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "~" or char.isdigit(): 
                    state = 146
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "." or char.isdigit():
                    state = 156
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == '"' or char.isdigit(): ## \" to treat " literally.
                    state = 167
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "#" or char.isdigit(): # (comment)
                    state = 170
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == ",": # Comma
                    state = 173
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == ":": # Colon
                    state = 174
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():  # Check for identifiers starting with lowercase letter
                    state = 20
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif not char.isspace():
                    output_text.insert(tk.END, f"Line {line_number + 1}: Unknown\n")
                    state = "x"

            elif state == 'x':
                if char.islower():
                        word = ""
                        output_text.insert(tk.END, f"State: {state}\n")
                        state = 'y'
            elif state == 'y':
                if char == " ":
                        word += char
                        output_text.insert(tk.END, f"State: {state}\n")
                        state = 0 

            elif state == 1: #For Build, Base, Broke
                if char == "u":
                    state = 2
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "a":
                    state = 11
                    word += char
                    target_word = "Base"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "r":
                    state = 21
                    word += char
                    target_word = "Broke"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'u' or 'a' after 'B'\n")
                    state = 0
                    word = ""

            elif state == 21: #For Broke
                if char == "o":
                    state = 22
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'o' \n")
                    state = 0
                    word = ""

            elif state == 22: #For Broke
                if char == "k":
                    state = 23
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'k' \n")
                    state = 0
                    word = ""

            elif state == 23: #For Broke
                if char == "e":
                    state = 24
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""

            elif state == 24: #For Broke
                if char == ";":
                    state = 145
                    word = ""
                    target_word = "Broke"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    lexeme_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    state = 0
                    word = ""
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ';' \n")
                    state = 0
                    word = ""

            elif state == 25: # h or o or r  
                if char == "h":
                    state = 26
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "o": #For Con or Const
                    state = 31
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "r": #For create
                    state = 35
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 25
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'h' or 'o' or 'or' \n")
                    state = 0
                    word = ""
            
            elif state == 26: #For Change
                if char == "a":
                    state = 27
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'a' \n")
                    state = 0
                    word = ""
            
            elif state == 27: #For Change
                if char == "n":
                    state = 28
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'n' \n")
                    state = 0
                    word = ""
            
            elif state == 28: #For Change
                if char == "g":
                    state = 29
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'g' \n")
                    state = 0
                    word = ""
            
            elif state == 29: #For Change
                if char == "e":
                    state = 30
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 30: #Final state for Change
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Change"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "(":
                    state = 141
                    word = char
                    target_word = "Change"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '(' \n")
                    state = 0
                    word = ""
            
            elif state == 31: # For Con
                if char == "n":
                    state = 32
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'n' \n")
                    state = 0
                    word = ""
            
            elif state == 32: #Final state for Con
                if char == ";":
                    state = 0
                    word = ""
                    target_word = "Con"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ';' or 's' \n")
                    word = ""
                    state = 0
                elif char == "s": #For Const
                    word += char
                    state = 33
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ';' \n")
                    state = 0
                    word = ""

            elif state == 33: #For Const
                if char == "t":
                    state = 34
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't' \n")
                    state = 0
                    word = ""
            
            elif state == 34: #Final state for Const
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Const"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' \n")
                    state = 0
                    word = ""
            
            elif state == 35: #For Create
                if char == "e":
                    state = 36
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 36: #For Create
                if char == "a":
                    state = 37
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'a' \n")
                    state = 0
                    word = ""
            
            elif state == 37: #For Create
                if char == "t":
                    state = 38
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't' \n")
                    state = 0
                    word = ""
            
            elif state == 38: #For Create
                if char == "e":
                    state = 39
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""

            elif state == 39: #Final state for Create
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Create"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "(":
                    state = 141
                    word = char
                    target_word = "Create"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '(' \n")
                    state = 0
                    word = ""

            elif state == 40: #For Def, Do, Destroy, Display
                if char == "e":
                    state = 41
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "o": #For Do
                    state = 48
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "i": #For Do
                    state = 49
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' or 'o' or 'i' \n")
                    state = 0
                    word = ""
            
            elif state == 41: #For Def
                if char == "f":
                    state = 42
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "s": #For Destroy
                    state = 43
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'f' or 's' \n")
                    state = 0
                    word = ""

            elif state == 42: #Final state for Def
                if char == ":":
                    state = 174
                    word = ""
                    target_word = "Def"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ':' \n")
                    state = 0
                    word = ""
            
            elif state == 43: #For Destroy
                if char == "t":
                    state = 44
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't' \n")
                    state = 0
                    word = ""
            
            elif state == 44: #For Destroy
                if char == "r":
                    state = 45
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'r' \n")
                    state = 0
                    word = ""

            elif state == 45: #For Destroy
                if char == "o":
                    state = 46
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'o' \n")
                    state = 0
                    word = ""
            
            elif state == 46: #For Destroy
                if char == "y":
                    state = 47
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'y' \n")
                    state = 0
                    word = ""
            
            elif state == 47: #Final state for Destroy
                if char.strip() == "":
                    state = 0
                    word = ""
                    target_word = "Destroy"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<null>' \n")
                    state = 0
                    word = ""
            
            elif state == 48: #Final state for Do
                if char == " " or char == "{" or char == "(":
                    state = 0
                    word = ""
                    target_word = "Do"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or <openbrace> or ( \n")
                    state = 0
                    word = ""
            
            elif state == 49: #For Display
                if char == "s":
                    state = 50
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 's' \n")
                    state = 0
                    word = ""
            
            elif state == 50: #For Display
                if char == "p":
                    state = 51
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'p' \n")
                    state = 0
                    word = ""
            
            elif state == 51: #For Display
                if char == "l":
                    state = 52
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'l' \n")
                    state = 0
                    word = ""

            elif state == 52: #For Display
                if char == "a":
                    state = 53
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'a' \n")
                    state = 0
                    word = ""
            
            elif state == 53: #For Display
                if char == "y":
                    state = 54
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'y' \n")
                    state = 0
                    word = ""

            elif state == 54: #Final state for Display
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Display"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == '"':
                    state = 167
                    word = ""
                    target_word = "Display"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f'Line {line_number + 1}: Lexical error at position {index}: should be <space> or " \n')
                    state = 0
                    word = ""
            
            elif state == 55: #For Flip
                if char == "l":
                    state = 56
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'l' \n")
                    state = 0
                    word = ""
            
            elif state == 56: #For Flip
                if char == "i":
                    state = 57
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'i' \n")
                    state = 0
                    word = ""
            
            elif state == 57: #For Flip
                if char == "p":
                    state = 58
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'p' \n")
                    state = 0
                    word = ""

            elif state == 58: #Final state for Flip
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Flip"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""
            
            elif state == 59: #For Ifsnap
                if char == "f":
                    state = 60
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'f' \n")
                    state = 0
                    word = ""

            elif state == 60: #For Ifsnap
                if char == "s":
                    state = 61
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 's' \n")
                    state = 0
                    word = ""

            elif state == 61: #For Ifsnap
                if char == "n":
                    state = 62
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'n' \n")
                    state = 0
                    word = ""

            elif state == 62: #For Ifsnap
                if char == "a":
                    state = 63
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'a' \n")
                    state = 0
                    word = ""
            
            elif state == 63: #For Ifsnap
                if char == "p":
                    state = 64
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'p' \n")
                    state = 0
                    word = ""
            
            elif state == 64: #Final state for Ifsnap
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Ifsnap"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "{":
                    word = char
                    target_word = "Ifsnap"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    state = 139 #state of {
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '<open_curly_brace>'\n")
                    state = 0
                    word = ""

            elif state == 65: #For Link
                if char == "i":
                    state = 66
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'i' \n")
                    state = 0
                    word = ""
            
            elif state == 66: #For Link
                if char == "n":
                    state = 67
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'n' \n")
                    state = 0
                    word = ""

            elif state == 67: #For Link
                if char == "k":
                    state = 68
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'k' \n")
                    state = 0
                    word = ""

            elif state == 68: #Final state for Link
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Link"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""

            elif state == 69: #For Pane Piece Put
                if char == "a":
                    state = 70
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "i":
                    state = 73
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "u":
                    state = 77
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'a' or 'i' or 'u' \n")
                    state = 0
                    word = ""
            
            elif state == 70: #For Pane
                if char == "n":
                    state = 71
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'n' \n")
                    state = 0
                    word = ""

            elif state == 71: #For Pane
                if char == "e":
                    state = 72
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 72: #Final state for Pane
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Pane"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "(":
                    state = 141
                    word = char
                    target_word = "Pane"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '('\n")
                    state = 0
                    word = ""
            
            elif state == 73: #For Piece
                if char == "e":
                    state = 74
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e23' \n")
                    state = 0
                    word = ""
            
            elif state == 74: #For Piece
                if char == "c":
                    state = 75
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'c' \n")
                    state = 0
                    word = ""
            
            elif state == 75: #For Piece
                if char == "e":
                    state = 76
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e1' \n")
                    state = 0
                    word = ""
            
            elif state == 76: #Final state for Piece
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Piece"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""
            
            elif state == 77: #For Put
                if char == "t":
                    state = 78
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't' \n")
                    state = 0
                    word = ""
            
            elif state == 78: #Final state for Put
                if char == " " or char == "(":
                    state = 0
                    word = ""
                    target_word = "Put"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""
            
            elif state == 79: #For Revoid
                if char == "e":
                    state = 80
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 80: #For Revoid Rebrick
                if char == "v":
                    state = 81
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "b": #FPr Rebrick
                    state = 85
                    word += char
                    output_text.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'v' or 'b' \n")
                    state = 0
                    word = ""
            
            elif state == 81: #For Revoid
                if char == "o":
                    state = 82
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'o' \n")
                    state = 0
                    word = ""
            
            elif state == 82: #For Revoid
                if char == "i":
                    state = 83
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'i' \n")
                    state = 0
                    word = ""

            elif state == 83: #For Revoid
                if char == "d":
                    state = 84
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'd' \n")
                    state = 0
                    word = ""
            
            elif state == 84: #Final state for Revoid
                if char == ";":
                    state = 0
                    word = ""
                    target_word = "Revoid"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n") 
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<semicolon>'\n")
                    state = 0
                    word = ""

            elif state == 85: #For Rebrick
                if char == "r":
                    state = 86
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'r' \n")
                    state = 0
                    word = ""

            elif state == 86: #For Rebrick
                if char == "i":
                    state = 87
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'i' \n")
                    state = 0
                    word = ""

            elif state == 87: #For Rebrick
                if char == "c":
                    state = 88
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'c' \n")
                    state = 0
                    word = ""

            elif state == 88: #For Rebrick
                if char == "k":
                    state = 89
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'k' \n")
                    state = 0
                    word = ""
            
            elif state == 89: #Final state for Rebrick
                if char == " " or char == ";":
                    state = 0
                    word = ""
                    target_word = "Rebrick"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '<semicolon>'\n")
                    state = 0
                    word = ""
            
            elif state == 90: #For Stable, Snap, Snapif, Subs
                if char == "t":
                    state = 91
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "n": #Snap and Snapif
                    state = 96
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "e": #For Set
                    state = 101
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "u": #For Set
                    state = 103
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't', 'n', 'u', 'e' \n")
                    state = 0
                    word = ""

            elif state == 91: #For Stable
                if char == "a":
                    state = 92
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'a' \n")
                    state = 0
                    word = ""

            elif state == 92: #For Stable
                if char == "b":
                    state = 93
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'b' \n")
                    state = 0
                    word = ""

            elif state == 93: #For Stable
                if char == "l":
                    state = 94
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'l' \n")
                    state = 0
                    word = ""

            elif state == 94: #For Stable
                if char == "e":
                    state = 95
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""

            elif state == 95: #Final state for Stable
                if char == ";":
                    state = 0
                    word = ""
                    target_word = "Stable"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<semicolon>'\n")
                    state = 0
                    word = ""
            
            elif state == 96: #For Snap
                if char == "a":
                    state = 97
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'a' \n")
                    state = 0
                    word = ""

            elif state == 97: #For Snap
                if char == "p":
                    state = 98
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'p' \n")
                    state = 0
                    word = ""

            elif state == 98: #Final state for Snap
                if char == " " or char == "{" or char == "\n":
                    state = 0
                    word = ""
                    target_word = "Snap"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "i": #For Snapif 
                    state = 99
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<open_curly_brace>' or 'i'\n")
                    state = 0
                    word = ""
            
            elif state == 99: #For Snapif
                if char == "f":
                    state = 100
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'f' \n")
                    state = 0
                    word = ""

            elif state == 100: #Final state for Snapif
                if char == " " or char == "(":
                    state = 0
                    word = ""
                    target_word = "Snapif"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '('\n")
                    state = 0   
                    word = ""
            
            elif state == 101: #For Set
                if char == "t":
                    state = 102
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't' \n")
                    state = 0
                    word = ""
            
            elif state == 102: #Final state for Set
                if char == " " or char == "{":
                    state = 0
                    word = ""
                    target_word = "Set"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '<open_curly_brace'\n")
                    state = 0   
                    word = ""
            
            elif state == 103: #For Subs
                if char == "b":
                    state = 104
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'b' \n")
                    state = 0
                    word = ""

            elif state == 104: #For Subs
                if char == "s":
                    state = 105
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 's' \n")
                    state = 0
                    word = ""
            
            elif state == 105: #Final state for Subs
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Subs"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0   
                    word = ""
            
            elif state == 106: #For While Wobble
                if char == "h": #For While 
                    state = 107
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "o": #For Wobble
                    state = 111
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'h' or 'o'\n")
                    state = 0
                    word = ""
            
            elif state == 107: #For While 
                if char == "i":
                    state = 108
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'i' \n")
                    state = 0
                    word = ""
            
            elif state == 108: #For While 
                if char == "l":
                    state = 109
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'l' \n")
                    state = 0
                    word = ""
            
            elif state == 109: #For While 
                if char == "e":
                    state = 110
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 110: #Final state for While
                if char == " " or char == "(":
                    state = 0
                    word = ""
                    target_word = "While"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '(' \n")
                    state = 0   
                    word = ""

            elif state == 111: #For Wobble 
                if char == "b":
                    state = 112
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'b' \n")
                    state = 0
                    word = ""
            
            elif state == 112: #For Wobble 
                if char == "b":
                    state = 113
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'b' \n")
                    state = 0
                    word = ""

            elif state == 113: #For Wobble 
                if char == "l":
                    state = 114
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'l' \n")
                    state = 0
                    word = ""
            
            elif state == 114: #For Wobble 
                if char == "e":
                    state = 115
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 115: #Final state for Wobble
                if char == ";":
                    state = 0
                    word = ""
                    target_word = "Wobble"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<semicolon>' \n")
                    state = 0   
                    word = ""
            
            elif state == 116: #Final state for '='
                if char == " ":
                    state = 0
                    word += char
                    target_word = "=" #For '=='
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 117
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 117: #Final state for '=='
                if char == " " or char == "(":
                    state = 0
                    word = char
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 118: #Final state for '+'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 119
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 119: #Final state for '+='
                if char == " " or char == "(":
                    state = 0
                    word = char
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 120: #Final state for '-'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 121
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 121: #Final state for '-='
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 122: #Final state for '*'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 123
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 123: #Final state for '*='
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 124: #Final state for '/'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 125
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 125: #Final state for '/='
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 126: #Final state for '%'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 127
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 127: #Final state for '%='
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 128: #Final state for '!'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "!":
                    state = 129
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "=": #For Snapif
                    state = 130
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 129: #Final state for '!!'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 130: #Final state for '!='
                if char == " ":
                    state = 0
                    word += char
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 131: #Final state for '<'
                if char == " ":
                    state = 0
                    word = char
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 132
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 132: #Final state for '<='
                if char == " ":
                    state = 0
                    word += char
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 133: #Final state for '>'
                if char == " ":
                    state = 0
                    word += char
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "=": #For Snapif
                    state = 134
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 134: #Final state for '>='
                if char == " ":
                    state = 0
                    word += char
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 135: #Final state for '&'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "&": #For Snapif
                    state = 136
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 136: #Final state for '&&'
                if char == " " or char == "(":
                    state = 0
                    word =""
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 137: #Final state for '|'
                if char == " " or char == "(":
                    state = 0
                    word += char
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "|": #For Snapif
                    state = 138
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char.islower():
                    state = 20
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 139: #Final state for '{'
                if char == " " or char == "{" or char == "\n":
                    state = 0
                    word += char
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 140: #Final state for '}'
                if char == " " or char == "{" or char == "\n":
                    state = 0
                    word += char
                    target_word = "}" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "}" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "}" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "}" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 141: #Final state for '('
                if char == " " or char == "{":
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word += char
                    state = 0
                elif char.islower():
                    state = 20
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char == ")":
                    state = 142
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 142: #Final state for ')'
                if char == " " or char == "{":
                    state = 0
                    word += char
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char == ";":
                    state = 145
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 143: #Final state for '['
                if char == " " or char == "{":
                    state = 0
                    word += char
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 144: #Final state for ']'
                if char == " " or char == "{":
                    state = 0
                    word += char
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char == "[":
                    state = 143
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 145: #Final state for ';'
                if char == " " or char == "\n":
                    state = 0
                    word += char
                    target_word = ";" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    output_text.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'space'\n")
                    state = 0
                    word = ""


            # FOR LINKLIT ---------------------------------------------------------------------------------------------------------------------------------
            elif state == 146: # ~[digit1] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 147
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 147: # ~[digit2] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 148
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 148: # ~[digit3] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 149
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 149: # ~[digit4] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 150
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""
            
            elif state == 150: # ~[digit5] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 151
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 151: # ~[digit6] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 152
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 152: # ~[digit7] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 153
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 153: # ~[digit8] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 154
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 154: # ~[digit9] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 155
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 155: # ~[digit10] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    output_text.insert(tk.END, f"Lexical error: Limit reached\n")
                elif char == ".":
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word} \n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 116
                        word = ""
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Linklit {word}\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""
            # FOR LINKLIT ---------------------------------------------------------------------------------------------------------------------------------


            
            elif state == 156: #[digit1] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 157
                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        word += char
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 157: #[digit2] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 158

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 158: #[digit3] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 159

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 159: #[digit4] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 160

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 160: #[digit5] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 161

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 161: #[digit6] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 162

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 162: #[digit7] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 163
                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 163: #[digit8] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 164

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 164: #[digit9] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 165

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""
            
            elif state == 165: #[digit10] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    state = 166

                elif char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 166: #[delimeter] [BUBBLE LITERAL]
                if char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 166
                        word = ""

            elif state == 167: #[first input] [PIECE LITERAL]
                if 32 <= ord(char) <= 33 or 35 <= ord(char) <= 126:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")                       
                    word += char
                elif char == '"':
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")  
                    state = 169
                    word += char
                else:
                    state == 168
                        
            elif state == 169: #[piece_delim] [PIECE LITERAL]
                if char == " ":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word} \n")
                    state = 0
                    word = ""
                elif char == ";":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word}\n")
                    state = 145 #state of ;
                    word = char
                elif char == "{":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word}\n")
                    state = 139 #state of {
                    word = ""
                elif char == "}":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word}\n")
                    state = 140 #state of }
                    word = ""
                elif char == ")":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word}\n")
                    state = 142 #state of )
                    word = ""
                elif char == "~":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word}\n")
                    state = 146 #state of ~
                    word = ""
                elif char == "=":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word}\n")
                    state = 116 #state of =
                    word = ""
                elif char == ":":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: Piecelit {word}\n")
                    state = 145 #state of ;
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                    state = 0
                    word = ""

            elif state == 170: #[piece_comment ascii] [PIECE LITERAL]
                if char == "#":
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: {char} \n")
                        state = 171
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 171: #[piece_comment ascii] [PIECE LITERAL]
                if char in {" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@",
                            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                            "[", "\\", "]", "^", "_", "`",
                            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                            "{", "|", "}", "~"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: {char} \n")
                        state = 172
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 172: #[piece_comment delim] [PIECE LITERAL]
                if char in {"\n"}:
                        lexeme_output.insert(tk.END, f"Reading: {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1} scanned: {char} \n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 173: #Final state for ','
                if char == " ":
                    state = 0
                    word += char
                    target_word = "," 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char.islower():
                    state = 20
                    target_word = "," 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "," 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "," 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
                
            elif state == 174: #Final state for ':'
                if char == " ":
                    state = 0
                    word += char
                    target_word = ":" 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif char == "{":
                    state = 139
                    target_word = ":" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                elif char == "\n":
                    state = 0
                    target_word = ":" 
                    lexeme_output.insert(tk.END, f"Reading: fetched {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    word = char
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 2:
                if char == "i":
                    state = 3
                    word += char
                    target_word = "Build"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == "b":
                    state = 7
                    word += char
                    target_word = "Bubble"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'i' or 'b' after 'Bu'\n")
                    state = 0
                    word = ""

            # Build transitions
            elif state == 3:
                if char == "l":
                    state = 4
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'l' after 'Bui'\n")
                    state = 0
                    word = ""

            elif state == 4:
                if char == "d":
                    state = 5
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'd' after 'Buil'\n")
                    state = 0
                    word = ""

            elif state == 5:  # Expect newline immediately after "Build"
                if char == "\n" or char == " " or char == "\t":
                    word = ""
                    target_word = "Build"
                    lexeme_output.insert(tk.END, f"Reading: {char} \n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                    state = 0  # Reset state for further processing
                    
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected newline after 'Build'\n")
                    state = 0
                    word = ""

            # Bubble transitions
            elif state == 7:
                if char == "b":
                    state = 8
                    word += char
                    lelexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'b' after 'Bub'\n")
                    state = 0
                    word = ""

            elif state == 8:
                if char == "l":
                    state = 9
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'l' after 'Bubb'\n")
                    state = 0
                    word = ""

            elif state == 9:
                if char == "e":
                    state = 10
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'e' after 'Bubbl'\n")
                    state = 0
                    word = ""

            elif state == 10:  #Final state for Bubble
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Bubble"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                else:
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""

            # Base transitions
            elif state == 11:
                if char == "s":
                    state = 12
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'a' after 'B'\n")
                    state = 0
                    word = ""

            elif state == 12:
                if char == "e":
                    state = 13
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                else:
                    lexeme_output.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 's' after 'Ba'\n")
                    state = 0
                    word = ""

            elif state == 13:
                if char == " " or char == ":" or char == "\n" or char == "\t":
                    target_word = "Base"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1}: {target_word}\n")
                    state = 0  # Reset state for further processing
                    word = ""
                elif char == "\n":
                    state = 0
                    word = ""
                elif char == '"':
                    state = 167
                    word = ""
                    target_word = "Base"
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: {target_word} \n")
                elif not char.isspace():
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected space, colon, newline, or tab after 'Base'\n")
                    state = 0
                    word = ""


            # Identifier transitions
            elif state == 20:
                if char.islower() or char.isupper() or char == "_" or char.isdigit():
                    word += char
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                elif char == ";":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word} \n")
                    state = 145 #state of ;
                    word = ""
                elif char == "{":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 139 #state of {
                    word = ""
                elif char == "}":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 140 #state of }
                    word = ""
                elif char == ")":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 142 #state of )
                    word += char
                elif char == "~":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 146 #state of ~
                    word = ""
                elif char == "(":
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 141 #state of (
                    word = ""
                elif char == "[": 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 143  #state of [
                    word = ""   
                elif char == "]": 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 144 #state of ]
                    word = ""
                elif char == "=": 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 116 #state of ]
                    word = ""
                elif char == " ": 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 0 
                    word = ""
                elif char == "\n": 
                    lexeme_output.insert(tk.END, f"Reading: {char}\n")
                    token_output.insert(tk.END, f"Line {line_number + 1} scanned: ID {word}\n")
                    state = 0 
                    word = ""
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                    state = 0
                    word = ""


# Create the main Tkinter window
root = tk.Tk()
root.title("LEGO Code Analyzer")
root.geometry("1920x1080")
root.configure(bg="#66B2FF")  # Blue background

# --- HEADER ---
header_frame = tk.Frame(root, bg="#002F6C", height=80)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="LEGO", bg="yellow", fg="black",
                        font=("Arial", 24, "bold"), anchor="w", padx=20)
header_label.pack(side="left", fill="y")

lego_logo = tk.Label(header_frame, text="Code Analyzer", fg="white", bg="#002F6C",
                     font=("Arial", 24, "bold"), padx=10, pady=5)
lego_logo.pack(side="left", padx=(20, 10))

# --- LEXICAL ANALYZER LABEL ---
lexical_label = tk.Label(root, text="Lexical Analyzer", bg="red", fg="white",
                         font=("Arial", 20, "bold"))
lexical_label.place(relx=0.05, rely=0.68, relwidth=0.6, height=50)

# --- MAIN INPUT FRAME (BIG BLACK BOX WITH YELLOW BORDER) ---
input_frame = tk.Frame(root, bg="yellow", bd=5)
input_frame.place(relx=0.05, rely=0.15, relwidth=0.6, relheight=0.5)

input_entry = tk.Text(input_frame, bg="black", fg="white", font=("Consolas", 14))
input_entry.pack(fill="both", expand=True)
input_entry.bind("<KeyRelease>", process_input)


# --- OUTPUT BOX (LEXICAL ERROR DISPLAY) ---
output_frame = tk.Frame(root, bg="#004080", bd=2)
output_frame.place(relx=0.05, rely=0.75, relwidth=0.6, relheight=0.2)

output_label = tk.Label(output_frame, text="Output Lexical Error", bg="#004080",
                        fg="white", font=("Arial", 12, "bold"))
output_label.pack(side="top", fill="x")

output_text = tk.Text(output_frame, bg="black", fg="white", font=("Consolas", 12),
                      state="normal")
output_text.pack(fill="both", expand=True)

# --- TOKEN HEADER AND BOX ---
token_table_frame = tk.Frame(root, bg="#004080", bd=2)
token_table_frame.place(relx=0.85, rely=0.15, relwidth=0.2, relheight=0.6)  # Smaller and correctly aligned right

# Token Label
token_label = tk.Label(token_table_frame, text="Token", bg="#004080", fg="white",
                       font=("Arial", 12, "bold"))
token_label.pack(side="top", fill="x")

# Token Output Box
token_output = tk.Text(token_table_frame, bg="white", fg="black", font=("Consolas", 12), wrap="none")
token_output.place(relx=0.3, rely=0.15, relwidth=0.15, height=40)
token_output.pack(fill="both", expand=True)

# --- LEXEME HEADER AND BOX ---
lexeme_table_frame = tk.Frame(root, bg="#004080", bd=2)
lexeme_table_frame.place(relx=0.65, rely=0.15, relwidth=0.2, relheight=0.6)  # Left of Token box

# Lexeme Label
lexeme_label = tk.Label(lexeme_table_frame, text="Lexeme", bg="#004080", fg="white",
                        font=("Arial", 12, "bold"))
lexeme_label.pack(side="top", fill="x")

# Lexeme Output Box
lexeme_output = tk.Text(lexeme_table_frame, bg="white", fg="black", font=("Consolas", 12), wrap="none")
lexeme_output.place(relx=0.3, rely=0.15, relwidth=0.15, height=40)
lexeme_output.pack(fill="both", expand=True)

# Run the application
root.mainloop()
