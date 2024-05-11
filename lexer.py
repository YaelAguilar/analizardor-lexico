import ply.lex as lex

tokens = [
    'FOR', 'DO', 'WHILE', 'IF', 'ELSE',
    'LPAREN', 'RPAREN'
]

t_FOR = r'for'
t_DO = r'do'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
