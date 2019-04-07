from PIL import Image
from PIL import ImageFilter


im = Image.open("nicholascage.jpg")
size_of_image = picture.size
#imm = im.filter(ImageFilter.SMOOTH_MORE)
im.show()

imm = im.filter(ImageFilter.E)
imm.show()
