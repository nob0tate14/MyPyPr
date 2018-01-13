'''
Created on 2018/01/06

@author: nob0tate14
'''
import os

from banne import PyBanner
from banne import AFD


if __name__ == '__main__':

    # simple sample
    os.system('python3 banne.py "Hello banne.py!" -s=kerning')

    # class sample
    pybanner = PyBanner()
    pybanner.set_param("option.symbol", True)
    # pybanner.set_config("font.width", 10)
    # pybanner.set_config("fill_error_font", True)

    pybanner.make_ban_text("<<spade>><<clover>><<heart>>"
                           "<<diamond>><<joker>>")
    print(pybanner.get_ban_text_string())

    pybanner.set_config("font", AFD)
    pybanner.make_ban_text("<<Gracie>>")
    txt_lst = pybanner.get_ban_text_list()
    for txt in txt_lst:
        print(txt)

'''end of file
'''
