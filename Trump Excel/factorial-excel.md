# How to Do Factorial (!) in Excel (FACT function)

**Source:** https://trumpexcel.com/factorial-excel

---

[Skip to content](https://trumpexcel.com/factorial-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/factorial-excel/#below-title)

I was kind of a math nerd in school and the sections about probability and permutation/combination were among my favorites.

I remember spending a lot of time calculating factorials as a part of the probability calculations.

But if you’re using Excel and somehow get into a situation where you need to calculate factorial, you don’t need to take out your pen and paper – a simple Excel formula would do that for you.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/factorial-excel/#)

What is a Factorial?
--------------------

_If you already know this and are here just to know how to calculate it in Excel, jump to the next section._

In mathematics, the factorial of a number is the result you get when you multiply that same number with all the integers after it till 1.

For example, the factorial of 5 would be 120 (5\*4\*3\*2\*1).

A factorial is written as the number after an exclamation sign after it. So the factorial of 5 would be written as 5! (and the value of this would be 120).

Calculating Factorial in Excel Using the FACT Function
------------------------------------------------------

Excel has the in-built FACT function that can be used to calculate the factorial of any number.

\=FACT(number)

The FACT function only takes one argument, which is the number for which you want to get the factorial value.

Below is the formula that will give you the factorial of 5.

\=FACT(5)

![FACT function in Excel to calculate factorial](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20153'%3E%3C/svg%3E)

The argument in the FACT function needs to be an integer.

In case you enter the number that has an integer as well as the decimal part to it, the formula would only consider the integer part.

For example, the result of =FACT(5) and =FACT(5.6) would be the same.

Also, you cannot use a negative number as an argument inside the FACT function. if you do, it will give you the #NUM! error

In case you 0 as the argument in the FACT function, it will give you 1.

Examples of Using the FACT function
-----------------------------------

Let me quickly show you an example where calculating factorial might be required (right out of my school math textbook)

Let’s say I have 5 different colored balls with me, and I want to find out how many pairs of different colored balls I can make (where the order of the colors matter, Red and Green would be different than Green and Red).

The mathematical formula to do this would be =5!/2!

And in Excel, you can use the below formula:

\=FACT(5)/FACT(2)

_In case you want to calculate unique combinations in Excel, you can use the COMBIN formula_.

So this is how you can easily calculate factorial in Excel.

I hope you found this formula tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Generate Random Numbers in Excel](https://trumpexcel.com/generate-random-numbers-excel/)
    
*   [How to Generate Unique Random Numbers in Excel (No Duplicates)](https://trumpexcel.com/generate-unique-random-numbers-in-excel/)
    
*   [How to Shuffle a List of Items/Names in Excel? 2 Easy Formulas!](https://trumpexcel.com/shuffle-list-excel/)
    
*   [How to Calculate Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [How to Get Descriptive Statistics in Excel?](https://trumpexcel.com/descriptive-statistics-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/factorial-excel/#respond)

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