class SyntaxAnalyzer:
    def __init__(self, tokens, lines):
        self.tokens = [token for token in tokens if token.strip() != "Space"]  # Filter out "Space" tokens
        self.lines = lines  # Original input lines for line tracking
        self.current_index = 0
        self.current_line = 1  # Start at line 1

    def analyze(self):
        """Starts parsing the program"""
        self.program()

    def program(self):
        """Parses the overall Lego-C program structure"""
        self.match_and_advance("Build", "program start")
        self.global_declaration()
        self.subs_functions()
        self.link_pane()
        self.match_and_advance("Destroy", "program end")

    def global_declaration(self):
        """Parses global declarations, ensuring Link Pane() is not mistaken for a variable"""
        self.debug_tokens()
        while self.peek_next_token() and self.peek_next_token() in ["Link", "Bubble", "Piece", "Flip", "Const", "Set"]:
            # Check for Link Pane() before proceeding to variable or array parsing
            if (self.peek_next_token() == "Link" and 
                self.current_index + 1 < len(self.tokens) and 
                self.tokens[self.current_index + 1] == "Pane" and 
                self.current_index + 2 < len(self.tokens) and 
                self.tokens[self.current_index + 2] == "("):
                return  # Exit early to let link_pane() handle the main function
            
            token = self.peek_next_token()
            if token in ["Link", "Bubble", "Piece", "Flip"]:
                if self.peek_two_tokens_ahead() == "[":
                    self.array_declaration()  # Handle array declarations
                else:
                    self.variable_declaration()  # Handle variable declarations
            elif token == "Const":
                self.const_declaration()
            elif token == "Set":
                self.struct_declaration()
            self.debug_tokens()  # Debug after each declaration to track progress

    def subs_functions(self):
        """Parses zero or more sub function declarations"""
        while self.peek_next_token() and self.peek_next_token() == "Subs":
            self.subfunction_declaration()

    def subfunction_declaration(self):
        """Parses a subfunction"""
        self.match_and_advance("Subs", "subfunction start")
        self.match_and_advance("Identifier", "subfunction name")
        self.match_and_advance("(", "parameter list open")
        self.parameter_list()
        self.match_and_advance(")", "parameter list close")
        self.match_and_advance("{", "subfunction body open")
        self.body()
        self.match_and_advance("}", "subfunction body close")

    def link_pane(self):
        """Parses 'Link Pane()' main function"""
        if self.peek_next_token() != "Link":
            raise SyntaxError(f"Line {self.current_line}: Expected 'Link' for main function, found '{self.peek_next_token()}'")
        self.match_and_advance("Link", "main function start")
        if self.peek_next_token() != "Pane":
            raise SyntaxError(f"Line {self.current_line}: Expected 'Pane' after 'Link', found '{self.peek_next_token()}'")
        self.match_and_advance("Pane", "main function name")
        self.match_and_advance("(", "main function params open")
        self.match_and_advance(")", "main function params close")
        self.match_and_advance("{", "main function body open")
        self.body()
        self.match_and_advance("Rebrick", "return statement")
        self.expression()
        self.match_and_advance(";", "return statement end")
        self.match_and_advance("}", "main function body close")

    def parameter_list(self):
        """Parses parameter list for functions"""
        if self.peek_next_token() in ["Link", "Bubble", "Piece", "Flip"]:
            self.data_type()
            self.match_and_advance("Identifier", "parameter name")
            while self.peek_next_token() == ",":
                self.match_and_advance(",", "parameter separator")
                self.data_type()
                self.match_and_advance("Identifier", "parameter name")

    def const_declaration(self):
        """Parses constant declarations"""
        self.match_and_advance("Const", "constant declaration")
        self.data_type()
        self.match_and_advance("Identifier", "constant name")
        self.match_and_advance("=", "constant assignment")
        self.expression()
        self.match_and_advance(";", "constant declaration end")

    def struct_declaration(self):
        """Parses structure declarations"""
        self.match_and_advance("Set", "struct declaration")
        self.match_and_advance("Identifier", "struct name")
        self.match_and_advance("{", "struct body open")
        while self.peek_next_token() in ["Link", "Bubble", "Piece", "Flip"]:
            self.variable_declaration()
        self.match_and_advance("}", "struct body close")

    def array_declaration(self):
        """Parses array declarations"""
        self.data_type()
        self.match_and_advance("Identifier", "array name")
        self.match_and_advance("[", "array size open")
        self.match_and_advance("Linklit", "array size")
        self.match_and_advance("]", "array size close")
        if self.peek_next_token() == "[":
            self.match_and_advance("[", "second dimension open")
            self.match_and_advance("Linklit", "second dimension size")
            self.match_and_advance("]", "second dimension close")
        if self.peek_next_token() == "=":
            self.match_and_advance("=", "array initialization")
            self.match_and_advance("{", "array values open")
            self.array_init()
            self.match_and_advance("}", "array values close")
        self.match_and_advance(";", "array declaration end")

    def array_init(self):
        """Parses array initialization values"""
        if self.peek_next_token() == "{":
            self.match_and_advance("{", "nested array open")
            self.array_init()
            self.match_and_advance("}", "nested array close")
            while self.peek_next_token() == ",":
                self.match_and_advance(",", "array value separator")
                self.match_and_advance("{", "nested array open")
                self.array_init()
                self.match_and_advance("}", "nested array close")
        else:
            self.literal()
            while self.peek_next_token() == ",":
                self.match_and_advance(",", "array value separator")
                self.literal()

    def body(self):
        """Parses function body"""
        while self.peek_next_token() and self.peek_next_token() not in ["}", "Rebrick"]:
            self.statements()
        if self.peek_next_token() == "}":
            return

    def statements(self):
        """Parses statements"""
        token = self.peek_next_token()
        if token in ["Link", "Bubble", "Piece", "Flip"]:
            if self.peek_two_tokens_ahead() == "[":
                self.array_declaration()
            else:
                self.variable_declaration()
        elif token == "Set":
            self.struct_declaration()
        elif token == "Create":
            self.input_statement()
        elif token == "Display":
            self.display_statement()
        elif token == "Ifsnap":
            self.if_statement()
        elif token == "Change":
            self.switch_statement()
        elif token in ["Put", "While", "Do"]:
            self.loop_statement()
        elif token == "Broke":
            self.match_and_advance("Broke", "break statement")
            self.match_and_advance(";", "break statement end")
        elif token == "Con":
            self.match_and_advance("Con", "continue statement")
            self.match_and_advance(";", "continue statement end")
        elif token.startswith("Identifier"):
            self.assignment_statement()
        elif token is None:
            raise SyntaxError(f"Line {self.current_line}: Unexpected end of input in statements")
        else:
            raise SyntaxError(f"Line {self.current_line}: Unexpected token '{token}' in statements")

    def variable_declaration(self):
        """Parses variable declarations, avoiding confusion with Link Pane()"""
        self.data_type()
        # Enhanced check to prevent misparsing Link Pane() as a variable
        if (self.peek_next_token() == "Pane" and 
            self.current_index + 1 < len(self.tokens) and 
            self.tokens[self.current_index + 1] == "("):
            raise SyntaxError(f"Line {self.current_line}: 'Link Pane()' should not appear in variable declarations; expected identifier")
        self.match_and_advance("Identifier", "variable name")
        if self.peek_next_token() == "=":
            self.match_and_advance("=", "variable assignment")
            self.expression()
        while self.peek_next_token() == ",":
            self.match_and_advance(",", "variable separator")
            self.match_and_advance("Identifier", "variable name")
            if self.peek_next_token() == "=":
                self.match_and_advance("=", "variable assignment")
                self.expression()
        self.match_and_advance(";", "variable declaration end")

    def data_type(self):
        """Parses data types"""
        token = self.peek_next_token()
        if token in ["Link", "Bubble", "Piece", "Flip"]:
            self.match_and_advance(token, "data type")
        else:
            raise SyntaxError(f"Line {self.current_line}: Expected data type, found '{token}'")

    def input_statement(self):
        """Parses input statement"""
        self.match_and_advance("Create", "input statement")
        self.match_and_advance("(", "input params open")
        self.match_and_advance("Identifier", "input variable")
        self.match_and_advance(")", "input params close")
        self.match_and_advance(";", "input statement end")

    def display_statement(self):
        """Parses display statement with adjusted flexibility"""
        self.match_and_advance("Display", "display statement")
        if self.peek_next_token() == '"':
            self.match_and_advance('"', "display format open")
            format_string = self.get_current_token()
            if format_string not in ["Piecelit", "Linklit", "Bubblelit", "Fliplit"]:
                raise SyntaxError(f"Line {self.current_line}: Expected format string literal, found '{format_string}'")
            self.advance()
            self.match_and_advance('"', "display format close")
        elif self.peek_next_token().startswith("Identifier"):
            self.match_and_advance("Identifier", "display variable")
        else:
            raise SyntaxError(f"Line {self.current_line}: Expected quoted literal or identifier after 'Display', found '{self.peek_next_token()}'")
        if self.peek_next_token() == ",":
            self.match_and_advance(",", "argument separator")
            self.expression()
        self.match_and_advance(";", "display statement end")

    def if_statement(self):
        self.match_and_advance("Ifsnap", "if statement")
        self.match_and_advance("(", "condition open")
        self.condition()
        self.match_and_advance(")", "condition close")
        
        # Check if next token is '{'
        if self.peek_next_token() == "{":
            self.match_and_advance("{", "if body open")
            self.body()
            self.match_and_advance("}", "if body close")
        else:
            # Single statement without braces
            self.statements()  # Parse a single statement
        
        # Handle optional Snapif clauses
        while self.peek_next_token() == "Snapif":
            self.match_and_advance("Snapif", "elseif statement")
            self.match_and_advance("(", "condition open")
            self.condition()
            self.match_and_advance(")", "condition close")
            if self.peek_next_token() == "{":
                self.match_and_advance("{", "elseif body open")
                self.body()
                self.match_and_advance("}", "elseif body close")
            else:
                self.statements()  # Single statement for Snapif
        
        # Handle optional Snap (else) clause
        if self.peek_next_token() == "Snap":
            self.match_and_advance("Snap", "else statement")
            if self.peek_next_token() == "{":
                self.match_and_advance("{", "else body open")
                self.body()
                self.match_and_advance("}", "else body close")
            else:
                self.statements()  # Single statement for Snap

    def switch_statement(self):
        """Parses switch statement"""
        self.match_and_advance("Change", "switch statement")
        self.match_and_advance("(", "switch expression open")
        self.match_and_advance("Identifier", "switch variable")
        self.match_and_advance(")", "switch expression close")
        self.match_and_advance("{", "switch body open")
        # Handle multiple Base cases
        while self.peek_next_token() == "Base":
            self.match_and_advance("Base", "case start")
            if self.peek_next_token() in ["Linklit", "Bubblelit", "Piecelit", "Fliplit"]:
                self.advance()  # Consume the literal for now, change it later for semantic analyzer
            self.match_and_advance(":", "case separator")
            # Parse case body (block or single/multiple statements)
            while self.peek_next_token() not in ["Base", "Def", "}", ""]:
                if self.peek_next_token() == "{":
                    self.match_and_advance("{", "case body open")
                    self.body()
                    self.match_and_advance("}", "case body close")
                else:
                    self.statements()
                # Handle Broke as a terminator
                if self.peek_next_token() == "Broke":
                    self.match_and_advance("Broke", "break statement")
                    self.match_and_advance(";", "break end")
                    break  # Exit inner loop after Broke
        
        # Handle optional Def case
        if self.peek_next_token() == "Def":
            self.match_and_advance("Def", "default case")
            self.match_and_advance(":", "default separator")
            while self.peek_next_token() not in ["}", ""]:
                if self.peek_next_token() == "{":
                    self.match_and_advance("{", "default body open")
                    self.body()
                    self.match_and_advance("}", "default body close")
                else:
                    self.statements()
                if self.peek_next_token() == "Broke":
                    self.match_and_advance("Broke", "break statement")
                    self.match_and_advance(";", "break end")
                    break
        
        self.match_and_advance("}", "switch body close")

    def loop_statement(self):
        """Parses loop statements"""
        token = self.peek_next_token()
        if token == "Put":
            self.for_loop()
        elif token == "While":
            self.while_loop()
        elif token == "Do":
            self.do_while_loop()

    def for_loop(self):
        """Parses for loop"""
        self.match_and_advance("Put", "for loop")
        self.match_and_advance("(", "for params open")
        if self.peek_next_token() != ";":
            if self.peek_next_token() in ["Link", "Bubble", "Piece", "Flip"]:
                self.variable_declaration()  # Rename to match your method
            else:
                self.assignment()
        self.match_and_advance(";", "init separator")
        
        # Condition
        if self.peek_next_token() != ";":
            self.condition()
        self.match_and_advance(";", "condition separator")
        
        # Update
        if self.peek_next_token() != ")":
            self.update_statement()
        self.match_and_advance(")", "loop close")
        
        # Body
        if self.peek_next_token() == "{":
            self.match_and_advance("{", "body open")
            self.body()
            self.match_and_advance("}", "body close")
        else:
            self.statements()

    def while_loop(self):
        """Parses while loop"""
        self.match_and_advance("While", "while loop")
        self.match_and_advance("(", "while condition open")
        self.condition()
        self.match_and_advance(")", "while condition close")
        self.match_and_advance("{", "while body open")
        self.body()
        self.match_and_advance("}", "while body close")

    def do_while_loop(self):
        """Parses do-while loop"""
        self.match_and_advance("Do", "do-while loop")
        self.match_and_advance("{", "do-while body open")
        self.body()
        self.match_and_advance("}", "do-while body close")
        self.match_and_advance("While", "do-while condition start")
        self.match_and_advance("(", "do-while condition open")
        self.condition()
        self.match_and_advance(")", "do-while condition close")
        self.match_and_advance(";", "do-while end")

    def assignment_statement(self):
        """Parses assignment statement"""
        self.match_and_advance("Identifier", "assignment variable")
        assign_op = self.peek_next_token()
        if assign_op in ["=", "+=", "-=", "*=", "/=", "%="]:
            self.match_and_advance(assign_op, "assignment operator")
            self.expression()
        else:
            raise SyntaxError(f"Line {self.current_line}: Expected assignment operator, found '{assign_op}'")
        
    def assignment(self):
        self.match_and_advance("Identifier", "assignment variable")
        assign_op = self.peek_next_token()
        if assign_op in ["=", "+=", "-=", "*=", "/=", "%="]:
            self.match_and_advance(assign_op, "assignment operator")
            self.expression()
        else:
            raise SyntaxError(f"Line {self.current_line}: Expected assignment operator, found '{assign_op}'")

    def condition(self):
        """Parses condition expressions"""
        self.term()
        while self.peek_next_token() in ["&&", "||"]:
            self.match_and_advance(self.peek_next_token(), "logical operator")
            self.term()

    def term(self):
        """Parses comparison terms"""
        self.expression()
        rel_op = self.peek_next_token()
        if rel_op in ["==", "!=", "<", ">", "<=", ">="]:
            self.match_and_advance(rel_op, "relational operator")
            self.expression()

    def expression(self):
        """Parses arithmetic expressions"""
        self.term_expression()
        while self.peek_next_token() in ["+", "-"]:
            self.match_and_advance(self.peek_next_token(), "arithmetic operator")
            self.term_expression()

    def term_expression(self):
        """Parses multiplication/division terms"""
        self.factor()
        while self.peek_next_token() in ["*", "/", "%"]:
            self.match_and_advance(self.peek_next_token(), "arithmetic operator")
            self.factor()

    def factor(self):
        """Parses basic factors in expressions"""
        token = self.peek_next_token()
        if token == "(":
            self.match_and_advance("(", "expression open")
            self.expression()
            self.match_and_advance(")", "expression close")
        elif token in ["Linklit", "Bubblelit", "Piecelit", "Fliplit"]:
            self.match_and_advance(token, "literal")
        elif token.startswith("Identifier"):
            self.match_and_advance("Identifier", "variable")
        elif token is None:
            raise SyntaxError(f"Line {self.current_line}: Unexpected end of input in expression")
        else:
            raise SyntaxError(f"Line {self.current_line}: Invalid expression token: '{token}'")

    def literal(self):
        """Parses literal values"""
        token = self.peek_next_token()
        if token in ["Linklit", "Bubblelit", "Piecelit", "Fliplit"]:
            self.match_and_advance(token, "literal")
        else:
            raise SyntaxError(f"Line {self.current_line}: Expected literal, found '{token}'")
        
    def update_statement(self):
        self.match_and_advance("Identifier", "update variable")
        if self.peek_next_token() in ["++", "--"]:
            self.match_and_advance(self.peek_next_token(), "increment/decrement")
        else:
            self.assignment()

    def match_and_advance(self, expected, context):
        """Matches and advances token with line number tracking"""
        token = self.get_current_token()
        if token is None:
            raise SyntaxError(f"Line {self.current_line}: Unexpected end of input, expected '{expected}' in {context}")
        if expected == "Identifier" and token.startswith("Identifier"):
            self.advance()
        elif token == expected:
            self.advance()
        else:
            raise SyntaxError(f"Line {self.current_line}: Expected '{expected}', found '{token}' in {context}")

    def get_current_token(self):
        """Gets current token and updates line number"""
        if self.current_index < len(self.tokens):
            token = self.tokens[self.current_index]
            token_count = 0
            for i, line in enumerate(self.lines, 1):
                line_tokens = len([t for t in line.split() if t.strip() and t != "Space"])
                token_count += line_tokens
                if self.current_index < token_count:
                    self.current_line = i
                    break
            else:
                self.current_line = len(self.lines)
            print(f"Token: {token}, Line: {self.current_line}, Index: {self.current_index}")
            return "Identifier" if token.startswith("Identifier") else token
        return None

    def peek_next_token(self):
        """Peeks at next token"""
        return self.tokens[self.current_index] if self.current_index < len(self.tokens) else None

    def peek_two_tokens_ahead(self):
        """Peeks two tokens ahead"""
        next_index = self.current_index + 1
        count = 0
        while next_index < len(self.tokens) and count < 1:
            count += 1
            next_index += 1
        if next_index < len(self.tokens):
            return self.tokens[next_index]
        return None

    def debug_tokens(self):
        """Print current token context for debugging"""
        print(f"Current index: {self.current_index}, Line: {self.current_line}")
        print(f"Current token: {self.get_current_token()}")
        print(f"Next token: {self.peek_next_token()}")
        print(f"Two ahead: {self.peek_two_tokens_ahead()}")
        print(f"Tokens remaining: {self.tokens[self.current_index:]}")

    def advance(self):
        """Advances to next token"""
        self.current_index += 1
