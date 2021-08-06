from PIL import Image, ImageChops
import os


IMAGE_PATH = "images/"

def process(baseline_file, file_name):
    baseline = Image.open(baseline_file).convert('RGB') 
    chrome_file = IMAGE_PATH + "chrome-" + file_name
    firefox_file = IMAGE_PATH + "firefox-" + file_name
    edge_file = IMAGE_PATH + "edge-" + file_name
    
    screenshot_name = file_name.split(".")[0]
    if os.path.isfile(chrome_file):
        print("Processing C")
        # compare(IMAGE_PATH + file, chrome_file, baseline, "chrome")
        compare(baseline, chrome_file, f"chrome-{screenshot_name}")
    if os.path.isfile(firefox_file):
        print("Processing F")
        # compare(IMAGE_PATH + file, firefox_file, baseline, "firefox") 
        compare(baseline, firefox_file, f"firefox-{screenshot_name}") 
    if os.path.isfile(edge_file):
        print("Processing E")
        # compare(IMAGE_PATH + file, edge_file, baseline, "edge")
        compare(baseline, edge_file, f"edge-{screenshot_name}") 

def compare(baseline, browser_image, browser_and_screen):
    comparison = Image.open(browser_image).convert('RGB') 
    diff = ImageChops.difference(baseline, comparison)

    if diff.getbbox():
        # other ways to compare
            # print(f"difference found: {browser}")
            # diff.show()
            # mask = Image.new("L", img1.size, 128)
            # im = Image.composite(img1, img2, mask)
            # # im.show()
            # im.save(IMAGE_PATH + browser + "-" + baseline + "-difference.jpg")
            # overlay = ImageChops.overlay(img1, img2)
            # overlay.show()
        diff.save(IMAGE_PATH + browser_and_screen + "-difference.png", "PNG")

for path, Directory, files in os.walk(IMAGE_PATH):
    for file in files:
        if file.startswith("zeplin-"):
            file_name = file.split("zeplin-")[1]
            process(IMAGE_PATH + file, file_name)
