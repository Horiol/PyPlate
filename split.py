# -*- encoding: utf-8 -*-

import img
import transf
from PIL import Image
import imgio

def split_digit(i):
    """
    Agafa una imatge en blanc i negre i retorna una tupla (D,R) on D és la imatge amb el dígit de més a l¡esquerre i R la resta de la imatge
    
    >>> split_digit(('1',[[255,0,0,0,255,255],[0,0,255,0,255,0],[0,0,0,0,255,0]]))
    (('1', [[255, 0, 0, 0, 255], [0, 0, 255, 0, 255], [0, 0, 0, 0, 255]]), ('1', [[255], [0], [0]]))
    """
    matriu=img.matrix(i)
    h=img.get_h(i)
    w=img.get_w(i)
    c=0
    while c<w:
        j=0
        compare=0
        while j<h:
            if matriu[j][c]==255:
                compare+=1
            j+=1
        if compare==h:
            W=(c+1)
            D=img.subimg(i,0,0,W,h)
            R=img.subimg(i,(W+1),0,(w-W),h)
            return (D,R)
        else:
            c+=1
    return img.null()
