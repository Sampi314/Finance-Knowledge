# How to Capitalize First Letter of a Text String in Excel (using Formula & VBA)

**Source:** https://trumpexcel.com/capitalize-first-letter-excel

---

[Skip to content](https://trumpexcel.com/capitalize-first-letter-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/capitalize-first-letter-excel/#below-title)

Apart from using Excel with numeric data, a lot of people also use it with text data. It could as simple as keeping a record of names to something more complex.

When working with text data, a common task is to make the data consistent by capitalizing the first letter in each cell (or to capitalize the first letter of each word in all the cells)

In this tutorial, I will show you a couple of methods to capitalize the first letter in Excel cells.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/capitalize-first-letter-excel/#)

Capitalize First Letter Using Formula
-------------------------------------

There can be two scenarios where you want to capitalize:

1.  The first letter of each word
2.  Only the first letter of the first word

### Capitalize the First Letter of Each Word

This one is fairly easy to do – as Excel has a dedicated [function](https://trumpexcel.com/excel-functions/)
 for this.

The [**PROPER function**](https://trumpexcel.com/excel-proper-function/)
, whose purpose of existence is to capitalize the first letter of each word.

Suppose you have a dataset as shown below and you want to quickly convert the first letter of each word into upper case.

![Data where first letter needs to be capitalized](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20218'%3E%3C/svg%3E)

Below is the formula you can use:

\=PROPER(A2)

![PROPER function to capitalize first letter of each word](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20652%20272'%3E%3C/svg%3E)

This would capitalize the first letter of each word in the referenced cell.

Pretty straight forward!

Once you have the desired result, you can copy the cells that have the formula and [paste it as values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 so it’s no longer linked to each other.

### Capitalize Only the First Letter of the First Word Only

This one is a little more tricky than the previous one – as there is no inbuilt formula in Excel to capitalize only the first letter of the first word.

However, you can still do this (easily) with a combination of formulas.

Again, there could be two scenarios where you want to do this:

1.  Capitalize the First Letter of the First Word and leave everything as is
2.  Capitalize the First Letter of the First Word and change the rest to lower case (as there may be some upper case letter already)

The formulas used for each of these cases would be different.

Let’s see how to do this!

#### Capitalize the First Letter of the First Word and Leave Everything As Is

Suppose you have the below dataset and you only want to capitalize the first letter (**and leave the rest as is**).

![Data where first letter needs to be capitalized](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20218'%3E%3C/svg%3E)

Below is the formula that will do this:

\=UPPER(LEFT(A2,1))&RIGHT(A2,LEN(A2)-1)

![Formula to convert first letter to capital and leave rest as is](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20272'%3E%3C/svg%3E)

The above formula uses the [LEFT function](https://trumpexcel.com/excel-left-function/)
 to extract the first character from the string in the cell. It then uses the [UPPER function](https://trumpexcel.com/excel-upper-function/)
 to change the case of the first letter to upper. It then concatenates the rest of the string (which is extracted using the [RIGHT function](https://trumpexcel.com/excel-right-function/)
).

So. if there are words that already have capitalized alphabets already, these would not be changed. Only the first letter would be capitalized.

#### Capitalize the First Letter of the First Word and Change the Rest to Lower Case

Another scenario could be where you want to change the case of only the first letter of the first word and keep everything in lower case. This could be when you text that you want to convert to [sentence case](https://www.thoughtco.com/sentence-case-titles-1691944)
.

In this scenario, you may get some cells where the remaining text is not in the lower case already, so you will have to force the text to be converted to lower case, and then use a formula to capitalize the first letter.

Suppose you have the dataset below:

![Dataset to capitalize first letter and keep everything else lowercase](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20652%20218'%3E%3C/svg%3E)

Below is the formula that will capitalize the first letter of the first word and change the rest to lower case:

\=REPLACE(LOWER(A2),1,1,UPPER(LEFT(A2,1)))

![REPLACE formlula to capitalize first letter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20674%20268'%3E%3C/svg%3E)

Let me explain how this formula works:

*   LOWER(A2) – This converts the entire text into lower case
*   UPPER(LEFT(A2,1) – This converts the first letter of the text string in the cell into the upper case.
*   REPLACE function is used to only replace the first character with the upper case version of it.

One of the benefits of using a formula is that it keeps the resulting data dynamic. For example, if you have the formula in place and you make any changes in the data in column A (the original text data), the resulting data would automatically update. In case you don’t want the original data and only want to keep the final result, make sure to [convert the formula to values](https://trumpexcel.com/convert-formulas-to-values-excel/)

Capitalize First Letter Using VBA
---------------------------------

While using formulas is a quick way to manipulate text data, it does involve a few extra steps of getting the result in an additional column and then copying and pasting it as values.

If you often need to use change the data as shown in one of the examples above, you can also consider using a VBA code. With a VBA macro code, you just have to set it once and then you can add it to the Quick Access Toolbar.

This way, the next time you need to capitalize the first letter, all you need to do is select the dataset and click the macro button in the QAT.

You can even [create an add-in](https://trumpexcel.com/excel-add-in/)
 and use the VBA code in all your workbooks (and can even share these with your colleagues).

Now let me give you the VBA codes.

Below code will capitalize the first letter of the first word and leave everything as-is:

Sub CapitalizeFirstLetter()
Dim Sel As Range
Set Sel = Selection
For Each cell In Sel
    cell.Value = UCase(Left(cell.Value, 1)) & Right(cell.Value, Len(cell.Value) - 1)
Next cell
End Sub

And below is the code that will capitalize the first letter of the text and make everything else in lower case:

Sub CapitalizeFirstLetter()
Dim Sel As Range
Set Sel = Selection
For Each cell In Sel
    cell.Value = Application.WorksheetFunction.Replace(LCase(cell.Value), 1, 1, UCase(Left(cell.Value, 1)))
Next cell
End Sub

You need to place this VBA code in a regular module in the VB Editor

These are some methods you can use to capitalize the first letter in Excel cells. Based on the scenario, you can choose the formula method or the VBA method.

Hope you found this Excel tutorial useful.

**You may also like the following Excel tutorials:**

*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [Remove Characters From Left in Excel](https://trumpexcel.com/remove-characters-from-left-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Capitalize First Letter of a Text String in Excel (using Formula & VBA)”
---------------------------------------------------------------------------------------------

1.  Great tips with extensive scenarios I couldn’t find anywhere else. You’re doing the God’s work. Thank you.
    
    [Reply](https://trumpexcel.com/capitalize-first-letter-excel/#comment-35498)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/capitalize-first-letter-excel/#respond)

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