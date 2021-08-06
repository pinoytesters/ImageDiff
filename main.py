from PIL import Image, ImageChops
import os


IMAGE_PATH = "images/"

def compare(image1, image2, baseline, browser):
    img1 = Image.open(image1).convert('RGB') 
    img2 = Image.open(image2).convert('RGB') 
    diff = ImageChops.difference(img1, img2)

    if diff.getbbox():
        # print(f"difference found: {browser}")
        # diff.show()
        # mask = Image.new("L", img1.size, 128)
        # im = Image.composite(img1, img2, mask)
        # # im.show()
        # im.save(IMAGE_PATH + browser + "-" + baseline + "-difference.jpg")
        diff.save(IMAGE_PATH + browser + "-" + baseline + "-difference.jpg")
    else:
        print("no diff found")

    # overlay = ImageChops.overlay(img1, img2)
    # overlay.show()

for path, Directory, files in os.walk(IMAGE_PATH):
    for file in files:
        if file.startswith("zeplin-"):
            baseline = file.split("zeplin-")[1]
            print(baseline)
            chrome_file = IMAGE_PATH + "chrome-" + baseline
            firefox_file = IMAGE_PATH + "firefox-" + baseline
            edge_file = IMAGE_PATH + "edge-" + baseline
            
            if os.path.isfile(chrome_file):
                print("Processing C")
                compare(IMAGE_PATH + file, chrome_file, baseline, "chrome")
            if os.path.isfile(firefox_file):
                print("Processing F")
                compare(IMAGE_PATH + file, firefox_file, baseline, "firefox") 
            if os.path.isfile(edge_file):
                print("Processing E")
                compare(IMAGE_PATH + file, edge_file, baseline, "edge")
