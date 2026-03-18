# Count Unique Values in Excel Using COUNTIF Function

**Source:** https://trumpexcel.com/count-unique-values-in-excel-countif

---

[Skip to content](https://trumpexcel.com/count-unique-values-in-excel-countif/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-unique-values-in-excel-countif/#below-title)

In this tutorial, you will learn how to count unique values in Excel using formulas ([COUNTIF](https://trumpexcel.com/excel-countif-function/)
 and [SUMPRODUCT](https://trumpexcel.com/excel-sumproduct-function/)
 functions).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-unique-values-in-excel-countif/#)

How to Count Unique Values in Excel
-----------------------------------

Let’s say we have a data set as shown below:

![Count Unique Values in Excel Using COUNTIF Function - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20184%20197'%3E%3C/svg%3E)

For the purpose of this tutorial, I will name the range A2:A10 as NAMES. Going forward we will use this named range in the formulas.

See Also: [How to create Named Ranges in Excel](https://trumpexcel.com/named-ranges-in-excel/)
.

In this data set, there is a repetition in the NAMES range. To get the count of unique names from this dataset (A2:A10), we can use a combination of COUNTIF and SUMPRODUCT functions as shown below:

\=SUMPRODUCT(1/COUNTIF(NAMES,NAMES))

![Count Unique Values in Excel Using COUNTIF Function - Countif Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20244'%3E%3C/svg%3E)

**How does this formula work?**

Let’s break down this formula to get a better understanding:

*   COUNTIF(NAMES,NAMES)
    *   This part of the formula returns an array. In the above example, it would be {2;2;3;1;3;1;2;3;2}. The numbers here indicate how many times a value occurs in the given range of cells.  
        _For example, the name is Bob, which occurs twice in the list, hence it would return the number 2 for Bob. Similarly, Steve occurs thrice and hence 3 is returned for Steve._
*   1/COUNTIF(NAMES,NAMES)
    *   This part of the formula would return an array – {0.5;0.5;0.333333333333333;1;0.333333333333333;1;0.5;0.333333333333333;0.5}  
        Since we have divided 1 by the array, it returns this array.  
        _For example, the first element of the array returned above was 2. When 1 is divided by 2, it returns .5._
*   SUMPRODUCT(1/COUNTIF(NAMES,NAMES))
    *   SUMPRODUCT simply adds all these numbers. Note that if Bob occurs twice in the list, the above array returns .5 wherever Bob name appeared in the list. Similarly, since Steve appears thrice in the list, the array returns .3333333 whenever Steve name appears. When we add the numbers for each name, it would always return 1. And if we add all the numbers, it would return the total count of unique names in the list.

This formula works fine until you don’t have any blank cells in the range. But if you have any blank cells, it would return a #DIV/0! error.

**How to Handle BLANK cells?**

Let’s first understand why it returns an error when there is a blank cell in the range. Suppose we have the data set as shown below (with cell A3 being blank):

![Count Unique Values in Excel Using COUNTIF Function - blank cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20181%20199'%3E%3C/svg%3E)

Now we if use the same formula we used above, the COUNTIF part of the formula returns an array {2;0;3;1;3;1;2;3;1}. Since there is no text in cell A3, its count is returned as 0.

![Count Unique Values in Excel Using COUNTIF Function - Error Array](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20203'%3E%3C/svg%3E)

And since we are dividing 1 by this entire array, it returns a #DIV/0! error.

To handle this [division error](https://trumpexcel.com/div-error-in-excel/)
 in case of blank cells, use the below formula:

\=SUMPRODUCT((1/COUNTIF(NAMES,NAMES&"")))

One change that we have made to this formula is the criteria part of the COUNTIF function. We have used NAMES&”” instead of NAMES. By doing this, the formula would return the count of blank cells (earlier it returned 0 where there was a blank cell).

NOTE: This formula would count blank cells as a unique value and return it in the result.

![Count Unique Values in Excel Using COUNTIF Function - blank cell counte as unique](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20637%20202'%3E%3C/svg%3E)

In the above example, the result should be 5, but it returns 6 as the blank cell is counted as one of the unique values.

Here is the formula that takes care of the blank cells and doesn’t count it in the final result:

\=SUMPRODUCT((NAMES<>"")/COUNTIF(NAMES,NAMES&""))

![Count Unique Values in Excel Using COUNTIF Function - ignore blank cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20637%20234'%3E%3C/svg%3E)

In this formula, instead of 1 as the numerator, we have used NAMES<>””. This returns an array of TRUEs and FALSEs. It returns FALSE whenever there is a blank cell. Since TRUE equates to 1 and FALSE equates to 0 in calculations, blank cells are not counted as the numerator is 0 (FALSE).

Now that we have the basic skeleton of the formula ready, we can go a step further and count different data types.

Also read: [Count Between Two Numbers in Excel (using COUNTIFS)](https://trumpexcel.com/count-between-two-numbers-excel/)

How to Count Unique Values in Excel that are Text  

----------------------------------------------------

We will use the same concept discussed above to create the formula that will only count text values that are unique.

Here is the formula that will count unique text values in Excel:

\=SUMPRODUCT((ISTEXT(NAMES)/COUNTIF(NAMES,NAMES&"")))

All we have done is used the formula ISTEXT(NAMES) as the numerator. It returns TRUE when the cell contains text, and FALSE if it doesn’t. It will not count blank cells, but will count cells that have an empty string (“”).

Also read: [Count Cells Less than a Value in Excel (COUNTIF Less Than)](https://trumpexcel.com/countif-less-than/)

How to Count Unique Values in Excel that are Numeric
----------------------------------------------------

Here is the formula that will count unique numeric values in Excel

\=SUMPRODUCT((ISNUMBER(NAMES))/COUNTIF(NAMES,NAMES&""))

Here, we are using ISNUMBER(NAMES) as the numerator. It returns TRUE when the cell contains numeric data type, and FALSE if it doesn’t. It doesn’t count blank cells.

**You May Also Like the Following Excel Tutorials:**

*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    .
*   [How to Count the Number of Words in Excel](https://trumpexcel.com/word-count-in-excel/)
    .
*   [Count Cells Based on Background Color in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    .
*   [Using Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “Count Unique Values in Excel Using COUNTIF Function”
-------------------------------------------------------------------

1.  Very nice ideas.  
    It avoids to make macros; it’s not sensible to missing values, and it’s finaly very simple, even to count text or numeric values.
    
    [Reply](https://trumpexcel.com/count-unique-values-in-excel-countif/#comment-14643)
    
2.  Thanks for trick.. One suggestion, if you can place downloadable example that will definitely help.
    
    [Reply](https://trumpexcel.com/count-unique-values-in-excel-countif/#comment-7648)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-unique-values-in-excel-countif/#respond)

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