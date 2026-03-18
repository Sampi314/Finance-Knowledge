# Understanding Excel VBA Data Types (Variables and Constants)

**Source:** https://trumpexcel.com/vba-data-types-variables-constants

---

[Skip to content](https://trumpexcel.com/vba-data-types-variables-constants/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-data-types-variables-constants/#below-title)

In Excel VBA, you would often be required to use variables and constants.

When working with VBA, a variable is a location in your computer’s memory where you can store data. The type of data you can store in a variable would depend on the data type of the variable.

For example, if you want to store integers in a variable, your data type would be ‘Integer’ and if you want to store text then your data type would be ‘String’.

More on data types later in this tutorial.

While a variable’s value changes when the code is in progress, a constant holds a value that never changes. As a good coding practice, you should define the data type of both – variable and constant.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-data-types-variables-constants/#)

Why Use Variables in VBA?
-------------------------

When you code in VBA, you would need variables that you can use to hold a value.

The benefit of using a variable is that you can change the value of the variable within the code and continue to use it in the code.

For example, below is a code that adds the first 10 positive numbers and then displays the result in a [message box](https://trumpexcel.com/vba-msgbox/)
:

Sub AddFirstTenNumbers()
Dim Var As Integer
Dim i As Integer
Dim k as Integer
For i = 1 To 10
k = k + i
Next i
MsgBox k
End Sub

There are three variables in the above code – **Var**, **i**, and **k.**

The above code uses a [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 where all these three variables are changed as the loops are completed.

The usefulness of a variable lies in the fact that it can be changed while your code is in progress.

Below are some rules to keep in mind when naming the variables in VBA:

1.  You can use alphabets, numbers, and punctuations, but the first number must be an alphabet.
2.  You can not use space or period in the variable name. However, you can use an underscore character to make the variable names more readable (such as Interest\_Rate)
3.  You can not use special characters (#, $, %, &, or !) in variable names
4.  VBA doesn’t distinguish between the case in the variable name. So ‘InterestRate’ and ‘interestrate’ are the same for VBA. You can use mixed case to make the variables more readable.
5.  VBA has some reserved names that you can use for a variable name. For example, you can not use the word ‘Next’ as a variable name, as it’s a reserved name for For Next loop.
6.  Your variable name can be up to 254 characters long.

Data Type of Variables
----------------------

To make the best use of variables, it’s a good practice to specify the data type of the variable.

The data type you assign to a variable will be dependent on the type of data you want that variable to hold.

Below is a table that shows all the available data types you can use in Excel VBA:

|     |     |     |
| --- | --- | --- |
| **Data Type** | **Bytes Used** | **Range of Values** |
| Byte | 1 byte | 0 to 255 |
| Boolean | 2 bytes | True or False |
| Integer | 2 bytes | \-32,768 to 32,767 |
| Long (long integer) | 4 bytes | \-2,147,483,648 to 2,147,483,647 |
| Single | 4 bytes | \-3.402823E38 to -1.401298E-45 for negative values; 1.401298E-45 to 3.402823E38 for positive values |
| Double | 8 bytes | \-1.79769313486231E308 to-4.94065645841247E-324 for negative values; 4.94065645841247E-324 to 1.79769313486232E308 for positive values |
| Currency | 8 bytes | \-922,337,203,685,477.5808 to 922,337,203,685,477.5807 |
| Decimal | 14 bytes | +/-79,228,162,514,264,337,593,543,950,335 with no decimal point;+/-7.9228162514264337593543950335 with 28 places to the right of the decimal |
| Date | 8 bytes | January 1, 100 to December 31, 9999 |
| Object | 4 bytes | Any Object reference |
| String (variable-length) | 10 bytes + string length | 0 to approximately 2 billion |
| String (fixed-length) | Length of string | 1 to approximately 65,400 |
| Variant (with numbers) | 16 bytes | Any numeric value up to the range of a Double |
| Variant (with characters) | 22 bytes + string length | Same range as for variable-length String |
| User-defined | Varies | The range of each element is the same as the range of its data type. |

When you specify a data type for a variable in your code, it tells VBA to how to store this variable and how much space to allocate for it.

For example, if you need to use a variable that is meant to hold the month number, you can use the BYTE data type (which can accommodate values from 0 to 255). Since the month number is not going to be above 12, this will work fine and also reserve less memory for this variable.

On the contrary, if you need a variable to store the row numbers in Excel, you need to use a data type that can accommodate a number up to 1048756. So it’s best to use the Long data type.

Declaring Variable Data Types
-----------------------------

As a good coding practice, you should declare the data type of variables (or constants) when writing the code. Doing this makes sure that VBA allocates only the specified memory to the variable and this can make your code run faster.

Below is an example where I have declared different data types to different variables:

Sub DeclaringVariables()
Dim X As Integer
Dim Email As String
Dim FirstName As String
Dim RowCount As Long
Dim TodayDate As Date
End Sub

To declare a variable data type, you need to use the DIM statement (which is short for Dimension).

In ‘**Dim X as Integer**‘, I have declared the variable X as Integer data type.

Now when I use it in my code, VBA would know that X can hold only integer data type.

If I try to assign a value to it which is not an integer, I will get an error (as shown below):

![Excel VBA Data Types assignment error mismatch](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20391'%3E%3C/svg%3E)

Note: You can also choose to not declare the data type, in which case, VBA automatically considers the variable of the variant data type. A variant data type can accommodate any data type. While this may seem convenient, it’s not a best practice to use variant data type. It tends to take up more memory and can make your VBA code run slower.

Making Variable Declaration Mandatory (Option Explicit)
-------------------------------------------------------

While you can code without ever declaring variables, it’s a good practice to do this.

Apart from saving memory and making your code more efficient, declaring variables has another major benefit – it helps trap errors caused by misspelled variable names.

To make sure you’re forced to declare variables, add the following line to the top of your module.

Option Explicit

When you add ‘Option Explicit’, you will be required to declare all the variables before running the code. If there is any variable that has not been declared, VBA would show an error.

There is a huge benefit in using Option Explicit.

Sometimes, you may end up making a typing error and enter a variable name which is incorrect.

Normally, there is no way for VBA to know whether it’s a mistake or is intentional. However, when you use ‘Option Explicit’, VBA would see the misspelled variable name as a new variable that has not been declared and will show you an error. This will help you identify these misspelled variable names, which can be quite hard to spot in a long code.

Below is an example where using ‘Option Explicit’ identifies the error (which couldn’t have been trapped had I not used ‘Option Explicit’)

Sub CommissionCalc()
Dim CommissionRate As Double
If Range("A1").Value > 10000 Then
CommissionRate = 0.1
Else
CommissionRtae = 0.05
End If
MsgBox "Total Commission: " & Range("A1").Value \* CommissionRate
End Sub

Note that I have misspelled the word ‘CommissionRate’ once in this code.

If I don’t use Option Explicit, this code would run and give me the wrong total commission value (in case the value in cell A1 is less than 10000).

But if I use Option Explicit at the top of the module, it will not let me run this code before I either correct the misspelled word or declare it as another variable. It will show an error as shown below:

![Variable not defined error in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20312%20223'%3E%3C/svg%3E)

While you can insert the line ‘Option Explicit’ every time you code, here are the steps to make it appear by default:

1.  In the VB Editor toolbar, click on Tools.
2.  Click on Options.![Select Options in Tools tab in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20247%20201'%3E%3C/svg%3E)
3.  In the Options dialog box, click on Editor tab.![Editor Tab in Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20440'%3E%3C/svg%3E)
4.  Check the option – “Require Variable Declaration”.![Require Variable Declaration Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20440'%3E%3C/svg%3E)
5.  Click OK.

Once you have enabled this option, whenever you open a new module, VBA would automatically add the line ‘Option Explicit’ to it.

Note: This option will only impact any module you create after this option is enabled. All existing modules are not affected.

Scope of Variables
------------------

So far, we have seen how to declare a variable and assign data types to it.

In this section, I will cover the scope of variables and how you can declare a variable to be used in a subroutine only, in an entire module or in all the modules.

The scope of a variable determines where can the variable be used in VBA,

There are three ways to scope a variable in Excel VBA:

1.  Within a single subroutine (Local variables)
2.  Within a module (Module-level variables)
3.  In all modules (Public variables)

Let’s look at each of these in detail.

### Within a Single Subroutine (Local Variables)

When you declare a variable within a subroutine/procedure, then that variable is available only for that subroutine.

You can not use it in other subroutines in the module.

As soon as the subroutine ends, the variable gets deleted and the memory used by it is freed.

In the below example, the variables are declared within the subroutine and would be deleted when this subroutine ends.

![declaring variables in a procedure](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20274'%3E%3C/svg%3E)

### Within a Module (Module-level Variables)

When you want a variable to be available for all the procedures in a module, you need to declare it at the top of the module (and not in any subroutine).

![Declare Variable for all procedures](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20317'%3E%3C/svg%3E)

Once you declare it at the top of the module, you can use that variable in all the procedures in that module.

In the above example, the variable ‘i’ is declared at the top of the module and is available to be used by all the modules.

Note that when the subroutine ends, the module level variables are not deleted (it retains its value).

Below is an example, where I have two codes. When I run the first procedure and then run the second one, the value of ‘i’ becomes 30 (as it carries the value of 10 from the first procedure)

![Module level variables](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20293'%3E%3C/svg%3E)

### In All Modules (Public Variables)

If you want a variable to be available in all the procedure in the workbook, you need to declare it with the Public keyword (instead of DIM).

The below line of code at the top of the module would make the variable ‘CommissionRate’ available in all the modules in the workbook.

 Public CommissionRate As Double

![Declaring a Public Variable](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20145'%3E%3C/svg%3E)

You can insert the variable declaration (using the Public keyword), in any of the modules (at the top before any procedure).

Static Variables (that retains the value)
-----------------------------------------

When you work with local variables, as soon as the procedure ends, the variable would lose its value and would be deleted from VBA’s memory.

In case you want the variable to retain the value, you need to use the **Static** keyword.

Let me first show you what happens in a normal case.

In the below code, when I run the procedure multiple times, it will show the value 10 everytime.

Sub Procedure1()
Dim i As Integer
i = i + 10
MsgBox i
End Sub

Now if I use the Static keyword instead of DIM, and run the procedure multiple times, it will keep on showing values in increments of 10. This happens as the variable ‘i’ retains its value and uses it in the calculation.

Sub Procedure1()
Static i As Integer
i = i + 10
MsgBox i
End Sub

Declaring Constants in Excel VBA
--------------------------------

While variables can change during the code execution, if you want to have fixed values, you can use constants.

A constant allows you to assign a value to a named string that you can use in your code.

The benefit of using a constant is that it makes it easy to write and comprehend code, and also allows you to control all the fixed values from one place.

For example, if you are calculating commissions and the commission rate is 10%, you can create a constant (CommissionRate) and assign the value 0.1 to it.

In future, if the commission rate changes, you just need to make the change at one place instead of manually changing it in the code everywhere.

Below is a code example where I have assigned a value to the constant:

Sub CalculateCommission()
Dim CommissionValue As Double
Const CommissionRate As Double = 0.1
CommissionValue = Range("A1") \* CommissionRate
MsgBox CommissionValue
End Sub

The following line is used to declare the constant:

Const CommissionRate As Double = 0.1

When declaring constants, you need to start with the keyword ‘**Const**‘, followed by the name of the constant.

Note that I have specified the data type of the constant as Double in this example. Again, it’s a good practice to specify the data type to make your code run faster and be more efficient.

If you don’t declare the data type, it would be considered as a variant data type.

Just like variables, constants can also have scope based on where and how these are declared:

1.  **Within a single subroutine (Local constants)**: These are available in the subroutine/procedure in which these are declared. As the procedure ends, these constants are deleted from the system’s memory.
2.  **Within a module (Module-level constants)**: These are declared at the top of the module (before any procedure). These are available for all the procedures in the module.
3.  **In all modules (Public constants)**: These are declared using the ‘Public’ keyword, at the top of any module (before any procedure). These are available to all the procedures in all the modules.

**You May Also Like the Following VBA Tutorials:**

*   [How to Record a Macro in Excel](https://trumpexcel.com/record-macro-vba/)
    
*   [Working with Cells and Ranges in Excel VBA](https://trumpexcel.com/vba-ranges/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    
*   [Working with Workbooks in Excel VBA](https://trumpexcel.com/vba-workbook/)
    
*   [VBA Events](https://trumpexcel.com/vba-events/)
    
*   [Excel VBA Loops](https://trumpexcel.com/vba-loops/)
    
*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    
*   [If Then Else Statement in Excel VBA.](https://trumpexcel.com/if-then-else-vba/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Understanding Excel VBA Data Types (Variables and Constants)”
---------------------------------------------------------------------------

1.  I need to clear to adjacent cells (i.e. cell 7 and 8), if the target cell 6 become blank.  
    With below formula, I could reach up to only next cell. Please help
    
    <Private Sub Worksheet\_Change(ByVal Target As Range)  
    <On Error Resume Next  
    <If Target.Column = 6 Then  
    <If Target.Validation.Type = " " Then  
    <Application.EnableEvents = False  
    <Target.Offset(0, 1).ClearContents  
    <End If  
    <End If  
    <If Target.Column = 7 Then  
    <If Target.Validation.Type = " " Then  
    <Application.EnableEvents = False  
    <Target.Offset(0, 1).ClearContents  
    <End If  
    <End If
    
    <exitHandler:  
    <Application.EnableEvents = True  
    <Exit Sub  
    <End Sub
    
    [Reply](https://trumpexcel.com/vba-data-types-variables-constants/#comment-12140)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-data-types-variables-constants/#respond)

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