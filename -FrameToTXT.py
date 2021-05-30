from PIL import Image

file = open(r""+ str(input("\nInsert txt ouput name: ")) + ".txt","w+")
Nframe = 0
FramesNumber = input("\nInsert the number of frames: ")
Hexadecimal = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","F"]

def ObtenerPixeles(Imagen):
    
    Y = 0; B = ""; i = 0
    a = Image.open("Frames/" + str(Imagen) + ".jpg", 'r')
    while i < 32:
        B = B + X(Y, a)
        Y += 1
        i += 1
        if i == 32:
            file.write(str(B))
            file.write("\n")
            print("Frame " + Imagen + "... Binarizado")

def X(y, A):
    x = 0
    line = ""
    pixeles = A.load()
    while x < 32:


        Red = Hexadecimal[(round((pixeles[x, y][0]) / 16))]
        Green = Hexadecimal[(round((pixeles[x, y][1]) / 16))]
        Blue = Hexadecimal[(round((pixeles[x, y][2]) / 16))]
        line = line + str(Red) + str(Green) + str(Blue)

        x += 1
        if x == 32:
            return line

while True:
    ObtenerPixeles(str(Nframe))

    if Nframe == int(FramesNumber):
        
        print("\n\n\n\n\n\n\n\n\n\nSuccess :D\n\n")
        input()
        break 
    Nframe += 1
    
    

    










    






