# Excel VBA Loops: For Next, Do While, Do Until, For Each (with Examples)

**Source:** https://trumpexcel.com/vba-loops

---

[Skip to content](https://trumpexcel.com/vba-loops/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-loops/#below-title)

To get the most out of Excel and VBA, you need to know how to use loops efficiently.

In VBA, loops allow you to go through a set of objects/values and analyze it one by one. You can also perform specific tasks for each loop.

Here is a simple example of using VBA loops in Excel.

Suppose you have a dataset and you want to highlight all the cells in even rows. You can use a VBA loop to go through the range and analyze each cell row number. If it turns out to be even, you give it a color, else you leave it as is.

Now this, of course, is very simple of looping in Excel VBA (and you can also do this [using conditional formatting](https://trumpexcel.com/highlight-every-other-row-excel/)
).

In real life, you can do a lot more with VBA loops in Excel that can help you automate tasks.

Here are some more practical examples where VBA loops can be useful:

*   Looping through a [range of cells](https://trumpexcel.com/vba-ranges/)
     and analyzing each cell (highlight cells with a specific text in it).
*   Looping through all the [worksheets](https://trumpexcel.com/vba-worksheets/)
     and do something with each (such as protect/unprotect it).
*   Loop through all the open [workbooks](https://trumpexcel.com/vba-workbook/)
     (and save each workbook or close all except the active workbook).
*   Loop through all the characters in a cell (and extract the numeric part from a string).
*   Loop through all the values an array.
*   Loop through all the charts/objects (and give a border or change the background color).

Now to best use loops in Excel VBA, you need to know about the different kinds that exist and the correct syntax of each.

![Using Loops in Excel VBA - The Ultimate Guide](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20300'%3E%3C/svg%3E)

In this tutorial, I’ll showcase different types of Excel VBA loops and cover a few examples for each loop

Note: This is going to be a huge tutorial, where I will try and cover each VBA loop in some detail. I recommend you bookmark this page for future reference.

If you’re interested in learning VBA the easy way, check out my **[Online Excel VBA Training](https://trumpexcel.com/excel-vba-jetpack-course/)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-loops/#)

For Next Loop
-------------

The ‘For Next’ loop allows you to go through a block of code for the specified number of times.

For example, if I ask you to add the integers from 1 to 10 manually, you would add the first two numbers, then add the third number to the result, then add the fourth number to the result, as so on..

Isn’t it?

The same logic is used in the For Next loop in VBA.

You specify how many times you want the loop to run and also specify what you want the code to do each time the loop is run.

Below is the syntax of the For Next loop:

For Counter = Start To End \[Step Value\]
\[Code Block to Execute\]
Next \[counter\]

In the For Next loop, you can use a Counter (or any variable) that will be used to run the loop. This counter allows you to run this loop for a required number of times.

For example, if I want to add the first 10 positive integers, then my Counter value would be from 1 to 10.

Let’s have a look at a few examples to better understand how For Next loop works.

### Example 1 – Adding the first 10 positive integers

Below is the code that will add the first 10 positive integers using a For Next loop.

It will then display a message box showing the sum of these numbers.

Sub AddNumbers()
Dim Total As Integer
Dim Count As Integer
Total = 0
For Count = 1 To 10
Total = Total + Count
Next Count
MsgBox Total
End Sub

In this code, the value of Total is set to 0 before getting into the For Next loop.

Once it gets into the loop, it holds the total value after every loop. So after the first loop, when Counter is 1, ‘Total’ value becomes 1, and after the second loop it becomes 3 (1+2), and so on.

And finally, when the loop ends, ‘Total’ variable has the sum of the first 10 positive integers.

A MsgBox then simply displays the result in a message box.

### Example 2 – Adding the first 5 Even Positive Integers

To sum the first five even positive integers (i.e, 2,4,6,8, and 10), you need a similar code with a condition to only consider the even numbers and ignore the odd numbers.

Here is a code that will do it:

Sub AddEvenNumbers()
Dim Total As Integer
Dim Count As Integer
Total = 0
For Count = 2 To 10 Step 2
Total = Total + Count
Next Count
MsgBox Total
End Sub

Note that we started the Count value from 2 and also used ‘**Step 2**‘.

When you use **‘Step 2’**, it tells the code to increment the ‘Count’ value by 2 every time the loop is run.

So the Count value starts from 2 and then becomes 4, 6, 8 and 10 as the looping occurs.

NOTE: Another way of doing this could be to run the loop from 1 to 10 and within the loop check whether the number is even or odd. However, using Step, in this case, is a more efficient way as it does not require the loop to run 10 times, but only 5 times.

The Step value can also be negative. In such as case, the Counter starts at a higher value and keeps getting decremented by the specified Step value.

### Example 3 – Entering Serial Number in the Selected Cells

You can also use the For Next loop to go through a collection of objects (such as cells or worksheets or workbooks),

Here is an example that quickly [enters serial numbers](https://trumpexcel.com/number-rows-in-excel/)
 in all the selected cells.

Sub EnterSerialNumber()
Dim Rng As Range
Dim Counter As Integer
Dim RowCount As Integer
Set Rng = Selection
RowCount = Rng.Rows.Count
For Counter = 1 To RowCount
ActiveCell.Offset(Counter - 1, 0).Value = Counter
Next Counter
End Sub

The above code first counts the number of selected rows and then assigns this value to the variable RowCount. We then run the loop from ‘1 to RowCount’.

Also note that since selection can be any number of rows, we have Set the variable Rng to Selection (with the line ‘Set Rng = Selection’). Now we can use the ‘Rng’ variable to refer to the selection in our code.

### Example 4 – Protect All Worksheets in the Active Workbook

You can use the ‘For Next’ loop to go through all the worksheets in the active workbook, and protect (or unprotect) each of the worksheets.

Below is the code that will do this:

Sub ProtectWorksheets()
Dim i As Integer
For i = 1 To ActiveWorkbook.Worksheets.Count
Worksheets(i).Protect
Next i
End Sub

The above code [counts the number of sheets](https://trumpexcel.com/count-sheets-excel/)
 by using ActiveWorkbook.Worksheets.Count. This tells VBA how many times the loop needs to be run.

In each instance, it refers to the Ith workbook (using Worksheets(i)) and protects it.

You can use this same code to Unprotect worksheets too. Just change the line _Worksheets(i).Protect_ to _Worksheets(i).UnProtect_.

### Nested ‘For Next’ Loops

You can use nested ‘For Next’ loops to get more complex automation done in Excel. A nested ‘For Next’ loop would mean that there is a ‘For Next’ loop within a ‘For Next’ loop.

Let me show you how to use this using an example.

Suppose I have 5 workbooks open in my system and I want to protect all the worksheets in all these workbooks.

Below is the code that will do this:

Sub ProtectWorksheets()
Dim i As Integer
Dim j As Integer
For i = 1 To Workbooks.Count
For j = 1 To Workbooks(i).Worksheets.Count
Workbooks(i).Worksheets(j).Protect
Next j
Next i
End Sub

The above is a nested [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 as we have used one For Next loop within another.

### ‘EXIT For’ Statements in For Next Loops

‘Exit For’ statement allows you to exit the ‘For Next’ loop completely.

You can use it in cases where you want the For Next loop to end when a certain condition is met.

Let’s take an example where you have a set of numbers in Column A and you want to highlight all the negative numbers in red font. In this case, we need to analyze each cell for its value and then change the font color accordingly.

But to make the code more efficient, we can first check if there are any negative values in the list or not. If there are no negative values, we can use the Exit For the statement to simply come out of the code.

Below is the code that does this:

Sub HghlightNegative()
Dim Rng As Range
Set Rng = Range("A1", Range("A1").End(xlDown))
Counter = Rng.Count
For i = 1 To Counter
If WorksheetFunction.Min(Rng) >= 0 Then Exit For
If Rng(i).Value < 0 Then Rng(i).Font.Color = vbRed
Next i
End Sub

When you use the ‘Exit For’ statement within a nested ‘For Next’ loop, it will come out of the loop in which it is executed and go on to execute the next line in the code after the For Next loop.

For example, in the below code, the ‘Exit For’ statement will get you out of the inner loop, but the outer loop would continue to work.

Sub SampleCode()
For i = 1 To 10
For j = 1 to 10
Exit For
Next J
Next i
End Sub

Do While Loop
-------------

A ‘Do While’ loop allows you to check for a condition and run the loop while that condition is met (or is TRUE).

There are two types of syntax in the Do While Loop.

Do \[While condition\]
\[Code block to Execute\]
Loop

and

Do
\[Code block to Execute\]
Loop \[While condition\]

The difference between these two is that in the first, the While condition is checked first before any code block is executed, and in the second case, the code block is executed first and then the While condition is checked.

This means that if the While condition is False is both the cases, the code will still run at least once in the second case (as the ‘While’ condition is checked after the code has been executed once).

Now let’s see some examples of using Do While loops in VBA.

### Example 1 – Add First 10 Positive Integers using VBA

Suppose you want to add the first ten positive integers using the Do While loop in VBA.

To do this, you can use the Do While loop until the next number is less than or equal to 10. As soon as the number is greater than 1o, your loop would stop.

Here is the VBA code that will run this Do While loop and the show the result in a message box.

Sub AddFirst10PositiveIntegers()
Dim i As Integer
i = 1
Do While i <= 10
Result = Result + i
i = i + 1
Loop
MsgBox Result
End Sub

The above loop continues to work until the value of ‘i’ becomes 11. As soon as it becomes 11, the loop ends (as the While condition becomes False).

Within the loop, we have used a Result variable that holds the final value Once the loop is completed, a message box shows the value of the ‘Result’ variable.

### Example 2 –  Enter Dates For the Current Month

Let’s say you want to enter all the dates of the current month into a worksheet column.

You can do that by using the following Do While loop code:

Sub EnterCurrentMonthDates()
Dim CMDate As Date
Dim i As Integer
i = 0
CMDate = DateSerial(Year(Date), Month(Date), 1)
Do While Month(CMDate) = Month(Date)
Range("A1").Offset(i, 0) = CMDate
i = i + 1
CMDate = CMDate + 1
Loop
End Sub

The above code would enter all the dates in the first column of the worksheet (starting from A1). The loops continue till the Month value of the variable ‘CMDate’ matches that of the current month.

### Exit Do Statement

You can use the Exit Do statement to come out of the loop. As soon as the code executes the ‘Exit Do’ line, it comes out of the Do While loop and passes the control to the next line right after the loop.

For example, if you want to enter the first 10 dates only, then you can exit the loop as soon as the first 10 dates are entered.

The below code will do this:

Sub EnterCurrentMonthDates()
Dim CMDate As Date
Dim i As Integer
i = 0
CMDate = DateSerial(Year(Date), Month(Date), 1)
Do While Month(CMDate) = Month(Date)
Range("A1").Offset(i, 0) = CMDate
i = i + 1
If i >= 10 Then Exit Do
CMDate = CMDate + 1
Loop
End Sub

In the above code, the [IF statement](https://trumpexcel.com/if-then-else-vba/)
 is used to check if the value of i is greater than 10 or not. As soon as the value of ‘i’ becomes 10, Exit Do statement is executed and the loop ends.

Do Until Loop
-------------

‘Do Until’ loops are very much like the ‘Do While’ loops.

In ‘Do While’, the loop runs till the given condition is met, while in ‘Do Until’, it loops until the specified condition is met.

There are two types of syntax in the Do Until Loop.

Do \[Until condition\]
\[Code block to Execute\]
Loop

and

Do
\[Code block to Execute\]
Loop \[Until condition\]

The difference between these two is that in the first, the Until condition is checked first before any code block is executed, and in the second case, the code block is executed first and then the Until condition is checked.

This means that if the Until condition is TRUE is both cases, the code will still run at least once in the second case (as the ‘Until’ condition is checked after the code has been executed once).

Now let’s see some examples of using Do Until loops in VBA.

Note: All the examples for Do Until are the same as that of Do While. These have been modified to show you how the Do Until loop works.

### Example 1 – Add First 10 Positive Integers using VBA

Suppose you want to add the first ten positive integers using the Do Until loop in VBA.

To do this, you need to run the loop until the next number is less than or equal to 10. As soon as the number is greater than 1o, your loop would stop.

Here is the VBA code that will run this loop and show the result in a message box.

Sub AddFirst10PositiveIntegers()
Dim i As Integer
i = 1
Do Until i > 10
Result = Result + i
i = i + 1
Loop
MsgBox Result
End Sub

The above loop continues to work until the value of ‘i’ becomes 11. As soon as it becomes 11, the loop ends (as the ‘Until’ condition becomes True).

### Example 2 –  Enter Dates For the Current Month

Let’s say you want to enter all the dates of the current month into a worksheet column.

You can do that by using the following Do Until loop code:

Sub EnterCurrentMonthDates()
Dim CMDate As Date
Dim i As Integer
i = 0
CMDate = DateSerial(Year(Date), Month(Date), 1)
Do Until Month(CMDate) <> Month(Date)
Range("A1").Offset(i, 0) = CMDate
i = i + 1
CMDate = CMDate + 1
Loop
End Sub

The above code would enter all the dates in the first column of the worksheet (starting from A1). The loop continues until the Month of variable CMDate is not equal to that of the current month.

### Exit Do Statement

You can use the ‘Exit Do’ statement to come out of the loop.

As soon as the code executes the ‘Exit Do’ line, it comes out of the Do Until loop and passes the control to the next line right after the loop.

For example, if you want to enter the first 10 dates only, then you can exit the loop as soon as the first 10 dates are entered.

The below code will do this:

Sub EnterCurrentMonthDates()
Dim CMDate As Date
Dim i As Integer
i = 0
CMDate = DateSerial(Year(Date), Month(Date), 1)
Do Until Month(CMDate) <> Month(Date)
Range("A1").Offset(i, 0) = CMDate
i = i + 1
If i >= 10 Then Exit Do
CMDate = CMDate + 1
Loop
End Sub

In the above code, as soon as the value of ‘i’ becomes 10, Exit Do statment is executed and the loop ends.

For Each
--------

In VBA, you can loop through a set of collections using the ‘For Each’ loop.

Here are some examples of collections in Excel VBA:

*   A collection of all the open Workbooks.
*   A collection of all worksheets in a workbook.
*   A collection of all the cells in a range of selected cells.
*   A collection of all the charts or shapes in the workbook.

Using the ‘For Each’ loop, you can go through each of the objects in a collection and perform some action on it.

For example, you can go through all the worksheets in a workbook and protect these, or you can go through all the cells in the selection and change the formatting.

With the ‘For Each’ loop (also referred to as the ‘For Each-Next’ loop), you don’t need to know how many objects are there in a collection.

‘For Each’ loop would automatically go through each object and perform the specified action. For example, if you want to protect all the worksheets in a workbook, the code would be the same whether you have a workbook with 3 worksheets or 30 worksheets.

Here is the syntax of For Each-Next loop in Excel VBA.

For Each element In collection
\[Code Block to Execute\]
Next \[element\]

Now let’s see a couple of examples of using the For Each Loop in Excel.

### Example 1 – Go through All the Worksheets in a Workbook (and Protect it)

Suppose you have a workbook where you want to protect all the worksheets.

Below For Each-Next loop can do this easily:

Sub ProtectSheets()
Dim ws As Worksheet
For Each ws In ActiveWorkbook.Worksheets
ws.Protect
Next ws
End Sub

In the above code, we have defined ‘ws’ variable as a Worksheet object. This tells VBA that ‘ws’ should be interpreted as a worksheet object in the code.

Now we use the ‘For Each’ statement to go through each ‘ws’ (which is a worksheet object) in the collection of all the worksheets in the active workbook (given by ActiveWorkbook.Worksheets).

Note that unlike other loops where we have tried to protect all the worksheets in a workbook, here we don’t need to worry about how many worksheets are there in the workbook.

We don’t need to count these to run the loop. For Each loop ensures that all the objects are analyzed one by one.

### Example 2 – Go through All the Open Workbooks (and Save All)

If you work with multiple workbooks at the same time, it can come in handy to be able to save all these workbooks at once.

Below VBA code can do this for us:

Sub SaveAllWorkbooks()
Dim wb As Workbook
For Each wb In Workbooks
wb.Save
Next wb
End Sub

Note that in this code, you don’t get a prompt that asks you to save the workbook in a specific location (if saving it for the first time).

It saves it in the default folder (it was the ‘Documents’ folder in my case). This code works best when these files are already saved and you’re making changes and you want to save all the workbooks quickly.

### Example 3 – Go through All the Cells in a Selection (Highlight negative values)

Using the ‘For Each’ loop, you can loop through all the cells in a specific range or in the selected range.

This can be helpful when you want to analyze each cell and perform an action based on it.

For example, below is the code that will go through all the cells in the selection and change the cell color of the cells with negative values to red.

Sub HighlightNegativeCells()
Dim Cll As Range
For Each Cll In Selection
If Cll.Value < 0 Then
Cll.Interior.Color = vbRed
End If
Next Cll
End Sub

(Note I’ve used Cll as a short variable name for Cell. It’s advisable not to use object names such as Sheets or Range as variable names)

In the above code, the For Each-Next loop goes through the collection of cells in the selection. IF statement is used to identify if the cell value is negative or not. In case it is, the cell is given a red interior color, else it goes to the next cell.

In case you don’t have a selection, and instead want VBA to select all the filled cells in a column, starting from a specific cell (just like we use Control + Shift + Down arrow key to select all filled cells), you can use the below code:

Sub HighlightNegativeCells()
Dim Cll As Range
Dim Rng As Range
Set Rng = Range("A1", Range("A1").End(xlDown))
For Each Cll In Rng
If Cll.Value < 0 Then
Cll.Interior.Color = vbRed
End If
Next Cll
End Sub

In the above example, it doesn’t matter how many filled cells are there. It will start from cell A1 and analyze all the contiguous filled cells in the column.

You also don’t need to have cell A1 selected. You can have any far-off cell selected and when the code runs, it will still consider all the cells in column A (starting from A1) and color the negative cells.

### ‘Exit For’ Statment

You can use the ‘Exit For’ statement in the For Each-Next loop to come out of the loop. This is usually done in case a specific condition is met.

For example, in Example 3, as we are going through a set of cells, it can be more efficient to check if there are any negative values or not. In case there are no negative values, we can simply exit the loop and save some VBA processing time.

Below is the VBA code that will do this:

Sub HighlightNegativeCells()
Dim Cll As Range
For Each Cll In Selection
If WorksheetFunction.Min(Selection) >= 0 Then Exit For
If Cll.Value < 0 Then
Cll.Interior.Color = vbRed
End If
Next Cll
End Sub

Where to Put the VBA Code
-------------------------

Wondering where the VBA code goes in your Excel workbook?

Excel has a VBA backend called the VBA editor. You need to copy and paste the code in the VB Editor module code window.

Here are the steps to do this:

1.  Go to the Developer tab.![IF Then Else in Excel VBA - Developer Tab in ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
2.  Click on the Visual Basic option. This will open the VB editor in the backend.![Click on Visual Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
3.  In the Project Explorer pane in the VB Editor, right-click on any object for the workbook in which you want to insert the code. If you don’t see the Project Explorer go to the View tab and click on Project Explorer.
4.  Go to Insert and click on Module. This will insert a module object for your workbook.![VBA Loops - inserting module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20494%20363'%3E%3C/svg%3E)
5.  Copy and paste the code in the module window.![VBA Loops - inserting module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20494%20363'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [How to record a macro in Excel](https://trumpexcel.com/record-macro-vba/)
    .
*   [Creating User-defined functions in Excel](https://trumpexcel.com/user-defined-function-vba/)
    .
*   [Excel VBA Msgbox](https://trumpexcel.com/vba-msgbox/)
    
*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    .
*   [How to Create and Use Add-ins in Excel](https://trumpexcel.com/excel-add-in/)
    .
*   [Excel VBA Events – An Easy (and Complete) Guide](https://trumpexcel.com/vba-events/)
    .
*   [How to Sort Data in Excel using VBA (A Step-by-Step Guide)](https://trumpexcel.com/sort-data-vba/)
    .
*   [24 Useful Excel Macro Examples for VBA Beginners (Ready-to-use).](https://trumpexcel.com/excel-macro-examples/)
    
*   [How to Use Excel VBA InStr Function (with practical EXAMPLES)](https://trumpexcel.com/excel-vba-instr/)
    .
*   [Excel Personal Macro Workbook | Save & Use Macros in All Workbooks.](https://trumpexcel.com/personal-macro-workbook/)
    
*   [Using Select Case in Excel VBA](https://trumpexcel.com/vba-select-case/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

12 thoughts on “Excel VBA Loops: For Next, Do While, Do Until, For Each (with Examples)”
----------------------------------------------------------------------------------------

1.  How to use such formula for the required cell in row using VBA =IF(AND(P$1&P280),1,IF(AND(Q$1&Q270),1,””))
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-13757)
    
2.  I have list of unique names of players in column A in sheet 1. And in sheet 2 I have data of cricket score of different matches for that particular player with same unique names. And in sheet 3 I have data of same players for football matches. Now I want to first find the name which is in the sheet 1 from sheet 2 and cut that data from sheet 2 and paste in same row of that particulate player. And find and cut the data from sheet 3 and paste it in sheet 1 on same row in next available cell. Do this task one by one for all players till cell is empty. In some cases I have multiple rows in sheet 2 and sheet 3 for the same name. In that case add a new row under that name and cut paste all the data. And every time I will update the sheet 2 and sheet 3 with the new data with new names which I will add in in sheet 1 too it will update all the data in sheet 1 by clicking a single button.
    
    I have tried lots of thin but still it is not working as I needed. Anybody can help me for this task…..
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-13413)
    
3.  Awesome Sir
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-12612)
    
4.  It would be great if you can write the examples with proper alignment in the code.
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-12539)
    
5.  The example Nº 1of “For Each” doesn’t work, it doesn”t change for next sheet, it protects sheet 1 over and over
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-12434)
    
    *   I’m sorry, I made something wrong. The example works great.
        
        [Reply](https://trumpexcel.com/vba-loops/#comment-12435)
        
6.  Excellent site, excellent explanations far more better than the “help” files from MS!
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-12275)
    
7.  Excellent training
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-11865)
    
8.  sir  
    i have question  
    how to Show the same months in combobox whose dates is written in the column A of the worksheet ?  
    i hope for positive and speedy result from you  
    thanx in advance
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-11628)
    
9.  sir  
    i have a question
    
    how to Show the same months of combobox whose dates is written in the column number one of the worksheet ?
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-11627)
    
10.  Your material is GREAT and very often saves me an enormous amount of time.  
    I have a VBA issue that I’m hoping you might solve: I have a range of cells in which there are dates in the form mm/dd/yyyy. Sometimes there’s 1 date, sometimes there are 2 dates. When there are 2 dates, they are separated by CHAR(10).  
    There is other unwanted content in many of the cells in the range. I’d like a VBA routine that will delete the unwanted information and retain the dates AND the CHAR(10)s. Possible?
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-11620)
    
11.  wonder tip and trick vba for new learner
    
    [Reply](https://trumpexcel.com/vba-loops/#comment-10396)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-loops/#respond)

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