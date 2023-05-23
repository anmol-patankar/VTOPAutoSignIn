from PIL import Image
from Levenshtein import distance as levdist
import time
import json
from difflib import SequenceMatcher
captchaAns=""
count=1
left=0
top=0

def ImagePreprocess():
    global cwidth,bottom,rgbimg
    im=Image.open("captcha.png").convert("L")
    pixel_matrix = im.load()
    for col in range(0, im.height):
        for row in range(0, im.width):
            if pixel_matrix[row, col] != 0:
                pixel_matrix[row, col] = 255
    rgbimg = Image.new("RGBA", im.size)
    rgbimg.paste(im)
    rgbimg.save('captcha_clean.png')
    cwidth,bottom=rgbimg.size
    



def LoadBitMap():
    global alphanum
    with open('captcha_bitmap.txt') as f:
        data=f.read()
    alphanum=json.loads(data)
def EvaluateChar(stri):
    temp=-1
    currentmaxsim=2000
    for key in alphanum:
        if(levdist(stri,alphanum[key])<currentmaxsim):
            currentmaxsim=levdist(stri,alphanum[key])
            temp=key
    return temp
def FlattenExtract(lst):
    return [item[0] for item in lst]
def CaptchaSolver():
    global captchaAns
    right=cwidth/6
    left=0
    while right<=cwidth:
        bitmap_string=""
        cropthing=(left, top+12, right, bottom-1)
        cr_im=rgbimg.crop(cropthing)
        pix_val = list(cr_im.getdata())
        pix_val=FlattenExtract(pix_val)
        for i in range(len(pix_val)):
            if pix_val[i]==0:
                bitmap_string+="0"
            else:
                bitmap_string+="1"
        captchaAns+=str(EvaluateChar(bitmap_string))
        left=right
        right+=cwidth/6

ImagePreprocess()
LoadBitMap()
CaptchaSolver()



