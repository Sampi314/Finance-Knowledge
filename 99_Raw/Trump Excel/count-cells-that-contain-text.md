# How to Count Cells that Contain Text Strings in Excel

**Source:** https://trumpexcel.com/count-cells-that-contain-text

---

[Skip to content](https://trumpexcel.com/count-cells-that-contain-text/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-cells-that-contain-text/#below-title)

**Watch Video – How to Count Cells that Contain Text Strings**

Counting is one of the most common tasks people do in Excel. It’s one of the metric that is often used to summarize the data.

For example, count sales done by Bob, or sales more than 500K or quantity of Product X sold.

Excel has a variety of count functions, and in most cases, these inbuilt Excel functions would suffice. Below are the count functions in Excel:

*   [COUNT](https://trumpexcel.com/excel-count-function/)
     – To count the number of cells that have numbers in it.
*   [COUNTA](https://trumpexcel.com/excel-functions/counta-function/)
     – To count the number of cells that are not empty.
*   [COUNTBLANK](https://trumpexcel.com/excel-countblank-function/)
     – To count blank cell.
*   [COUNTIF](https://trumpexcel.com/excel-countif-function/)
    /[COUNTIFS](https://trumpexcel.com/excel-countifs-function/)
     – To count cells when the specified criteria are met.

There may sometimes be situations where you need to create a combination of functions to get the counting done in Excel.

One such case is to count cells that contain text strings.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-cells-that-contain-text/#)

Count Cells that Contain Text in Excel
--------------------------------------

Text values can come in many forms. It could be:

*   **Text String**
    *   Text Strings or Alphanumeric characters. Example – Trump Excel or Trump Excel 123.
*   **Empty String**
    *   A cell that looks blank but contains **\=””** or ‘ (if you just type an apostrophe in a cell, it looks blank).
*   **Logical Values**
    *   Example – TRUE and FALSE.
*   **Special characters**
    *   Example – @, !, $ %.

Have a look at the data set shown below:

![Count Cells that Contain Text in Excel Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20246'%3E%3C/svg%3E)

It has all the combinations of text, numbers, blank, special characters, and logical values.

To count cells that contain text values, we will use the wildcard characters:

*   **Asterisk (\*)**: An asterisk represents any number of characters in excel. For example, ex**\*** could mean excel, excels, example, expert, etc.
*   **Question Mark (?)**: A question mark represents one single character. For example, Tr**?**mp could mean Trump or Tramp.
*   **Tilde (~)**: To identify wildcard characters in a string.

_See Also__:_ [Examples of using Wildcard Characters in Excel.](https://trumpexcel.com/excel-wildcard-characters/)

Now let’s create formulas to count different combinations.

### Count Cells that Contain Text in Excel (including Blanks)

Here is the formula:

\=COUNTIF(A1:A11,”\*”)

This formula uses COUNTIF function with a wildcard character in the criteria. Since asterisk (\*) represents any number of characters, it counts all the cells that have text characters in it.

It even counts cells that have an empty string in it (an empty string can be a result of formula returning =”” or a cell that contains an apostrophe). While a cell with empty string looks blank, it is counted by this formula.

Logical Values are not counted.

![Count Cells that Contain Text in Excel Text with blanks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20772%20246'%3E%3C/svg%3E)

Also read: [Check IF Cell Contains Partial Text in Excel](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)

### Count Cells that Contain Text in Excel (excluding Blanks)

Here is the formula:

\=COUNTIF(A1:A11,"?\*")

In this formula, the criteria argument is made up of a combination of two wildcard characters (question mark and asterisk).

This means that there should, at least, be one character in the cell.

This formula does not count cells that contain an empty string (an apostrophe or =””). Since an empty string has no character in it, it fails the criteria and is not counted.

Logical Values are also not counted.

![Count Cells that Contain Text in Excel Text without blanks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20770%20244'%3E%3C/svg%3E)

### Count Cells that Contain Text (excluding Blanks, including Logical Values)

Here is the formula:

\=COUNTIF(A1:A11,"?\*") + SUMPRODUCT(--(ISLOGICAL(A1:A11))

The first part of the formula uses a combination of wildcard characters (\* and ?). This returns the number of cells that have at least one text character in it (counts text and special characters, but does not count cells with empty strings).

The second part of the formula checks for logical values. Excel ISLOGICAL function returns TRUE if there is a logical value and FALSE if there isn’t.

A double negative sign ensures that TRUEs are converted into 1 and FALSEs into 0. Excel [SUMPRODUCT function](https://trumpexcel.com/excel-sumproduct-function/)
 then simply returns the number of cells that have a logical value in it.

![Count Cells that Contain Text in Excel Text with Logical Values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20769%20250'%3E%3C/svg%3E)

These above examples demonstrate how to use a combination of formulas and wildcard characters to count cells. In a similar fashion, you can also construct formulas to find the SUM or AVERAGE of a range of cells based on the data type in it.

**You May Also Like the Following Excel Tutorials:**

*   [Count the Number of Words in a Text String](https://trumpexcel.com/word-count-in-excel/)
    .
*   [Using Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    .
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    .
*   [Count Between Two Numbers in Excel (COUNTIF / COUNTIFS)](https://trumpexcel.com/count-between-two-numbers-excel/)
    
*   [Count Characters in a Cell (or Range of Cells) Using Formulas in Excel](https://trumpexcel.com/count-characters-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to Count Cells that Contain Text Strings”
------------------------------------------------------------

1.  Countif formula not working if need to count selected keyword like | within string.
    
    ID\_code|Tran\_date|Type\_tran|Amount\_Bill\_| \_ |  
    \=COUNTIF(P17,”\*|”)
    
    [Reply](https://trumpexcel.com/count-cells-that-contain-text/#comment-13652)
    
2.  A nice hack for you nerds: formula =COUNTIF(A1:A10,”><") will do the same as =COUNTIF(A1:A10,"?\*")
    
    [Reply](https://trumpexcel.com/count-cells-that-contain-text/#comment-13468)
    
3.  Thank you Sumit, You are a great teacher.. and your tutorial notes and video are well  
    documented. I have certainly learnt something new today. Thank you for sharing….Cathy
    
    [Reply](https://trumpexcel.com/count-cells-that-contain-text/#comment-2417)
    
    *   Thanks for the kind words Cathy.. I am glad you find the tutorials useful 🙂
        
        [Reply](https://trumpexcel.com/count-cells-that-contain-text/#comment-2418)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-cells-that-contain-text/#respond)

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