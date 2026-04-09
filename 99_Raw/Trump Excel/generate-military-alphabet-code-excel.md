# Generate Military Alphabet Code for a Text in Excel

**Source:** https://trumpexcel.com/generate-military-alphabet-code-excel

---

[Skip to content](https://trumpexcel.com/generate-military-alphabet-code-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/generate-military-alphabet-code-excel/#below-title)

‘A’ as in Alpha, ‘B’ as in Bravo, ‘C’ as in Charlie. Heard these phrases before?

These are called the [Military Alphabet Code](http://www.militaryfactory.com/military_alphabet_code.asp)
 (also known as [NATO alphabet code](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)
). It is often used by people (especially the call center guys) to communicate the name, email address or the home/office address.

Generate Military Alphabet Code in Excel
----------------------------------------

In my first job, I got a project where I had to do cold calling to get some information on medical devices.

Since we were connecting with people from all over the world with all kinds of accents, it was – at times – difficult to share our name and email or get theirs.

It was then that I started relying on military alphabet codes to communicate clearly. I have seen a lot of call center guys do this effectively.

With this in mind, I have created an [Excel Template](https://trumpexcel.com/free-excel-templates/)
 where you can enter a text string, and it will automatically generate the Military Alphabet code for the entered text.

Something as shown below:

![Generate Military Alphabet Code in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20196'%3E%3C/svg%3E)

As soon as you enter the text and hit Enter, it will automatically generate the military alphabet code for each alphabet in the text string.

Note that in this case, numbers and special characters would be shown as is. Also, this would work with either case – lower or upper.

_**Download the Military Alphabet Code Generator Template**  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/malfqpuhzmp1d4j/Military-Code.xlsm?dl=1)
_

Since this workbook contains a macro, as soon as you open it, you might see a yellow bar with the button – Enable Content. You need to click on this button for this to work.![Generate Military Alphabet Code in Excel - Enable Content](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%2034'%3E%3C/svg%3E)

#### How to Create this Military Alphabet Code Generator Template

This template works purely on VBA magic. There a [couple of loops](https://trumpexcel.com/vba-loops/)
 within the Worksheet Change event procedure that simply checks for each alphabet, and fetch the code word for that alphabet.

Here is the VBA code that does the work:

Private Sub Worksheet\_Change(ByVal Target As Range)
'created by Sumit Bansal of trumpexcel.com
Dim alphabetcount As Integer
Dim alphabet As String
Dim result As String
Dim i As Integer
Dim TargetColumn As Integer
Dim TargetRow As Integer
On Error Resume Next
TargetColumn = Target.Column
TargetRow = Target.Row

If TargetColumn = 4 And Cells(TargetRow, TargetColumn) = "" Then
Cells(TargetRow, TargetColumn + 1) = ""
Exit Sub
End If

If TargetColumn = 4 Then
alphabetcount = Len(Cells(TargetRow, TargetColumn))
For i = 1 To alphabetcount + 1
alphabet = Mid(Range(Target.Address), i, 1)
If Range("A2:A27").Find(alphabet) Is Nothing Then
result = result & ", " & alphabet
Else
result = result & ", " & Range("A2:A27").Find(alphabet).Offset(0, 1)
End If
Next i
Cells(TargetRow, TargetColumn + 1) = Mid(result, 3, Len(result) - 4)
End If
End Sub

If you’d like to change a couple of these code words to suit your audience/region, you can simply change it in column B in the [download file](https://www.dropbox.com/s/malfqpuhzmp1d4j/Military-Code.xlsm?dl=1)
. The code would automatically pick the changed codes.

Note that since this workbook contains a macro, you need to save the file in .xls or .xlsm format.

I hope this would help you the next time you try and communicate names, email ids, or address with people over a telephonic conversation.

Do let me know what you think of this [Excel Template](https://trumpexcel.com/free-excel-templates/)
 by leaving a comment below.

**Other Excel Templates You Might Like:**

*   [Task Prioritization Matrix Template](https://trumpexcel.com/free-excel-templates-excel-list/)
    .
*   [Email Generator Template](https://trumpexcel.com/send-email-from-excel-hyperlink/)
    .
*   [How to Create QR Codes in Excel (QR Code Generator)](https://trumpexcel.com/create-qr-codes-excel/)
    
*   [Employee Leave Tracker Template](https://trumpexcel.com/excel-leave-tracker/)
    .
*   [Employee Timesheet Calculator Template](https://trumpexcel.com/excel-timesheet-calculator-template/)
    .
*   [Calendar Integrated with a To-Do-List Template](https://trumpexcel.com/calendar-to-do-list-template/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Quickly Generate Military Alphabet Code for a Word in Excel”
---------------------------------------------------------------------------

1.  hi sumit
    
    please share me this Generate Military Alphabet Code in Excel i can’t download
    
    [Reply](https://trumpexcel.com/generate-military-alphabet-code-excel/#comment-11553)
    
2.  i downloaded the excel template and i want to see inside this the VBA code,how can i do it? or is locked?
    
    [Reply](https://trumpexcel.com/generate-military-alphabet-code-excel/#comment-10431)
    
3.  You spelled “Alfa” incorrectly. It should be “Alpha”.
    
    [Reply](https://trumpexcel.com/generate-military-alphabet-code-excel/#comment-9376)
    
4.  Printable military alphabet charts here [http://militaryalphabet.net](http://militaryalphabet.net/)
    
    [Reply](https://trumpexcel.com/generate-military-alphabet-code-excel/#comment-3485)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/generate-military-alphabet-code-excel/#respond)

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