# How to Use Excel MOD Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-mod-function

---

[Skip to content](https://trumpexcel.com/excel-mod-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-mod-function/#below-title)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-mod-function/#)

Excel MOD Function (Example + Video)
------------------------------------

![Excel MOD Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20330'%3E%3C/svg%3E)

### When to use Excel MOD Function

MOD function can be used when you want to get the remainder when one number is divided by another number.

### What it Returns

It returns a numerical value that represents the remainder when one number is divided by another.

### Syntax

\=MOD(number, divisor)

### Input Arguments

*   **number –** A numeric value for which you want to find the remainder.
*   **divisor –** A number with which you want to divide the _number_ argument. If the _divisor_ is 0, then it will return the #DIV/0! error.

### Additional Notes

*   If the _divisor_ is 0, then it will return the #DIV/0! error.
*   The result always has the same sign as that of the divisor.
*   You can use decimal numbers in the MOD function. For example, if you use the function =MOD(10.5,2.5), it will return 0.5.

Examples of Using MOD Function in Excel
---------------------------------------

Here are useful examples of how you can use the MOD function in Excel.

### Example 1 – Add Only the Odd or the Even Numbers

Suppose you have a dataset as shown below:

![Excel MOD Function - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20544%20351'%3E%3C/svg%3E)

Here is the formula you can use to add only the even numbers:

**\=SUMPRODUCT($A$2:$A$11\*(MOD($A$2:$A$11,2)=0))**

Note that here I have hard coded the range ($A$2:$A$11). If your data is likely to change, you can use an [Excel Table](https://trumpexcel.com/excel-table/)
 or created a [dynamic named range](https://trumpexcel.com/named-ranges-in-excel/)
.

Similarly, if you want to add only the odd numbers, use the below formula:

**\=SUMPRODUCT($A$2:$A$11\*(MOD($A$2:$A$11,2)=1))**

![MOD function to calcuate odd numbers in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20398'%3E%3C/svg%3E)

This formula works by calculating the remainder using the MOD function.

For example, when calculating the sum of odd numbers, (MOD($A$2:$A$11,2)=1) would return an array of TRUEs and FALSEs. If the number is odd, it would return a TRUE, else a FALSE.

[SUMPRODUCT function](https://trumpexcel.com/excel-sumproduct-function/)
 then only adds those numbers that are returning a TRUE (i.e., odd numbers).

The same concept works when calculating the sum of even numbers.

### Example 2 – Specify a Number in Every Nth Cell

Suppose you are making a list of fix expenses every month as shown below:

![Using MOD Function to specify an amount every three months](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20326'%3E%3C/svg%3E)

While the house and car EMIs are monthly, the insurance premium is paid every three months.

You can use the MOD function to quickly fill the cell in every third row with the EMI value.

Here is the formula that will do this:

\=[IF](https://trumpexcel.com/excel-if-function/)
(MOD(([ROW()](https://trumpexcel.com/excel-row-function/)
\-1),3)=0,457,””)

![Fill every nth cell with a value in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20371'%3E%3C/svg%3E)

This formula simply analyzes the number given by ROW()-1.

ROW function gives us the row number and we have subtracted 1 as our data starts from second row onwards. Now the MOD function checks the remainder when this value is divided by 3.

It will be 0 for every third row. Whenever this is the case, IF function would return 457, else it will return a blank.

### Example 3 – Highlight Alternate Rows in Excel

Highlighting alternate rows can increase the readability of your data set (especially when it’s printed).

Something as shown below:

![Highlight Every other row using MOD Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20325'%3E%3C/svg%3E)

Note that every second row of the dataset is highlighted.

While you can do this manually for a small dataset, if you have a huge one, you can leverage the power of [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
 with the MOD function.

Here are the steps that will highlight every second row in the dataset:

*   Select the entire data set.
*   Go to the Home tab.
*   Click on Conditional Formatting and select New Rule.![conditional formatting in incell charts](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20196%20385'%3E%3C/svg%3E)
*   In the ‘New Formatting Rule’ dialog box, select ‘Use a formula to determine which cells to format’.![Conditional Formatting Use Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20366'%3E%3C/svg%3E)
*   In the formula field, enter the following formula: =MOD(ROW()-1,2)=0![Mod function in Conditional Formatting dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20366'%3E%3C/svg%3E)
*   Click on the Format button and specify the color in which you want the rows highlighted.
*   Click OK.

This will instantly highlight alternate rows in the dataset.

You can read more about this technique and variations of it in [this tutorial](https://trumpexcel.com/highlight-every-other-row-excel/)
.

### Example 4 – Highlight All the Integer /Decimal Values

You can use the same conditional formatting concept shown above to highlight integer values or decimal values in a data set.

For example, suppose you have a dataset as shown below:

![Highlight Numbers with decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20411%20257'%3E%3C/svg%3E)

There are numbers that are integers and some of these have decimal values as well.

Here are the steps to highlight all the numbers that have decimal value in it:

*   Select the entire data set.
*   Go to the Home tab.
*   Click on Conditional Formatting and select New Rule.![conditional formatting in incell charts](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20196%20385'%3E%3C/svg%3E)
*   In the ‘New Formatting Rule’ dialog box, select ‘Use a formula to determine which cells to format’.![Conditional Formatting Use Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20366'%3E%3C/svg%3E)
*   In the formula field, enter the following formula: =MOD(A1,1)<>0
*   Click on the Format button and specify the color in which you want the rows highlighted.
*   Click OK.

This will highlight all the numbers that have a decimal part to it.

![Data with decimal part highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20258'%3E%3C/svg%3E)

Note that we in this example, we have used the formula =MOD(A1,1)<>0. In this formula, make sure the cell [reference is absolute](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 (i.e., A1) and not relative (i.e., it shouldn’t be $A$1, $A1 or A$1).

**Excel MOD Function – Video Tutorial**

**Related Excel Functions:**

*   [Excel INT Function](https://trumpexcel.com/excel-int-function/)
    .
*   [Excel RAND Function](https://trumpexcel.com/excel-rand-function/)
    .
*   [Excel RANDBETWEEN Function](https://trumpexcel.com/excel-randbetween-function/)
    .
*   [Excel ROUND Function](https://trumpexcel.com/excel-round-function/)
    .
*   [Excel RANK Function](https://trumpexcel.com/excel-rank-function/)
    .
*   [Excel LARGE Function](https://trumpexcel.com/excel-large-function/)
    .
*   [Excel MAX Function](https://trumpexcel.com/excel-max-function/)
    .
*   [Excel MIN Function](https://trumpexcel.com/excel-min-function/)
    .
*   [Excel SMALL Function](https://trumpexcel.com/excel-small-function/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Use Excel MOD Function (Examples + Video)”
---------------------------------------------------------------

1.  I am a little confused about the statement in example 4 on using absolute cell references in the conditional formatting formula. The example given, cell A1, with text saying this is an absolute reference is contradictory to the linked cell reference article. The linked article says a cell reference with no $ signs is a relative reference while a cell reference with $ signs is an absolute reference.
    
    The exact text from above article is: “In this formula, make sure the cell reference is absolute (i.e., A1) and not relative (i.e., it shouldn’t be $A$1, $A1 or A$1).”
    
    In the linked article ‘Absolute, Relative and Mixed Cell References in Excel’ an absolute cell reference is described as: “A dollar symbol, when added in front of the row and column number, makes it absolute…”
    
    Please will you explain the apparent contradiction of if I am missing something.
    
    [Reply](https://trumpexcel.com/excel-mod-function/#comment-14126)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-mod-function/#respond)

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