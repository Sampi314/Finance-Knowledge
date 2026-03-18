# Using A1 or R1C1 Reference Notation in Excel (& How to Change These)

**Source:** https://trumpexcel.com/a1-r1c1-reference-notation-excel

---

[Skip to content](https://trumpexcel.com/a1-r1c1-reference-notation-excel#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/a1-r1c1-reference-notation-excel#below-title)

Most Excel users, including many advanced Excel users, have no idea what the R1C1 and A1 notation means in Excel.

In almost all of the situations, you don’t need to know what this is, and the default settings in Excel would be enough for you.

But since you are here reading this article, I’m assuming that you either have a need to know what is the difference between the R1C1 and A1 reference notations, or you’re naturally curious.

In this article, I will tell you everything you need to know about **R1C1 and A1 reference notation in Excel**, and the Pros and Cons of each.

So, let’s get to it!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/a1-r1c1-reference-notation-excel#)

What is A1 Reference Style in Excel?
------------------------------------

The A1 reference style is the default reference style notation in Excel, and if you have used Excel even for a few hours, I’m assuming you have already used it.

In layman’s terms, a reference style is a style you use to refer to the cells in Excel.

When using the A1 reference style, you would refer to any sale by first specifying the column alphabet/letter for that cell, followed by the [row number](https://trumpexcel.com/number-rows-in-excel/)
 for that cell.

For example, if you want to refer to the top-left cell in a worksheet in Excel, you would use A1 – where A tells us that it’s in column A, and 1 tells us that it’s in the first row.

![A1 Cell in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20557%20257'%3E%3C/svg%3E)

As I mentioned, A1 is the default reference style notation in Excel. so if you enter and equal to sign in a cell in the worksheet, and then select any cell, you would automatically see the reference of that cell appear in the active cell.

![A cell referring to cell A1 in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20511%20248'%3E%3C/svg%3E)

What is R1C1 Reference Style in Excel?
--------------------------------------

R1C1 is the other type of reference style that you can use in Excel.

Here, R refers to the Row and C refers to the column, so R1C1 would refer to the cell in the first row and first column.

![R1C1 cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20418%20164'%3E%3C/svg%3E)

Similarly, R2C3 would refer to the cell in the second row and third column.

![R2C3 cell in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20215'%3E%3C/svg%3E)

This is also known as the Relative Notation as the cell reference uses a row number and column number that tells you the relative position of that reference from the active cell.

For example, if I am in the top left in the worksheet (which is cell A1 or R1C1), and I want to refer to cell D5, then in R1C1 notation, the reference would be R5C4 (as D5 would be the cell in the fifth row and fourth column)

![Referring to R5C4 cell using R1C1 reference notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20264'%3E%3C/svg%3E)

Just like the A1 notation, where you have absolute and relative references, you can also have these in the R1C1 notation.

### Relative References in R1C1 Reference Style

Before I talk about the absolute cell reference in R1C1 notation, let me first talk about the relative reference.

If I’m in cell A1 (the top-left cell in the worksheet), and I want to refer to cell D5, below is the relative R1C1 reference I would have to use:

\=R\[4\]C\[3\]

The above notation indicates that from the active cell I need to refer to the cell which is 4 rows below the active cell and 3 columns to the right of the active cell.

![Referring to cell D5 from A1 in R1C1 notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20256'%3E%3C/svg%3E)

So if I am using this formula in cell A1, then this would refer to cell D5.

And the reason why we call this a relative reference is to use the same formula in cell A2, then it would refer to cell D6 (which is again 5 rows below and 4 columns to the right).

![Referring to cell D6 from A2 in R1C1 notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20296'%3E%3C/svg%3E)

In a nutshell, the number in the square bracket is the offset value to consider. So R\[5\] means that we need to offset the row number by 5 and consider the row number that is five rows below the active cell, and similarly, for the column, C\[4\] offsets the column number by 4 so we need to refer to the column number that is four columns to the right.

One useful feature of using the R1C1 relative reference notation is that you can also use negative numbers in these square brackets.

So if you use =R\[-1\]C\[-1\], it would refer to the cell one row above and one column to the left.

### Absolute References in R1C1 Reference Style

Absolute reference in the R1C1 notation is quite straightforward.

You don’t use the square brackets in the absolute reference, and the reference you specify is the one that is actually used (so there is no offsetting).

For example, if I need to refer to cell D5, I will use R5C4.

![Referring to R5C4 cell using R1C1 reference notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20264'%3E%3C/svg%3E)

An example of Absolute R1C1 reference notation

No matter where in my worksheet I use this reference R5C4, it would always refer to cell D5.

Hence it’s called absolute (as it doesn’t change).

Unlike relative references, you cannot use negative numbers in Absolute Reference. You also can not use 0. The number should always be a positive whole number.

Also read: [Absolute, Relative, and Mixed Cell References in Excel](https://trumpexcel.com/absolute-relative-mixed-cell-references/)

How to Switch from A1 to R1C1 Notation (or R1C1 to A1)?
-------------------------------------------------------

As I mentioned, by default Excel has the A1 reference style enabled. but you can easily switch between the two reference styles with a few clicks.

Below are the steps to switch from the A1 reference style to the R1C1 reference style:

1.  Click the File tab in the ribbon
2.  Click on Options.
3.  In the [Excel Options dialog box](https://trumpexcel.com/excel-options-hacks/)
    , click on Formulas

![Select Formulas in the Excel options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20545%20431'%3E%3C/svg%3E)

4.  Within the ‘Working with Formulas’ section, check the ‘R1C1 reference style’ option

![Check the R1C1 reference Style option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20481'%3E%3C/svg%3E)

5.  Click Ok

The above steps would enable the R1C1 reference notation. in case you already have some formulas in the worksheet, you’ll notice that the reference style would now be shown in the R1C1 format.

Similarly, if you want to switch the reference style back to A1, follow the same steps and uncheck the ‘R1C1 reference style’ option in Step 4.

When you change the reference style from A1 to R1C1, you will notice that the row and column headers now both show numbers (while earlier the column headers had letters)

A1 vs R1C1 Notation Comparison
------------------------------

Below I have a table where I have compared the two reference styles notations:

| Formula in Cell | A1 Reference Style | R1C1 Reference Style |
| --- | --- | --- |
| A1  | \=A2 | \=R\[1\]C |
| A1  | \=$A$2 | \=R2C1 |
| A3  | \=A1+A2 | \=R\[-2\]C+R\[-1\]C |
| A3  | \=$A$1+$A$2 | \=R1C1+R2C1 |
| A4  | \=SUM(A1:A3) | \=SUM(R\[-4\]C:R\[-2\]C) |

Which Reference Style Should You Be Using?
------------------------------------------

Unless you have a reason to use the R1C1 reference style notation, **I would recommend sticking to the default A1 reference style**.

A1 style it’s easier to use, And since almost all the Excel users use it, it makes it easier for you to share your work with other people.

One instance where you may want to use the R1C1 notation is when you want to [debug formulas](https://trumpexcel.com/excel-formula-debugging/)
 and identify errors.

But it’s still a good idea to understand how both these notations work. While you may not have much use of the R1C1 notation in the worksheet, an understanding of how these work can be useful if you work often with VBA coding.

I hope you found this excel tutorial useful.

**Other excel tutorials you may also like:**

*   [How to Find Circular Reference in Excel](https://trumpexcel.com/find-circular-reference-excel/)
    
*   [How to Reference Another Sheet or Workbook in Excel (with Examples)](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    
*   [#REF! Error in Excel – How to Fix the Reference Error!](https://trumpexcel.com/ref-error-in-excel/)
    
*   [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    
*   [How to Find External Links and References in Excel](https://trumpexcel.com/find-external-links-excel/)
    
*   [How to Return Cell Address Instead of Value in Excel](https://trumpexcel.com/return-cell-address-instead-of-value-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/a1-r1c1-reference-notation-excel/#respond)

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

![](https://pixel.rubiconproject.com/token?pid=49096&us_privacy=1YNY)

✕

Do not sell or share my personal information.
---------------------------------------------

You have chosen to opt-out of the sale or sharing of your information from this site and any of its affiliates. To opt back in please click the "Reenable Personalization" link.  
  
This site collects information through the use of cookies and other tracking tools. Cookies and these tools do not contain any information that personally identifies a user, but personal information that would be stored about you may be linked to the information stored in and obtained from them. This information would be used and shared for Analytics, Ad Serving, Interest Based Advertising, among other purposes.  
  
For more information please visit this site's Privacy Policy.

CANCEL

CONTINUE

Your Use of Our Content
-----------------------

✕

The content we make available on this website \[and through our other channels\] (the “Service”) was created, developed, compiled, prepared, revised, selected, and/or arranged by us, using our own methods and judgment, and through the expenditure of substantial time and effort. This Service and the content we make available are proprietary, and are protected by these Terms of Service (which is a contract between us and you), copyright laws, and other intellectual property laws and treaties. This Service is also protected as a collective work or compilation under U.S. copyright and other laws and treaties. We provide it for your personal, non-commercial use only.

You may not use, and may not authorize any third party to use, this Service or any content we make available on this Service in any manner that (i) is a source of or substitute for the Service or the content; (ii) affects our ability to earn money in connection with the Service or the content; or (iii) competes with the Service we provide. These restrictions apply to any robot, spider, scraper, web crawler, or other automated means or any similar manual process, or any software used to access the Service. You further agree not to violate the restrictions in any robot exclusion headers of this Service, if any, or bypass or circumvent other measures employed to prevent or limit access to the Service by automated means.

Information from your device can be used to personalize your ad experience.  
  
[Do not sell or share my personal information.](https://trumpexcel.com/)

[Terms of Content Use](https://trumpexcel.com/)

A Raptive Partner Site