from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='this is a image rezise cli tool created by Atharva')
parser.add_argument("--image" , required=True , help = 'Add image name here') 
parser.add_argument("--width" , required=True ,type = int ,help = 'Add desired width here') 
parser.add_argument("--height" , required=True ,type = int, help = 'Add desired height here') 
parser.add_argument("--resized" , required=True , help = 'Add the image file name here (resized)')
args = parser.parse_args()

im = Image.open(args.image)
size = im.size

if im.mode == 'RGBA':
    im = im.convert('RGB')

width = args.width
height = args.height
resize = im.resize((width,height))
resize.save(args.resized)
print("Image successfully Resized!")
