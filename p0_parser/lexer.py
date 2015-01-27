
tokens = ('PRINT','INT','PLUS', 'NEG', 'VAR', 'EQUALS', 'COMMENT')

t_PRINT = r'print'
t_PLUS = r'\+'
t_NEG = r'-'
t_EQUALS = r'='
t_ignore = ' \t'
t_COMMENT = '\#.*\n'
def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "integer value too large", t.value
        t.value = 0
    return t

def t_VAR(t):
    r'\w[a-zA-Z0-9]*'
    # will catch PRINT so we need to change it back when it does
    if t.value == r'print':
        t.type = 'PRINT'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
def t_error(t):
    print "Illegal character %s" % t.value[0]
    t.lexer.skip(1)


import ply.lex as lex

lexer = lex.lex()
def mylex(inp):
    lexer.input(inp)
    for t in lexer:
        print t

mylex("print 4 + 8\nx=10 # setting x to 10\nx2=x+-9")
