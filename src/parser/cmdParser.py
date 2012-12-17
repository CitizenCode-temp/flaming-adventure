import os, sys

lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import ply.lex as lex
import ply.yacc as yacc
import base.Events as Events

reserved = { 
  'say' : 'SAY',
  }

tokens = [
  'STRING'
  ] + list(reserved.values())

# Tokens

def t_STRING(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  t.type = reserved.get(t.value,'STRING')
  return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lex.lex()

# Parsing rules

precedence = (
    ('nonassoc','SAY'),
    ('right','STRING'),
    )

def p_expression_say(p):
    "expression : SAY expression"
    """
    mvEvent = Events.LogMsgEvent(str( p[2] ))
    self.appCollection.notify( mvEvent )
    """
    print( p[2] )

def p_words_expression(p):
    "expression : expression STRING"
    p[0] = p[1] + " " + p[2]

def p_string_expression(p):
    "expression : STRING"
    p[0] = p[1]

def p_error(p):
    if p:
        print("Syntax error at " + p.value)
    else:
        print("Syntax error at EOF")

yacc.yacc()

def parse(s):
  if not s: return
  yacc.parse(s)
 
def parseLoop():
  while True:
    s = input("kadv: ")
    if not s: return
    yacc.parse(s)

if __name__ == "__main__":
  parseLoop()
