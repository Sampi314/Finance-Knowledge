# How to Quickly Insert Date and Timestamp in Excel

**Source:** https://trumpexcel.com/date-timestamp-excel

---

[Skip to content](https://trumpexcel.com/date-timestamp-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/date-timestamp-excel/#below-title)

A timestamp is something you use when you want to track activities.

For example, you may want to track activities such as when was a particular expense incurred, what time did the sale invoice was created, when was the data entry done in a cell, when was the report last updated, etc.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/date-timestamp-excel/#)

Let’s get started.

Keyboard Shortcut to Insert Date and Timestamp in Excel
-------------------------------------------------------

If you have to insert the date and timestamp in a few cells in Excel, doing it manually could be faster and more efficient.

Here is the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 to quickly enter the current Date in Excel:

**Control + :** (hold the control key and press the colon key).

Here is how to use it:

*   Select the cell where you want to insert the timestamp.
*   Use the keyboard shortcut **Control + :**
    *   This would instantly insert the current date in the cell.

![Automatically insert Timestamp in Excel - Keyboard shortcut](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20216'%3E%3C/svg%3E)

A couple of important things to know:

*   This shortcut would only insert the current date and not the time.
*   It comes in handy when you want to selectively enter the current date.
*   It picks the current date from your system’s clock.
*   Once you have the date in the cell, you can apply any date format to it. Simply go to the ‘Number Format’ drop-down in the ribbon and select the date format you want.

Note that this is not dynamic, which means that it will not refresh and change the next time you open the workbook. Once inserted, it remains as a static value in the cell.

While this shortcut does not insert the timestamp, you can use the following shortcut to do this:

**Control + Shift + :**

This would instantly insert the current time in the cell.

![Automatically insert date and Timestamp in Excel - shift-control-colon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20624%20228'%3E%3C/svg%3E)

So if you want to have both date and timestamp, you can use two different cells, one for date and one for the timestamp.

Using TODAY and NOW Functions to Insert Date and Timestamps in Excel
--------------------------------------------------------------------

In the above method using shortcuts, the date and timestamp inserted are static values and don’t update with the change in date and time.

If you want to update the current date and time every time a change is done in the workbook, you need to use [Excel functions](https://trumpexcel.com/excel-functions/)
.

This could be the case when you have a report and you want the printed copy to reflect the last update time.

### Insert Current Date Using TODAY Function

To insert the current date, simply enter [\=TODAY()](https://trumpexcel.com/excel-today-function/)
 in the cell where you want it.

![Automatically insert Timestamp in Excel - Using Today Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20228'%3E%3C/svg%3E)

Since all the dates and times are stored as numbers in Excel, make sure that the cell is formatted to display the result of the TODAY function in the date format.

To do this:

*   Right-click on the cell and select ‘Format cells’.![Automatically insert Timestamp in Excel - format cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20431'%3E%3C/svg%3E)
*   In the Format Cells dialog box, select Date category in the Number tab.![Automatically insert Timestamp in Excel - date-category](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20467'%3E%3C/svg%3E)
*   Select the required date format (or you can simply go with the default one).
*   Click OK.

Note that this formula is [volatile](https://trumpexcel.com/excel-volatile-formulas/)
 and would recalculate every time there is a change in the workbook.

### Insert Date and Timestamp Using NOW Function

If you want the date and timestamp together in a cell, you can use the [NOW function](https://trumpexcel.com/excel-now-function/)
.

![Automatically insert date and Timestamp in Excel - now function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20228'%3E%3C/svg%3E)

Again, since all the dates and times are stored as numbers in Excel, it is important to make sure that the cell is formatted to have the result of the NOW function displayed in the format that shows the date as well as time.

To do this:

*   Right-click on the cell and select ‘Format cells’.
*   In the Format Cells dialog box, select ‘Custom’ category in the Number tab.
*   In the Type field, enter _dd-mm-_yyyy _hh:mm:ss![insert-date-and-timestamp-in-excel-custom-format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20467'%3E%3C/svg%3E)_
*   Click OK.

This would ensure that the result shows the date as well as the time.

Note that this formula is volatile and would recalculate every time there is a change in the workbook.

Circular References Trick to Automatically Insert Date and Timestamp in Excel
-----------------------------------------------------------------------------

One of my readers Jim Meyer reached out to me with the below query.

_“Is there a way we can automatically Insert Date and Time Stamp in Excel when a data entry is made, such that it does not change every time there is a change or the workbook is saved and opened?”_

This can be done using the keyboard shortcuts (as shown above in the tutorial). However, it is not automatic. With shortcuts, you’ll have to manually insert the date and timestamp in Excel.

To automatically insert the timestamp, there is a smart technique using circular references (thanks to Chandoo for this wonderful [technique](http://chandoo.org/wp/2009/01/08/timestamps-excel-formula-help/)
).

Let’s first understand what a [circular reference](https://trumpexcel.com/find-circular-reference-excel/)
 means in Excel.

Suppose you have a value 1 in cell A1 and 2 in cell A2.

Now if you use the formula =A1+A2+A3 in cell A3, it will lead to a circular reference error. You may also see a prompt as shown below:

![circular reference prompt in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20992%20161'%3E%3C/svg%3E)

This happens as you are using the cell reference A3 in the calculation that is happening in A3.

Now, when a circular reference error happens, there is a non-ending loop that starts and would have led to a stalled Excel program. But the smart folks in the Excel development team made sure that when a circular reference is found, it is not calculated and the non-ending loop disaster is averted.

However, there is a mechanism where we can force Excel to at least try for a given number of times before giving up.

Now let’s see how we can use this to automatically get a date and timestamp in Excel (as shown below).

![inserting the date and time automatically using circular reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20240'%3E%3C/svg%3E)

Note that as soon as I enter something in cells in column A, a timestamp appears in the adjacent cell in column B. However, if I change a value anywhere else, nothing happens.

Here are the steps to get this done:

*   Go to File –> Options.![insert-date-and-timestamp-in-excel-options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20303%20389'%3E%3C/svg%3E)
*   In the Excel Options dialog box, select Formulas.![Changing formulas settings in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20274'%3E%3C/svg%3E)
*   In the Calculated options, check the Enable iterative calculation option.![Enable iterative calculation in Excel for inserting timestamps](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20827%20257'%3E%3C/svg%3E)
*   Go to cell B2 and enter the following formula:
    
    \=IF(A2<>"",IF(B2<>"",B2,NOW()),"")
    

That’s it!

Now when you enter anything in column A, a timestamp would automatically appear in column B in the cell adjacent to it.

![insert-date-and-timestamp-in-excel-timestamp-demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20240'%3E%3C/svg%3E)

With the above formula, once the timestamp is inserted, it doesn’t update when you change the contents of the adjacent cell.

If you want the timestamp to update every time the adjacent cell in Column A is updated, use the below formula (use **Control + Shift + Enter** instead of the Enter key):

\=IF(A2<>"",IF(AND(B2<>"",CELL("address")=ADDRESS(ROW(A2),COLUMN(A2))),NOW(),IF(CELL("address")<>ADDRESS(ROW(A2),COLUMN(A2)),B2,NOW())),"")

![insert-date-and-timestamp-in-excel-timestamp-update-demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20240'%3E%3C/svg%3E)

This formula uses the CELL function to get the reference of the last edited cell, and if it’s the same as the one to the left of it, it updates the timestamp.

Note: When you enable iterative calculations in the workbook once, it will be active until you turn it off. To turn it off, you need to go to Excel Options and uncheck the ‘Enable iterative calculation’ option.

Using VBA to Automatically Insert Timestamp in Excel
----------------------------------------------------

If VBA is your weapon of choice, you’ll find it to be a handy way to insert a timestamp in Excel.

VBA gives you a lot of flexibility in assigning conditions in which you want the timestamp to appear.

Below is a code that will insert a timestamp in column B whenever there is any entry/change in the cells in Column A.

'Code by Sumit Bansal from https://trumpexcel.com
Private Sub Worksheet\_Change(ByVal Target As Range)
On Error GoTo Handler
If Target.Column = 1 And Target.Value <> "" Then
Application.EnableEvents = False
Target.Offset(0, 1) = Format(Now(), "dd-mm-yyyy hh:mm:ss")
Application.EnableEvents = True
End If
Handler:
End Sub

This code uses the [IF Then construct](https://trumpexcel.com/if-then-else-vba/)
 to check whether the cell that is being edited is in column A. If this is the case, then it inserts the timestamp in the adjacent cell in column B.

Note that this code would overwrite any existing contents of the cells in column B. If you want. You can modify the code to add a message box to show a prompt in case there is any existing content.

**Where to Put this Code?**

This code needs to be entered as the worksheet change event so that it gets triggered whenever there is a change.

To do this:

*   Right-click on the [worksheet tab and select View Code (or use the keyboard shortcut Alt + F11 and then double click on the sheet name](https://trumpexcel.com/get-sheet-name-excel/)
     in the project explorer).![insert-date-and-timestamp-in-excel-sheet-right-click](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20204%20275'%3E%3C/svg%3E)
*   Copy-paste this code into the code window for the sheet.![insert-date-and-timestamp-in-excel-worksheet-change-code2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20828%20265'%3E%3C/svg%3E)
*   Close the VB Editor.

Make sure you save the file with .XLS or .XLSM extension as it contains a macro.

Creating a Custom Function to Insert Timestamp
----------------------------------------------

Creating a custom function is a really smart way of inserting a timestamp in Excel.

It combines the power of VBA with functions, and you can use it like any other worksheet function.

Here is the code that will create a custom “Timestamp” function in Excel:

'Code by Sumit Bansal from http://trumpexcel.com
Function Timestamp(Reference As Range)
If Reference.Value <> "" Then
Timestamp = Format(Now, "dd-mm-yyy hh:mm:ss")
Else
Timestamp = ""
End If
End Function

**Where to Put this Code?**

This code needs to be placed in a module in the VB Editor. Once you do that, the Timestamp function becomes available in the worksheet (just like any other regular function).

Here are the steps to place this code in a module:

*   Press ALT + F11 from your keyboard. It will open the VB Editor.
*   In the Project Explorer in VB Editor, right-click on any of the objects and go to Insert –> Module. This will insert a new module.![insert-date-and-timestamp-in-excel-insert-module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20466%20428'%3E%3C/svg%3E)
*   Copy-paste the above code in the module code window.![insert-date-and-timestamp-in-excel-code-in-module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20704%20255'%3E%3C/svg%3E)
*   Close the VB Editor or press ALT + F11 again to go back to the worksheet.

Now you can use the function in the worksheet. It will evaluate the cell to its left and insert the timestamp accordingly.

![insert-date-and-timestamp-in-excel-timestamp-formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%20244'%3E%3C/svg%3E)

It also updates the timestamp whenever the entry is updated.

Make sure you save the file with .XLS or .XLSM extension as it contains VB code.

Hope you’ve found this tutorial useful.

Let me know your thoughts in the comments section.

**You May Also Like the Following Excel Tutorials and Resources:**

*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    .
*   [How to Create and Use an Excel Add-ins](https://trumpexcel.com/excel-add-in/)
    .
*   [Select Multiple Items from a Drop Down List in Excel](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    .
*   [Inserting Date and Timestamp in Google Sheets.](https://spreadsheetpoint.com/insert-timestamps-in-google-sheets/)
    
*   [A Collection of FREE Excel Templates](https://trumpexcel.com/free-excel-templates/)
    .
*   [Excel Timesheet Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Excel Calendar Template](https://trumpexcel.com/calendar-template/)
    .
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Autofill Only Weekday Dates in Excel (Formula)](https://trumpexcel.com/autofill-only-weekday-dates-excel/)
    
*   [Make VBA Code Pause or Delay (Using Sleep / Wait Commands)](https://trumpexcel.com/vba-sleep-wait/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

61 thoughts on “How to Quickly Insert Date and Timestamp in Excel”
------------------------------------------------------------------

1.  so amazing
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-14467)
    
2.  All of this is very clever and I even got it all to work using VBA to insert a time in a column to the right of where I entered some data. Perfect but .. How can you protect your code, as you can see it and edit it by doing View Code, even if the sheet and/or workbook is protected? Also when I saved it and then re-opened the worksheet it stopped working – what have I done wrong? Wonderful stuff!! Thank you.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-14337)
    
3.  Thank you awesome work i know its hard to get these formulas running how you like and i just wanted to thank you for letting people like me steal them off the web 🙂
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-14237)
    
4.  Doesn’t work in Online Excel ?
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-13659)
    
5.  What if I want to check a range of cells B2 – G2 and if any are updated, update the date and timestamp?
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-13353)
    
6.  Thank you for all the instructions, I used this option
    
    \=IF(A2″”,IF(AND(B2″”,CELL(“address”)=ADDRESS(ROW(A2),COLUMN(A2))),NOW(),IF(CELL(“address”)ADDRESS(ROW(A2),COLUMN(A2)),B2,NOW())),””)
    
    Works fine, but after keeping the sheet open for a few hours, while updating it, the timestamp gives an #N/A error and can’t get it back.
    
    I use the VBA timestamp function to get over this, seems to be working fine…
    
    Any ideas?
    
    Thank you
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12977)
    
7.  For Timestamp Update Formula:
    
    \=IF(B4″”,IF(AND(F4″”,CELL(“address”)=ADDRESS(ROW(B4),COLUMN(F4))),NOW(),IF(CELL(“address”)ADDRESS(ROW(B4),COLUMN(B4)),F4,NOW())),””)
    
    Works fine when it is on the same sheet, but its not working for different sheet even after changing the reference all B4 into Sheet1!B4 and looking output in the Sheet 2 in F4 Cell
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12833)
    
8.  This has worked perfect for what I was trying to create. I now have the problem of the timestamp resetting each time I reopen the file. Is there a way for the timestamp to stay the same from when the data was put in?
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12815)
    
    *   Disregard…
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12816)
        
9.  Hi
    
    I need a timestamp on “C” that updates the time when either “A” or “B” is updated. I can’t use a macro as I need my file in Sharepoint and to be accessible by many people at the same time.
    
    How can I use the circular reference or the Custom Function for this purpose?
    
    Thanks!
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12737)
    
10.  it working fine with me, however i have issue when using auto-filter or Auto-clear-filter function for designated table, it will keep updating the timestamp in all timestamp reference cells…
    
    below sub :  
    ——————————————————————–  
    Sub Access\_Filter()
    
    Dim WeekS As String  
    Dim WeekE As String
    
    WeekS = “>=” & Application.InputBox(Prompt:=”Enter Start Date”, Default:=Format(Date, “dd mmm yyyy”), Type:=2)  
    WeekE = “<=" & Application.InputBox(Prompt:="Enter End Date", Default:=Format(Date, "dd mmm yyyy"), Type:=2)
    
    ActiveSheet.ListObjects("ACCESS").Range.AutoFilter Field:=3, Criteria1:=WeekS, Operator:=xlAnd, Criteria2:=WeekE
    
    End Sub  
    ———————————————————————————-  
    Sub Access\_Clear\_All\_Filters\_Range()
    
    'To Clear All Fitlers use the ShowAllData method for  
    'for the sheet. Add error handling to bypass error if  
    'no filters are applied. Does not work for Tables.  
    On Error Resume Next  
    ActiveSheet.ListObjects("ACCESS").Range.AutoFilter Field:=3  
    On Error GoTo 0  
    ActiveSheet.ListObjects("ACCESS").Range.End(xlDown).Select
    
    End Sub
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12564)
    
    *   I am having this issue too. I am using it in a table and every time i change filters, it updates to the current time.
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12817)
        
11.  Great job thanks!
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12418)
    
12.  How to put an start date and time with end date and time? Same as above with duration.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12408)
    
13.  Hi guys, I tried to apply the formula below. It works and i saved my macro excel. But when I opened my file (1st time after the file created) the macro was put to disable. when i enable it then the timestamp reset. It also happened when the file was opened from other user which using the same network folder. any idea how to prevent the timestamp reset?
    
    Function Timestamp(Reference As Range)  
    If Reference.Value “” Then  
    Timestamp = Format(Now, “dd-mm-yyy hh:mm:ss”)  
    Else  
    Timestamp = “”  
    End If  
    End Function
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12253)
    
    *   Same issue not sure if anyone found a solution.
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12395)
        
14.  For the formula  
    \=IF(A2″”,IF(AND(B2″”,CELL(“address”)=ADDRESS(ROW(A2),COLUMN(A2))),NOW(),IF(CELL(“address”)ADDRESS(ROW(A2),COLUMN(A2)),B2,NOW())),””)
    
    is it possible to change “A2” to a range of cells?
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12127)
    
    *   I agree is it possible to add a list of cells that are changed and record the dates the they were changed??
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-13713)
        
15.  For the formula  
    \=IF(A2″”,IF(AND(B2″”,CELL(“address”)=ADDRESS(ROW(A2),COLUMN(A2))),NOW(),IF(CELL(“address”)ADDRESS(ROW(A2),COLUMN(A2)),B2,NOW())),””)
    
    is it possible to change “A2” to a range of cells?  
    I would like to use “A2:M2” as the affected cells, so the timestamp updates when any one of that range of cells is modified. I tried to change it but it would not work.  
    I added another set of parentheses to each A2:M2 range, still no luck.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11682)
    
    *   H i Ron, I had the same problem and fixed it by adding an OR within the AND expression like:
        
        In an example field C2 is also ‘monitored’ for change.  
        It is a formula mess but it works.
        
        \=IF(A2″”,IF(AND(B2″”,OR(CELL(“address”)=ADDRESS(ROW(A2),COLUMN(A2)),CELL(“address”)=ADDRESS(ROW(C2),COLUMN(C2)))),NOW(),IF(CELL(“address”)ADDRESS(ROW(A2),COLUMN(A2)),B2,NOW())),””)
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12262)
        
16.  Hi Guys i’m looking for something similar the point of difference is as follows … eg There is a column A which is part of a table where it records a series of values based on a formula. values are “text 1″,”text2″ text3” etc . What i want is in column b, should the value in corresponding Acell reaches “text3” then it records the date when the cell reached “Text 3” else blank. Can anyone help…
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11562)
    
17.  excellent!
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11528)
    
18.  Hi, Sumit.Greetings!!  
    I’m preparing a worksheet to enter all the received purchase orders & associated details viz. customer name, item type, item drawing no., drawing revision no. in po, etc. Say BOOK1  
    When all the relevant data is entered then I get ” found-clear” in column O & now all the data related to that entry is to be extracted to another book, say BOOK-2.  
    Also extracted data should appear in BOOK-2 in a sequential manner, without blank rows & as any entry is cleared in BOOK-1(PO entry workbook), it should appear in BOOK-2 below all the previously extracted entries.
    
    To solve this, I thought of getting :  
    1) Fixed, non-volatile timestamps as soon as ” found-clear” appears in column O for any PO entry.  
    2) To give Rank to these timestamps, using Rank Function.  
    3) Then use Index, Match, Rows to extract data in a sequential sorted manner.
    
    To get fixed( non-volatile) timestamps I applied two approaches as shown by you:  
    1) Circular reference with NOW()  
    2) UDF
    
    I’ve attached an excel file with two sheets:  
    1) Examples  
    2) Application
    
    Problem 1) with circular reference & NOW()
    
    1A) Also if I change conditions so that “found-clear” is removed & then recreate the conditions to get “found-clear” back, timestamp disappears.
    
    Problem 2) with UDF; refer sheet” examples”, SAMPLE-3  
    2A) It is showing the year as 1989 in place of 2019.  
    2B) If I make any changes to the worksheet, like add or remove cells anywhere in the worksheet, all the timestamps change to current time & date.  
    2C) Rank function not working.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11451)
    
19.  Guys,
    
    I have a different requirement and this is for stock market.
    
    Let us say I have Columns A to G in the excel sheet and the columns heading reading as below for stock market :
    
    Symbol, Lot Size, Open, High, Low, LTP and the Signal Column (which gives Buy or Sell based on a strategy).
    
    The last column which is the Signal Column (and which happens to be Column G) contains the “Buy”or “Sell” or Ëmpty when there is no signal. This column is dynamic, in the sense, as and when the data across A-F changes, I get new signals like Buy or Sell or Empty, depending upon the strategy.
    
    My expectation is, as and when I get a Buy or a Sell or an empty in Column G (in the event of a Buy and Sell that has changed to an empty cell), I want to timestamp, let us say, Column H with the exact time the change happened (regardless of Buy or Sell or empty (post a buy or sell). And this timestamp should not change the time, unless any change happens in Column G. For e.g. a buy changing to a sell or a sell changing to a buy or a buy/sell changing to an empty cell.
    
    Let me know if the above explanation helps.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11340)
    
    *   The challenge I have with the available solution on the net is, my Excel sheet refreshes every 1 minute pulling data off the net, and as and when it does, the timestamp changes to the current time as against the time the signal came.  
        For e.g. a BUY or SELL that came at say 11:15 AM, should remain static unless the signal changes from a buy to sell or a sell to buy, but everytime my excel refreshes it updates with the current time in this column. What I am looking for is to understand what time a buy or sell came.
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11341)
        
20.  I used this formula yesterday on 5th March and it worked perfect =IF(A2″”,IF(B2″”,B2,NOW()),””) my dates registered as 5th March timestamp. However I’ve now come into the same spreadsheet the very next day on 6th March but when i enter data into column A new rows, the formula in column B remains blank no result. Is there another step I’ve missed so it recognises a new day?
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11328)
    
21.  Super easy directions – thankyou 🙂
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-11317)
    
22.  This has been really helpful! thank you! I was wondering if we’re able to input in multiple cells (e.g. A2, B2, D2) and still get and updated timestamp in “F2” when ever the multiple cells (A2, B2, D2) are updated.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10918)
    
23.  It worked on one Excel Spreadsheet but when I tried it again on another Spreadsheet (totally different workbook), it just shows a blank cell. I have it formatted for date.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10867)
    
24.  In the example, “Using VBA to Automatically Insert Timestamp in Excel” I have a condition where a process is running and I want to ‘time stamp’ when it began in one column and ‘time stamp’ (date and time) when the process ended, a few columns to the right…meaning a start and stop time stamp. Can this formula accommodate this requirement?
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10853)
    
25.  Hi,
    
    Thanks Sumit, very nice contribution 🙂
    
    To add to your article for those, who like to have a static value for Date or Time Stamp and need a specific date / time format but without going through VBA, you may consider this option:
    
    1\. Choose one Reference Cell, e.g. \[A1\]. It can be on a separate worksheet.
    
    Put in the formula  
    \=today()  
    or  
    \=now()
    
    2\. Give that cell the name “Time” or “Date”
    
    3\. Now, if you want to enter current Date or Time in any cell in your workbook, just type
    
    \=Date  
    or  
    \=Time
    
    The target cell can be formatted according to your preferences, e.g. “YYYY-MM-DD” or “hh:mm:ss”. The advantage is that you can also catch the seconds which is not possible with the keyboard shortcut \[CTRL\] + \[SHIFT\] + \[:\].
    
    4\. You can also incorporate this in any formulas you are using in your worksheet.
    
    Example:
    
    Every time you enter the word “ok” in Row \[C\], Row \[B\] will automatically register the current time. To do this format Row \[B\] as “hh:mm:ss”.  
    Now, in cell \[B1\] you enter the formula
    
    if(C1=”ok”,Time,””)
    
    Then you copy this formula to the range you will be using.
    
    Now, every time you enter “ok” in a cell on Row \[C\], you will get an automatic (and static) time stamp in the adjacent cell in Row \[B\].
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10820)
    
26.  NICE great article style and super helpful
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10683)
    
27.  I’m trying to create a timestamp based on a dropdown value, however leveraging the macro is providing a validation error. Is there a workaround? If I use in a blank (no validation field) the vba/macro works correctly.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10608)
    
28.  Function Timestamp(Reference As Range)  
    If Reference.Value “” Then  
    Timestamp = Format(Now, “dd-mm-yyy hh:mm:ss”)  
    Else  
    Timestamp = “”  
    End If  
    End Function
    
    is not worjking ???
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10565)
    
    *   there is a typo in the formula,  
        replace -yyy by -yyyy (4 letters) and it will work.
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10606)
        
29.  Hi there – this is FABULOUS! Really saved me a lot of pain!
    
    Can you assist with one thing?
    
    I need to be able to create the timestamp, on a separate row, each time a (custom function) button is pressed?
    
    We will be using this to create a basic “footfall counter” to count the time/date and number of people passing into our IT support area.
    
    If you can assist, this would be amazing…
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10554)
    
30.  Thank you for your tips! I am an italian Excel Professionist and often i read your blog. Good work 😉 Marck
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10348)
    
31.  Is it possible to write a code that take effect of Cell A or Cell B for the timestamp?
    
    using below code:  
    Function Timestamp(Reference As Range)  
    If Reference.Value <> “” Then  
    Timestamp = Format(Now, “dd-mm-yyy hh:mm:ss”)  
    Else  
    Timestamp = “”  
    End If  
    End Function
    
    In cell C, should I use =timestamp(A1:B2)
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10199)
    
32.  This is just what I needed. You rock!  
    Thank you!
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10222)
    
33.  \=IF($A12<>“”,IF(AND($I12<>“”,CELL(“address”)=ADDRESS(ROW($A12),COLUMN($A12))),NOW(),IF(CELL(“address”)<>ADDRESS(ROW($A12),COLUMN($A12)),$I12,NOW())),””)
    
    i CHECKED FOR ITERATION ALSO.. EVEN ITS NOT WORKING KINDLY HELP ON THIS
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10250)
    
34.  NOT WORKING SECOND FORMULA
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10243)
    
35.  I use the following formula (=IF(A2″”,IF(B2″”,B2,NOW()),””)  
    But whenever i type in other cells, the time updated.  
    or when i save and close, then reopen the date and time updated automatically.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-10034)
    
36.  Superb Job.Thanks
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-9914)
    
37.  Can the custom function be modified to display hh:mm then am or pm?
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-9479)
    
38.  Wowww This is what I am looking for!!!
    
    THANK YOU SO MUCHHH!!!!
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-9338)
    
39.  One issue: keeping the formula options for iterations to prevent the cirucular reference error. The options are not saved with the sheet. They are saved on the computer and those saved options change with each workbook you open. For a timestamp with a circular reference you need to set the options as the workbook opens. Use this macro:
    
    Private Sub Workbook\_Open()  
    Application.Calculation = xlCalculationAutomatic  
    Application.Iteration = True  
    Application.MaxIterations = 1  
    End Sub
    
    That solves the problem and the formula works fine every time.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-8691)
    
40.  Why =IF($A$1″”,NOW()) does not work here.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-4043)
    
41.  grate! just you should say that it works mailny or totaly only on ENG versions.  
    I have Excel in italian and many of this stuff does not work like that
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3891)
    
42.  I have checked ‘enable iterative calculation’ option and I have put the formula =IF(A2””,IF(B2””,B2,NOW()),””) in cell B2 but I am getting error #Name? when I enter any text in A2.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3860)
    
    *   Hello Sajid.. Your double quotes are not in the right format (it happens sometimes when copied directly from the webpage). Just delete the double quotes and enter it manually. It would work then.
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3861)
        
        *   Yes, Now it’s working. Thank you so much Sumit.
            
            [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3862)
            
43.  I like the automated timestamp, I have users who have asked for similar things, it gives ideas on how to implement.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3847)
    
44.  Thanks Sumit……..I was searching this for more over decade.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3843)
    
    *   Glad you found this useful Anand!
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3844)
        
45.  When I tried to use the formulas to insert the timestamp, it returned 1/0/1900. It sounds like some setting that needs to changed but I couldn’t figure out where or what to change.
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3839)
    
    *   Hello Terry.. You need to check the ‘enable iterative calculation’ option for this to work
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3840)
        
        *   How to make it work for an online excel sheet shared with multiple people?
            
            [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-12092)
            
46.  Good one! thanks
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3837)
    
    *   Thanks Ashesh!
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3845)
        
47.  Excellent tip! Thank you!
    
    [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3819)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/date-timestamp-excel/#comment-3821)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/date-timestamp-excel/#respond)

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