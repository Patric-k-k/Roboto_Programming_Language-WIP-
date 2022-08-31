##################
# COLORS
##################
from ast import expr


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
##################
#ERRORS
##################
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        result += f'\n File: {self.pos_start.fn}, line: {self.pos_start.ln + 1}'
        return result
class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, error_name, details):
        super().__init__(pos_start, pos_end, error_name, details)
##################
# CONSTATS
##################
DIGITS = '0123456789'
##################
# POSISION
##################
#create a class for positions
class POSITION:
    #Initialize the position
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt
    #Advanced POSITION
    def advance(self, current_char):
        self.idx += 1
        self.col += 1
        if current_char == '\n':
            self.ln += 1
            self.col += 1
        return self
    #copy POSITION
    def copy(self):
        return POSITION(self.idx, self.ln, self.col, self.fn, self.ftxt)
##################
# TOKENS
##################
#type of tokens
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'
TT_EQ = 'TT_EQ'
#create a class for Tokens
class Token:
    #Initialize the token
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    #copy Token
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
##################
# Lexer
##################
#create a class for Lexer
class Lexer:
    #Initialize the Lexer
    def __init__(self, fn, text):
        self.fn = fn 
        self.text = text
        self.pos = POSITION(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()
    #advance the Lexer
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
    #create tokens
    def make_tokens(self):
        tokens = []
        #check what the current character is
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, value='+'))                
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, value='*'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, value='-'))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, value='/'))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, value='('))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, value=')'))
                self.advance()                            
            else:
                #throw an error if the character is not recognized
                pos_start = self.pos.copy()
                print(pos_start)

                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "Illegal syntax", char)
        return tokens, None
    #Make the number
    def make_number(self):
        #make the variables
        num_str = ''
        dot_count = 0
        #check if the current character is a digit
        while self.current_char is not None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                #check if there is more than one dot, if so, close the program
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                #add the digit to the string
                num_str += self.current_char
            self.advance()
        #check if the number is a float
        if dot_count == 0:
            #else, return the number as an int
            return Token(TT_INT, int(num_str))
        else:
            #if so, return the float
            return Token(TT_FLOAT, float(num_str))

class Parser():
    tok_vals = {'TT_PLUS': '+', 'TT_MINUS': '-', 'TT_MUL': '*', 'TT_DIV': '/', 'TT_LPAREN': '(', 'TT_RPAREN': ')', 'TT_EQ': '='}
    tok_keys = ['TT_PLUS', 'TT_MINUS', 'TT_MUL', 'TT_DIV', 'TT_LPAREN', 'TT_RPAREN', 'TT_EQ']

    def __init__(self, tokens):
        self.tokens = tokens
    
    def basic_math(self):
        # Expression
        expr = ""

        # Append tokens to expresion
        for tok in self.tokens:
            expr += str(tok.value)
        
        # Evaluating the mathematical expression
        expr_eval = eval(expr)
        print(expr_eval)
        return expr_eval


##################
# RUN
##################
#run the program
def run(fn, text):
    lexer = Lexer(fn, text)
    return tokens, error
