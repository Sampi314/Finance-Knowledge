# UDF Functions for Financial Models

**Source:** https://edbodmer.com/udf-functions-for-financial-models

---

I made a set of pages that are sub menus to this page that describe certain UDF functions that can be helpful in different kinds of financial models. In the associated child pages to this page you can see how to make a series of user-defined functions that fix problems with excel. I start with some relatively simple user-defined functions including MAXIF, MINIF, SUMNA, XMIRR function and a PAYBACK function. I then move to more tricky functions for resolving the vintage depreciation problem and developing dynamic goal seeks that do not require you to stop excel.  I have included excel files along with the copied code.

Fixing Problems with Excel
--------------------------

My uncle Walter is a famous statistician and and geneticist.  He was the last PHD student of R.A. Fischer, the father of statistics. Walter told me that I am an idiot for using excel instead of using something more sophisticated like matlab.  If you could not fix excel with UDF functions, he would be correct.  But through using VBA user-defined functions and fixing excel, you can dramatically change the power of the program (a good example of this is the LOOKUP INTERPOLATE function that is described in this section of the website).  With user defined functions, you can take back control of of excel; solve circular references; optimize equations; create functions for computing volatility etc.

General Principles of User-Defined Functions
--------------------------------------------

To begin the process of solving circular references by functions, I demonstrate some of the principles of user defined functions below. I have tried to read books on VBA and I have used a lot of discussion boards. I find these very difficult or sometimes to easy to be useful. I don’t care about making range’s dimensioned and using complex syntax. All I want to do is make a loop and compute some numbers that can be output to excel. This is the idea of my introduction. So, here are some general principles about functions including naming the function, using OPTION BASE 1, collecting inputs (you cannot refer to ranges in excel without using them to input) :

The Name of the Function Must be a Variable and the Result
----------------------------------------------------------

1\. The name of the function must be defined with and = sign. For example if you make a function named BONJOUR with Function Bonjour, then somewhere in the function you must have the statement BONJOUR = something (for example, BONJOUR = “Bonjour Monde”.

.

Function bonjour
bonjour = "Bonjour Monde"
end function

.

You Must Read Variables that You Want to Use into the Function
--------------------------------------------------------------

2\. You cannot use RANGES from the excel file. For example, you cannot use RANGE(“A1”) in your function. Instead, you must read the variable into excel. If you want to put the date into your BONJOUR function and the date is in excel, you must read the date into your function. To do this you would enter something like FUNCTION BONJOUR(Todaydate).

.

Function bonjour(todaydate)
bonjour = "Bonjour Monde" & todaydate
end function

.

Reading Scalars and Arrays
--------------------------

3\. You should understand the difference between SCALAR and ARRAY variables. If you read a series of inputs into the function, they are array variables such as the series of capital expenditures, or EBITDA over time. If you read a single variable like the debt to capital ratio, this is a scalar variable that must not have an index like debt\_to\_capital(i).  If you read in an array variable and then do not include an index, you will probably get the dreaded and painful #VALUE.

Option Base 1
-------------

4\. If you are making a loop in a function and you start the loop at 1 instead of zero (like I always do), then you should put the statement OPTION BASE 1 at the top of your module.  If you do not do this, your function will often be off by 1.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1571&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12728&rand=0.4806514144357633)