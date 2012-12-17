import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import ply.lex as lex

class kadvLexer:
  def __init__(self):
    self.lexer = lex.lex(module=self)

  reserved = { 
    'log' : 'LOG',
    }

  tokens = [
    'STRING'
    ] + list(reserved.values())

  # Tokens

  def t_STRING(self,t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = self.reserved.get(t.value,'STRING')
    return t

  t_ignore = " \t"

  def t_newline(self,t):
      r'\n+'
      t.lexer.lineno += t.value.count("\n")
      
  def t_error(self,t):
      print("Illegal character '%s'" % t.value[0])
      t.lexer.skip(1)
