from PIL import Image
import sys

def main():
    if len(sys.argv) == 3:
        infile = sys.argv[1]
        outfile = sys.argv[2]
        size = int(sys.argv[3])
    else:
        print("Do this:\n extruder.py *input picture path* *output picture path* *tile side length (for example: 16)*")
        quit()


    image = Image.open(infile)
    inPixels = image.load()

    width = image.size[0]
    newWidth = width + width // size * 2
    height = image.size[1]
    newHeight = height + height // size * 2

    outImage = Image.new("RGB", (newWidth, newHeight), "green")
    outPixels = outImage.load()

    for w in range(width // size):
        for h in range(height // size):
            for i in range(size):
                for j in range(size):
                    outPixels[i + size * w + w * 2 + 1, j + size * h + h * 2 + 1] = inPixels[i + size * w, j + size * h]

    for w in range(width // size):
        for h in range(newHeight):
            outPixels[w * size + w * 2, h] = outPixels[w * size + w * 2 + 1, h]

    for w in range(width // size):
        for h in range(newHeight):
            outPixels[(w + 1) * size + w * 2 + 1, h] = outPixels[(w + 1) * size + w * 2, h]

    for w in range(newWidth):
        for h in range(height // size):
            outPixels[w, h * size + h * 2] = outPixels[w, h * size + h * 2 + 1]

    for w in range(newWidth):
        for h in range(height // size):
            outPixels[w, (h + 1) * size + h * 2 + 1] = outPixels[w, (h + 1) * size + h * 2]

    outImage.save(outfile)

if __name__ == "__main__":
    main()
