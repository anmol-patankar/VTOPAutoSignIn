from PIL import Image
from Levenshtein import distance as levdist
import time
import json
from difflib import SequenceMatcher
im=Image.open("captcha_clean.png")
rgbimg = Image.new("RGBA", im.size)
rgbimg.paste(im)
rgbimg.save('captcha_clean.png')
im=Image.open("captcha_clean.png")
cwidth,cheight=im.size
top=0
bottom=cheight
captchaAns=""
count=1
left=0
right=cwidth/6
with open('captcha_bitmap.txt') as f:
    data=f.read()
alphanum=json.loads(data)
def checkVal(stri):
    temp=-1
    currentmaxsim=2000
    for key in alphanum:
        if(levdist(stri,alphanum[key])<currentmaxsim):
            currentmaxsim=levdist(stri,alphanum[key])
            temp=key
    return temp
def Extract(lst):
    return [item[0] for item in lst]
while right<=cwidth:
    
    bitmap_string=""
    cropthing=(left, top+12, right, bottom-1)
    cr_im=im.crop(cropthing)
    pix_val = list(cr_im.getdata())
    pix_val=Extract(pix_val)
    for i in range(len(pix_val)):
        if pix_val[i]==0:
            bitmap_string+="0"
        else:
            bitmap_string+="1"
    captchaAns+=str(checkVal(bitmap_string))
    left=right
    right+=cwidth/6
def captchaSolve():
    return captchaAns


