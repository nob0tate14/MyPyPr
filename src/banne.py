#  Copyright 2018 Nobuo Tateishi<nob0tate14@gmail.com>
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
'''Created on 2018/01/03

@author: nob0tate14
'''

import argparse
from builtins import str
import sys


DFD = {}
DFD["0"] = (0x0E, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0E)
DFD["1"] = (0x04, 0x0C, 0x04, 0x04, 0x04, 0x04, 0x0E)
DFD["2"] = (0x0E, 0x11, 0x02, 0x04, 0x08, 0x10, 0x1F)
DFD["3"] = (0x0E, 0x11, 0x01, 0x0E, 0x01, 0x11, 0x0E)
DFD["4"] = (0x02, 0x06, 0x0A, 0x12, 0x1F, 0x02, 0x02)
DFD["5"] = (0x1F, 0x10, 0x10, 0x1E, 0x01, 0x11, 0x0E)
DFD["6"] = (0x0E, 0x11, 0x10, 0x1E, 0x11, 0x11, 0x0E)
DFD["7"] = (0x1F, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08)
DFD["8"] = (0x0E, 0x11, 0x11, 0x0E, 0x11, 0x11, 0x0E)
DFD["9"] = (0x0E, 0x11, 0x11, 0x0F, 0x01, 0x11, 0x0E)
DFD["A"] = (0x04, 0x0A, 0x11, 0x11, 0x1F, 0x11, 0x11)
DFD["B"] = (0x1E, 0x11, 0x11, 0x1E, 0x11, 0x11, 0x1E)
DFD["C"] = (0x0E, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0E)
DFD["D"] = (0x1E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x1E)
DFD["E"] = (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x1F)
DFD["F"] = (0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x10)
DFD["G"] = (0x0E, 0x11, 0x10, 0x13, 0x11, 0x11, 0x0E)
DFD["H"] = (0x11, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11)
DFD["I"] = (0x0E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E)
DFD["J"] = (0x01, 0x01, 0x01, 0x01, 0x01, 0x11, 0x0E)
DFD["K"] = (0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11)
DFD["L"] = (0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1F)
DFD["M"] = (0x11, 0x1B, 0x15, 0x11, 0x11, 0x11, 0x11)
DFD["N"] = (0x11, 0x11, 0x19, 0x15, 0x13, 0x11, 0x11)
DFD["O"] = (0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E)
DFD["P"] = (0x1E, 0x11, 0x11, 0x1E, 0x10, 0x10, 0x10)
DFD["Q"] = (0x0E, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0D)
DFD["R"] = (0x1E, 0x11, 0x11, 0x1E, 0x14, 0x12, 0x11)
DFD["S"] = (0x0E, 0x11, 0x10, 0x0E, 0x01, 0x11, 0x0E)
DFD["T"] = (0x1F, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04)
DFD["U"] = (0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E)
DFD["V"] = (0x11, 0x11, 0x11, 0x11, 0x11, 0x0A, 0x04)
DFD["W"] = (0x11, 0x11, 0x11, 0x11, 0x15, 0x1B, 0x11)
DFD["X"] = (0x11, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x11)
DFD["Y"] = (0x11, 0x11, 0x0A, 0x04, 0x04, 0x04, 0x04)
DFD["Z"] = (0x1F, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1F)
DFD["a"] = (0x00, 0x00, 0x0E, 0x01, 0x0F, 0x11, 0x0F)
DFD["b"] = (0x10, 0x10, 0x16, 0x19, 0x11, 0x11, 0x1E)
DFD["c"] = (0x00, 0x00, 0x0F, 0x10, 0x10, 0x10, 0x0F)
DFD["d"] = (0x01, 0x01, 0x0D, 0x13, 0x11, 0x11, 0x0F)
DFD["e"] = (0x00, 0x00, 0x0E, 0x11, 0x1F, 0x10, 0x0F)
DFD["f"] = (0x03, 0x04, 0x0E, 0x04, 0x04, 0x04, 0x04)
DFD["g"] = (0x00, 0x00, 0x0F, 0x11, 0x0F, 0x01, 0x0E)
DFD["h"] = (0x10, 0x10, 0x16, 0x19, 0x11, 0x11, 0x11)
DFD["i"] = (0x04, 0x00, 0x0C, 0x04, 0x04, 0x04, 0x04)
DFD["j"] = (0x04, 0x00, 0x0C, 0x04, 0x04, 0x04, 0x18)
DFD["k"] = (0x10, 0x10, 0x12, 0x14, 0x18, 0x14, 0x12)
DFD["l"] = (0x0C, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04)
DFD["m"] = (0x00, 0x00, 0x1A, 0x15, 0x15, 0x15, 0x11)
DFD["n"] = (0x00, 0x00, 0x1E, 0x11, 0x11, 0x11, 0x11)
DFD["o"] = (0x00, 0x00, 0x0E, 0x11, 0x11, 0x11, 0x0E)
DFD["p"] = (0x00, 0x00, 0x1E, 0x11, 0x1E, 0x10, 0x10)
DFD["q"] = (0x00, 0x00, 0x0F, 0x11, 0x0F, 0x01, 0x01)
DFD["r"] = (0x00, 0x00, 0x17, 0x18, 0x10, 0x10, 0x10)
DFD["s"] = (0x00, 0x00, 0x0F, 0x10, 0x0E, 0x01, 0x1E)
DFD["t"] = (0x00, 0x04, 0x0E, 0x04, 0x04, 0x04, 0x03)
DFD["u"] = (0x00, 0x00, 0x11, 0x11, 0x11, 0x11, 0x0F)
DFD["v"] = (0x00, 0x00, 0x11, 0x11, 0x11, 0x0A, 0x04)
DFD["w"] = (0x00, 0x00, 0x11, 0x15, 0x15, 0x15, 0x1A)
DFD["x"] = (0x00, 0x00, 0x11, 0x0A, 0x04, 0x0A, 0x11)
DFD["y"] = (0x00, 0x00, 0x11, 0x0A, 0x04, 0x08, 0x10)
DFD["z"] = (0x00, 0x00, 0x1F, 0x02, 0x04, 0x08, 0x1F)
DFD[" "] = (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
DFD["!"] = (0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04)
DFD['"'] = (0x0A, 0x0A, 0x0A, 0x00, 0x00, 0x00, 0x00)
DFD["#"] = (0x0A, 0x0A, 0x1F, 0x0A, 0x1F, 0x0A, 0x0A)
DFD["$"] = (0x04, 0x0F, 0x14, 0x0E, 0x05, 0x1E, 0x04)
DFD["%"] = (0x19, 0x19, 0x02, 0x04, 0x08, 0x13, 0x13)
DFD["&"] = (0x0C, 0x12, 0x12, 0x0C, 0x15, 0x12, 0x1D)
DFD["'"] = (0x04, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00)
DFD["("] = (0x04, 0x08, 0x10, 0x10, 0x10, 0x08, 0x04)
DFD[")"] = (0x04, 0x02, 0x01, 0x01, 0x01, 0x02, 0x04)
DFD["*"] = (0x00, 0x04, 0x15, 0x0E, 0x15, 0x04, 0x00)
DFD["+"] = (0x00, 0x04, 0x04, 0x1F, 0x04, 0x04, 0x00)
DFD[","] = (0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x08)
DFD["-"] = (0x00, 0x00, 0x00, 0x1F, 0x00, 0x00, 0x00)
DFD["."] = (0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x04)
DFD["/"] = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x00)
DFD[":"] = (0x00, 0x04, 0x04, 0x00, 0x04, 0x04, 0x00)
DFD[";"] = (0x00, 0x04, 0x04, 0x00, 0x04, 0x04, 0x08)
DFD["<"] = (0x02, 0x04, 0x08, 0x10, 0x08, 0x04, 0x02)
DFD["="] = (0x00, 0x00, 0x1F, 0x00, 0x1F, 0x00, 0x00)
DFD[">"] = (0x08, 0x04, 0x02, 0x01, 0x02, 0x04, 0x08)
DFD["?"] = (0x0E, 0x11, 0x02, 0x04, 0x04, 0x00, 0x04)
DFD["@"] = (0x0E, 0x11, 0x01, 0x0D, 0x15, 0x15, 0x0B)
DFD["["] = (0x1E, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1E)
DFD["yen"] = (0x11, 0x0A, 0x1F, 0x04, 0x1F, 0x04, 0x04)
DFD["\\"] = (0x00, 0x10, 0x08, 0x04, 0x02, 0x01, 0x00)
DFD["]"] = (0x0F, 0x01, 0x01, 0x01, 0x01, 0x01, 0x0F)
DFD["^"] = (0x04, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00)
DFD["_"] = (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F)
DFD["`"] = (0x04, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00)
DFD["{"] = (0x0E, 0x08, 0x08, 0x10, 0x08, 0x08, 0x0E)
DFD["|"] = (0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04)
DFD["}"] = (0x0E, 0x02, 0x02, 0x01, 0x02, 0x02, 0x0E)
DFD["~"] = (0x0D, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00)
DFD["<<spade>>"] = (0x08, 0x1C, 0x3E, 0x7F, 0x7F, 0x08, 0x1C)
DFD["<<clover>>"] = (0x1C, 0x1C, 0x6B, 0x7F, 0x6B, 0x08, 0x1C)
DFD["<<heart>>"] = (0x22, 0x77, 0x7F, 0x7F, 0x3E, 0x1C, 0x08)
DFD["<<diamond>>"] = (0x08, 0x1C, 0x3E, 0x7F, 0x3E, 0x1C, 0x08)
DFD["<<joker>>"] = (0x22, 0x77, 0x22, 0x08, 0x41, 0x3E, 0x1C)

AFD = {}
AFD["<<Gracie>>"] = (
    0x0FFC7FC,
    0xF00F802,
    0x20FC1E4,
    0x1F87E88,
    0x0004910,
    0x0005F20,
    0x0018018,
    0x0063E06,
    0x008C101,
    0x0113F81,
    0x0EFDE01,
    0x081BE02,
    0x040F842,
    0x030018C,
    0x00E0E30,
    0x001FFC0)

EFD = {}
EFD["ERROR"] = (0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F)


def get_pipeline_text():
    text = sys.stdin.readline()
    return text


def do_parse_args():
    parser = argparse.ArgumentParser(
        prog="banner.py",
        usage="python3 banne.py \"0123ABCDwxyz:;<=\\]^_\`{|}~%%&\" -w12 -m1,1",
        description="banner by python\n",
        add_help=True)

    parser.add_argument("text", nargs="?", action="store", type=str,
                        default=None, help="banner text")
    parser.add_argument("-b", "--bright", action="store", type=str,
                        default=" ", help="bright pixel")
    parser.add_argument("-d", "--dark", action="store", type=str,
                        default="#", help="dark pixel")
    parser.add_argument("-m", "--margin", action="store", type=str,
                        default="1,0",
                        help="margin for space of char and line.")
    parser.add_argument("-o", "--option", action="store", type=str,
                        default=None, help="optional function")
    parser.add_argument("-s", "--style", action="store", type=str,
                        default=None, help="style for text. can use bold,"
                        "italic,bottomline,linethrough,kerning")
    parser.add_argument("-w", "--wrap", action="store", type=int,
                        default=None, help="wrap the text")
    args = parser.parse_args()

    return args


def do_args_to_param(args):
    param = {}

    param["margin.x"] = int(args.margin.split(",")[0])
    param["margin.y"] = int(args.margin.split(",")[1])

    param["option.yen"] = False
    param["option.symbol"] = False
    if args.option is not None:
        if args.option.find("yen") >= 0:
            param["option.yen"] = True
        if args.option.find("symbol") >= 0:
            param["option.symbol"] = True

    param["pixel.bright"] = args.bright
    param["pixel.dark"] = args.dark

    param["style.bold"] = False
    param["style.italic"] = False
    param["style.bottomline"] = False
    param["style.linethrough"] = False
    param["style.kerning"] = False
    if args.style is not None:
        if args.style.find("bold") >= 0:
            param["style.bold"] = True
        if args.style.find("italic") >= 0:
            param["style.italic"] = True
        if args.style.find("bottomline") >= 0:
            param["style.bottomline"] = True
        if args.style.find("linethrough") >= 0:
            param["style.linethrough"] = True
        if args.style.find("kerning") >= 0:
            param["style.kerning"] = True

    if args.text is not None:
        param["text"] = args.text

    param["wrap"] = args.wrap

    return param


class PyBanner:

    def __init__(self, *, config=None, param=None):
        self.param = {}
        self.config = {}
        self.ban_text = []

        if config is None:
            self.set_default_config()
        else:
            self.config = config

        if param is None:
            self.set_default_param()
        else:
            self.param = param

    def set_default_config(self):
        self.config["font"] = DFD
        self.config["font.width"] = 5
        self.config["fill_error_font"] = False

    def set_default_param(self):
        self.param["margin.x"] = 1
        self.param["margin.y"] = 0
        self.param["option.yen"] = False
        self.param["option.symbol"] = False
        self.param["pixel.bright"] = " "
        self.param["pixel.dark"] = "#"
        self.param["style.bold"] = False
        self.param["style.italic"] = False
        self.param["style.bottomline"] = False
        self.param["style.linethrough"] = False
        self.param["style.kerning"] = False
        self.param["wrap"] = None

    def set_param(self, name, value):
        self.param[name] = value

    def set_config(self, name, value):
        self.config[name] = value

    def get_current_text(self):
        return self.param["text"]

    def make_ban_text(self, text):
        # hex to binary
        def htob(hex_char, width):
            bin_char = format(hex_char, "b")
            ret_char = bin_char.zfill(width)
            if self.param["style.bold"] is True:
                ret_char = ret_char.replace("0", "00")
                ret_char = ret_char.replace("1", "11")
            ret_char = ret_char.replace("0", self.param["pixel.bright"])
            ret_char = ret_char.replace("1", self.param["pixel.dark"])
            return ret_char

        # char to line list and kerning hell...
        def append_char(line_list, c):
            if c not in self.config["font"]:
                if self.config["fill_error_font"] is True:
                    font = EFD["ERROR"]
                else:
                    return
            else:
                font = self.config["font"][c]
            font_width = len(format(max(font), "b"))
            if self.config["font.width"] > font_width:
                font_width = self.config["font.width"]
            if c != " " and self.param["style.kerning"] is True:
                mtrx = []
                for i in range(font_height):
                    mtrx.append(htob(font[i], font_width))
                for i in range(font_width):
                    for ii in range(font_height):
                        if mtrx[ii][0] == self.param["pixel.dark"]:
                            break
                    else:
                        for iii in range(font_height):
                            mtrx[iii] = mtrx[iii][1:]
                        continue
                    break

                for i in range(font_width)[::-1]:
                    for ii in range(font_height):
                        if mtrx[ii][-1:] == self.param["pixel.dark"]:
                            break
                    else:
                        for iii in range(font_height):
                            mtrx[iii] = mtrx[iii][:-1]
                        continue
                    break

                for i in range(font_height):
                    line_list[i].append(mtrx[i])
            else:
                for i in range(font_height):
                    line_list[i].append(htob(font[i], font_width))

        # line list to line text
        def get_line_text(line_list):
            line_text = ""
            for char in line_list:
                line_text = line_text + marginx + char
            return line_text

        def do_linethrough(line_text, i):
            if i == round(font_height / 2) - 1 and \
                    self.param["style.linethrough"] is True:
                line_text = line_text.replace(
                    self.param["pixel.bright"], self.param["pixel.dark"])
            return line_text

        def do_bottomline(line_text):
            if self.param["style.bottomline"] is True:
                line_text = line_text.replace(
                    self.param["pixel.bright"], self.param["pixel.dark"])
                self.ban_text.append(line_text)

        # line text to banner text
        def store_line_text(line_text, i):
            slant = ""
            if self.param["style.italic"] is True:
                slant = self.param["pixel.bright"] * i
            self.ban_text.append(slant + line_text)

        self.ban_text = []

        marginx = ""
        for i in range(self.param["margin.x"]):
            marginx += self.param["pixel.bright"]

        font_height = len(list(self.config["font"].values())[0])

        line_list = []
        for i in range(font_height):
            line_list.append([])

        char_list = []
        if self.param["option.symbol"] is True:
            txt_dsct = text
            for word in self.config["font"]:
                if word.startswith("<<"):
                    txt_dsct = txt_dsct.replace(word, "\t" + word + "\t")
            txt_dsct = txt_dsct.split("\t")
            for word in txt_dsct:
                if word in self.config["font"]:
                    char_list.append(word)
                else:
                    for c in word:
                        char_list.append(c)
        else:
            for c in text:
                char_list.append(c)

        for c in char_list:
            if c == "\\" and self.param["option.yen"] is True \
                    and "yen" in self.config["font"].keys():
                c = "yen"
            append_char(line_list, c)

        if self.param["wrap"] is None:
            for i in range(font_height):
                line_text = get_line_text(line_list[i])
                line_text = do_linethrough(line_text, i)
                store_line_text(line_text, font_height - i)
            do_bottomline(line_text)

        else:
            ii = 0
            while ii < len(line_list[0]):
                iii = ii + self.param["wrap"]
                for i in range(font_height):
                    line_text = get_line_text(line_list[i][ii:iii])
                    line_text = do_linethrough(line_text, i)
                    store_line_text(line_text, font_height - i)
                do_bottomline(line_text)

                ii += self.param["wrap"]
                for i in range(self.param["margin.y"]):
                    self.ban_text.append("")

    def get_ban_text_string(self):
        ret_str = ""
        for text in self.ban_text:
            if ret_str != "":
                ret_str = ret_str + "\n"
            ret_str = ret_str + text
        return ret_str

    def get_ban_text_list(self):
        return self.ban_text


if __name__ == '__main__':

    args = do_parse_args()

    param = do_args_to_param(args)
    pybanner = PyBanner(param=param)
    if args.text is None:
        args.text = get_pipeline_text()

    pybanner.make_ban_text(args.text)

    print(pybanner.get_ban_text_string())

    # txt_lst = pybanner.get_ban_text_list()
    # for txt in txt_lst:
    #     print(txt)

''' end of file
'''
