# Using Python with Excel – Part Three - Lentran Modelling Solutions

**Source:** http://www.lentransolutions.com/using-python-with-excel-part-3

---

Using Python with Excel – Part Three
====================================

May 5, 2019[No Comments](http://www.lentransolutions.com/using-python-with-excel-part-3#respond)
[Theo West](http://www.lentransolutions.com/author/theowest/)

### Using Python with Excel for Powerful Financial Modelling Solutions

#### Integrating Python with Excel

This tutorial will provide an overview on how to integrate Python within Excel, such that Excel remains the front end interface for the user but predominantly the code is written in Python. This allows users to create extremely powerful models without sacrificing the popular and familiar Excel front-end.

#### Implementing Python’s programming power in Excel models

Thanks to Python library ‘**xlwings**‘, Excel and Python applications can interact directly with each other. This allows you to retain an Excel interface while utilising Python’s powerful technology in the background for performing **data analysis**.

Xlwings allows interaction or instruction between Excel and Python in both directions. For example, the following interactions are possible:

1.  Control an Excel workbook through code from within Python
2.  Utilise Excel VBA to call specific Python scripts

#### Data analysis with Python

**Pandas** is an incredible useful Python library when it comes to analysing and manipulating data. It also allows reading and writing of data to and from Excel. In combination with xlwings we can create an interactive environment, which utilises Python for data collections and manipulations and Excel for reporting results.

Below we will illustrate an example of how a user can combine Excel, Python and pandas to build an **advanced data analysis tool**. This tool will retrieve information from an external database, manipulate the data and present it in the familiar Excel spreadsheet format.

#### Interactive data analysis with Excel and Python

The graph below illustrates how our data analysis tool will be structured and how Excel/VBA, Python/pandas and the database will interact with each other:

![](<Base64-Image-Removed>)

The Excel spreadsheet model will be the front-end user interface. Inputs for performing the data analysis, such as the location of the data set and operations to be performed on the data will be stored there. The Excel model will directly interact with Python through the ‘xlwings’ bridge. Python, especially the **pandas** library, will perform all the heavy lifting in the background. Python will interact with both the Excel model to acquire the user-inputs and the database file. Based on the user’s instructions the database file will be read and manipulated. After Python has completed the procedure it will write the finalised data back into the main Excel spreadsheet model.

At first look this sounds relatively complex or convoluted and you might well wonder why the reading and manipulating of data is not done directly within the Excel model and in doing so make the middle step obsolete. The reason is that while for many applications VBA alone is sufficient, on the other hand for complex data analysis techniques such as machine learning, or big data sets with billions of data points VBA will either be too slow or simply unable to deal with the task at hand. In these cases the use of advanced programming languages such as Python is an appropriate and powerful solution.

#### A practical working example

The next tutorial in this series provides a practical working example of the above. We will provide Excel interface files, the necessary VBA code and step by step instruction on how to get Python and xlwings installed and active.

[](javascript:void(0) "Share this")
[](javascript:void(0) "Tweet this")
[](javascript:void(0) "Share this")
[](javascript:void(0) "Share this")
[](javascript:void(0) "Pin this")

[Previous post Using Python with Excel – Part Two](http://www.lentransolutions.com/using-python-with-excel-part-2/)
 [Next post Using Python with Excel – Part Four](http://www.lentransolutions.com/using-python-with-excel-part-4/)

### Leave a Reply [Cancel reply](http://www.lentransolutions.com/using-python-with-excel-part-3#respond)

Your email address will not be published. Required fields are marked \*

  

[](javascript:void(0);)
[](http://www.lentransolutions.com/using-python-with-excel-part-3# "Back to top")