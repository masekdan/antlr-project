grammar Lang;

/** The start rule; begin parsing here. */
program: statement+ ;

statement
    : primitiveType IDENTIFIER (',' IDENTIFIER)* ';'                # declaration // var declaration
    | expr ';'                                                      # printExpr
    | READ_KEYWORD IDENTIFIER (',' IDENTIFIER)* ';'                 # readExp
    | WRITE_KEYWORD expr (',' expr)* ';'                            # writeExp
    | '{' statement+ '}'                                            # blockExp
    | IF_KEYWORD ( condition ) statement (ELSE_KEYWORD statement)?  # ifElse
    | WHILE_KEYWORD ( condition ) statement                         # whileLoop
    | FOR_KEYWORD '(' expr ';' expr ';' expr ')' statement                # forLoop
    | ';'                                                           # emptyCmd
    ;

expr: op='-' expr                           # unaryMinus
    | op='!' expr                           # not
    | expr op=(MUL|DIV) expr                # mulDiv
    | expr op=(ADD|SUB) expr                # addSub
    | expr op=MOD expr                      # modulo
    | expr op='.' expr                      # concat
    | expr op=(GT|LT) expr                  # relational
    | expr op=(EQ|NEQ) expr                 # compare
    | expr op=AND expr                      # logicAnd
    | expr op=OR expr                       # logicOr
    | IDENTIFIER                            # id
    | INT                                   # int
    | FLOAT                                 # float
    | 'true'                                # boolTrue
    | 'false'                               # boolFalse
    | STRING                                # string
    | '(' expr ')'                          # parens
    | expr '?' expr op=':' expr             # ternary
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
FOR_KEYWORD : 'for';

READ_KEYWORD : 'read';
WRITE_KEYWORD : 'write';
IF_KEYWORD : 'if';
ELSE_KEYWORD : 'else';
WHILE_KEYWORD : 'while';

SEMI:               ';';
COMMA:              ',';

// operators
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