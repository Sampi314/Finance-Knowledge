# Heavy Financial Models

**Source:** https://edbodmer.com/heavy-financial-models

---

On this page I try to review what makes a model heavy — when excel is slow to compute; when excel files are large in terms of size; and when excel workbooks are very slow in terms of adding new lines and re-structuring pages. I find the third issue — adding lines and re-structuring pages — the most irritating problem when inserting or deleting new lines which can take what seems to be forever. The first point about the size of a model should be a much smaller issue as it is so easy to save your files on the cloud. The most general point to make is that if you have a whole bunch of inputs and a lot of columns and a lot of equations there is nothing magic that you can to to make your model smaller and there is probably little you can do to make your model faster.

On this page I document some of the research I have made to see just how what are the effects of things like using the entire line in formulas like LOOKUP, the effects of OFFSET; the effects of conditional formatting and so forth. When I go to google and try to lookup what causes files to be heavy — slow or large — you just get some old wives tales without any proof or objective tests (sorry for using this phrase which may not be quite politically correct). I try to present objective tests of exactly how much these things affect the speed and size of your file. I have attempted to create unbiased tests so that you can document different strategies for making your file more manageable with time tests and size tests rather than believing vague myths from a google search. Please understand that if you have a whole lot of data and associated equations, the model will be big in terms of size and the calculations may be slow. If somebody demands that you make a month by month model for 70 years for five plants with ten debt issues, the model will be large.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-13.png)

I find that there is little cost to using the OFFSET function which has such a bad name because of the supposed volatile nature of the function. Here is the issue with a volatile function that you can create yourself by putting in the line:

application.Volatile

For volatile functions, every calculation in the sheet is computed for the function to work. For other functions like the SUM function, only the values that change are recomputed when you press the F9 key. Let’s say you have a really big model and you do not change anything at all and you press F9 to re-calculate. This should be very fast if you have no volatile functions. On the other hand, if you have a volatile function, excel will re-compute all of the formulas even when nothing changes.

My problem with this discussion is that when you have a SUM function or a SUMIF function and you change some input or some scenario, do you really think there is a big difference between the functions that are re-calculated and those that are not. For example, if you change the price, then revenues change, EBITDA changes, financing changes, all of the output pages change, the IRR changes and so forth. There may be a few items such as fixed operating cost that do not change but I have difficulty believing that this makes a really big impact on a model. I have tried to create some examples below where I illustrate specific issues related to volatile functions and show that there is in fact no cost in terms of the key speed issues from using OFFSET with SUM versus SUMIF to accomplish the same task. I also demonstrate that critiques of using an entire row or column in a formula seem to be incorrect and that using an entire row in the LOOKUP or SUMIF function does not have a cost. You can argue that my tests are incorrect and I would be very interested in comments on the experiments. If you want to dispute these ideas, I am interested in your proofs or how you think that my proofs are biased.

.

Objective Tests of What Makes a Model Slow and 10 Tips that are B.S. Old Wives Tales
------------------------------------------------------------------------------------

I googled what makes a spreadsheet slow and something named Trump excel came up with a list that I have replicated in the screenshot below. This list made me very scared. The Trump thing made two big points that I would take away. The first point implies that you should not use OFFSET or INDIRECT which are sometimes invaluable. I would be very depressed if this makes the models really slow although I agree that INDIRECT can slow down a model. Helper columns (point 2) seem to have something to do with VLOOKUP which should never ever be used anyway. I do use conditional formatting (point 4) and I agree that it can mess things up (you can use a macro to clean this up). I hate using too many range names (point 5) and I think they can really screw up a model so I strongly dispute this point. I don’t see how you can convert formulas into values and of course you should not include formulas that you do not need (point 6). If you keep all of the input data in one sheet (point 7), you may have big difficulties in inserting rows but you can use Sean’s FORCEFULLCALCULATION that is very creative. Point 8 — Avoid using entire rows or columns in references is the point that makes me very worried and I believe this point is not correct at least in terms of LOOKUP and INDIRECT.

In my objective tests below I demonstrate that many if not all of these points really are like old wives tales that have not truth to them. Test this using an objective an transparent method and I provide the files so you can make the tests yourself.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-33.png)

In assuring that your spreadsheet is not too slow (heavy), there are a few obvious things to do first. As explained below, you should delete extra rows; you should get rid of range names that are linked to another sheet; you should , you should use ALT, e, k to get rid of links. Other issues that are more subtle include:

*   Does using entire lines in Lookup, SUMIF, INDEX and MATCH cost anything in terms time to calculate and time to insert lines.
*   Is use of the OFFSET function really that bad relative to alternatives as is suggested by some websites and some canned audit packages.
*   How bad is a few conditional conditional formatting conditions in a file.
*   Can you use alternative strategies with INDIRECT to make the calculations not too slow.

My method to evaluate these issues include the following process:

|     |
| --- |
| Create a really big workbook by copying a whole lot of identical sheets using a looping macro (this is shown at the bottom of this page). |
|     |
| When you copy the different sheets, isolate on different methods for the test (e.g. in one case use the entire row in LOOKUP and in another case leave everything the same but lock in the references with F4 used by the LOOKUP; in another example use SUMIF instead of OFFSET) |
|     |
| To test the speed of the calculation in the very heavy model you have created, make a macro to change an input and re-calculate the workbook (with application.calculate); record the time before the calculate and after the calculate. |
|     |
| Make a similar test for inserting a line in the input sheet and the calculation sheet. Insert a line and write a macro that records the time before the insert starts and then measure how long it takes. |

Experimenting with Deleting Sheets, Separating Input Sheets, Selective Calculation
----------------------------------------------------------------------------------

.

The code below illustrates how you can write a simple little macro to test your model and try different experiments. After you run these macros with different tests you can change strategies like separating sheets etc. The first macro is for testing the calculation speed and the second macro is for testing the time to insert a row.

.Sub test\_merchant\_scenario()
Dim start\_test As Variant
Dim start\_code As Single
start\_test = MsgBox(" Test changing the merchant scenario " & Chr(10) & Chr(10) & Chr(10) & \_
" This goes to the time series sheet and changes the merchant code " & Chr(10) & Chr(10) & Chr(10) & \_
" Press OK to Start the Test, Cancel to Stop ", vbOKCancel)

If start\_test = 2 Then Exit Sub
Range("start\_time\_scenario") = Time
Sheets("scenarios").Select
start\_code = Range("merchant\_price")
If Range("merchant\_price") = 9 Then
Range("merchant\_price") = 2
Else
Range("merchant\_price") = 9
End If
Range("end\_time\_scenario") = Time
Range("merchant\_price") = start\_code
Sheets("scenarios").Select
End Sub

The next macro is for testing the time to insert lines.

Sub test\_row\_insert()
Dim start\_test As Variant
start\_test = MsgBox(" Test for inserting line " & Chr(10) & Chr(10) & Chr(10) & \_
" This goes to the input sheet and inserts a line " & Chr(10) & Chr(10) & Chr(10) & \_
" Press OK to Start the Test, Cancel to Stop ", vbOKCancel)

If start\_test = 2 Then Exit Sub
Range("start\_time") = Time
Sheets("scenarios").Select
`Sheets("Inputs").Select Rows("1:5").Select Selection.Insert Shift:=xlDown ActiveCell.FormulaR1C1 = "a" Rows("1:5").Select Range("A2").Activate Selection.delete Shift:=xlUp`
Range("end\_time") = Time
Sheets("scenarios").Select
End Sub

Once you create the macros, you can put tabulate the speed.

![](https://edbodmer.com/wp-content/uploads/2021/11/image-7.png)

I suggest re-running the tests after you have run it one time to make sure that nothing funny is going on. Next, re-save the file after deleting selected sheets to try and understand what is causing the slowness of the model.

Alternative to INDIRECT that is Much Faster
-------------------------------------------

In working with large data it is very clear to me that the INDIRECT function really slows things down. But I really like the way the INDIRECT function can be used to get data from different sheets. If you are using a macro to read data into different sheets you can use the INDIRECT to compare data from different sheets. One alternative to using the INDIRECT function is to use the SUM(Start:End!A1) where the data is inbetween the sheet names Start and End.

If you have a lot of data from different sheets you can use the macro below to read in the data. When using the macro, you need to define the range names for the titles and the row\_1 for where the lookup will be copied.

Sub Macro2()
'
' Alternative to Indirect
'
'
For col = 1 To Range("sheet\_names").Columns.Count 
        ' sheet\_names is range name with sheets to get
         `name_of_sheet = Range("sheet_names").Cells(1, col)` 
         `' Work through the name of each` 

         `sheet name_to_replace = "'" & name_of_sheet & "'"` 
 
         `' create a range name for lookup` 
         `' MsgBox name_to_replace` 

`lookup_name = "=LOOKUP($A5," & name_to_replace & "!A:A," & name_to_replace & "!B:B)"` 

`' MsgBox lookup_name` 

`Range("row_1").Cells(1, col) = lookup_name` 

`' Make sure the row_1 name is there`
Next col
End Sub

Splitting the Input Sheet to Reduce Time to Insert Rows
-------------------------------------------------------

I find the input sheet sometimes is a pain where the inputs go to a big model calculation sheet. If you split up the input sheet that is one of the easiest things to make the model work more quickly.

Some Basic Things to Try when the Model is Heavy
------------------------------------------------

Write a small VBA program to count how many conditional format conditions there are in each sheet. I will demonstrate that this is the biggest culprit in making rows slow to insert is too many conditional formatting items. If it is taking a really long time to insert lines, you can try other things. One is to try are splitting up really long sheets. A second is simply closing a model after working on it for a while and then re-opening it.

**[Excel File Demonstrating Methods for Using SUMIF and OFFSET Functions for Accumulating Debt Service](https://edbodmer.com/wp-content/uploads/2021/02/Monthly-Accumulation.xlsm)
**

Get Rid of Range Names with #REF’s
----------------------------------

I often get models that have an absurd number of range names and many of them cannot be used because they have #REF’s or they refer to other sheets. Here is an extreme example.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-62.png)

The first thing I do in a case like this is use CNTL F3 to get a list of the range names. Then sort the range names and then delete all of the range names with the #REF’s

Testing the Speed of a Model – The Case of Using the Entire Line in LOOKUP, SUMIF, INDEX, MATCH etc.
----------------------------------------------------------------------------------------------------

In this section I test something which is very close to my heart. I demand that my students stop wasting time pressing the F4 key to lock cells in the LOOKUP, INDEX, MATCH, SUMIF, IRR and other functions. I tell them to hurry up and just use the entire row or column. I think it makes the models less prone to errors and more transparent. But the question is, does it slow down the models. In particular does use of the entire row slow down the insert process when you are editing sheets, which can be really painful. This is what I test here.

The results of my test are shown in the screenshot below.  The top part of the screenshot demonstrates the inputs for the test.  The second part of the screenshot demonstrates that outputs for the file size and the time taken for calculation for the scenario.  After the scenario is run with different equations, the tests for the size and calculation time can be copied. The screenshot below shows how you can compute the time difference in seconds by multiplying the time by 60 seconds per minute and 60 minutes per hour and 24 hours per day.

#### Case with LOOKUP using entire row

In the discussion below I will go through the process to create a heavy model and to make tests. But before we start, I summarise some of the key results. I first test the crucial subject of whether a lookup function that uses the entire line causes problems. My research suggests that problems with using the entire line as illustrated below are complete B.S. and Old Wives Tales. The screenshot below illustrates the case with the entire line. This is a typical thing I do to make the programming easier.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-16-1536x765.png)

The screenshot below is for using the lookup function with the entire line. This sheet uses the LOOKUP with the entire line on 80 sheets where each sheet has 400 columns of calculations. The tests are illustrated on the screenshot below. In case you don’t believe me, I have put this large file below so you can download it. Note that:

*   The thing that takes the most time is inserting lines in the input sheet. This takes 89 seconds.
*   The time to make a single calculation with the 81 calculation sheets takes 13 seconds.
*   Note that the size of the file is 10 MB — this should be enough to be called a heavy model.
*   The time to insert rows in the calculation sheets is not long.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-17.png)

#### Case with Using Lookup with Fixed Ranges Using F4

Now lets go to the case where we fix the inputs instead of using the entire row in the LOOKUP function. In this case instead of clicking on the whole line, you use only the cells that will be used in the calculation. The change in the formula for the LOOKUP function is shown in the screenshot below. The general form LOOKUP(Lookup cell, Fixed Input Comparison, Fixed Input Values).

![](https://edbodmer.com/wp-content/uploads/2021/04/image-19.png)

Here is the big result for this case where you have to waste a lot of time pressing the F4 key for both the lookup index (the date line) and the data line (the interest rates). In this case the time for the calculations are just about the same. This for me is a big result. Namely, that wasting a lot of time pressing F4 inside the calculations does not save time.

*   First it takes about the same time with the calculations, which are about 13 seconds.
*   More importantly, the time to insert lines in the input sheet is the same as the case where the lines are inserted. Both cases seem to take forever at 89 seconds.
*   When you input lines in a single calculation sheet, things are not bad at all — it only takes 4 seconds.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-20.png)

In summary, complaining about the use of entire rows or columns is a B.S. old wives tail.

Test of Volatile Functions — the Offset Case
--------------------------------------------

One of the things that prompted me to make this analysis is something called the rainbow program. I cannot tell you how much I hate this program and how destructive it is. The rainbow program gives a score that auditors can use to critique a program. The output from the rainbow program is shown below. It gives you a lower score if you use the the OFFSET function because the program tells you that it is a volatile function. If you are like me, you have made some of your own functions — UDF’s and you have tried to use the application.volatile statement. It never makes much of a difference to me. Other functions do not run when you they are not affected by some input that has changed but volatile functions run whenever anything is changed. In writing UDF’s this has never made much difference to me as if you write a good model, all of the equations are used when you make a change. Critiques of OFFSET are indeed an old wives tale.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-36.png)

It seems that Mr. Power makes the same point in an emotional way. If you can use the files and tests that I have provided to demonstrate that my tests are biased I would be very interested to see the results.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-34.png)

In this case, I left in the OFFSET function with the SUM(OFFSET()). But I deleted the SUMIF method. I did this for one sheet as illustrated below. This is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-29.png)

After removing the offset and only leaving the OFFSET function above, I copy the sheets 100 times and make a big file. This file is 13 MB as shown below using the filesize function. When you add the 100 sheets, the file takes a long time (it still has the XLOOKUP function). The results of this test are:

*   Time to calculate: 27 seconds
*   Time to insert in input: 470 seconds
*   Time to insert in one calculation sheet: 12 seconds
*   Time to add all of the sheets: 1,006

![](https://edbodmer.com/wp-content/uploads/2021/04/image-28.png)

### Sumif Case

In this case, I left in the SUMIF function and not the OFFSET. I deleted the OFFSET method as shown in the screenshot below. I did this for one sheet as illustrated below. This is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-30.png)

After starting with a file that has no copied sheets, I copy 100 sheets. Then after I copy the 100 sheets I test how long the calculation takes using the test where I change a variable from one amount to another. After changing the variable and running the calculate all I see how long the calculation takes. The interesting thing here is that the speed is exactly the same as the speed with the OFFSET function.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-32.png)

Creating Macros to Test the Speed of a Heavy Model
--------------------------------------------------

You can create a macro with the Time and Size statement.  Then you can put the issue that make your model calculations operate slowly or that make you models difficult to structure (add lines and so forth).  You can also test how large your models are before and after you do something like accidently go to the end of the sheet.   The file and the macros shown below illustrate the test I have tried to make for evaluating whether using an entire line in the LOOKUP function makes the file heavier than if you lock in the input cells and do not use the entire row or column.  I have made the file so that you can try different equations and then I make a loop that goes around and re-calculates many times.  In the exercise below, I have tried the following four scenarios:

1.  No Equation
2.  The look up equation with fixed values (e.g. LOOKUP(B5,$A$7:$K$7,$A$8:$K$8))
3.  The look up equation with total rows (e.g. LOOKUP(B5,A:A,K:K))
4.  The lookup interpolate UDF function (e.g. INTERPOLATE\_LOOKUP(B5,A:A,K:K))

You can also test the speed of alternative ways to run a macro as illustrated in the macro below.  Note how the TIME function is used before and after the macro below.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-31.png)

![](https://edbodmer.com/wp-content/uploads/2020/04/Macro-Speed.jpg)

.

.

Sub table()

Range("StartTime") = Time
Dim output() As Double
Dim Rows, Columns As Single
Dim Cost\_of\_Equity As Single
Dim array\_size As Single

Cost\_of\_Equity = Range("Applied").Cells(9, 1)
Terminal\_Value = Range("Applied").Cells(6, 1)
Rows = Range("endrow") - Range("startrow") + 1
Columns = Range("endcol") - Range("startcol") + 1

array\_size = Columns \* Rows

'MsgBox Rows & " " & Columns
Range(Cells(Range("startrow"), Range("endcol")), Cells(Range("endrow"), Range("endcol"))).Select

'Range(Cells(13, 6), Cells(31, 16)).ClearContents
' Selection.ClearContents

ReDim output(Rows, Columns) As Double

Application.ScreenUpdating = False

RowCounter = 0

For Row = Range("startrow") To Range("endrow")
RowCounter = RowCounter + 1
ColumnCounter = 0

Range("Applied").Cells(9, 1) = Cells(Row, Range("startcol") - 1)

For Column = Range("startcol") To Range("endcol")
ColumnCounter = ColumnCounter + 1

Range("Applied").Cells(6, 1) = Cells(Range("startrow") - 1, Column)

'Cells(Row, Column) = Range("truevalue")
'MsgBox Range("truevalue")

output(RowCounter, ColumnCounter) = Range("truevalue")

Next Column


Next Row

Range("table\_output") = output

Range("Applied").Cells(9, 1) = Cost\_of\_Equity
Range("Applied").Cells(6, 1) = Terminal\_Value

Range("EndTime") = Time
End Sub

Saving, Closing and Opening a File to Speed Up Row Insertion
------------------------------------------------------------

The code below checks the speed of the calculaitons

![](https://edbodmer.com/wp-content/uploads/2021/04/image-15.png)

Sub calc\_tests()
Application.Calculation = xlCalculationManual
Range("debt\_pct") = 0.8
ActiveWorkbook.Save
Range("start\_size\_calc") = filesize
Range("start\_calc") = Time
Range("debt\_pct") = 0.9
Application.CalculateFull
Range("end\_calc") = Time
'end\_time\_insert
'start\_time\_insert
Range("end\_size\_calc") = filesize
Application.Calculation = xlCalculationSemiautomatic
End Sub

Random things to try when it takes forever to insert lines
----------------------------------------------------------

### Open File without Macros

One of the really irritating things that can happen with a heavy model is the time it takes to simply insert lines. I was working on a model when it took about 2-4 minutes simply to add lines to a page. I tried many different things, but one of the things that worked was to open the file without enabling the macros. Who knows why this worked but it did help

### Close the file and re-open it

This sounds so stupid but it does work sometimes.

Eliminating too Many Conditional Formatting Conditions
------------------------------------------------------

I had a big model that was really slow in adding or deleting lines. I looked at various sheets and there was not too much conditional formatting. But one sheet has 57,000 different conditions. This did not cause problems in only one sheet, but inserting sheets took forever in each sheet.

I have made some macros to get rid of the surplus conditional formatting conditions. You can press the RESET button and press the link to get rid of prior conditional formatting conditions. The VBA code to get rid of the formatting conditions is shown below.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-42.png)

‘ MsgBox clean\_conditional\_formatting

    If clean_conditional_formatting Then
        Application.ScreenUpdating = False
        On Error GoTo 0
    
        For row = 1 To max_row
            range_name = row & ":" & row
            Range(range_name).Select
            Selection.FormatConditions.Delete
        Next row
    
        Cells.Select
        FormatConditions.Select
        Selection.FormatConditions.Delete
    
    End If

Reducing Size by Removing Columns at the End of a Sheet
-------------------------------------------------------

When re-structuring models I receive from other people, I often find surprising and easy ways to make models operate more quickly through eliminating columns that are mistakenly added to the end of a sheet. 

I have noticed that when people hide columns at the end of a sheet, there is often some little problem with something getting to the end.  Further, there may be some kind of shape such as a button that somehow is at the end of the sheet.  Excel tells you to delete all of the columns at the end of the sheet and then save the file. When there is a shape somewhere, this does not work and the message shown below appears.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9758&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=14184&rand=0.9097473247845654)