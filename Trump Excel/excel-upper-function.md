# How to Use Excel UPPER Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-upper-function

---

[Skip to content](https://trumpexcel.com/excel-upper-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-upper-function/#below-title)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-upper-function/#)

In Excel. there are [text functions](https://trumpexcel.com/excel-functions/)
 that allow you to quickly change the case of the text (to lower case, upper case, or proper case).

Below is an example of each type of case:

![Lower Case, Upper Case, Proper Case - Example Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20143'%3E%3C/svg%3E)

Excel UPPER Function – Overview
-------------------------------

UPPER function is one of the many text function in Excel.

### What does it do?

It takes a string as the input and converts all the lower case characters in that text string to upper case.

### When to Use it?

Use it when you have a text string and you want to convert it all characters into upper case. This can often be the case when you get the data from an external source and you want to clean it and make it consistent.

One example of this could be when you have Product Ids in inconsistent format and you want to make it all in upper case.

### UPPER Function Syntax

\=UPPER(text)

*   text: This is the text string in which you want to convert lower case characters to upper case.

Examples of Using Excel Upper Function
--------------------------------------

Here are some practical examples to show you how to use the UPPER function in an Excel worksheet.

### Example 1 – Convert text in all Cells into Uppercase

Suppose you have a dataset as shown below where you want to make it consistent and make all the cells text in uppercase.

![Excel UPPER Function - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20303%20169'%3E%3C/svg%3E)

The below formula would convert all the lowercase characters into the upper case:

\=UPPER(A2)

![Excel Upper Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20227'%3E%3C/svg%3E)

### Example 2 – Combine Cells While Keeping one Part in Upper Case

Suppose you have the address data as shown below and you want to [combine this data](https://trumpexcel.com/combine-cells-in-excel/)
.

![Excel Upper Function - Example 2 dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20196'%3E%3C/svg%3E)

Since the state code is in lower case, you can use the combination of [TextJoin](https://trumpexcel.com/concatenate-excel-ranges/)
 and Upper formula to combine and get the address with state codes in upper case.

Below is the formula that would do this:

\=TEXTJOIN(", ",TRUE,A2,B2,UPPER(C2))

![Excel Upper Function with textjoin](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20783%20255'%3E%3C/svg%3E)

If you’re using a version where TextJoin function is not available, you can use the below formula (which uses the [CONCATENATE function](https://trumpexcel.com/excel-concatenate-function/)
):

\=CONCATENATE(A2,", ",B2,", ",UPPER(C2))

**Some useful things to know about the UPPER Function:**

1.  Numbers, special characters, and punctuations are not changed by the Upper function.
2.  The UPPER function only affects the lowercase characters of the text string. Any character other than the lowercase text characters is left unchanged.
3.  If you use a null character (or a reference to an empty cell), it will return a null character.

**Other Useful Excel Functions:**

*   [Excel FIND Function](https://trumpexcel.com/excel-find-function/)
     – The FIND function finds a text string within another text string and returns its position
*   [Excel Lower Function](https://trumpexcel.com/excel-lower-function/)
    . – The Lower function converts a given text string from upper case to lower case. Numbers, punctuations, and special characters are not changed.
*   [Excel PROPER Function](https://trumpexcel.com/excel-proper-function/)
    . – The PROPER function converts a given text string to the proper case (where the first letter of [each word is capitalized](https://trumpexcel.com/capitalize-first-letter-excel/)
    ). Numbers, punctuations, and special characters are not changed
*   [Excel TRIM Function](https://trumpexcel.com/excel-trim-function/)
     – The TRIM function removes leading, trailing, and double spaces from a text string.
*   [Excel LEN Function](https://trumpexcel.com/excel-len-function/)
    : It counts the total number of characters in a cell. It’s commonly used to get the length of a text string.

**Similar Function in VBA:**

*   [VBA UCase Function](https://trumpexcel.com/vba-ucase/)
     – It converts a text string to the upper case in VBA.

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-upper-function/#respond)

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