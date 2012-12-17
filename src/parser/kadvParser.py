import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import ply.lex as lex
import ply.yacc as yacc
import parser.kadvLexer as kl

class kadvParser:
  def __init__(self, inputController):
    self.kLex = kl.kadvLexer()
    self.tokens = self.kLex.tokens
    self.parser = yacc.yacc(module=self)
    self.inputController = inputController
    
  # Parsing rules
  precedence = (
      ('nonassoc','SAY'),
      ('right','STRING'),
      )

  def p_expression_say(self,p):
      "expression : SAY expression"
      """
      mvEvent = Events.LogMsgEvent(str( p[2] ))
      self.appCollection.notify( mvEvent )
      """
      print( p[2] )

  def p_words_expression(self,p):
      "expression : expression STRING"
      p[0] = p[1] + " " + p[2]

  def p_string_expression(self,p):
      "expression : STRING"
      p[0] = p[1]

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

