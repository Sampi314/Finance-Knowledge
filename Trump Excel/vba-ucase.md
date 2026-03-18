# VBA UCASE Function – Convert Text to Upper Case in Excel

**Source:** https://trumpexcel.com/vba-ucase

---

[Skip to content](https://trumpexcel.com/vba-ucase/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-ucase/#below-title)

In Excel worksheet, the [UPPER function](https://trumpexcel.com/excel-upper-function/)
 converts all the lowercase characters of a text string into uppercase.

There is a similar function in that also does the same – the **UCase** function.

The VBA UCase function takes a string as the input and converts all the lower case characters into upper case.

Syntax of the VBA UCASE Function
--------------------------------

Below is the syntax of the VBA UCase function

UCase(String)

**‘String’** is the text in which you want to convert all the lowercase to uppercase.

You can use a text string, a range reference that contains the text string, or a variable that has the text string.

Let’s have a look at a couple of example of using the UCase function in Excel VBA.

VBA UCase Examples
------------------

The below code would convert the specified text into uppercase and then display a [message box](https://trumpexcel.com/vba-msgbox/)
 with this text.

Sub UCaseExample1()
MsgBox UCase("Good Morning")
End Sub

![Excel VBA Ucase Function Example - Message Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20170%20186'%3E%3C/svg%3E)

Below is another example VBA code, where I have used a variable (‘Var’) to hold the text string. The UCase function is then used to convert it the lower case characters into uppercase.

Sub UCaseExample2()
Dim Var As String
Var = "Good Morning"
MsgBox UCase(Var)
End Sub

Another example below shows how to take the string from a cell (A1) and show the uppercase text of it in a message box.

Sub UCaseExample3()
MsgBox UCase(Range("A1"))
End Sub

While all these above examples work, you’re unlikely to use this function to simply convert or show the uppercase string.

Below is a **more practical example** of the UCase function in Excel VBA.

The below code would go through all the cells in the selected range and convert all the text strings into upper case.

Sub UCaseExample4()
Dim rng As Range
Set rng = Selection
For Each Cell In rng
Cell.Value = UCase(Cell)
Next Cell
End Sub

![Using UCase function in VBA to convert to uppercase](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20324'%3E%3C/svg%3E)

Here are a few important things to know about the VBA UCase function:

1.  It affects only the lowercase characters of the text string. Any character other than the lowercase text characters is left unchanged. This means that numbers, special characters, and punctuations remain unchanged.
2.  If you use a null character (or a reference to an empty cell), it will return a null character.

**Other Useful Excel VBA Functions:**

*   [VBA LCase Function](https://trumpexcel.com/vba-lcase/)
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

3 thoughts on “VBA UCASE Function – Convert Text to Upper Case in Excel”
------------------------------------------------------------------------

1.  Thank you 🙂
    
    [Reply](https://trumpexcel.com/vba-ucase/#comment-13375)
    
2.  hi  
    want to learn vba from beginning
    
    [Reply](https://trumpexcel.com/vba-ucase/#comment-12258)
    
3.  Good  
    very helpful
    
    [Reply](https://trumpexcel.com/vba-ucase/#comment-11638)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-ucase/#respond)

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