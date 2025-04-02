grammar expr;

/** The start rule; begin parsing here. */
prog: (expr ';')+;

expr: expr op=('*'|'/') expr  #Mul
    | expr op=('+'|'-') expr  #Add
    | OCT                     #Octal
    | INT                     #Integer
    | HEX                     #Hexa
    | '(' expr ')'            #Par
    ;

INT : [0-9]+ ;          // match integers
OCT : '0'[0-7]+;
HEX : '0x'[0-9a-fA-F]+;
WS : [ \t\r\n]+ -> skip ;   // toss out whitespace