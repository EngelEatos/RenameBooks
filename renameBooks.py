import os
import re
#options
#1 - surname, name - serie bd. {} - title
    #1.1 - surname, name - title1 - title2
    #1.2 - surname, name - title
#2 - name surname - serie bd. {} - title
    #2.1 name surname - title1 - title2
    #2.2 name surname - title
#3 - #1 & #2 without bd.

pattern_1 = r'^(?P<surname>.*?),\s(?P<name>.*?)\s-\s(?P<serie>.*?)\s[B|b]d.\s(?P<number>[0-9]{1,2})\s-\s(?P<title>.*?)\.epub$'
pattern_1_1 = r'^(?P<surname>.*?),\s(?P<name>.*?)\s-\s(?P<serie>.*?)\s-\s(?P<title>.*?)\.epub$'
pattern_1_2 = r'^(?P<surname>.*?),\s(?P<name>.*?)\s-\s(?P<title>.*?)\.epub$'

pattern_2 = r'^(?P<name>.*?)\s(?P<surname>.*?)\s-\s(?P<serie>.*?)\s[B|b]d.\s(?P<number>[0-9]{1,2})\s-\s(?P<title>.*?)\.epub$'
pattern_2_1 = r'^(?P<name>.*?)\s(?P<surname>.*?)\s-\s(?P<serie>.*?)\s-\s(?P<title>.*?)\.epub$'
pattern_2_2 = r'^(?P<name>.*?)\s(?P<surname>.*?)\s-\s(?P<title>.*?)\.epub$'

def clean_filename(s):
    return s.replace("_", " ")

def match(f):
    pattern = [pattern_1, pattern_1_1, pattern_1_2, pattern_2, pattern_2_1, pattern_2_2]
    result = {}
    for p in pattern:
        regex = re.compile(p)
        m = regex.match(f)

        if m:
            groupNames = list(regex.groupindex.keys())
            print(m.groups())
            for i in range(len(m.groups())):
                result[groupNames[i]] = m.groups(0)[i]
            return result

FOLDER = "/mnt/veracrypt1/BOOKS"
for dirpath, dnames, fnames in os.walk("/home/chaos/Dropbox/Ebooks"):
    for f in fnames:
        if f.endswith(".epub"):
            print(f, "==>", match(clean_filename(f)))
