import argparse
from PyPDF2 import PdfWriter

merger = PdfWriter()

parser = argparse.ArgumentParser(description='this is a pdf merger tool')

parser.add_argument('--files' , nargs='+', required=True, help= 'name of the files to be merged' )
parser.add_argument('--output', required=True, help= 'name of the output pdf file' )

args = parser.parse_args()

print("Files to be merged: " , args.files)
print("name of the file which is merged: " , args.output)

for i in args.files:
    merger.append(i)

merger.write(args.output)
merger.close()
