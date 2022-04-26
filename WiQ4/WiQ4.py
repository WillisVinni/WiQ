from lexer import Lexer

text_input = """
version: version: "2";
md: version: " version: ";
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)