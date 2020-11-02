fn = '<path_of_text_file>'
p = os.popen('attrib +h ' + fn)
t = p.read()
p.close()