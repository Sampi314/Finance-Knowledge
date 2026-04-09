# How to make Excel VLOOKUP Case Sensitive

**Source:** https://trumpexcel.com/vlookup-case-sensitive

---

[Skip to content](https://trumpexcel.com/vlookup-case-sensitive/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vlookup-case-sensitive/#below-title)

By default, the lookup value in the VLOOKUP function is not case sensitive. For example, if your lookup value is MATT, matt, or Matt, it’s all the same for the VLOOKUP function. It’ll return the first matching value irrespective of the case.

Making VLOOKUP Case Sensitive
-----------------------------

Suppose you have the data as shown below:

![Excel Vlookup Example - Case Sensitive](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20213'%3E%3C/svg%3E)

As you can see, there are three cells with the same name (A2, A4, and A5) but with a different letter case. On the right (in E2:F4), we have the three names (Matt, MATT, and matt) along with their scores in Math.

[Excel VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 function is not equipped to handle case-sensitive lookup values. In this above example, no matter what lookup value case is (Matt, MATT, or matt), it’ll always return 38 (which is the first matching value).

In this tutorial, you’ll learn how to make VLOOKUP case sensitive by:

*   Using a Helper Column.
*   Without Using a Helper Column and Using a Formula.

##### Making VLOOKUP Case Sensitive – Using Helper Column

A helper column can be used to get unique lookup value for each item in the lookup array. That helps in differentiating between names with different letter case.

Here are the steps to do this:

*   Insert a helper column to the left of the column from where you want to fetch the data. In the example below, you need to insert the helper column between column A and C.  
    ![Excel VLOOKUP Case Sensitive - Helper Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20232'%3E%3C/svg%3E)
*   In the helper column, enter the formula =ROW(). It’ll insert the row number in each cell.![Excel VLOOKUP Case Sensitive - Helper Column ROW](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20553%20233'%3E%3C/svg%3E)
*   Use the following formula in cell F2 to get the case-sensitive lookup result.
    
    \=VLOOKUP([MAX](https://trumpexcel.com/excel-max-function/)
    (EXACT(E2,$A$2:$A$9)\*([ROW](https://trumpexcel.com/excel-row-function/)
    ($A$2:$A$9))),$B$2:$C$9,2,0)
    
*   Copy paste it for the remaining cells (F3 and F4).  
    ![Excel VLOOKUP Case Sensitive - result with helper](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20557%20228'%3E%3C/svg%3E)

_**Note:** Since this is an array formula, use Control + Shift + Enter instead of just enter._

**How does this work?**

Let’s break down the formula to understand how it works:

*   EXACT(E2,$A$2:$A$9) – This part compares the lookup value in E2 with all the values in A2:A9. It returns an array of TRUEs/FALSEs where TRUE is returned when there is an exact match. In this case, where the value in E2 is Matt, it would return the following array:  
    {TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE}.
*   EXACT(E2,$A$2:$A$9)\*(ROW($A$2:$A$9) – This part multiplies the array of TRUEs/FALSEs with the row number of A2:A9. Wherever there is a TRUE, it gives the row number, else it gives 0. In this case, it would return {2;0;0;0;0;0;0;0}.
*   MAX(EXACT(E2,$A$2:$A$9)\*(ROW($A$2:$A$9))) – This part returns the maximum value from the array of numbers. In this case, it would return 2 (which is the row number where there is an exact match).
*   Now we simply use this number as the lookup value and use the lookup array as B2:C9.

_Note: You can insert the helper column anywhere in the data set. Just make sure it is to the left of the column from where you want to fetch the data. You need to then adjust the column number in the VLOOKUP function accordingly._

Now if you’re not a fan of helper column, you can also do a case-sensitive lookup without the helper column.

##### Making VLOOKUP Case Sensitive – Without the Helper Column

Even when you don’t want to use the helper column, you still need to have a virtual helper column. This virtual column is not a part of the worksheet but is constructed within the formula (as shown below).

Here is the formula that’ll give you the result without the helper column:

\=VLOOKUP(MAX(EXACT(D2,$A$2:$A$9)\*(ROW($A$2:$A$9))),CHOOSE({1,2},ROW($A$2:$A$9),$B$2:$B$9),2,0)

**How does this work?**

The formula also uses the concept of a helper column. The difference is that instead of putting the helper column in the worksheet, consider it as virtual helper data that is a part of the formula.

Here is the part that works as the helper data (highlighted in orange):

\=VLOOKUP(MAX(EXACT(D2,$A$2:$A$9)\*(ROW($A$2:$A$9))),**CHOOSE({1,2},[ROW](https://trumpexcel.com/excel-row-function/)
($A$2:$A$9),$B$2:$B$9)**,2,0)

Let me show you what I mean by virtual helper data.

![VLOOKUP Case Sensitive - Helper in Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20276'%3E%3C/svg%3E)

In the above illustration, as I select the CHOOSE part of the formula and press F9, it shows the result that the CHOOSE formula would give.

The result is {2,38;3,88;4,57;5,82;6,55;7,44;8,75;9,38}

It’s an array where a comma represents next cell in the same row and semicolon represents that the following data is in the next row. Hence, this formula creates 2 columns of data – One column has the row number and one has the math score.

Now, when you use the VLOOKUP function, it simply looks for the lookup value in the first column (of this virtual 2 column data) and returns the corresponding score. The lookup value here is a number that we get from the combination of MAX and EXACT function.

**_Download the Example File  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/04/Excel-VLOOKUP-Case-Sensitive.xlsx)
_**

Is there any other way you know to do this? If yes, do share with me in the comments section.

**You May Also Like the Following VLOOKUP Tutorials:** 

*   [Using VLOOKUP Function with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    .
*   [XLOOKUP vs VLOOKUP Function](https://trumpexcel.com/excel-functions/vlookup-vs-xlookup/)
    

*   [Using VLOOKUP Function to Get the Last Number in a List](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/)
    .
*   [VLOOKUP Vs. INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “How to make VLOOKUP Case Sensitive”
--------------------------------------------------

1.  This formula is working in first name when we enter second name formula is not working  
    \=VLOOKUP(MAX(EXACT(D2,$A$2:$A$9)\*(ROW($A$2:$A$9))),CHOOSE({1,2},ROW($A$2:$A$9),$B$2:$B$9),2,0)
    
    [Reply](https://trumpexcel.com/vlookup-case-sensitive/#comment-13526)
    
2.  Very good and essential
    
    [Reply](https://trumpexcel.com/vlookup-case-sensitive/#comment-11350)
    
3.  Good Day,  
    Why is it that I always get an error?But when I press F9, it gives me the correct value.
    
    [Reply](https://trumpexcel.com/vlookup-case-sensitive/#comment-9366)
    
4.  check this it will help you  
    [http://tutorialway.com/microsoft-excel-font-formatting/](http://tutorialway.com/microsoft-excel-font-formatting/)
    
    [Reply](https://trumpexcel.com/vlookup-case-sensitive/#comment-7373)
    
5.  hi  
    i have a website ” [http://www.officekade.com](http://www.officekade.com/)
     ” in iran . i need change calendar to ” shamsi” . can you help me?
    
    [Reply](https://trumpexcel.com/vlookup-case-sensitive/#comment-3288)
    
6.  Hi Sumit,  
    Coincidently, I have a similar post regarding case-sensitive lookup.  
    Three different ways to do case-sensitive lookup  
    [https://wmfexcel.com/2016/04/09/three-different-ways-to-do-case-sensitive-lookup/](https://wmfexcel.com/2016/04/09/three-different-ways-to-do-case-sensitive-lookup/)
      
    Hope you and your read like it. 🙂  
    Cheers,
    
    [Reply](https://trumpexcel.com/vlookup-case-sensitive/#comment-3208)
    
7.  I found a simpler solution:  
    \= INDEX ($B$2:$B$9, MATCH(TRUE, EXACT(D2, $A$2:$A$9), 0))
    
    [Reply](https://trumpexcel.com/vlookup-case-sensitive/#comment-3205)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vlookup-case-sensitive/#respond)

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