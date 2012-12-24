import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import ply.lex as lex
import ply.yacc as yacc
import FAParsers.kadvLexer as kl

class kadvParser:
  def __init__(self, inputController):
    self.kLex = kl.kadvLexer()
    self.tokens = self.kLex.tokens
    self.parser = yacc.yacc(module=self)
    self.inputController = inputController
  
# # Parsing rules
# precedence = (
#   #('nonassoc','QUIT'),
#   ('left','LOG'),
#    ('nonassoc','INSPECT'),
#   #('right','STRING'),
#    ('right','ME'),
#   )

  def p_expr_log(self,p):
    "command : LOG STRING"
    self.inputController.log( p[2] )

# def p_command_quit(self,p):
#   "command : QUIT"
#   self.inputController.quit()

  def p_error(self,p):
    if p:
      print("Syntax error at " + p.value)
    else:
      print("Syntax error at EOF")

if __name__ == "__main__":
  kp = kadvParser()
  while True:
    s = input("kadv: ")
    if not s: continue 
    kp.parser.parse(s)
