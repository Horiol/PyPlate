# -*- encoding: utf-8 -*-
 
def null():
     """
     retorna una imatge nula
     >>> null()
     ('NULL', None)
     """
     return ('NULL', None)
 
def is_null(i):
     """
     retorna true si i es una imatge nula
     >>> is_null(('NULL', None))
     True
     
     """
     return i == null()
def white_rgb(w,h):
     """
     Retorna una imatge en format RGB
     >>> white_rgb(2,2)
     ('RGB', [[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
     >>> white_rgb(1,1)
     ('RGB', [[(255, 255, 255)]])
     """
     i=0
     l=[]
     while i<(h):
         j=0
         l_2=[]
         while j<(w):
             l_2+=[(255,255,255)]
             j+=1
         l+=[l_2]
         i+=1
     return ('RGB',l)

def white_grey(w,h):
     """
     retorna una imatge en blanc en escala de grisos
     >>> white_grey(2,2)
     ('L', [[255, 255], [255, 255]])
     >>> white_grey(1,1)
     ('L', [[255]])
     """
     i=0
     l=[]
     while i<(h):
         j=0
         l_2=[]
         while j<(w):
             l_2+=[(255)]
             j+=1
         l+=[l_2]
         i+=1
     return ('L',l)

def white_bw(w,h):
     """
     retorna una imatge en blanc en el format blanc i negre
     >>> white_bw(3,3)
     ('1', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
     >>> white_bw(1,1)
     ('1', [[255]])
     """
     i=0
     l=[]
     while i<(h):
         j=0
         l_2=[]
         while j<(w):
             l_2+=[(255)]
             j+=1
         l+=[l_2]
         i+=1
     return ('1',l)

def format1(i):
     """
     Donada una imatge en retorna el format
     >>> format1(('RGB',[(234,9,8),(234,235,123),(255,123,2)]))
     'RGB'
     >>> format1(('L', [[234, 123, 123]]))
     'L'
     """
     return i[0]

def matrix(i):
     """
     Donada una imatge img retorna la matriu de pixels corresponent
     >>> matrix(('1',[255,0,255]))
     [255, 0, 255]
     """
     return i[1]

def img(matrix,model='DISCOVER'):
     """
	Donada una matriu de pixels, detecta si es tracta de una imatge de rgb, escala de grisos o blanc i negre i creara una imatge nova.
	>>> img([(255,0,0),(255,255,255),(255,0,255)], model='DISCOVER')
	('1', [(255, 0, 0), (255, 255, 255), (255, 0, 255)])
        >>> img([(233, 0 ,0)], model='DISCOVER')
        ('L', [(233, 0, 0)])
	"""
     tipo=""
     if model != 'DISCOVER':
          return (model, matrix)
     t=()
     for element in matrix:
          for pixel in element:
               if type(pixel)==type(t):
                    return('RGB',matrix)
               elif pixel>=1 and pixel<=254:
                    return ('L',matrix)
               else:
                    tipo='1'
     return (tipo,matrix)
     
def get_w(i):
     """
     Retorna la amplada de la imatge
     >>> get_w(('1',[[255,0],[0,255]]))
     2
     >>> get_w(('RGB',[[(255,234,234)]]))
     1
     """
     a=matrix(i)
     return len(a[0])

def get_h(i):
     """
     Retorna la alçada de la imatge
     >>> get_h(('1',[[255,0],[255,0],[255,0]]))
     3
     >>> get_h(('L',[[255,0],[255,0]]))
     2
     """
     return len(matrix(i))

def subimg(i,ow,oh,w,h):
     """
    retorna una sub-imatge img que té l'origen a les coordenades (ow,oh) i té mides w i h
    
    >>> subimg(('1',[[255,255,0],[0,0,255],[0,0,255]]),0,0,1,1)
    ('1', [[255]])
    >>> subimg(('RGB', [[(234, 123, 123)]]), 0,0,1,1)
    ('RGB', [[(234, 123, 123)]])
    """
     matriu=matrix(i)
     subimg=[]
     for f, fila in enumerate(matriu):
          f_n = [
              columna for c, columna in enumerate(fila)
              if f >= oh and f < oh + h and c >= ow and c < ow + w
          ]
          if f>=oh and f<oh+h:
              subimg+=[f_n]
     return (i[0],subimg)
