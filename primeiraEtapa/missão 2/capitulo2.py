import cv2
#Lendo a imagem e armazenando em uma variável 
imagem = cv2.imread('entrada2.jpg')
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB

# Analisando o pixel mais a esquerda
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

# Varrendo todos os pixeis (sendo y = pixeis da altura e x = pixeis da largura) e modificando suas cores para
# (255, 0, 0), como a ordem é BGR, a cor será azul
# Não é muito eficiente pois é um processo lento varrer toda a imagem pixel a pixel
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (255,0,0)

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)


# Mesmo conceito do for anterior, porém aqui usamos as variáveis de coluna e altura para serem 
# componentes da cor, e como queremos um valor entre 0 e 255, aplicamos o mod de 256 a variável
for y in range(0, imagem.shape[0]): #percorre linhas
    for x in range(0, imagem.shape[1]): #percorre colunas
        imagem[y, x] = (x%256,y%256,x%256)

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)


# Também semelhante ao for anterior, porém note que não teremos blue nem red na imagem, e novamente estamos usando
# as variáveis de altura e coluna para compor o Green, mas dessa vez elas são somadas e como nosso limite é 256,
# fazemos o mod 256
for y in range(0, imagem.shape[0]): #percorre as linhas
    for x in range(0, imagem.shape[1]): #percorre as colunas
        imagem[y, x] = (0,(x*y)%256,0)

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)


# Como a imagem já foi muito modificada nos for's anteriores, optei por "resetar" ela
imagem = cv2.imread('entrada2.jpg')
# Note que apesar de também ir alterando a imagem pixel a pixel, neste for fazemos um pouco diferente
# daremos passos de 10 em 10 pixels tanto na altura quanto na largura, e criamos um quadrado 5x5 da cor
# (0,255,255), como apenas o Blue está zerado, Red + Green nos dará um amarelo
for y in range(0, imagem.shape[0], 10): #percorre linhas
    for x in range(0, imagem.shape[1], 10): #percorre colunas
        imagem[y:y+5, x: x+5] = (0,255,255)

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

