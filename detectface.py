#!/usr/bin/env python
"""
    Usage:
        python detectface.py -i image.jpg
"""

from argparse import ArgumentParser
import boto3
from pprint import pprint
import sys

def get_client(endpoint):
    client = boto3.client('rekognition')
    return client

def get_args():
    parser = ArgumentParser(description='Detect faces')
    parser.add_argument('-e', '--endpoint')
    parser.add_argument('-i', '--image')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    if (args.image is None):
        print('''
        Usage:
            python detectface.py --help
            ''')
        sys.exit(-1)
    client = get_client(args.endpoint)
    with open(args.image, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()},Attributes=['ALL'])
        pprint(response)
