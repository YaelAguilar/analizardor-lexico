import ply.lex as lex

reserved = {
    'for': 'FOR',
    'if': 'IF',
    'do': 'DO',
    'while': 'WHILE',
    'else': 'ELSE'
}

tokens = [
    'LPAREN', 'RPAREN'
] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(t):
    r'\w+'
    t.value = t.value.lower()
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
