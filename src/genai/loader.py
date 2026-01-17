import os
from pypdf import PdfReader

# loaders for different file types

def load_text(fname,raw=True):
    """ loads text file, returns either raw text or list of words 
    Args:
        fname: The name of the file to load.
        raw: If True, returns the raw text; if False, returns a list of words.
    """
    with open(fname,'r') as f:
        text=f.read()
    if raw:
        return text.lower()
    out=text.lower().split()
    return out

def load_pdf(fname,raw=True):
    """ loads pdf file, returns either raw text or list of words and a list ofimages
    Args:
        fname: The name of the PDF file to load.
        raw: If True, returns the raw text; if False, returns a list of words.
    """
    reader = PdfReader(fname)
    text=""
    images=[]

    # extract text and images
    for page in reader.pages:
        text+=(page.extract_text() or "") + " "
        for i, image_file_object in enumerate(page.images):
            images.append(image_file_object)
            # image_file_object.image.save(file_name)
    if raw:
        return text.lower(),images
    return text.lower().split(),images

def load_gen(fname):
    """ loads a .gen file, returns a dict of word:percent
    Args:
        fname: The name of the .gen file to load.
    """
    out={}

    # extract word frequencies
    with open(fname,'r') as f:
        t=f.readlines()
        # skip header
        for l in t[1:]:
            rank,word,count,percent,cumulative=l.split()
            # remove % sign
            percent=float(percent[:-1])
            out[word]=percent
    return out