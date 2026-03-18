# Convert Scientific Notation to Number or Text in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/convert-scientific-notation-to-number-text

---

[Skip to content](https://trumpexcel.com/convert-scientific-notation-to-number-text/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-scientific-notation-to-number-text/#below-title)

If you enter a number that has more than 11 digits in a cell in Excel, it will automatically be converted into the scientific notation (as shown below).

![Number displayed in Scientific notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20481%20121'%3E%3C/svg%3E)

While the number in the back end would still remain the same, Excel changes the way it shows you that number.

Sometimes that’s what you want, and sometimes you may want to convert the scientific notation back to regular numbers.

In this short tutorial, I’m going to show you a couple of ways to **convert numbers that are shown in the scientific notation back into being shown as regular numbers**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-scientific-notation-to-number-text/#)

Convert Scientific Notation to Numbers in Excel
-----------------------------------------------

Let me first show you a very simple method to change the way numbers are shown to the users in a cell in Excel.

As I mentioned, any number that is more than 11 digits would automatically be converted into scientific notation.

Using the method below, you can force the formatting of the cell to show the entire number instead of converting it into scientific notation.

### By Changing the Cell Format

Below I have a data set where I have some large numbers in cells in column a comma and I want to show these numbers as is.

As of now, you can see that these have been converted into scientific notation.

![Data with numbers in scientific notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20310'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cells that have the numbers in the scientific notation
2.  Click the Home tab in the ribbon

![Click Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20223'%3E%3C/svg%3E)

3.  In the Number group, click on the dialog box launcher icon (the small tilted arrow icon). This will open the

![Click the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20161'%3E%3C/svg%3E)

4.  In the Format Cells dialog box that opens, click on the Number tab

![Click the Number tab in Format Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  In the Category options, select ‘Custom’
6.  In the Type field, enter 0

![Enter 0 as the format for the cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

7.  Click Ok

The above steps would force the selected cells to show the whole number instead of converting them into scientific notation.

![Number in Scientific notation converted back to numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20276%20310'%3E%3C/svg%3E)

One important thing you need to remember when working with large numbers in Excel is that Excel would only show you numbers up to 15 digits with precision. This means that in case you have a 17-digit number, Excel will automatically convert the last two digits into 0.

If you’re working with numbers larger than 15 digits and want to show the entire number, you cannot do that by keeping it as a number in Excel. You will have to [convert it into text](https://trumpexcel.com/convert-numbers-to-text-excel/)
 (covered later in this tutorial).

Also read: [How to Write Scientific Notation in Excel?](https://trumpexcel.com/scientific-notation-excel/)

### By adjusting the Column Width (If the Number is 11 Digits or Less)

Sometimes, when you’re working with numbers that have 11 or less than 11 digits (which is the length at which Excel should not convert these numbers into scientific notation), there is still a possibility that you may see these numbers be converted into scientific notation.

![Number shown in scientific notation when column width is less](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20357%20350'%3E%3C/svg%3E)

This can happen if the [column width](https://trumpexcel.com/lock-row-height-column-width-excel/)
 is not wide enough to show the entire number, so Excel tries to [adjust the column width](https://trumpexcel.com/autofit-excel/)
 by showing that number in the scientific notation.

If you increase the [column width](https://trumpexcel.com/copy-column-width-excel/)
 enough to show the whole number, you’ll see that it will solve the problem.

Note that this would work only for numbers that are 11 digits or less. Any number that is longer than 11 digits would anyway be shown in the scientific notation, so adjusting the column width won’t help. In such cases, use the method covered before (by changing cell formatting)

Convert Scientific Notation to Text in Excel
--------------------------------------------

In the above section, I showed you how to convert numbers that are being shown in scientific notation back into regular numbers that show all the digits.

As I mentioned, if you’re working with numbers that are more than 15 digits, Excel will automatically convert all the digits after the 15th digit to 0.

In such cases, it would be better to convert these numbers into text. Numbers that have been converted into the text format are not changed and are shown as is.

Let’s see a couple of easy ways to do this.

### Adding an Apostrophe at the Beginning

If you’re manually entering numbers with more than 11 digits comma adding an apostrophe at the beginning of these numbers would convert the entire number to text.

Below I have an example where I have large numbers in two columns. The cells in column A are in the number format and the numbers in it are converted into scientific notation, but the numbers in column B have a leading apostrophe, so it’s treated as text and is shown as is.

![Number with apostrophe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20287'%3E%3C/svg%3E)

One thing to remember about this method is that you won’t be able to use these numbers in formulas that specifically need a numeric value (such as the SUM formula). Thankfully, most Excel formulas that deal with numeric values would be able to interpret this as a number.

When you add an apostrophe before a number. Excel would show a green triangle at the top-left of the cell. That’s Excel’s way of letting you know that something may be wrong. You can ignore it, or select the cell, click on the yellow triangle warning icon that shows, and then click on ‘Ignore Error’.

### Using Formulas (UPPER, TRIM, TEXT)

If you have some numbers that are being shown in scientific notation, you can use some really easy text formulas to quickly convert them into text so that the entire number is shown.

Below I have some numbers in column a that are currently being shown if scientific notation.

Here’s a formula that could show the entire number:

\=TRIM(A2)

![TRIM formula to show large numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20470%20397'%3E%3C/svg%3E)

Although the [TRIM formula](https://trumpexcel.com/excel-trim-function/)
 is used to [remove extra spaces from text](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
, in this case, it takes the number and returns that number as is.

You can also use any of the below formulas:

\=[UPPER](https://trumpexcel.com/excel-upper-function/)
(A2)

Or

\=[LOWER](https://trumpexcel.com/excel-lower-function/)
(A2)

So these are some of the methods you can use to convert numbers that are being shown in scientific notation to show the full numbers.

If the number is 11 digits or less, you can use the first two methods.

If the number is more than 11 digits, you can use any one of the methods to convert scientific notation to text (by adding an apostrophe at the beginning of the number or by using formulas such as TRIM or UPPER/LOWER).

I hope you found this Excel tutorial useful!

**Other Excel tutorials you may also like:**

*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [Convert Date to Text in Excel – Explained with Examples](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [How to Display Numbers as Fractions (Write Fractions in Excel)](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    
*   [Convert Number to Words in Excel](https://trumpexcel.com/number-to-words-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-scientific-notation-to-number-text/#respond)

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