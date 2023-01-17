#!/usr/bin/python3
""" Uses requests module to fetch URL status"""

import requests


if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(req.text)))
    print('\t- content: {_content}'.format(_content=req.text))
