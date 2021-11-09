#Analizador Lexico Para el lenguaje C++

# Integrantes:
#Jose Ricardo May Estrella
#Jose Mauricio Canul Chuc
#Marco Antonio Tuz Pech

import ply.lex as lex
import sys
from ply.lex import Lexer

palabrasReservadas = {

    'include':'INCLUDE',
    'using':'USING',
    'namespace':'NAMESPACE',
    'std':'STD',
    'cout':'COUT',
    'cin':'CIN',
    'main' : 'MAIN',
    'endl':'ENDL',
    'if':'IF',
    'else':'ELSE',
    'int':'INT',
    'float':'FLOAT',
    'string':'STRING',
    'char':'CHAR',
    'bool':'BOOL',
    'const':'CONST',
    'void':'VOID',
    'do':'DO',
    'while':'WHILE',
    'for':'FOR',
    'switch':'SWITCH',
    'break':'BREAK',
    'try':'TRY',
    'catch':'CATCH',
    'return':'RETURN',
    'private':'PRIVATE',
    'public':'PUBLIC',
    'default':'DEFAULT',
    'delete':'DELETE',
    'true':'TRUE',
    'false':'FALSE'
}

tokens = list(palabrasReservadas.values()) + [
            'IDENTIFICADOR',
            'NUMBER',
            'PARENTESIS_LEFT',
            'PARENTESIS_RIGHT',
            'LLAVE_LEFT',
            'LLAVE_RIGHT',
            'SUMA',
            'RESTA',
            'MULTIPLICACION',
            'DIVISION',
            'MODULO',
            'FIN_DE_INSTRUCCION',
            'PUNTO_Y_COMA',
            'MAYOR_QUE',
            'MENOR_QUE',
            'MAYOR_IGUAL_QUE',
            'MENOR_IGUAL_QUE',
            'DIFERENTE_DE',
            'ASIGNACION',
            'COMPARACION',
            'AND',
            'OR',
            'NOT',
            'NUMERAL',
            'COMENTARIOS_UNA_LINEA',
            'COMENTARIOS_VARIAS_LINEAS',
            'COMILLAS',
            'APOSTROFES',
            'APOSTROFE_LEFT',
            'PUNTO',
            'COMA',
            'DOS_PUNTOS',
            'MAS_MAS',
            'MENOS_MENOS',
            'MAYOR_ESCRIBIR_MOSTRAR',  #caracteres que se utilizan en C++ como cout<<
            'MENOR_OBTENER_ALMACENAR', #caracteres que se utilizan en C++ para recibir cin>>
            'ERROR'

]

#EXPRESIONES REGUALES PARA SÍMBOLOS ESPECIALES DE CARACTER SIMPLE
#t_ignore = '\t'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'\%'
t_ASIGNACION = r'='
t_PARENTESIS_LEFT = r'\('
t_PARENTESIS_RIGHT = r'\)'
t_LLAVE_LEFT = r'\{'
t_LLAVE_RIGHT = r'\}'
t_DOS_PUNTOS = r':'
t_PUNTO = r'\.'
t_COMA = r','
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_MAYOR_IGUAL_QUE = r'>='
t_MENOR_IGUAL_QUE = r'<='
t_DIFERENTE_DE = r'!='
t_COMPARACION = r'=='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_COMILLAS = r'\" '
t_APOSTROFE_LEFT = r'\''

"""def t_IDENTIFICADOR(t):
    r'[a-zA-Z0-9_]+' #esto es lo que reconoce un identificador
    if t.value.upper() in palabrasReservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t"""
def t_IDENTIFICADOR(t):
    r'[a-zA-Z](\w)*'  # esto es lo que reconoce un identificador
    if t.value in palabrasReservadas:
        t.type = palabrasReservadas[t.value]  # Check for reserved words
        return t
    else:
        return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_FLOAT(t):
    r'\d+[^.]+\d' #reconoce numeros flotantes o decimales
    return t

def t_STRING(t):

    r'\"?(\w+ \ *\w*\d* \ *)\"?' #expresion regular para reconocer los STRING
    return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_MAS_MAS(t):
    r'\+\+'
    return t

def t_MENOS_MENOS(t):
    r'\-\-'
    return t

def t_COMENTARIOS_UNA_LINEA(t):
    r'\/\/.*' #no devuelve un valor, reconoce que es un comentario pero obvia la función y no devuelve nada
    pass

def t_COMENTARIOS_VARIAS_LINEAS(t):
    r'\/\*\[a-zA-Z0-9_\s]*\*\/ | \*\/.*\*\/'   #no reconcoe las cadenas de caracteres de los comentarios, permite escribirlos pero los ignora
    pass #obviamos, reconoce el token pero no lo va devolver, es decir es ignorado.


def t_FIN_DE_INSTRUCCION(t):
    r'\;'
    return t #esto es un cambio de linea

def t_MAYOR_ESCRIBIR_MOSTRAR(t):
    r'\<\<'
    return t

def t_MENOR_OBTENER_ALMACENAR(t):
    r'\>\>'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'

def t_comments1(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments2(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    t.type = t.value[0]
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

def test(data, lexer):
    lexer.input(data)
    i = 1  # Representa la línea
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("\t" + str(i) + " - " + "Linea: " + str(tok.lineno) + "\t" + str(tok.type) + "\t -->  " + str(tok.value))
        i += 1
    # print(tok)


lexer: Lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'index.txt'
    f = open(fin, 'r')
    data = f.read()
    #print (data)
    # lexer.input(data)
    test(data, lexer)
# input()