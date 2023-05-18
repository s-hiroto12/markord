import re
import elements
from io_files import *
from extract_chords import *

#following code should be written in extract_chords.py as main function
for i in range(6):
    #extracted_chords: [dict]
    extracted_chords = extract_chords('data/text_area/' + str(i) + '.txt')
    #split key chunks to chord progressions
    for j, ex_c in enumerate(extracted_chords):
        chord_progression = elements.Chord_progression(ex_c)
        out_lines('data/chord_progressions/' + str(i) +'_'+str(j)+'.txt', chord_progression.normalize())

files = get_file_names('data/chord_progressions')
print(files)
f = open('data/all_progressions', 'w')
for file in files:
    print(file_to_line(file))
    f.write(file_to_line(file) + '\n')
