import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import ply.lex as lex

class kadvLexer:
  def __init__(self):
    self.lexer = lex.lex(module=self)

  states = ( ('string', 'exclusive'), ) 

  tokens = [ 'LOG', 'STRING', 'QUIT', ]

  # Tokens
  
  def t_quit(self, t):
    r'quit'
    t.type = 'QUIT'
    return t

  def t_log(self, t):
    r'log'
    t.type = 'LOG'
    return t

  def t_string(self, t):
    r'"'
    t.lexer.code_start = t.lexer.lexpos
    t.lexer.begin('string')

  def t_string_slashquote(self, t):
    r'\"'
    pass

  def t_string_quote(self, t):
    r'"'
    t.value = t.lexer.lexerdata[t.lexer.code_start:t.lexer.lexpos]
    t.type = "STRING"
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    print("string")
    return t

  def t_string_any(self, t):
    r'[^\n]'
    pass

  def t_string_error(self, t):
    print("(string) Illegal character " + t.value[0])
    t.lexer.skip(1)

  t_string_ignore = " \t"
  t_ignore = " \t"

  def t_error(self,t):
    print("(initial) Illegal character " + t.value[0])
    t.lexer.skip(1)

  def run_lexer(self, data):
    lexer = self.lexer

    try:
      lexer.input(data)
      for tok in lexer:
        print(tok)
    except:
      print("failed!")

if __name__ == "__main__":
  fal = kadvLexer()
  while True:
    fal.run_lexer( input("kadv: ") )

  # ok
  f('log "this is a test"')
  f('log "this is a test"  ')
  f('log "this is a \\"test"  ')    

  # should fail
  f('log "this is a \n test"')
  # only parses log, doesn't fail on eof like it should :/
  f('log "this is a testz ')
