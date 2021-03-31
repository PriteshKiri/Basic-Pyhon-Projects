from PIL import Image, ImageFilter

img = Image.open('bulbasaur.jpg')

#filter image
filtered_image = img.filter(ImageFilter.BLUR) #we can also do SMOOTH,SHARPEN etc. need to check the documentation
filtered_image = img.convert('L')
filtered_image.save("grey.png",'png') #need to convert into png coz png supports these image filters
filtered_image.show() #will show the image

#ROTATION
rot = img.rotate(-12.6) 
rot.show()


# #RESIZING
resize = img.resize((300,200)) #resize accepts the tuple
resize.show()


# #CROPING
box = (100, 100, 400, 400) #first two are the coordinates of upper left corner and next two are the coordinates of bottom right corner
cropp = img.crop(box)
cropp.show()

#THUMBNAIL - Reszing without lossing aspect ratio
astro  = Image.open('space3.jpg')
astro.thumbnail((1920,1080))
astro.save('newspace.jpg')



#CROPPING AND PASTING
paste = (160,149,320,298)
region = region.transpose(Image.ROTATE_180)
im.paste(region, paste)
im.show()


#ROLLING OF IMAGE
image = Image.open('bulbasaur.jpg')
delta = 160

def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))

    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image.show()

roll(image,delta)


#More editing tools can be explored from the documentation
#Thank you !