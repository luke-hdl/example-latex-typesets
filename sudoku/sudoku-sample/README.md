# Sudoku
Sample TeX file that uses Tikz, Calc, and XString to draw "Sudoku Pages" for puzzle books, etc.

The sudoku used is in this format: 

~5~7~3~6~~~7~~~8~~~~~816~~~~~~~3~~~~~~5~~~1~~73~~4~~869~6~~~2~484~572~93~~~4~9~~~

where ~ represent a spot that begins blank. It is read from the top-left corner, going right, then wrapping every 9.

The format used is based on the Sudoku Exchange puzzle bank, which generates puzzles with QQWing Sudoku and grades them with Sukaku Explainer. Note that Sukaku's "easy" rating is still relatively hard compared to many syndicated sudoku. These puzzles are public domain. 

Several files of puzzles are included in this repo. The piles in /puzzles/puzzlebank are the raw exchange file. In the /puzzles directory, there's a Python 3 script, "converter.py", to strip out difficulty-related information, etc. so that you can directly copy-and-paste them in, as well as "ready-to-paste-easy.txt", which has the contents of the Easy file. 