# How to Use Excel LEN Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-len-function

---

[Skip to content](https://trumpexcel.com/excel-len-function/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-len-function/#below-title)

Excel LEN Function (Example + Video)
------------------------------------

![Excel Len Function](https://trumpexcel.com/wp-content/uploads/2014/03/LEN-FORMULA-EXCEL.png)

### When to use Excel LEN Function

LEN function can be used when you want to get the total number of characters in a specified string. This is useful when you want to know the length of a string in a cell.

### What it Returns

It returns a number that represents the number of characters in the specified string.

### Syntax

\=LEN(text)

### Input Arguments

*   text – the string for which you want to find the number of characters. 

### Additional Notes

*   Spaces are [counted as characters](https://trumpexcel.com/count-characters-in-excel/)
    . So if you have leading/trailing spaces, or spaces between words, then these will be counted as one character. To remove leading, trailing, and double spaces, use the [TRIM function](https://trumpexcel.com/excel-trim-function/)
    .
*   It also works with numbers and treats numbers as text.
    *   In case of numbers, formatting does not change the number of characters. For example, if 1000 is formatted as $1,000 or 1,000.00, the LEN function would still return 4.

Excel LEN Function Examples
---------------------------

Following are some useful examples of using the LEN function in Excel.

### Example 1 – To get the Length of a Text String

If you have some text in cell A1 and you want to quickly know the total number of characters in it, you can use the following function:

\=LEN(A1)

![Len Function in Excel - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20147'%3E%3C/svg%3E)

In the above example, there are a total of 43 characters – including spaces.

### Example 2 – Using LEN Function with TRIM and CLEAN

Sometimes, you may get a dataset that has extra spaces in between words or at the beginning/ending of the text string. In such cases, if you use the LEN function, it will also count the number of spaces.

To avoid this to happen, you can use LEN function along with the TRIM function.

Below is an example where you can see that while the text looks the same, the result of LEN function is different in each case as there are trailing spaces in it.

![Len Function in Excel - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20619%20185'%3E%3C/svg%3E)

The following formula will get rid of any extra spaces as well as leading/trailing spaces:

\=LEN(TRIM(A1))

In the above example, while the trailing spaces are still there is A2 and A3, but since we have used TRIM, it removes these spaces before the length of the text is counted by the LEN function.

### Example 3 – Counting the Number of Words in a Sentence

You can use the LEN function to count the number of words in a text string.

This can be done by counting the number of spaces between words. If I know the number of spaces in between words, then I can add 1 to it and that will be the number of words in the sentence.

For example, in the text – “Good Morning”, there is one space and two words.

Below is the formula that will give the word count:

\=LEN(TRIM(A1))-LEN(SUBSTITUTE(A1," ",""))+1

![Len Function in Excel - word count](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20677%20130'%3E%3C/svg%3E)

The above formula counts:

*   The total number of characters and
*   The total number of characters without spaces.

It then subtracts these two to get the number of spaces, and then add 1 to it.

Note that you need to use TRIM in the first part of the formula to make sure any extra spaces are not counted (only the single spaces between words).

Excel LEN Function – Video Tutorial
-----------------------------------

**Related Excel Functions:**

*   [Excel CONCATENATE Function](https://trumpexcel.com/excel-concatenate-function/)
    .
*   [Excel LEFT Function](https://trumpexcel.com/excel-left-function/)
    .
*   [Excel MID Function](https://trumpexcel.com/excel-mid-function/)
    .
*   [Excel REPT Function](https://trumpexcel.com/excel-rept-function/)
    .
*   [Excel RIGHT Function](https://trumpexcel.com/excel-right-function/)
    .
*   [Excel TEXT Function](https://trumpexcel.com/excel-text-function/)
    .
*   [Excel TRIM Function](https://trumpexcel.com/excel-trim-function/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [How to Count the Number of Words in Excel](https://trumpexcel.com/word-count-in-excel/)
    .
*   [Find the Position of the Nth Occurrence of a Character in a String in Excel](https://trumpexcel.com/find-characters-last-position/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-len-function/#respond)

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