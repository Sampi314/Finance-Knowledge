# How to Calculate Ratios in Excel? 3 Easy Ways!

**Source:** https://trumpexcel.com/calculate-ratios-excel

---

[Skip to content](https://trumpexcel.com/calculate-ratios-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-ratios-excel/#below-title)

It’s a common task to calculate ratios when working with financial data or doing other data analysis work in Excel.

Even in our day-to-day life, we use ratios in areas such as screen size (in specifying resolutions such as 16:9) or cooking (in specifying proportions such as using two ingredients in 2:3 proportion).

While there is no inbuilt formula in Excel to calculate ratios, there are a couple of simple workarounds you can use to do this.

In this short tutorial, I’m going to show you a couple of simple formulas that you can use to **calculate ratios in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-ratios-excel/#)

Calculate Ratios Using the GCD Function
---------------------------------------

When calculating the ratios of two numbers, we have to find out the lowest proportion in which we can write it.

For example, If we want to calculate the ratio of 1920 and 1080 (the screen dimension of a 1080p resolution), the answer would be 16:9.

While we could have also used 1920:1080, it’s not the most simplified ratio, so we divided both these values by 480 (which is the Greatest Common Divisor that divides both numbers).

So if we want to calculate ratios in Excel, The first step would be to calculate the Greatest Common Divisor for the given numbers. Thankfully, Excel already has an inbuilt function to calculate the GCD for us.

Let me show you how it works.

Below I have a data set where I have the width value in column A and the height value in column B, and I want to calculate the ratio of these two numbers.

![Data set to calculate GCD and ratios](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20247'%3E%3C/svg%3E)

Before getting the ratio, I would have to calculate the GCD value, which can be done using the below formula.

\=GCD(A2,B2) 

Enter this formula in cell C2 and copy it for the entire column to get the GCD value for the entire data set.

![Formula to calculate the greatest common divisor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20298'%3E%3C/svg%3E)

Once I have the GCD value, I can calculate the ratio by using the below formula:

\=A2/C2&":"&B2/C2

![Formula to calculate ratio using GCD](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20295'%3E%3C/svg%3E)

The above formula divides the values in A2 and B2 by the Greatest Common Divisor value in cell C2.

And then, both these values (A2/C2 and B2/C2) are then combined Using the ampersand ‘&’ operator, and a colon is inserted in between the values.

If you do not want to create an additional column that calculates the GCD value, you can use the below formula, where the GCD values are calculated in the formula itself:

\=A2/GCD(A2,B2)&":"&B2/GCD(A2,B2)

![Formula to calculate ratio with GCD formula baked in](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20301'%3E%3C/svg%3E)

**Note**: In this example, I have shown you how to calculate the ratio for two numbers. You can follow the same process to calculate the ratio for three numbers as well.

Also read: [Convert Decimal To Fraction In Excel](https://trumpexcel.com/display-numbers-as-fractions-excel/)

Calculate Ratios Using Custom Number Formatting
-----------------------------------------------

There is also a less-known [custom formatting technique](https://trumpexcel.com/excel-custom-number-formatting/)
 that allows you to format numbers as ratios.

The only drawback of this method is that it will give you the ratio with a forward slash (/) instead of the colon (:).

Let me show you how it works.

Below I have the data set where I have the width value in column and height value in column B, and I want to calculate the ratios in column C.

![Data set to calculate ratios in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20250'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Enter the following formula in cell C2

\=A2/B2

![Enter the division formula in cell C2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20390%20306'%3E%3C/svg%3E)

2.  Copy this formula for the [entire column](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
    .

![Apply the formula to the entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20357%20251'%3E%3C/svg%3E)

3.  Select the entire data set that has the values in column C (C2:C7 in our example)
4.  Hold the Control key and then press the 1 key. This will open the ‘Format Cells’ dialog box.
5.  Within the Number group, select the Custom option.

![Click on the custom option in the number tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)

6.  Enter the following format in the Type: field.

#/#

![Enter the format in the type field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)

7.  Click OK

When you apply the above custom number format, it will show you the result of the division in the ratio format (except that there would be a forward slash instead of a colon in between the two numbers).

![Ratio values are shown in the specified custom format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%20251'%3E%3C/svg%3E)

One benefit of this method is that the result in the cells showing the ratios still contains the number that you got after dividing values in column A and column B. So you see 16:9 in cell C2, the value in the backend is still 1.77778 (which we got when we divided 1600 by 900). So while you see a ratio in the cell, you can use the decimal value in the back end in calculations

Calculate Ratios Using the TEXT Function
----------------------------------------

Another formula you can use to calculate ratios in Excel is by using the TEXT function, along with the SUBSTITUTE function.

The TEXT function allows you to use a custom number format to calculate the ratio, and then the SUBSTITUTE function replaces the forward slash (/) with the colon (:).

Let me show you how it works.

Below I have the same data set where I have the width value in column A and the height value in column B, and I want to get the ratio in column C.

![Data set to calculate ratios in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20250'%3E%3C/svg%3E)

Here is the formula that would give us the ratio:

\=SUBSTITUTE(TEXT(A2/B2,"#/#"),"/",":")

Enter this formula in cell C2 and copy it for all the cells in the column.

![Text function to calculate ratios in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20297'%3E%3C/svg%3E)

Let me explain how this formula works:

*   [TEXT function](https://trumpexcel.com/excel-text-function/)
     takes two arguments, the value (which is where we have calculated the ratio using A2/B2) and the format in which it should be displayed (which is “#/#”). The result of the TEXT function would be 16/9 in cell C2.
*   [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
     Is then applied on the result of the TEXT function to replace the forward slash (/) with a colon (:)

The result that you get from this formula is a text value, Which means that you can append text before or after the ratio if you want.

For example, I can use the below formula to append the text “Resolution” followed by the ratio value:

\="Resolution - "&SUBSTITUTE(TEXT(A2/B2,"#/#"),"/",":")

![Appending text to the text function for ratios](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20738%20304'%3E%3C/svg%3E)

In this article, I’ve covered three methods you can use to calculate ratios in Excel. The easiest way would be to calculate the Greatest Common Divisor value using the GCD function in Excel and then use it to calculate the ratio.

In many cases, I prefer using the custom formatting method, where I am ok showing a forward slash instead of the colon.

I hope you found this Excel tutorial useful.

**Other Exel articles you may also like:**

*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    
*   [How to Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)
    
*   [How to Square a Number in Excel](https://trumpexcel.com/square-number-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-ratios-excel/#respond)

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