#!/usr/bin/python

#P0 compiler

from compiler.ast import *
import compiler
import sys
import string

class my_compiler:
    #variables
    __dict_vars = {} #dictionary of variable names to memory locations relative to ebp
    __stack_offset = 0
    __generated_code = ""

    def get_gen_code(self):
        return self.__generated_code


infile = sys.argv[1]
basename = infile[:len(infile)-3]
compileObj = csci4555_compiler(myfile)
file = open(basename+".s","w")
file.write(compileObj.get_generated_code())
file.close()

