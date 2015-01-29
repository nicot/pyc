#!/usr/bin/env python

#P0 compiler

from compiler.ast import *
import sys
import string
import lex as lexer
import yacc
import compiler

class my_compiler:
    #variables
    __dict_vars = {} #dictionary of var names to memory locations relative to ebp
    __stack_offset = 0
    __generated_code = ""

    def get_generated_code(self):
        return self.__generated_code

    def flatten(self, ast):
        flat_ast = compiler.ast.Module(None, compiler.ast.Stmt([]))
        self.flatten_sub(ast, 0, flat_ast, self.__dict_vars)
        return flat_ast

    # Recursive flattening function
    # args: ast - ast to be flattened
    #       tmpNum - num of next tmp var to be used
    #       flat_ast - new flattened ast
    def flatten_sub(self, ast, tmpNum, flat_ast, __dict_vars):
        if isinstance(ast, Module):
            self.flatten_sub(ast.node, tmpNum, flat_ast, self.__dict_vars)
            return 0

        elif isinstance(ast,  Stmt):
            for node in ast.nodes:
                tmpNum = self.flatten_sub(node, tmpNum, flat_ast, self.__dict_vars)
                tmpNum += 1
            return tmpNum
            
        elif isinstance(ast, Printnl):
            # get tmp var to be printed
            toPrint = self.flatten_sub(ast.nodes[0], tmpNum, flat_ast, self.__dict_vars)
            # build statement 
            stmt = 'print tmp' + str(toPrint)
            flat_ast.node.nodes.append(compiler.parse(stmt).node.nodes[0])
            return toPrint

        elif isinstance(ast, Add):
            # get left and right tmp vars
            left = self.flatten_sub(ast.left, tmpNum, flat_ast, self.__dict_vars)
            right = self.flatten_sub(ast.right, left + 1, flat_ast, self.__dict_vars)
            # build statement to add tmp vars
            stmt = 'tmp' + str(right + 1) + ' = tmp' + str(left) + ' + tmp' + str(right)
            flat_ast.node.nodes.append(compiler.parse(stmt).node.nodes[0])
            return right + 1

        elif isinstance(ast, UnarySub):
            # get tmp var to be negated
            toNeg = self.flatten_sub(ast.expr, tmpNum, flat_ast, self.__dict_vars)
            stmt = 'tmp' + str(toNeg + 1) + ' = -tmp' + str(toNeg)
            flat_ast.node.nodes.append(compiler.parse(stmt).node.nodes[0])
            return toNeg + 1
            
        elif isinstance(ast, CallFunc):
            # CallFunc always refers to an input() in p0
            stmt = 'tmp' + str(tmpNum) + ' = input()'
            flat_ast.node.nodes.append(compiler.parse(stmt).node.nodes[0])
            return tmpNum
                
        elif isinstance(ast, Name):
            ast.name = "__"+ast.name
            stmt = 'tmp' + str(tmpNum) + ' = ' + ast.name
            flat_ast.node.nodes.append(compiler.parse(stmt).node.nodes[0])
            return tmpNum

        elif isinstance(ast, Assign):
            varName = "__"+ast.nodes[0].name
            # get tmp var containing the value to be assigned (right value)
            right = self.flatten_sub(ast.expr, tmpNum, flat_ast, self.__dict_vars)
            stmt = varName + ' = tmp' + str(right)
            flat_ast.node.nodes.append(compiler.parse(stmt).node.nodes[0])
            return right
            
        elif isinstance(ast, Discard):
            self.flatten_sub(ast.expr, tmpNum, flat_ast, self.__dict_vars)
            return tmpNum
        
        elif isinstance(ast, Const):
            stmt = 'tmp' + str(tmpNum) + ' = ' + str(ast.value)
            flat_ast.node.nodes.append(compiler.parse(stmt).node.nodes[0])
            return tmpNum
            
        else:
            raise Exception("Error: Unrecognized node type")
            
    def _update_dict_vars(self, varName):
        self.__stack_offset = self.__stack_offset + 4
        self.__dict_vars[varName] = self.__stack_offset
        return self.__stack_offset

    def _encapsulate_generated_code(self):
        self.__generated_code = ".globl main\nmain:\npushl %ebp\nmovl %esp, %ebp\nsubl $"+str(self.__stack_offset)+",%esp\n" + self.__generated_code + "movl $0, %eax\nleave\nret\n"

    def generate_x86_code(self, ast, _dict_vars):
        if isinstance(ast, Module):
            self.generate_x86_code(ast.node, _dict_vars)
            return
        elif isinstance(ast, Stmt):
            for node in ast.nodes:
                self.generate_x86_code(node, _dict_vars)
            return
            
        elif isinstance(ast, Printnl):
            self.generate_x86_code(ast.nodes[0], _dict_vars)
            # get value stored in eax and push for call to print
            self.__generated_code += "pushl %eax\n"
            self.__generated_code += "call print_int_nl\n"
            self.__generated_code += "addl $4, %esp\n"
            return

        elif isinstance(ast, Add):
            # process LHS, move to edx
            self.generate_x86_code(ast.left, _dict_vars)
            self.__generated_code += "movl %eax, %edx\n"
            # RHS
            self.generate_x86_code(ast.right, _dict_vars)
            # add
            self.__generated_code += "addl %edx, %eax\n"
            return
        
        elif isinstance(ast, UnarySub):
            self.generate_x86_code(ast.expr, _dict_vars)
            self.__generated_code += "negl %eax\n"
            return
        
        elif isinstance(ast, CallFunc):
            # CallFunc always refers to input() in p0
            self.__generated_code += "call input\n"
            return
        
        elif isinstance(ast, Name):
            # get var from stack and move to %eax
            try:
                self.__generated_code += "movl -" + str(_dict_vars[ast.name]) + "(%ebp), %eax\n"
            except KeyError:
                raise Exception("Error: Unassigned variable")
            return

        elif isinstance(ast, Assign):
            # Get the name of the variable being assigned to (l value)
            varName = ast.nodes[0].name
            
            #emit our expression (RHS)
            self.generate_x86_code(ast.expr, _dict_vars)
            
            #now, the result of that should be stored in %eax, so do the assignment
            try:
                var_offset = _dict_vars[varName]
                self.__generated_code += "movl %eax, -"+str(var_offset)+"(%ebp)\n"
            except KeyError:
                #this means that the variable was not yet assigned
                var_offset = self._update_dict_vars(varName)
                self.__generated_code += "movl %eax, -"+str(var_offset)+"(%ebp)\n"

        elif isinstance(ast, Discard):
            self.generate_x86_code(ast.expr, _dict_vars)
            return
        
        elif isinstance(ast, Const):
            self.__generated_code += "movl $" + str(ast.value) + ", %eax\n"
            return   

        else:
            raise Exception("Error: Unrecognized node type")                             

    def __init__(self, codefile):
        ast = parser(codefile)
        flatast = self.flatten(ast)
        self.generate_x86_code(flatast, self.__dict_vars)
        self._encapsulate_generated_code()

class parser:
    tokens = ('PRINT', 'INT', 'PLUS', 'MINUS', 'EQUALS', 'INPUT', 'LPARENS', 'RPARENS', 'NAME')
    def lex(self, code):
        tokens = self.tokens
        t_PRINT = r'print'
        t_PLUS = r'\+'
        t_MINUS = r'-'
        t_EQUALS = r'='
        t_INPUT = r'input'
        t_LPARENS = r'\('
        t_RPARENS = r'\)'
        t_ignore = ' \t'

        def t_NAME(t):
            r'[a-zA-Z][a-zA-Z0-9_]*'
            return t
        def t_INT(t):
            r'\d+'
            t.value = int(t.value)
            return t
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += t.value.count("\n")
        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)
        
        lexer.lex()
        lexedTokens = []
        lexer.input(code)
        while True:
            tok = lexer.token()
            print(tok)
            if not tok: break
            lexedTokens.append(tok)
        return lexedTokens
        
    def parse(self, lexedTokens):
        tokens = self.tokens
        precedence = (
                ('nonassoc', 'PRINT'),
                ('left', 'PLUS')
                )
        def p_print_statement(t):
            'statement : PRINT expression'
            t[0] = Printnl(t[2], None)
        def p_plus_expression(t):
            'expression : expression PLUS expression'
            t[0] = Add((t[1], t[3]))
        def p_int_expression(t):
            'expression : INT'
            t[0] = Const(t[1])
        def p_error(t):
            print("Syntax error at '%s'" % t.value)

        yacc.yacc()
        for tok in lexedTokens:
            yacc.parse(tok)


    def __init__(self, codefile):
        # Take a path to a file with python code
        # Return a python AST
        f = open(codefile, "r")
        code = f.read()
        f.close()
        lexedTokens = self.lex(code)
        ast = self.parse(tokens)
        return ast

myfile = sys.argv[1]
basename = myfile[:len(myfile)-3]
compileObj = my_compiler(myfile)
f = open(basename+".s","w")
f.write(compileObj.get_generated_code())
f.close()
