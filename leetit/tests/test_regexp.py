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
        r = regexp.findall(case[0])
        assert r == case[1]

# TODO Write all other tests

def test_yus():
    cases = (
        ("u Use    SaMe ",["u Use    SaMe"]),
        (" you     Use SaMe",["you     Use SaMe"]),
        (" u - you - Use - SaMe ",[]),
    )
    check_regexp(VOC["YUS"][0], cases)


def test_leet():
    cases = (
        (
            " lEeT  eLeEt  LeEtE  eLeEtE  eLeTe  let  elet  lete ",
            ["lEeT", "eLeEt", "LeEtE", "eLeEtE", "eLeTe"]
        ),
        (" alEeT  eLeEta  aLeEtE  eLeEtEa  aeLeTe  let  elet  lete ", []),
    )
    check_regexp(VOC["LEET"][0], cases)


def test_woot():
    cases = (
        ("wE OwNeD oThEr tEaM",["wE OwNeD oThEr tEaM"]),
        ("sonetext wE OwNeD oThEr tEaM sometext",["wE OwNeD oThEr tEaM"]),
        (" wE - OwNeD - oThEr - tEaM - sometext",[]),
        (" awE OwNeD oThEr tEaM",[]),
        (" wE OwNeD oThEr tEaMa ",[]),
    )
    check_regexp(VOC["WOOT"][0], cases)


def test_wp():
    cases = (
        ("wElL pLaYeD",["wElL pLaYeD"]),
        ("sometext wElL pLaYeD sometext",["wElL pLaYeD"]),
        (" wElL - pLaYeD ",[]),
        (" awElL  pLaYeD ",[]),
    )
    check_regexp(VOC["WP"][0], cases)

"""
def test_hf():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_tv():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_thx():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_cu():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_idk():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_idc():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_idgaf():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_bm():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_bd():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_nc():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_we():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_ez():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_nvm():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_oz():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dod():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_tdude():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dude():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dudes():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_bye():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_bb():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_bl():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_gl():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_gg():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_stfu():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_norp():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_omg():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_wtf():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_omgwtf():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_pwnd():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_pwn():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_noob():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_or():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_nd():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_and():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_now():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_zero():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_one():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_n1():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_two():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dot():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dots():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dog():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dogs():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_star():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_stars():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_dnt():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_u():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)


def test_q():  # TODO
    cases = (
        ("",[]),
    )
    check_regexp(VOC[""][0], cases)
"""

def test_kk():
    cases = (
        ("ok", ["ok"]),
        ("   oK", ["oK"]),
        ("Ok   ", ["Ok"]),
        ("   OK   ", ["OK"]),
        ("sometext ok sometext", ["ok"]),
        ("sometextok", []),
        ("oksometext", []),
        ("sometextoksometext", []),
        (" o  k  aoa  aka  ", []),
    )
    check_regexp(VOC["KK"][0], cases)


