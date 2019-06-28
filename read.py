import cv2

c = 0
 
steps = input()

steps = steps.split(" ")

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
        cv2.imshow("step", image) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
if(c == 1):
    print("Error en la ejecución")
else:   
    print("Success!!!")    

"""
cv2.namedWindow('step', cv2.WINDOW_NORMAL)
image = cv2.imread("U.PNG",1)
cv2.imshow("step",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""