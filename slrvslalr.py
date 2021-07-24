from ply.lex import lex
from ply.yacc import yacc


tokens = ('id', 'MULT', 'EQUAL')

t_EQUAL = r'='
t_MULT = r'\*'
t_ignore = '\t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_equality(p):
    """
    S : L EQUAL R
    """
    return p

def p_initial_simple_transform(p):
    """
    S : R
    """
    return p

def p_multiplication(p):
    """
    L : MULT R
    """
    return p

def p_define_id(p):
    """
    L : id
    """
    return p

def p_simple_transform(p):
    """
    R : L
    """
    return p

def p_error(p):
    print("Syntax error: {p.value!r}")


yacc(method='SLR', debugfile='slr_parser.out', tabmodule='slr_parsetab')
yacc(method='LALR', debugfile='lalr_parser.out', tabmodule='lalr_parsetab')