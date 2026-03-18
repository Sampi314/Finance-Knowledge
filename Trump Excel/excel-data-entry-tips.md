# 10 Excel Data Entry Tips You Can't Afford to Miss

**Source:** https://trumpexcel.com/excel-data-entry-tips

---

[Skip to content](https://trumpexcel.com/excel-data-entry-tips/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-data-entry-tips/#below-title)

Excel is an amazing tool with fascinating capabilities to analyze data (be it using [functions](https://trumpexcel.com/excel-functions/)
, [charts](https://trumpexcel.com/charting/)
 or [dashboards](https://trumpexcel.com/creating-excel-dashboard/)
). The ease with which data can be entered and stored in Excel makes it a compelling choice.

In this blog post, I have listed 10 useful Excel Data Entry tips that will make you more efficient and save a lot of time.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-data-entry-tips/#)

#1 Use Excel Data Entry Form
----------------------------

[Excel Data Entry form](https://trumpexcel.com/data-entry-form/)
 enables you to add records to an existing data set. It gives a pop-up form that can be filled by the user. It is especially convenient when the data set has many columns and would require you to scroll right and left again and again as you key in data points.

Data Form feature is not already available in Excel ribbon. We first need to make it available by adding it to the [Quick Access toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
.

**Adding Excel Data Entry Form to Quick Access Toolbar**

1.  Go to Quick Access Toolbar, right-click and select Customize quick Access Toolbar.  
    ![Excel Data Entry - Add Data Form](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%2086'%3E%3C/svg%3E)
2.  In the [Excel Options](https://trumpexcel.com/excel-options-hacks/)
     Dialogue box, Select All Commands and Go to Form. Select Form and press Add. This will add the Data Forms Icon to the Quick Access Toolbar.  
    ![Excel Data Entry - Add Data Form from All Commands](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20103'%3E%3C/svg%3E)

**Using Excel Data Entry Form**

1.  Select any cell in the data range and click on the Data Form icon from the Quick Access Toolbar.
2.  In the Pop-up Data form, all the column titles are listed vertically. Fill the data in the adjacent text box for each heading.
3.  Once you have entered the data, press Enter.
4.  Click on New to add a new record.

Using the Excel Data Entry form, you can also navigate through the existing data (row by row), or find data by specifying the criteria (try this by clicking on the criteria button).

Also read: [Prevent Duplicate Entries in Excel](https://trumpexcel.com/prevent-duplicate-entries-excel/)

#2 Quickly Enter Numbers with Fixed Decimal Numbers
---------------------------------------------------

If you are in a situation where you have to manually enter data in Excel that also has a decimal part to it, this trick could be mighty useful.

For example, suppose you have to enter marks for students in percentage with up to 2 decimal points.

You can enable a feature where you just type the numbers without bothering about hitting the dot key every time. To enable this:

1.  Go To File –> Options.
2.  In the [Excel Options](https://trumpexcel.com/excel-options-hacks/)
     Dialogue box, select Advanced.
3.  In Advanced Options, check the option “Automatically Insert a decimal point”.
4.  Specify the number of decimals you want (for example, 2 in this case).

Now, whenever you enter any number, excel automatically places the last 2 digits after the decimal. So 1 becomes .01, 10 becomes 0.1, 100 becomes 1, 2467 becomes 24.67, and so on.

![Excel Data Entry - Add Decimal Automatically](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20132'%3E%3C/svg%3E)

Once you are done with data entry, simply switch it off by unchecking the same option.

#3 Automatically Add Ordinal to Numbers
---------------------------------------

Yes, you can use a combination of Excel functions (such as VALUE, [RIGHT](https://trumpexcel.com/excel-right-function/)
, [IF](https://trumpexcel.com/excel-if-function/)
, [OR](https://trumpexcel.com/excel-or-function/)
) to add ordinals (‘st’ in 1st, ‘nd’ in 2nd, and so on..).

Here is the formula:

\=A1&IF(OR(VALUE(RIGHT(A1,2))={11,12,13}),"th",IF(OR(VALUE(RIGHT(A1))={1,2,3}),CHOOSE(RIGHT(A1),"st","nd","rd"),"th"))

#4 Fill Down Using Control + D
------------------------------

This is a nifty Excel Data Entry trick. If you have to copy the above cell, just press Control + D.

It copies the content as well as the formatting. If there is a formula in the above cell, the formula is copied (with adjusted references).

This works for more than one cell as well. So if you want to copy the entire row above, select the current row and press Control + D.

If you select more than one cell/cells, than the cell above selection is copied to all the cells.

**See Also**: [200+ Excel Keyboard Shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
.

#5 Quickly Enter Date/Time in Excel Cells
-----------------------------------------

Do not remember the current date? Don’t worry; just press **Control + ;** (semicolon Key), and it will enter the current date in the cell.

Similarly, you can enter the current time by using the shortcut **Control + Shift + :** (colon key)

Remember, these are absolute values and won’t change if the date or time changes.

If you want to have a dynamic date and time value that changes whenever you open the workbook or when there is a re-calculation, use [TODAY](https://trumpexcel.com/excel-today-function/)
 and [NOW](https://trumpexcel.com/excel-now-function/)
 functions.

**Also See:** [How to Automatically Insert Date and Time Stamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
.

#6 Control + Enter to Fill Entire Selection with Content in Active Cell
-----------------------------------------------------------------------

When you select multiple cells in Excel, one of the cells with light shade (as compared with the remaining selected cells) is the active cell.

If you enter something in the active cell when the selection is made and press **Control + Enter**, the value is inserted into all the selected cells.

This holds true for [formulas](https://trumpexcel.com/excel-functions/)
 as well. If you enter a formula in the active cell and press Control + Enter, all the cells will get that formula (with adjusted references).

#7 Alt + Down Arrow to Get a List of All Unique Values in that column
---------------------------------------------------------------------

This one can save some time that you might otherwise waste in typing. Suppose you are entering data in a column with activity status (To be Done, Completed).

Instead of typing the status repeatedly, you just need to type it in a couple of cells, and then you can use the keyboard shortcut Alt + Down arrow.

It gives you a list of all the unique entries, and you can quickly select from the list.

![Excel Data Entry - Alt Down Arrow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20268%20180'%3E%3C/svg%3E)

If you want to select from pre-specified options, you can create a [drop down list](https://trumpexcel.com/excel-drop-down-list/)
.

Also read: [Cell References in Excel](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 (Absolute, Relative, and Mixed )

#8 Quickly Sift through Multiple Worksheet Tabs in a Workbook
-------------------------------------------------------------

This one saves tons of time. Simply use the keyboard shortcut Control + Page Up/Page Down to navigate through multiple worksheet tabs in a workbook.

See Also: [200+ Excel Keyboard Shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
.

#9 Enter Long Text by Using Abbreviations
-----------------------------------------

If you have to enter long names or keywords again and again in your worksheet, this trick will come in handy.

For example, you may want that whenever you type ABC, Excel should automatically replace it with ABC Technology Corporation Limited.

Something as shown below:

![Excel Complete Abbreviations - Excel Data Entry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20116'%3E%3C/svg%3E)

This feature can be enabled using the autocorrect options. [Read how to enable it](https://trumpexcel.com/autocorrect/)
.

#10 Enter Data in Non-Contiguous Ranges
---------------------------------------

Suppose you have a [template](https://trumpexcel.com/free-excel-templates/)
 as shown below, and you have to enter data in all the cells highlighted in red, in the order specified by the arrows.

![Enter Data in Excel in Specific Order - Excel Data Entry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20459%20228'%3E%3C/svg%3E)

**Here is a quick way to do this:**

*   Select all the cells where you need to enter the data (press control and then select one by one).
    *   **Start with the second cell in your sequence** of data entry (start with D3). Select the first cell B3 (where data entry begins) at last.
*   Once selected, go to [Name Box](https://trumpexcel.com/name-box-excel/)
     (which is on the left of the formula bar).
*   Type any name without spaces.
*   _That’s It!!_ Select the Named Range by clicking the Name Box drop-down. Now start entering your data and use **Enter/Tab** to jump to the next cell.

[Read more about this trick](https://trumpexcel.com/enter-data-in-excel-in-specific-order/ "Quickly Enter Data in Excel in a Specific Order in Non-Contiguous Cells")
.

These are my top ten excel data entry tips that can significantly improve your productivity and save time.

**You May Also Like the Following Excel Tips:**

*   [10 Super Neat Ways to Clean Data in Excel Spreadsheets.](https://trumpexcel.com/clean-data-in-excel/)
    
*   [24 Daily Excel Issues and their Quick Fixes.](https://trumpexcel.com/24-excel-tricks/)
    
*   [How to Track Changes in Excel.](https://trumpexcel.com/track-changes-in-excel/)
    
*   [How to Recover Unsaved Excel Files](https://trumpexcel.com/recover-unsaved-excel-files/)
    .
*   [How to Enable Conditional Data Entry in Excel.](https://trumpexcel.com/conditional-data-entry-in-excel/)
    
*   [Suffering from Slow Excel Spreadsheets? 10 tips to SPEED-UP your Excel.](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
    
*   [Get more out of Find and Replace in Excel (4 Amazing Tips).](https://trumpexcel.com/find-and-replace-in-excel/)
    
*   [How to Use Excel Freeze Panes in Excel](https://trumpexcel.com/excel-freeze-panes/)
    .
*   [100+ Excel Interview Questions](https://trumpexcel.com/excel-interview-questions/)
    
*   [Fill Down Blank Cells Until the Next Value in Excel](https://trumpexcel.com/fill-down-blank-cells-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

12 thoughts on “10 Excel Data Entry Tips You Can’t Afford to Miss”
------------------------------------------------------------------

1.  Great post. this tips is very helpful for data entry jobs. Placementindia.com is best portal for find wide list of data entry jobs.
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-14434)
    
2.  Hi Sumit!  
    I am very grateful for your videos, they are extremely helpful for me especially in Finance/Treasury. I do have a question though, I use excel Solver now for this issue, but I find it quite inefficient because it doesn’t give me the right combination. How can I verify which combination of values (amounts) in a column that adds up to a specific value (Amount) in a cell? Is there any VBA code, I can use for this? Thanks a lot for your help!  
    For instance, the sum of invoices amounts that add up to an amount paid by a client. without me knowing before hands the invoices number/refs.
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-14118)
    
3.  It is good , really a tim
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-13909)
    
4.  it helps in time saving , really good
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-13908)
    
5.  it helps in time saving , really good
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-13907)
    
6.  Mujay Vo sutro ko dakhna hai jaise  
    sum=(n1.n2)  
    Minimam =  
    Maxim bale suyr
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-13176)
    
7.  Are you looking for Business Leads , data entry of specific criteria?
    
    Well, I am providing targeted Business Leads,(Company Name,Website,Business Phone Number,Direct Email address) data entry of your Specific Criteria/Location(Zip Code,City,State,Country) with high accuracy.  
    Check it out! tajnur2 will data entry, lead generation, for your targeted Business for $5 on #Fiverr [https://www.fiverr.com/s2/1d0d98a8b2](https://www.fiverr.com/s2/1d0d98a8b2)
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-9368)
    
8.  THANKS SO MUCH, YOU CREATING BETTER ACCOUNTANTS
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-1532)
    
    *   Hehe.. Thanks Divine.. This is definitely one of the best comments I have got so far 🙂
        
        [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-1533)
        
9.  #7 is a game changer for me!!! Wish I knew that shortcut years ago! Great list Sumit 🙂
    
    [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-1510)
    
    *   Thanks Chris.. #7 is indeed an awesome one.. I use it all the time now 🙂
        
        [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-1511)
        
    *   Indeed. It’s a real time saver
        
        [Reply](https://trumpexcel.com/excel-data-entry-tips/#comment-3621)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-data-entry-tips/#respond)

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