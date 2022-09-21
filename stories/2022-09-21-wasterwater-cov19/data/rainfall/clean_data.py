import re 
from glob import glob 
regex = r"([\s]{2,})"
subst = ","
files = glob("./*.txt")

for file in files:
    with open(file) as f:
        data = f.readlines()
    # some data has extra lines of information before data
    # so we need to find it... 
    crop = 0
    for l in data:
        if 'year' not in l:
            crop=crop+1
        else:
            break
    for idx, ln in enumerate(data[crop:]):
        data[crop+idx] =  re.sub(regex, subst, ln, 0)       
    nn = f"{file.replace('txt','cleaned_.csv')}"
    with open(nn, 'w') as nf:
        nf.writelines(data[crop:])
