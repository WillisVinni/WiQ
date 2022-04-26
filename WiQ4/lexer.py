from rply import LexerGenerator
class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
    def _add_tokens(self):
        # functions
        self.lexer.add('VERSION', r'version')
        self.lexer.add('MDF', r'md')
        # Go value
        self.lexer.add('VALUE', r'\:')
        # End of line
        self.lexer.add('SEMI_COLON', r'\;')
        # text
        self.lexer.add("STRING", "[\'|\"].*[\'|\"]")
        # no spaces
        self.lexer.ignore('\s+')
    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()