
"""
Script to do the replacement of labels into one-liner references in beamer
frames

TODO: Write argparser in the form
python replace_script [file_bibtex] [file_beamer] [file_output] - now too tired
"""

import numpy as np
from funcs import make_article_element
from funcs import make_list_of_reference_dicts
from funcs import replace_labels_to_foot_notes


#replace_labels_to_foot_notes(bibtex_file="bib_nsnm_siemens.txt",
#                            beamer_file = "beamer.tex",
#                            new_file_path = "new_new_test.tex")
