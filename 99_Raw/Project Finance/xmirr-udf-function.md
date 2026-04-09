# XMIRR UDF

**Source:** https://edbodmer.com/xmirr-udf-function

---

This page demonstrates how to create an XMIRR function that works in a similar manner to the MIRR function, but includes specific dates and produces and annual return. To create the XMIRR function you can see how to create user-defined functions with VBA and how the IRR function in excel really works.

The modified IRR or MIRR function has been suggested by some as better then the regular old IRR function because it contains assumptions about re-investment. For most applications, this idea is total rubbish. There are many problems with the IRR related to not accounting for changes in risk and understating long-term cash flows when the IRR is high, but the MIRR does not do much to solve these problems. All it does is to move the IRR toward an arbitrary re-investment assumption. So, please don’t think I am advocating use of the MIRR. Of course, if there are not any intermediate cash flows, the MIRR is no different from the IRR because the re-investment assumption only affects intermediate cash flow.

The real measure is to reconcile the IRR with the ROI and use rates other than the IRR itself to discount the IRR over the project life. (If you have no idea what I am talking about you can go to the advanced corporate finance section).

Creating an XMIRR Function
--------------------------

I made an XMIRR a long time ago. While the concept of XMIRR is a lot of B.S., making the function does demonstrate that the IRR is just a compound growth rate. The XMIRR function converts annual rates to daily rates and then pushes the middle cash flows to the future value by compounding the cash flows at a daily re-investment rate. The exerpt below demonstrates results of the MIRR function. Note that you can find the functions in a library of functions in Chapter 1 of the google drive under the last folder for L. Excel Utilities / Function Library.

The file with the user defined function for the XMIRR is available for download by pressing the button below.  After you open the file, you can either press the macro button to get the VBA code to copy or alternatively you can use the ALT, F8 sequence to get the VBA Code and put it in your file.

**[Excel File with VBA code for User-defined Function that Computes XMIRR with Compound Growth Formula](https://edbodmer.com/wp-content/uploads/2018/05/XMIRR.xlsm)
**

VBA Code for Creating XMIRR
---------------------------

To create the XMIRR function, you need to create a function. This means that you must (1) define the name of the function somewhere in the function and (2) read in arguments for the function rather than using RANGE(“…”) in excel. You must also understand the difference between an array and a scalar. Array’s can be read into the function and then work through a loop. Once you have created a function in one file, you cannot use it in another file even if the file is open (this contrasts with regular old macros). The XMIRR macro is demonstrated below. You can find this function in the XMIRR file above.

.

Function xmirr(cash\_flow, dates, borrow\_rate, finance\_rate)

num = cash\_flow.Count ' count then number of cash flows for loop

daily\_borrow = (1 + borrow\_rate) ^ (1 / 365) - 1 ' compute daily rate from annual rate
daily\_finance = (1 + finance\_rate) ^ (1 / 365) - 1

' The IRR is a growth rate and you need the future value as well as present value
' Then you compute the compound annual growth with FV/PV
' You can do this on a daily basis

p\_v = 0
f\_v = 0

For i = 1 To num

days\_count = dates(i) - dates(1)
days\_count1 = dates(num) - dates(i)

borrow\_factor = 1 / (1 + daily\_borrow) ^ days\_count
refinance\_factor = (1 + daily\_finance) ^ days\_count1

If cash\_flow(i) <= 0 Then p\_v = p\_v + borrow\_factor \* cash\_flow(i)
If cash\_flow(i) > 0 Then f\_v = f\_v + refinance\_factor \* cash\_flow(i)

Next i

years = days\_count / 365 ' convert back to annual number

xmirr = (f\_v / -p\_v) ^ (1 / years) - 1 ' This is CAGR

End Function

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1581&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.8534429485922848)