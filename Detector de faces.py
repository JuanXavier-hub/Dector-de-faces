import PySimpleGUI as sg
import cv2
from PIL import ImageGrab
import numpy as np

#função de ajuste de tamanho de imagem

def redimensiona (frame, scale=1):
    
    width = int((frame.shape[1] * scale))
    hight = int((frame.shape[0] * scale))
    dimensions = (width, hight)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

#Função de detecção de faces

def detecta_face (imagem):   
   
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = classificador.detectMultiScale(cinza, 1.3, 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(imagem,(x,y),(x+w,y+h),(255,0,0),2)
    return imagem

#layout

sg.theme("DarkBlue")

layout = [
         [sg.Text("Detector de Faces", size=(60, 1), justification="center")],
         [sg.Image(filename="", key='frame')],
         [sg.Button('Sair')]
         ]

#Inicialização da janela e carregamento do classificador para detecção dos rostos

janela = sg.Window("Gravador de tela", layout, location=(300,100))
classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #arquivo padrão obtido em https://github.com/opencv/opencv/tree/master/data/haarcascades

#Manipulação dos dados

while janela:
    event, values = janela.Read(timeout=20)
    if event == "Sair" or event == sg.WIN_CLOSED:
        break
    frame = np.array(ImageGrab.grab(bbox=())) #captura de frame e transformação em um array
    frame = redimensiona(frame, .5) #Ajuste de tamanho (metade do tamanho original)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Ajuste de cor
    detecta_face(frame) #Detecta faces
    janela['frame'](data=cv2.imencode('.png', frame)[1].tobytes()) #Atualiza o frame na janela

cv2.destroyAllWindows
janela.close()
