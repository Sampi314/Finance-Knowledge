# Excel VBA InStr Function - Explained with Examples

**Source:** https://trumpexcel.com/excel-vba-instr

---

[Skip to content](https://trumpexcel.com/excel-vba-instr/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba-instr/#below-title)

Yesterday, I got an email from one of my readers – June.

She wanted to know how to apply bold font format to a specific part of a string within a cell. For example, apply the bold format to only the word ‘Hello’ from ‘Hello World’.

And she wanted to do this for hundreds of cell at once.

Since there is no inbuilt functionality in Excel that can do that, I created a simple macro that uses the **Excel VBA InStr function** (you will see how to do this in Example 4 in this tutorial).

But first, let’s see how the Excel VBA InStr function works!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba-instr/#)

Excel VBA InStr Function
------------------------

In this tutorial, I will explain the usage of InStr function in Excel VBA and see some practical examples where it can be used.

### Excel VBA InStr Function – Introduction

InStr function finds the position of a specified substring within the string and returns the first position of its occurrence.

For example, if you want to find the position of ‘x’ in ‘Excel’, using the Excel VBA InStr function would return 2.

### Syntax of InStr Function

InStr( \[Start\], String1, String2, \[Compare\] )

*   **\[Start\]** – (optional argument) this is an integer value that tells the InStr function the starting position from which it should start looking. For example, if I want the search to start from the beginning, I will enter the value as 1. If I want it to begin with the third character onwards, I will use 3. If omitted, the default value of 1 is taken.
*   **String1** – This is the main string (or the parent string) in which you want to search. For example, if you’re looking for the position of x in Excel, String 1 would be “Excel”.
*   **String2** – This is the substring that you are searching for. For example, if you’re looking for the position of x in Excel, String2 would be x.
*   **\[Compare\]** – (optional argument) You can specify one the following three values for \[compare\] argument:
    *   **vbBinaryCompare** – This would do a character by character comparison. For example, if you’re looking for ‘x’ in ‘Excel’, it will return 2, but if you’re looking for ‘X’ in ‘Excel’, it will return 0 as X is in upper case. You can also use 0 instead of vbBinaryCompare. If the \[Compare\] argument is omitted, this is the taken as default.
    *   **vbTextCompare** – This would do a textual comparison. For example, if you look for ‘x’ or ‘X’ in Excel, it would return 2 in both the cases. This argument ignores the letter case. You can also use 1 instead of vbTextCompare.
    *   **vbDatabaseCompare** –  This is used for Microsoft Access only.  It uses the information in the database to perform the comparison. You can also use 2 instead of vbDatabaseCompare.

#### Additional Notes on Excel VBA InStr Function:

*   InStr is a VBA function and not a worksheet function. This means that you can not use it within the worksheet.
*   If String2 (which is the substring whose position you’re looking for) is empty, the function would return the value of the \[Start\] argument.
*   If the InStr function can not find the substring within the main string, it would return 0.

Now let’s have a look at some example of using the Excel VBA InStr Function

### Example 1 – Finding the Position from the beginning

In this example, I will use the InStr function to find the position of ‘V’ in ‘Excel VBA’ from the beginning.

The code for this would be:

Sub FindFromBeginning()
Dim Position As Integer
Position = InStr(1, "Excel VBA", "V", vbBinaryCompare)
MsgBox Position
End Sub

When you run this code, it will show a [message box](https://trumpexcel.com/vba-msgbox/)
 with the value 7, which is the position of ‘V’ in the string ‘Excel VBA’.

### Example 2 – Finding the Position from the beginning of the Second Word

Suppose, I want to find the position of ‘the’ in the sentence – ‘The quick brown fox jumps over the lazy dog’

However, I want the search to begin with the second word onwards.

In this case, we need to change the \[Start\] argument to make sure it specifies the position from where the second word starts.

Here is the code that will do this:

Sub FindFromSecondWord()
Dim Position As Integer
Position = InStr(4, "The quick brown fox jumps over the lazy dog", "the", vbBinaryCompare)
MsgBox Position
End Sub

This code will show the message box with the value 32 as we have specified the starting position as 4. Hence it ignores the first ‘The’ and finds the second ‘the’ in the sentence.

If you want to make it more dynamic, you can enhance the code so that it automatically ignore the first word.

Here is the enhanced code that will do this:

Sub FindFromSecondWord()
Dim StartingPosition As Integer
Dim Position As Integer
StartingPosition = InStr(1, "The quick brown fox jumps over the lazy dog", " ", vbBinaryCompare)
Position = InStr(StartingPosition, "The quick brown fox jumps over the lazy dog", "the", vbBinaryCompare)
MsgBox Position
End Sub

This code first finds the position of a space character and stores it in the variable StartingPosition.

It then uses this variable as the starting position to look for the word ‘the’.

Hence it returns 32 (which is the starting position of ‘the’ after the first word).

### Example 3 – Finding the Position of @ in Email Address

You can easily create a custom function to find the position of @ in an email address using the Excel VBA InStr function.

Here is the code to create the custom function:

Function FindPosition(Ref As Range) As Integer
Dim Position As Integer
Position = InStr(1, Ref, "@")
FindPosition = Position
End Function

Now you can use this custom function as any other worksheet function. It will take a cell reference as input and give you the position of @ in it.

![Excel VBA InStr Function - Finding @](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20178'%3E%3C/svg%3E)

Similarly, you can create a custom function to find the position of any substring within the main string.

### Example 4 – Highlighting a Part of String within Cells

This is the query that was asked by June (my reader who also inspired me to write this tutorial).

Here is a sample data in the format June sent me:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20183%20289'%3E%3C/svg%3E)

Her query was to make the numbers outside the bracket bold.

Here is the code I created that does this:

Sub Bold()
Dim rCell As Range
Dim Char As Integer
For Each rCell In Selection
 CharCount = Len(rCell)
 Char = InStr(1, rCell, "(")
 rCell.Characters(1, Char - 1).Font.Bold = True
Next rCell
End Sub

The above code uses the [For Each loop](https://trumpexcel.com/vba-loops/)
 to go through each of the cells in the selection. It identifies the position of the opening bracket character using the [InStr function](https://trumpexcel.com/excel-vba-instr/)
. It then changes the font of the text before the bracket.

To use this code, you need to copy and paste in a module in the VB editor.

Once you have copy pasted the code, select the cells in which you want to do this formatting and [run the macro](https://trumpexcel.com/run-a-macro-excel/)
 (as shown below).

![Excel VBA InStr Function - Bold Format Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20308'%3E%3C/svg%3E)

**You May Also Like the following Excel VBA Tutorials:**

*   [Excel VBA SPLIT Function](https://trumpexcel.com/vba-split-function/)
    .
*   [VBA TRIM Function](https://trumpexcel.com/vba-trim/)
    .
*   [The Ultimate Guide to Excel VBA Loops](https://trumpexcel.com/vba-loops/)
    .
*   [A Beginner’s Guide to Using For Next Loop in Excel VBA](https://trumpexcel.com/for-next-loop-excel-vba/)
    .
*   [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)
    .
*   [How to Combine Multiple Workbooks into One Excel Workbook.](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    .
*   [Useful Excel VBA Macro Examples for Beginners](https://trumpexcel.com/excel-macro-examples/)
    .
*   [How to Sort Data in Excel using VBA (A Step-by-Step Guide)](https://trumpexcel.com/sort-data-vba/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “Excel VBA InStr Function – Explained with Examples”
------------------------------------------------------------------

1.  Hi ,  
    I was asked to copy a range of cells from another sheet and paste it in the main sheet.Then compare this range to the entire column containing single word or sometimes even sentences. I have drafted using INSTR function where It compared single word with those range of valus I pasted. But it is not comparing sentences to those range evnthough I have a word within that sentence. Can you help me with this.  
    heres my code,
    
    Sub fillcells()  
    Dim finalrow As Integer  
    Sheets(“Data”).Range(“B2:I10”).ClearContents  
    Dim srchrng As Range, cel As Range  
    Dim zipA As Range, srch As Range  
    Dim i As Integer  
    Set zipA = Range(“B1:I1”)  
    Set srchrng = Range(“A2:A10”)  
    i = 2  
    For Each cel In srchrng  
    j = 2  
    For Each srch In zipA
    
    If InStr(1, srch.Value, cel.Value, vbBinaryCompare) Then  
    Cells(i, j) = “yes”  
    j = j + 1  
    GoTo Mylabel  
    Else  
    Cells(i, j) = “no”  
    j = j + 1  
    GoTo Mylabel  
    End If
    
    Mylabel:  
    Next srch  
    GoTo Mylabel1
    
    Mylabel1:  
    i = i + 1  
    Next cel  
    End Sub
    
    [Reply](https://trumpexcel.com/excel-vba-instr/#comment-14154)
    
2.  This post must be very old, sorry for late response, but I agree with Tjaart. You have a wonderful method of teaching, always very clear and makes me want to try it myself!
    
    [Reply](https://trumpexcel.com/excel-vba-instr/#comment-13491)
    
    *   Thank you for the kind words Inna… Glad you’re finding the tutorials useful!
        
        [Reply](https://trumpexcel.com/excel-vba-instr/#comment-13494)
        
3.  Hi sumit, can you help me with this. Suppose we have a employee table in sheet 1 and my task is if managerId is typed in one cell, i should get the employee name accordingly in the very next cell and this should be displayed in the second sheet. Can you please help me with this…
    
    [Reply](https://trumpexcel.com/excel-vba-instr/#comment-12554)
    
4.  CharCount is not being used in this code, is it? What’s the purpose of using it?
    
    [Reply](https://trumpexcel.com/excel-vba-instr/#comment-11564)
    
5.  I thrive on simplicity. Only a real teachers understand that concept. Explaining something with 123, 1 being the problem, 2 being the code, 3 being the answer. The logic is simple. Most snippets start with 2. Thanks mate, you are great.
    
    [Reply](https://trumpexcel.com/excel-vba-instr/#comment-10609)
    
6.  Thanks a lot for this simple and awesome tutorial
    
    [Reply](https://trumpexcel.com/excel-vba-instr/#comment-8763)
    
    *   Glad you liked it!
        
        [Reply](https://trumpexcel.com/excel-vba-instr/#comment-8764)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-vba-instr/#respond)

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