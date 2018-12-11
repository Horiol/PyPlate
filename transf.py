# -*- encoding: utf-8 -*-

import img
import imgio
from PIL import Image

def vtrim(i):
    """
    Donada una imatge img en blanc i negre, retorna l'imatge resultant de retallar-la verticalment
    >>> vtrim(('1',[[255,255,255,255],[255,0,255,255],[255,255,255,255],[255,255,0,255]]))
    ('1', [[255, 255], [0, 255], [255, 255], [255, 0]]
    """ 
    matriu=img.matrix(i)
    h=img.get_h(i)
    w=img.get_w(i)
    wo=""
    wf=1
    c=0
    while c<w:
        f=0
        while f<h:
            if wo=="" and matriu[f][c]==0:
                wo=c
            if wo!="" and matriu[f][c]==0:
                wf=c
            f+=1
        c+=1
    if wo=="":
        return img.null()
    else:
        img_n=img.subimg(i,wo,0,wf,h)
        return img_n

def htrim(i):
    """
    Donada una imatge img en blanc i negre, retorna la imatge resultant de retallar-la hortizontalment
    >>> htrim(('1',[[255,255,255,255],[255,0,255,255],[255,0,255,255],[255,255,255,255]]))
    ('1', [[255, 0, 255, 255], [255, 0, 255, 255]])
    """ 
    matriu=img.matrix(i)
    w=img.get_w(i)
    ho=""
    hf=1
    f=0
    for fila in matriu:
        for columna in fila:
            if ho=="" and columna==0:
                ho=f
            if ho!="" and columna==0:
                hf=(f-ho+1)
        f+=1
    if ho=="":
        return img.null()
    else:
        img_n=img.subimg(i,0,ho,w,hf)
        return img_n

def scale(i,h):
    """
    Escala homogeniament una imatge 'i' fins que la seva alçada es 'h'
    >>> scale(('1',[[0,255,255,255],[255,255,255,255],[255,255,255,255],[255,255,255,255]]),2)
    ('1', [[0, 255], [255, 255]])
    """
    matriu=img.matrix(i)
    W=img.get_w(i)
    H=img.get_h(i)
    fh=float(H)/float(h)
    w=W/fh
    w=int(w)
    matriu_n=img.matrix(img.white_bw(w,h))
    f=0
    while f<h:
        c=0
        while c<w:
            matriu_n[f][c]=matriu[int(f*fh)][int(c*fh)]
            c+=1
        f+=1
    return ('1',matriu_n)
                        
