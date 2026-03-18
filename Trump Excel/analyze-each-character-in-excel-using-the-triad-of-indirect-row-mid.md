# Analyze Each Character in a Cell in Excel using the Triad of Indirect(), Row() & Mid()

**Source:** https://trumpexcel.com/analyze-each-character-in-excel-using-the-triad-of-indirect-row-mid

---

[Skip to content](https://trumpexcel.com/analyze-each-character-in-excel-using-the-triad-of-indirect-row-mid/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/analyze-each-character-in-excel-using-the-triad-of-indirect-row-mid/#below-title)

Today I am going to give you a powerful formula cocktail. The less-used [INDIRECT()](https://trumpexcel.com/excel-indirect-function/)
 and [ROW()](https://trumpexcel.com/excel-row-function/)
 function together with the [MID()](https://trumpexcel.com/excel-mid-function/)
 function can create a magnificent concoction.

This triad enables you to get into the contents in a cell. and analyze each character separately. For example, suppose you have Excel123 in a cell, and you want to identify if it contains a numeric value or not _(which it does!!)_. Excel inbuilt formulas can not help you here as excel consider this as text _(Try and use Type() function to see for yourself)._

What you need here is a way to check each character separately and then identify if it contains a number. Lets first have a look at the formula that can separate each character:

\=MID(B2,ROW(INDIRECT("1:"&[LEN](https://trumpexcel.com/excel-len-function/)
(B2))),1)

_**Here this works:**_

![Indirect Row Combo Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20647%20299'%3E%3C/svg%3E)

Now when you have it all dissected, you are free to analyze each character separately.

_Note that this technique is best used when combined with other formulas (as you will see later in this post). As a stand-alone technique, it could hardly be of any use. Also, Indirect() is a volatile function, so use cautiously. [\[Know more about volatile formula\]](https://trumpexcel.com/excel-volatile-formulas/)
_

Here are a few examples where this technique could be helpful:

_**1\. To identify cells that contain a numeric character:**_

Suppose you have a list as shown below, and you want to identify (or filter) any cell that contains a numeric character anywhere in the cell

![Number in Product Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20146%20164'%3E%3C/svg%3E)To do this, use the following formula. It returns a _True_ if a cell contains any numeric character, and _False_ if it doesn’t.

\=OR(ISNUMBER(MID(A2,ROW(INDIRECT(“1:”&LEN(A2))),1)\*1))

Use Control + Shift + Enter to enter this formula (instead of Enter), as it is an array formula.

_**2\. To identify the position of the first occurrence of a number**_

To do this, use the following formula. It returns the position of the first occurrence of a number in a cell. For example, if a cell contains ProductA1, it will return _9_. In case there is no number, it returns _“No Numeric Character Present”_

\=IFERROR(MATCH(1,–ISNUMBER(MID(B3,ROW(INDIRECT(“1:”&LEN(B3))),1)\*1),0),”No Numeric Character Present”)

Use Control + Shift + Enter to enter this formula

Hope this saves you some time and effort. If you come up with any other way to use this technique, do share it with me as well.

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/analyze-each-character-in-excel-using-the-triad-of-indirect-row-mid/#respond)

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