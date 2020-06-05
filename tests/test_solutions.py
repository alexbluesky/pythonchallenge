#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Create by Cao Ya'nan on 2020-06-04
"""
import string
from collections import Counter
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
        # print(result)
        # print(''.join([c for c in result[1] if c in ascii_letters]))

        c = Counter(result[1])
        asc_counter = [x for x in c.most_common() if x[0] in string.ascii_letters]
        min_num = min([i[1] for i in asc_counter])
        min_asc = [x[0] for x in asc_counter if x[1] == min_num]
        print(''.join(min_asc))

    # wb.open('http://www.pythonchallenge.com/pc/def/equality.html')


def test_3():
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as f:
        text = re.findall('<!--(.*?)-->', f.read().decode('utf8'), re.S)
        # text[0] = text[0].replace('\n', '')
        # re_pattern = ''
        # result = re.findall('([a-z].{80}?)?([A-Z].{80}?)([A-Z].{80}?)([A-Z].{77}?)([A-Z]{3}([a-z])[A-Z]{3}?)(.{77}[A-Z]{1}?)(.{80}[A-Z]{1}?)(.{80}[A-Z]{1}?)(.{79}[a-z]{1}?)?', text[0], re.S)
        result = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text[0])
        print(result)
        print(''.join([i[0] for i in result]))


def test_4():
    base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
    number = 12345
    for i in range(400):
        try:
            with urllib.request.urlopen(base_url.format(number), timeout=3) as req:
                if req.code != 200:
                    break
                req_content = req.read().decode('utf8').split()
                # if i == 399:
                #     print(req_content)
                # print(i, req_content)
                if req_content[0] != 'and':
                    print(i, ' '.join(req_content))
                if req_content[0] in ['yes', 'Yes.']:
                    number /= 2
                else:
                    number = int(req_content[-1])
                # print(number)

                # if number:
                #     print(req_content.split()[-1])
        except Exception as e:
            print(e)
            if 'invalid literal for int() with base 10' in str(e):
                break

