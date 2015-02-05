from compiler.ast import *
from x86_ast import *

def select(flatAST):
    options = { '' : stmt }

class translate:
    __dict_vars = {} #dictionary of var names to memory locations relative to ebp
    __stack_offset = 0
    __generated_code = ""
    
    def __init__(self, flat_ast):        
        self.generate_x86_code(flat_ast)
        self.encapsulate_generated_code()


    def get_generated_code(self):
        return self.__generated_code
        
    def _update_dict_vars(self, varName):
        self.__stack_offset = self.__stack_offset + 4
        self.__dict_vars[varName] = self.__stack_offset
        return self.__stack_offset

    def encapsulate_generated_code(self):
        self.__generated_code = ".globl main\nmain:\npushl %ebp\nmovl %esp, %ebp\nsubl $"+str(self.__stack_offset)+",%esp\n" + self.__generated_code + "movl $0, %eax\nleave\nret\n"

    # Takes a flattened ast and each variables offset relative to %ebp
    # and recursively generates the appropriate x86 code (stored in __generated_code)
    def generate_x86_code(self, ast):
        if isinstance(ast, Module):
            self.generate_x86_code(ast.node)
            return
        elif isinstance(ast, Stmt):
            for node in ast.nodes:
                self.generate_x86_code(node)
            return
            
        elif isinstance(ast, Printnl):
            self.generate_x86_code(ast.nodes[0])
            # get value stored in eax and push for call to print
            self.__generated_code += "pushl %eax\n"
            self.__generated_code += "call print_int_nl\n"
            self.__generated_code += "addl $4, %esp\n"
            return

        elif isinstance(ast, Add):
            # process LHS, move to edx
            self.generate_x86_code(ast.left)
            self.__generated_code += "movl %eax, %edx\n"
            # RHS
            self.generate_x86_code(ast.right)
            # add
            self.__generated_code += "addl %edx, %eax\n"
            return
        
        elif isinstance(ast, UnarySub):
            self.generate_x86_code(ast.expr)
            self.__generated_code += "negl %eax\n"
            return
        
        elif isinstance(ast, CallFunc):
            # CallFunc always refers to input() in p0
            # general case would something like
            #self.__generated_code += "call " + str(ast.node.name) + "\n"
            self.__generated_code += "call input\n"
            return
        
        elif isinstance(ast, Name):
            # get var from stack and move to %eax
            try:
                self.__generated_code += "movl -" + str(self.__dict_vars[ast.name]) + "(%ebp), %eax\n"
            except KeyError:
                print ast
                raise Exception("Error: Unassigned variable")
            return

        elif isinstance(ast, Assign):
            # Get the name of the variable being assigned to (l value)
            varName = ast.nodes[0].name            
            #emit our expression (RHS)
            self.generate_x86_code(ast.expr)            
            #now, the result of that should be stored in %eax, so do the assignment

            try:
                var_offset = self.__dict_vars[varName]
                self.__generated_code += "movl %eax, -"+str(var_offset)+"(%ebp)\n"
            except KeyError:
                #this means that the variable was not yet assigned
                var_offset = self._update_dict_vars(varName)

                self.__generated_code += "movl %eax, -"+str(var_offset)+"(%ebp)\n"

        elif isinstance(ast, Discard):
            self.generate_x86_code(ast.expr)
            return
        
        elif isinstance(ast, Const):
            self.__generated_code += "movl $" + str(ast.value) + ", %eax\n"
            return   

        else:
            print ast
            raise Exception("Error: Unrecognized node type")                             
