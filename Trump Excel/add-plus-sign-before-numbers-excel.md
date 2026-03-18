# How to Add Plus Sign Before Numbers in Excel

**Source:** https://trumpexcel.com/add-plus-sign-before-numbers-excel

---

[Skip to content](https://trumpexcel.com/add-plus-sign-before-numbers-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-plus-sign-before-numbers-excel/#below-title)

Excel is a great spreadsheet tool, but there are a few things about it that may irritate you sometimes.

For example, if you add a plus sign before a number in a cell in Excel, that plus sign would just go away. The same happens when you try and [add leading zeros](https://trumpexcel.com/add-leading-zeroes-excel/)
 before a number.

The reason for this is that Excel considers these as redundant (which is correct). But sometimes, you may need to be able to add a plus sign before a number (especially when you’re showing changes as shown below):

![Dataset with numbers with plus sign](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20286'%3E%3C/svg%3E)

Another common use-case of this is when you want the plus sign before a phone number (as phone are often written with a leading + sign)

While the plus sign goes away when you add it in front of a number by default, if you need it to be there, you can use a workaround.

In this tutorial, I will show you a simple way to add a plus sign before a positive number in Excel.

So let’s get started!

Using a Custom Number Format
----------------------------

You can create a [custom number format](https://trumpexcel.com/excel-custom-number-formatting/)
 for the cell where you want to show a plus sign before the number (only the positive numbers).

Doing this would not change the value in the cell. It will only change the way the cell data is displayed. So while you will see the plus sign before the number, that sign is not there as the actual content of the cell. So you can continue to use these numbers in calculations.

Suppose you have a dataset as shown below and you want to add a plus sign before all the positive numbers:

![Dataset where plus sign needs to be added](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20287'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cells that have the numbers when you want to add the + sign
2.  Right-click and then click on Format Cells![Right click and then click on Format cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20600'%3E%3C/svg%3E)
3.  In the Format Cells dialog box, within the Number tab, click on Custom option with the Category![Click on Custom in Number Format dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
4.  In the Type field, enter the following: **+0;-0;0![Enter the custom formatting code in the type field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20377'%3E%3C/svg%3E)**
5.  Click on OK

You would notice that a plus sign has now been added to the positive numbers, while everything else remains the same.

![Dataset with numbers with plus sign](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20286'%3E%3C/svg%3E)

Note that this actual content of the cell hasn’t changed. For example, the value in cell D3 is still 35. It’s just shown to you as a number that has a plus sign before it.

Also, just like any other formatting, you can copy-paste this format to other cells as well. To do this, just copy the cells that have this custom format and paste only the formats in the destination cells.

Some other custom formats that you may find useful:

*   Positive Numbers with a plus sign and negative numbers in bracket: +0;(0);0
*   Positive Numbers with a plus sign and negative numbers in red: +0;\[Red\]-0;0
*   Positive Numbers in green and negative numbers in red: \[Green\]+0;\[Red\]-0;0

Manually Adding the Plus Sign Before Positive Numbers
-----------------------------------------------------

The above custom number formatting method is the way to go in most cases. It’s fool-proof and works well even if you have large data sets.

In some cases, if you only have a few cells where you need to add the plus sign before a positive number, a quick way would be to simply add an apostrophe and then add the plus sign.

Adding an apostrophe converts the cell content into text, so when you add the plus sign, it sticks. Also, the apostrophe itself is not visible in the cell so you can use this in reports/dashboards and even print it.

So these are some ways you can use to add a plus sign before numbers in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials that you may like:**

*   [How to Copy Conditional Formatting to Another Cell in Excel](https://trumpexcel.com/copy-conditional-formatting-another-cell-excel/)
    
*   [How to Remove Table Formatting in Excel (Easy Guide)](https://trumpexcel.com/remove-table-formatting-excel/)
    
*   [How to Remove Cell Formatting in Excel (from All, Blank, Specific Cells)](https://trumpexcel.com/remove-cell-formatting-in-excel/)
    
*   [Change Negative Number to Positive in Excel \[Remove Negative Sign\]](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [How to Make Negative Numbers Show Up in Red in Excel](https://trumpexcel.com/negative-numbers-red-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-plus-sign-before-numbers-excel/#respond)

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