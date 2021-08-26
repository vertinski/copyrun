

'''
WARNING!!
USE AT YOUR OWN RISK! NO GUARANTIES IF ANYTHING GETS BROKEN.
DO NOT COPY ANYTHING EXCEPT PYTHON CODE YOU HAVE REVIEWED!!
FOR EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY.

This app executes Python code after it is copied in clipboard.
It saves the contents of the clipboard in file "testscript.py" and executes it.
It ONLY executes content which is different from previously copied contents.
The CopyRun app waits for the launched code to exit and then continues to work.
At all times there should be a warning window visible, which indicates
that this app is active and running. It also writes status messages in terminal.

This warning is a part of CopyRun app and should be included in code at all times!

'''


import tkinter as tk
import subprocess
import time






warning = """WARNING!!
USE AT YOUR OWN RISK! NO GUARANTIES IF ANYTHING GETS BROKEN.
DO NOT COPY ANYTHING EXCEPT PYTHON CODE YOU HAVE REVIEWED!!
FOR EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY.

This app executes Python code after it is copied in clipboard.
It saves the contents of the clipboard in file "testscript.py" and executes it.
It ONLY executes content which is different from previously copied contents.
The CopyRun app waits for the launched code to exit and then continues to work.
At all times there should be a warning window visible, which indicates
that this app is active and running. It also writes status messages in terminal.

This warning is a part of CopyRun app and should be included in code at all times!"""

print()
print (warning)
print()



def main():

    app = tk.Tk()     # create Tkinter instance
    app.title ("CopyRun")
    app.geometry ("200x120")
    app.configure(bg='black')
    app.call ('wm', 'attributes', '.', '-topmost', True)


    # add a warning label
    #lbl1 = tk.Label (app, text='CopyRun', font=('Arial Bold', 16), fg='red', bg='black')
    #lbl1.pack()
    lbl0 = tk.Label (app, text='       ', font=('Arial Bold', 8), fg='red', bg='black')
    lbl0.pack()

    lbl2 = tk.Label (app, text='APP IS ACTIVE!!', font=('Arial Bold', 16), fg='red', bg='black')
    lbl2.pack()

    lbl3 = tk.Label (app, text='Copy Python code ONLY', font=('Arial Bold', 8), fg='red', bg='black')
    lbl3.pack()

    lbl4 = tk.Label (app, text='       ', font=('Arial Bold', 8), fg='red', bg='black')
    lbl4.pack()

    # add exit button
    btn = tk.Button (app, text='Exit', command=app.destroy)
    btn.pack()


    old_clip = app.clipboard_get()   # previously copied buffer for comparison
    clip_text = old_clip             # both filled with current clipboard

    #app.clipboard_clear()        # THIS SOMEHOW FUCKS UP TKinter window :(
    #app.clipboard_append ('')    # clear existing clipboard
    #app.update()


    while True:
        print ('CopyRun app is active and running.........')

        clip_text = app.clipboard_get()    # get clipboard text
        time.sleep (0.5)

        if clip_text != old_clip:           # if new text is copied in clipboard
            with open ('testscript.py', 'w') as f:    # save to file and run it
                f.write (clip_text)
            p = subprocess.run (['python3', 'testscript.py'])
            old_clip = clip_text



if __name__ == "__main__":

    try:
        main()

    except:
        old_clip = ''      # clear the clipboard buffer
        clip_text = ''
        print('Exiting!')


