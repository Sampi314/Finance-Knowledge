# What is VBA in Excel? Learn Excel VBA Programming!

**Source:** https://trumpexcel.com/excel-vba

---

[Skip to content](https://trumpexcel.com/excel-vba/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/#below-title)

Do you know you can easily automate a lot of tasks in Excel? Imagine tasks that were taking minutes and even hours getting done with a single click.

**Excel VBA can make that happen.**

Visual Basic for Applications (VBA) is the programming language in Excel that can help you automate tasks, create your own functions (pretty cool), and even create applications.

If the world of VBA is new to you, don’t worry.

VBA is pretty easy to learn.

In this article, I will take you on a journey to explore the world of VBA. Give you all the VBA basics you need to know, and even tell you the best ways to learn VBA (absolutely free).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/#)

What is VBA in Excel?
---------------------

VBA stands for **Visual Basic for Applications**.

It is a programming language developed by Microsoft and has been incorporated into several major Office applications, such as Word, Excel, Outlook, and Access.

Using VBA, you can do the following:

*   **Automate repetitive Excel tasks**, such as formatting, filtering, and data entry. For example, if I get some data set regularly and I need to do the same steps to clean the data, I can create a VBA code that does all that as soon as the code is run.
*   **Create custom Excel functions** (UDFs) to perform specialized calculations. While Excel does have a lot of functions, in case there is something you need that cannot be done with the built-in Excel function, you can create your own User Defined Functions using VBA.
*   **Use Loops** that allow you to go through cells/rows/columns/sheets/workbooks/charts and do the specified task. For example, I can use VBA to go through all the worksheets in the workbook and change the formatting in each of the worksheets.
*   **Work with Other MS Applications**. For example, I can write a VBA code to quickly import data from multiple Microsoft Word documents into an Excel sheet.

If you want to learn VBA from scratch, check out my [**free Excel VBA video course**](https://trumpexcel.com/excel-vba-course/)
. It’s created for VBA beginners and covers all the important basics before delving into some advanced VBA stuff.

The Concept of Object Oriented Programming
------------------------------------------

VBA is an Object Oriented Programming (OOP) language, which means that VBA works with objects such as Workbooks, worksheets, cells, rows, columns, charts, etc.

So when you are writing a code in VBA, you start with an object, and then you specify what change you want to make.

Let me give you an example.

Let’s say I want to change the color of cell A1 in the sheet named Sheet1 in the workbook named Example.xlsx

Below is the VBA code that will do this:

    Sub ChangeCellColor()
    
    Application.Workbooks("Example.xlsx").Sheets("Sheet1").Range("A1").Interior.Color = RGB(255, 0, 0)
    
    End Sub
    

Here is what is happening in this code:

1.  We start with the main object, which is the Excel application.
2.  Within the Excel application, we then go to the workbook called Example.xlsx
3.  Within that workbook, we then go to the sheet with the name Sheet1
4.  Within the sheet, we then refer to the cell where we want to make the color change, which is cell A1
5.  Within the cell, we refer to the interior object that will allow us to make changes inside the cell
6.  Finally, we refer to the color property of the cell Interior object that allows us to change the color to red.

This is a really simple example to explain object-oriented programming, but it encapsulates the essence of how it works.

We always start with the main object, and then we keep zeroing in till we reach the object in which we want to make the change (which was the cell interior in the above example).

Once we have the object in which we want to make the change, we then use the property/method of that object to make the change. For example, in this case, we used the color property to change the color of the cell.

To give you an example outside the programming world, imagine You have sent a letter to your friend. Now, for that letter to be delivered, the post office is going to first check which country the letter needs to be delivered.

Once the letter is in the country, they would check which state or city the letter needs to be delivered.

When the letter is in that city, the delivery person will check the locality, followed by the street address and the house number.

This is just like our example above, where we first started with the Excel application, then we zeroed into the workbook, then the worksheet, then the cell in the worksheet, and then the color interior object that we needed to change.

_**Related Articles:**_

*   [Working with Cells and Ranges in Excel VBA (Select, Copy, Move, Edit)](https://trumpexcel.com/vba-ranges/)
    
*   [Working with Worksheets using Excel VBA (Explained with Examples)](https://trumpexcel.com/vba-worksheets/)
    
*   [Using Workbook Object in Excel VBA (Open, Close, Save, Set)](https://trumpexcel.com/vba-workbook/)
    

Excel VBA Programming Basics
----------------------------

To start working with VBA programming in Excel, It would be good if you could familiarize yourself with some common terms that will come in handy when you start writing code.

It’s pretty basic stuff, and you don’t need to memorize each and everything.

### Subroutine

In Excel VBA, a subroutine is a block of code that performs a specific task.

For example, the below code would be called a subroutine.

    Sub SubRoutineExample()
        MsgBox "Good Day"
    End Sub

The above code is called a subroutine (or a procedure) and will always start with the word **Sub**. and end with **End Sub**.

When you start your code with the word sub, VBA knows that this is a subroutine, and it needs to follow all the steps that are mentioned in the subroutine.

You can have as many subroutines as you want in an Excel file.

Examples of subroutines in VBA include procedures for opening and closing workbooks, copying and pasting data, and formatting cells.

### Functions

In Excel VBA, a function is a block of code that performs a specific task and returns a value.

Below is an example of a function that takes two numbers and returns the product of the two numbers:

    Function MultiplyNums(Num1 As Double, Num2 As Double) As Double
        MultiplyNums = Num1 * Num2
    End Function

VBA codes of Functions start with the **Function** keyword and end with the **End Function** keywords.

You can use functions to perform calculations, manipulate strings, or do any other operation that returns a value.

In the context of Excel VBA, Subroutines (Sub) perform actions but don’t return a value. Functions (Function) perform actions and do return a value.

### DIM (Dimensions)

In VBA (Visual Basic for Applications), Dim is a keyword used to declare a new variable.

Dim stands for “Dimension”, which is used to allocate storage space in memory for variables, which can then be used to store data in your VBA code.

When you declare a variable using Dim, you also specify the type of data the variable can hold, such as Integer, String, Boolean, or other types.

If you don’t specify a data type, the variable will be of Variant type, which can hold any type of data. It’s a good practice to declare variables as it makes your code more efficient and also saves space in the memory.

Here’s the syntax for declaring a variable using Dim:

    Dim variableName As DataType

*   **variableName**: The name of the variable you are declaring.
*   **DataType**: The type of data the variable can hold, such as Integer, String, Boolean, Range, etc.

Here are a few examples of using Dim to declare different types of variables:

    ' Declare an Integer variable named count
    Dim count As Integer
    
    ' Declare a String variable named name
    Dim name As String
    
    ' Declare a Boolean variable named isActive
    Dim isActive As Boolean
    
    ' Declare a Range object variable named rng
    Dim rng As Range

If you don’t declare and specify the data type, VBA will automatically consider the variable a Variant data type.

### Objects, Properties, Methods

Objects, properties, and methods are the fundamental components of VBA code, facilitating users to interact with and manipulate Excel elements.

**Objects** in the VBA language are the **building blocks of a VBA program**, which can be used to store, manipulate, and perform operations on data. Some examples of objects would be the workbook object, the worksheet object, the range object, or the rows/columns object.

**Properties** are the characteristics of an object, such as its font size or color.

**Methods** are the actions that can be performed on an object, like sorting or filtering.

Mastering the use of objects, properties, and methods is key to developing efficient VBA code and automating tasks in Excel.

### Message Box and Input Box

Message boxes and Input boxes are employed to present information and collect user input in VBA.

A message box is a simple dialog box that displays a message to the user.

Below is the VBA code that will open a message box showing the message “Good Day”

    Sub ShowMessageBox()
       MsgBox "Good Day"
    End Sub

Below is the image of the message box you would see.

![Messagebox Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20452'%3E%3C/svg%3E)

An input box prompts the user to enter a value or piece of information (such as the range of cells, text strings, or numbers).

Below is a VBA code that asks the user to select a range of cells and then count the number of cells in the range and show the result in a message box.

    Sub CountCellsInRange()
        Dim selectedRange As Range
        Dim cellCount As Long
        
        ' Prompt the user to select a range of cells
        On Error Resume Next
        Set selectedRange = Application.InputBox("Select a range of cells:", Type:=8)
        On Error GoTo 0
        
        ' Check if a range has been selected
        If selectedRange Is Nothing Then
            MsgBox "You did not select a range!", vbExclamation
            Exit Sub
        End If
        
        ' Count the number of cells in the range
        cellCount = selectedRange.Cells.Count
        
        ' Display the result in a message box
        MsgBox "The number of cells in the selected range is: " & cellCount, vbInformation
    End Sub

These tools are useful for providing feedback to the user, guiding them through a process, or collecting data for further processing.

Incorporating message boxes and input boxes into your VBA code can enhance interactivity and user-friendliness for those utilizing your Excel workbook.

Also read: [Excel VBA MsgBox](https://trumpexcel.com/vba-msgbox/)

### Variables and Constants

Variables and constants are used to store and manage data within VBA code.

A **variable** is a storage location in memory that can hold a value, which may change during the execution of the code.

For example, if you’re running a loop 10 times, you can create a variable (say LoopCount) that increments by one every time the loop is completed. This way, you can use the variable to keep track of how many times the looping is done.

A **constant**, on the other hand, is a storage location that holds a fixed value, which cannot be changed during the execution of the code.

For example, if you’re working on sales data, you can use a constant to store the commission percentage value that would remain the same throughout.

Also read: [Understanding Excel VBA Data Types (Variables and Constants)](https://trumpexcel.com/vba-data-types-variables-constants/)

### Arrays

Arrays are utilized to store multiple values within a single variable.

They are useful for organizing and managing large amounts of data, as well as performing operations on that data, such as sorting or filtering.

Arrays can be one-dimensional (like a list) or multi-dimensional (like a table).

To give you an example, if you want to store all the values in a selected range of cells in Excel, then you can use an array to do that.

Below is the code that would store the values of range A1:A10 in an array and then show them one by one in the message box.

    Sub ArrayExample()
        ' Declare an array to hold the values from cells A1:A10
        Dim values(1 To 10) As Variant
        
        ' Declare a variable for looping
        Dim i As Integer
        
        ' Loop through cells A1:A10 and store the values in the array
        For i = 1 To 10
            values(i) = Cells(i, 1).Value
        Next i
        
        ' Loop through the array and display each value in a MessageBox
        For i = 1 To 10
            MsgBox "Value at position " & i & " is " & values(i)
        Next i
    End Sub

### Conditional Statements (If Then Else, Select Case)

Conditional statements in VBA control the flow of code based on certain conditions, such as the value of a variable or the result of a calculation.

There are two conditional statements in Excel VBA:

*   If Then Else Statement
*   Select Case Statement

In my experience, you are going to be using If Then Else statement a lot more than Select Case.

#### If Then Else Statement in VBA

The If Then Else statement allows you to run a block of code if a specific condition is met or execute another block of code if the condition is not met.

Below is an example code where If Then statements check whether the value in cell A1 is Excel or not. If the value in the cell is “Excel”, it colors the cell red, else it does nothing.

    Sub ColorCell()
        If Range("A1").Value = "Excel" Then
            Range("A1").Interior.Color = vbRed
        End If
    End Sub

Here is an example of IF Then Else (which also uses the Else block of code, which the above example didn’t use)

    Sub ColorCell()
    
        If Range("A1").Value = "Excel" Then
            Range("A1").Interior.Color = vbRed
        Else
            Range("A1").Interior.Color = vbYellow
        End If
    
    End Sub

The above code checks the value in cell A1, and if the value is “Excel”, it would color it red, else it would color it yellow.

#### [Select Case Statement in VBA](https://trumpexcel.com/vba-select-case/)

The Select Case statement allows you to execute different blocks of code based on the value of a variable or expression.

Below is an example of a code where the select case statement checks the value of cell A1. If the value is “Excel”, it colors it green. If the value is “PowerPoint”, it colors it red. Else, in all other cases, it colors it yellow.

    Sub ColorCell()
    Set cellrng = ThisWorkbook.Sheets("Sheet1").Range("A1")
         Select Case cellrng.Value
                Case "Excel"
                    cellrng.Interior.Color = vbGreen
                Case "PowerPoint"
                    cellrng.Interior.Color = vbRed
                Case Else
                    cellrng.Interior.Color = vbYellow
            End Select
    End Sub

Note that in the above code, I have set the variable cellrng using _Set cellrng = ThisWorkbook.Sheets(“Sheet1”).Range(“A1”)_. Doing this simplifies my code instead of using _ThisWorkbook.Sheets(“Sheet1”).Range(“A1”)_ everywhere, I can use the variable _cellrng_

### [Loops (For Next, For Each, Do While, Do Until)](https://trumpexcel.com/vba-loops/)

Loops in VBA enable the repetition of a code block for a specific number of times or the iteration through a collection of objects. The primary types of loops in VBA are:

1.  The Do Until Loop executes a code block until a specified condition is satisfied.
2.  The Do While Loop executes a code block while a certain condition remains valid.
3.  The For-Loop executes a code block a predefined number of times.

Loops, as a potent programming technique, can automate repetitive tasks in Excel, significantly enhancing the efficiency of your VBA code.

To give you an example, below is a code using For Each Next loop, that goes through each cell in A1:A10, and highlights all cells where the value is more than 80.

    Sub HighlightCells()
        ' Declare a Range object to represent the range A1:A10
        Dim rng As Range
        Set rng = ThisWorkbook.Sheets("Sheet1").Range("A1:A10")
        
        ' Declare a Cell object to represent each individual cell in the range
        Dim cell As Range
        
        ' Loop through each cell in the range using For Each...Next loop
        For Each cell In rng
            ' Check if the value of the cell is more than 80
            If cell.Value > 80 Then
                ' Highlight the cell by changing its interior color to yellow
                cell.Interior.Color = RGB(255, 255, 0)
            End If
        Next cell
    End Sub
    

_Related Articles:_

*   [If Then Else Statement in Excel VBA](https://trumpexcel.com/if-then-else-vba/)
    
*   [For Next Loop in Excel VBA](https://trumpexcel.com/for-next-loop-excel-vba/)
    

### Events (Advanced VBA)

Events in VBA refer to actions or occurrences that would start the execution of VBA code.

For example, you can write a code that automatically runs whenever you open a specific workbook, close a workbook, select any other sheet, or change the value of a cell.

Events are an advanced VBA concept and can really make some amazing things possible.

Below is a very simple example (and fairly useless one) of workbook\_open event that shows a message whenever you open the workbook.

    Private Sub Workbook_Open()
        MsgBox "Howdy! Welcome to This Worbook", vbInformation, "Welcome Message"
    End Sub

Below are some real-world scenarios where events can be useful:

*   When a workbook is opened, the Workbook\_Open event can be used to automatically refresh data from external sources, ensuring the user always sees the most up-to-date information.
*   In a shared workbook, the Workbook\_SheetChange event can be used to log user activities, such as which cells were modified, by whom, and when, to maintain an audit trail.
*   The Workbook\_BeforeClose event can be used to ensure that a workbook is automatically saved when a user attempts to close it, preventing potential data loss.

Also read: [Excel VBA Events](https://trumpexcel.com/vba-events/)
 - Complete Guide!

### UserForm (Advanced VBA)

UserForms are custom dialog boxes created using VBA to gather user input or display information to the user.

You can create some cool applications using Userforms in VBA (it’s an advanced concept).

For example, you can create an application where the user can enter the details, and the application would automatically generate invoices and save them as PDFs (or email them to specified people).

Or, you can create a UserForm that takes input from the user and generates budget reports or sales reports for them.

**CAUTION**: Changes done by VBA codes are irreversible. So it’s always a good idea to create a backup copy of your file before running the code.

Where to Put VBA Code in Excel?
-------------------------------

VBA code needs to be placed in the VB Editor ([Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
).

VB Editor is the interface that allows us to work with VBA. When you open Excel, it also opens the VB Editor in the back end, but you don’t see it.

Here are the different ways to open the VB Editor:

1.  Hold the ALT key and then press the F11 key (for Windows). If using a Mac, the shortcut would be _Opt + F11_ or _Fn + Opt + F11_
2.  Click the Developer tab in the ribbon and then click on the Visual Basic icon

Once the VB Editor is open, you can insert a module where our VBA codes need to go.

Here are the steps to insert a module:

1.  Click the Insert option in the menu.
2.  Click on Module.

The above steps would insert a new module, and you can write the code in the module code window. If you’re getting your code from somewhere else, you can copy and paste the code into the module code window.

### Where to Put VBA Events Code?

When working with event-related VBA codes, you will have to place the code:

*   ThisWorkbook object for events pertaining to the workbook
*   Worksheet object for events pertaining to that workbook

And how do you open the code window for these objects?

Open the VB Editor, and in the Project Explorer, double-click on the object for which you want to open the code window.

If you want to reuse the VBA code in your workbook, you need to save the file as a Macro Enabled file with .xlsm extension. If you don’t do this, your VBA code will be lost. Excel does show you a warning message when you saving a workbook with VBA code in any other file format.

[How to Run VBA Codes in Excel?](https://trumpexcel.com/run-a-macro-excel/)

----------------------------------------------------------------------------

Running VBA code in Excel is a simple process.

You can execute the VBA code by pressing the ‘F5’ key or selecting the ‘Run’ icon in the toolbar within the VBA editor.

You can also open the Macro dialog box (by clicking the Developer tab and then clicking on the Macro option). You will see all the macros listed in the Macro dialog box, and you can select the macro you want to run and then click on the Run button.

Additionally, you can [assign your VBA code to buttons](https://trumpexcel.com/assign-macro-to-button-in-excel/)
 or events within your workbook, allowing users to easily run the code by interacting with the workbook.

Below is a video that will show you how to run VBA codes in Excel.

Recording a Macro (Let Excel Write VBA Code for You)
----------------------------------------------------

If you’re new to VBA or just want to generate macros to save time, Excel provides a handy feature called “Record Macro” that allows you to create macros and generate VBA code, also known as macro code, automatically by performing actions in the spreadsheet.

To record a macro, simply navigate to the Developer tab and click the Record Macro button.

As you perform actions in the spreadsheet, such as entering data, formatting cells, or creating charts, Excel VBA will automatically generate the corresponding code for you.

Once you’re done recording, you can stop the macro recorder and view the generated code in the VBA editor, where you can make any necessary modifications or enhancements.

If you’re a beginner, recording a macro is an easy way to automate tasks and also learn how VBA code works. You can record the macro while performing some tasks and then analyze the code to see how it works.

Also read: [How to Record a Macro in Excel?](https://trumpexcel.com/record-macro-vba/)

Debugging and Error Handling in Excel VBA
-----------------------------------------

Like any programming language, being able to identify and resolve issues in your VBA code is important.

Debugging and [error-handling techniques in Excel VBA](https://trumpexcel.com/vba-error-handling/)
 can help you pinpoint problems, understand their causes, and implement solutions to ensure your code runs smoothly and efficiently.

The VBA editor provides several debugging tools, such as breakpoints, watches, and the Immediate window, which can assist you in testing and debugging your code.

Mastering these techniques allows you to develop robust, error-free VBA programs, thus enhancing your Excel experience.

Limitations of VBA in Excel?
----------------------------

While VBA is a powerful tool for automating tasks and enhancing functionality in Excel, it does have some limitations.

*   VBA can be slow for large datasets and complex calculations, especially compared to more modern programming languages and environments.
*   Creating user-friendly, modern, and intuitive interfaces is challenging in VBA. The UserForm object used for creating custom forms in VBA is quite outdated and limited in terms of design and functionality.
*   VBA macros can be a security risk, as malicious code can be run through macros. This has led to many organizations disabling macros, which limits the use of VBA.
*   VBA is not supported in Excel for Mac to the same extent as in Excel for Windows, which could cause compatibility issues. It is also not supported in Excel Online.
*   While VBA can integrate with other Microsoft Office applications, integration with external systems and databases can be more challenging compared to more versatile languages like Python or C#.

Additionally, newer tools such as Power Query may be able to complete tasks that were once only achievable using VBA.

It’s important to be aware of these limitations when deciding whether VBA is the right tool for your particular needs and to consider alternative solutions when necessary.

Best Practices When Writing Excel VBA Programming
-------------------------------------------------

When writing Excel VBA (Visual Basic for Applications) code, it’s important to follow best practices to ensure that your code is efficient, maintainable, and error-free.

Note that these best practices would be applicable to any programming language and not just VBA.

Here are some best practices to consider:

1.  Add comments to your code to explain the logic and any complex operations. It’s especially helpful if you need to revisit the code later or you’re sharing it with someone else.
2.  Use meaningful and descriptive names for variables, functions, subs, and modules. This makes following and interpreting the code a lot easier.
3.  Use consistent indentation and formatting to improve the code readability. Also, break long lines of code into multiple lines.
4.  Use error handling by using ‘On error GoTo’ statement
5.  Declare all variables using the Dim statement.
6.  Break your code into small, reusable functions and subroutines.
7.  Turn off screen updating (Application.ScreenUpdating = False) and calculation (Application.Calculation = xlCalculationManual) while your macro is running.
8.  Turn off screen updating (Application.ScreenUpdating = False) and calculation (Application.Calculation = xlCalculationManual) while your macro is running.
9.  Avoid hardcoding worksheet names, range addresses, and file paths.
10.  Always back up your work before implementing VBA code.

VBA vs. Office Scripts in Excel
-------------------------------

VBA and Office Scripts are both powerful tools for automating tasks and enhancing functionality in Excel, but they do have some key differences.

While VBA is a programming language primarily used for the desktop version of Excel, Office Scripts are designed for the online version of Excel and other Microsoft Office applications.

Office Scripts are written in TypeScript or JavaScript and leverage the Office Scripts JavaScript APIs to interact with Excel workbooks.

While VBA offers more extensive capabilities, the rise of cloud computing and collaboration has given Office Scripts a distinct advantage.

Integrating with Office 365 services allows Office Scripts to offer features like real-time collaboration and version control. Additionally, Office Scripts provide enhanced security measures to protect your data and scripts.

VBA in Other Microsft Office Applications
-----------------------------------------

VBA is not limited to Excel; it can also be used in other Microsoft Office applications, such as Word, PowerPoint, and Outlook.

Learning the use of VBA in these other applications lets you automate tasks, save macros, develop custom functions, and boost the overall functionality of the entire Office suite.

Whether you’re working on a complex report in Word, a dynamic presentation in PowerPoint, or streamlining your email management in Outlook, VBA can help you work more efficiently and effectively across the entire range of Microsoft Office applications.

What is the Best Way to Learn VBA?
----------------------------------

[**Check out my free Excel VBA course**](https://www.youtube.com/playlist?list=PLm8I8moAHiH2n5HC4ZXBgS-cBLjxWDreu)
 (no sign-up needed).

I created it for VBA beginners, so it covers every concept in detail so that you build a rock-solid foundation. It also covers some advanced VBA stuff that will blow your mind.

Once you’re done with the course, you will easily be able to use VBA to automate stuff in Excel.

Frequently Asked Questions about Excel VBA
------------------------------------------

Below are some questions you may still have about Excel VBA

### Is Excel VBA a good skill?

Excel VBA is an invaluable skill, especially for data analysis, finance, and project management professionals. If you work with Excel and automating your work can be useful, definitely learn VBA (it’s not that hard)

### Is it easy to learn VBA?

VBA may seem daunting to learn, but its straightforward syntax makes it relatively easy to master with time and dedication. If you have learned any other programming language, you will find VBA to be a cake walk. If you have never learned any programming language, you will have a little bit of learning curve.

### Is VBA similar to Python?

VBA and Python share some similarities, such as the Object Model being the same across both languages.

However, VBA is best suited for automating and customizing Microsoft Office applications, while Python is better for general-purpose programming.

**Related Excel VBA Articles:**

*   [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)
    
*   [Excel Personal Macro Workbook | Save & Use Macros in All Workbooks](https://trumpexcel.com/personal-macro-workbook/)
    
*   [Excel VBA Immediate Window](https://trumpexcel.com/vba-immediate-window/)
    
*   [Excel VBA Autofilter](https://trumpexcel.com/vba-autofilter/)
    
*   [Excel VBA FileSystemObject (FSO)](https://trumpexcel.com/vba-filesystemobject/)
    
*   [Excel VBA InStr Function – Explained with Examples](https://trumpexcel.com/excel-vba-instr/)
    
*   [Excel VBA SPLIT Function – Explained with Examples](https://trumpexcel.com/vba-split-function/)
    
*   [Make VBA Code Pause or Delay (Using Sleep / Wait Commands)](https://trumpexcel.com/vba-sleep-wait/)
    

Excel VBA Tips & Tutorials (How-Tos)
------------------------------------

This section provides various VBA tips and tutorials that you can use to automate your work in Excel.

These are usually focused on getting a specific task done (such as highlighting blank cells or inserting dates and timestamps). The tutorials use a lot of the concepts covered in the previous section.

As I write more How-to VBA tips, I will add them to the list below.

*   [How to Select Every Third Row in Excel (or select every Nth Row)](https://trumpexcel.com/select-every-third-row/)
    
*   [24 Useful Excel Macro Examples for VBA Beginners (Ready-to-use)](https://trumpexcel.com/excel-macro-examples/)
    
*   [How to Highlight Blank Cells in Excel (in less than 10 seconds)](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [How to Quickly Insert Date and Timestamp in Excel](https://trumpexcel.com/date-timestamp-excel/)
    
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [How to Filter Cells with Bold Font Formatting in Excel (An Easy Guide)](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [How to Make Multiple Selections in a Drop Down List in Excel](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    
*   [How to Filter Cells that have Duplicate Text Strings (Words) in it](https://trumpexcel.com/duplicate-text-strings/)
    
*   [\[Quick Tip\] How to Select 500 cells/rows in Excel (with a single click)](https://trumpexcel.com/select-500-cells-rows/)
    
*   [How to Quickly Remove Hyperlinks from a Worksheet in Excel](https://trumpexcel.com/remove-hyperlinks/)
    
*   [Get the List of File Names from a Folder in Excel (with and without VBA)](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
    
*   [How to Sort Data in Excel using VBA](https://trumpexcel.com/sort-data-vba/)
    
*   [Sort Worksheets in Excel](https://trumpexcel.com/sort-worksheets/)
     (in alphabetical order)
*   [How to Hide a Worksheet in Excel (that can not be unhidden)](https://trumpexcel.com/hide-worksheet/)
    
*   [Extract Numbers from String in Excel](https://trumpexcel.com/extract-numbers-from-string-excel/)
    
*   [Highlight the Active Row and Column in a Data Range in Excel](https://trumpexcel.com/highlight-active-row-column-excel/)
    
*   [How to Convert Excel to PDF Using VBA](https://trumpexcel.com/convert-excel-to-pdf/)
    
*   [How to Add Leading Zeroes in Excel](https://trumpexcel.com/add-leading-zeroes-excel/)
    
*   [How to Combine Multiple Excel Files into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    
*   [Delete Blank Rows in Excel (with and without VBA)](https://trumpexcel.com/delete-blank-rows-excel/)
    
*   [Get a List of All the Comments in a Worksheet in Excel](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/)
    
*   [How to Create a Stopwatch in Excel (Basic + ToastMasters Style)](https://trumpexcel.com/stopwatch-in-excel/)
    
*   [Quickly Generate Military Alphabet Code for a Word in Excel](https://trumpexcel.com/generate-military-alphabet-code-excel/)
    
*   [Matrix Falling Numbers Effect in Excel using VBA](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/)
    
*   [Dynamic Charting – Highlight Data Points in Excel with a Click of a Button](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/)
    
*   [Adjust Scroll Bar Maximum Value based on a Cell Value in Excel](https://trumpexcel.com/adjust-scroll-bar-maximum-value/)
    
*   [Quickly Create Summary Worksheet with Hyperlinks in Excel](https://trumpexcel.com/create-summary-worksheet-in-excel/)
    
*   [Get Multiple Lookup Values in a Single Cell (With & Without Repetition)](https://trumpexcel.com/multiple-lookup-values-single-cell-excel/)
    
*   [Unhide Sheets in Excel](https://trumpexcel.com/unhide-sheets-excel/)
     (All in one go)
*   [Split Each Excel Sheet Into Separate Files](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/)
    
*   [How to Delete Entire Row in Excel Using VBA](https://trumpexcel.com/vba-delete-row-excel/)
    
*   [How to Delete All Hidden Rows and Columns in Excel](https://trumpexcel.com/delete-hidden-rows-columns-in-excel/)
    
*   [Using Active Cell in VBA in Excel (Examples)](https://trumpexcel.com/active-cell-vba-excel/)
    
*   [How to Open Excel Files Using VBA (Examples)](https://trumpexcel.com/open-excel-files-using-vba/)
    
*   [Rename Files Using VBA](https://trumpexcel.com/excel-vba/rename-files/)
    
*   [VBA Check IF Cell is Empty (ISEMPTY Function)](https://trumpexcel.com/excel-vba/check-if-cell-empty/)
    
*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [VBA Delete Sheet](https://trumpexcel.com/excel-vba/delete-sheet/)
    
*   [VBA Check IF Sheet Exists](https://trumpexcel.com/excel-vba/check-if-sheet-exists/)
    
*   [VBA Rename Sheet in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)
    
*   [VBA Activate Sheet (Worksheet.Activate)](https://trumpexcel.com/excel-vba/activate-sheet/)
    
*   [VBA Create New Sheet (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    
*   [VBA Protect / Unprotect Sheet](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)
    
*   [VBA Clear Sheet](https://trumpexcel.com/excel-vba/clear-sheet/)
    
*   [VBA Hide or Unhide Sheets](https://trumpexcel.com/excel-vba/hide-unhide-sheet/)
    
*   [VBA Remove Duplicate Values in Excel](https://trumpexcel.com/excel-vba/remove-duplicate-values/)
    
*   [VBA Count Rows](https://trumpexcel.com/excel-vba/count-rows/)
    
*   [Using VLOOKUP in VBA](https://trumpexcel.com/excel-vba/vlookup/)
    
*   [Check If Workbook Is Open Using VBA](https://trumpexcel.com/excel-vba/check-if-workbook-open/)
    
*   [Remove Password from VBA Project in Excel](https://trumpexcel.com/excel-vba/remove-password/)
    
*   [VBA Exit Sub Statement](https://trumpexcel.com/excel-vba/exit-sub/)
    
*   [Run Time Error 9 (Subscript Out of Range)](https://trumpexcel.com/excel-vba/run-time-error-9/)
    

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