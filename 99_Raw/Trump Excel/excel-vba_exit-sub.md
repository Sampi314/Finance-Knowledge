# VBA Exit Sub Statement - Easy Explanation!

**Source:** https://trumpexcel.com/excel-vba/exit-sub

---

[Skip to content](https://trumpexcel.com/excel-vba/exit-sub/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/exit-sub/#below-title)

Exit Sub statement in VBA allows you to exit a subroutine at any point in the code.

As soon as your VBA code encounters an _Exit Sub_ statement, it stops executing the rest of the code and brings it out of that subroutine.

In this article, I’ll tell you everything you need to know about the _Exit Sub_ statement and how to use it the right way in your VBA code.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/exit-sub/#)

Using Exit Sub Statement in VBA
-------------------------------

To use the Exit Sub statement in VBA, simply enter the text Exit Sub in a new line in the code.

Below is an example:

    Sub CheckInput()
        
        Dim inputValue As Integer
        inputValue = InputBox("Enter a number")
        
        If inputValue < 0 Then
            MsgBox "Negative numbers are not allowed!"
            Exit Sub ' Exit sub if number is negative
        End If
        
        MsgBox "You entered: " & inputValue
        
    End Sub

In the above code, I use an input box to ask the user for a number, and if the number is negative, Exit Sub is used to exit the subroutine.

While this is a very basic example, it gives you an idea that you can use Exit Sub with [If conditions](https://trumpexcel.com/if-then-else-vba/)
 or [Loops](https://trumpexcel.com/vba-loops/)
 to make your code more efficient.

Note: If you want to use the Exit Sub functionality within a Function, you need to use _Exit Function_ instead

Error Handling with Exit Sub in VBA
-----------------------------------

Exit Sub can be a useful tool for [error-handling in your VBA codes](https://trumpexcel.com/vba-error-handling/)
.

You can use it in combination with _On Error_ statements, where, as soon as your code encounters an error, it would be taken to the On Error statement, which can then be used to exit the subroutine.

    Sub ErrorHandling()
        
        On Error GoTo ErrorHandler
        
        ' Your code goes here
    
        Exit Sub
    
    ErrorHandler:
        
        ' Handling the error
        MsgBox "An error occurred: " & Err.Description
      
    End Sub

In the above VBA code, I have the _On Error GoTo ErrorHandler_ statement followed by the code that I want to execute.

If the code runs without any error, Exit Sub is used to then exit from that subroutine. If there is an error, the code jumps to the ErrorHandler procedure and shows a message box.

Early Termination of Code with Exit Sub
---------------------------------------

Using Exit Sub can improve the performance of your code as it allows you to exit a subroutine if a specific condition is met.

Below is an example where _Exit Sub_ allows us to exit the subroutine when a specific criterion is met, saving us time and processing that would otherwise have been used in going through the entire code:

    Sub FindFirstNegativeCell()
        Dim cell As Range
        For Each cell In ActiveSheet.UsedRange
            If cell.Value < 0 Then
                MsgBox "First negative value found in cell " & cell.Address
                Exit Sub
            End If
        Next cell
        MsgBox "No negative values found."
    End Sub

The above code is used to find the first negative value in a range of cells and it uses Exit Sub to exit the code as soon as it finds the first negative value.

Exit Sub vs End Sub
-------------------

While both Exit Sub and End Sub can be used to exit the subroutine, they are not the same.

Here are the differences:

| EXIT SUB | END SUB |
| --- | --- |
| Immediately exits the current subroutine | It can be used anywhere within the subroutine body |
| Can be used anywhere within the subroutine body | Always placed at the very end of the subroutine |
| Allows for conditional early termination of the subroutine | Execution reaches this point naturally if no Exit Sub is encountered |
| Can appear multiple times in the same subroutine | Appears in a subroutine only once |

Exit Sub provides flexibility in controlling when a subroutine terminates, whereas End Sub is a required element that defines the end of the subroutine.

In this article, I covered everything you need to know about the VBA Exit Sub statement. I hope this article was useful.

**Other Excel articles you may also like:**

*   [Learn All About Excel VBA](https://trumpexcel.com/excel-vba/)
    
*   [Excel VBA MsgBox \[Message Box\] – All You Need to Know!](https://trumpexcel.com/vba-msgbox/)
    
*   [Create New Sheet Using VBA in Excel (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    
*   [Rename Files Using VBA](https://trumpexcel.com/excel-vba/rename-files/)
    
*   [Comments in Excel VBA (Add, Remove, Block Commenting)](https://trumpexcel.com/comments-excel-vba/)
    
*   [Excel VBA Select Case Statement](https://trumpexcel.com/vba-select-case/)
    
*   [Make VBA Code Pause or Delay (Using Sleep / Wait Commands)](https://trumpexcel.com/vba-sleep-wait/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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