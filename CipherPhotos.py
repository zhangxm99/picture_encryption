from PIL import Image
import sys
import random

percent = 0.8
MAX = 255

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def imageplus(a,b):
	return (a+b) % MAX

if __name__ == "__main__":
	image = Image.open(sys.argv[1])
	width = image.size[0]
	height = image.size[1]

	rgb = image.convert('RGB')
	src_strlist = rgb.load()

	pieces = input('How many parts :')
	for p in range(int(pieces) - 1):
		img = Image.new('RGB', (width, height), (10, 32, 4))
		for h in range(height):
			for w in range(width):
				if random.random() < percent:
					img.putpixel((w, h), random_color())
		img.save(str(p)+'.png','PNG')


	_strlist = []
	for p in range(int(pieces) - 1):
		_image = Image.open(str(p)+'.png')
		_rgb = _image.convert('RGB')
		strlist = _rgb.load()
		_strlist.append(strlist)
	_strlist.append(src_strlist)

	_img = Image.new('RGB', (width, height), (0, 0, 0))
	for h in range(height):
		for w in range(width):
			sum1 = sum2 = sum3 = 0
			for picture in _strlist:
				sum1 = imageplus(picture[w,h][0],sum1)
				sum2 = imageplus(picture[w,h][1],sum2)
				sum3 = imageplus(picture[w,h][2],sum3)
			_img.putpixel((w, h), (sum1,sum2,sum3))
	_img.save(str(int(pieces) - 1)+'.png','PNG')
		
		
	
	