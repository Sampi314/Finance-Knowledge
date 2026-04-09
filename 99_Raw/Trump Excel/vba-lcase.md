# VBA LCASE Function - Convert Text to Lower Case in Excel

**Source:** https://trumpexcel.com/vba-lcase

---

[Skip to content](https://trumpexcel.com/vba-lcase/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-lcase/#below-title)

In Excel worksheet, there is a [LOWER function](https://trumpexcel.com/excel-lower-function/)
 that converts a text string into lower case.

Just like the LOWER function, there is a similar inbuilt function in Excel VBA – **LCASE**

The VBA LCASE function takes a string as the input and converts it into a lower case string.

Syntax of VBA LCASE Function
----------------------------

Below is the syntax of the VBA LCase function

LCase(String)

**‘String’** is the text that you want to convert to lower case.

You can use a text string, a range reference that contains the text string, or a variable that has the text string.

Let’s have a look at a couple of example of using the LCase function.

VBA LCase Examples
------------------

The below code would convert the specified text into lower case and show it in a [message box](https://trumpexcel.com/vba-msgbox/)
.

Sub LCaseExample1()
MsgBox LCase("Good Morning")
End Sub

![Excel VBA LCase Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%20186'%3E%3C/svg%3E)

Here is another example, where we have used a variable (‘Var’) to hold the text string and then used the LCase function to convert it into lower case.

Sub LCaseExample2()
Dim Var As String
Var = "Good Morning"
MsgBox LCase(Var)
End Sub

Another example below shows how to take the string from a cell (A1) and show the lowercase version of it in a message box.

Sub LCaseExample3()
MsgBox LCase(Range("A1"))
End Sub

While all these above examples work, you’re unlikely to use this function to simply convert or show the lowercase string.

Below is a **more practical example** of the LCase function in Excel VBA. The below code would go through all the cells in the selected range and convert all the text strings into lower case.

Sub LCaseExample1()
Dim rng As Range
Set rng = Selection
For Each Cell In rng
Cell.Value = LCase(Cell)
Next Cell
End Sub

![VBA LCase to convert selection to lower case](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20320'%3E%3C/svg%3E)

A few important things to know about the VBA LCase function:

1.  It affects only the Uppercase characters of the text string. Any character other than the Uppercase text characters is left unchanged.
2.  If you use a null character (or a reference to an empty cell), it will return a null character.

**Other Useful VBA Functions:**

*   [VBA UCase Function](https://trumpexcel.com/vba-ucase/)
    .
*   [VBA TRIM Function](https://trumpexcel.com/vba-trim/)
    .
*   [VBA INSTR Function](https://trumpexcel.com/excel-vba-instr/)
    .
*   [VBA SPLIT FUNCTION](https://trumpexcel.com/vba-split-function/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “VBA LCASE Function – Convert Text to Lower Case in Excel”
------------------------------------------------------------------------

1.  Here is an update:
    
    Sub LCaseExample1()  
    Dim W as Worksheet: set W = ActiveSheet  
    Dim R As Range  
    Set R = Selection  
    Dim cell as Range  
    For Each cell In Selection  
    Cell.Value = LCase(Cell)  
    Next cell  
    End Sub
    
    [Reply](https://trumpexcel.com/vba-lcase/#comment-13811)
    
2.  Sub LCaseExample1()  
    Dim rng As Range  
    Set rng = Selection  
    For Each Cell In rng  
    Cell.Value = LCase(Cell)  
    Next Cell  
    End Sub
    
    This code is wrong.  
    What about Dim for Cell?
    
    [Reply](https://trumpexcel.com/vba-lcase/#comment-13810)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-lcase/#respond)

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