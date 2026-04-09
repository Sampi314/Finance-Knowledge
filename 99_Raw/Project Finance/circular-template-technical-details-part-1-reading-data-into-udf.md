# Reading Data into UDF

**Source:** https://edbodmer.com/circular-template-technical-details-part-1-reading-data-into-udf

---

This page describes how to construct user defined functions in excel that require reading in a lot of different types of data. When constructing a UDF, attempting to read in separate variables can be very clumsy and make the UDF’s unusable. The discussion below demonstrates how you can make the process of reading a lot of data into a UDF reasonable through reading in a contiguous table in an excel sheet. Using this process, you can also read in the data in a flexible manner where some of the data is scalars and some of the data is in vectors. (A scalar is a single number and a vector is a set of numbers in a row).

To demonstrate the process of reading in data, I use the case of a UDF that solves the difficult problem of computing sculpted debt repayment with a non-constant DSCR when the debt to capital, the minimum DSCR and the maximum debt life is defined. In solving this problem, you need some kind of optimization that adjusts the DSCR over time and reduces that DSCR to a minimum DSCR by the end of the life of the project. This process requires a lot of input data and I have developed a quasi template function to do this. A file that contains this method for reading in data is available for download by clicking on the button below.

**[Excel Spreadsheet with Comprehensive Structuring Example - Single and Multiple Issues and Shaped DSCR](https://edbodmer.com/wp-content/uploads/2025/07/Webinar-Structuring-with-Multiple-Debt-Issues-V3.xlsm)
**

Example of Using Table Method Read Data into UDF
------------------------------------------------

The screenshot below illustrates a case where you can read a lot of data into a UDF.  Note in the table there is text as well as data; there are some variables that are TRUE/FALSE boolean variables and other variables that are regular numbers; and, there are some variables (at the bottom) that are vectors and others that are scalars.

![](https://edbodmer.com/wp-content/uploads/2018/05/Reading-UDF-1.jpg)

When you operate a UDF with a table like this, you can apply the following steps:

1.  Copy the UDF function into your program using ALT, F8 technique, where you copy the code from one file and insert it into another program.
2.  Select the area that will b used for the output of the table as you would for other array functions like the TRANSPOSE function or the FREQUENCY function.  If you already have entered the function, then use the SHIFT, CNTL, –> and the SHIFT, CNTL down arrow.
3.  Enter the function name that uses the read table function and select the area with entire rows as shown in the screenshot below.
4.  Press SHIFT, CNTL, ENTER

I hope as you get used to this, you can do it in a matter of seconds.

![](https://edbodmer.com/wp-content/uploads/2018/05/Read-UDF-2.jpg)

VBA Code for Reading a Data Table into a UDF
--------------------------------------------

Putting a whole lot of data from separate places in an excel model can make the UDF process very clumsy.  It may be a good idea to see if the existing code works for you. I suggest that you go to the data in the sheet that is available for downloading above.  Then copy the data to a new sheet (without any of the VBA Code).  Then copy the code below and see if you can read the data.  This is a big step because after reading the data and creating an output matrix, the rest is replicating equations in your financial model.

.

' The function that will use the data

Function optimise(read\_table) As Variant

read\_table\_result = read\_table\_data(read\_table)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3639&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13108&rand=0.9454395958898761)