from PIL import Image, ImageChops


img1 = Image.open('images/zeplin.png').convert('RGB') 
# img2 = Image.open('images/chrome.png').convert('RGB') 
img2 = Image.open('images/wrong.png').convert('RGB') 
# img1 = Image.open('images/zeplin.jpeg')
# img2 = Image.open('images/wrong.jpeg')


diff = ImageChops.difference(img1, img2)

# print(diff.getbbox())
if diff.getbbox():
    print("different")
    # diff.show()

    mask = Image.new("L", img1.size, 128)
    im = Image.composite(img1, img2, mask)
    # im.show()
    im.save("images/test.jpg")
else:
    print("no diff found")

# overlay = ImageChops.overlay(img1, img2)
# overlay.show()