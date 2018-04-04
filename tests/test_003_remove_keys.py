"""
test_remove_keys.py - test removing keys on card

Copyright (C) 2016, 2018  g10 Code GmbH
Author: NIIBE Yutaka <gniibe@fsij.org>

This file is a part of Gnuk, a GnuPG USB Token implementation.

Gnuk is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Gnuk is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Remove a key material on card by changing algorithm attributes of the key

from card_const import *

def test_rsa_keyattr_change_1(card):
    r = card.cmd_put_data(0x00, 0xc1, KEY_ATTRIBUTES_RSA4K)
    if r:
        r = card.cmd_put_data(0x00, 0xc1, KEY_ATTRIBUTES_RSA2K)
    assert r

def test_rsa_keyattr_change_2(card):
    r = card.cmd_put_data(0x00, 0xc2, KEY_ATTRIBUTES_RSA4K)
    if r:
        r = card.cmd_put_data(0x00, 0xc2, KEY_ATTRIBUTES_RSA2K)
    assert r

def test_rsa_keyattr_change_3(card):
    r = card.cmd_put_data(0x00, 0xc3, KEY_ATTRIBUTES_RSA4K)
    if r:
        r = card.cmd_put_data(0x00, 0xc3, KEY_ATTRIBUTES_RSA2K)
    assert r
