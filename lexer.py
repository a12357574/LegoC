import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from syntax_analyzer import SyntaxAnalyzer

def run_lexical_analysis():
    process_input(analyze=True)
    syntax_output_text.delete("1.0", tk.END)
def run_syntax_analysis():
    # Get tokens and input text from the GUI
    tokens = token_output.get("1.0", tk.END).splitlines()
    input_text = input_entry.get("1.0", tk.END)
    lines = input_text.splitlines()
    
    # Create analyzer with both tokens and lines
    analyzer = SyntaxAnalyzer(tokens, lines)
    try:
        analyzer.analyze()
        syntax_output_text.delete("1.0", tk.END)
        syntax_output_text.insert(tk.END, "Syntax Analysis Complete - No errors found\n")
    except SyntaxError as e:
        syntax_output_text.delete("1.0", tk.END)
        syntax_output_text.insert(tk.END, f"Syntax Error: {str(e)}\n")

def run_semantic_analysis():
    tokens = token_output.get("1.0", tk.END).splitlines()
    input_text = input_entry.get("1.0", tk.END)
    lines = input_text.splitlines()
    
    analyzer = SyntaxAnalyzer(tokens, lines)
    try:
        result = analyzer.analyze()
        semantic_output_text.delete("1.0", tk.END)
        semantic_output_text.insert(tk.END, result + "\n")
    except SyntaxError as e:
        semantic_output_text.delete("1.0", tk.END)
        semantic_output_text.insert(tk.END, f"Syntax Error: {str(e)}\n")

def open_file():
    
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                # Clear existing content
                input_entry.delete("1.0", tk.END)
                
                # Read and insert new content
                content = file.read()
                input_entry.insert("1.0", content)
                
                # Update line numbers
                update_line_numbers()
                
                # Clear output boxes
                lexeme_output.delete("1.0", tk.END)
                token_output.delete("1.0", tk.END)
                output_text.delete("1.0", tk.END)
                
                # Optional: Show success message
                output_text.insert(tk.END, f"File loaded successfully: {file_path}\n")
        except Exception as e:
            output_text.insert(tk.END, f"Error opening file: {str(e)}\n")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            content = input_entry.get("1.0", tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            output_text.insert(tk.END, "File saved successfully!\n")
        except Exception as e:
            output_text.insert(tk.END, f"Error saving file: {str(e)}\n")

def process_input(event=None, analyze=False):
    if not analyze:  # If not triggered by analysis button, return
        return
    input_text = input_entry.get("1.0", tk.END)  # Get input text
    lines = input_text.splitlines()
    lexeme_output.delete("1.0", tk.END)  # Clear previous output
    token_output.delete("1.0", tk.END)   # Clear token output
    output_text.delete("1.0", tk.END)    # Clear lexical error output

    target_words = {"Build": "\n", "Bubble": " ", "Base": [" ", ":", "\n", "\t"]}
    quotation = '"'
    # Split input into lines
    lines = input_text.split("\n")
    if not any(not c.isspace() for c in input_text):  #if input is empty or all spaces
        if input_text:  #if there are spaces, process
            for char in input_text:
                if char == " ":
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
        else:  #empty input
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
                    
                elif char == "C":
                    state = 25
                    word += char
                elif char == "D":
                    state = 40
                    word += char
                elif char == "F":
                    state = 55
                    word += char
                elif char == "I":
                    state = 59
                    word += char
                elif char == "L":
                    state = 65
                    word += char
                elif char == "P":
                    state = 69
                    word += char
                elif char == "R":
                    state = 79
                    word += char
                elif char == "S":
                    state = 90
                    word += char
                elif char == "W":
                    state = 106
                    word += char
                elif char == "=": # Equal
                    state = 116
                    word += char
                elif char == "+": # Positive / add
                    state = 118
                    word += char
                elif char == "-": # Minus 
                    state = 120
                    word += char
                elif char == "*": # Multiply (asterisk)
                    state = 122
                    word += char
                elif char == "/": # Division (slash)
                    state = 124
                    word += char
                elif char == "%": # Percentage
                    state = 126
                    word += char
                elif char == "!": # Not (exclamation point)
                    state = 128
                    word += char
                elif char == "<": # Greater than
                    state = 131
                    word += char
                elif char == ">": # Less than
                    state = 133
                    word = ""
                elif char == "&": # Ampersand
                    state = 135
                    word += char
                elif char == "|": # 
                    state = 137
                    word += char
                elif char == "{": # Open curly brace
                    state = 139
                    word += char
                elif char == "}": # Closed curly brace
                    state = 140
                    word += char
                elif char == "(": # Open parenthesis
                    state = 141
                    word += char
                elif char == ")": # Closed parenthesis
                    state = 142
                    word += char
                elif char == "[": # Open brace
                    state = 143
                    word += char
                elif char == "]": # Closed brace
                    state = 144
                    word += char
                elif char == ";": # Semicolon
                    state = 145
                    word += char
                elif char == "\0":
                    state = 146
                    word += char
                elif char == "~" or char.isdigit(): 
                    state = 146
                    word += char
                elif char == "." or char.isdigit():
                    state = 156
                    word += char
                elif char == '"' or char.isdigit(): ## \" to treat " literally.
                    state = 167
                    word += char
                elif char == "#": # (comment)
                    state = 555
                    word += char
                elif char == ",": # Comma
                    state = 173
                    word += char
                elif char == ":": # Colon
                    state = 174
                    word += char
                elif char.islower():  # Check for identifiers starting with lowercase letter
                    state = 20
                    word += char
                elif char == " ":
                    state = 0
                    word = ""
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")

                
                elif not char.isspace():
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical Error\n")
                    state = "x"

            elif state == 'x':
                if char.islower():
                        word = ""
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical Error\n")
                       
            

            elif state == 1: #For Build, Base, Broke
                if char == "u":
                    state = 2
                    word += char
                
                elif char == "a":
                    state = 11
                    word += char
                elif char == "r":
                    state = 21
                    word += char
                
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'u' or 'a' after 'B'\n")
                    state = 0
                    word = ""

            elif state == 21: #For Broke
                if char == "o":
                    state = 22
                    word += char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'o' \n")
                    state = 0
                    word = ""

            elif state == 22: #For Broke
                if char == "k":
                    state = 23
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
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
                elif char == "o": #For Con or Const
                    state = 31
                    word += char
                elif char == "r": #For create
                    state = 35
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(":
                    state = 141
                    word = char
                    target_word = "Change"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '(' \n")
                    state = 0
                    word = ""
            
            elif state == 31: # For Con
                if char == "n":
                    state = 32
                    word += char
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
                    state = 145
                    word = ""
                    target_word = "Con"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == " ":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ';' or 's' \n")
                    word = ""
                    state = 0
                elif char == "s": #For Const
                    word += char
                    state = 33
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ';' \n")
                    state = 0
                    word = ""

            elif state == 33: #For Const
                if char == "t":
                    state = 34
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' \n")
                    state = 0
                    word = ""
            
            elif state == 35: #For Create
                if char == "e":
                    state = 36
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(":
                    state = 141
                    word = char
                    target_word = "Create"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '(' \n")
                    state = 0
                    word = ""

            elif state == 40: #For Def, Do, Destroy, Display
                if char == "e":
                    state = 41
                    word += char
                    
                elif char == "o": #For Do
                    state = 48
                    word += char
                    
                elif char == "i": #For Do
                    state = 49
                    word += char
                    
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
                elif char == "s": #For Destroy
                    state = 43
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ':' \n")
                    state = 0
                    word = ""
            
            elif state == 43: #For Destroy
                if char == "t":
                    state = 44
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    # fixed test item 5, "first character after destroy appears in terminal instead in lexeme"
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<null>' \n")
                    state = 0
                    word = ""
            
            elif state == 48: #Final state for Do
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Do"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(":
                    state = 141
                    word = char
                    target_word = "Do"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "{":
                    state = 139
                    word = char
                    target_word = "Do"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or <openbrace> or ( \n")
                    state = 0
                    word = ""
            
            elif state == 49: #For Display
                if char == "s":
                    state = 50
                    word += char
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
                    state = 175
                    word = ""
                    target_word = "Display"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == '"': #reminder, bug for the pieceliteral, should read #,pieceliteral,# instead of "pieceliteral"
                    state = 167
                    word = ""
                    target_word = "Display"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, '"\n')  # Add opening quote token
                    token_output.insert(tk.END, '"\n')
                else:
                    output_text.insert(tk.END, f'Line {line_number + 1}: Lexical error at position {index}: should be <space> or " \n')
                    state = 0
                    word = ""
            
            elif state == 55: #For Flip
                if char == "l":
                    state = 56
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""
            
            elif state == 59: #For Ifsnap
                if char == "f":
                    state = 60
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "{":
                    word = char
                    target_word = "Ifsnap"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    state = 139 #state of {
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '<open_curly_brace>'\n")
                    state = 0
                    word = ""

            elif state == 65: #For Link
                if char == "i":
                    state = 66
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""

            elif state == 69: #For Pane Piece Put
                if char == "a":
                    state = 70
                    word += char
                elif char == "i":
                    state = 73
                    word += char
                elif char == "u":
                    state = 77
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(":
                    state = 141
                    word = char
                    target_word = "Pane"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '('\n")
                    state = 0
                    word = ""
            
            elif state == 73: #For Piece
                if char == "e":
                    state = 74
                    word += char
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 74: #For Piece
                if char == "c":
                    state = 75
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""
            
            elif state == 77: #For Put
                if char == "t":
                    state = 78
                    word += char
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't' \n")
                    state = 0
                    word = ""
            
            elif state == 78: #Final state for Put
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Put"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(":
                    state = 0
                    word = ""
                    target_word = "Put"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "(\n")
                    token_output.insert(tk.END, "(\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""
            
            elif state == 79: #For Revoid
                if char == "e":
                    state = 80
                    word += char
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
                elif char == "b": #FPr Rebrick
                    state = 85
                    word += char
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
                    state = 145
                    word = ""
                    target_word = "Revoid"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n") 
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<semicolon>'\n")
                    state = 0
                    word = ""

            elif state == 85: #For Rebrick
                if char == "r":
                    state = 86
                    word += char
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
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'k' \n")
                    state = 0
                    word = ""
            
            elif state == 89: #Final state for Rebrick
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Rebrick"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == ";":
                    state = 145
                    word = ""
                    target_word = "Rebrick"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '<semicolon>'\n")
                    state = 0
                    word = ""
            
            elif state == 90: #For Stable, Snap, Snapif, Subs
                if char == "t":
                    state = 91
                    word += char
                elif char == "n": #Snap and Snapif
                    state = 96
                    word += char
                elif char == "e": #For Set
                    state = 101
                    word += char
                elif char == "u": #For Set
                    state = 103
                    word += char
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
                    state = 145
                    word = ""
                    target_word = "Stable"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<semicolon>'\n")
                    state = 0
                    word = ""
            
            elif state == 96: #For Snap
                if char == "a":
                    state = 97
                    word += char
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
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'p' \n")
                    state = 0
                    word = ""

            elif state == 98: #Final state for Snap
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Snap"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "\n":
                    state = 0
                    word = ""
                    target_word = "Snap"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "{":
                    state = 139
                    word = ""
                    target_word = "Snap"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "i": #For Snapif 
                    state = 99
                    word += char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<open_curly_brace>' or 'i'\n")
                    state = 0
                    word = ""
            
            elif state == 99: #For Snapif
                if char == "f":
                    state = 100
                    word += char
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'f' \n")
                    state = 0
                    word = ""

            elif state == 100: #Final state for Snapif
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Snapif"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(":
                    state = 141
                    word = ""
                    target_word = "Snapif"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '('\n")
                    state = 0   
                    word = ""
            
            elif state == 101: #For Set
                if char == "t":
                    state = 102
                    word += char
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 't' \n")
                    state = 0
                    word = ""
            
            elif state == 102: #Final state for Set
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Set"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "{":
                    state = 139
                    word = ""
                    target_word = "Set"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '<open_curly_brace'\n")
                    state = 0   
                    word = ""
            
            elif state == 103: #For Subs
                if char == "b":
                    state = 104
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0   
                    word = ""
            
            elif state == 106: #For While Wobble
                if char == "h": #For While 
                    state = 107
                    word += char
                elif char == "o": #For Wobble
                    state = 111
                    word += char
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
                elif char == "":
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}\n")
                    word = ""
                    state = 0
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'e' \n")
                    state = 0
                    word = ""
            
            elif state == 110: #Final state for While
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "While"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(":
                    state = 0
                    word = ""
                    target_word = "While"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "(")
                    token_output.insert(tk.END, "(")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>' or '(' \n")
                    state = 0   
                    word = ""

            elif state == 111: #For Wobble 
                if char == "b":
                    state = 112
                    word += char
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, ";\n")
                    token_output.insert(tk.END, ";\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<semicolon>' \n")
                    state = 0   
                    word = ""
            
            elif state == 116: #Final state for '='
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "=" #For '=='
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "=": #For Snapif
                    state = 117
                    word = char
                elif char.islower():
                    state = 20
                    target_word = "=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 117: #Final state for '=='
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word = char
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "==" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 118: #Final state for '+'
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word = ""
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "=": #For Snapif
                    state = 119
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "+" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 119: #Final state for '+='
                if char == " ":
                    state = 0
                    word = char
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "+=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 120: #Final state for '-'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "-"  
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "=": #For Snapif
                    state = 121
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "-" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 121: #Final state for '-='
                if char == " ":
                    state = 0
                    word = char
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "-=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 122: #Final state for '*'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "=": #For Snapif
                    state = 123
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "*" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 123: #Final state for '*='
                if char == " ":
                    state = 0
                    word = char
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "*=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 124: #Final state for '/'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "=": #For Snapif
                    state = 125
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "/" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 125: #Final state for '/='
                if char == " ":
                    state = 0
                    word = char
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "/="
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "/=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 126: #Final state for '%'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "=": #For Snapif
                    state = 127
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "%" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 127: #Final state for '%='
                if char == " ":
                    state = 0
                    word = char
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "%=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 128: #Final state for '!'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == "!":
                    state = 129
                    word += char
                elif char == "=": #For Snapif
                    state = 130
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or '(' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 129: #Final state for '!!'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "!!" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or '(' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 130: #Final state for '!='
                if char == " ":
                    state = 0
                    word += char
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char.islower():
                    state = 20
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "!=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 131: #Final state for '<'
                if char == " ":
                    state = 0
                    word = char
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "=": #For Snapif
                    state = 132
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "<" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 132: #Final state for '<='
                if char == " ":
                    state = 0
                    word += char
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char.islower():
                    state = 20
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "<=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 133: #Final state for '>'
                if char == " ":
                    state = 0
                    word += char
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "=": #For Snapif
                    state = 134
                    word += char
                elif char.islower():
                    state = 20
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = ">" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 134: #Final state for '>='
                if char == " ":
                    state = 0
                    word += char
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char.islower():
                    state = 20
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = ">=" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 135: #Final state for '&'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "&" 
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                elif char == "&": #For Snapif
                    state = 136
                    word += char
                elif char.islower():
                    state = 20
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 136: #Final state for '&&'
                if char == " ":
                    state = 0
                    word =""
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "&&" 
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "&&" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 137: #Final state for '|'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "|": 
                    state = 138
                    word += char
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "|" 
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "|" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 138: #Final state for '||'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "||" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "(": 
                    state = 141
                    word += char
                    target_word = "||" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char.islower():
                    state = 20
                    target_word = "||" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "||" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "||" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '=' or 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
            
            elif state == 139: #Final state for '{'
                if char == " ":
                    state = 0
                    word += char
                    target_word = "{" 
                    lexeme_output.insert(tk.END, "{\n")
                    token_output.insert(tk.END, "{\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "\n":
                    state = 0
                    word += char
                    target_word = "{" 
                    lexeme_output.insert(tk.END, "{\n")
                    token_output.insert(tk.END, "{\n")

                elif char.islower():
                    state = 20
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "{":
                    state = 139
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "{" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'open curly bracket' or 'alphanum' or 'space' or 'newline '\n")
                    state = 0
                    word = ""

            elif state == 140: #Final state for '}'
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "}" 
                    lexeme_output.insert(tk.END, "}\n")
                    token_output.insert(tk.END, "}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "\n":
                    state = 0
                    word = ""
                    target_word = "}" 
                    lexeme_output.insert(tk.END, "}\n")
                    token_output.insert(tk.END, "}\n")
                elif char.islower():
                    state = 20
                    target_word = "}" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "{":
                    state = 139
                    target_word = '}' 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "}" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "}" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'open curly bracket' or 'alphanum' or 'space' or 'newline '\n")
                    state = 0
                    word = ""

            elif state == 141: #Final state for '('
                if char == " ":
                    target_word = "(" 
                    lexeme_output.insert(tk.END, "(\n")
                    token_output.insert(tk.END, "(\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                    word = ""
                    state = 0
                elif char == "\n":
                    target_word = "("
                    lexeme_output.insert(tk.END, "(\n")
                    token_output.insert(tk.END, "(\n")
                    word = ""
                elif char == ")":
                    state = 142
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.islower():
                    state = 20
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "{":
                    state = 139
                    target_word = '(' 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "(" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isspace():
                     state = 141
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'open curly bracket' or 'alphanum' or 'space' or 'newline '\n")
                    state = 0
                    word = ""

            elif state == 142: #Final state for ')'
                if char == " ":
                    state = 0
                    word = ""
                    target_word = ")" 
                    lexeme_output.insert(tk.END, ")\n")
                    token_output.insert(tk.END, ")\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "\n":
                    state = 0
                    word = ""
                    target_word = ")"
                    lexeme_output.insert(tk.END, ")\n")
                    token_output.insert(tk.END, ")\n")
                elif char == ";": # Semicolon
                        target_word = ")"
                        lexeme_output.insert(tk.END, f"{target_word}\n")
                        token_output.insert(tk.END, f"{target_word}\n")
                        state = 145
                        word = ""
                elif char.islower():
                    state = 20
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "{":
                    state = 139
                    target_word = ')' 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = ")" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'open curly bracket' or 'alphanum' or 'space' or 'newline '\n")
                    state = 0
                    word = ""

            elif state == 143: #Final state for '['
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "[" 
                    lexeme_output.insert(tk.END, "[\n")
                    token_output.insert(tk.END, "[\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char.islower():
                    state = 20
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "{":
                    state = 139
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "[" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'open curly bracket' or 'alphanum' or 'space' or 'newline '\n")
                    state = 0
                    word = ""

            elif state == 144: #Final state for ']'
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "]" 
                    lexeme_output.insert(tk.END, "]\n")
                    token_output.insert(tk.END, "]\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char.islower():
                    state = 20
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == ";":
                    state = 145
                    target_word = ']' 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "[":
                    state = 143
                    target_word = ']' 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "{":
                    state = 139
                    target_word = ']' 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "]" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'open curly bracket' or 'alphanum' or 'space' or 'newline '\n")
                    state = 0
                    word = ""

            elif state == 145: #Final state for ';'
                if char == " ":
                    state = 0
                    word += char
                    target_word = ";" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "\n":
                    state = 0
                    word += char
                    target_word = ";"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'space'\n")
                    state = 0
                    word = ""


            # FOR LINKLIT ---------------------------------------------------------------------------------------------------------------------------------
            elif state == 146: # ~[digit1] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 147
                elif char == ".":
                    word += char
                    target_word = "."
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Close brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 147: # ~[digit2] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 148
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 148: # ~[digit3] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 149
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 149: # ~[digit4] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 150
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""
            
            elif state == 150: # ~[digit5] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 151
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 151: # ~[digit6] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 152
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 152: # ~[digit7] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 153
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 153: # ~[digit8] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 154
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 154: # ~[digit9] [LINK LITERAL]
                if char.isdigit():
                    word += char
                    state = 155
                elif char == ".":
                    word += char
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Linklit\n")
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
                    state = 156
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Linklit\n")
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
                    state = 157
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 157: #[digit2] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 158

                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 158: #[digit3] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 159

                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 159: #[digit4] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 160

                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 160: #[digit5] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 161

                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 161: #[digit6] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 162

                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 162: #[digit7] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 163
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 163: #[digit8] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 164

                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 164: #[digit9] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    state = 165

                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""
            
            elif state == 165: #[digit10] [BUBBLE LITERAL]
                if char.isdigit():
                    word += char
                    output_text.insert(tk.END, f"Lexical error: Limit reached\n")
                
                elif char == " ":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\n":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "\t":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "+": # positive
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 118
                        word = ""
                elif char == "-": # negative
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 120
                        word = ""
                elif char == "*": # multiply
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 122
                        word = ""
                elif char == "/": # division
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 124
                        word = ""
                elif char == "%": # modulo
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 126
                        word = ""
                elif char == "?": # question
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 0
                        word = ""
                elif char == "!": # not
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 128
                        word = ""
                elif char == "~": # tilde
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 146
                        word = ""
                elif char == "<": # less than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 131
                        word = ""
                elif char == ">": # greater than
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 133
                        word = ""
                elif char == "=": # equal
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 116
                        word = char
                elif char == "(": # open parenthesis
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 141
                        word = ""
                elif char == ")": # closed parenthesis
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 142
                        word = ""
                elif char == "[": # Open brace 
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 143
                        word = ""
                elif char == "]": # Open brace
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 144
                        word = ""
                elif char == ",": # Comma
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 173
                        word = ""
                elif char == "}": # Closed curly brace
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 140
                        word = ""
                elif char == ";": # Semicolon
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 145
                        word = ""
                elif char == ":": # Colon
                        lexeme_output.insert(tk.END, f"{char}\n")
                        token_output.insert(tk.END, f"Bubblelit\n")
                        state = 174
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 0
                        word = ""

            elif state == 166: #[delimeter] [BUBBLE LITERAL]
                if char in {" ", "\n", "\t", "+", "-", "*", "/", "%", "?", "!", "~", "<", ">", "=", "(", ")", "[", "]", ",", "}", ";"}:
                        lexeme_output.insert(tk.END, f" {char}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1}  Bubblelit {word}\n")
                        state = 0
                        word = ""
                else:
                        output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                        state = 166
                        word = ""

            

            elif state == 167: #[first input] [PIECE LITERAL]
                if 32 <= ord(char) <= 33 or 35 <= ord(char) <= 126:
                                     
                    word += char
                elif char == '"':
                    state = 169
                    lexeme_output.insert(tk.END, f"{word}\n")  # Output the string content
                    token_output.insert(tk.END, f"Piecelit\n")
                    lexeme_output.insert(tk.END, '"\n')  # Add closing quote token
                    token_output.insert(tk.END, '"\n')
                    word = ""
                else:
                    state = 168
            
            elif state == 555: #[first input] [PIECE LITERAL]
                if char == "#":
                    word += char
                    lexeme_output.insert(tk.END, f"{word}")   
                    state = 556
                else:
                    state == 0
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be ""#"" \n")

            elif state == 556: #[first input] [PIECE LITERAL]
                if 32 <= ord(char) <= 34 or 36 <= ord(char) <= 126:
                    lexeme_output.insert(tk.END, f"{char}")                       
                    word += char
                elif char == "\n":
                    lexeme_output.insert(tk.END, f"{char}")  
                    token_output.insert(tk.END, f"Comment {word} \n")
                    state = 0
                    word = ""
                else:
                    state == 0
                    word = ""
            
            elif state == 557: #[piece_delim] [PIECE LITERAL]
                if char == " ":
                    lexeme_output.insert(tk.END, f" {char}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 0
                    word = ""
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                    state = 0
                    word = ""

            elif state == 169: #[piece_delim] [PIECE LITERAL]
                if char == " ":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 0
                    word = ""
                elif char == ";":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 145 #state of ;
                    word = char
                elif char == "{":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 139 #state of {
                    word = ""
                elif char == "}":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 140 #state of }
                    word = ""
                elif char == ")":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 142 #state of )
                    word = ""
                elif char == "~":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 146 #state of ~
                    word = ""
                elif char == "=":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 116 #state of =
                    word = ""
                elif char == ":":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
                    state = 174 #state of ;
                    word = char
                elif char == ",":
                    state = 173 #state of ,
                    word = ""
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                    state = 0
                    word = ""

            elif state == 170: #[piece_comment ascii] [PIECE LITERAL]
                if char == "#":
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, f"Line {line_number + 1}  {char} test\n")
                        state = 171
                        word += char
                

            elif state == 171: #[piece_comment ascii] [PIECE LITERAL]
                if 32 <= ord(char) <= 34 or 36 <= ord(char) <= 125:
                    lexeme_output.insert(tk.END, f" {char}\n")                       
                    word += char
                elif char == "A":
                    lexeme_output.insert(tk.END, f" {char} test\n") 
                    token_output.insert(tk.END, f"Line {line_number + 1}  {char} test\n") 
                    state = 172
                    word += char
                

            elif state == 172: #[piece_comment delim] [PIECE LITERAL]
                if char == "A":
                    lexeme_output.insert(tk.END, f" {char}\n")
                    token_output.insert(tk.END, f"Piecelit\n")
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
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char.islower():
                    state = 20
                    target_word = "," 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isupper():
                    state = 20
                    target_word = "," 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char.isdigit():
                    state = 146
                    target_word = "," 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'alphanum' or 'space'\n")
                    state = 0
                    word = ""
                
            elif state == 174: #Final state for ':'
                if char == " ":
                    state = 0
                    word += char
                    target_word = ":" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                elif char == "{":
                    state = 139
                    target_word = ":" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                elif char == "\n":
                    state = 0
                    target_word = ":" 
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    word = char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be 'open curly bracket' or 'newline' or 'space'\n")
                    state = 0
                    word = ""

            elif state == 175:
                if char == '"':
                    state = 167
                    lexeme_output.insert(tk.END, '"\n')  # Output opening quote
                    token_output.insert(tk.END, '"\n')
                    word = ""
                else:
                    output_text.insert(tk.END, f'Line {line_number + 1}: Lexical error at position {index}: Expected " after Display <space>\n')
                    state = 0
                    word = ""

            elif state == 2:
                if char == "i":
                    state = 3
                    word += char
                elif char == "b":
                    state = 7
                    word += char
                    target_word = "Bubble"
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'i' or 'b' after 'Bu'\n")
                    state = 0
                    word = ""

            # Build transitions
            elif state == 3:
                if char == "l":
                    state = 4
                    word += char
                    
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'l' after 'Bui'\n")
                    state = 0
                    word = ""

            elif state == 4:
                if char == "d":
                    state = 5
                    word += char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'd' after 'Buil'\n")
                    state = 0
                    word = ""

            elif state == 5:  # Expect newline immediately after "Build"
                if char == "\n" or char == " " or char == "\t":
                    word = ""
                    target_word = "Build"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
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
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'b' after 'Bub'\n")
                    state = 0
                    word = ""

            elif state == 8:
                if char == "l":
                    state = 9
                    word += char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'l' after 'Bubb'\n")
                    state = 0
                    word = ""

            elif state == 9:
                if char == "e":
                    state = 10
                    word += char
                else:
                    
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'e' after 'Bubbl'\n")
                    state = 0
                    word = ""

            elif state == 10:  #Final state for Bubble
                if char == " ":
                    state = 0
                    word = ""
                    target_word = "Bubble"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    lexeme_output.insert(tk.END, "Space\n")
                    token_output.insert(tk.END, "Space\n")
                else:
                    lexeme_output.insert(tk.END, f" {char}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: should be '<space>'\n")
                    state = 0
                    word = ""

            # Base transitions
            elif state == 11:
                if char == "s":
                    state = 12
                    word += char
                    
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 'a' after 'B'\n")
                    state = 0
                    word = ""

            elif state == 12:
                if char == "e":
                    state = 13
                    word += char
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected 's' after 'Ba'\n")
                    state = 0
                    word = ""

            elif state == 13:
                if char == " " or char == "\n" or char == "\t":
                    target_word = "Base"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                    state = 0  # Reset state for further processing
                    word = ""
                elif char == "\n":
                    state = 0
                    word = ""
                elif char == '"':
                    state = 167
                    word = ""
                    target_word = "Base"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif char == ":":
                    state = 174
                    word = ""
                    target_word = "Base"
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    token_output.insert(tk.END, f"{target_word}\n")
                elif not char.isspace():
                    lexeme_output.insert(tk.END, f"{target_word}\n")
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected space, colon, newline, or tab after 'Base'\n")
                    state = 0
                    word = ""
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Expected space, colon, newline, or tab after 'Base'\n")
                    state = 0
                    word = ""

            # Identifier transitions
            elif state == 20: # ID 2
                if char.islower() or char.isupper() or char == "_" or char.isdigit():
                    word += char
                elif char.isspace():
                    if word and len(word.strip()) > 0 and not word.isspace():  # Only output if we have a word
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, "Identifier\n")
                        word = ""
                        state = 0
                elif char == ";":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 145 #state of ;
                    word = ""
                elif char == "{":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 139 #state of {
                    word = ""
                elif char == "}":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 140 #state of }
                    word = ""
                elif char == ")":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 142 #state of )
                    word += char
                elif char == "~":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 146 #state of ~
                    word = ""
                elif char == "(":
                    if word:  # Only output if we have a word
                        lexeme_output.insert(tk.END, f"{word}\n")
                        token_output.insert(tk.END, "Identifier\n")
                    state = 141 #state of (
                    word = ""
                elif char == "[": 
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 143  #state of [
                    word = ""   
                elif char == "]": 
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 144 #state of ]
                    word = ""
                elif char == "=": 
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 116 #state of ]
                    word = ""
                elif char == ">": 
                        state = 133 #state of >
                        word = ""    
                elif char == " ": 
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 0 
                    word = ""
                elif char == ",":
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 173
                    word = ","
                elif char == "\n": 
                    lexeme_output.insert(tk.END, f"{word}\n")
                    token_output.insert(tk.END, "Identifier\n")
                    state = 0 
                    word = ""
                else:
                    output_text.insert(tk.END, f"Line {line_number + 1}: Lexical error at position {index}: Invalid character in identifier\n")
                    state = 0
                    word = ""

            
# Create the main Tkinter window
root = tk.Tk()
root.title("LEGO Code Analyzer")
root.geometry("1200x1000")
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
lexical_label = tk.Label(root, text="Code Analyzer", bg="red", fg="white",
                         font=("Arial", 20, "bold"))
lexical_label.place(relx=0.02, rely=0.68, relwidth=0.6, height=50)
 
# --- MAIN INPUT FRAME (BIG BLACK BOX WITH YELLOW BORDER) ---
input_frame = tk.Frame(root, bg="yellow", bd=5)
input_frame.place(relx=0.02, rely=0.15, relwidth=0.6, relheight=0.5)

# Move function definitions before widget creation
def update_line_numbers(event=None):
    lines = input_entry.get("1.0", "end-1c").split("\n")
    line_numbers.config(state=tk.NORMAL)
    line_numbers.delete("1.0", tk.END)
    line_numbers.insert("1.0", "\n".join(str(i) for i in range(1, len(lines) + 1)))
    line_numbers.config(state=tk.DISABLED)

def on_text_change(event=None):
    """Handle text changes including copy-paste"""
    update_line_numbers()
    process_input(event)

# INNER FRAME TO HOLD LINE NUMBERS AND INPUT
inner_frame = tk.Frame(input_frame)
inner_frame.pack(fill="both", expand=True)

# Modify the inner frame setup and line number synchronization
def sync_input_scroll(*args):
    """Synchronize input text and line numbers scrolling"""
    # Sync line numbers with input text
    if len(args) > 0:
        # Store current positions
        line_pos = line_numbers.yview()
        input_pos = input_entry.yview()
        
        # Update both widgets
        line_numbers.yview_moveto(args[0])
        input_entry.yview_moveto(args[0])
        
        # Verify positions are synced
        if line_numbers.yview() != input_entry.yview():
            # Re-sync if needed
            line_numbers.yview_moveto(input_entry.yview()[0])

# Add scrollbar for input text
input_scrollbar = tk.Scrollbar(inner_frame)
input_scrollbar.pack(side="right", fill="y")

# Modify line numbers widget
line_numbers = tk.Text(inner_frame, width=4, bg="lightgray", fg="black",
                      font=("Consolas", 14), yscrollcommand=sync_input_scroll)
line_numbers.pack(side="left", fill="y")
line_numbers.config(state=tk.DISABLED)

# Modify input entry widget
input_entry = tk.Text(inner_frame, bg="white", fg="black", font=("Consolas", 14),
                     yscrollcommand=sync_input_scroll)
input_entry.pack(side="left", fill="both", expand=True)

# Configure scrollbar
input_scrollbar.config(command=sync_input_scroll)

# Update mousewheel handling
def on_input_mousewheel(event):
     # Store positions before scroll
    current_pos = input_entry.yview()[0]
    
    # Scroll both widgets
    line_numbers.yview_scroll(int(-1*(event.delta/120)), "units")
    input_entry.yview_scroll(int(-1*(event.delta/120)), "units")
    
    # Ensure synchronization
    if line_numbers.yview() != input_entry.yview():
        line_numbers.yview_moveto(input_entry.yview()[0])
    
    return "break"

# Bind mousewheel to both text widgets
line_numbers.bind("<MouseWheel>", on_input_mousewheel)
input_entry.bind("<MouseWheel>", on_input_mousewheel)

# Bind events after both widgets are created
input_entry.bind("<KeyRelease>", on_text_change)

# Update the line numbers update function
def update_line_numbers(event=None):
    """Update line numbers with proper synchronization"""
    # Get all lines including empty ones at the end
    content = input_entry.get("1.0", "end-1c")
    lines = content.split("\n")
    total_lines = len(lines)

    # Store current view position
    current_pos = input_entry.yview()[0]
    
    # Update line numbers
    line_numbers.config(state=tk.NORMAL)
    line_numbers.delete("1.0", tk.END)
    line_numbers.insert("1.0", "\n".join(str(i) for i in range(1, total_lines + 1)))
    line_numbers.config(state=tk.DISABLED)
    
    # Restore view position
    line_numbers.yview_moveto(current_pos)
    input_entry.yview_moveto(current_pos)

input_entry.bind("<<Modified>>", on_text_change)  # Catches all text modifications
input_entry.bind("<KeyRelease>", on_text_change)  # Catches keyboard input
 
 
# --- OUTPUT SECTION WITH NOTEBOOK ---
output_notebook_frame = tk.Frame(root, bg="#004080", bd=2)
output_notebook_frame.place(relx=0.02, rely=0.75, relwidth=0.6, relheight=0.2)

# Create notebook
output_notebook = ttk.Notebook(output_notebook_frame)
output_notebook.pack(fill="both", expand=True)

# Create frames for each tab
lexical_tab = tk.Frame(output_notebook, bg="#004080")
syntax_tab = tk.Frame(output_notebook, bg="#004080")
semantic_tab = tk.Frame(output_notebook, bg="#004080")

# Add frames to notebook
output_notebook.add(lexical_tab, text="Lexical Analysis")
output_notebook.add(syntax_tab, text="Syntax Analysis")
output_notebook.add(semantic_tab, text="Semantic Analysis")

# Lexical Error Output
output_text = tk.Text(lexical_tab, bg="black", fg="white", font=("Consolas", 12),
                      state="normal")
output_text.pack(fill="both", expand=True)
output_text.bind("<Key>", lambda e: "break")
output_text.bind("<Button-1>", lambda e: "break")

# Syntax Error Output
syntax_output_text = tk.Text(syntax_tab, bg="black", fg="white", font=("Consolas", 12),
                      state="normal")
syntax_output_text.pack(fill="both", expand=True)
syntax_output_text.bind("<Key>", lambda e: "break")
syntax_output_text.bind("<Button-1>", lambda e: "break")

# Semantic Error Output
semantic_output_text = tk.Text(semantic_tab, bg="black", fg="white", font=("Consolas", 12),
                      state="normal")
semantic_output_text.pack(fill="both", expand=True)
semantic_output_text.bind("<Key>", lambda e: "break")
semantic_output_text.bind("<Button-1>", lambda e: "break")

# --- TOKEN HEADER AND BOX ---
token_table_frame = tk.Frame(root, bg="#004080", bd=2)
token_table_frame.place(relx=0.81, rely=0.15, relwidth=0.18, relheight=0.8)

# Add scrollbar for token output
token_scrollbar = tk.Scrollbar(token_table_frame)
token_scrollbar.pack(side="right", fill="y")

# Token Label
token_label = tk.Label(token_table_frame, text="Token", bg="#004080", fg="white",
                       font=("Arial", 12, "bold"))
token_label.pack(side="top", fill="x")

# Token Output Box with scrollbar
token_output = tk.Text(token_table_frame, bg="black", fg="white", 
                      font=("Consolas", 12), wrap="none",
                      yscrollcommand=token_scrollbar.set)
token_output.pack(fill="both", expand=True)
token_scrollbar.config(command=token_output.yview)

# --- LEXEME HEADER AND BOX ---
lexeme_table_frame = tk.Frame(root, bg="#004080", bd=2)
lexeme_table_frame.place(relx=0.63, rely=0.15, relwidth=0.18, relheight=0.8)

# Add scrollbar for lexeme output
lexeme_scrollbar = tk.Scrollbar(lexeme_table_frame)
lexeme_scrollbar.pack(side="right", fill="y")

# Lexeme Label
lexeme_label = tk.Label(lexeme_table_frame, text="Lexeme", bg="#004080", fg="white",
                        font=("Arial", 12, "bold"))
lexeme_label.pack(side="top", fill="x")

# Lexeme Output Box with scrollbar
lexeme_output = tk.Text(lexeme_table_frame, bg="black", fg="white", 
                       font=("Consolas", 12), wrap="none",
                       yscrollcommand=lexeme_scrollbar.set)
lexeme_output.pack(fill="both", expand=True)
lexeme_scrollbar.config(command=lexeme_output.yview)

# Function to sync scrolling
def sync_scroll(*args):
    # Sync both text widgets
    lexeme_output.yview_moveto(args[0])
    token_output.yview_moveto(args[0])

# Configure scrollbars to use sync_scroll
lexeme_scrollbar.config(command=sync_scroll)
token_scrollbar.config(command=sync_scroll)

# Bind mousewheel events
def on_mousewheel(event):
    lexeme_output.yview_scroll(int(-1*(event.delta/120)), "units")
    token_output.yview_scroll(int(-1*(event.delta/120)), "units")
    return "break"

# Bind mousewheel to both text widgets
lexeme_output.bind("<MouseWheel>", on_mousewheel)
token_output.bind("<MouseWheel>", on_mousewheel)

# Keep existing input prevention bindings
lexeme_output.bind("<Key>", lambda e: "break")
lexeme_output.bind("<Button-1>", lambda e: "break")
token_output.bind("<Key>", lambda e: "break")
token_output.bind("<Button-1>", lambda e: "break")

#lexical analysis button
lexical_button = tk.Button(root, 
    text="Lexical Analyzer",
    command=run_lexical_analysis,
    bg="#004080",  # Dark blue background
    fg="white",    # White text
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    relief=tk.RAISED,
    bd=3)
lexical_button.place(relx=0.02, rely=0.08, relwidth=0.15, relheight=0.05)

#syntax analysis button
syntax_button = tk.Button(root, 
    text="Syntax Analyzer",
    command=run_syntax_analysis,
    bg="#004080",  # Dark blue background
    fg="white",    # White text
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    relief=tk.RAISED,
    bd=3)
syntax_button.place(relx=0.18, rely=0.08, relwidth=0.15, relheight=0.05)

#semantic analysis button
semantic_button = tk.Button(root, 
    text="Semantic Analyzer",
    command=run_semantic_analysis,
    bg="#004080",  # Dark blue background
    fg="white",    # White text
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    relief=tk.RAISED,
    bd=3)
semantic_button.place(relx=0.34, rely=0.08, relwidth=0.15, relheight=0.05)

def open_file():
    from tkinter import filedialog
    
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                # clear
                input_entry.delete("1.0", tk.END)
                
                # read and insert
                content = file.read()
                input_entry.insert("1.0", content)
                
                # update line numbers
                update_line_numbers()
                
                # clear output boxes
                lexeme_output.delete("1.0", tk.END)
                token_output.delete("1.0", tk.END)
                output_text.delete("1.0", tk.END)
                
                # show success
                output_text.insert(tk.END, f"File loaded successfully: {file_path}\n")
        except Exception as e:
            output_text.insert(tk.END, f"Error opening file: {str(e)}\n")

# file open button
open_button = tk.Button(root, 
    text="Open File",
    command=open_file,
    bg="#004080",  # Dark blue bg
    fg="white",    # White text
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    relief=tk.RAISED,
    bd=3)
open_button.place(relx=0.64, rely=0.08, relwidth=0.15, relheight=0.05)

# file save button
save_button = tk.Button(root, 
    text="Save File",
    command=save_file,
    bg="#004080",  # Dark blue bg
    fg="white",    # White text
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    relief=tk.RAISED,
    bd=3)
save_button.place(relx=0.82, rely=0.08, relwidth=0.15, relheight=0.05)

# run app
root.mainloop()
