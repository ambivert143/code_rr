import mss
import mss.tools

with mss.mss() as sct:

    #get value from user
    top = int(input("Top: "))
    left = int(input("Left: "))
    width = int(input("Width: "))
    height = int(input("Height: "))

    #the screen part to capture
    monitor = {"top": top,
               "left": left,
               "width": width,
               "height": height,
               }

    #grab the data
    sct_image = sct.grab(monitor)
    output = f"image-{top}x{left}_{width}x{height}.png"

    #save to the picture file
    mss.tools.to_png(sct_image.rgb, sct_image.size, output=output)
    print(output)