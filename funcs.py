def make_article_element(article_element):

    """
    No documentation
    """

    article_element_dict = {}

    for part in article_element:

        if "author = " in part:

            eq_index = part.find("=")
            author_singe_text = (part[eq_index+2::]).replace("{", "")
            author_singe_text = author_singe_text.replace("}", "")
            index_end = author_singe_text.find(",")
            author_singe_text = author_singe_text[0:index_end]

        if "journal = " in part:

            eq_index = part.find("=")
            journal_text = (part[eq_index+2::]).replace("{", "")
            journal_text = journal_text.replace("}", "")
            journal_text = journal_text.replace(",", "")

        if "volume = " in part:

            eq_index = part.find("=")
            volume_text = (part[eq_index+2::]).replace("{", "")
            volume_text = volume_text.replace("}", "")
            volume_text = volume_text.replace(",", "")

        if "number = " in part:

            eq_index = part.find("=")
            number_text = (part[eq_index+2::]).replace("{", "")
            number_text = number_text.replace("}", "")
            number_text = number_text.replace(",", "")

        if "year = " in part:

            eq_index = part.find("=")
            year_text = (part[eq_index+2::]).replace("{", "")
            year_text = year_text.replace("}", "")
            year_text = year_text.replace(",", "")

    if "number_text" not in locals():

	number_text = ""

    article_element_dict["ReferenceKey"] = (author_singe_text + year_text).replace("\n", "")

    article_element_dict["FootNoteText"] = (author_singe_text + " et. al. " + journal_text +
                                            ", " + volume_text + "(" + number_text + ") " + year_text).replace("\n", "")

    return article_element_dict

def make_list_of_reference_dicts(bibtex_file):

    results = []
    with open(bibtex_file) as inputfile:
        
        for line in inputfile:
            
            results.append(line)
            
    article_index = []
    
    for line, ind in zip(results, range(len(results))):
        
        if "@article" in line:
            
            article_index.append(ind)
            
    article_dict_list = []
            
    for i in range(len(article_index)-1):
        
        article_element = results[article_index[i]:article_index[i+1]]
    
        article_d = make_article_element(article_element)

        article_dict_list.append(article_d)

    return article_dict_list

def replace_labels_to_foot_notes(bibtex_file, beamer_file, new_file_path):

    foo = make_list_of_reference_dicts(bibtex_file)
    
    with open(new_file_path, "w") as new_file:
	
	with open(beamer_file) as file_tex: 
	    
	    for line in file_tex:

		if "%%Label{" in line:

            	    key_label = line.replace("%%Label{", "")
            	    key_label = key_label.replace("}", "")
            	    key_label = key_label.replace("\n", "")                    

            	    for di in foo:

            	        if di['ReferenceKey'] == key_label:
            	            
            	            line_to_write = "\\blfootnote{" + di["FootNoteText"] + "}\n"

            	            new_file.write(line_to_write)
            	            
            	else:
            	    
            	    new_file.write(line)

