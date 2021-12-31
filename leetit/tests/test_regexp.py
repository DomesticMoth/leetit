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
from leetit import VOC


def check_regexp(regexp, cases):
    for case in cases:
        r = regexp.search(case[0])
        if r is not None:
            r = r.group(0)
        assert r == case[1]

def test_ok():
    cases = (
        ("ok", "ok"),
        ("   ok", "   ok"),
        ("ok   ", "ok   "),
        ("   ok   ", "   ok   "),
        ("sometext ok sometext", " ok "),
        ("sometextok", None),
        ("oksometext", None),
        ("sometextoksometext", None),
        #
        ("oK", "oK"),
        ("   oK", "   oK"),
        ("oK   ", "oK   "),
        ("   oK   ", "   oK   "),
        ("sometext oK sometext", " oK "),
        ("sometextoK", None),
        ("oKsometext", None),
        ("sometextoKsometext", None),
        #
        ("Ok", "Ok"),
        ("   Ok", "   Ok"),
        ("Ok   ", "Ok   "),
        ("   Ok   ", "   Ok   "),
        ("sometext Ok sometext", " Ok "),
        ("sometextOk", None),
        ("Oksometext", None),
        ("sometextOksometext", None),
        #
        ("OK", "OK"),
        ("   OK", "   OK"),
        ("OK   ", "OK   "),
        ("   OK   ", "   OK   "),
        ("sometext OK sometext", " OK "),
        ("sometextOK", None),
        ("OKsometext", None),
        ("sometextOKsometext", None),
    )
    check_regexp(VOC["KK"][0], cases)

# TODO Write test for all other vocabular regexps (have time to do it by the next year)
