# -*- encoding: utf-8 -*-

import imgio
import img

def load_patterns(prefix):
    patlst=[]
    for x in range(10):
        arxiu = f"{prefix}_{x}.jpeg"
        num=imgio.read_bn(arxiu)
        patlst+=[num]
    return patlst

def match(i,patlst):
    x=0
    m=0
    num=0
    while x<len(patlst):
        patro=patlst[x]
        m_2=sim(i,patro)
        if m_2>m:
            m=m_2
            num=x
        x+=1
    return num

def sim(A,B):
    """
    >>> sim(('1',[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,255,255,0]]),('1',[[255,255],[255,255],[255,255],[255,255]]))
    2
    """
    matriu_A=img.matrix(A)
    matriu_B=img.matrix(B)
    wa=img.get_w(A)
    wb=img.get_w(B)
    h=img.get_h(A)
    sim_f=0
    cnt=0
    if wa>=wb:
        while cnt<=(wa-wb):
            sim=0
            x=0
            while x<h:
                y=0
                while y<wb:
                    if matriu_A[x][y+cnt]==matriu_B[x][y]:
                        sim+=1
                    y+=1
                x+=1
            if sim>sim_f:
                sim_f=sim
            cnt+=1

    else:
        while cnt<=(wb-wa):
            sim=0
            x=0
            while x<h:
                y=0
                while y<wa:
                    if matriu_B[x][y+cnt]==matriu_A[x][y]:
                        sim+=1
                    y+=1
                x+=1
            if sim>sim_f:
                sim_f=sim
            cnt+=1

    return sim_f


