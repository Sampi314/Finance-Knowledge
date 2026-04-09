# How to Generate Random Numbers in Excel (A Step-by-Step Guide)

**Source:** https://trumpexcel.com/generate-random-numbers-excel

---

[Skip to content](https://trumpexcel.com/generate-random-numbers-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/generate-random-numbers-excel/#below-title)

There may be cases when you need to generate random numbers in Excel.

For example, to select random winners from a list or to get a random list of numbers for data analysis or to create random groups of students in class.

In this tutorial, you will learn how to generate random numbers in Excel (with and without repetitions).

Generate Random Numbers in Excel
--------------------------------

There are two [worksheet functions](https://trumpexcel.com/excel-functions/)
 that are meant to generate random numbers in Excel: RAND and RANDBETWEEN.

*   [RANDBETWEEN function](https://trumpexcel.com/excel-randbetween-function/)
     would give you the random numbers, but there is a **high possibility of repeats** in the result.
*   [RAND function](https://trumpexcel.com/excel-rand-function/)
     is more likely to give you a result without repetitions. However, it only gives random numbers between 0 and 1. It can be used with RANK to generate unique random numbers in Excel (as shown later in this tutorial).

### **Generate Random Numbers using RANDBETWEEN function in Excel**

Excel RANDBETWEEN function generates a set of integer random numbers between the two specified numbers.

RANDBETWEEN function takes two arguments – the Bottom value and the top value. It will give you an integer number between the two specified numbers only.

For example, suppose I want to generate 10 random numbers between 1 and 100.

Here are the steps to generate random numbers using RANDBETWEEN:

*   Select the cell in which you want to get the random numbers.
*   In the active cell, enter =RANDBETWEEN(1,100).
*   Hold the Control key and Press Enter.

This will instantly give me 10 random numbers in the selected cells.

![Generate Random Numbers in Excel - Randbetween](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20305'%3E%3C/svg%3E)

While RANDBETWEEN makes it easy to get integers between the specified numbers, there is a high chance of repetition in the result.

For example, when I use the RANDBETWEEN function to get 10 random numbers and use the formula =RANDBETWEEN(1,10), it gives me a couple of duplicates.

![Generate Random Numbers in Excel - Randbetween repetition](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20301'%3E%3C/svg%3E)

If you’re OK with duplicates, RANDBETWEEN is the easiest way to generate random numbers in Excel.

Note that RANDBETWEEN is a [volatile function](https://trumpexcel.com/excel-volatile-formulas/)
 and recalculates every time there is a change in the worksheet. To avoid getting the random numbers recalculate, again and again, [convert the result of the formula to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

### **Generate Unique Random Numbers using RAND and RANK function in Excel**

I tested the RAND function multiple times and didn’t find duplicate values. But as a caution, I recommend you check for duplicate values when you use this function.

Suppose I want to generate 10 random numbers in Excel (without repeats).

Here are the steps to generate random numbers in Excel without repetition:

*   Select the cells in which you want to get the random numbers.
*   In the active cell, enter =RAND()
*   Hold the Control key and Press Enter.![Generate Random Numbers in Excel - rand](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20319%20326'%3E%3C/svg%3E)
*   Select all the cell (where you have the result of the RAND function) and [convert it to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
    .
*   In the adjacent column, use the following formula: =RANK.EQ(A2,$A$2:$A$11)![Generate Random Numbers in Excel - Rank Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20323'%3E%3C/svg%3E)

Now you can use the values in column B as the random numbers.

Note: RAND is a volatile formula and would recalculate every time there is any change in the worksheet. Make sure you have converted all the RAND function results to values.

**Caution:** While I checked and didn’t find repetitions in the result of the RAND function, I still recommend you check once you have generated these numbers. You can use [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 to highlight duplicates or use the [Remove Duplicate](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
 option to get rid of it.

**You May Also Like the Following Excel Tutorials:**

*   [Automatically Sort Data in Alphabetical Order using Formula](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    .
*   [Random Group Generator Template](https://trumpexcel.com/random-group-generator-template/)
    
*   [How to Shuffle a List of Items/Names in Excel?](https://trumpexcel.com/shuffle-list-excel/)
    
*   [How to Do Factorial (!) in Excel (FACT function)](https://trumpexcel.com/factorial-excel/)
    
*   [Create All Possible Combinations from Lists in Excel](https://trumpexcel.com/create-all-combinations-from-lists-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Generate Random Numbers in Excel”
-------------------------------------------------------

1.  The link or the Ebooks do not send to my email
    
    [Reply](https://trumpexcel.com/generate-random-numbers-excel/#comment-14779)
    
2.  Just a trick, RAND and RANDBETWEEN are volatile functions, so each time there’s a change they will be updated. To avoid this, you can create a Pivot Table referencing the cells with the random values (functions) and then reference the Pivot Table values. This way the random values won’t change until the Pivot Table is updated.
    
    [Reply](https://trumpexcel.com/generate-random-numbers-excel/#comment-9111)
    
    *   qawq
        
        [Reply](https://trumpexcel.com/generate-random-numbers-excel/#comment-13933)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/generate-random-numbers-excel/#respond)

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