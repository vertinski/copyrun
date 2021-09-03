
'''
This file is part of CopyRun.
    CopyRun is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    CopyRun is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with CopyRun.  If not, see <https://www.gnu.org/licenses/>.
'''


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


Information:

CopyRun is written by Vertinski
vertinski@inbox.lv

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




def toggle_active (tog_butt):
    global app_active

    if app_active == True:
        app_active = False
        tog_butt.config (image=off_image)    # change toggle button image to non-active
        lbl2.config (fg='grey')
        lbl3.config (fg='grey')

    else:
        app_active = True
        tog_butt.config (image=on_image)    # change toggle button image to active
        lbl2.config (fg='red')
        lbl3.config (fg='red')

    #return app_active     #return app status boolean



tog_stat = 'Active'
app_active = True



def main():

    app = tk.Tk()     # create Tkinter instance
    app.title ("CopyRun")
    app.geometry ("200x140")
    app.configure(bg='black')
    app.call ('wm', 'attributes', '.', '-topmost', True)


    # add a warning label
    #lbl1 = tk.Label (app, text='CopyRun', font=('Arial Bold', 16), fg='red', bg='black')
    #lbl1.pack()
    lbl0 = tk.Label (app, text='       ', font=('Arial Bold', 8), fg='red', bg='black')
    lbl0.pack()

    global lbl2, lbl3

    lbl2 = tk.Label (app, text='APP IS ACTIVE!!', font=('Arial Bold', 16), fg='red', bg='black')
    lbl2.pack()

    lbl3 = tk.Label (app, text='Copy Python code ONLY', font=('Arial Bold', 8), fg='red', bg='black')
    lbl3.pack()

    lbl4 = tk.Label (app, text='       ', font=('Arial Bold', 8), fg='red', bg='black')
    lbl4.pack()

    global on_image, off_image

    on_image = tk.PhotoImage(file='assets/toggle_button_green.png')
    off_image = tk.PhotoImage(file='assets/toggle_button_grey.png')

    #tog_image = on_image

    tog_butt = tk.Button (app, bg='black', activebackground='black', image=on_image,
                          command= lambda:toggle_active(tog_butt), highlightthickness=0, borderwidth=0)
    tog_butt.pack (padx=10, side='left')


    # add exit button
    exit_image= tk.PhotoImage(file='assets/exit_button.png')

    exit_btn = tk.Button (app, bg='black', activebackground='black', image=exit_image,
                          command=app.destroy, highlightthickness=0, borderwidth=0)
    #exit_btn['activebackground'] = 'black'
    exit_btn.pack (padx = 10, side='right')


    app.clipboard_append ('zzzzzzzzz')   # add string into clipboard to avoid errors

    old_clip = app.clipboard_get()   # previously copied buffer for comparison
    clip_text = old_clip             # both filled with current clipboard

    #app.clipboard_clear()        # THIS SOMEHOW FUCKS UP TKinter window :(
    #app.clipboard_append ('')    # clear existing clipboard
    #app.update()

    while True:
        if app_active == True:
            print ('CopyRun app is active and running.........')
            clip_text = app.clipboard_get()    # get clipboard text
            time.sleep (0.2)

            if clip_text != old_clip:           # if new text is copied in clipboard
                with open ('testscript.py', 'w') as f:    # save to file and run it
                    f.write (clip_text)
                p = subprocess.run (['python3', 'testscript.py'])
                old_clip = clip_text

        else:
            print ('CopyRun app is paused.........')
            old_clip = app.clipboard_get()
            time.sleep (0.2)

        app.update()



if __name__ == "__main__":

    try:
        main()

    except:
        old_clip = ''      # clear the clipboard buffer
        clip_text = ''
        print('Exiting!')

