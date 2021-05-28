# the Tkinter filedialog for saving file
# tkfd.asksaveasfile(**options) returns file handle to save to

try:
    # Python2
    import Tkinter as tk
    import tkFileDialog as tkfd
except ImportError:
    # Python3
    import tkinter as tk
    import tkinter.filedialog as tkfd

mask = [
    ("Text files","*.txt"),
    ("Python files","*.py *.pyw"),
    ("All files","*.*")]

# if the filename does not have extension
# it will add the specified defaultextension
file_save = "test77"
fout = tkfd.asksaveasfile(
    title="testing defaultextension='.txt'",
    initialdir="C:/Python27/Atest27/Bull",
    initialfile=file_save,
    defaultextension=".txt",
    filetypes=mask)

# test write a file
data = """\
1
2
3
4
"""
fout.write(data)
fout.close()