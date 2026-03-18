# How to Select Every Third Row in Excel (or select every Nth Row)

**Source:** https://trumpexcel.com/select-every-third-row

---

[Skip to content](https://trumpexcel.com/select-every-third-row/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/select-every-third-row/#below-title)

A few days ago, one of my [VBA course](https://trumpexcel.com/excel-vba-jetpack-course/)
 students asked me if there was a way to select every third row in a dataset in Excel.

While there is no way to do this using inbuilt functionalities in Excel, it can easily be done using VBA.

Something as shown below:

![Select Every Third Row in Excel - Demo](https://trumpexcel.com/wp-content/uploads/2017/10/Select-Every-Third-Row-in-Excel-Demo.gif)

In this tutorial, I will give you the VBA code and show you the exact steps to get this done in Excel.

**[Click here to download the example file and follow along](https://www.dropbox.com/s/qn0mjspbo5fn5q5/Select-Every-Third-Row-in-Excel.xlsm?dl=1)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/select-every-third-row/#)

Let me first give you the VBA code that will select every third row in the dataset that you have selected.

Note that I have taken every third row as an example and you can modify the code to select every second, fourth, fifth, or Nth row (or even columns) in the dataset.

VBA Code to Select Every Third Row in a Dataset in Excel
--------------------------------------------------------

Below is the code that will select every third row in the dataset that you have selected.

Sub SelectEveryThirdRow()
'Created by Sumit Bansal at https://trumpexcel.com/
Dim MyRange As Range
Dim RowSelect As Range
Dim i As Integer
Set MyRange = Selection
Set RowSelect = MyRange.Rows(3)
For i = 3 To MyRange.Rows.Count Step 3
Set RowSelect = Union(RowSelect, MyRange.Rows(i))
Next i
Application.Goto RowSelect
End Sub

Note that this code will work only when you select a dataset. As soon as you run this code, it will select every third row in the selected dataset.

What does the Code do?
----------------------

The code uses two object variables – MyRange and RowSelect.

*   The selected range is assigned to the ‘MyRange’ variable. This means that as soon as you select a range of cells and run this code, the first thing it does is assigns that selected range of cells to this variable ‘MyRange’. The following line of code does this:

Set MyRange = Selection

*   The second step is to assign the third row in the dataset to another object variable ‘RowSelect’. The following line in the code does this:

Set RowSelect = MyRange.Rows(3)

*   When the above two steps are done, the code runs a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
    . It starts from the third row and runs till the variable ‘i’ reaches the number equal to the total number of rows in the dataset. The total number of rows is given by MyRange.Rows.Count. Also, note that I have used Step 3 here which means that the value of the variable ‘i’ in the loop will change in steps of 3 (for example 3, then 6, then 9, and so on). The following line of code does all this:

For i = 3 To MyRange.Rows.Count Step 3

*   Within the loop, we just combine every third row in the data set using the [UNION method](https://msdn.microsoft.com/en-us/vba/excel-vba/articles/application-union-method-excel)
     in VBA. All these rows (i.e., every third row in the data set) is assigned to the object variable ‘RowSelect’. The following line of code does this:

Set RowSelect = Union(RowSelect, MyRange.Rows(i))

*   Finally, when the loop is over, we ask the Excel application to go and select all the rows stored in the object ‘RowSelect’. The following line of code does this:

Application.Goto RowSelect

Now let’s see where you need to copy and paste this code into Excel.

**Download the Example File**  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/qn0mjspbo5fn5q5/Select-Every-Third-Row-in-Excel.xlsm?dl=1)

Where to Copy and Paste this VBA Code
-------------------------------------

Here are the steps you need to follow to copy this code in the VB Editor from where it can be run:

*   Copy the code mentioned above.
*   Go to the Developer tab ([click here](https://trumpexcel.com/excel-developer-tab/)
     if you don’t see the developer tab in the ribbon).![Select Every Third Row in Excel - Developer Tab in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20130'%3E%3C/svg%3E)
*   Click on Visual Basic (or use the keyboard shortcut – ALT + F11).![Selecting Visual Basic in the Developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20130'%3E%3C/svg%3E)
*   In the VB Editor, right-click on any of the workbook objects (if you can’t see the Project Explorer, use the keyboard shortcut – Control + R).
*   Go to the ‘Insert’ option and click on ‘Module’.![inserting a module in the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20377'%3E%3C/svg%3E)
*   Double-click on the Module object that is inserted.
*   Paste the code in the Module code window.![Copy the code to select every third row in Excel in the module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20731%20235'%3E%3C/svg%3E)
*   Close the VB Editor.

Once you have copied the code in the VB Editor, you can now use it in the workbook.

[Click here to learn different ways to run a macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
.

Note that since the workbook would have a macro code in it, you need to save it in the .xlsm or .xls extension.

Variations in the Code (Examples)
---------------------------------

The above code would select every third row in the selected dataset.

This could be useful if you want to [delete every third row](https://trumpexcel.com/vba-delete-row-excel/)
 or copy these and paste it into a new worksheet.

But what if you want to select every second row, or every fourth row, or every second column (or any Nth row/column for that matter).

In those cases, you can easily modify the VBA code.

Here are some example codes.

### Example 1 – Select Every Fourth Row in a Dataset

Below is the code that will select every fourth row in the selected dataset:

Sub SelectEveryFourthRow()
'Created by Sumit Bansal at https://trumpexcel.com/
Dim MyRange As Range
Dim RowSelect As Range
Dim i As Integer
Set MyRange = Selection
Set RowSelect = MyRange.Rows(4)
For i = 4 To MyRange.Rows.Count Step 4
Set RowSelect = Union(RowSelect, MyRange.Rows(i))
Next i
Application.Goto RowSelect
End Sub

Note that the only change I have made here is the number in the code (from 3 to 4).

### Example 2 – Select Every Second Column in a Dataset

Below is the code that will select every second column in the selected dataset:

Sub SelectEverySecondColumn()
'Created by Sumit Bansal at https://trumpexcel.com/
Dim MyRange As Range
Dim ColumnSelect As Range
Dim i As Integer
Set MyRange = Selection
Set ColumnSelect = MyRange.Columns(2)
For i = 2 To MyRange.Columns.Count Step 2
Set ColumnSelect = Union(ColumnSelect, MyRange.Columns(i))
Next i
Application.Goto ColumnSelect
End Sub

### Example 3 – Selecting Every Third Row in an Excel Table

If you work with data regularly, you may be using Excel tables (you must if you aren’t already).

When [using an Excel Table](https://trumpexcel.com/excel-table/)
, you can modify the code so that you don’t have to select the data set. The code will automatically go to the Excel Table and select every third row in it ( or whatever number of row/column you have specified in the code).

So if I created an Excel Table (named Table1), I can use the below code to select every third row in it.

Sub SelectEveryThirdRow()
'Created by Sumit Bansal at https://trumpexcel.com/
Dim MyRange As Range
Dim RowSelect As Range
Dim i As Integer
Set MyRange = Range("Table1")
Set RowSelect = MyRange.Rows(3)
For i = 3 To MyRange.Rows.Count Step 3
Set RowSelect = Union(RowSelect, MyRange.Rows(i))
Next i
Application.Goto RowSelect
End Sub

The only change I have made here is that instead of using

Set MyRange = Selection

I have used

Set MyRange = Range("Table1")

How to Add this Macro to the Quick Access Toolbar
-------------------------------------------------

If selecting every third row is a task that you need to do often, it’s a good idea to save this macro in your personal macro workbook. Here is a detailed guide on how to save a macro in the [personal macro workbook](https://trumpexcel.com/personal-macro-workbook/)
.

Once you have saved the macro in the personal macro workbook, you can add it to the Quick Access Toolbar (QAT). This way, you will have access to this macro in all the workbooks and you will be able to run it right from the QAT.

Here are the steps to save a macro to the QAT:

*   Click on the Customize Quick Access Toolbar icon.![Customize the Quick Access Toolbar Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20100'%3E%3C/svg%3E)
*   Select ‘More Commands’.![More Commands to add macro to QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20403'%3E%3C/svg%3E)
*   In the Excel Options dialogue box, in the ‘Choose command from’ dialog box, select ‘Macros’.![Macros in Excel Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20234'%3E%3C/svg%3E)
*   Click on the Macro that you want to add to the QAT.![Select Every Third Row in Excel Icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20350'%3E%3C/svg%3E)
*   Click on Add.![Select Every Third Row in Excel - Click on Add Macro Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20350'%3E%3C/svg%3E)
*   Click OK.

This will add this macro in the QAT, as shown below.

![Macro when added to the QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20369%20110'%3E%3C/svg%3E)

Now you can simply select the data set (in which you want to select every third/Nth row), and click on the macro icon in the QAT.

**Download the Example File**  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/qn0mjspbo5fn5q5/Select-Every-Third-Row-in-Excel.xlsm?dl=1)

**You May Also Like the Following Excel Tutorials:**

*   [3 Quick Ways to Select Visible Cells in Excel](https://trumpexcel.com/select-visible-cells/)
    
*   [24 Useful Excel Macros for VBA Beginners](https://trumpexcel.com/excel-macro-examples/)
    .
*   [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)
    .
*   [How to Quickly Select Blank Cells in Excel](https://trumpexcel.com/select-blank-cells-in-excel/)
    .
*   [Number Rows in Excel](https://trumpexcel.com/number-rows-in-excel/)
    .
*   [How to Select 500 cells/rows in Excel (with a single click)](https://trumpexcel.com/select-500-cells-rows/)
    .
*   [Select Till End of Data in a Column in Excel (Shortcuts)](https://trumpexcel.com/select-end-of-data-in-column-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

19 thoughts on “How to Select Every Third Row in Excel (or select every Nth Row)”
---------------------------------------------------------------------------------

1.  Hi, thanks for the tip, I was desperate to find this.  
    Unfortunately when I try it I have a syntax error message for the line
    
    For i = 3 To MyRange.Rows.Count Step 3
    
    This is on office 365. what did I do wrong ?
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-14629)
    
2.  Use the MOD() function. It returns the remainder of a number and it’s divisor.
    
    MOD(ROW(), n) where n is the n’th row you wish to identify or filter.
    
    For example, MOD(ROW(), 3) will have a value of 1, 2, and 0 every third row. You can filter columns and select or un-select as needed.
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-12758)
    
3.  Hy guys, i have a problem i have more than 10 k rows and i wrote the same formula as abova and when i want to select the rows with the macro excel freezes. I also encountered a problem when i select 900 row and want to apply this macro to select every 2nd row it\`s selecting just 500 and a bit. I would be happy to get a solution for this. Thanks in advance. Kind Regards, Arnold S.
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-11985)
    
4.  Why wouldn’t the ‘OFFSET’ command work to select every third row?
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-11388)
    
5.  GM All,  
    i have a problem in which 2 spreadsheet , one spread sheet contain incoming of whole month, with vender code ,sap item code and incoming qty,  
    and in another sheet contain vender code and sap item code , we need to take the data for incoming qty in the second one with out using filter option.
    
    please support. and give the best guidance.
    
    thanks  
    Hemant Sharma  
    9911195566
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9891)
    
6.  I tried the code for selecting every 3rd row and it worked but only up to the 321st row but my dataset had 3339 rows and went up to column AA. Any reason why it would stop at 321? I’m using Office 2013.
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9830)
    
7.  Hi Sumit,
    
    I am non VBA guy whereas i use standard Excel logics to do such activities….
    
    the way which i know to extract the nth row without VBA is
    
    \={IF(ROWS($K$1:K1)>COUNTIF($I$1:$I$14,0),””,INDEX(A$1:A$14,SMALL(IF(MOD((ROW($B$1:$B$14)-ROWS($B$1)+1),3)=0,(ROW($B$1:$B$14)-ROWS($B$1)+1)),ROWS($K$1:K1))))}
    
    The above formula has to be used with CSE.
    
    Hope this will also meet the requirement…….
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9814)
    
    *   Thanks for sharing the formula Shyam.
        
        While a lot can be done with formulas, it can not select cells/rows. The intent here is not to extract every third row, but to select it. For example, suppose I have dataset and I want to delete every third row (or change the value in every third cell in a column), then I can use VBA to get this done faster.
        
        [Reply](https://trumpexcel.com/select-every-third-row/#comment-9815)
        
8.  Thank you! Interesting to learn how to solve Excel-problems in VBA.
    
    However this case I suppose it would be faster to use the functions within Excel? Input for example the numbers 1, 2, 3 in a new column – drag the column all the way down to the end (by marking the fist tre rows of that column). In a new sheet use the if-formula to import rows where the new column equals to 3. Mark everything, import as text, delete doubles (and delete the remaining blank row (assuming there are now doubles to keep))…
    
    Just an example of how I would solve the problem without using VBA (since I’m terribly bad at it at the moment)…
    
    Keep up the good work!
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9802)
    
    *   Hey Torvald, Thanks for sharing. With VBA, you don’t need any new column/sheet to be added. You can simply select the data set and run the code to select every third row/column. The formula approach is useful when you have to get this done once or twice only. In case this is something needed regularly, creating the macro, saving it in personal macro workbook and the adding it to QAT is a one-time activity. Then it can be done with a single click.
        
        [Reply](https://trumpexcel.com/select-every-third-row/#comment-9806)
        
        *   Thank’s for your answer Sumit, most claryfying.
            
            OC I don’t need the extra column – typical of me to make the solution more complicated than neccessary…
            
            Yes I clearly see the advantage of VBA-solutions. Especially it the Excel-calculations are going to be made by someone else than me. I do from time to time create sheets to be used by others, and in those cases I also have to put in time for explanation/creating a manual…
            
            Thanks a lot for a great site! 😀
            
            [Reply](https://trumpexcel.com/select-every-third-row/#comment-9809)
            
9.  To select every 3rd row, can we do like this ?  
    Suppose your data range is A1:C27. Select A3 & fill cell with colour. Now select A1:A3, select format painter & paste it on A4;A27. You get all 3rd row highlighted.
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9800)
    
    *   Hey Ketan.. This will get every third row highlighted, not selected. When selected, you can do a lot more such as copy the value, delete the rows, change the values, format etc.
        
        [Reply](https://trumpexcel.com/select-every-third-row/#comment-9805)
        
        *   Agree, it will only highlight & not select. For selection, i have to filter by color. This was basically for persons like me who dont know XYZ of VBA. I also like reply from Torvald which is basically similar to mine.  
            However, Excel has endless possibilities. It is always learning to go through your post/emails.
            
            [Reply](https://trumpexcel.com/select-every-third-row/#comment-9807)
            
10.  Hello sumit,, im really happy with your tutorial,,
    
    And i need your help about my project, i need print all with vlookup,, like a mailmerge in word,, maybe you cant show me,, how print all data using vlook up,, sorry for my bad english.. and before that,, thank you so much,, sumit,, you tutorial is great
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9799)
    
11.  Hello, in Example 2 – Select Every Second Column in a Dataset rows should be changed to columns.
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9798)
    
    *   Thanks for letting me know Albert.. Have corrected it 🙂
        
        [Reply](https://trumpexcel.com/select-every-third-row/#comment-9804)
        
12.  Hi,  
    i think as nth row is the variable, i would add  
    dim nthRow as integer  
    and change  
    For i = nthRow To MyRange.Rows.Count Step nthRow  
    and change only once the number of row
    
    [Reply](https://trumpexcel.com/select-every-third-row/#comment-9792)
    
    *   Hey, by Nth I meant any number (could be every 3rd row, or every 4th row, or every 5th row). The code would be:
        
        Sub SelectEveryThirdRow()  
        Dim MyRange As Range  
        Dim RowSelect As Range  
        Dim i As Integer  
        Set MyRange = Selection  
        Set RowSelect = MyRange.Rows(N)  
        For i = N To MyRange.Rows.Count Step N  
        Set RowSelect = Union(RowSelect, MyRange.Rows(i))  
        Next i  
        Application.Goto RowSelect  
        End Sub
        
        In the above code, you can change N with the number you want.
        
        [Reply](https://trumpexcel.com/select-every-third-row/#comment-9794)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/select-every-third-row/#respond)

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