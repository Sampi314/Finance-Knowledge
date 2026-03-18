# How to Round to the Nearest Integer or Multiple of 0.5 / 5 / 10 in Excel

**Source:** https://trumpexcel.com/round-to-nearest-integer

---

[Skip to content](https://trumpexcel.com/round-to-nearest-integer/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/round-to-nearest-integer/#below-title)

**Watch Video – Round to the Nearest Integer or the Multiple of 0.5 / 5 / 10 in Excel**

Rounding a number to the nearest integer or the nearest 0.5 or 5 or 10 multiple is a common task for many people.

For example, if you’re a project manager involved in effort estimate, you can’t have 12.7 full-time resources working on a project.

You need to round-up this number to 13 (the nearest integer).

Similarly, if you’re buying stocks that are sold in a batch of 5, and you can afford a maximum of 123 shares only, you need to round it down to 120 (i.e., the lower multiple of 5).

While you can do this manually for a couple of values, doing it for hundreds of such value could become tedious and highly prone to errors.

There are a couple of [great functions in Excel](https://trumpexcel.com/excel-functions/)
 that allows you to quickly round to the nearest integer or the nearest 0.5 or 5 or 10 multiple.

In this tutorial, I will show you how to use the MROUND, CEILING, and FLOOR functions to do this type of rounding in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/round-to-nearest-integer/#)

Round to the Nearest Integer in Excel
-------------------------------------

Taking the example of project management, suppose you have a dataset as shown below where you want to quickly find out the number of resources needed for various projects that you’re managing.

![Round to the nearest integer - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20519%20164'%3E%3C/svg%3E)

Note that the ‘FTE Needed’ column has the values in decimals (calculated by dividing ‘Est Time’ with ‘Duration’).

In this case, you may need to convert these values into the next integer.

Here is the formula that will do this for you:

**\=ROUNDUP(D2,0)**

![Round to the nearest integer - ROUNDUP formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20217'%3E%3C/svg%3E)

ROUNDUP formula takes two arguments – the number to be rounded and the number of decimals to round it to.

Since in this case, we are looking for integers, we have used 0 as the second argument.

In case you want to round to the lower integer, you can use ROUNDDOWN formula as shown below:

**\=ROUNDDOWN(D2,0)**

Round to the Nearest Multiple of 0.5 in Excel
---------------------------------------------

Now suppose you have the same dataset as shown above, but now you can assign a 0.5 resource for a project.

In such cases, you would want to round a number with a decimal part:

*   Less than 0.5 to 0.5
*   More than 0.5 to 1

The following formula can be used to do this:

**\=CEILING.MATH(D2,0.5)**

![Round a number to 0.5 - CEILING function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20214'%3E%3C/svg%3E)

CEILING.MATH function takes the number and rounds it up to the specified multiple to which you want to round up.

In our example, since the significance value is 0.5, 6.71 becomes 7.0 and 7.29 becomes 7.5.

Note that Excel also has a CEILING function which works the same way. It has been kept for backward compatibility purposes.

![CEILING function in Excel for backward compatibility](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20176%2074'%3E%3C/svg%3E)

Also read: [Convert Mm To Inches In Excel](https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel/)

Round to the Nearest Multiple of 5 in Excel
-------------------------------------------

To round to the nearest 5 in Excel, you can use the MROUND function.

Suppose you have a dataset as shown below where you want to round the estimated number of hours to the nearest 5.

This would mean that 161 should become 160 and 163 would become 165.

![Round to the nearest 5 - example dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20272%20163'%3E%3C/svg%3E)

Below is the formula that will do this:

**\=MROUND(B2,5)**

MROUND function takes two arguments. The first argument is the number that you want to round, and the second argument is the multiple to which it should round.

In this case, since we want to round to the nearest 5, I have used 5 as the second argument.

Keep in mind that this doesn’t necessarily round to the higher or lower number. The result would depend on the value. In this example, if the decimal part in the value is less than 2.5, it becomes 0 and if it is more than or equal to 2.5, then it becomes 5.

Round Up to the Nearest Multiple of 5 in Excel
----------------------------------------------

In the above example, MROUND function would round to the nearest 5 based on the value. This could either be a round up or a round down.

But what if you want to **only round up to the nearest 5**.

Then you can use the CEILING.MATH function.

Here is the formula that will round up to the nearest 5.

**\=CEILING.MATH(B2,5)**

![Round up to the nearest 5 - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20399%20212'%3E%3C/svg%3E)

Round Down to the Nearest Multiple of 5
---------------------------------------

To round down to the nearest 5, you can use the below FLOOR.MATH function:

**\=FLOOR.MATH(B2,5)**

![Round down to the nearest 5 - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20209'%3E%3C/svg%3E)

Round to the Nearest Multiple of 10 in Excel
--------------------------------------------

Taking the same example (dataset shown below), if you want to round off the number of hours to the nearest 10, you can use the MROUND function.

![Round to the nearest 10 - example dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20272%20163'%3E%3C/svg%3E)

The following formula would round these numbers to the nearest 10:

**\=MROUND(B2,10)**

In this case, since we want to round to the nearest 10, I have used 10 as the second argument.

Keep in mind that this doesn’t necessarily round to the higher or lower number. The result would depend on the value. In this example, if the decimal part in the value is less than 5, it becomes 0, and if it is more than or equal to 5, then it becomes 10.

In case you only want to round up or round down to the nearest 10, use the CEILING.MATH or FLOOR.MATH functions.

Here are the two formula that will **round up to the nearest multiple of 10**:

**\=CEILING.MATH(B2,10)**

**\=ROUNDUP(B2,-1)**

Both these function would give the same result.

Similarly, if you want to **round down to the nearest multiple of 10**, you can use the below formulas:

**\=FLOOR.MATH(B2,10)**

**\=ROUNDDOWN(B2,-1)**

In case you’re wondering what’s the difference between the MROUND and CEILING/FLOOR functions, here is a comparison of results.![Round to the nearest 10 - MROUND CEILING AND FLOOR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20511%20165'%3E%3C/svg%3E)

In case you think the results of MROUND and FLOOR function are same, look again (hint: Project D).

Hope you find the methods shown in this tutorial useful.

In case there are other ways to get the rounding done, do share with me in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [Convert Date to Text in Excel.](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)
    .
*   [How to Calculate the Number of Days Between Two Dates in Excel](https://trumpexcel.com/number-of-days-between-two-dates/)
    .
*   [How to Stop Excel from Rounding Numbers](https://trumpexcel.com/stop-excel-from-rounding-numbers/)
    
*   [How to Display Numbers as Fractions in Excel (Write Fractions in Excel)](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    
*   [Round to the Nearest 1000 in Excel](https://trumpexcel.com/round-to-nearest-1000-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Round to the Nearest Integer or Multiple of 0.5 / 5 / 10 in Excel”
----------------------------------------------------------------------------------------

1.  super explanation ……thanks a lot
    
    [Reply](https://trumpexcel.com/round-to-nearest-integer/#comment-14155)
    
2.  In using the Google-Type Suggestion search box with vba-codes … I used that feature and it is great! Now, I need vba-codes to clear that dropdown selection field-item selected, so other selection may be made, quicker (dynamically). Can you help me with vba-codes that I may use as a button to clear that field?
    
    [Reply](https://trumpexcel.com/round-to-nearest-integer/#comment-9917)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/round-to-nearest-integer/#respond)

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