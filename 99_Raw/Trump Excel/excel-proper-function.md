# How to Use Excel PROPER Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-proper-function

---

[Skip to content](https://trumpexcel.com/excel-proper-function/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-proper-function/#below-title)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-proper-function/#)

In Excel. you can quickly change the case of the text in a cell (to lower case, upper case, or proper case) using [text functions](https://trumpexcel.com/excel-functions/)
.

Below is an example of each type of case:

![Lower Case, Upper Case, Proper Case - Example Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20143'%3E%3C/svg%3E)

Excel PROPER Function – Overview
--------------------------------

PROPER function is one of the many text functions in Excel.

### What Does it Do?

It takes a string as the input and returns a string where the first letter of all the words has been capitalized and all the remaining characters are in lower case.

### When to Use it?

Use it when you have a text string and you want to capitalize the first alphabet of each word in the text string and make all the other character in lowercase. This could be the case when you have names in different formats and you want to make it consistent by capitalizing the first alphabet of the first and the last name.

### Proper Function Syntax

\=PROPER(text)

*   **text –** the text string in which you want in capitalize the first letter of each word.

Examples of using PROPER Function
---------------------------------

Here are some practical examples to show you how to the PROPER function in an Excel worksheet.

### Example 1 – Making Names Consistent

Suppose you have the dataset as shown below:

![Excel Proper Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20191'%3E%3C/svg%3E)

The names in this dataset are all inconsistent.

You can use the PROPER function to make these consistent (where the first alphabet of each name is capitalized and rest all are small).

The below formula would do this:

\=PROPER(A2&" "&B2)

![Result Proper function in Excel - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20572%20192'%3E%3C/svg%3E)

In the above formula, I use the ampersand operator to add the text in cells in column A and B, and then PROPER function makes the combined string consistent.

### Example 2 – Making Address Consistent

Just like the names, you can also use it to make the address consistent.

Below is an example dataset where the addresses are in an inconsistent format:

![Dataset for Proper formula Excel - example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20220'%3E%3C/svg%3E)

You can use the below formula to make all these addresses in a consistent format:

\=PROPER(A2)

Note that this formula works perfectly, but if you want the state code (such CA, NV, NY) in upper case, it will not be done with PROPER function only.

In that case, you need to use the below formula:

\=PROPER(LEFT(A2,FIND("@",SUBSTITUTE(A2,",","@",LEN(A2)-LEN(SUBSTITUTE(A2,",",""))),1)))&RIGHT(A2,LEN(A2)-FIND("@",SUBSTITUTE(A2,",","@",LEN(A2)-LEN(SUBSTITUTE(A2,",",""))),1))

You can get an idea of how this formula works [from this tutorial](https://trumpexcel.com/find-characters-last-position/)
.

The PROPER function works by analyzing non-text characters in a string. When it finds a non-text character, it capitalizes the next following character. While this works great in most of the cases, in some scenarios, this may not work as expected. For example, if you use the formula on the text – **it’s awesome** – it will give you the result as **It’S Awesome**. As it capitalizes the character after the non-text character, it does that with an apostrophe in this case.

**Some useful things to know about the PROPER Function:**

1.  The PROPER function only affects the first character of every word in a text string. All the other characters are left unchanged.
2.  It [capitalizes the first letter](https://trumpexcel.com/capitalize-first-letter-excel/)
     of any word that follows a non-text character. For example: **\=PROPER(hello,excel)** returns **Hello,Excel**
3.  Numbers, special characters, and punctuations are not changed by the PROPER function.
4.  If you use a null character (or a reference to an empty cell), it will return a null character.

**Other Useful Excel Functions:**

*   **[Excel FIND Function](https://trumpexcel.com/excel-find-function/)
    **: Excel FIND function can be used when you want to locate a text string within another text string and find its position. It returns a number that represents the starting position of the string you are finding in another string. It is case-sensitive.
*   [**Excel LOWER Function**:](https://trumpexcel.com/excel-lower-function/)
     Excel LOWER function can be used when you want to convert all uppercase letter in a text string to lowercase. Numbers, special characters, and punctuations are not changed by it.
*   [**Excel UPPER Function**:](https://trumpexcel.com/excel-upper-function/)
     Excel UPPER function can be used when you want to convert all lowercase letter in a text string to uppercase. Numbers, special characters, and punctuations are not changed by it.
*   [**Excel REPLACE Function**](https://trumpexcel.com/excel-replace-function/)
    : Excel REPLACE function can be used when you want to replace a part of the text string with another string. It returns a text string where a part of the text has been replaced by the specified string.
*   [**Excel SEARCH Function**](https://trumpexcel.com/excel-search-function/)
    : Excel SEARCH function can be used when you want to locate a text string within another text string and find its position. It returns a number that represents the starting position of the string you are finding in another string. It is NOT case-sensitive.
*   [**Excel SUBSTITUTE Function**](https://trumpexcel.com/excel-substitute-function/)
    : Excel SUBSTITUTE function can be used when you want to substitute text with new specified text in a string. It returns a text string where an old text has been substituted by the new one.

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Excel PROPER Function (Useful Examples + Video)”
---------------------------------------------------------------

1.  Thanks!  
    How do I make Proper() to fix the text it returned and not the formula? e.g. If I say Proper (A2) and excel returns the text in A2. After that if I delete cell A2, the returned text also disappears. How do I make sure it stays?
    
    [Reply](https://trumpexcel.com/excel-proper-function/#comment-11459)
    
2.  Well done. Clear and easily understood.
    
    [Reply](https://trumpexcel.com/excel-proper-function/#comment-10686)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-proper-function/#respond)

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