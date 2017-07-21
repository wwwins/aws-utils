# aws-utils
aws utilities

## installation
pip install boto

## s3upload
python s3upload.py -b bucket -i image.jpg
python s3upload.py -b bucket -f images -i image.jpg
python s3upload.py -b bucket -f images -i image.jpg -t img.jpg
python s3upload.py -p tokyo -b bucket -i image.jpg

## detectface
python detectface.py -i image.jpg
