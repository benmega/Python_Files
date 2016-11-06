from tkinter.filedialog import askdirectory
import os
from html import escape

def usermakeskeletoncopy():
<<<<<<< HEAD
    from tkinter.filedialog import askdirectory
=======
>>>>>>> origin/master
    print('Please select a folder of which to make a skeleton copy.')
    origdir = askdirectory()
    print('Please select a location to save this copy.')
    skeletondir = askdirectory()
    inputname = input('And what would you like it to be named?')
<<<<<<< HEAD
        #This fails if user input impossible folder name
=======
    #Fails if user requests impossible folder name
>>>>>>> origin/master
    skeletonname = inputname.strip()
    try:
        makefolderskeletoncopy(origdir, skeletondir, skeletonname)
        result = 'Operation succeeded ' + skeletondir + '/' + skeletonname + ' created'
    except:
        result = 'Operation failed to create ' + skeletondir + '/' + skeletonname + '. Please confirm this folder does not already exist'
    return result

def makefolderskeletoncopy(origdir, skeletondir, skeletonname):
<<<<<<< HEAD
    import os
    from html import escape
=======
>>>>>>> origin/master
    dir2 = escape(origdir)
    os.chdir(dir2)
    subfolders = next(os.walk('.'))[1]
    for x in subfolders:
        os.makedirs(skeletondir + '\\' + skeletonname + '\\' + str(x))
