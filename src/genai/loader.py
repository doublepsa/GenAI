import os
from pypdf import PdfReader

def load_text(fname,raw=True):
    with open(fname,'r') as f:
        text=f.read()
    if raw:
        return text.lower()
    out=text.lower().split()
    return out

def load_pdf(fname,raw=True):
    reader = PdfReader(fname)
    text=""
    images=[]
    for page in reader.pages:
        text+=(page.extract_text() or "") + " "
        for i, image_file_object in enumerate(page.images):
            images.append(image_file_object)
            # image_file_object.image.save(file_name)
    if raw:
        return text.lower(),images
    return text.lower().split(),images

def load_gen(fname):
    out={}
    with open(fname,'r') as f:
        t=f.readlines()
        for l in t[1:]:
            rank,word,count,percent,cumulative=l.split()
            percent=float(percent[:-1])
            out[word]=percent
    return out
