from PIL import Image
import sys
import random

MAX = 255
def imageminus(a,b):
	return (a-b) % MAX

if __name__ == "__main__":
    pieces = input('how many parts: ')

    _strlist = []
    for p in range(int(pieces)):
        _image = Image.open(str(p)+'.png')
        _rgb = _image.convert('RGB')
        strlist = _rgb.load()
        _strlist.append(strlist)
    width = _image.size[0]
    height = _image.size[1]

    origin = _strlist[int(pieces) - 1]
    _strlist.pop()
    _img = Image.new('RGB', (width, height), (0, 0, 0))
    _img.show()
    for h in range(height):
        for w in range(width):
            sum1 = origin[w,h][0]
            sum2 = origin[w,h][1]
            sum3 = origin[w,h][2]
            for picture in _strlist:
                sum1 = imageminus(sum1,picture[w,h][0])
                sum2 = imageminus(sum2,picture[w,h][1])
                sum3 = imageminus(sum3,picture[w,h][2])
            _img.putpixel((w, h), (sum1,sum2,sum3))
    _img.save('origin.png','PNG')