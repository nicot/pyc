from compiler.ast import *
from lexer import *

debug = False
# Parser
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

if debug:
    myfile = open(sys.argv[1], "r")
    txt = myfile.read()
    print "\nparser:\n", parser.parse(txt)
