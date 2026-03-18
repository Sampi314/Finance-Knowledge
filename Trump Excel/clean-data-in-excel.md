# 10 Super Neat Ways to Clean Data in Excel Spreadsheets

**Source:** https://trumpexcel.com/clean-data-in-excel

---

[Skip to content](https://trumpexcel.com/clean-data-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/clean-data-in-excel/#below-title)

**Watch Video – 10 Ways to Clean Data in Excel**

Data forms the backbone of any analysis that you do in Excel. And when it comes to data, there are tons of things that can go wrong – be it the structure, placement, formatting, extra spaces, and so on.

In this blog post, I will show you 10 simple ways to clean data in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/clean-data-in-excel/#)

#1 Get Rid of Extra Spaces
--------------------------

Extra spaces are painfully difficult to spot.

While you may somehow spot the extra spaces between words or numbers, trailing spaces are not even visible.

Here is a neat way to get rid of these extra spaces – Use [TRIM Function](https://trumpexcel.com/excel-trim-function/)
.

Syntax: TRIM(text)

The Excel TRIM function takes the cell reference (or text) as the input.

It removes leading and trailing spaces as well as the additional spaces between words (except single spaces).

Also read: [How to Delete Rows in Excel (Single or Multiple)?](https://trumpexcel.com/delete-rows/)

#2 Select and Treat All Blank Cells
-----------------------------------

Blank cells can create havoc if not treated beforehand. I often face issues with blank cells in a data set that is used to create reports/dashboards.

You may want to fill all blank cells with ‘0’ or ‘Not Available’, or may simply want to highlight it.

If there is a huge data set, doing this manually could take hours. Thankfully, there is a way you can select all the blank cells at once.

1.  Select the entire data set.
2.  Press F5 (this opens the Go To dialogue box)
3.  Click on the Special… button (at the bottom left). This opens the Go To Special dialog box.  
    ![Clean Data in Excel - Go To Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20236%20218'%3E%3C/svg%3E)
4.  Select Blank and Click OK  
    ![Clean Data in Excel - Go To Dialogue Box Select Blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20262%20267'%3E%3C/svg%3E)

This selects all the blank cells in your data set.

If you want to enter 0 or Not Available in all these cells, just type it and press **Control + Enter** (remember, if you press only enter, the value is inserted only in the active cell).

Also read: [How to use Fill Handle in Excel](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)

#3 Convert Numbers Stored as Text into Numbers
----------------------------------------------

Sometimes when you import data from text files or external databases, numbers get stored as text.

Also, some people are in the habit of using an apostrophe (‘) before a number to make it text.

This could create serious issues if you are using these cells in calculations.

Here is a foolproof way to convert these numbers stored as text back into numbers.

1.  In any blank cell, type 1
2.  Select the cell where you typed 1, and press Control + C
3.  Select the cell/range which you want to convert to numbers
4.  Select Paste –> Paste Special (_Key Board Shortcut – Alt + E + S_)
5.  In the Paste Special Dialogue box, select Multiply (in operations category)  
    ![Clean Data in Excel - Paste Special Multiply](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20253'%3E%3C/svg%3E)
6.  Click OK. This converts all the numbers in text format back to numbers.

There is a lot more you can do with paste special operations options. Here are various other ways to [multiply in Excel using Paste Special.](https://trumpexcel.com/multiply-in-excel-using-paste-special/)

Also read: [Remove Last Character in Excel](https://trumpexcel.com/remove-last-character/)

#4 – Remove Duplicates
----------------------

There can be 2 things you can do with duplicate data – **_Highlight It_** or **_Delete It._**

*   _**Highlight Duplicate Data:**_
    *   Select the data and Go to Home –> Conditional Formatting –> Highlight Cells Rules –> Duplicate Values.
    *   Specify the formatting and all the duplicate values get highlighted.  
        ![Clean Data in Excel - Highlight Duplicates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20232%20260'%3E%3C/svg%3E)
*   _**Delete Duplicates in Data:**_ 
    *   Select the data and Go to Data –> Remove Duplicates.
    *   If your data has headers, ensure that the checkbox at the top right is checked.
    *   Select the Column(s) from which you want to remove duplicates and click OK.  
        ![Clean Data in Excel - Remove Duplicates select column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20257'%3E%3C/svg%3E)

This removes duplicate values from the list. If you want the original list intact, copy-paste the data at some other location and then do this.

_Related:_ [The Ultimate Guide to Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
.

#5 Highlight Errors
-------------------

There are two ways you can highlight Errors in Data in Excel:

_**Using Conditional Formatting**_

1.  Select the entire data set
2.  Go to Home –> Conditional Formatting –> New Rule
3.  In New Formatting Rule Dialogue Box select ‘Format Only Cells that Contain’
4.  In the Rule Description, select Errors from the drop down
5.  Set the format and click OK. This highlights any error value in the selected dataset  
    ![Clean Data in Excel - Highlight Errors](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20288'%3E%3C/svg%3E)

_**Using Go To Special**_

1.  Select the entire data set
2.  Press F5 (this opens the Go To Dialogue box)
3.  Click on Special Button at the bottom left
4.  Select Formulas and uncheck all options except Errors  
    ![Clean Data in Excel - Select Errors](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20261%20266'%3E%3C/svg%3E)

This selects all the cells that have an error in it. Now you can manually highlight these, delete it, or type anything into it.

Also read: [Remove Parentheses in Excel](https://trumpexcel.com/remove-parentheses-excel/)

#6 Change Text to Lower/Upper/Proper Case
-----------------------------------------

When you inherit a workbook or import data from text files, often the names or titles are not consistent. Sometimes all the text could be in lower/upper case or it could be a mix of both. You can easily make it all consistent by using these three functions:

[LOWER()](https://trumpexcel.com/excel-lower-function/)
 –  Converts all text into Lower Case.  
[UPPER()](https://trumpexcel.com/excel-upper-function/)
 – Converts all text into Upper Case.  
[PROPER()](https://trumpexcel.com/excel-proper-function/)
 – Converts all Text into Proper Case.

Also read: [Excel Skills (Basic, Intermediate, and Advanced)](https://trumpexcel.com/excel-skills/)

#7 Parse Data Using Text to Column
----------------------------------

When you get data from a database or import it from a text file, it may happen that all the text is cramped in one cell. You can parse this text into multiple cells by using Text to Column functionality in Excel.  
![Clean Data in Excel - Text to Column Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%2029'%3E%3C/svg%3E)

1.  Select the data/text you want to parse
2.  Go To Data –> Text to Column (This opens the Text to Columns Wizard)
    *   Step 1: Select the data type (select Delimited if your data in not equally spaced, and is separated by characters such as comma, hyphen, dot..). Click Next  
        ![Clean Data in Excel - Text to Column 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20249'%3E%3C/svg%3E)
    *   Step 2: Select Delimiter (the character that separates your data). You can select pre-defined delimiter or anything else using the Other option  
        ![Clean Data in Excel - Text to Column 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20249'%3E%3C/svg%3E)
    *   Step 3: Select the data format. Also select the destination cell. If destination cell is not selected, the current cell is overwritten  
        ![Clean Data in Excel - Text to Column 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20251'%3E%3C/svg%3E)

_Related__:_ [Extract username from email id using text to column](https://trumpexcel.com/extract-usernames-from-email-ids/)
.

#8 Spell Check
--------------

Nothing lowers the credibility of your work than a spelling mistake.

Use the keyboard shortcut F7 to run a spell check for your data set.

Here is a detailed tutorial on how to use [Spell check in Excel](https://trumpexcel.com/using-spell-check-in-excel/)
.

#9 Delete all Formatting
------------------------

In my job, I used multiple databases to get the data in excel. Every database had it’s own data formatting. When you have all the data in place, here is how you can [delete all the formatting](https://trumpexcel.com/remove-table-formatting-excel/)
 at one go:

1.  Select the data set
2.  Go to Home –> Clear –> Clear Formats  
    ![Clean Data in Excel - Clear Formats](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20180%20189'%3E%3C/svg%3E)

Similarly, you can also clear only the comments, hyperlinks, or content.

Also read: [Delete Blank Columns in Excel (3 Easy Ways + VBA)](https://trumpexcel.com/delete-blank-columns-excel/)

#10 Use Find and Replace to Clean Data in Excel
-----------------------------------------------

Find and replace is indispensable when it comes to data cleansing. For example, you can select and remove all zeros, change references in formulas, find and change formatting, and so on.

[Read more about how Find and Replace can be used to clean data](https://trumpexcel.com/find-and-replace-in-excel/)
.

These are my top 10 techniques to clean data in Excel. If you would like to learn some more techniques, here is a guide by the MS Excel team – [Clean Data in Excel](https://support.office.com/en-nz/article/Top-ten-ways-to-clean-your-data-2844b620-677c-47a7-ac3e-c2e157d1db19)
.

If there are any more techniques that you use, do share it with us in the comments section!

**You May Also Like the Following Excel Tutorials:**

*   [How to Transpose Data in Excel](https://trumpexcel.com/transpose-data-excel/)
    .
*   [Remove Spaces in Excel – Leading, Trailing, and Double.](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
    
*   [8 Ways to Reduce Excel File Size (that actually work)](https://trumpexcel.com/reduce-excel-file-size/)
    
*   [Recover Unsaved Excel Files](https://trumpexcel.com/recover-unsaved-excel-files/)
    .
*   [Hide Zero Values in Excel](https://trumpexcel.com/hide-zero-values-excel/)
    
*   [How to Remove Leading Zeros in Excel (5 Easy Ways)](https://trumpexcel.com/remove-leading-zeros-excel/)
    
*   [How to Format Phone Numbers in Excel?](https://trumpexcel.com/format-phone-numbers-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

43 thoughts on “10 Super Neat Ways to Clean Data in Excel Spreadsheets”
-----------------------------------------------------------------------

1.  Thanks
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-14873)
    
2.  Very useful  
    Thank u sir
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-14851)
    
3.  Thank you for the valuable information!
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-13260)
    
4.  I like how you show the example and explain step-by-step how to do them. Also the examples are relevant and easy to understand. Thanks!
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-12830)
    
5.  This has been s informative. Easy to follow – thank you!
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-12697)
    
6.  Was looking for a website to learn advanced excel and i must say i’ve not seen any better than this. Thanks
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-12630)
    
7.  Was looking for VBA solutions to a different problem but this video had some tricks I haven’t seen before. Great job sir I tip my hat to you on a job well done. (Great pace as well!)
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-11994)
    
8.  Thank you! 🙂
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-11022)
    
9.  Extremely useful. Thank you for the tips.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-10743)
    
10.  I don’t know if I’m asking on the correct website or not, but here goes… I’m trying to upload an excel file to my website, normally the excel spreadsheet is in nice and neat columns, but the new spreadsheet I’ve been sent just seems to be a mess (Almost everything in under category A column). Is there a way to separate all columns from one column into several?
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-9711)
    
    *   Hello David.. You can try the Text to Columns feature in Excel: [https://trumpexcel.com/excel-text-to-columns-examples/](https://trumpexcel.com/excel-text-to-columns-examples/)
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-9712)
        
    *   Make sure that the person saves the original file as a .XLSX and you should be good to go. Otherwise the other comments process would work as well. Just more of a hassle
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-12174)
        
11.  Please tell me this has nothing to do with our current douchebag in chief
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-9175)
    
    *   Your mismanage emotions are 100%. The information here might have not help you, but help others. We the readers deserve respect. Avoid useless comments.
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-10744)
        
12.  Sort both ways (A>>Z; Z>>A) to see extremes of your data  
    fast and furious. Also filter dropdown is useful, to see unique values  
    at glance.
    
    Applying General formatting unhides most of the issues with incorect data types.
    
    The conversion of text numbers to regular numbers is even less work, if  
    you select blank cell and use “Add” or “Subtract” methods.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-8483)
    
    *   Thanks for sharing your tips!
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-8493)
        
13.  For me it was amazing
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3875)
    
14.  caveat for No 3 – cells must not be formatted as text  
    my method is as follows:  
    1 select the cells you wish to convert  
    2 format as General (Ctrl-sh-~ does it for me) or whatever non-text format you fancy  
    3 on another sheet, copy a blank cell (then you don’t have to reselect)  
    4 back with your original selection, paste special as above but ADD the value (ie zero)
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3582)
    
15.  Dear.sir I need subtotal & grand total in next column of number in pivot table
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3476)
    
    *   subtotalling works better in rows – try that  
        Grand totalling (rows and/or columns) is available on the pivot table options
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3583)
        
16.  Thank you for this. Although I consider myself an advanced user I still learnt some useful tips in these 10. One question I have is how to quickly find and remove cells where users have merged cells. This can be so irritating when it stops you creating pivots or filters.  
    I find your site one of the most useful and easiest to follow solutions to any problems. Thank you again.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3227)
    
    *   select the whole sheet and press ctrl-F1 to format cells; clear the merge cells tick box and click OK
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3581)
        
        *   You mean Ctrl-1. Ctrl-F1 hides/shows the ribbon 🙂
            
            [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3684)
            
    *   if you only want to find and select them, use Find but leave the “Find what” text empty, expand the Options>> and click Format…, select the Alignment tab and check Merge cells then click OK  
        Press alt-A to Find All, then ctrl-A to leave all those cells selected when you quit the Find dialogue box
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3584)
        
17.  Very Nice Tricks..
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2993)
    
    *   Thanks Bijay.. Glad you found these useful 🙂
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-3005)
        
18.  One thing I would mention is the removal of non-breaking spaces, symbolized as nbsp or character 160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2845)
    
    *   Thanks for commenting.. Non-breaking spaces could be a real pain, especially when I copy data from a webpage
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2868)
        
    *   Thanks for commenting.. Non-breaking spaces could be a pain when it comes to data in Excel
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2870)
        
19.  One thing I would mention is the removal of non-breaking spaces, symbolized as nbsp or character 160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2844)
    
20.  One thing I would mention is the removal of non-breaking spaces, symbolized as nbsp or character 160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2843)
    
21.  One thing I would mention is the removal of non-breaking spaces, symbolized as nbsp or character 160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2842)
    
22.  One thing I would mention is the removal of non-breaking spaces, symbolized as   or &#160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2841)
    
23.  One thing I would mention is the removal of non-breaking spaces, symbolized as   or &#160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2840)
    
24.  One thing I would mention is the removal of non-breaking spaces, symbolized as   or &#160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2839)
    
25.  One thing I would mention is the removal of non-breaking spaces, symbolized as   or &#160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2838)
    
26.  One thing I would mention is the removal of non-breaking spaces, symbolized as   or &#160. These have caused me much grief.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2837)
    
27.  Fantastic! I can’t wait to get into work on Monday and try some of these babies out. Thanks for all the effort you put into this blog as a way to share your knowledge.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2101)
    
    *   Thanks for the kind words.. I am glad you like the techniques here 🙂
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2102)
        
        *   I think it’s wonderful. The thing I love about the internet is people sharing their knowledges and passions. The two things I use the internet for the most is excel tips and Real Housewives (reality TV show!) recaps. Strange combination, I know. Thanks again. I love the passion and the knowledge that goes into your site.
            
            [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2105)
            
28.  Thanks Sumit. I need to share this with my colleagues who send me the data 😉
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2099)
    
    *   Thanks for commenting Gary.. I too shared it with a lot of my colleagues. And it made my life a lot easier 🙂
        
        [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-2103)
        
29.  Number 11: Sometimes there are unprintable characters. Use Clean() to get rid of those. I like using it with TRIM, i.e. TRIM(CLEAN()) or CLEAN(TRIM()) work for me.
    
    [Reply](https://trumpexcel.com/clean-data-in-excel/#comment-1731)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/clean-data-in-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](https://trumpexcel.com/wp-content/uploads/2024/03/Free-Excel-Tips-EBook-Sumit-Bansal-1.png)

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

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](https://trumpexcel.com/wp-content/uploads/2024/03/Free-Excel-Tips-EBook-Sumit-Bansal-1.png)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](https://trumpexcel.com/wp-content/uploads/2024/03/Free-Excel-Tips-EBook-Sumit-Bansal-1.png)

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