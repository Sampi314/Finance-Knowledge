# How to Quickly Combine Cells in Excel

**Source:** https://trumpexcel.com/combine-cells-in-excel

---

[Skip to content](https://trumpexcel.com/combine-cells-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/combine-cells-in-excel/#below-title)

**Watch Video – Combine Two cells in Excel (using Formulas)**

A lot of times, we need to work with text data in Excel. It could be Names, Address, Email ids, or other kinds of text strings. Often, there is a need to combine cells in Excel that contain the text data.

Your data could be in adjacent cells (rows/columns), or it could be far off in the same worksheet or even a different worksheet.

How to Combine Cells in Excel
-----------------------------

In this tutorial, you’ll learn how to Combine Cells in Excel in different scenarios:

*   How to Combine Cells without Space/Separator in Between.
*   How to Combine Cells with Space/Separator in Between.
*   How to Combine Cells with Line Breaks in Between.
*   How to Combine Cells with Text and Numbers.

### How to Combine Cells without Space/Separator

This is the easiest and probably the most used way to combine cells in Excel. For example, suppose you have a data set as shown below:

![Combine Cells in Excel - Data without separator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20267%20152'%3E%3C/svg%3E)

You can easily combine cells in columns A and B to get a string such as A11, A12, and so on..

Here is how you can do this:

*   Enter the following formula in a cell where you want the combined string:
    
    \=A2&B2
    
*   Copy-paste this in all the cells.

This will give you something as shown below:

![Combine Cells in Excel - Result without separator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20431%20190'%3E%3C/svg%3E)

You can also do the same thing using the [CONCATENATE function](https://trumpexcel.com/excel-concatenate-function/)
 instead of using the ampersand (&). The below formula would give the same result:

\=CONCATENATE(A2,B2)

### How to Combine Cells with Space/Separator in Between

You can also combine cells and have a specified separator in between. It could be a space character, a comma, or any other separator.

Suppose we have a dataset as shown below:

![Combine Cells in Excel - Data with separator dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20324%20204'%3E%3C/svg%3E)

Here are the steps to [combine the first and the last name](https://trumpexcel.com/combine-first-and-last-name-excel/)
 with a space character in between:

*   Enter the following formula in a cell:
    
    \=A2&" "&B2
    
*   Copy-paste this in all the cells.

This would combine the first name and last name with a space character in between.

![Combine Cells in Excel - Result with separator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20246'%3E%3C/svg%3E)

If you want any other separator (such as comma, or dot), you can use that in the formula.

### How to Combine Cells with Line Breaks in Between

Apart from separators, you can also add line breaks while you combine cells in Excel.

Suppose you have a dataset as shown below:

![Combine Cells in Excel - Address](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20474%2098'%3E%3C/svg%3E)

In the above example, different parts of the address are in different cells (Name, House #, Street, City, and Country).

You can use the CONCATENATE function or the & (ampersand) to combine these cells.

However, just by combining these cells would give you something as shown below:

![Combine Cells in Excel - Address without linebreak](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20834%20130'%3E%3C/svg%3E)

This is not in a good address format. You can try using the text wrap, but that wouldn’t work either.

What is needed here is to have each element of the address on a separate line in the same cell. You can achieve that by using the CHAR(10) function along with the & sign.

_CHAR(10) is a line feed in Windows, which means that it forces anything after it to go to a new line._

Use the below formula to get each cell’s content on a separate line within the same cell:

\=A2&CHAR(10)&B2&CHAR(10)&C2&CHAR(10)&D2&CHAR(10)&E2

This formula uses the CHAR(10) function in between each cell reference and inserts a line break after each cell. Once you have the result, [apply wrap text in the cells](https://trumpexcel.com/wrap-text/)
 that have the results and you’ll get something as shown below:

![Combine Cells in Excel - Address with linebreak](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20302'%3E%3C/svg%3E)

Also read: [Generate All Possible Combinations from Lists in Excel](https://trumpexcel.com/create-all-combinations-from-lists-excel/)

### How to Combine Cells with Text and Numbers

You can also combine cells that contain different types of data. For example, you can combine cells that contain text and numbers.

Let’s have a look at a simple example first.

Suppose you have a dataset as shown below:

![Combine Cells in Excel - text and numbers dataset1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%20151'%3E%3C/svg%3E)

The above data set has text data in one cell and a number is another cell. You can easily combine these two by using the below formula:

\=A2&"-"&B2

Here I have used a dash as the separator.

![Combine Cells in Excel - text and numbers dash](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20192'%3E%3C/svg%3E)

You can also add some text to it. So you can use the following formula to create a sentence:

\=A2&" region has "&B2&" offices"

Here we have used a combination of cell reference and text to construct sentences.

![Combine Cells in Excel - text and numbers dash sentence](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20189'%3E%3C/svg%3E)

Now let’s take this example forward and see what happens when you try and use numbers with some formatting applied to it.

Suppose you have a dataset as shown below, where we have sales values.

![Combine Cells in Excel - text and numbers sales](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20153'%3E%3C/svg%3E)

Now let’s combine the cells in Column A and B to construct a sentence.

Here the formula I’ll be using:

\=A2&" region generated sales of "&B2

Here is how the results look like:

![Combine Cells in Excel - text and numbers sales 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20188'%3E%3C/svg%3E)

Do you see the problem here? Look closely at the format of the sales value in the result.

![Combine Cells in Excel - text and numbers sales 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20184'%3E%3C/svg%3E)

You can see that the formatting of the sales value goes away and the result has the plain numeric value. This happens when we combine cells with numbers that have formatting applied to it.

Here is how to fix this. Use the below formula:

\=A2&" region generated sales of "&[TEXT](https://trumpexcel.com/excel-text-function/)
(B2,"$ ###,0.0")

In the above formula, instead of using B2, we have used the [TEXT function](https://trumpexcel.com/excel-text-function/)
. TEXT function makes the number show up in the specified format and as text. In the above case, the format is **$ ###,0.0.** This format tells Excel to show the number with a dollar sign, a thousand-separator, and one decimal point.

Similarly, you can use the Text function to show in any format allowed in Excel.

Here is another example. There are names and date of birth, and if you try and combine these cells, you get something as shown below:

![Combine Cells in Excel - DOB1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20191'%3E%3C/svg%3E)

You can see that Excel completely screws up the date format. The reason is that date and time are stored as numbers in Excel, and when you combine cells that have numbers, as shown above, it shows the number value but doesn’t use the original format.

Here is the formula that will fix this:

\=A2&" was born on "&TEXT(B2,"dd mmm yyy")

![Combine Cells in Excel - DOB with text function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20677%20194'%3E%3C/svg%3E)

Again, here we have used the TEXT function and specified the format in which we want the Date of Birth to show up in the result.

Here is how this date format works:

*   dd – Shows the day number of the date. (try using ddd and see what happens).
*   mmm – shows the three-letter code for a month.
*   yyy – shows the year number.

Cool… Isn’t it?

Let me know your thoughts in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [CONCATENATE Excel Range (with and without separator).](https://trumpexcel.com/concatenate-excel-ranges/)
    
*   [How to Merge Cells in Excel the Right Way.](https://trumpexcel.com/how-to-merge-cells-in-excel/)
    
*   [How to Combine Multiple Workbooks into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    .
*   [How to Combine Data from Multiple Workbooks into One Excel Table (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    .
*   [How to Merge Cells in Excel](https://trumpexcel.com/how-to-merge-cells-in-excel/)
    
*   [How to Combine Duplicate Rows and Sum the Values in Excel](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/)
    
*   [Combine Date and Time in Excel](https://trumpexcel.com/combine-date-time-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

15 thoughts on “How to Combine Cells in Excel”
----------------------------------------------

1.  Excellent tutorial. Thank you. (I am a retired person trying to learn coding for personal use. I find your tutorials very useful.)
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-14832)
    
2.  Another excellent tutorial – thanks so much Sumit!
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-14716)
    
3.  Thank you for sharing this great resource
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-13535)
    
4.  Hi, is there any way to combine multiple table data (same format) into 1 table with additional column of total?
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-13534)
    
5.  if any cell is blank this formula takes care of it  
    B2&IF(ISBLANK(C2),,CHAR(10)&C2)&IF(ISBLANK(D2),,CHAR(10)&D2)&IF(ISBLANK(E2),,CHAR(10)&E2)&IF(ISBLANK(F2),,CHAR(10)&F2)&IF(ISBLANK(G2),,CHAR(10)&F2)&IF(ISBLANK(H2),,CHAR(10)&H2)
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-13527)
    
6.  Great … & awesome.  
    Thanks for shairing.
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-13524)
    
7.  Well done.
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-13523)
    
8.  Ok, I need help! =( How do I add space and commas using this formula: =H2&CHAR(10)&I2&CHAR(10)&J2&K2&L2  
    everything lined up nicely, but it looks as if I concatenated some data here (city state and zip); See example below:  
    Outcome:  
    123 Happy life  
    #21  
    Los AngelesCA91111
    
    what I’m looking for:
    
    123 Happy Life  
    #21  
    Los Angeles, CA 91111
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-10242)
    
    *   Try:
        
        \=H2&CHAR(10)&I2&CHAR(10)&J2&”, “&K2&” “&L2
        
        [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-13519)
        
9.  What if I want to get [0001@domain.com](mailto:0001@domain.com)
    ?  
    When I combine 0001 and @domain.com, I get [1@domain.com](mailto:1@domain.com)
     even though the first cell is formatted at 0000 (4 digits)
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-9657)
    
    *   Hey.. This happens as the combined value becomes a text and number formatting does not apply to it. To keep the 0000 formatting, you need to use the TEXT function. [http://trumpexcel.com/excel-functions/excel-text-function/](http://trumpexcel.com/excel-functions/excel-text-function/)
        
        [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-9679)
        
10.  Thanks for the CHAR(10) tip. Useful.
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-3023)
    
11.  That’s very useful and I do like the way you explain the additional functions in an easy to understand way. Many thanks indeed.
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-3021)
    
12.  Really you are helping the Excel lovers with your simple and very useful tricks/tips. Thanks on behalf of all my Excel lovers/addicts/friends/learners.
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-3017)
    
13.  Thanks a million Mr. Sumit Bansal for such a great function. I was wondering whether is it possible or not earlier but for now there is no doubt about it………….great help
    
    [Reply](https://trumpexcel.com/combine-cells-in-excel/#comment-3016)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/combine-cells-in-excel/#respond)

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