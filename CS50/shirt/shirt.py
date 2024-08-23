import sys
from PIL import Image
from PIL import ImageOps
import os
def main ():
    file1,file2 =file()
    design(file1,file2)

def file() :
    if len(sys.argv)!=3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        file_1= sys.argv[1].lower()
        file_2 = sys.argv[2].lower()
        file1_ext = os.path.splitext(file_1)[1]
        file2_ext= os.path.splitext(file_2)[1]
        valid_extension = [".jpg",".jpeg",".png"]
        if file1_ext not in valid_extension and file2_ext not in valid_extension:
            sys.exit("Invalid output")
        if file1_ext != file2_ext:
            sys.exit("Input and output have different extensions")
        return file_1,file_2


def design(file1,file2):
    try:
        with Image.open(file1) as im:
            shirt = Image.open("shirt.png")
            im = ImageOps.fit(im, shirt.size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
            im.paste(shirt, shirt)
            im.save(file2)


    except FileNotFoundError:

        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
