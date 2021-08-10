# Write in 2018 after company remove pdf merge/split software.
# Split function can split a pdf file into pdf files for each page by page number.
# Merge function can merge pdf files in the same folder alphabetically into one pdf file.

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import tkinter
import tkinter.filedialog
import os

# Split pdf code
def split_pdf():
    fn=tkinter.filedialog.askopenfilename(title='Choose a file', filetypes=[('pdf','.pdf')])    # use tkinter to choose file

    fn_name=fn[len(fn)-fn[::-1].find('/')::]    # get file name without path information
    fn_loc=fn[0:len(fn)-fn[::-1].find('/')] + "split_" + fn_name[:(len(fn_name)-4)] + '/'   #new folder name with path information

    # make directory if not exist
    try:
        os.stat(fn_loc)
    except:
        os.mkdir(fn_loc)


    infile = PdfFileReader(fn, 'rb')

    i=1
    for i in range(infile.getNumPages()):
        p = infile.getPage(i)
        outfile = PdfFileWriter()
        outfile.addPage(p)
        outfilename='page-%03d.pdf' % i
        completename=os.path.join(fn_loc,outfilename) 
        with open(completename, 'wb') as f:
            outfile.write(f)

def merge_pdf():
    merger = PdfFileMerger()
    fd = tkinter.filedialog.askdirectory()
    files = [x for x in os.listdir(fd) if x.endswith('.pdf')]
    for fname in sorted(files):
        merger.append(PdfFileReader(open(os.path.join(fd, fname), 'rb')))

    merger.write(fd + "_merge.pdf")

top = tkinter.Tk()
Button_split = tkinter.Button(top,text ="Split PDF", command = split_pdf)
Button_merge = tkinter.Button(top,text ="Merge PDF", command = merge_pdf)
Button_split.pack()
Button_merge.pack()
top.mainloop()

exit()