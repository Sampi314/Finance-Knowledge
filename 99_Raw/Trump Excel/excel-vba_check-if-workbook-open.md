# Check If Workbook Is Open Using VBA in Excel

**Source:** https://trumpexcel.com/excel-vba/check-if-workbook-open

---

[Skip to content](https://trumpexcel.com/excel-vba/check-if-workbook-open/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/check-if-workbook-open/#below-title)

Sometimes, when working with VBA code, you may want to check whether a workbook is open or not.

For example, if you plan on using a workbook in your VBA code later, you may want to first quickly run a check to ensure that the work is already open.

There are a couple of simple methods I’ll show you in this article that you can use to quickly check whether a book is open or not using VBA.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/check-if-workbook-open/#)

Loop Through the Workbooks Collection to Check If Workbook Is Open
------------------------------------------------------------------

One of the easiest ways to check if a workbook is open or not is to go through all the workbooks and check their names.

If any of the open workbooks’ names match the one that you’re looking for, it means that the workbook is open. Else, it’s closed.

Let’s say that I want to check whether the workbook Annual Budget.xlsx is open or not.

I can do this using the below VBA code:

    Sub LoopCheckIfWorkbookOpen()
    Dim wb As Workbook
    Dim wbName As String
    Dim wbOpen As Boolean
    wbName = "Annual Budget.xlsx"
    wbOpen = False
    For Each wb In Workbooks
    If wb.Name = wbName Then
        wbOpen = True
        wb.Activate
        MsgBox "The workbook """ & wbName & """ is open."
        Exit For
    End If
    Next wb
    If Not wbOpen Then
        MsgBox "The workbook """ & wbName & """ is not open."
    End If
    End Sub

When you run the code and the workbook ‘Annual Budget.xlsx’ is open, the code will activate the workbook and [display a message box](https://trumpexcel.com/vba-msgbox/)
 indicating that the workbook is open:

![VBA message box when the workbook is already open](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20272%20133'%3E%3C/svg%3E)

If the workbook is not open, the code shows a message box indicating that the workbook is not open:

![VBA message box when the workbook is not open](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20293%20133'%3E%3C/svg%3E)

### Explanation of the Code

The example code loops through the [‘Workbooks’ collection](https://trumpexcel.com/vba-workbook/)
 (that is a collection of all the open workbooks) and compares the name ‘Annual Budget.xlsx’ with the names of the open workbooks.

If there is a match, it activates the ‘Annual Budget.xlsx’ workbook, displays a message box indicating that the workbook is open, and exits the code.

On the other hand, if there is no match, it displays a message box indicating that the workbook is not open.

Note: Instead of hardcoding the name of the workbook you want to check, you can prompt the user to enter it using the ‘InputBox’ function. To implement this, replace the statement _wbName = “Annual Budget.xlsx”_ with _wbName = InputBox (“Enter the Workbook’s Name:”)_.

Also read: [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)

Using Error Handling to Check If Workbook Is Open
-------------------------------------------------

Another way to check whether the book book is open or not is by trying to set a variable (say wb) to the workbook.

This would only work if the workbook is already open, and if it is not, it would result in an error.

So if we get an error, we know that the workbook is not open, and if we don’t get an error, then we can safely assume that the workbook is open

Below is an example code that tries to check whether the workbook ‘Annual Budget.xlsm’ is open or not.

    Sub ErrorHandlingCheckIfWorkbookOpen()
    Dim wbName As String
    Dim wb As Workbook
    wbName = "Annual Budget.xlsm"
    On Error Resume Next
    Set wb = Workbooks(wbName)
    On Error GoTo 0
    If Not wb Is Nothing Then
        MsgBox wbName & " is open."
    Else
        MsgBox wbName & " is not open."
    End If
    End Sub

When you execute the code and the workbook ‘Annual Budget.xlsm’ is open, the code will display a message box indicating that the workbook is open:

![VBA Msgbox when workbook is open](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20133'%3E%3C/svg%3E)

If the workbook is not open, the code will display a message box stating it is not open.

Note: A regular workbook has a .xlsx extension, and a macro-enabled one has a .xlsm extension. If you are uncertain whether the workbook you want to check is open and has macros enabled, you can use the asterisk (\*) [wildcard character](https://trumpexcel.com/excel-wildcard-characters/)
 in the file extension. For example, in this case, you can assign “Annual Budget.xls\*” to the ‘wbName’ variable. An asterisk character (\*) represents any number of characters, so as long as the workbook extension has .xls, this would work.

### Explanation of the Code

The code attempts to reference the workbook you are checking by assigning it to an object variable.

An error occurs if the workbook is not open and the code displays an appropriate message. If the workbook is open, no error occurs, and the code displays a message box stating that the workbook is open.

Note: The subroutine does not use [looping](https://trumpexcel.com/vba-loops/)
, so it is slightly more efficient than the code in Method #1.

Also read: [VBA Check IF Cell is Empty (ISEMPTY Function)](https://trumpexcel.com/excel-vba/check-if-cell-empty/)

Using a User-Defined Function (UDF) to Check If the Workbook Is Open
--------------------------------------------------------------------

You can [create a UDF (User Defined Function) in VBA](https://trumpexcel.com/user-defined-function-vba/)
 and call it in a subroutine to check if a workbook is open.

Suppose you want to check if the workbook ‘Annual Budget.xlsx’ is open.

You can use the following code that calls a UDF to get this done:

    Sub UDFCheckIfWorkbookOpen()
    Dim wbName As String
    wbName = "Annual Budget.xlsx"
    If CheckIfWorkbookOpen(wbName) Then
        MsgBox wbName & " is open."
    Else
        MsgBox wbName & " is not open."
    End If
    End Sub
    
    Function CheckIfWorkbookOpen(wbName As String) As Boolean
    Dim wb As Workbook
    For Each wb In Workbooks
        If wb.Name = fileName Then
            CheckIfWorkbookIsOpen = True
            Exit Function
        End If
    Next wb
    CheckIfWorkbookIsOpen = False
    End Function

When you execute the ‘UDFCheckIfWorkbookOpen’ subroutine, it calls the ‘IsWorkbookOpen’ function and checks whether the ‘Annual Budget.xlsx’ workbook is open.

*   If the workbook is open, the subroutine displays a message box stating that the workbook is open.

![VBA Msgbox that workbook is open](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20187%20133'%3E%3C/svg%3E)

*   If the workbook is not open, the code displays a message box indicating that the workbook is not open.

### Explanation of the Code

The ‘IsWorkbookOpen’ UDF takes a workbook name as input and iterates through all open workbooks using a For Each loop, checking each workbook’s name against the specified workbook name.

If it finds a match, the UDF returns ‘True’ and exits the loop. If it does not find a match, the UDF returns ‘False.’

Using UDF to Check If the Workbook Is Already Open at a Specific Path
---------------------------------------------------------------------

You can use a User-Defined Function (UDF) to check whether another user has opened a workbook at a specific path.

Suppose you want to check if the workbook ‘\\\\Server1\\Reports\\Annual Budget.xlsx’ is already opened by another user.

You can use the following code to perform the task:

    Sub CheckWorkbookOpenAtPath()
    Dim Result As Boolean
    Result = CheckWorkbookOpenByPath("\\Server1\Reports\Annual Budget.xlsx")
        If Result = True Then
            MsgBox "Workbook is open."
        Else
            MsgBox "Workbook is not open."
        End If
    End Sub
    
    Function CheckWorkbookOpenByPath(FileName As String)
    Dim filenumber As Long, errorNumber As Long
    On Error Resume Next
    filenumber = FreeFile()
    Open FileName For Input Lock Read As #filenumber
    Close filenumber
    errorNumber = Err
    On Error GoTo 0
    Select Case errorNumber
    Case 0: CheckWorkbookOpenByPath = False
    Case 70: CheckWorkbookOpenByPath = True
    Case Else: Error errorNumber
    End Select
    End Function

When you execute the code and the ‘Annual Budget.xlsx’ workbook is open at the specified path, the code displays a message box stating that the workbook is open.

If the workbook is not open, the code returns a message box indicating that the workbook is not open.

### Explanation of the Code 

The code attempts to open the ‘Annual Budget.xlsx’ workbook at the specified path in exclusive mode for input.

If another user has not opened the workbook, the error code 0 occurs. If another user has opened the workbook, a permission-related error code 70 occurs.

The logic behind this code is that if another user has already opened the target workbook, you will encounter a permission-related error if you attempt to open it for input in exclusive mode.

Display the Names of All Open Workbooks 
----------------------------------------

In situations where you want to perform an operation across multiple workbooks, you may need to ascertain which workbooks are open.

You can use the code below to print the names of the workbooks in the ‘Workbooks’ collection to the Immediate window:

    Sub DisplayNamesOpenWorkbooks()
    Dim wb As Workbook
    For Each wb In Workbooks
        Debug.Print wb.Name
    Next wb
    End Sub

When you execute the code, it prints the names of the workbooks that are currently open to the Immediate window:

![List of all the workbook names that are open](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20365%20130'%3E%3C/svg%3E)

Note: If the Immediate window is closed, you can open it by pressing CTRL + G.

### Explanation of the Code

The code iterates through each workbook in the collection of open workbooks using a [‘For Each Next’ loop](https://trumpexcel.com/for-next-loop-excel-vba/)
, and for each workbook, it prints the workbook’s name in the [Immediate window](https://trumpexcel.com/vba-immediate-window/)
.

In this article, I’ve covered five examples where I’ve used simple VBA codes to check whether a workbook is open or not using VBA.

I hope you found this article helpful.

If you have any questions or you have any other idea about how a workbook is open or not can be checked using VBA, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [Split Each Excel Sheet Into Separate Files](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/)
    
*   [How to Open Excel Files Using VBA (Examples)](https://trumpexcel.com/open-excel-files-using-vba/)
    
*   [How to Automatically Open Specific Excel File on Startup](https://trumpexcel.com/automatically-open-excel-file-startup/)
    

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