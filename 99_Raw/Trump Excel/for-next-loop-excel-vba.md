# For Next Loop in Excel VBA - A Beginner's Guide with Examples

**Source:** https://trumpexcel.com/for-next-loop-excel-vba

---

[Skip to content](https://trumpexcel.com/for-next-loop-excel-vba/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/for-next-loop-excel-vba/#below-title)

In VBA, looping is used when you need to perform the same task multiple times until a condition is met (or until a condition is true).

In this tutorial, you’ll learn how to use the For Next Loop in Excel VBA.

If you’re interested in learning VBA the easy way, check out my **[Online Excel VBA Training](https://trumpexcel.com/excel-vba-jetpack-course/)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/for-next-loop-excel-vba/#)

Using FOR NEXT Loop in Excel VBA
--------------------------------

‘For Next’ Loop works by [running the loop](https://trumpexcel.com/vba-loops/)
 the specified number of times.

For example, if I ask you to add the integers from 1 to 10 manually, you would add the first two numbers, then add the third number to the result, then add the fourth number to the result, as so on..

Isn’t it?

The same logic is used in the For Next loop in VBA.

You specify how many times you want the loop to run and also specify what you want the code to do each time the loop is run.

Here is the For Next loop format you need to use in VBA to add the first 10 whole numbers.

For i = 1 to 10
\[add the ith positive integer to the result\]
Next i

Now let’s have a look at a few examples of how to use the For Next loop.

### Example 1: Adding the First 10 Positive Integers

Below is the code that will add the first 10 positive integers using a For Next loop. It will then display a message box showing the sum of these numbers.

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

And finally, when the loop ends and when Total has the sum of the first 10 positive integers, a [MsgBox](https://trumpexcel.com/vba-msgbox/)
 simply displays the result in a message box.

**[Click here to download the example file](https://www.dropbox.com/s/3iuki7m0o46icrm/Add-First-10-Positive-Integers.xlsm?dl=1)
**

### Example 2: Adding the first 5 Even Positive Integers

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

Note that we started the Count value from 2 and also used Step 2 in the For syntax.

Step 2 would tell the code to increment the ‘Count’ value by 2 every time the loop is run. So the Count value starts from 2 and then becomes 4, 6, 8 and 10 as the looping occurs.

NOTE: Another way of doing this could be to run the loop from 1 to 10 and within the loop check whether the number is even or odd. However, using Step, in this case, is a more efficient way as it does not require the loop to run 10 times, but only 5 times.

**[Click here to download the example file](https://www.dropbox.com/s/t71pv4gc2pvqdek/Add-First-5-Even-Positive-Integers.xlsm?dl=1)
**.

### Example 3: Get the Numeric Part from an Alphanumeric String

‘For Next’ loop can also be used to loop through each character in a string.

For example, if you have a list of alphanumeric strings, you can use the For Next loop to extract the numbers from it (as shown below):

![For Next Loop in Excel VBA Extract Numbers from Alphanumeric](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20318%20180'%3E%3C/svg%3E)

Here is a code that creates a custom function in VBA that can be used like any other worksheet function.

It extracts the numeric part from the alphanumeric string.

Function GETNUMERIC(Cl As Range)
Dim i As Integer
Dim Result as Long
For i = 1 To Len(Cl)
If IsNumeric(Mid(Cl, i, 1)) Then
Result = Result & Mid(Cl, i, 1)
End If
Next i
GetNumeric = Result
End Function

In this code, the number of times the loop is run is dependent on the length of the alphanumeric string (it uses the [LEN function](https://trumpexcel.com/excel-len-function/)
 to find the length of the string).

You need to put this function in the module code window, and then you can use it like any other worksheet function.

![For Next Loop in Excel VBA GetNumeric](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20172'%3E%3C/svg%3E)

**[Click here to download the example file](https://www.dropbox.com/s/mo6vc45c0bsz2p4/Get-Numeric-Part-from-Alphanumeric-String.xlsm?dl=1)
**.

### Example 4: Getting Random Numbers in the Selected Range

Suppose you want to quickly enter random numbers in the selected cells, here the code that will do it.

Sub RandomNumbers()
Dim MyRange As Range
Dim i As Integer, j As Integer
Set MyRange = Selection
For i = 1 To MyRange.Columns.Count
For j = 1 To MyRange.Rows.Count
MyRange.Cells(j, i) = Rnd
Next j
Next i
End Sub

This is an example of nested For Next loop where a For loop is used within a For Loop.

Suppose you make a selection of 10 rows and 4 columns, the value of i varies from 1 to 4 and the value of j varies from 1 to 10.

When the first For loop is run, the value of i is 1. It then moves to the second For loop which runs 10 times (for each row).

Once the second For loop has been executed 10 times, it goes back to the first For loop where now the value of i becomes 2. Again the next For loop runs for 10 times.

This is how the nested For Next loop works.

![For Next Loop in Excel VBA random Numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%20235'%3E%3C/svg%3E)

**[Click here to download the example file](https://www.dropbox.com/s/x5hzf81wfdb6qdn/Insert-Random-Numbers.xlsm?dl=1)
**.

**You May Also Like the Following Excel VBA Tutorials:**

*   [Working with Cells and Ranges in Excel VBA](https://trumpexcel.com/vba-ranges/)
    .
*   [Working with Worksheets in Excel VBA](https://trumpexcel.com/vba-worksheets/)
    .
*   [Working with Workbooks using VBA](https://trumpexcel.com/vba-workbook/)
    .
*   [Using IF Then Else Statements in VBA](https://trumpexcel.com/if-then-else-vba/)
    .
*   [Excel VBA Select Case](https://trumpexcel.com/vba-select-case/)
    .
*   [Creating a User-Defined Function in Excel](https://trumpexcel.com/user-defined-function-vba/)
    .
*   [Excel VBA Events – An Easy (and Complete) Guide](https://trumpexcel.com/vba-events/)
    
*   [How to Record a Macro in Excel](https://trumpexcel.com/record-macro-vba/)
    .
*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    .
*   [How to Create an Add-in in Excel](https://trumpexcel.com/excel-add-in/)
    .
*   [How to Save and Reuse Macro using Excel Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
    .
*   [Useful Excel Macro Examples for Beginners](https://trumpexcel.com/excel-macro-examples/)
    .
*   [Using InStr Function in VBA](https://trumpexcel.com/excel-vba-instr/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “For Next Loop in Excel VBA – A Beginner’s Guide with Examples”
-----------------------------------------------------------------------------

1.  Hi, Is my first time here, really good. Question. I have a column Range(“A2:2700”) with a random sequence of numbers (1 to 48 is the set), I would like to produce a report of how many time each number followed each one, but has to start from the button to the to the searching process like A2700 founded 1 next cell A2699 found 2 then count 1 on C3 for the numbers 2 and 1. thank you for any help.
    
    [Reply](https://trumpexcel.com/for-next-loop-excel-vba/#comment-11648)
    
2.  I am new learner. How to write code in VB if I want to add a range of cells using loops function. Suppose I want to add data in rows A2:B2, A3:B3, A4:B4 so on and get its result in corresponding rows C2, C3, C4
    
    [Reply](https://trumpexcel.com/for-next-loop-excel-vba/#comment-11249)
    
3.  Hi Sumit………
    
    Trying to run VBA, But it occurs attached error.
    
    Pls help.
    
    [https://uploads.disquscdn.com/images/ddf545f5157c16f1137bf3940f799825401ffde304aba74230c0b5d6bef980f3.jpg](https://uploads.disquscdn.com/images/ddf545f5157c16f1137bf3940f799825401ffde304aba74230c0b5d6bef980f3.jpg)
    
    [Reply](https://trumpexcel.com/for-next-loop-excel-vba/#comment-3883)
    
    *   Hello Anand,, It seems you have not enabled macros. When you open a file that has a macro, it shows a prompt in a bar that asks you to enable macros. Once you enable it, only then can it run the macros in the file.
        
        [Reply](https://trumpexcel.com/for-next-loop-excel-vba/#comment-3884)
        
        *   Got Resolved. Thanks !
            
            And Helpful Post………….
            
            [Reply](https://trumpexcel.com/for-next-loop-excel-vba/#comment-3885)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/for-next-loop-excel-vba/#respond)

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