from lexer import lexer

def analyze_text(text):
    lexer.input(text)
    result = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        result.append((tok.type, tok.value, tok.lineno))
    return result
