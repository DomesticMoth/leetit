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

# re.IGNORECASE
#  => (?:\s+|^)
#  => (?:\s+|$)

#(?:\s+|^)(?:\s+|$)


"""
[name]: ([pattern], ([sub1], [sub2],  ...  [subN]))
"""
VOC={
    "YUS": [r"(?:(?:you)|u)\s+use\s*same", ["yus",]],
    "LEET": [r"(?:(?:e{0,1}(?:leet)e{0,1})|(?:elete))", ["1337",]],
    "WOOT": [r"we\s+ow{0,1}ned\s+other\s+tea{0,1}m", ["woot",]],
    "WP": [r"wel+\s+played", ["wp",]],
    "HF": [r"ha[vw]e\s+fun", ["hf",]],
    "TY": [r"thank\s+(?:(?:you)|u)", ["ty",]],
    "THX": [r"than(?:x|(?:ks))", ["thx",]],
    "CU": [r"(?:(?:see\s+(?:(?:you)|u))|(?:cu)|(?:cy))", ["cu", "cy"]],
    "IDK": [r"i\s+don['`]*t\s+k{0,1}now", ["idk",]],
    "IDC": [r"i\s+don['`]*t\s+care", ["idc",]],
    "IDGAF": [r"i\s+don['`]*t\s+give\s+a\s+fuck", ["idgaf",]],
    "BM": [r"bad\s+man+ers", ["bm",]],
    "BD": [r"ban+e*d", ["bd",]],
    "NC": [r"no\s+com+ents", ["n/c",]],
    "WE": [r"wh{0,1}atever", ["w/e",]],
    "EZ": [r"ea{0,1}[sz][ye]", ["ez",]],
    "NVM": [r"never\s+mind", ["nvm",]],
    "OZ": [r"o(?:(?:th)|z)er", ["oz",]],
    "DOD": [r"du+de", ["dod", "dude", "duude"]],
    "TDUDE": [r"he", ["this duude", "this dude", "this dood"]],
    "DUDE": [r"(?:(?:man)|(?:human)|(?:male)|(?:guy)|(?:person))", ["dude", "duude", "dood", "comrad"]],
    "DUDES": [r"(?:(?:mans)|(?:humans)|(?:males)|(?:guys)|(?:people)|(?:party))", ["duudes", "dudes", "doods", "comrads"]],
    "BYE":  [r"bye", ["bye bye",]],
    "BB": [r"bye\s+bye", ["bb",]],
    "BL": [r"bad\s+luck", ["bl",]],
    "GL": [r"good\s+luck", ["gl",]],
    "GG": [r"good\s+game", ["gg",]],
    "STFU": [r"shut\s+(?:(?:the)|(?:de)|(?:da))\s+fuck\s+up", ["stfu",]],
    "NORP": [r"(?:(?:porno*)|(?:pron)|(?:norp)|(?:porm)|(?:pornography))", ["pron","norp","porm"]],
    "OMG": [r"oh\s+my\s+go+d", ["OMG",]],
    "WTF": [r"wh+at\s+(?:(?:the)|(?:da)|(?:ze))\s+f[ua]c*k*", ["WTF",]],
    "OMGWTF": [r"omg\s+wtf", ["OMGWTF",]],
    "PWND": [r"owned", ["pwnd",]],
    "PWN": [r"own", ["pwn",]],
    "NOOB": [r"(?:(?:no+b)|(?:newbi*e*))", ["noob","newbie"]],
    "OR": [r"or", ["|", "||"]],
    "NO": [r"(?:(?:no)|(?:not)|(?:false)|(?:nope))", ["!", "nope"]],
    "AND": [r"and", ["&", "&&"]],
    "NOW": [r"k{0,1}now", ["now", "know"]],
    "ZERO": [r"(?:(?:zero)|(?:none)|(?:n[iu]+l+))", ["0",]],
    "ONE": [r"(?:(?:one)|(?:first))", ["1",]],
    "N1": [r"nice\s+one", ["n1", "nice 1", "none"]],
    "TWO": [r"(?:(?:tw*o)|2)", ["two", "to", "2"]],
    "DOT": [r"dot", [".",]],
    "DOTS": [r"dots", ["..",]],
    "DOG": [r"dog", ["@",]],
    "DOGS": [r"dogs", ["@@",]],
    "STAR": [r"star", ["*",]],
    "STARS": [r"stars", ["**",]],
    "DNT": [r"do[nm]['`]*t", ["dnt",]],
    "KK": [r"[o0][kc]", ["kk",]],
    "U": [r"you", ["u",]],
    "Q": [r"q(?:ue){2}", ["Q",]],
}

for key in VOC.keys():
    start = r"(?:\s+|^)"
    end = r"(?:\s+|$)"
    VOC[key][0] = re.compile(start+VOC[key][0]+end, re.IGNORECASE)
    for i in range(len(VOC[key][1])):
        VOC[key][1][i] = " "+VOC[key][1][i]+" "

def clear(text: str) -> str:
    pass

def vocabular(text: str, seed: int = 1337) -> str:
    pass # TODO

def morphology(text: str, seed: int = 1337) -> str:
    pass # TODO

def substitution(text: str, unicode: bool = False, seed: int = 1337) -> str:
    pass # TODO

def convert(text: str, unicode: bool = False, seed: int = 1337) -> str:
    return substitution(morphology(vocabular(text, seed), seed), unicode, seed)
