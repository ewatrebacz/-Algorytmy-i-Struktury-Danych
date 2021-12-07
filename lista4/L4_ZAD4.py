from os import path

def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    file_obj = open(filename, 'r')
    text = file_obj.read()
    text_list = text.split('-->')
    for i in range(0,len(text_list)):
        index = text_list[i].find('<!--')
        text_list[i] = text_list[i][0:index]
    new_text = ''.join(text_list)
    new_text = new_text.split('>')
    stack = []
    for i in range(0, len(new_text)-1):
        if new_text[i].count('<') != 1:
            return False
        start = new_text[i].find('<')
        step = start + 1 
        while new_text[i][step] == ' ':
            step += 1
        end = new_text[i].find(' ', step+1)
        if end == -1:
            mar = new_text[i][step:]
        else:
            mar = new_text[i][step:new_text[i].find(' ',step+1)]
        if mar not in ['meta', 'link', 'img', 'hr', '!DOCTYPE', 'br']:
            if mar[0] != '/':
                stack = [mar] + stack
            else:
                if mar[1:] == stack[0]:
                    stack = stack[1:]
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
