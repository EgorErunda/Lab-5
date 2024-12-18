import re
import codecs


#task 2
pattern = r'<([a-zA-Z][a-zA-Z0-9]*)>'

file_HTML = codecs.open("task2.html", "r", "utf_8_sig" )
txt = file_HTML.read()
file_HTML.close()
open_tags = re.findall(pattern, txt)
unique_tags = list(dict.fromkeys(open_tags))
print(unique_tags)