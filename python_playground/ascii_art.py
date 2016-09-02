import sys, random, argparse
import numpy as np
import math

from PIL import Image
# each ascii will be converted too 0-225 grey scale.
#need same width focnt
"""

Convert the input image to grayscale.
2.	 Split the image into MxN tiles.
3.	 Correct M (the number of rows) to match the image and font aspect
ratio.
ASCII Art     914.	 Compute the average brightness for each image tile and then look up a
suitable ASCII character for each.
5.	 Assemble rows of ASCII character strings and print them to a file to
form the final image.

using pillow pibrary

# grayscale level values from:
# http://paulbourke.net/dataformats/asciiart/

"""

#defining levals of greay
# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
# 10 levels of gray
gscale2 = '@%#*+=-:. '


def getAverageL(image):
    #get image as numpy array
    im = np.array(image)
    #get dimensions
    w,h = im.shape
    #get average
    return np.average(im.reshape(w*h))



def covertImageToAscii(fileName, cols, scale, moreLevels):

    global gscale1, gscale2

    #open image and convert to grayscale
    image = Image.open(fileName).convert('L')
    #store image dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))
    #COMPUTE TILE width
    w = W/cols
    #compute tile heigh based on ascpect ratio and scale of font
    h = w/scale
    #compute number of rows to use in final grip
    rows = int(H/h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dimsL %d x %d" % (w,h))

    #check if image is too small
    if cols > W or rows > H:
        print("Image to small ")
        exit(0)


#COMPUTING AVERAGE BRIGHTNESS


#GENERATING ASCII CONTENT FROM IMAGE
    aimg=[]
    #list of tile imensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        #correct the last tile
        if j == rows-1:
            y2 = H
        #append an empy string
        aimg.append("")
        for i in range(cols):
            #crop image to fit
            x1 = int(i*w)
            x2 = int((i+1)*w)
            #correct last time
            if i == cols-1:
                x2 = W
            #crop image to extract tile into the tile into another image object
            img = image.crop((x1, y1, x2, y2))
            #get the average luminance
            avg = int(getAverageL(img))
            #look up the ASCII character for grayscale value (avg)
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            #append Ascii cahracter to the string
            aimg[j] += gsval
        #return text image
    return aimg


#MAIN FUNCTION
def main():
    # create Parser
    #COMMAND LINE OPTIONS
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    #expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action='store_true')
    parser.add_argument('--cols', dest='cols', required=False)

    args = parser.parse_args()

    imgFile = args.imgFile
    #set output file
    outFile = 'out.txt'
    # set scale default as 0.43, which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    cols = 80
    if args.cols:
        cols = int(args.cols)
    print('Generating ASCII ART...')
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)

    #open a new text file
#WRITING ASCII ART STRINGS TO TEXT FILE

    #open a new text file
    #if args.outFile:
    f = open(outFile, 'w')
    #write each string in the list to the new file
    for row in aimg:
        f.write(row + '\n')
    #clean up
    f.close()
    print("ASCII art written to %s" % outFile)


#CALL MAIN
if __name__== '__main__':
    main()




