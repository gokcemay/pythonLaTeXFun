

import os, re 

Line = '''\includepdf[pages=-, addtotoc={1,section,0, FileName ,chap:samplepdfone}]{FileLoc}'''   # LaTeX code I want to generate
RE = re.compile(u'[şıöğçüİÜŞÇ]', re.UNICODE) #to Remove Turkish char from file 
with open("output.txt", "w") as a: 
    for path, subdirs, files in os.walk(r'd:/temp/TR'):  #get file names from subfolders
       files = [ fi for fi in files if  fi.endswith(".pdf")] #get only pdf files
       for filename in files:
         f = os.path.join(path, filename) #get path
         f = re.sub('d:/temp/TR\\\\', '', f) #remove d:/temp/TR\\
         f_n = f   #f_n is for file names 
         f = re.sub('.pdf','',f_n) #remove .pdf
         f = re.sub('[^A-Za-z0-9]+', '_', f) #replace special chars with _
         f = f + '.pdf' #add .pdf
         f= RE.sub('_',f) #remove Turkish Chars
         f=re.sub(r'\\','/',f) #replace \ with /
         for x in range(0, 8): #Remove subfolders from file name they were Yariyil_1 to 8
            f_n=re.sub('Yariyil_'+str(x)+r'_tr\\','',f_n)
         f_n = re.sub('.pdf','',f_n) #remove PDF
         Line2= re.sub('FileName',f_n,Line) #Put f_n to FileName in LaTeX line
         Line2= re.sub('FileLoc',f,Line2) #Put f to FileLoc in LaTeX line
         a.write(Line2+ os.linesep) #write to text file
        

