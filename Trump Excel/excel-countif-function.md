# How to Use Excel COUNTIF Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-countif-function

---

[Skip to content](https://trumpexcel.com/excel-countif-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-countif-function/#below-title)

Simple calculation such as adding the values in a range of cells or counting the values in reach of cells is something that you would have to do when working with data in Excel.

And in some cases, you may have to count only those cells that meet a specific criterion.

And you can easily do that with the **COUNTIF function in Excel**

In this tutorial, I will show you how the Excel COUNTIF function works with simple examples add a detailed explanation

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-countif-function/#)

Let’s first look at the syntax of the COUNTIF function:

Excel COUNTIF Function Syntax
-----------------------------

\=COUNTIF(range, criteria)

where

*   **range** is the range of cells where you want to count cells that meet the condition
*   **criteria** is the condition that must be evaluated against the range of cells for a cell to be counted.

Excel COUNTIF Function Examples
-------------------------------

Now let’s have a look at some examples that will show you how to use the COUNTIF function in Excel.

### Count Cells With a Specific Text String

With the COUNTIF function, you can count all the cells that contain a specific text string.

Suppose you have a dataset as shown below and you want to count all the cells that have the text Printer in it.

![Dataset for counting text and greater less than](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20452'%3E%3C/svg%3E)

Here is the formula that will do this:

\=COUNTIF(A2:A9,"Printer")

![COUNTIF Formula to count the number of times printer repeats](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20504'%3E%3C/svg%3E)

The above formula uses the text I specified as the second argument as the criteria and counts all the cells that have the same text (which is “Printer”)

In this example, I have manually entered the criteria text, but you can also refer to a cell that contains the criteria text.

Note: Criteria text in the COUNTIF formula is not case sensitive. So I can also use ‘printer’ or ‘PRINTER’, as the result would still be the same

### Count Cells Value Greater than or Less than

Just like I used the COUNTIF function with text, I can also use it with cells containing numbers.

Suppose I have a dataset as shown below and I want to count all the cells where the number in column B is greater than 30.

![Dataset for counting text and greater less than](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20452'%3E%3C/svg%3E)

Below is the formula that will do this:

\=COUNTIF(B2:B10,">30")

![COUNTIF formula to count cells with value greater than 30](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20737'%3E%3C/svg%3E)

The above formula uses the greater than an operator with the number as the criteria. This tells Excel to only consider those cells where the value is more than 30.

You can also use other operators such as less than (<). equal to (=), and not equal to (<>) in the COUNTIF criteria.

### Count Cells that Contain Text String

While there is the [COUNTA function](https://trumpexcel.com/excel-functions/counta-function/)
 that counts the cells that contain numbers, there is no in-built formula that can count only those cells that contain a text string.

But it can easily be done using the COUNTIF function.

Suppose you have a dataset as shown below and you only want to count the number of cells that are text (and ignore the numbers).

![Dataset to count text cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20379'%3E%3C/svg%3E)

Here is the formula that will do this:

\=COUNTIF(A2:A10,"\*")

![formula to count cells that contain text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20577'%3E%3C/svg%3E)

The above formula uses an asterisk (which is a [wildcard character](https://trumpexcel.com/excel-wildcard-characters/)
). An asterisk represents the text of any length.

So this criteria would count all the cells where there is any text string (of any length). In case the cells are empty/blank or have numbers in them, then those would not be counted.

Some Additional Notes
---------------------

*   Criteria could be a number, expression, cell reference, text, or a formula.
    *   Criteria which are text or mathematical/logical symbols (such as =,+,-,/,\*) should be in double-quotes.
*   Wildcard characters can be used in criteria.
    *   There are three wildcard characters in Excel – the question mark (?), an asterisk (\*), and tilde (~)
        *   A question mark (?) matches any single character
        *   An asterisk matches (\*) any sequence of characters.
        *   If you want to find an actual question mark or asterisk, type a tilde (**~**) before the character.
*   Criteria are case-insensitive (“Hello” and “hello” are treated as the same).

**Related Excel Functions:**

*   [Excel COUNT Function](https://trumpexcel.com/excel-count-function/)
    .
*   [Excel COUNTBLANK Function](https://trumpexcel.com/excel-countblank-function/)
    .
*   [Excel COUNTIFS Function](https://trumpexcel.com/excel-countifs-function/)
    
*   [Excel Functions](https://trumpexcel.com/excel-functions/)
    

**You May Also Like the Following Tutorials:**

*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    .
*   [Using Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    
*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    
*   [Count Cells Less than a Value in Excel (COUNTIF Less Than)](https://trumpexcel.com/countif-less-than/)
    
*   [How to Count Colored Cells In Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [Count Characters in a Cell (or Range of Cells) Using Formulas in Excel](https://trumpexcel.com/count-characters-in-excel/)
    
*   [Count Between Two Numbers in Excel](https://trumpexcel.com/count-between-two-numbers-excel/)
    
*   [Prevent Duplicate Entries in Excel](https://trumpexcel.com/prevent-duplicate-entries-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-countif-function/#respond)

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