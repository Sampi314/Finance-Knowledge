# How to Calculate Compound Annual Growth Rate (CAGR) in Excel

**Source:** https://trumpexcel.com/calculate-cagr-excel

---

[Skip to content](https://trumpexcel.com/calculate-cagr-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-cagr-excel/#below-title)

If you’re into and financial planning or analysis, you must have heard about the **Compound Annual Growth Rate** (or CAGR).

In this tutorial, you’ll learn different ways to calculate the CAGR in Excel:

*   Using Operators
*   Using the POWER function.
*   Using RATE function.
*   Using the IRR Function.

But before we dive into how to calculate CAGR in Excel, let’s first understand what it means (feel free to skip this section if you already know what it is).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-cagr-excel/#)

What is CAGR?
-------------

CAGR or the Compound Annual Growth Rate tells us the growth rate at which our investments have grown on an annual basis.

For example, suppose you bought gold worth USD 100 in 2010 and it is worth USD 300 in 2020, CAGR would be the rate at the which your investment in gold grew every year.

Want to know more about CAGR, here is a detailed explanation on [Investopedia](http://www.investopedia.com/terms/c/cagr.asp)
.

Note that this number is completely imaginary. If your gold grew at 11.6% from USD 100 in 2010 to USD 300 in 2020, it doesn’t mean that it grew at this rate every year. The actual growth could be different, but it gives us an indication of how much growth our investment in gold has given us on an annual basis.

While we will see how to calculate CAGR in Excel, its importance lies in the fact that it makes it easier for us to compare different investment options.

Related tutorial: [How to Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)

How is CAGR calculated?
-----------------------

Here is the formula that will calculate the CAGR.

**CAGR = (Ending value / Beginning value)^(1/n) - 1**

Now let’s see how to calculate CAGR in Excel.

### Calculating CAGR in Excel Using Operators

Suppose we have the Beginning value in cell C2 and Ending Value in cell C3 (as shown below):

![how to calculate CAGR in Excel - data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20113'%3E%3C/svg%3E)

Here is the formula that will calculate the CAGR:

\=(C3/C2)^(1/10)-1

Here 10 is the number of years between the beginning of the investment period and the end of it.

![how to calculate CAGR in Excel - using operators](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20204'%3E%3C/svg%3E)

The 11.6% CAGR means that this investment has grown at a rate of 11.6% every year.

This would also help you compare it with your other investments (such as bank interests or government bonds).

### Calculating CAGR in Excel Using POWER Function

The [POWER function](https://office.microsoft.com/en-gb/excel-help/power-function-HP010342773.aspx)
 in Excel is a replacement of the ^ operator.

It just makes the formula more readable and clean.

Here is the POWER function that will give us the CAGR in Excel.

\=POWER(C3/C2,1/10)-1

![how to calculate CAGR in Excel - using Power Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20203'%3E%3C/svg%3E)

Also read: [Excel Formula for Percentage Increase](https://trumpexcel.com/percentage-change-excel/)

### Calculating CAGR in Excel Using the RATE Function

In this case, the RATE function can calculate the CAGR when you provide the time period, beginning value, and ending value.

The RATE function is made for much more than just CAGR.

Here is the syntax of the function:

RATE(Nper, Pmt, Pv, \[Fv\], \[Type\],\[Guess\])

Here is what each argument means:

*   Nper: The total number of payments done in the specified period.
*   Pmt:  Value of the payment made in each period.
*   Pv: The present value of the payment (or all the payments made in the specified period).
*   \[Fv\] (optional): The future value of the payment (or all the payments made in the specified period).
*   \[Type\] (optional): It specifies when the payments are due. 0 when the payment are due in the beginning and 1 when due at the end of the period. If omitted, defaults to 0.
*   \[Guess\] (optional): Your guess on the rate. Defaults to 10%.

Now don’t worry about all the arguments and the complicated syntax. As I mentioned, RATE function can be used for much more than just calculating the CAGR.

However, when calculating CAGR in Excel, you only need to use the following syntax:

\=RATE(Nper,,Pv, Fv)

Note that all three arguments are compulsory when calculating CAGR in Excel.

Here is the formula that will give the CAGR value:

\=RATE(B3-B2,,-C2,C3)

![how to calculate CAGR in Excel - rate](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20204'%3E%3C/svg%3E)

Now there are a couple of things you need to note about this function while calculating CAGR in Excel:

*   The second argument is left empty as there are no regular payments. This is used in cases where you make regular payments (monthly, quarterly, yearly), such as in the case of mutual funds.
*   There is a negative sign for the beginning value as it is an outflow of cash. The formula would return an error.

Note: You can also use the RRI function to calculate CAGR in Excel.

### Calculating CAGR in Excel Using the IRR Function

IRR stands for [Internal Rate of Return](https://trumpexcel.com/calculate-irr-excel/)
.

The difference between IRR and other formulas discussed above is that by using IRR, you can account for different value payments made during the time period.

For example, suppose you invest USD 100 in gold in 2010 and then you invest the same amount again 2014, and your final gold value is USD 300 in 2020, then you can calculate the CAGR using the IRR function.

This is something you can not do using the RATE of IRR [functions in Excel](https://trumpexcel.com/excel-functions/)
.

However, to use IRR, you need to structure your data as shown below:

![how to calculate CAGR in Excel - IRR Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20309%20310'%3E%3C/svg%3E)

Here there are three scenarios where the outflow is highlighted in [red and is negative](https://trumpexcel.com/negative-numbers-red-excel/)
, while the final value is positive.

Here is the formula that will give you the CAGR:

\=IRR(A2:A12)

All you need to do is select all the cells, where each cell represents payment in an equally spaced interval.

![how to calculate CAGR in Excel - IRR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20347%20382'%3E%3C/svg%3E)

Also, it is interesting to note that in scenarios 2 and 3, the invested amount is the same (i.e., USD 100), but since it’s invested later in scenario 3, the CAGR is higher.

These are some of the ways you can use to calculate CAGR in Excel. Which one do you like best? Or is there any other method you use to calculate CAGR in Excel?

Let me know in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [How to Calculate Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    .
*   [Calculating Loan Payments Using PMT Function](https://trumpexcel.com/pmt-function/)
    .
*   [How to Calculate Age in Excel using Formulas](https://trumpexcel.com/calculate-age-in-excel/)
    .
*   [How to Calculate and Format Percentages in Excel](https://trumpexcel.com/calculate-percentages-excel/)
    .
*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    .
*   [Calculating Compound Interest in Excel](https://trumpexcel.com/compound-interest-calculator/)
    .
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate Square Root in Excel](https://trumpexcel.com/calculate-square-root-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Calculate Compound Annual Growth Rate (CAGR) in Excel”
----------------------------------------------------------------------------

1.  Hi, How come my CAGR percentages are slightly lower for the three scenarios? For example scenario 1: yours is 11% whereas mine is 10.5%
    
    [Reply](https://trumpexcel.com/calculate-cagr-excel/#comment-13059)
    
2.  wonderful. really wonderful. please upload an example file in excel for all your articles relating to formulas.
    
    [Reply](https://trumpexcel.com/calculate-cagr-excel/#comment-12626)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-cagr-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK