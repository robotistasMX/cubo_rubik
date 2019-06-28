#microcoders RobotistasMX
#librerias................
import numpy as np
import cv2
import kociemba
cap = cv2.VideoCapture(0)

def nothing(x):
    pass

#Creamos una ventana llamada 'image' en la que habra todos los sliders
cv2.namedWindow('image')
cv2.createTrackbar('Hue Minimo','image',0,255,nothing)
cv2.createTrackbar('Hue Maximo','image',0,255,nothing)
cv2.createTrackbar('Saturation Minimo','image',0,255,nothing)
cv2.createTrackbar('Saturation Maximo','image',0,255,nothing)
cv2.createTrackbar('Value Minimo','image',0,255,nothing)
cv2.createTrackbar('Value Maximo','image',0,255,nothing)

#0 amarillo, 1 azul, 2 verde, 3 naranja, 4 rojo, 5 blanco
n=-1
cadena=""
bandera=0
colores=[]
amarillo=[]
azul=[]
verde=[]
naranja=[]
rojo=[]
blanco=[ ]

opc_cubo=0
if opc_cubo == 0:
    cubo = "cubo1.txt"
if opc_cubo == 1:
    cubo = "cubo2.txt"

i=0
archivo = open(cubo, "r")
for linea in archivo.readlines():
    #print(linea)
    x = linea.split(",")
    if i==0:
        for line_num in range(0,6):
            amarillo.append(int(x[line_num]))
    if i==1:
        for line_num in range(0,6):
            azul.append(int(x[line_num]))
    if i==2:
        for line_num in range(0,6):
            verde.append(int(x[line_num]))
    if i==3:
        for line_num in range(0,6):
            naranja.append(int(x[line_num]))
    if i==4:
        for line_num in range(0,6):
            rojo.append(int(x[line_num]))
    if i==5:
        for line_num in range(0,6):
            blanco.append(int(x[line_num]))
    i=i+1
archivo.close()


COLOR_MIN=[]
COLOR_MAX=[]

COLOR_MIN.append(np.array([amarillo[0],amarillo[1],amarillo[2]],np.uint8))       # HSV color code lower and upper bounds
COLOR_MAX.append(np.array([amarillo[3],amarillo[4],amarillo[5]],np.uint8))       # color yellow
COLOR_MIN.append(np.array([azul[0],azul[1],azul[2]],np.uint8))       # HSV color code lower and upper bounds
COLOR_MAX.append(np.array([azul[3],azul[4],azul[5]],np.uint8))       ## color blue
COLOR_MIN.append(np.array([verde[0],verde[1],verde[2]],np.uint8))       # HSV color code lower and upper bounds
COLOR_MAX.append(np.array([verde[3],verde[4],verde[5]],np.uint8))       ## color green
COLOR_MIN.append(np.array([naranja[0],naranja[1],naranja[2]],np.uint8))       # HSV color code lower and upper bounds
COLOR_MAX.append(np.array([naranja[3],naranja[4],naranja[5]],np.uint8))       ## color orange
COLOR_MIN.append(np.array([rojo[0],rojo[1],rojo[2]],np.uint8))       # HSV color code lower and upper bounds
COLOR_MAX.append(np.array([rojo[3],rojo[4],rojo[5]],np.uint8))       ## color red
COLOR_MIN.append(np.array([blanco[0],blanco[1],blanco[2]],np.uint8))       # HSV color code lower and upper bounds
COLOR_MAX.append(np.array([blanco[3],blanco[4],blanco[5]],np.uint8))       ## color white

while(True):
    _, im = cap.read()
    #im = cv2.bilateralFilter(im,9,75,75)
    #im = cv2.fastNlMeansDenoisingColored(im,None,10,10,7,21)
    #hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2YUV)   # HSV image
    hsv_img= im
    hMin = cv2.getTrackbarPos('Hue Minimo','image')
    hMax = cv2.getTrackbarPos('Hue Maximo','image')
    sMin = cv2.getTrackbarPos('Saturation Minimo','image')
    sMax = cv2.getTrackbarPos('Saturation Maximo','image')
    vMin = cv2.getTrackbarPos('Value Minimo','image')
    vMax = cv2.getTrackbarPos('Value Maximo','image')

    lower = np.array([hMin,sMin,vMin])
    upper = np.array([hMax,sMax,vMax])
    calibracion = cv2.inRange(hsv_img, lower,upper )
    filtro1 = cv2.erode(calibracion, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
    filtro2 = cv2.erode(filtro1, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
    del colores[:]
    for i in range(0,6):
        frame_threshed = cv2.inRange(hsv_img, COLOR_MIN[i], COLOR_MAX[i])     # Thresholding image
        imgray = frame_threshed
        ret,thresh = cv2.threshold(frame_threshed,127,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # print type(contours)

        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            #area=(x+w)*(y+h)
            if i==0:
                if w > 100 and h >100:
                    #print("AMARILLO:")
                    #print(x,y,w,h)
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,255),2)
                    colores.append(str(x)+","+str(y)+","+"amarillo")
            elif i==1:
                if w > 100 and h >100:
                    #print("AZUL:")
                    #print(x,y,w,h)
                    cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                    colores.append(str(x)+","+str(y)+","+"azul")
            elif i==2:
                if w > 100 and h >100:
                    #print("VERDE:")
                    #print(x,y,w,h)
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                    colores.append(str(x)+","+str(y)+","+"verde")
            elif i==3:
                if w > 100 and h >100:
                    #print("NARANJA:")
                    #print(x,y,w,h)
                    cv2.rectangle(im,(x,y),(x+w,y+h),(20,117,255),2)
                    colores.append(str(x)+","+str(y)+","+"naranja")
            elif i==4:
                if w > 100 and h >100:
                    #print("ROJO:")
                    #print(x,y,w,h)
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
                    colores.append(str(x)+","+str(y)+","+"rojo")
            elif i==5:
                if w > 100 and h >100 and w < 700 and h <700 :
                    #print("BLANCO:")
                    #print(x,y,w,h)
                    cv2.rectangle(im,(x,y),(x+w,y+h),(255,255,255),2)
                    colores.append(str(x)+","+str(y)+","+"blanco")

    cv2.imshow("Resultado",im)
    bandera=1
    cv2.imshow('calibracion', filtro2)
    cv2.imshow("Camara",im)

    k = cv2.waitKey(10)
    if k == 27:
        cv2.destroyWindow("Resultado")

    if k & 0xFF == ord('e'):
        break

    if k & 0xFF == ord('n'):
        print("next")
        n=n+1
        if n==6:
            n=0
        if n==0:
            print("Calibrar amarillo")
            cv2.setTrackbarPos('Hue Minimo','image',amarillo[0])
            cv2.setTrackbarPos('Hue Maximo','image', amarillo[3])
            cv2.setTrackbarPos('Saturation Minimo','image',amarillo[1])
            cv2.setTrackbarPos('Saturation Maximo','image',amarillo[4])
            cv2.setTrackbarPos('Value Minimo','image',amarillo[2])
            cv2.setTrackbarPos('Value Maximo','image',amarillo[5])

        if n==1:
            print("Calibrar azul")
            cv2.setTrackbarPos('Hue Minimo','image',azul[0])
            cv2.setTrackbarPos('Hue Maximo','image', azul[3])
            cv2.setTrackbarPos('Saturation Minimo','image',azul[1])
            cv2.setTrackbarPos('Saturation Maximo','image',azul[4])
            cv2.setTrackbarPos('Value Minimo','image',azul[2])
            cv2.setTrackbarPos('Value Maximo','image',azul[5])
        if n==2:
            print("Calibrar verde")
            cv2.setTrackbarPos('Hue Minimo','image',verde[0])
            cv2.setTrackbarPos('Hue Maximo','image', verde[3])
            cv2.setTrackbarPos('Saturation Minimo','image',verde[1])
            cv2.setTrackbarPos('Saturation Maximo','image',verde[4])
            cv2.setTrackbarPos('Value Minimo','image',verde[2])
            cv2.setTrackbarPos('Value Maximo','image',verde[5])
        if n==3:
            print("Calibrar naranja")
            cv2.setTrackbarPos('Hue Minimo','image',naranja[0])
            cv2.setTrackbarPos('Hue Maximo','image', naranja[3])
            cv2.setTrackbarPos('Saturation Minimo','image',naranja[1])
            cv2.setTrackbarPos('Saturation Maximo','image',naranja[4])
            cv2.setTrackbarPos('Value Minimo','image',naranja[2])
            cv2.setTrackbarPos('Value Maximo','image',naranja[5])
        if n==4:
            print("Calibrar rojo")
            cv2.setTrackbarPos('Hue Minimo','image',rojo[0])
            cv2.setTrackbarPos('Hue Maximo','image', rojo[3])
            cv2.setTrackbarPos('Saturation Minimo','image',rojo[1])
            cv2.setTrackbarPos('Saturation Maximo','image',rojo[4])
            cv2.setTrackbarPos('Value Minimo','image',rojo[2])
            cv2.setTrackbarPos('Value Maximo','image',rojo[5])
        if n==5:
            print("Calibrar blanco")
            cv2.setTrackbarPos('Hue Minimo','image',blanco[0])
            cv2.setTrackbarPos('Hue Maximo','image', blanco[3])
            cv2.setTrackbarPos('Saturation Minimo','image',blanco[1])
            cv2.setTrackbarPos('Saturation Maximo','image',blanco[4])
            cv2.setTrackbarPos('Value Minimo','image',blanco[2])
            cv2.setTrackbarPos('Value Maximo','image',blanco[5])



    if k & 0xFF == ord('s'):
        if n==0:
            print("Se cambio valores amarillo")
            COLOR_MIN[0] = np.array([hMin,sMin,vMin])
            COLOR_MAX[0] = np.array([hMax,sMax,vMax])
            amarillo=[hMin,sMin,vMin,hMax,sMax,vMax]
        if n==1:
            print("Se cambio valores azul")
            COLOR_MIN[1] = np.array([hMin,sMin,vMin])
            COLOR_MAX[1] = np.array([hMax,sMax,vMax])
            azul=[hMin,sMin,vMin,hMax,sMax,vMax]
        if n==2:
            print("Se cambio valores verde")
            COLOR_MIN[2] = np.array([hMin,sMin,vMin])
            COLOR_MAX[2] = np.array([hMax,sMax,vMax])
            verde=[hMin,sMin,vMin,hMax,sMax,vMax]
        if n==3:
            print("Se cambio valores naranja")
            COLOR_MIN[3] = np.array([hMin,sMin,vMin])
            COLOR_MAX[3] = np.array([hMax,sMax,vMax])
            naranja=[hMin,sMin,vMin,hMax,sMax,vMax]
        if n==4:
            print("Se cambio valores rojo")
            COLOR_MIN[4] = np.array([hMin,sMin,vMin])
            COLOR_MAX[4] = np.array([hMax,sMax,vMax])
            rojo=[hMin,sMin,vMin,hMax,sMax,vMax]
        if n==5:
            print("Se cambio valores blanco")
            COLOR_MIN[5] = np.array([hMin,sMin,vMin])
            COLOR_MAX[5] = np.array([hMax,sMax,vMax])
            blanco=[hMin,sMin,vMin,hMax,sMax,vMax]
            n=-1

        f = open(cubo,'w')
        f.write(str(amarillo[0])+","+str(amarillo[1])+","+str(amarillo[2])+","+str(amarillo[3])+","+str(amarillo[4])+","+str(amarillo[5])+ '\n')
        f.write(str(azul[0])+","+str(azul[1])+","+str(azul[2])+","+str(azul[3])+","+str(azul[4])+","+str(azul[5])+'\n')
        f.write(str(verde[0])+","+str(verde[1])+","+str(verde[2])+","+str(verde[3])+","+str(verde[4])+","+str(verde[5])+'\n')
        f.write(str(naranja[0])+","+str(naranja[1])+","+str(naranja[2])+","+str(naranja[3])+","+str(naranja[4])+","+str(naranja[5])+ '\n')
        f.write(str(rojo[0])+","+str(rojo[1])+","+str(rojo[2])+","+str(rojo[3])+","+str(rojo[4])+","+str(rojo[5])+ '\n')
        f.write(str(blanco[0])+","+str(blanco[1])+","+str(blanco[2])+","+str(blanco[3])+","+str(blanco[4])+","+str(blanco[5])+ '\n')
        f.close()


    if k & 0xFF == ord('q'):
        print(colores)

    if k & 0xFF == ord('r'):
        cadena=""

    if k & 0xFF == ord('c') and bandera ==1:
        for caras in range(1,len(colores)):
            for ordenar in range(caras,0,-1):
                x2 = colores[ordenar].split(",")
                x = colores[ordenar-1].split(",")
                if int(x[1]) >= int(x2[1]):
                    aux_colores=colores[ordenar-1]
                    colores[ordenar-1]=colores[ordenar]
                    colores[ordenar]=aux_colores

        renglon1 = [colores[0],colores[1],colores[2]]
        renglon2 = [colores[3],colores[4],colores[5]]
        renglon3 = [colores[6],colores[7],colores[8]]

        for caras in range(1,len(renglon1)):
            for ordenar in range(caras,0,-1):
                x2 = renglon1[ordenar].split(",")
                x = renglon1[ordenar-1].split(",")
                if int(x[0]) >= int(x2[0]):
                    aux_colores=renglon1[ordenar-1]
                    renglon1[ordenar-1]=renglon1[ordenar]
                    renglon1[ordenar]=aux_colores

        for caras in range(1,len(renglon2)):
            for ordenar in range(caras,0,-1):
                x2 = renglon2[ordenar].split(",")
                x = renglon2[ordenar-1].split(",")
                if int(x[0]) >= int(x2[0]):
                    aux_colores=renglon2[ordenar-1]
                    renglon2[ordenar-1]=renglon2[ordenar]
                    renglon2[ordenar]=aux_colores

        for caras in range(1,len(renglon3)):
            for ordenar in range(caras,0,-1):
                x2 = renglon3[ordenar].split(",")
                x = renglon3[ordenar-1].split(",")
                if int(x[0]) >= int(x2[0]):
                    aux_colores=renglon3[ordenar-1]
                    renglon3[ordenar-1]=renglon3[ordenar]
                    renglon3[ordenar]=aux_colores

        colores=[renglon1[0],renglon1[1],renglon1[2],renglon2[0],renglon2[1],renglon2[2],renglon3[0],renglon3[1],renglon3[2]]
        #print(colores)
        #rojo F, blanco R, amarillo L, naranja B, azul D, verde U
        for num_colores in range(0,len(colores)):
            x = colores[num_colores].split(",")
            if x[2] == "amarillo":
                cadena = cadena + "L"
            if x[2] == "azul":
                cadena = cadena + "D"
            if x[2] == "verde":
                cadena = cadena + "U"
            if x[2] == "naranja":
                cadena = cadena + "B"
            if x[2] == "rojo":
                cadena = cadena + "F"
            if x[2] == "blanco":
                cadena = cadena + "R"

        print(cadena)
        print("FALTAN: "+ str(int(6-(len(cadena)/9))) +" CARAS.")
        bandera=0

    if k & 0xFF == ord('p'):
        solucion=kociemba.solve(cadena)
        print(solucion)
        steps = solucion.split(" ")

        cv2.namedWindow("step", cv2.WINDOW_NORMAL)

        image = cv2.imread("wait.png",1)
        cv2.imshow("Wait",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        for i in range(len(steps)):
            print(steps[i])
            cv2.namedWindow("step", cv2.WINDOW_NORMAL)
            image = cv2.imread(""+ steps[i] + "" + ".PNG" , 1)
            print(""+ steps[i] + "" + ".PNG")
            if (not image.data):
                print("No se encontró la imager...")
                c = 1
                break
            else:
                c=0
                cv2.imshow("step", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        if(c == 1):
            print("Error en la ejecución")
        else:
            print("Success!!!")

cv2.destroyAllWindows()
