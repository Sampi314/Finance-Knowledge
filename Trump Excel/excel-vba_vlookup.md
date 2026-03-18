# Using VLOOKUP in VBA (Examples)

**Source:** https://trumpexcel.com/excel-vba/vlookup

---

[Skip to content](https://trumpexcel.com/excel-vba/vlookup/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/vlookup/#below-title)

VLOOKUP is one of the most used functions in Excel, and you can also use it easily in VBA as well.

VBA does not have a separate VLOOKUP function, so to use VLOOKUP in a VBA code, you need to use the same VLOOKUP function that you use in he worksheet.

In this article, I will show you how to use VLOOKUP in VBA and some examples of using it in different scenarios.

Let’s get into it!

Using VLOOKUP in VBA

[Toggle](https://trumpexcel.com/excel-vba/vlookup/#)

VBA VLOOKUP Syntax
------------------

Below is the wheel lookup syntax in VBA.

Application.VLOOKUP(lookup\_value, table\_array, column\_index, range\_lookup)

As you might have already noticed, the syntax of the VLOOKUP function looks exactly the same as that you use in the worksheet.

That is because when using VLOOKUP in VBA, we are referring to the same VLOOKUP function that you already know.

Using VLOOKUP in VBA (Examples)
-------------------------------

Now, let’s see a couple of examples of using VLOOKUP in VBA.

### Fetch a Value Using VLOOKUP in VBA

Below, I have a data set where I have student names in column A and their scores in column B, and I want to fetch their scores of Brandon.

![Dataset of student's scores for VLOOKUP in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20477'%3E%3C/svg%3E)

Here is the VBA code that will do that and show me Brandon’s score in a [message box](https://trumpexcel.com/vba-msgbox/)
.

    Sub GetScore()
    
        score = Application.VLookup("Brandon", Range("A2:B16"), 2, False)
    
        If IsError(score) Then
            MsgBox "Brandon's score not found."
        Else
            MsgBox "Brandon's score: " & score
        End If
    
    End Sub

The above code uses the [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
 to go through the leftmost column in the specified range (A2:B16), look for the name ‘Brandon’, and when it finds the name, show us the score in a message box.

In case the code is not able to find the name in column A, it will show the message “Brandon’s score not found.”

If you want the VB code to prompt the user to enter the name to look for, and then get its score, you can use the below code:

    Sub GetScoreUsingVLOOKUP()
    
        Dim studentName As String
        Dim score As Variant
    
        ' Ask the user to enter the student's name
        studentName = InputBox("Enter the student's name:", "Student Name")
    
        ' Check if the user entered a name
        If studentName <> "" Then
            ' Perform VLOOKUP with the entered name
            score = Application.VLookup(studentName, Range("A2:B16"), 2, False)
    
            ' Check if the score is found and display a message
            If IsError(score) Then
                MsgBox "Score not found for " & studentName & "."
            Else
                MsgBox studentName & "'s score: " & score
            End If
        Else
            MsgBox "No name entered."
        End If
    End Sub

In the VBA codes shown above, I have hard-coded the range that has the data. You can also use a [named range](https://trumpexcel.com/named-ranges-in-excel/)
 instead of the range reference.

### VLOOKUP From Another Sheet Using VBA

You can also use VLOOKUP to go through the data in another sheet and then give us the result.

Below I have a data set of students names in column A and their scores in column B in a sheet named ‘Scores’.

![Dataset of student's scores for VLOOKUP in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20477'%3E%3C/svg%3E)

And I have the following table with some student names in column A in a separate sheet named ‘Result’.

![Dataset to fetch values using VBA VLOOKUP from another sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20215'%3E%3C/svg%3E)

I want to use VBA VLOOKUP to fetch the results sheet by going through the data in the scores sheet.

Below is the code that will do this:

    Sub VLOOKUPAnotherSheet()
    
        
        For Each cell In Range("A2:A5")
        cell.Offset(0, 1) = Application.VLookup(cell, Sheets("Scores").Range("A2:B16"), 2, False)
        Next
    
    End Sub

The above code goes through each cell in the range A2:A5 in the active sheet (which is the Result sheet), and uses the name in the cell as the look up value.

It then goes to the Scores sheet and scans the names in A2:A16. When it finds the name, it fetches the score from column B and then puts that score next to the name in the Result sheet.

In case it doesn’t find the score for a given name, it would return the #N/A error.

Also read: [VBA Check IF Cell is Empty (ISEMPTY Function)](https://trumpexcel.com/excel-vba/check-if-cell-empty/)

### VLOOKUP From Another Workbook Using VBA

You can also use the VLOOKUP function in VBA to refer to another workbook and fetch the value from there.

Below, I have a data set of students’ names in column A and their scores in column B. This data is in a workbook named Scores.xlsx and the sheet named ‘Data’.

![Dataset of student's scores for VLOOKUP in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20477'%3E%3C/svg%3E)

And I have the below dataset in another workbook:

![Dataset to fetch values using VBA VLOOKUP from another workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20215'%3E%3C/svg%3E)

Now, I want to use VLOOKUP to go through the names in the Scores.xlsx workbook, fetch the scores for each name, and put it in the adjacent cell.

Here is the VBA code that will do this:

    Sub VLOOKUPAnotherWorkbook()
        Dim cell As Range
        
        For Each cell In Range("A2:A5")
        cell.Offset(0, 1) = Application.VLookup(cell, Workbooks("Scores.xlsx").Sheets("Data").Range("A2:B16"), 2, False)
        Next
    
    End Sub

The above code goes through each cell in the range A2:A5 in the active sheet.

For each name in this range, it does a VLOOKUP by going to the Scores.xlsx workbook and looking for the names in the A1:A16 range in the Data worksheet.

When it finds the name, it returns the score for that name back in column B in the active sheet.

Note: For this code to work, it is necessary that the other worksheet from which you are getting the value using Vlooku is open. If that workbook is not open, you will get a Runtime error in the code.

### VLOOKUP From Another Closed Workbook Using VBA

If you want to use VLOOKUP to get the values from a closed workbook, you need to first open the workbook using your code and then go through the data from it using a Vlookup function.

The result that you then find in this workbook would then be written back into the active sheet.

Let me explain with an example.

Below, I have a data set in a sheet named ‘Result,’ where I have some names in column A, and I want to get their scores from a closed workbook named Scores.xlsx. In this closed workbook, the scores are provided in a table in the sheet named ‘Data’.

![Get values using VBA VLOOKUP from another closed workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20215'%3E%3C/svg%3E)

Here is the code that will work in this case:

    Sub VLOOKUPAnotherWorkbook()
    
        Dim cell As Range
        Dim wb As Workbook
        Dim ws As Worksheet
        Dim result As Variant
        Dim workbookIsOpen As Boolean
    
        ' Check if Scores.xlsx is already open
        workbookIsOpen = False
        For Each wb In Workbooks
            If wb.Name = "Scores.xlsx" Then
                workbookIsOpen = True
                Exit For
            End If
        Next wb
    
        ' Open Scores.xlsx if it's not already open
        If Not workbookIsOpen Then
            Set wb = Workbooks.Open("C:\Users\sumit\Downloads\Scores.xlsx")
        Else
            Set wb = Workbooks("Scores.xlsx")
        End If
    
        Set ws = wb.Sheets("Data")
    
        ' Loop through cells and apply VLOOKUP
        For Each cell In ThisWorkbook.Sheets("Result").Range("A2:A5")
            result = Application.VLookup(cell.Value, ws.Range("A2:B16"), 2, False)
    
            ' Check if VLOOKUP returned an error
            If IsError(result) Then
                cell.Offset(0, 1).Value = "Not Found" ' Or any other default value
            Else
                cell.Offset(0, 1).Value = result
            End If
        Next cell
    
        ' Close the workbook if it was not open before
        If Not workbookIsOpen Then
            wb.Close SaveChanges:=False
        End If
    
    End Sub

The above VBA macro code loops through a range of cells in the “Result” sheet of the current workbook and performs a VLOOKUP in the “Data” sheet of “Scores.xlsx”.

The results are written next to the original cells. If no match is found, “Not Found” is written.

It also handles the opening and closing of “Scores.xlsx” intelligently, ensuring it only closes the workbook if it wasn’t already open when the macro began.

Also read: [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)

Error handling When Using VLOOKUP in VBA
----------------------------------------

Here are a few tips to handle errors when using Vlookup in VBA in Excel.

### Using ISERROR

You can use the ISERROR function in VBA to check whether VLOOKUP has returned an error or not, and in case it has returned an error, then handle it.

Below is an example code on handling errors given by VLOOKUP in VBA:

    Sub VLOOKUPError()
    
    Dim result As Variant
    
    result = Application.VLookup(lookupValue, tableArray, colIndex, False)
    
    If IsError(result) Then
        result = "Not Available"  ' Set to your default value
    End If
    
    End Sub 

The above code uses a variable _result_ to store the result of the VLOOKUP formula.

It then uses an IF statement to check the value of IsError(result). If IsError(result) is True, which means that VLOOKUP has returned an error, it will execute the lines of codes in the IF condition (which is to set the value of the result as ‘Not Available’)

Also read: [Error Handling in VBA](https://trumpexcel.com/vba-error-handling/)

### Using On Error Resume Next

Another way you can handle errors given by VLOOKUP function is by using On Error Resume Next.

When we add this line to our code, it ignores any errors it encounters and moves on to executing the next line of code.

This can be used if you expect some errors to happen and do not want the code to stop because of them. However, It’s important to use this with caution as it can make debugging difficult by ignoring all errors.

In this article, I showed you how to use the VLOOKUP function in VBA in Excel using some examples.

If you have any feedback or suggestions for me, do let me know in the comments section.

**Other Excel VBA articles you may also like:**

*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [VBA Protect and Unprotect Sheets](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)
    
*   [VBA Count Sheets](https://trumpexcel.com/count-sheets-excel/)
    

**Other Excel articles you may also like:**

*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    
*   [How to make VLOOKUP Case Sensitive](https://trumpexcel.com/vlookup-case-sensitive/)
    
*   [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    
*   [VLOOKUP Vs. INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [Lookup the Second, the Third, or the Nth Value in Excel](https://trumpexcel.com/lookup-second-value/)
    

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