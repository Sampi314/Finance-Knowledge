# How to Convert Inches to MM, CM, or Feet in Excel? Easy Formula

**Source:** https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel

---

[Skip to content](https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel/#below-title)

If you work with measurement data and there is a need to convert the data from one length measurement unit to another, you can use some inbuilt formulas in excel to do that.

For example, you may have a need to convert data in centimeters/millimeters to inches or feet.

In this short tutorial, I will show you how to use a simple formula to convert a value in one length measurement unit to another.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel/#)

CONVERT Formula in Excel
------------------------

Before I show you how to convert data from one unit to another, let me quickly introduce the formula that is going to help us do that.

It’s the CONVERT formula in Excel.

Below is the syntax of the CONVERT formula:

CONVERT(number, from\_unit, to\_unit)

Where:

*   number is the value that you want to convert from one measurement unit to another
*   from\_unit is the code for the measurement unit in which you already have the number
*   to\_unit is the code for the measurement unit in which you want the number to be converted

While it’s a simple formula, you do need to know the right measurement codes that you can use in the formula.

Below are some of the codes we will be using in this tutorial.

*   Inch – “in”
*   Feet – “ft”
*   Meter – “m”
*   Milimeter – “mm”
*   Centimeter – “cm”

If you want a full list of all the code (for various categories such as weight, distance, time, pressure, force, energy, power, etc), you can [check it out here](https://support.microsoft.com/en-us/office/convert-function-d785bef1-808e-4aac-bdcd-666c810f9af2?ns=excel&version=90&ui=en-us&rs=en-us&ad=us)
.

Now that we know what formula to use to convert Inches to a millimeter or centimeter or meter, let’s have a look at the examples.

### Converting Inches to Millimeter (MM), Centimeter (CM), Meter (M), or Feet

Suppose you have a dataset as shown below and you want to convert the values in inches into MM, CM, and M

Below is the formula to convert Inches to Millimeter:

\=CONVERT(A2,"in","mm")

![Convert Inches to MM](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20576%20324'%3E%3C/svg%3E)

Below is the formula to convert Inches to Centimeter:

 =CONVERT(A2,"in","cm") 

![Convert Inches to CM formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20315'%3E%3C/svg%3E)

Below is the formula to convert Inches to Meter:

 =CONVERT(A2,"in","m") 

![Convert inches to meter formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20316'%3E%3C/svg%3E)

And in the same way, if you want to do the reverse – i.e., to convert MM or CM to Inches – you just need to reverse the codes.

So the formula to convert MM to Inches would be:

 =CONVERT(A2,"mm","in") 

![Convert MM to Inches](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20316'%3E%3C/svg%3E)

### Converting Inches to Feet

A more common conversion needed is between inches and feet.

Again, you can use the same formula with the right measurement codes as the from\_unit and to\_unit.

Below is the formula to convert inches to feet:

  =CONVERT(A2,"in","ft")  

![Convert Inches to Feet formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20573%20316'%3E%3C/svg%3E)

Some Important Things to Know about the Convert Formula
-------------------------------------------------------

*   In case you use an incorrect from\_unit or to\_unit code, the fromula will return a [#N/A error](https://trumpexcel.com/iferror-vlookup/)
    
*   You can only convert a value in the same group of measurement. For example, if you’re dealing with millimeter and centimeter values, then these are in the distance group. You can only convert a value from this group into another value in the group. In case you try conversion in different group, it will give you a #N/A error
*   While you’re entering the formula, Excel helps you by showing all units that are available to use and you can then choose from the intellisense. I don’t know why, but “mm” and “cm” are not part of the list it shows, but these still work in the formula.
*   The unit codes/names are [case sensitive](https://trumpexcel.com/vlookup-case-sensitive/)
    . So you can not use “MM” or “CM” instead of “mm” or “cm”. If you do, it gives the #N/A error

While I have only covered a part of the CONVERT formula and showed you how to convert MM or CM or Feet to Inches (or vice-versa), you can do some very useful other conversions as well (such as Grams/Kilograms to Pound or Feet to Yard).

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Convert Numbers to Text in Excel – 4 Super Easy Ways](https://trumpexcel.com/convert-numbers-to-text-excel/)
    
*   [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [Convert Date to Text in Excel – Explained with Examples](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [Convert Bytes to MB or GB in Excel (2 Easy Ways)](https://spreadsheetplanet.com/convert-bytes-to-mb-gb-excel/)
    
*   [](https://spreadsheetplanet.com/convert-bytes-to-mb-gb-excel/)
    [How to Convert Radians to Degrees in Excel (Easy Formula)](https://spreadsheetplanet.com/convert-radians-to-degrees-excel/)
    
*   [Convert Number to Words in Excel](https://trumpexcel.com/number-to-words-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-inches-to-mm-cm-feet-excel/#respond)

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