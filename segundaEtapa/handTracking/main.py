import cv2
import mediapipe as mp


# Função para detectar a mão na imagem e desenhar pontos-chave
def detect_hand(imagem):
    # Inicializar o mediapipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    # Ler a imagem
    image = cv2.imread(imagem)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Converter de BGR para RGB

    # Detectar mãos na imagem
    results = hands.process(imageRGB)
    handsPoints = results.multi_hand_landmarks

    # desenhar pontos-chave na imagem
    if handsPoints:
        for points in handsPoints:
            for landmark in points.landmark:
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)  #desenha um circulo nas landmarks
    
    if handsPoints:          
        numero = 0
        for i in range(5):
            hand = results.multi_hand_landmarks[0]
            if hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y:
                numero += 2**i

        # Desenha o número na imagem
        cv2.putText(image, str(numero), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)            

    # Mostrar a imagem com os pontos-chave da mão
    cv2.imshow('Hand Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Chamada da função para detectar a mão na imagem
detect_hand('mao5.jpg')
