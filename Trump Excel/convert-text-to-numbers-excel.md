# Convert Text to Numbers in Excel - A Step By Step Tutorial

**Source:** https://trumpexcel.com/convert-text-to-numbers-excel

---

[Skip to content](https://trumpexcel.com/convert-text-to-numbers-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-text-to-numbers-excel/#below-title)

It’s common to find numbers stored as text in Excel. This leads to incorrect calculations when you use these cells in Excel functions such as SUM and AVERAGE (as these functions ignore cells that have text values in it).

In such cases, you need to convert cells that contain numbers as text back to numbers.

Now before we move forward, let’s first look at a few reasons why you may end up with a workbook that has numbers stored as text.

1.  Using ‘ (apostrophe) before a number.
    *   A lot of people enter apostrophe before a number to make it text. Sometimes, it’s also the case when you download data from a database. While this makes the numbers show up without the apostrophe, it impacts the cell by forcing it to treat the numbers as text.
2.  Getting numbers as a result of a formula (such as LEFT, RIGHT, or MID)
    *   If you extract the numerical part of a text string (or even a part of a number) using the TEXT functions, the result is a number in the text format.

Now, let’s see how to tackle such cases.

Convert Text to Numbers in Excel
--------------------------------

In this tutorial, you’ll learn how to convert text to numbers in Excel.

The method you need to use depends on how the number has been converted into text. Here are the ones that are covered in this tutorial.

*   Using the ‘Convert to Number’ option.
*   Change the format from Text to General/Number.
*   Using Paste Special.
*   Using [Text to Columns](https://trumpexcel.com/excel-text-to-columns-examples/)
    .
*   Using a Combination of VALUE, TRIM, and CLEAN function.

### Convert Text to Numbers Using ‘Convert to Number’ Option

When an apostrophe is added to a number, it changes the number format to text format. In such cases, you’ll notice that there is a green triangle at the top left part of the cell.

![Convert Text to Numbers in Excel - Green Triangle](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20167%20163'%3E%3C/svg%3E)

In this case, you can easily convert numbers to text by following these steps:

*   Select all the cells that you want to convert from text to numbers.![Convert Text to Numbers in Excel - Select Cells Green Triangle](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20189%20174'%3E%3C/svg%3E)
*   Click on the yellow diamond shape icon that appears at the top right. From the menu that appears, select ‘Convert to Number’ option.

This would instantly convert all the numbers stored as text back to numbers. You would notice that the numbers get aligned to the right after the conversion (while these were aligned to the left when stored as text).

### Convert Text to Numbers by Changing Cell Format

When the numbers are formatted as text, you can easily convert it back to numbers by changing the format of the cells.

Here are the steps:

*   Select all the cells that you want to convert from text to numbers.
*   Go to Home –> Number. In the Number Format drop-down, select General.

This would instantly change the format of the selected cells to General and the numbers would get aligned to the right. If you want, you can select any of the other formats (such as Number, Currency, Accounting) which will also lead to the value in cells being considered as numbers.

Also read: [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)

### Convert Text to Numbers Using Paste Special Option

To convert text to numbers using Paste Special option:

*   Enter 1 in any empty cell in the worksheet. Make sure it is formatted as a number (i.e., aligned to the right of the cell).
*   Copy the cell that contains 1.
*   Select the cells that you want to convert from text to numbers.
*   Right-click and select Paste Special.![Convert Text to Numbers in Excel - paste special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20281'%3E%3C/svg%3E)
*   In the Paste Special dialog box, select Multiply within the Operation category.![Convert Text to Numbers in Excel - multiply paste special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20340'%3E%3C/svg%3E)
*   Click OK.

### Convert Text to Numbers Using Text to Column

This method is suitable in cases where you have the data in a single column.

Here are the steps:

*   Select all the cells that you want to convert from text to numbers.
*   Go to Data –> Data Tools –> Text to Columns.![Convert Text to Numbers in Excel - text to column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20331%20133'%3E%3C/svg%3E)
*   In the Text to Column Wizard:
    *   In Step 1: Select Delimited and click on Next.![Convert Text to Numbers in Excel - text to column step1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20424'%3E%3C/svg%3E)
    *   In Step 2: Select Tab as the delimiter and click on Next.![Convert Text to Numbers in Excel - text to column step2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20422'%3E%3C/svg%3E)
    *   In Step 3: In Column data format, make sure General is selected. You can also specify the destination where you want the result. If you don’t specify anything, it will replace the original data set.![Convert Text to Numbers in Excel - text to column step3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20422'%3E%3C/svg%3E)

While you may still find the resulting cells to be in the text format, and the numbers still aligned to the left, now it would work in functions such as SUM and AVERAGE.

Also read: [How to Write Scientific Notation in Excel?](https://trumpexcel.com/scientific-notation-excel/)

### Convert Text to Numbers Using the VALUE Function

You can use a combination of VALUE, TRIM and CLEAN function to convert text to numbers.

*   VALUE function converts any text that represents a number back to a number.
*   [TRIM](https://trumpexcel.com/excel-trim-function/)
     function [removes any leading or trailing spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
    .
*   CLEAN function removes extra spaces and non-printing characters that might sneak in if you import the data or download from a database.

Suppose you want convert cell A1 from text to numbers, here is the formula:

\=VALUE(TRIM(CLEAN(A1)))

If you want to apply this to other cells as well, you can copy and use the formula.

Finally, you can [convert the formula to value using paste special](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

**You May Also Like the Following Excel Tutorials:**

*   [Multiply in Excel Using Paste Special](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
    .
*   [How to Convert Text to Date in Excel (8 Easy Ways)](https://trumpexcel.com/convert-text-to-date-excel/)
    
*   [How to Convert Numbers to Text in Excel](https://trumpexcel.com/convert-numbers-to-text-excel/)
    
*   [Convert Formula to Values Using Paste Special](https://trumpexcel.com/convert-formulas-to-values-excel/)
    .
*   [Excel Custom Number Formatting](https://trumpexcel.com/excel-custom-number-formatting/)
    .
*   [Convert Time to Decimal Number in Excel](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [Change Negative Number to Positive in Excel](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [How to Capitalize First Letter of a Text String in Excel](https://trumpexcel.com/capitalize-first-letter-excel/)
    
*   [Convert Scientific Notation to Number or Text in Excel](https://trumpexcel.com/convert-scientific-notation-to-number-text/)
    
*   [How To Convert Date To Serial Number In Excel?](https://trumpexcel.com/convert-date-to-serial-number-excel/)
    
*   [How to Convert Fraction to Decimal in Excel](https://trumpexcel.com/convert-fraction-to-decimal-excel/)
    
*   [How to Format Phone Numbers in Excel?](https://trumpexcel.com/format-phone-numbers-excel/)
    
*   [Convert Amount to Words in Excel](https://trumpexcel.com/number-to-words-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “Convert Text to Numbers in Excel”
------------------------------------------------

1.  I have see that most of tips are very helpful
    
    [Reply](https://trumpexcel.com/convert-text-to-numbers-excel/#comment-14839)
    
2.  Thanks for this. Didn’t actually work but gave me the idea to multiply the cells by 1, drag and drop and use those instead, which worked
    
    [Reply](https://trumpexcel.com/convert-text-to-numbers-excel/#comment-14442)
    
3.  I have numbers from a financial database that are formatted with the suffix for basis points — e.g., 14bp . By default, they are read into Excel as text. I have not found a way to convert these to numbers except for very time-consuming methods: use text to columns to get rid of the bp (which I can do on the initial parse when I still have spaces so that I can use Fixed Width parsing, but if I try to do it after the first parsing, then Excel has stripped the leading spaces and I have to use Delimited parsing and tell it to treat “b” as a separator.) Otherwise, I’m down to using Left(thenumber, len(thenumber)-2), which then may need to be converted into text again.  
    Do you have a faster way to do this? I thought, perhaps, if I made bp a custom number format Excel would then recognize 14bp as a number when it reads it, but that doesn’t work.
    
    [Reply](https://trumpexcel.com/convert-text-to-numbers-excel/#comment-14234)
    
4.  thank you . now i can sum numbers with changing their formats from text to numbers
    
    [Reply](https://trumpexcel.com/convert-text-to-numbers-excel/#comment-14044)
    
5.  none of these worked
    
    [Reply](https://trumpexcel.com/convert-text-to-numbers-excel/#comment-13654)
    
6.  very helpful thanks allot
    
    [Reply](https://trumpexcel.com/convert-text-to-numbers-excel/#comment-11281)
    
7.  Clear precious information
    
    [Reply](https://trumpexcel.com/convert-text-to-numbers-excel/#comment-11168)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-text-to-numbers-excel/#respond)

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