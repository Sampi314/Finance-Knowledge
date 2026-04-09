# How to Lock Formulas in Excel (a Step-by-Step Guide)

**Source:** https://trumpexcel.com/lock-formulas-excel

---

[Skip to content](https://trumpexcel.com/lock-formulas-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/lock-formulas-excel/#below-title)

**Watch Video – How to Lock Formulas in Excel**

Excel formulas are easy to create and edit in Excel.

You can easily edit a formula through the formula bar or directly in the cell.

While this makes it convenient to create formulas in Excel, it comes with a few disadvantages as well.

Consider this.

You are going through a worksheet full of formulas, and you accidentally hit the delete key, or backspace key, or some other number/alphabet key.

Now you’ll be lucky if you’re able to spot the error and correct it. But if you are not, it may lead to some erroneous results.

And let me tell you this, errors in Excel have cost millions to companies (read [this](https://www.theregister.co.uk/2003/06/19/excel_snafu_costs_firm_24m/)
 or [this](http://ww2.cfo.com/spreadsheets/2014/10/spreadsheet-error-costs-tibco-shareholders-100m/)
).

The chances of such errors increase multifold when you share a file with colleagues or managers or clients.

One of the ways to prevent this from happening is to [lock the worksheet and all the cells](https://trumpexcel.com/lock-cells-in-excel/)
. However, doing this would prevent the user from making any changes to the worksheet. For example, if you’re sending a workbook to your manager for review, you may want to allow him to add his comments or change some cells.

A better workaround to this is to lock only those cells that have formulas in it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/lock-formulas-excel/#)

How to Lock Formulas in Excel
-----------------------------

Before I show you how to lock formulas in Excel, here is something you must know:

By default, all the cells are locked in Excel. Only when you protect the locked cells can you truly restrict the user from making changes. This also means that if a cell is not locked and you protect it, the user would be able to make changes.

Here are the steps to lock formulas in Excel (explained in detail later on):

1.  Select all the cells and unlock these.
2.  Select all the cells that have formulas (using Go To Special).
3.  Lock these selected cells.
4.  Protect the worksheet.

Now that I have outlined the steps above, let’s dive in and see how to do this (and more importantly, why we must do this):

### Step 1: Select All the Cells and Unlock it

While you may find it confusing, bear with me and keep reading.

As I mentioned, only the cells that are locked as well as protected can truly be restricted. If all the cells are locked, and I protect the entire worksheet, it would mean a user can’t change anything.

But we only want to lock (restrict access) to the cells that have formulas in it.

To do this, we first need to unlock all the cells and then select and lock only those cells that have formulas in it.

Here are the steps to unlock all the cells:

*   Select all the cells in the worksheet (use the keyboard shortcut Control + A).
*   Use the keyboard shortcut Control + 1 (hold the Control key and then press 1). This will open the format cells dialog box.
*   In the format cells dialog box, select the Protection tab.![How to Lock Formulas in Excel - Protection tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20460'%3E%3C/svg%3E)
*   Uncheck the ‘Locked’ option.![How to Lock Formulas in Excel - Unchek Locked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20460'%3E%3C/svg%3E)
*   Click ok.

### Step 2: Select All the Cells that Have Formulas

Now that all the cells have been unlocked, we need to make sure that the cells that have formulas are locked.

To do this, we need to first select all the cells with formulas.

Here are the steps to select all the cells that have formulas:

*   Select all the cells in the worksheet (use Control + A).
*   Go to Home and within the Editing group, click on Find & Select.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%2097'%3E%3C/svg%3E)
*   From the drop-down, select Go to Special.![How to Lock Formulas in Excel - Go to special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20211%20349'%3E%3C/svg%3E)
*   In the Go To Special dialog box, select Formulas.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20314%20325'%3E%3C/svg%3E)
*   Click OK.

This would select all the cells that have formulas in it.

### Step 3: Lock the Cells with Formulas

Now that we have selected the [cells with formulas](https://trumpexcel.com/highlight-cells-with-formulas-excel/)
, we need to go back and lock these cells (enable the lock property that we disabled in step 1).

Once we do this, protecting the worksheet would lock these cells that have formulas, but not the other cells.

Here are the steps to Lock Cells with Formulas:

*   With the cells with formulas selected, press Control + 1 (hold the Control key and then press 1).
*   In the format cells dialog box, select the Protection tab.![How to Lock Formulas in Excel - Protection tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20460'%3E%3C/svg%3E)
*   Check the ‘Locked’ option.![How to Lock Formulas in Excel - locked](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20460'%3E%3C/svg%3E)
*   Click ok.

### Step 4 – Protect the Worksheet

Now that the ‘Locked’ property is enabled for cells with formulas (and not for other cells), protecting the entire worksheet would only restrict access to the cells with formulas.

Here are the steps to protect the worksheet:

*   Go to the Review tab.![How to Lock Formulas in Excel - review](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20125'%3E%3C/svg%3E)
*   Click on Protect Sheet.![How to Lock Formulas in Excel - Protect Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20497%20132'%3E%3C/svg%3E)
*   In the Protect Sheet dialog box, make sure the option ‘Protect worksheet and contents of the locked cells’ is checked.![How to Lock Formulas in Excel - protect worksheet and content](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20303'%3E%3C/svg%3E)
*   \[Optional\] Specify the password.
*   Click OK.

Once you are done with the above four steps, all the cells that have formulas would be locked, and the user wouldn’t be able to change anything in it.

If the user tries to change the cells, he/she will get a prompt as shown below:

![How to Lock Formulas in Excel - locked prompt](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20116'%3E%3C/svg%3E)

Also read: [How to Freeze Multiple Columns in Excel](https://trumpexcel.com/freeze-multiple-columns-excel/)

How to Hide Formulas in Excel
-----------------------------

When you lock formulas in Excel, the user can’t make any changes to the cells with formulas.

However, if that cell is selected, the formula in the cell would be visible in the formula bar.

While this isn’t an issue in most cases, but if you don’t want the formula to be visible, you need to hide it.

Here are the steps to [hide formulas](https://trumpexcel.com/hide-formulas-excel/)
 in locked cells:

*   Select all the cells in the worksheet (use Control + A).
*   Go to Home and within the Editing group, click on Find & Select.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%2097'%3E%3C/svg%3E)
*   From the drop-down, select Go to Special.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20211%20349'%3E%3C/svg%3E)
*   In the Go To Special dialog box, select Formulas.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20314%20325'%3E%3C/svg%3E)
*   Click OK. This will select all the cells that have formulas in it.
*   Press Control + 1 (hold the control key and then press 1). This will open the format cells dialog box.
*   In the Format Cells dialog box, go to the Protection tab.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20460'%3E%3C/svg%3E)
*   Check the Hidden option.![How to Lock Formulas in Excel - hidden](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20460'%3E%3C/svg%3E)
*   Click OK.

Now, when the user selects a cell that has a formula and is locked, he/she will not be able to see the formula in the formula bar.

Note: As mentioned earlier, a cell that has not been locked cannot be protected. The same applies when you hide formulas in Excel. Unless the cell is locked, only checking the Hidden checkbox wouldn’t do anything. To truly hide formulas in Excel, the cells should have the Locked and Hidden check boxes selected, and then it should be protected.

**You May Also Like the Following Excel Tutorials:**

*   [Lock Rows/Columns using Excel Freeze Panes.](https://trumpexcel.com/excel-freeze-panes/)
    
*   [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    .
*   [Unlock VBA Project in Excel (without password)](https://trumpexcel.com/excel-vba/remove-password/)
    
*   [Show Formulas in Excel Instead of the Values](https://trumpexcel.com/show-formulas-in-excel/)
    .
*   [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)
    .
*   [Unhide Columns in Excel](https://trumpexcel.com/unhide-columns/)
    
*   [Unprotect Excel Sheets Without Password](https://trumpexcel.com/unprotect-excel-sheets-without-password/)
    
*   [How to Lock Row Height & Column Width in Excel](https://trumpexcel.com/lock-row-height-column-width-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

35 thoughts on “How to Lock Formulas in Excel (a Step-by-Step Guide)”
---------------------------------------------------------------------

1.  Thank you, I found that very helpful. I am left with one problem. On the sheets that are protected, I (and others) can enter values into the unprotected cells, but a lot of other functions are greyed out, like formatting. For instance, I had a cell in red because I had a query. Once that query was solved, I can’t change the cell back to black without unprotecting the sheet.  
    How do I get round this please?
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-40794)
    
2.  thank you. indeed very useful. Can you please tell us if we can prevent editing the cells based on dates?
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-14819)
    
3.  Thanks for the video, this was Exactly what we were looking for, how to lock cell’s with formulas. And thanks for the bonus info, on how to hide the formulas.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-14659)
    
4.  Thanks for the Great tutorial! follow the steps and this will work.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-14510)
    
5.  Great video, thank you!
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-13778)
    
6.  Exel lent tutorial. Very well exposed, explained and illustrated. Highly recommended. Thank you.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-13217)
    
7.  I enter the same formula in cell C1, C2, and C3. For example:
    
    \=A1\*B2
    
    On Monday I enter into A1: 12  
    Enter into B2: 10  
    I get an answer of 120 in cells C1, C2, and C3.  
    Perfect.  
    On Tuesday I have a new set of numbers for a different result.  
    But I need to save the answer of 120 from Monday in cell C1.  
    How can I lock that cell so that when I enter my new data into A1 and B2 it doesn’t change the answer from the previous day in cell C1 (120), it only enters the new data in cell C2 and C3?
    
    I have multiple cells using the same formula but I need to save the results in each cell and protect it from changing when I enter new numbers in the other cells using the same formula.  
    Is it possible?  
    Please help!  
    208-610-3300  
    Thank you,  
    Leigh Britton
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-13068)
    
8.  Thank you, very cool and easy to follow!
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-13038)
    
9.  Thanks for freely sharing your vast knowledge of Excel here! I bet I visit this site at least monthly; there is always something new to know! With gratitude, Bx
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12992)
    
10.  Once you lock the formulas the entire sheet gets locked and I can’t seem to input figures. So, I have a formula in the total=SUM(O6:T6). I need people to input their projections in cells O6:T6. When I lock the sheet and formulas, I cannot put figures in the other cells. Please advise
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12705)
    
    *   Hi Jayshree, The same question to yours. Do you find out the way to solve it?
        
        [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12893)
        
        *   This worked perfectly for me, I followed the above directions and only locked the cells with the formulas. If there is a formula in a cell no one should be entering any information in that cell. following the logic above if inputting in O6:T6 the locked cell should actually be s6 with the formula. The search for only formulas was the magic.
            
            [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-14511)
            
11.  Dear how we can exclude a cell from total; this cell also have formula for calculation like =300000-(50000+10000)
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12689)
    
12.  Hi thank you for explanations. When I use these steps everything works as expected … but I discovered that I loose filtering feature for my columns which I still need to have. Is there workaround?
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12654)
    
13.  Is there a way to lock the cells but still insert rows WITH AN AUTOPOPULATING FORMULA? I have a budget worksheet with columns A-J and Rows 3-33. Columns that have entry fields include:  
    B – Average Cost for row 1, 2, 3…  
    C – Option “fixed” or “variable” cost  
    D – Range of variance if variable cost
    
    Columns E-J include:  
    E – Maximum cost for row 1, 2, 3…  
    F – Minimum cost for row 1, 2, 3…  
    G – Rows are divided into “groups” to indicate budget category. Column G sums total costs for category  
    H – Calculates % of budget allowance OR total costs  
    I, J – calculate above percentage using maximum/minimum cost calculations
    
    Each group/category currently has four rows allotted, but users might need to add row(s) if there are more costs in that category. (Example: For housing costs I might have a row for 1) mortgage 2)electricity 3) utilities 4) maintenance 5) Project X fund 6) Security, etc.). Columns E-J are all formulas that don’t need to be touched, but that need to be “carried down” if user adds a row.
    
    I tried a macro that auto-populates auto-adds a row with formulas using a double click, and that works well…when the sheet isn’t protected. I also tried setting it up as a table and that works fine, too, until I protect the sheet/associated formula columns. Despite giving permissions to add/delete new rows, columns, etc. an error message appears when I try to run the macro. Manually inserting a row – both using the macro version and the table version – results in a new row without the formulas.
    
    It seems like there’s got to be a workaround as this seems like a pretty basic function for a straight-forward spreadsheet. Any insight or advice?
    
    Thanks so much!
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12445)
    
    *   I’m curious for this answer, I decided for a work around to add an extra blank column with all of the formulas in it I can use if needed. I would like to protect my formatting but alas its late and I need to rest these eyes and this overloaded brain. Enuf fun for the evening. Cheers
        
        [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-14512)
        
14.  Hi,
    
    Enjoyed the video – very helpful.
    
    Can I protect a cell so that the formula can not be removed but I can still change the source data to reflect a new value in the cell?
    
    Is this the “hidden” feature?
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12421)
    
15.  Hi this is a simple way of understanding. I also would like to know how to lock the formulas in multiple sheets at a time which are in one work book. Like in one work book, sheet 1, sheet 2,….. sheet 30.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12307)
    
16.  Thank you!
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12242)
    
17.  excellent support! it was so easy for me to follow through. Many thanks!
    
    Chirac
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12040)
    
18.  Very helpful tutorial. thanks!
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11524)
    
19.  Your instruction locks the entire worksheet.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11489)
    
20.  Hello sir  
    I am a businessman and daily I use Excel I need your help in making it better as well as I want to access the files on my mobile too so can I get you mobile no so I can send you my Excel to understand it better
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11462)
    
21.  I am trying to figure out how to simulate a basketball score spread sheet that will generate a random score between selected integers for each of four quarters (or two halves) for several different teams during a playoff tournament. I know how to generate random numbers and to total the four quarter scores but how can I repeat this several times for each of 16 (or more) playoff games? I am fascinated by these formulas.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11336)
    
22.  The article proved very helpful. It gave me all what i wanted. Very clear and easy to understand instructions. Thank you.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11287)
    
23.  i have a formula, =Ordersinhouse!H126, that fills in a cell, i want to fill in the cell with this data but want to block/lock keyboard entries in this cell, is this possible?
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11124)
    
24.  This is so helpful, simple clear and concise instructions. Makes me look like an expert. Thank you so much
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11070)
    
    *   Thank you for the kind words Priscilla! Glad you found the tutorial useful.
        
        [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-11071)
        
25.  Can this be applied to an entire FILE, not just the worksheet?
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-10426)
    
    *   it can be applied to the whole file. so in order to do that, you have to select worksheet locked instead of Spread Sheet Lock
        
        [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-12332)
        
26.  Thank you! I just found your site, and it has already helped me immensely.
    
    Your instructions are wonderfully clear and detailed just enough without going overboard. Awesome!
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-10111)
    
    *   Glad you found it useful!
        
        [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-10112)
        
27.  Hi. Nice article. There is no thing more evil to do than to hardcode a value to a verification column.
    
    There is a typo in the section How to Lock Formulas in Excel in the second step 2. Select all the cells that have formulas (using paste special). It should be Go To Special, not paste special. Typo can cause confusion.
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-9118)
    
28.  Many thanks for you, Awesome Tips
    
    [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-9096)
    
    *   Very nice and simple.
        
        [Reply](https://trumpexcel.com/lock-formulas-excel/#comment-13861)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/lock-formulas-excel/#respond)

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