def counting_chars_without_ifs(filename):
    """Count the number of times each character appears in the text file given as the argument
    
@param filename:(str) name of the text file

@return:(dict) dictionary where the keys are the characters appearing in the text and the values ​​are the number of occurrences of each character"""
    file_ref = open(filename, 'r')
    text = file_ref.read()
    text_list = text.split()
    char_list = []
    for i in text_list:
        for j in i:
            char_list.append(j.lower())
    char_set = set(char_list)
    char_count = {}
    for i in char_set:
        char_count[i] = (text.lower()).count(i)
    file_ref.close()
    return char_count