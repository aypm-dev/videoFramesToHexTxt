from PIL import Image
import os
import time

outputFolder = "output"
file = open(r"" + outputFolder + "/" + str(input("\nInsert txt ouput name: ")) + ".txt","w+")
hexadecimalLookupTable = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","F"]

framesFolder = "videoFrames"
frameExtension = ".jpg"

def processRow(rowY, imageData):
    x = 0
    line = ""
    pixeles = imageData.load()

    while x < 32:
        red = hexadecimalLookupTable[(round((pixeles[x, rowY][0]) / 16))]
        green = hexadecimalLookupTable[(round((pixeles[x, rowY][1]) / 16))]
        blue = hexadecimalLookupTable[(round((pixeles[x, rowY][2]) / 16))]
        line += str(red) + str(green) + str(blue)
        x += 1
        if x == 32:
            return line

def processImageRows(imageData):
    currentY = 0
    colorData = ""
    i = 0

    while i < 32:
        colorData += processRow(currentY, imageData)
        currentY += 1
        i += 1

    return colorData

def getPixelsFromImage(imagePath):
    imageData = Image.open(framesFolder + "/" + imagePath, 'r')
    colorData = processImageRows(imageData)
    file.write(colorData)
    file.write("\n")
    print("Frame " + imagePath + "... Converted to Hexadecimal RGB")

def main():
    videoFramesAmount = len([file for file in os.listdir(framesFolder) if file.endswith(frameExtension)])
    print(f"Detected {videoFramesAmount} frames in the folder. \n\n Getting data...")

    # Pause for 1 second to allow the user to see the detected frame count
    time.sleep(3)

    currentFrame = 0

    while True:
        getPixelsFromImage(str(currentFrame) + frameExtension)

        if currentFrame == (videoFramesAmount - 1):
            print("\n\n\n\n\n\n\n\n\n\nSuccess :D\nSaved to: " + file.name + "\n\n")
            input()
            break 

        currentFrame += 1
    

main()
    

    










    






