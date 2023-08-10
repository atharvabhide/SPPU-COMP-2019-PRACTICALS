from captcha.image import ImageCaptcha

# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)

# Image captcha text
captcha_text = 'CSDF LAB 2'

# generate the image of the given text
data = image.generate(captcha_text)

# write the image on the given file and save it
image.write(captcha_text, 'CAPTCHA.png')

#read from image text
X = input("Enter text from image captcha below-\n")

#compare input with captcha text
if X == captcha_text:
    print("Verified")
else:
    print("Failed")
