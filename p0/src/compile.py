#!/usr/bin/python

import compiler
import sys
import string
import python_ast 
import translate 

debug = False
if(len(sys.argv) > 2):
    if(sys.argv[2] == '-debug'):
       debug = True

myfile = sys.argv[1] 
ast = compiler.parseFile(myfile)
flatAST = python_ast.python_ast().flatten(ast)

x86code = translate.translate(flatAST)

# save the generated assembly code to FILENAME.s
basename = myfile[:len(myfile)-3]
file = open(basename+".s","w")
file.write(x86code.get_generated_code())
file.close()
