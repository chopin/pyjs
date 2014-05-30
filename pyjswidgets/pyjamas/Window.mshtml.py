#from __pyjamas__ import get_main_frame, JS, doc, wnd

def getClientHeight():
    return doc().body.clientHeight

def getClientWidth():
    return doc().body.clientWidth

#It is not called. WHY???
#def resize(width, height):
#    mainWnd=get_main_frame()
#    mainWnd.resize(width, height)

