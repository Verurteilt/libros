from gui5 import HelloButton

class MyButton(HelloButton):        # subclass HelloButton
    def callback(self):             # redefine press-handler method
        print "Ignoring press!..."

if __name__ == '__main__':
    MyButton(None, text='Hello subclass world').mainloop( )

