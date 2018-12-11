# -*- encoding: utf-8 -*-

import sys
import img
import imgio
import discret
import match
import transf
import split


matricula=imgio.read_rgb(sys.argv[2])
#imgio.show(matricula)
matricula_bn=discret.rgb_to_bn(matricula)
#imgio.show(matricula_bn)
patterns=match.load_patterns(sys.argv[1])
matricula_bn=transf.htrim(matricula_bn)
H=img.get_h(patterns[0])
matricula_final=transf.scale(matricula_bn,H)
imgio.show(matricula_final)
matricula_final=transf.vtrim(matricula_final)
num_f=""
while not img.is_null(matricula_final):
    digit=split.split_digit(matricula_final)
    digit_final=transf.vtrim(digit[0])
    #imgio.show(digit_final)
    num_f+=str(match.match(digit_final,patterns))
    matricula_final=transf.vtrim(digit[1])
print
print "The license plate number is:",num_f
print
