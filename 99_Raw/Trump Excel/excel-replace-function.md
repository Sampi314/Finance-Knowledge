# How to Use Excel REPLACE Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-replace-function

---

[Skip to content](https://trumpexcel.com/excel-replace-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-replace-function/#below-title)

In this tutorial, I will show you how to use the REPLACE function in Excel (with examples).

![Excel REPLACE Function](https://trumpexcel.com/wp-content/uploads/2014/03/REPLACE-FORMULA-EXCEL.png)

Replace is a text function that allows you to quickly replace a string or a part of the string with some other text string.

This can be really useful when you’re working with a large dataset and you want to replace or remove a part of the string. But the real power of the replace function can be unleashed when you use it with other formulas in Excel (as we will in the examples covered later in this tutorial).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-replace-function/#)

Before I show you the examples of using the function, let me quickly cover the syntax of the REPLACE function.

Syntax of the REPLACE Function
------------------------------

\=REPLACE(old\_text, start\_num, num\_chars, new\_text)

**Input Arguments**

*   **old\_text** – the text that you want to replace.
*   **start\_num** – the starting position from where the search should begin.
*   **num\_chars** – the number of characters to replace.
*   **new\_text** – the new text that should replace the old\_text.

Note that the Start Number and Number of Characters argument cannot be negative.

Now let’s have a look at some examples to see how the REPLACE function can be used in Excel.

Example 1 – Replace Text with Blank
-----------------------------------

Suppose you have the following data set and you want to replace the text “ID-” and only want to keep the numeric part.

![Replace ID from the text - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20338'%3E%3C/svg%3E)

You can do this by using the following formula:

\=REPLACE(A2,1,3,"")

The above formula replaces the first three characters of the text in each cell with a blank.

![Replace formula to replace text with a blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20474%20392'%3E%3C/svg%3E)

Note: The same result can also be achieved by other techniques such as using the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
 or by extracting the text to the right of the dash by using the combination of RIGHT and FIND functions.

Example 2: Extract the User Name from the Domain name
-----------------------------------------------------

Suppose you have a dataset as shown below and you want to remove the domain part (the one that follows the @ sign).

![Email Dataset for Replace Function Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20543%20198'%3E%3C/svg%3E)

To do this, you can use the below formula:

\=REPLACE(A2,FIND("@",A2),LEN(A2)-FIND("@",A2)+1,"")

![Formula to get the username from an email](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20738%20255'%3E%3C/svg%3E)

The above function uses a combination of REPLACE, LEN and FIND function.

It first uses the FIND function to get the position of the @. This value is used as the Start Number argument and I want to [remove the entire text](https://trumpexcel.com/remove-text-before-after-character-excel/)
 string starting from the @ sign.

Another thing I need to remove this string is the total number of characters after the @ so that I can specify these many characters to be replaced with a blank. This is where I have used the formula combination of LEN and FIND.

Pro Tip: In the above formula, since I want to remove all the characters after the @ sign, I don’t really need the number of characters. I can specify any large number (which is greater than the number of characters after the @ sign), and I will get the same result. So I can even use the following formula: =REPLACE(A2,FIND(“@”,A2),LEN(A2),””)

Example 3: Replace One Text String with Another
-----------------------------------------------

In the above two examples, I showed you how to extract a part of the string by replacing the remaining with blank.

Here is an example where you change one text string with another.

Suppose you have the below dataset and you want to change the domain from example.net to example.com.

![replace domain name TLDs](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20542%20200'%3E%3C/svg%3E)

You can do this using the below formula:

\=REPLACE(A2,FIND("net",A2),3,"com")

![Replace domain TLD using the formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20254'%3E%3C/svg%3E)

Difference between Replace and Substitute functions
---------------------------------------------------

There is a major difference in the usage of the REPLACE function and the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
 (although the result expected from these may be similar).

The REPLACE function requires the position from which it needs to start replacing the text. It then also requires the number of characters you need to replace with the new text. This makes REPLACE function suitable where you have a clear pattern in the data and want to replace text.

A good example of this could be when working with email ids or address or ids – where the construct of the text is consistent.

SUBSTITUTE function, on the other hand, is a little more versatile. You can use it to replace all the instances of an occurrence of a string with some other string.

For example, I can use it to replace all the occurrence of character Z with J in a text string. And at the same time, it also gives you the flexibility to only change a specific instance of the occurrence (for example, only substitute the first occurrence of the matching string or only the second occurrence).

Note: In many cases, you can do away with using the REPLACE function and instead use the FIND and REPLACE functionality. It will allow you to change the data set without using the formula and getting the result in another column/row. REPLACE function is more suited when you want to keep the original dataset and also want the resulting data to be dynamic (such that updates in case you change the original data).

Excel REPLACE Function – Video Tutorial
---------------------------------------

**Related Excel Functions:**

*   [Excel FIND Function](https://trumpexcel.com/excel-find-function/)
    .
*   [Excel LOWER Function](https://trumpexcel.com/excel-lower-function/)
    .
*   [Excel UPPER Function](https://trumpexcel.com/excel-upper-function/)
    .
*   [Excel PROPER Function](https://trumpexcel.com/excel-proper-function/)
    .
*   [Excel SEARCH Function](https://trumpexcel.com/excel-search-function/)
    .

**You may also like the following Excel Tutorials:**

*   [How to Remove the First Character from a String in Excel](https://trumpexcel.com/remove-first-character-from-string/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-replace-function/#respond)

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