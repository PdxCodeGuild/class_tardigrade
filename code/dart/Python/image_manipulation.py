from PIL import Image, ImageOps
from PIL import Image, ImageDraw
import colorsys

""" VERSION 1 - make the pic grayscale """

# image = Image.open("lenna.png")
# image_2 = ImageOps.grayscale(image) # changes pic to grayscale 
# width, height = image.size
# pixels = image.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]

#         # Y = (0.299*R + 0.587*G + 0.114*B)

#         pixels[i, j] = (r, g, b)

# image_2.show()

""" VERSION 2 - increase the saturation, decrease the brightness and rotate the hue """

# image = Image.open("lenna.png")
# width, height = image.size
# pixels = image.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
# # colorsys uses colors in the range [0, 1]
# h, s, v = colorsys.rgb_to_hsv(r/3, g/3, b/3)

# # do some math on h, s, v

# # r, g, b = colorsys.hsv_to_rgb(h, s, v)

# # convert back to [0, 255]

# # r = int(r*255)
# # g = int(g*255)
# # b = int(b*255)

""" VERSION 3 - draw stick figure using Pillow"""

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((100, 100), (300, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)


circle_x = width/2
circle_y = height/2
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()