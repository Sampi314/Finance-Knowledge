# Run Time Error 9 (Subscript Out of Range) - How to Fix!

**Source:** https://trumpexcel.com/excel-vba/run-time-error-9

---

[Skip to content](https://trumpexcel.com/excel-vba/run-time-error-9/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/run-time-error-9/#below-title)

Run Time Error 9, also known as “Subscript Out of Range,” is a common issue that Excel users may encounter while working with VBA in Excel.

This error typically occurs when you’re trying to access an array element, range, worksheet/workbook that doesn’t exist.

In this article, I will cover the most common reasons that lead to _Run Time Error 9 (Subscript Out of Range)_ and how to fix them.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/run-time-error-9/#)

Referring to Non-Existent Worksheet
-----------------------------------

If you try to refer to a worksheet that does not exist, VBA will show you the runtime error 9.

Below is a simple VBA code where I am trying to activate a sheet named Example. If this gives me a runtime error 9, this would indicate that either the sheet does not exist or I have misspelled the sheet name.

    Sub NonExistentWorksheet()
        ' This will cause an error if there's no Example Sheet
        Sheets("Example").Activate
    End Sub

When you’re working with the longer VBA code, and you get this error, you can click on the Debug button, and it’ll take you to the exact line in the code that is causing that error.

### **How to Fix This**

*   Check for worksheet’s existence before [running the code](https://trumpexcel.com/run-a-macro-excel/)
    . You can also Use _Worksheets.Count_ property to iterate through all sheets. Compare each sheet’s name with the target sheet name. Only activate the sheet if it exists.
*   Use [error handling](https://trumpexcel.com/vba-error-handling/)
     to manage missing sheets. Implement On Error Resume Next before the activation code. Check _Err.Number_ after the activation attempt. Take appropriate action if an error occurs.
*   Consider creating the sheet if it doesn’t exist. Add code to create the “Example” sheet if it’s not found. This ensures your code works even if the sheet was accidentally deleted.
*   Double-check sheet name spelling. Verify the exact spelling of the sheet name in your workbook. VBA is case-sensitive, so ensure the case matches exactly.
*   Use a variable to store the sheet name. Define the sheet name as a variable at the beginning of your code. Use this variable throughout your code to avoid typos.

Referring to a Closed Workbook
------------------------------

If you refer to a closed workbook through your VBA code, you’ll also end up getting the runtime error 9.

This is because the VBA code cannot do anything with a closed workbook. So you either need to have that workbook already open or you need to first have a few lines in your code that open that workbook and then execute the rest.

Below is the VBA code where I want to enter my name in cell A1 in the Example.xlsx workbook.

    Sub ClosedWorkbookError()
        ' This will cause an error if the workbook is not open
        Workbooks("Example.xlsx").Sheets(1).Range("A1").Value = "Sumit Bansal"
    End Sub

If the workbook is already open, this code will execute perfectly, but if the workbook is not open, then I will get the _Run Time Error 9 (Subscript Out of Range)_ error.

### How to Fix?

*   Check if the workbook is open before accessing it. Use the Workbooks collection to see if the workbook is already open. If it’s not, open it before proceeding with your code.
*   Open the workbook at the beginning of your code: If you know you’ll need the workbook, open it explicitly at the start of your procedure. This avoids potential errors later in the code.
*   Use a separate function to get or open the workbook: Create a helper function that checks for the workbook, opens it if necessary, and returns a reference to it. This centralizes the logic and makes your main code cleaner.
*   Use error handling to manage closed workbooks. Implement _On Error Resume Next_ before accessing the workbook. Check _Err.Number_ after the attempt. If an error occurs, open the workbook and retry the operation.
*   Specify the full path of the workbook: Instead of just the filename, use the complete file path. This ensures VBA can locate and open the file if it’s closed.

Referring to Non-Existent Workbook (or Misspelling the Workbook Name)
---------------------------------------------------------------------

Another common reason you may end up getting this error is when you’re trying to refer to a verb that either does not exist, or you have misspelled the name of the workbook.

Below is an example code where I’m trying to enter my name in cell A1 in an open workbook called Example.xlsx. But since I’ve misspelled the book name, it shows me the runtime error 9.

    Sub MisspelledWorkbookError()
        ' This will cause an error if the workbook name is misspelled
        Workbooks("Exampl.xlsx").Sheets(1).Range("A1").Value = "Sumit Bansal"
    End Sub

### How to Fix?

*   Before trying to access the workbook, loop through the Workbooks collection to check if a workbook with the specified name exists. This can help identify misspellings.
*   Define workbook names at the beginning of your module or in a separate configuration file. This centralizes name management and reduces the chance of typos in your code.
*   If you’re unsure about the exact spelling, use the Like operator with [wildcards](https://trumpexcel.com/excel-wildcard-characters/)
     to find workbooks with similar names.
*   Use error handling to catch misspelled workbook names. Implement On Error Resume Next before accessing the workbook.
*   If the workbook isn’t found, show the user a list of currently open workbooks. This can help identify if the desired workbook is open under a different name.

Undimensioned Array Error
-------------------------

When working with dynamic arrays in VBA, we need to define the size of that array.

If I don’t specify the size of the array and then try to assign a value to it, it will give me runtime error 9.

Let me explain with an example:

    Sub UninitializedExample()
        Dim myArray() As Integer
        
        ' This will cause Error 9
        myArray(0) = 10  ' Array hasn't been sized yet
    
    End Sub

In the above code, I have myArray(), but I have not specified its dimension when I have initialized it with the statement – _Dim myArray() As Integer_

Now, when I use _myArray(0) = 10_, VBA has no idea how many elements the array can hold, and hence, it shows me the runtime error.

### How to Fix?

*   Use the ReDim statement to set the size of the array before assigning values to it. This allocates the necessary memory for the array.
*   If you need to change the size of the array later in your code, use ReDim Preserve to resize it without losing existing data.
*   For truly dynamic data structures, consider using Collection or Dictionary objects instead of arrays. These can grow and shrink without explicit resizing.
*   Use On Error statements to catch potential array-related errors and handle them gracefully.
*   Use Option Base to set the default lower bound: If you consistently use 0-based or 1-based arrays, set Option Base at the top of your module to establish a default lower bound for all arrays.

Accessing Out of Bound Array Index
----------------------------------

Another dynamic array-related situation that can lead to runtime error 9 is when you try to access the element of an array which has not been initialized.

Below, I have a VBA code where I have an array called myArray, and it is initialized to have three elements. Now, when I use myArray(4), it has no idea what to refer to, and it shows an error.

    Sub ArrayOutOfBounds()
        Dim myArray(1 To 3) As Integer
        myArray(1) = 10
        myArray(2) = 20
        myArray(3) = 30
        ' This will cause a Subscript Out of Range error
        Debug.Print myArray(4)
    End Sub

### How to Fix?

*   Check array bounds before accessing elements. Use the LBound and UBound functions to determine the lower and upper bounds of the array. Verify that the index you’re trying to access falls within these bounds.
*   Use error handling (of course)
*   If you need to access elements beyond the current array size, use ReDim Preserve to expand the array before accessing the new elements.
*   If your data structure needs frequent resizing, consider using a Collection or Dictionary object instead of an array, as these can grow dynamically without explicit bounds checking.
*   Create a separate function that checks if an index is within the array’s bounds. Use this function before accessing array elements to prevent out-of-bounds errors.

**Other Excel articles you may also like:**

*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [Using VBA FileSystemObject (FSO) in Excel](https://trumpexcel.com/vba-filesystemobject/)
    
*   [Check If Workbook Is Open Using VBA](https://trumpexcel.com/excel-vba/check-if-workbook-open/)
    
*   [Check IF Sheet Exists Using VBA in Excel](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    

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