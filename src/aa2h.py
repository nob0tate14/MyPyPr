'''
Created on 2018/01/08

@author: nob0tate14
'''
import re
import sys


if __name__ == '__main__':

    args = sys.argv

    f = open(args[1], 'r')

    hex_list = []
    for r in f:
        r = re.sub("\S", "1", r)
        r = r.replace(" ", "0")
        r = r.strip()
        if r != "":
            h = hex(int(r, 2))
        else:
            h = ""
        hex_list.append(h)

    h_text = ""
    for h in hex_list:
        if h == "":
            print(h_text)
            h_text = ""
        else:
            if h_text != "":
                h_text += ", "
            h_text += h
    else:
        print(h_text)
