# How to Get Rid of #DIV/0! Error in Excel? Easy Formulas!

**Source:** https://trumpexcel.com/div-error-in-excel

---

[Skip to content](https://trumpexcel.com/div-error-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/div-error-in-excel/#below-title)

If you have been working with formulas in Excel, I am sure you have encountered the #DIV/0! error (the Division error).

In this short tutorial, I will show you how to quickly remove the division error in Excel (using some easy formulas).

I will also show you how you can find all the cells in a worksheet or workbook that contain the DIV errors.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/div-error-in-excel/#)

What is a #DIV/0! Error in Excel?
---------------------------------

In Excel, you will get a DIV error when you have a formula where there is a division and the divisor is 0.

For example, if you enter =12/0 in a cell in Excel, it will give you the division error (#DIV/0!)

![DIV Error in a cell formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20499%20196'%3E%3C/svg%3E)

Of course, you wouldn’t use a formula like this in real life, but in most cases, the division error is a result of larger formulas where you use cell references in the formula, and some of the references could have the value 0 or could be blank.

And sometimes, you may get this error as part of the data you download from a database or from the web.

Remove #DIV/0! Error Using IFERROR
----------------------------------

If you’re working with formulas and want to get rid of the #DIV/0! error (which often occurs as the result of the formula), you can use the IFERROR technique.

Below is the syntax of the [IFERROR formula](https://trumpexcel.com/excel-iferror-function/)
:

\=IFERROR(value, value\_if\_error)

here:

*   value – this is the formula that can give you the division error
*   value\_if\_error – this is the value specify you should get when you have any error

Let me explain this using an example.

Suppose you have a dataset as shown below where I have the division formula in column C.

As you can see, I get div errors in all the cases where the divisor is 0 or blank in column B.

![Division error when cells have 0 or blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20598%20372'%3E%3C/svg%3E)

To remove the div error, I can use the below formula:

\=IFERROR(A2/B2,"")

![IFERROR formula to show blank instead of DIV error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20596%20419'%3E%3C/svg%3E)

The above formula returns the resulting value after the division if it’s not an error, and in case it gives an error, it replaces the div error with a blank.

Similarly, if you want to replace the div error with something more meaningful than a blank, you can specify that as the second argument.

Below is the formula that will give you the text “Not Available” instead of the division error:

\=IFERROR(A2/B2,"Not Available")

![IF and ISERROR formula to remove DIV error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20598%20418'%3E%3C/svg%3E)

A few important things to know about the IFERROR formula:

*   IFERROR formula was introduced in Excel 2007 onwards. So if you’re using Excel 2003 or prior versions, you won’t get to use this formula (use the method I cover next in that case)
*   IFERROR works for all the error values (including N/A, #DIV/0!, #VALUE!, #REF!, #NAME, #NUM, etc.). So in case your formula returns any other error, it would also be treated the same way

Remove #DIV/0! Error Using ISERROR and IF
-----------------------------------------

While using the IFERROR function is the preferred way to handle the #DIV/0! error in Excel, in case you’re using an old version of Excel that does not have the IFERROR function (or you need backward compatibility in case you have to share the file with someone who is still using an older [version of Excel](https://spreadsheetplanet.com/find-version-of-excel/)
), you can use the [IF](https://trumpexcel.com/excel-if-function/)
 + ISERROR method.

This one works just like the IFERROR function but has a few more arguments.

Again, suppose I have the below dataset and I want to remove the #DIV/0! error.

I can use the below formula to do this:

\=IF(ISERROR(A2/B2),"Not Available",A2/B2)

![IF and ISERROR formula to remove DIV error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20598%20418'%3E%3C/svg%3E)

The above formula first checks whether our formula gives an error or not (using the ISERROR formula), and in case it does, it gives the second argument as the result, else it gives the third argument as the result.

Find all Cells with #DIV/0! Error in Excel
------------------------------------------

In this section, I will show you how to quickly find and select all the cells that contain the #DIV/0! error.

This could be useful when you get a file from a colleague or download it from the web and it has the div error that you want to remove.

While this method won’t remove the DIV error, it can be useful in finding and highlighting these errors so you can decide how to handle these (such as delete it or check the data and rectify it).

Below are the steps to find and remove all DIV errors in the worksheet/workbook:

1.  Open the file in which you want to remove all the div erorrs
2.  Hold the Control key and press the F key (or Command + F if using Mac). This will open the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
     dialog box

![Find and Replace dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20225'%3E%3C/svg%3E)

3.  Click on the Options button. This will show you some additional options.

![Click on the Options button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20225'%3E%3C/svg%3E)

4.  In the ‘Find what:’ field, enter #DIV/0!

![Enter DIV in Find What field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)

5.  From the ‘Within’ drop-down, select Sheet or Workbook (select Workbook if you want to find the error cells in the entire file)

![Select Sheet in within options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)

6.  From the ‘Look in’ drop-down, select ‘Values’

![Select Values in the look in drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)

7.  Click on Find All. This will find all the cells that have the division erorr and show you the references below the Find and Replace dialog box.

![Click on Find All button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)

8.  Hold the Control key and press the A key (or Command + A if using Mac). This would select all the cells that contain the division error.

![All cell references with div erorr in it are selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20393'%3E%3C/svg%3E)

Once selected, you can remove the error from all these cells by hitting the delete key, or highlight these by giving the cells a background color.

So these are some of the ways you can use to remove the DIV errors (division error) in Excel. If it’s a result of your own formulas, you can use the IFERROR function, and if you have these in a workbook that you have inherited or downloaded, you can use the Find and Replace dialog box technique I covered.

I hope you found this tutorial helpful!

**Other Excel tutorials you may also like:**

*   [NAME Error in](https://trumpexcel.com/name-error-excel/)
     [](https://trumpexcel.com/name-error-excel/)
    [Excel (#NAME?)- What Causes it and How to Fix it!](https://trumpexcel.com/name-error-excel/)
    
*   [#REF! Error in Excel – How to Fix the Reference Error!](https://trumpexcel.com/ref-error-in-excel/)
    
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    
*   [Identify Errors Using Excel Formula Debugging](https://trumpexcel.com/excel-formula-debugging/)
    
*   [How to Fix #VALUE Error in Excel?](https://trumpexcel.com/fix-value-error-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Get Rid of #DIV/0! Error in Excel? Easy Formulas!”
-----------------------------------------------------------------------

1.  This was exactly what I was looking for! Thank you so much for this tutorial! It was concise and very helpful.
    
    [Reply](https://trumpexcel.com/div-error-in-excel/#comment-49052)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/div-error-in-excel/#respond)

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