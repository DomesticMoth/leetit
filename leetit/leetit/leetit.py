"""
    This file is part of leetit.

    leetit is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    leetit is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with leetit.  If not, see <https://www.gnu.org/licenses/>.
"""
import re
import random
import string


"""
[name]: ([pattern], ([sub1], [sub2],  ...  [subN]))
"""
VOC={
    "YUS":    [r"(?:(?:you)|u)\s+use\s*same",                                        ["yus",]],
    "LEET":   [r"(?:(?:e{0,1}(?:leet)e{0,1})|(?:elete))",                            ["1337",]],
    "WOOT":   [r"we+\s+ow{0,1}ned\s+other\s+tea{0,1}m",                              ["woot",]],
    "WP":     [r"wel+\s+played",                                                     ["wp",]],
    "HF":     [r"ha[vw]e\s+fun",                                                     ["hf",]],
    "TY":     [r"thank\s+(?:(?:you)|u)",                                             ["ty",]],
    "THX":    [r"than(?:x|(?:ks))",                                                  ["thx",]],
    "CU":     [r"(?:(?:see\s+(?:(?:you)|u))|(?:cu)|(?:cy))",                         ["cu", "cy"]],
    "IDK":    [r"i\s+don['`]*t\s+k{0,1}now",                                         ["idk",]],
    "IDC":    [r"i\s+don['`]*t\s+care",                                              ["idc",]],
    "IDGAF":  [r"i\s+don['`]*t\s+give\s+a\s+fuck",                                   ["idgaf",]],
    "BM":     [r"bad\s+man+ers",                                                     ["bm",]],
    "BD":     [r"ban+e*d",                                                           ["bd",]],
    "NC":     [r"no\s+com+ents",                                                     ["n/c",]],
    "WE":     [r"wh{0,1}atever",                                                     ["w/e",]],
    "EZ":     [r"ea{0,1}[sz][ye]",                                                   ["ez",]],
    "NVM":    [r"never\s+mind",                                                      ["nvm",]],
    "OZ":     [r"o(?:(?:th)|z)er",                                                   ["oz",]],
    "DOD":    [r"du+de",                                                             ["dod", "dude", "duude"]],
    "TDUDE":  [r"he",                                                                ["this duude", "this dude", "this dood"]],
    "DUDE":   [r"(?:(?:man)|(?:human)|(?:male)|(?:guy)|(?:person))",                 ["dude", "duude", "dood", "comrad"]],
    "DUDES":  [r"(?:(?:mans)|(?:humans)|(?:males)|(?:guys)|(?:people)|(?:party))",   ["duudes", "dudes", "doods", "comrads"]],
    "BYE":    [r"bye",                                                               ["bye bye",]],
    "BB":     [r"bye\s+bye",                                                         ["bb",]],
    "BL":     [r"bad\s+luck",                                                        ["bl",]],
    "GL":     [r"good\s+luck",                                                       ["gl",]],
    "GG":     [r"good\s+game",                                                       ["gg",]],
    "STFU":   [r"shut\s+(?:(?:the)|(?:de)|(?:da))\s+fuck\s+up",                      ["stfu",]],
    "NORP":   [r"(?:(?:p[o*]rno*)|(?:pr[o*]n)|(?:norp)|(?:porm)|(?:p[o*]rnography))",["pron","norp","porm"]],
    "OMG":    [r"oh\s+my\s+go+d",                                                    ["OMG",]],
    "WTF":    [r"wh+at\s+(?:(?:the)|(?:da)|(?:ze))\s+f[ua]c*k*",                     ["WTF",]],
    "OMGWTF": [r"omg\s+wtf",                                                         ["OMGWTF",]],
    "PWND":   [r"owned",                                                             ["pwnd",]],
    "PWN":    [r"own",                                                               ["pwn",]],
    "NOOB":   [r"(?:(?:no+b)|(?:newbi*e*))",                                         ["noob","newbie"]],
    "COOL":   [r"(?:cool)",                                                          ["k1", "k!"]],
    "YEAH":   [r"(?:yeah)",                                                          ["ya1", "ya!"]],
    "IM":      [r"(?:i['` ]*a*m)",                                                   ["ya", "i", "i"]],
    "I":      [r"(?:i)",                                                             ["ya", "i"]],
    "LOVE":   [r"(?:love)",                                                          ["luv", "love"]],
    "OR":     [r"or",                                                                ["|", "||"]],
    "NO":     [r"(?:(?:no)|(?:not)|(?:false)|(?:nope))",                             ["!", "nope"]],
    "AND":    [r"and",                                                               ["&", "&&"]],
    "NOW":    [r"k{0,1}now",                                                         ["now", "know"]],
    "ZERO":   [r"(?:(?:zero)|(?:none)|(?:n[iu]+l+))",                                ["0",]],
    "ONE":    [r"(?:(?:one)|(?:first))",                                             ["1",]],
    "N1":     [r"nice\s+one",                                                        ["n1", "nice 1", "none"]],
    "TWO":    [r"(?:(?:tw*o)|2)",                                                    ["two", "to", "2"]],
    "DOT":    [r"dot",                                                               [".",]],
    "DOTS":   [r"dots",                                                              ["..",]],
    "DOG":    [r"dog",                                                               ["@",]],
    "DOGS":   [r"dogs",                                                              ["@@",]],
    "STAR":   [r"star",                                                              ["*",]],
    "STARS":  [r"stars",                                                             ["**",]],
    "DNT":    [r"do[nm]['`]*t",                                                      ["dnt",]],
    "KK":     [r"[o0][kc]",                                                          ["kk",]],
    "U":      [r"you",                                                               ["u",]],
    "Q":      [r"q(?:ue){2}",                                                        ["Q",]],
    "TEH":    [r"q(?:the){2}",                                                       ["teh", "tex", "the", "the", "the"]],
}

MORPHEMES = (
    (re.compile(r"(?:(?:\Bcker\b)|(?:\Bker\b))"), ["xxor", "xzor", "zzor"]),
    (re.compile(r"(?:(?:\Bckers\b)|(?:\Bkers\b))"), ["xxorz", "xzorz", "zzorz"]),
    (re.compile(r"(?:(?:\Ber\b)|(?:\Bor\b))"), ["xor", "zor", "xor", "zor", "xorz", "zorz"]),
    (re.compile(r"(?:(?:\Bers\b)|(?:\Bors\b))"), ["xorz", "zorz"]),
    (re.compile(r"(?:(?:and)|(?:end)|(?:anned)|(?:ant)|(?:ent))"), ["&", "7"]),
    (re.compile(r"(?:(?:ait)|(?:ate))"), ["8", "*"]),
    (re.compile(r"(?:\Bing\b)"), ["ping"]),
    (re.compile(r"(?:\Bent\b)"), ["10", "wnt", "wnt", "ent", "ent", "ent", "ent"]),
    (re.compile(r"(?:\Bist\b)"), ["izd", "ist", "ist", "ist", "ist"]),
    (re.compile(r"(?:\Bian\b)"), ["yan", "ian", "ian"]),
    (re.compile(r"(?:\Bism\b)"), ["izm", "ism"]),
    (re.compile(r"(?:(?:\Bes\b)|(?:\Bess\b))"), ["ez"]),
    (re.compile(r"(?:\Bth\b)"), ["z", "th", "th"]),
    (re.compile(r"(?:\Bs\b)"), ["z", "s"]),
    (re.compile(r"(?:\Bed\b)"), ["t", "et", "et", "ed", "ed"]),
    (re.compile(r"(?:\Be\b)"), ["e", "e", "e", ""]),
    (re.compile(r"cks"), ["xx"]),
    (re.compile(r"(?:(?:ks)|(?:cs)|(?:x))"), ["ks", "cs", "x", "x", "x"]),
    (re.compile(r"(?:(?:u)|(?:oo))"), ["u", "oo"]),
)

ALPHABET_NOMBERS = {
    "a": ["4"],
    "b": ["8", "13"],
    "e": ["3"],
    "g": ["9", "6"],
    "i": ["1"],
    "l": ["1", "2", "7"],
    "o": ["0"],
    "p": ["9"],
    "q": ["2"],
    "r": ["9", "7", "2", "12", "3"],
    "s": ["5", "2"],
    "t": ["7"],
    "y": ["j"],
    "z": ["2"],
}

ALPHABET_ASCII = {
    "a": ["/\\", "@", "/-\\", "^", "(L"],
    "b": ["I3", "|3", "!3", "(3", "/3", ")3", "j3"],
    "c": ["[", "<", "("],
    "d": [")", "|)", "(|", "[)", "I>", "|>", "?", "T)", "I7", "c1", "|}", "|]"],
    "e": ["&", "[-", "|=-"],
    "f": ["|=", "|#", "ph", "/="],
    "g": ["&", "(_+", "C-", "gee", "(?", "[,", "(,", "(."],
    "h": ["#", "/-/", "\\-\\", "[-]", "]-[", ")-(", "(-)", ":-:", "|~|", "}{", "!-!", "1-1", "!-1", "1-!", "I-I"],
    "i": ["|", "!", "eye", "3y3"],
    "j": [",_|", "_|", "._|", "_]", "]"],
    "k": [">|", "|<", "1<", "|c"],
    "l": ["|", "|_"],
    "m": ["/\\/\\", "/V\\", "[V]", "|\\/|", "^^", "<\\/>", "{v}", "(v)", "|\\|\\", "nn", "11"],
    "n": ["^/", "|\\|", "/\\/", "[\\]", "<\\>", "{\\}", "/V", "^"],
    "o": ["()", "ch", "[]", "p", "<>"],
    "p": ["|*", "|o", "?", "|^", "|>", "[]D", "|7"],
    "r": ["I2", "|~", "|?", "/2", "|^", "lz", "[z", ".-", "|2", "|-"],
    "s": ["$", "z", "ehs"],
    "t": ["+", "-|-", "']['", "~|~"],
    "u": ["(_)", "|_|", "v", "L|"],
    "v": ["\\/", "|/", "\\|"],
    "w": ["\\/\\/", "vv", "\\N", "'//", "\\^/", "(n)", "\\v/", "\\X/", "\\|/", "\\_|_/", "uu", "2u"],
    "x": ["><", "}{", "ecks", "*", "?", "}{", ")(", "]["],
    "y": ["j", "\\//"],
    "z": ["7_", "-/_", "%", ">_", "s"],
}

ALPHABET_UNICODE_ONLY = {
    "a": ["Д"],
    "b": ["ß"],
    "c": ["¢", "©"],
    "e": ["£", "€", "ё"],
    "f": ["ƒ"],
    "n": ["И"],
    "p": ["|°"],
    "r": ["®", "Я"],
    "s": ["§"],
    "t": ["†"],
    "u": ["µ"],
    "w": ["Ш"],
    "x": ["Ж"],
    "y": ["Ч"],
}

ALPHABET_UNICODE = {}


__USAGE_LETTERS = "abcdefghijklmno"


def __wrap(a):
    for key in a.keys():
        wrapper = r"\b"
        a[key][0] = re.compile(wrapper+a[key][0]+wrapper, re.IGNORECASE)
    return a


VOC = __wrap(VOC)


def __concat_alphabets(a, b):
    for k in b.keys():
        if k in a:
            for e in b[k]:
                a[k].append(e)
        else:
            a[k] = b[k]
    return a


ALPHABET_ASCII = __concat_alphabets(ALPHABET_ASCII, ALPHABET_NOMBERS)

ALPHABET_UNICODE = __concat_alphabets(ALPHABET_UNICODE_ONLY, ALPHABET_ASCII)


def acronims(text: str, seed: int = 1337) -> str:
    random.seed(seed)
    for k in VOC.keys():
        regexp = VOC[k][0]
        subs = VOC[k][1]
        fragments = regexp.split(text)
        if len(fragments) > 0:
            text = ""
            for i, fragment in enumerate(fragments):
                text+=fragment
                if i < len(fragments)-1:  # If not last
                    text+=random.choice(subs)
    return text


def morphology(text: str, seed: int = 1337) -> str:
    random.seed(seed)
    for m in MORPHEMES:
        regexp = m[0]
        subs = m[1]
        fragments = regexp.split(text)
        if len(fragments) > 0:
            text = ""
            for i, fragment in enumerate(fragments):
                text+=fragment
                if i < len(fragments)-1:  # If not last
                    text+=random.choice(subs)
    return text


def randomcase(text: str) -> str:
    ret = ""
    for i in range(len(text)):
        if random.choice([True, False]):
            ret += text[i].upper()
        else:
            ret += text[i].lower()
    return ret


def substitution(text: str, seed: int = 1337, percent:int = 50, alphabet = ALPHABET_ASCII, chars = string.ascii_lowercase) -> str:
    random.seed(seed)
    ret = ""
    for i in range(len(text)):
        if text[i] in chars and text[i] in alphabet:
            if random.randint(0, 100) <= percent:
                ret += random.choice(alphabet[text[i]])
            else:
                ret += text[i]
        else:
            ret += text[i]
    return randomcase(ret)


def leet(text: str, seed: int = 1337, percent:int = 50, alphabet = ALPHABET_ASCII, chars = string.ascii_lowercase) -> str:
    return substitution(morphology(acronims(text, seed), seed), seed, percent, alphabet, chars)
