# Syntax_Analyzer

This is a Python program that simulates the first phase of compiling a code - lexical analysis. The analyzer accepts a simple programming laguage that contains the followng lexical units: <br>
1. keywords <br>
for - start of a for loop (KW_FOR) <br>
rof - closing a for loop (KW_ROF) <br>
from  - start of a range (KW_FROM) <br>
to - end of a range (KW_TO) <br>
<br>
2. variables/identifiers (IDN) <br> <br>
3. operators + (OP_ADD), - (OP_SUB), * (OP_MUPLTIPLY), / (OP_DIVIDE), ( (LEFT_P), ) (RIGHT_P), = (OP_ASSIGN) <br> <br>
4. constants (only integers for simplicity) (NUM) <br>
<br>

The program takes output of a Lexical Analyzer (https://github.com/ZrinkaCvitanovic/LexicalAnalyzer) and produces a syntax tree. 
The rules are defined in patterns variable in the code.
Since this is only a simplified version, it does not recover from mistkaes. Therefore, if there is a mistake in code, it will terminate the program and the user will not be notified if there are more mistakes afterwards. However, the program still lets the user know which line contains an error.
