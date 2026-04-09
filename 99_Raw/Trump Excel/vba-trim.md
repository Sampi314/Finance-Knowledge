# Excel VBA TRIM Function (explained with Examples)

**Source:** https://trumpexcel.com/vba-trim

---

[Skip to content](https://trumpexcel.com/vba-trim/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-trim/#below-title)

Excel already has a [TRIM](https://trumpexcel.com/excel-trim-function/)
 worksheet function that you can use to [get rid of leading, trailing, and extra spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 in between words/strings.

There is a TRIM function in VBA as well (and it does exactly the same thing – remove extra spaces).

**Why do we need a TRIM function in VBA too?**

Fair question!

While you can work with the inbuilt TRIM function in Excel worksheets to get rid of spaces. in some cases, you may need to do this using VBA.

This could be as a part of a bigger code.

Syntax of the VBA TRIM function
-------------------------------

_TRIM(String)_

‘String’ is the argument that can be a text string or a variable that holds a text string.

Let’s learn how to use the VBA TRIM function with a couple of examples.

### Example 1 – Showing Result in a message box

Suppose you have the following text in cell A1

![Excel VBA Trim Function - Examples 1 Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20444%20102'%3E%3C/svg%3E)

Note that there are spaces before and after the sentence.

The below code would take this sentence, and show the result after trimming the extra spaces

Sub TrimExample1()
MsgBox Trim(Range("A1"))
End Sub

![VBA Trim Function code result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20186'%3E%3C/svg%3E)

There is one important thing to know when using the TRIM function in VBA –  it will only remove the leading and trailing spaces. It will not remove the extra spaces in between words (which the in-built TRIM function in the worksheet does).

For example, suppose you have the following text in cell A1 (with extra spaces in between words):

![VBA TRIM Function - Extra spaces in between words](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%2095'%3E%3C/svg%3E)

If I use the above VBA code, it will show a message box as shown below:

![MessageBox with extra spaces](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20364%20186'%3E%3C/svg%3E)As you can see in the message box result, the extra spaces between words are not removed by the VBA TRIM function.

_**Then what’s the alternative?**_

If you want to remove leading, trailing, as well as double spaces in between words, it’s better to use the following code:

Sub TrimExample1()
MsgBox WorksheetFunction.Trim(Range("A1"))
End Sub

The above code uses the worksheet TRIM function (instead of using the TRIM function in VBA).

Note: VBA Trim function does not remove the non-whitespace characters – such as newlines (_vbNewLine_, _vbCrLf_) etc.

### Example 2 – Quickly Remove Leading and Trailing Spaces from a Range of Cells

Suppose you have a data set as shown below where there are leading and trailing spaces:

![VBA TRIM Example 2 Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20152'%3E%3C/svg%3E)

You can use the below code to instantly clean this data and remove all the leading and trailing spaces:

Sub TrimExample1()
Dim Rng As Range
Set Rng = Selection
For Each Cell In Rng
Cell.Value = Trim(Cell)
Next Cell
End Sub

The above code goes through all the cells in the selection and removes the leading and trailing spaces.

![Clean Data with VBA TRIM Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20176'%3E%3C/svg%3E)

**You May Also Like the Following Excel/VBA Tutorials:**

*   [10 Ways to Clean Data in Excel.](https://trumpexcel.com/clean-data-in-excel/)
    
*   [Excel VBA Split Function.](https://trumpexcel.com/vba-split-function/)
    
*   [Excel VBA InStr Function.](https://trumpexcel.com/excel-vba-instr/)
    
*   [VBA LCase Function](https://trumpexcel.com/vba-lcase/)
    .
*   [VBA UCase Function](https://trumpexcel.com/vba-ucase/)
    .
*   [Creating a User Defined Function (UDF) in Excel VBA.](https://trumpexcel.com/user-defined-function-vba/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Excel VBA TRIM Function (explained with Examples)”
-----------------------------------------------------------------

1.  I didn’t expect to get any response to my search. Instead I got the equal most complete treatment I have come across of any issue … ever! Thanks! Loved the live ‘Run the Code’.
    
    [Reply](https://trumpexcel.com/vba-trim/#comment-14783)
    
2.  Sub TrimCells()  
    Dim Mrang As Range  
    Dim Mcell As Range  
    On Error GoTo hendler:  
    ‘ used selected range  
    Set Mrang = Intersect(Range(Selection.Address), Range(Selection.Address).Parent.UsedRange)  
    For Each Mcell In Mrang  
    If Len(Mcell) > 0 Then Cell = Trim(Mcell)  
    ‘ all space in text  
    While InStr(1, Mcell, ” “) > 0  
    Mcell = Replace(Mcell.Value2, ” “, ” “)  
    Wend  
    Next Mcell  
    Set Mrang = Nothing  
    Set Mcell = Nothing  
    hendler:  
    Err.Clear  
    End Sub
    
    [Reply](https://trumpexcel.com/vba-trim/#comment-13852)
    
3.  Thanks for posting this. When I copy this code, it cycles through all the cells in the range, but doesn’t perform the trim on them. Or maybe it does, but it doesn’t replace the current string in the cell, so none of the leading spaces are removed.  
    Sub Trimcells()  
    Dim Rng As Range  
    Range(“B2:D10”).Select  
    Set Rng = Selection  
    For Each Cell In Rng  
    Cell.Value = trim(Cell)  
    Next Cell
    
    End Sub
    
    [Reply](https://trumpexcel.com/vba-trim/#comment-11267)
    
    *   Your code should say:
        
        Cell.Value = trim(Cell.Value)
        
        [Reply](https://trumpexcel.com/vba-trim/#comment-13513)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-trim/#respond)

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