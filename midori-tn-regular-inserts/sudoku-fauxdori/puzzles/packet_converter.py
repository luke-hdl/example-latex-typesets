# Script to process a file line by line,
# extract characters 14 through 94 (inclusive),
# replace all '0's with '~',
# and write the result to a new file.

INPUT_FILE = "easy.txt"
OUTPUT_FILE = "easy_latex.tex"  

def process_file(input_path, output_path, max_lines):
    current = 0
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Python uses 0-based indexing, so 14th char is at index 13, 94th at index 93
            current += 1
            if max_lines > 0 and max_lines < current:
                break
            segment = line[13:94]  # Slices up to but not including index 94, so index 93 is included
            segment = segment.replace('0', '~')
            outfile.write("\sudoku{1}{0}{0}{" + segment + '}\r\n\\newpage\r\n')

process_file(INPUT_FILE, OUTPUT_FILE, 32)
