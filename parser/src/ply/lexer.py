from compiler.ast import *
testSyn = "print 4 + 8 + 11\nx=10 # setting x to 10\nx2=x+-9"
tokens = ('PRINT','INT','PLUS', 'NEG', 'NAME', 'EQUALS', 'COMMENT')

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

def t_NAME(t):
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

mylex(testSyn)

# Parser
from compiler.ast import Printnl, Add, Const, Name, Assign, AssName
precedence = (
    ('nonassoc','PRINT'),
    ('left','PLUS')
)
def p_print_statement(t):
    'statement : PRINT expression'
    t[0] = Printnl([t[2]], None)
def p_assign_statement(t):
    'statement : NAME EQUALS expression'
    t[0] = Assign([AssName(t[1], flags='OP_ASSIGN')], t[3])
def p_name_statement(t):
    'statement : NAME'
    t[0] = Name(t[1]) 
def p_plus_expression(t):
    'expression : expression PLUS expression'
    t[0] = Add((t[1], t[3]))
def p_int_expression(t):
    'expression : INT'
    t[0] = Const(t[1])

def p_neg_expression(t):
    'expression : NEG expression'
    t[0] = UnarySub(t[2])
   
def p_error(t):
    print "Illegal character %s" % t

import ply.yacc as yacc
parser = yacc.yacc()

print "\nparser:\n", parser.parse("x=1+4+3")
