grammar Lang;

/** The start rule; begin parsing here. */
program: statement+ ;

statement
    : primitiveType IDENTIFIER (',' IDENTIFIER)* ';' # declaration // var declaration
    | expr ';'                                       # printExpr
    | read IDENTIFIER (',' IDENTIFIER)* ';'
    | write expr (',' expr)* ';'
    | { statement }
    | if ( condition ) statement (else statement)?
    | while ( condition ) statement
    ;

expr: expr op=(MUL|DIV) expr                # mulDiv
    | expr op=(ADD|SUB) expr                # addSub
    | expr op=(MOD) expr                    # modulo
    | op='-' expr                           # unaryMinus
    | op='!' expr                           # not
    | expr op='.' expr                      # concat
    | expr op=(GT|LT) expr                  # relational
    | expr op=(EQ|NEQ) expr                 # compare
    | expr op=(AND|OR) expr                 # logic
    | IDENTIFIER                            # id
    | INT                                   # int
    | FLOAT                                 # float
    | BOOL                                  # bool
    | STRING                                # string
    | '(' expr ')'                          # parens
    | <assoc=right> IDENTIFIER '=' expr     # assignment
    ;

condition
    : expr
    ;

primitiveType
    : type=INT_KEYWORD
    | type=FLOAT_KEYWORD
    | type=BOOL_KEYWORD
    | type=STRING_KEYWORD
    ;


INT_KEYWORD : 'int';
FLOAT_KEYWORD : 'float';
BOOL_KEYWORD : 'bool';
STRING_KEYWORD : 'string';

SEMI:               ';';
COMMA:              ',';

MUL : '*' ; 
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
MOD : '%' ;
GT : '>' ;
LT : '<' ;
EQ : '==';
NEQ : '!=';
AND : '&&';
OR : '||';

IDENTIFIER : [a-zA-Z]+ ; // var name
FLOAT : [0-9]+'.'[0-9]+ ;
INT : [0-9]+ ; 
BOOL : 'true' | 'false';
STRING : '"' (~["\r\n])* '"' ;

WS : [ \t\r\n]+ -> skip ; // toss out whitespace
COMMENT : '//' ~[\r\n]* -> skip ; // ignore comments