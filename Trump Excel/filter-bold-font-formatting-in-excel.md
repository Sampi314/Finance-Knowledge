# How to Filter Cells with Bold Font Formatting in Excel (An Easy Guide)

**Source:** https://trumpexcel.com/filter-bold-font-formatting-in-excel

---

[Skip to content](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#below-title)

I get this query all the time. People have huge data sets and someone in their team has highlighted some records by formatting it in bold font.

Now, you are the one who gets this data, and you have to filter all these records that have a bold formatting.

For example, suppose you have the data set as shown below, and you want to filter all the cells that have been formatted in bold font.

![Formatting in Excel - Filter Bold](https://trumpexcel.com/wp-content/uploads/2015/02/Formatting-in-Excel-Filter-Bold.png)

Let’s face it.

There is no straightforward way of doing it.

You cannot simply use an Excel filter to get all the bold cells. But that doesn’t mean you have to waste hours and do it manually.

In this tutorial, I will show you three ways to filter cells with bold font formatting in Excel:

This Tutorial Covers:

[Toggle](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#)

![Filter Cells with Bold Font Formatting in Excel - Image](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20390%20309'%3E%3C/svg%3E)

Method 1 – Filter Bold Cells Using Find and Replace
---------------------------------------------------

[Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
 can be used to find specific text in the worksheet, as well as a specific format (such as cell color, font color, bold font, font color).

The idea is to find the bold font formatting in the worksheet and convert it into something that can be easily filtered _(Hint: Cell color can be used as a filter)_.

Here are the steps filter cells with bold text format:

1.  Select the entire data set.
2.  Go to the Home tab.
3.  In the Editing group, click on the Find and Select drop down.
4.  Click on Replace. (_Keyboard shortcut: Control + H_)![filter by bold font format in Excel - Click on Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20231%20354'%3E%3C/svg%3E)
5.  In the Find and Replace dialog box, click on the Options button.![how to filter bold text in Excel - Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20194'%3E%3C/svg%3E)
6.  In the Find what section, go to the Format drop-down and select ‘Choose Format From Cell’.![Choose bold font format from cell directly](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20562%20248'%3E%3C/svg%3E)
7.  Select any cell which has the text in bold font format.![filter by bold font format in Excel - Preview](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20673%20243'%3E%3C/svg%3E)
8.  In the ‘Replace with:’ section, go to Format drop-down and click on ‘Choose Format From Cell’ option.![Select the format with which you want to replace bold font](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20249'%3E%3C/svg%3E)
9.  In the Replace Format dialog box, select the Fill Tab and select any color and click OK (make sure it’s a color that is not there already in your worksheet cells).
10.  Click on Replace All. This will color all the cells that have the text with bold font formatting. ![Formatting in Excel - bold cells colored](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2081%20227'%3E%3C/svg%3E)

In the above steps, we have converted the bold text format into a format that is recognized as a filter criterion by Excel.

Now to filter these cells, here are the steps:

1.  Select the entire data set.
2.  Go to the Data tab.
3.  Click on the Filter icon _(Key Board Shortcut: Control + Shift + L)![Filter Icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20132'%3E%3C/svg%3E)_
4.  For the column that you want to filter, click on the filter icon (the downward pointing arrow in the cell).
5.  In the drop-down, go to the ‘Filter by Color’ option and select the color you applied to cells with text in bold font format.![Filter cell with text with bold font formatting - filter by color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20385%20456'%3E%3C/svg%3E)

This will automatically filter all those cells that have bold font formatting in it.

_**Try it yourself.. Download the file  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/b0heam03vph048t/FilterBoldCells.xlsm?dl=1)
  
**_

Also read: [Best Excel Fonts](https://trumpexcel.com/best-excel-fonts/)

Method 2 – Using Get.Cell Formula
---------------------------------

It time for a hidden gem in Excel. It’s an Excel 4 macro function – **GET.CELL()**.

This is an old function which does not work in the worksheet as regular functions, but it still works in [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
.

GET.CELL function gives you the information about the cell.

For example, it can tell you:

*   If the cell has bold formatting or not
*   If the cell has a formula or not
*   If the cell is locked or not, and so on.

Here is the syntax of the GET.CELL formula

**\=GET.CELL(type\_num, reference)**

*   **Type\_num** is the argument to specify the information that you want to get for the referenced cell (for example, if you enter 20 as the type\_num, it would return TRUE if the cell has a bold font format, and FALSE if not).
*   **Reference** is the cell reference that you want to analyze.

Now let me show you how to filter cells with text in a bold font format using this formula:

1.  Go to Formulas tab.
2.  Click on the Define Name option.![Select Define Name in Formula Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20138'%3E%3C/svg%3E)
3.  In the New Name dialog box, use the following details:
    *   Name: FilterBoldCell
    *   Scope: Workbook
    *   Refers to: \=GET.CELL(20,$A2)![Create a new Named Range to use getcell function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20232'%3E%3C/svg%3E)
4.  Click OK.
5.  Go to cell B2 (or any cell in the same row as that of the first cell of the dataset) and type \=FilterBoldCell
6.  Copy this formula for all the cell in the column. It will return a TRUE if the cell has bold formatting and FALSE if it does not.
7.  Now select the entire data set, go to the Data tab and click on the Filter icon.
8.  In the column where you have TRUE/FALSE, select the filter drop-down and select TRUE.![Select TRUE to filter cells that have text with bold font format in cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20270%20433'%3E%3C/svg%3E)

That’s it!

All the cells with text in bold font format have now been filtered.

_Note: Since this is a macro function, you need to save this file with a .xlsm_ or ._xls extension._

_I could not find any help article on GET.CELL() by Microsoft. [Here](http://www.mrexcel.com/forum/excel-questions/20611-info-only-get-cell-arguments.html)
 is something I found on Mr. Excel Message Board._

_**Try it yourself.. Download the file  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/b0heam03vph048t/FilterBoldCells.xlsm?dl=1)
**_

Method 3 – Filter Bold Cells using VBA
--------------------------------------

Here is another way of filtering cells with text in bold font format by using VBA.

Here are the steps:

1.  Right-click on the worksheet tab and select View Code (or use the keyboard shortcut ALT + F11). This opens the VB Editor backend._![Right click on the sheet tab and click on view code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20182%20271'%3E%3C/svg%3E)_
2.  In the VB Editor window, there would be the Project Explorer pane. If it is not there, go to View and select Project Explorer.![Project Explorer in the Backend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20345%20290'%3E%3C/svg%3E)
3.  In the Project Explorer pane, right click on the workbook (VBAProject) on which you are working, go to Insert and click on Module. This inserts a module where we will put the VBA code.![Insert a Module for function to filter sort cells with bold font format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20434'%3E%3C/svg%3E)
4.  Double click on the module icon (to make sure your code into the module), and paste the following code in the pane on the right:
    
    Function BoldFont(CellRef As Range)
    BoldFont = CellRef.Font.Bold
    End Function
    
5.  Go to the worksheet and use the below formula: \=BoldFont(B2)
6.  This formula returns TRUE wherever there is bold formatting applied to the cell and FALSE otherwise. Now you can simply filter all the TRUE values (as shown in Method 2)![using custom function to filter cells with bold font formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20361'%3E%3C/svg%3E)

Again! This workbook now has a macro, so save it with .xlsm or .xls extension

_**Try it yourself.. Download the file  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/b0heam03vph048t/FilterBoldCells.xlsm?dl=1)
**_

I hope this will give you enough time for that much-needed coffee break 🙂

Do you know any other way to do this? I would love to learn from you. Leave your thoughts in the comment section and be awesome.

**You May Also Like the Following Excel Tutorials:**

*   [An Introduction to Excel Data Filter Options.](https://trumpexcel.com/excel-data-filter/)
    
*   [Filter By Color in Excel](https://trumpexcel.com/filter-by-color-excel/)
    
*   [Create Dynamic Excel Filter – Extract Data as you type.](https://trumpexcel.com/dynamic-excel-filter/)
    
*   [Creating a Drop Down Filter to Extract Data Based on Selection](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [Filter the Smart Way – Use Advanced Filter in Excel](https://trumpexcel.com/excel-advanced-filter/)
    
*   [Count Cells Based on a Background Color](https://trumpexcel.com/count-colored-cells-in-excel/)
    .
*   [Highlight Blank Cells in Excel.](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [How to Create a Heat Map in Excel.](https://trumpexcel.com/heat-map-excel/)
    
*   [Excel VBA Autofilter](https://trumpexcel.com/vba-autofilter/)
    .
*   [Change the Default Font in Excel](https://trumpexcel.com/change-default-font-excel/)
    
*   [How to Filter Strikethrough in Excel](https://trumpexcel.com/filter-strikethrough-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

32 thoughts on “How to Filter Cells with Bold Font Formatting in Excel (An Easy Guide)”
---------------------------------------------------------------------------------------

1.  None of these commands are present in the current version of Excel for Mac (there’s no “Refers to” field in the Find & Replace dialogue; there’s no “Refers to” window in the Name dialogue; etc.) Thanks anyway, but back to the old drawing board.
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-11881)
    
2.  Thank you so much for this post!!! The simple replace with a cell color worked for me. Saved me tons of time. Thanks again!
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-11877)
    
3.  Thank you very much.
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-11773)
    
4.  Thanks!!!  
    I can use Method 1, 2. But I can use Method 3!!  
    Really Thank you.
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-11439)
    
5.  Nice job. Thanks
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-11434)
    
6.  Thank you so much! I’ve been using Excel since the ’90s and this is the first time I’ve ever had to do this – worked great!
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-11214)
    
7.  I actually want to filter by unbold, not by bold. Is there a way to do that?
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-10883)
    
8.  Fantastic!!
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-10591)
    
9.  Thank you! Folks like you who unselfishly take the time to share tips like this are truly appreciated. 🙂
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-9206)
    
10.  Way useful! Thanks for the info!
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-8875)
    
11.  Hi sumit, better to do a demo and upload it in youtube thanks
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-8844)
    
    *   Will make a video on this soon!
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-8911)
        
12.  Thanks a lot!!!
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-7943)
    
    *   Glad you found this useful!
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-8525)
        
13.  [http://tutorialway.com/microsoft-excel-font-formatting/](http://tutorialway.com/microsoft-excel-font-formatting/)
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-7370)
    
14.  The first option does not exactly work for Excel 2010.  
    However, instead of ‘Choose Format from Cell’ you can select ‘Format’ -> ‘Font’->’Bold’ in Font Style->OK  
    Rest is okay.
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-5814)
    
    *   Thanks for commenting Wazeem.. Why would the first one not work for 2010?
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-8526)
        
15.  Thank you very much, helped me.
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-3255)
    
    *   Glad it helped!
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-8527)
        
16.  Thanks, it helps a lot
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-3179)
    
    *   You’re welcome! 🙂
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-12168)
        
17.  super. This helped to change font in another column. Because the format painter did not work in some cases.
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-2606)
    
18.  Great Tip!
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1844)
    
    *   Thanks for commenting Alec. Glad you liked it!
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1845)
        
19.  Really liking the **Find/Replace** method, just because it’s one less column I have to add to my data set. I still wish Microsoft would give us built-in functions that could analyze cell formats (ie CountIfColor, etc…). I’ll keep dreaming 🙂
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1742)
    
    *   Thanks for commenting Chris.. Find and Replace is my favorite method too.. hassle free and no extra column. And I am right there with you in appealing to the Excel Team to add a feature to filter based on formatting. This has a real world utility.
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1743)
        
20.  v nice thankq.. will use it from now..
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1737)
    
    *   Thanks for commenting Ravi.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1739)
        
21.  woow nice…keep it up dear… 🙂
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1736)
    
    *   Thanks Mehar.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1738)
        
22.  Cool tip 🙂 Thanks for helping me save a lot of time!
    
    [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1734)
    
    *   Thanks Mehar.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#comment-1735)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/filter-bold-font-formatting-in-excel/#respond)

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