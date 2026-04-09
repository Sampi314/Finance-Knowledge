# How to Shuffle a List of Items/Names in Excel? 2 Easy Formulas!

**Source:** https://trumpexcel.com/shuffle-list-excel

---

[Skip to content](https://trumpexcel.com/shuffle-list-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/shuffle-list-excel/#below-title)

If you have a list of items or names or numbers, you can use simple formulas in Excel to randomize this list.

I often need to use this when I’m creating tutorials where I need a random set of numbers or items. It could also be useful if you’re creating a random team in your office or classroom.

In this tutorial, I will show you three easy ways to quickly **shuffle a list of names or items in Excel**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/shuffle-list-excel/#)

Randomize List Using SORTBY Formula
-----------------------------------

Suppose you have a list of names as shown below, and you want to randomize this list.

![Name list to be shuffled](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20497'%3E%3C/svg%3E)

Below is the formula that will do this:

\=SORTBY(A2:A15,RANDARRAY(COUNTA(A2:A15)))

![SORTBY formula to shuffle the list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20549'%3E%3C/svg%3E)

I have used the [COUNTA function](https://trumpexcel.com/excel-functions/counta-function/)
 to get the total number of names in the list, which is then used within the RANDARRAY function to generate a list of 14 random numbers (as there are 14 names in the list).

This random list of 14 numbers is then used within the SORTBY function to give us the shuffled list of names.

In case you want to shuffle this list again, hit the F9 key and the list would shuffle again (this happens because RANDARRAY is a [volatile function](https://trumpexcel.com/excel-volatile-formulas/)
 and refreshes whenever you hit F9 or make a change in the Excel file)

Once you have the list of random names you want, you can [convert the formula to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 so that it doesn’t change again.

Note that both ‘SORTBY’ and ‘RANDARRAY’ are new formulas and are only available in **Excel for Microsoft 365, Excel 2021, and Excel for the Web**. In case you’re using an older version of Excel, you won’t have access to these functions. If that’s the case with you, you can use the method covered next.

Also read: [Separating First and Last Names in Excel](https://trumpexcel.com/separate-first-and-last-name-excel/)

Randomize List Using RAND Formula + SORT Feature (for Older Excel Versions)
---------------------------------------------------------------------------

In case you don’t have access to SORTBY and RANDARRAY functions, you can randomize the list the old-fashioned way.

Below I again have the list of names that I want to shuffle and get a new list.

![Name dataset with additional random number column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20526%20500'%3E%3C/svg%3E)

Here are the steps to do this:

1.  In the adjacent column, enter the following formula: =RAND()
2.  [Copy and paste the formula](https://trumpexcel.com/copy-paste-formulas-excel/)
     to all the adjacent cells in column B

![RAND function to get random numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20529%20541'%3E%3C/svg%3E)

3.  Select the dataset (including names and the numbers in column B)
4.  Click the Data tab in the ribbon

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20223'%3E%3C/svg%3E)

5.  In the Sort and Filter group, click on the ‘Sort’ icon

![Click the Sort icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20735%20163'%3E%3C/svg%3E)

6.  In the Sort dialog box, select ‘Random Number’ from the Sort by drop-down

![Sort by Random Number column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20320'%3E%3C/svg%3E)

7.  Click OK

The above steps would sort the list of names based on the random numbers we generated.

In case you want to shuffle the list again, just hit the F9 key. This will force the RAND formula to recalculate and it will give you a new set of random numbers.

Now you can [sort the list of names](https://trumpexcel.com/sort-excel/)
 based on this new random number dataset and you will have the new shuffled list of names.

Once done, you can delete the numbers in column B.

These are two simple ways that you can use to shuffle a list of names or items in Excel.

If you’re using Excel for Microsoft 365 or Excel 2021, you can use the first method where I use the SORTBY and RANDARRAY function.

And in case you are using older versions of Excel, then you can use the second method where I use the [RAND function](https://trumpexcel.com/excel-rand-function/)
.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like**:

*   [How to Generate Random Numbers in Excel](https://trumpexcel.com/generate-random-numbers-excel/)
    
*   [Random Group Generator Template \[FREE Download\]](https://trumpexcel.com/random-group-generator-template/)
    
*   [How to Generate Unique Random Numbers in Excel (No Duplicates)](https://trumpexcel.com/generate-unique-random-numbers-in-excel/)
    
*   [How to Sort by the Last Name in Excel (Easy Guide)](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [How to Combine First and Last Name in Excel](https://trumpexcel.com/combine-first-and-last-name-excel/)
    
*   [Extract Last Name in Excel (5 Easy Ways)](https://trumpexcel.com/extract-last-name-excel/)
    
*   [How to Do Factorial (!) in Excel (FACT function)](https://trumpexcel.com/factorial-excel/)
    
*   [How to Switch First and Last Name in Excel with Comma?](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/shuffle-list-excel/#respond)

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