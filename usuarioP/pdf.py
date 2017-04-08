__author__ = 'liscano PDF'
#-*- coding: utf-8 -*-
'''from reportlab.pdfgen import canvas
def hello(c):
    c.drawString(50, 50,"<h1>hola jose P</h1>")
c=canvas.Canvas("hellop.pdf")
hello(c)
c.showPage()
c.save()
'''
import ho.pisa as pisa

def helloWorld():
    filename = __file__ + ".pdf"
    pdf = pisa.CreatePDF("Hello <strong>World</strong>",
                         file(filename, "wb")
                         )
    if not pdf.err:
        pisa.startViewer(filename)
        if __name__=="__main__":
            pisa.showLogging()
helloWorld()
