#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Create by Cao Ya'nan on 2020-06-04
"""
import string
from string import ascii_letters
import re, urllib.request, webbrowser as wb


def test_0():
    print(pow(2, 38))


def test_1():
    text = '''
    g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
    '''
    low_asc = string.ascii_lowercase
    rep_asc = (low_asc[2:] + low_asc[:2])
    trans_table = str.maketrans(low_asc, rep_asc)
    text = text.translate(trans_table)
    print(text)
    print('map'.translate(trans_table))


def test_2():
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') as f:
        result = re.findall('<!--(.*?)-->', f.read().decode('utf8'), re.S)
        print(result)
        print(''.join([c for c in result[1] if c in ascii_letters]))

    # wb.open('http://www.pythonchallenge.com/pc/def/%s.html'%.join())
