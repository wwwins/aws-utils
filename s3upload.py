# -*- coding: utf-8 -*-
"""
    Usage:
        python s3upload.py -b bucket -i image.jpg
        python s3upload.py -b bucket -f images -i image.jpg
        python s3upload.py -b bucket -f images -i image.jpg -t img.jpg
        python s3upload.py -p tokyo -b bucket -i image.jpg
"""

from argparse import ArgumentParser
from pprint import pprint
import boto3
import os
import sys

def get_client(profile):
    boto3.setup_default_session(profile_name=profile)
    client = boto3.client('s3')
    return client

def get_args():
    parser = ArgumentParser(description='upload file to s3')
    parser.add_argument('-p', '--profile', default='default')
    parser.add_argument('-i', '--image')
    parser.add_argument('-b', '--bucket')
    parser.add_argument('-f', '--folder')
    parser.add_argument('-t', '--target')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    # pprint(args)
    if (args.image is None):
        print('''
        Usage:
            python s3upload.py --help
            ''')
        sys.exit(-1)
    folder = ''
    image = ''
    if args.folder:
        folder = args.folder+'/';
    if args.target:
        image = args.target;
    else:
        image = os.path.basename(args.image)

    # print(args.bucket+'/'+folder+image)
    client = get_client(args.profile)
    client.upload_file(args.image, args.bucket, folder+image)
    print('done')
