# How to Use Excel TRIM Function to Remove Spaces and Clean Data

**Source:** https://trumpexcel.com/excel-trim-function

---

[Skip to content](https://trumpexcel.com/excel-trim-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-trim-function/#below-title)

Excel TRIM Function – An Overview
---------------------------------

![Excel TRIM Function - Explaination](https://trumpexcel.com/wp-content/uploads/2017/01/Excel-Trim-Function-image.png)

### When to use Excel TRIM Function

Excel TRIM Function is best suited for situations when you need to [clean the dataset](https://trumpexcel.com/clean-data-in-excel/)
 by [removing leading, trailing, and double spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
.

### What it Returns

It returns the text string where all the leading, trailing, and double spaces have been removed.

### Syntax

\=TRIM(text)

### Input Arguments

*   Here, ‘text’ is the text string from which you want to remove the extra spaces. This could either be entered manually (within double quotes) or can be a cell reference that contains the text string. For example, if you want to remove extra spaces from the text in cell A1, then you can use the formula =TRIM(A1)

Excel TRIM Function – Examples
------------------------------

The best way to understand how useful Excel TRIM function can be would be to see it in action.

Here are three practical examples of using the TRIM function.

### Example 1 – Remove Leading, Trailing, and Double Spaces

TRIM function is made to do this.

Below is an example where there are leading, trailing, and double spaces in the cells.

![Excel TRIM Function - Data set Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20169'%3E%3C/svg%3E)

You can easily remove all these extra spaces by using the below TRIM function:

\=TRIM(A1)

Copy-paste this into all the cells and you are all set.

### ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20853%20205'%3E%3C/svg%3E)  
Example 2 – Remove Leading Spaces Only

In some cases, you may want to get rid of only the leading spaces and not the rest.

For example, below I have a list of addresses where there is a double space between the different parts of the address (done to increase the readability). However, there are also some leading spaces (in row 2 and 4).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20580%20158'%3E%3C/svg%3E)

If you use the TRIM function on this, it will remove the leading spaces, but it will also remove the double spaces that we have intentionally placed.

Here is the formula that will remove only the leading spaces from this dataset:

\=RIGHT(A1,LEN(A1)-FIND(MID(TRIM(A1),1,1),A1)+1)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20787%20187'%3E%3C/svg%3E)

**How does this formula work?**

Let me break it down for you:

*   MID(TRIM(A1),1,1) – This part of the formula will give you the first character of the address (after removing the leading spaces). For example, in the case of second address (3344 Better Street), there are leading spaces, but this formula would return 3.
*   FIND(MID(TRIM(A1),1,1),A1) – This part of the formula would find the position of the first character in the address. For example, in the second address, 3 is in the third position (as there are two leading spaces before it).
*   LEN(A1)-FIND(MID(TRIM(A1),1,1),A1)+1 – This part of the formula would give you the total length of the address after removing the leading spaces.
*   \=RIGHT(A1,LEN(A1)-FIND(MID(TRIM(A1),1,1),A1)+1) – This would give you the result where it extracts all the characters after the leading spaces.

On similar lines, you can create formulas that can remove only the trailing, or only leading and trailing spaces from the text.

### Example 3 – Correctly Count Number of words when there are Additional spaces

Spaces in a text is also an indication of the [word count](https://trumpexcel.com/word-count-in-excel/)
 in it.

For example, if you want to count the total number of words in the phrase – “The quick brown fox jumps over the lazy dog”, you can simply count the spaces in between the words and add 1 to it.

Here is the formula you can use to count words:

\=LEN(A1)-LEN(SUBSTITUTE(A1," ",""))+1

This formula substitutes all the spaces with blanks and then counts the number of spaces in the text and add 1 to it.

However, when you have additional spaces in the text, this [formula would not work](https://trumpexcel.com/excel-formulas-not-working/)
.

Here is the formula that you should use in such a case:

\=LEN(TRIM(A1))-LEN(SUBSTITUTE(A1," ",""))+1

The TRIM part of the formula in this takes care of the additional spaces.

**Related Excel Functions:**

*   [Excel CONCATENATE Function](https://trumpexcel.com/excel-concatenate-function/)
    .
*   [Excel LEFT Function](https://trumpexcel.com/excel-left-function/)
    .
*   [Excel LEN Function](https://trumpexcel.com/excel-len-function/)
    .
*   [Excel MID Function](https://trumpexcel.com/excel-mid-function/)
    .
*   [Excel REPT Function](https://trumpexcel.com/excel-rept-function/)
    .
*   [Excel RIGHT Function](https://trumpexcel.com/excel-right-function/)
    .
*   [Excel TEXT Function](https://trumpexcel.com/excel-text-function/)
    .
*   [VBA TRIM Function](https://trumpexcel.com/vba-trim/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-trim-function/#respond)

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