# -*- encoding: utf-8 -*-

import imgio
from PIL import Image
import img

def rgb_to_bn(i):
    img_luminancia=luminancia(i)
    histograma=calc_hist(img_luminancia)
    matriu=img.matrix(img_luminancia)
    llindar=calc_llinda(histograma)
    matriu_bn=[]
    for fila in matriu:
        fila_n=[]
        for pixel in fila:
            fila_n += [0] if pixel<llindar else [255]
        matriu_bn+=[fila_n]
    return ("1",matriu_bn)

def calc_hist(i):
    matriu=img.matrix(i)
    llista=[0]*256
    for fila in matriu:
        for pixel in fila:
            llista[pixel]+=1
    return llista

def luminancia(i):
    matriu=img.matrix(i)
    w=img.get_w(i)
    h=img.get_h(i)
    imatge_grey=img.white_grey(w,h)
    imatge_grey=imatge_grey[1]
    i=0
    while i<h:
        j=0
        while j<w:
            pixel=matriu[i][j]
            pixel_grey=(pixel[0]+pixel[1]+pixel[2])/3
            imatge_grey[i][j]=pixel_grey
            j+=1
        i+=1
    return 'L', imatge_grey
            
def calc_llinda(histData):

    total = sum(histData)
    s = sum(t*histData[t] for t in range(256))
    sumB = 0.0
    (wB) = 0
    (wF) = 0
    varMax = 0.0
    threshold = 0
    for t in range(256):
        wB += histData[t]          
        if (wB == 0): 
            continue
        wF = total - wB            
        if (wF == 0):
            break
        sumB += t * histData[t]
        mB = sumB / wB;            
        mF = (s - sumB) / wF;    
        varBetween = wB *wF *( mB - mF) * (mB - mF)
        if (varBetween > varMax):
            varMax = varBetween
            threshold = t
    return threshold
