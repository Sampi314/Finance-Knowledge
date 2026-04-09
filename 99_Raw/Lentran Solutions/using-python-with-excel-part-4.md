# Using Python with Excel – Part Four - Lentran Modelling Solutions

**Source:** http://www.lentransolutions.com/using-python-with-excel-part-4

---

Using Python with Excel – Part Four
===================================

May 9, 2019[No Comments](http://www.lentransolutions.com/using-python-with-excel-part-4#respond)
[Theo West](http://www.lentransolutions.com/author/theowest/)

### Excel and Python for Financial Modelling: Installation Guide

#### Building powerful models with Microsoft Excel and Python

This article provides an installation guide for running Python through Excel. This is achieved via **xlwings**, which is a Python library and Excel add-in. It is assumed that Excel and Python are already installed on your computer. For readers that do not have Python yet we have provided a link, which guides the user through the installation process.

#### Python installation guide

First Python has to be installed. We recommend installing Anaconda, which is a free and open-source distribution already containing all packages for mathematics, science, engineering and data science.

**Datacamp** has an excellent tutorial on how to install the Python – Anaconda package manager on Microsoft Windows – the tutorial can be found [here](https://www.datacamp.com/community/tutorials/installing-anaconda-windows)
.

Second, install Python packages **pandas** and **xlwings**. To do this open the Anaconda prompt – make sure to run the prompt as an administrator. The code to install them is simple – in the prompt type:

**pandas:**

|     |     |
| --- | --- |
| 1   | `conda install pandas` |

**xlwings:**

|     |     |
| --- | --- |
| 1   | `conda install xlwings` |

This is all that is required to install the pandas and xlwings packages in Python.

#### VBA installation guide

The last step is for the xlwings add-in to be added to Excel. Open the command prompt (make sure to run this as an administrator) and type:

|     |     |
| --- | --- |
| 1   | `xlwings addin install` |

After opening Excel, the xlwings add-in will be shown on the Excel ribbon as per below:

![](http://www.lentransolutions.com/wp-content/uploads/2019/03/xlwings-ribbon.jpg)

The official xlwings add-in installation guide can be found [here](https://docs.xlwings.org/en/stable/addin.html#xlwings-addin)
.

### Interactive data analysis with Excel and Python

#### Getting started

As a first test we code a simple script that copies the content from one cell into another. We want this to be performed after clicking the “Test Connection” button in the model that can be downloaded at the end of this tutorial.

The code for copying is written in Python, however the user will only interact with Excel. The communication between Excel and Python is achieved through xlwings.

We recommend writing the Python code in **Spyder**, a platform that is included in Anaconda.

The Python script is shown below:

|     |     |
| --- | --- |
| 1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7<br><br>8<br><br>9<br><br>10<br><br>11<br><br>12<br><br>13<br><br>14<br><br>15<br><br>16<br><br>17 | `import` `pandas as pd`<br><br>`import` `xlwings as xw`<br><br>`#Function to copy from one cell to another`<br><br>`def` `TestConnectionPython():`<br><br>    `# Make a connection to the calling Excel file`<br><br>    `wb` `=` `xw.Book.caller()`<br><br>    `# Store the main sheet location`<br><br>    `MainSheet` `=` `wb.sheets[``'Main'``]`<br><br>    `# Store the content of the named cell 'Copy_Test'`<br><br>    `CopyTestValue` `=` `MainSheet.``range``(``'Copy_Test'``).value`<br><br>    `# Output the data just to make sure it all works`<br><br>    `MainSheet.``range``(``'Paste_Test'``).value` `=` `CopyTestValue` |

Most of the Python code utilises the ‘xlwings’ library. Users familiar with VBA will notice a clear similarity between VBA and xlwings Python code. To run the above Python script from within Excel, VBA code is required. The VBA code makes use of the ‘xlwings’ add-in to control Python. For most Excel-Python application the following code structure is suffice:

`RunPython (import PYTHONFILE; PYTHONFILE.PYTHONFUNCTION())` 

**RunPython** is a xlwings function. It imports a Python script and calls a specific function from this script. To call Python function ‘TestConnectionPython’ (which we coded before) the following VBA sub can be used:

|     |     |
| --- | --- |
| 1<br><br>2<br><br>3 | `Sub` `TestConnectionVBA()`<br><br>    `RunPython (import TestConnection; TestConnection.TestConnectionPython())`<br><br>`End` `Sub` |

What the code does is first import the Python script ‘TestConnection.py’. Subsequently, the ‘TestConnection.py’ function calls ‘TestConnectionPython’. This Python function will access the Excel spreadsheet and copies a value from one cell to another.

At the end of this tutorial an Excel sample model and Python script can be downloaded. The Python script will download as a .txt file. Rename it to TestConnection.py and make sure that both the Excel model and the Python script are saved in the same folder, otherwise there might be complications.

#### Next steps

This concludes the first example on utilising Python in conjunction with Excel through the xlwings bridge. In the next article we will illustrate how powerful Python is when it comes to reading, analysing and manipulating vast amounts of data. The resulting dataset will be written back into the master Excel model.

[DOWNLOAD EXCEL MODEL](http://www.lentransolutions.com/wp-content/uploads/2019/05/9_LMS-Tutorial_Excel-Python-Connection-Test.xlsm)

[DOWNLOAD PYTHON SCRIPT](http://www.lentransolutions.com/wp-content/uploads/2019/03/TestConnection.txt)

[](javascript:void(0) "Share this")
[](javascript:void(0) "Tweet this")
[](javascript:void(0) "Share this")
[](javascript:void(0) "Share this")
[](javascript:void(0) "Pin this")

[Previous post Using Python with Excel – Part Three](http://www.lentransolutions.com/using-python-with-excel-part-3/)

### Leave a Reply [Cancel reply](http://www.lentransolutions.com/using-python-with-excel-part-4#respond)

Your email address will not be published. Required fields are marked \*

  

[](javascript:void(0);)
[](http://www.lentransolutions.com/using-python-with-excel-part-4# "Back to top")