# How to Use Excel FIND Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-find-function

---

[Skip to content](https://trumpexcel.com/excel-find-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-find-function/#below-title)

Excel FIND Function (Example + Video)
-------------------------------------

![Excel FIND Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20330'%3E%3C/svg%3E)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-find-function/#)

### When to use Excel FIND Function

Excel FIND function can be used when you want to locate a text string within another text string and find its position.

### What it Returns

It returns a number that represents the starting position of the string you are finding in another string.

### Syntax

\=FIND(find\_text, within\_text, \[start\_num\])

### Input Arguments

*   find\_text – the text or string that you need to find.
*   within\_text – the text within which you want to find the find\_text argument.
*   \[start\_num\] – a number that represents the position from which you want the search to begin. If you omit it, it starts from the beginning.

### Additional Notes

*   If the start number is not specified, then it starts looking from the beginning of the string.
*   Excel FIND function is **_case-sensitive._** If you want to do a case-insensitive search, use [Excel SEARCH function](https://trumpexcel.com/excel-search-function/)
    .
*   Excel FIND function **_cannot handle [wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
    ._** If you want to use wildcard characters, use the Excel SEARCH function.
*   It returns a #VALUE! error if the searched string is not found in the text.

Excel FIND Function – Examples
------------------------------

Here are four examples of using Excel FIND function:

### Searching for a Word in a Text String (from the beginning)

![Excel FIND Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20716%20230'%3E%3C/svg%3E)

In the above example, when you look for the word Good in the text Good Morning, it returns 1, which is the position of the starting point of the searched word.

Note that Excel FIND function is case-sensitive. When you use good instead of Good, it returns a #VALUE! error.

If you are looking for a case-insensitive search, use Excel SEARCH function.

### Finding a Word in a Text String (with a specified beginning)

![Excel FIND Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20717%20257'%3E%3C/svg%3E)

The third argument in the FIND function is the position within the text from where you want to start the search. In the example above, the function returns 1 when you search for the text Good in Good Morning and the starting position is 1.

However, it returns an error when you make it start at 2. Hence, it looks for the text Good in ood Morning. Since it can not find it, it returns an error.

_Note: If you skip the last argument and don’t provide the starting position, by default it takes it as 1._

### When there are Multiple Occurrence of the Searched Text

![Excel FIND Function - Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20719%20285'%3E%3C/svg%3E)

Excel FIND function starts looking in the specified text from the specified position. In the above example, when you look for the text Good in Good Good Morning with the starting position as 1, it returns 1, as it finds it at the beginning.

When you start the search from the second character onwards, it returns 6, as it finds the matching text at the sixth position.

### Extracting Everything to the Left a Specified Character/String

Suppose you have the email ids do some superheroes as shown below and you want to extract only the username part (which would be the characters before the @).

![Extract Usernames using Excel FIND Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20205'%3E%3C/svg%3E)

Below is the formula that will find the position of ‘@’ in each email id and extract all the characters to the left of it:

\=LEFT(A2,FIND(“@”,A2,1)-1)

![Extracting the usernames using FIND and LEFT functions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20542%20250'%3E%3C/svg%3E)

The FIND function in this formula gives the position of the ‘@’ character. The [LEFT function](https://trumpexcel.com/excel-left-function/)
 that uses this position to extract the username.

For example, in the case of brucewayne@batman.com, the FIND function returns 11. LEFT function then uses FIND(“@”,A2,1)-1 as the second argument to get the username.

Note that 1 is subtracted from the value returned by the FIND function as we want to exclude the @ from the result of the LEFT function.

Excel FIND Function – VIDEO
---------------------------

**Related Excel Functions:**

*   [Excel LOWER Function](https://trumpexcel.com/excel-lower-function/)
    .
*   [Excel UPPER Function](https://trumpexcel.com/excel-upper-function/)
    .
*   [Excel PROPER Function](https://trumpexcel.com/excel-proper-function/)
    .
*   [Excel REPLACE Function](https://trumpexcel.com/excel-replace-function/)
    .
*   [Excel SEARCH Function](https://trumpexcel.com/excel-search-function/)
    .
*   [Excel SUBSTITUTE Function](https://trumpexcel.com/excel-substitute-function/)
    .

**You May Also Like the Following Tutorials:**

*   [How to Quickly Find and Remove Hyperlinks in Excel](https://trumpexcel.com/find-hyperlinks-in-excel/)
    .
*   [How to Find Merged Cells in Excel.](https://trumpexcel.com/find-merged-cells/)
    
*   [How to Find and Remove Duplicates in Excel.](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    
*   [Using Find and Replace in Excel](https://trumpexcel.com/find-and-replace-in-excel/)
    .
*   [Check IF Cell Contains Partial Text in Excel](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-find-function/#respond)

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