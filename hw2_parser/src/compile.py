#!/usr/bin/python

from compiler.ast import *
import compiler
import sys
import string
from flatten import *
from translate import *
from my_parser import *

debug = False
if(len(sys.argv) > 2):
    if(sys.argv[2] == '-debug'):
       debug = True

myfile = sys.argv[1]
ast = my_parser().parseFile(myfile)

flatAST = python_ast().flatten(ast)

x86code = translate(flatAST)

# save the generated assembly code to FILENAME.s
basename = myfile[:len(myfile)-3]
file = open(basename+".s","w")
file.write(x86code.get_generated_code())
file.close()
