# How to Use Excel SEARCH Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-search-function

---

[Skip to content](https://trumpexcel.com/excel-search-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-search-function/#below-title)

Excel SEARCH Function (Example + Video)
---------------------------------------

![Excel SEARCH Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20327'%3E%3C/svg%3E)

### When to use Excel SEARCH Function

Excel SEARCH function can be used when you want to locate a text string within another text string and find its position.

### What it Returns

It returns a number that represents the starting position of the string you are finding in another string.

### Syntax

\=SEARCH(find\_text, within\_text, \[start\_num\])

### Input Arguments

*   find\_text – the text or string that you need to find.
*   within\_text – the text within which you want to find the find\_text argument.
*   \[start\_num\] – a number that represents the position from which you want the search to begin. If you omit it, it starts from the beginning.

### Additional Notes

*   If the start number is not specified, then it starts looking from the beginning of the string.
*   SEARCH function is not **_case-sensitive._** If you want to do a case-sensitive search, use [FIND function](https://trumpexcel.com/excel-find-function/)
    .
*   SEARCH function **_can handle wildcard characters._**
    *   There are three [wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
         in Excel – the question mark (?), asterisk (\*), and tilde (~).
        *   A question mark matches any single character.
        *   An asterisk matches any sequence of characters.
        *   If you want to find an actual question mark or asterisk, type a tilde (**~**) before the character.
*   It returns a #VALUE! error if the searched string is not found in the text.

Excel SEARCH Function – Examples
--------------------------------

Here are four examples of using Excel SEARCH function:

### **#1 Searching for a Word in a Text String (from the beginning)**

![Excel Search Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20718%20221'%3E%3C/svg%3E)

In the above example, when you search for the word good in the text Good Morning, it returns 1, which is the position of the starting point of the searched word.

Note that Excel SEARCH function is not case sensitive. So you get the same result whether you use good, Good, or GOOD.

If you are looking for a case sensitive search, use Excel FIND function.

### **#2 Searching for a Word in a Text String (with a specified beginning)**

![Excel Search Function - Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20771%20268'%3E%3C/svg%3E)

The third argument in the SEARCH function is the position within the text from where you want to start the search. In the example above, the function returns 1 when you search for the text good in Good Morning and the starting position is 1.

However, it returns an error when you make it start at 2. Hence, it looks for the text good in ood Morning. Since it can not find it, it returns an error.

Note: If you skip the last argument and don’t provide the starting position, by default it takes it as 1.

### **#3 When there are Multiple Occurrence of the Searched Text**

![Excel Search Function - Example 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20768%20284'%3E%3C/svg%3E)

Excel SEARCH function starts looking in the specified text from the specified position. In the above example, when you look for the text good in Good Good Morning with the starting position as 1, it returns 1, as it finds it at the beginning.

When you start the search from the second character onwards, it returns 6, as it finds the matching text at the sixth position.

###  **#4 Using Wildcard Characters in Excel Search Function**

![Excel Search Function - Example 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20193'%3E%3C/svg%3E)

Excel SEARCH Function can also handle wildcard characters. In the above example, the searched text is c\*l, which means any text string that beings with c and end with l and can have any number of characters in between. In Excel, it finds the searched string at the third position (Ex**cel**) and returns 3.

Excel SEARCH Function – Video Tutorial
--------------------------------------

**Related Excel Functions:**

*   [Excel FIND Function](https://trumpexcel.com/excel-find-function/)
    .
*   [Excel LOWER Function](https://trumpexcel.com/excel-lower-function/)
    .
*   [Excel UPPER Function](https://trumpexcel.com/excel-upper-function/)
    .
*   [Excel PROPER Function](https://trumpexcel.com/excel-proper-function/)
    .
*   [Excel REPLACE Function](https://trumpexcel.com/excel-replace-function/)
    .
*   [Excel SUBSTITUTE Function](https://trumpexcel.com/excel-substitute-function/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [Search and Highlight Data Using Conditional Formatting](https://trumpexcel.com/search-highlight-using-conditional-formatting/)
    .
*   [Create Dynamic Filter in Excel](https://trumpexcel.com/dynamic-excel-filter/)
    .
*   [Create Drop Down List with Search Suggestions](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [Separate First and Last Name in Excel](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [Check IF Cell Contains Partial Text in Excel](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-search-function/#respond)

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