# Creating a User Defined Function (UDF) in Excel VBA [Ultimate Guide]

**Source:** https://trumpexcel.com/user-defined-function-vba

---

[Skip to content](https://trumpexcel.com/user-defined-function-vba/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/user-defined-function-vba/#below-title)

With VBA, you can create a custom Function (also called a User Defined Function) that can be used in the worksheets just like regular functions.

These are helpful when the existing Excel functions are not enough. In such cases, you can create your own custom User Defined Function (UDF) to cater to your specific needs.

In this tutorial, I’ll cover everything about creating and using custom functions in VBA.

If you’re interested in learning VBA the easy way, check out my **[Online Excel VBA Training](https://trumpexcel.com/excel-vba-jetpack-course/)
**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/user-defined-function-vba/#)

What is a Function Procedure in VBA?
------------------------------------

A Function procedure is a VBA code that performs calculations and returns a value (or an array of values).

Using a Function procedure, you can create a function that you can use in the worksheet (just like any regular Excel function such as SUM or VLOOKUP).

When you have created a Function procedure using VBA, you can use it in three ways:

1.  As a formula in the worksheet, where it can take arguments as inputs and returns a value or an array of values.
2.  As a part of your VBA subroutine code or another Function code.
3.  In [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
    .

While there are already 450+ inbuilt [Excel functions](https://trumpexcel.com/excel-functions/)
 available in the worksheet, you may need a custom function if:

*   The inbuilt functions can’t do what you want to get done. In this case, you can create a custom function based on your requirements.
*   The inbuilt functions can get the work done but the formula is long and complicated. In this case, you can create a custom function that is easy to read and use.

Note that custom functions created using VBA can be significantly slower than the inbuilt functions. Hence, these are best suited for situations where you can’t get the result using the inbuilt functions.

### Function Vs. Subroutine in VBA

A ‘Subroutine’ allows you to execute a set of code while a ‘Function’ returns a value (or an array of values).

To give you an example, if you have a list of numbers (both positive and negative), and you want to identify the negative numbers, here is what you can do with a function and a subroutine.

A subroutine can loop through each cell in the range and can highlight all the cells that have a negative value in it. In this case, the subroutine ends up changing the properties of the range object (by changing the color of the cells).

With a custom function, you can use it in a separate column and it can return a TRUE if the value in a cell is negative and FALSE if it’s positive. With a function, you can not change the object’s properties. This means that you can not change the color of the cell with a function itself (however, you can do it using conditional formatting with the custom function).

When you create a User Defined Function (UDF) using VBA, you can use that function in the worksheet just like any other function. I will cover more on this in the ‘Different Ways of Using a User Defined Function in Excel’ section.

Creating a Simple User Defined Function in VBA
----------------------------------------------

Let me create a simple user-defined function in VBA and show you how it works.

The below code creates a function that will extract the numeric parts from an alphanumeric string.

Function GetNumeric(CellRef As String) as Long
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If IsNumeric(Mid(CellRef, i, 1)) Then Result = Result & Mid(CellRef, i, 1)
Next i
GetNumeric = Result
End Function

When you have the above code in the module, you can use this function in the workbook.

Below is how this function – _GetNumeric_ – can be used in Excel.

![Using a User Defined Function in Excel - GetNumeric](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20668%20320'%3E%3C/svg%3E)

Now before I tell you how this function is created in VBA and how it works, there are a few things you should know:

*   When you create a function in VBA, it becomes available in the entire workbook just like any other regular function.
*   When you type the function name followed by the equal to sign, Excel will show you the name of the function in the list of matching functions. In the above example, when I entered =Get, Excel showed me a list that had my custom function.

I believe this is a good example when you can use VBA to create a simple-to-use function in Excel. You can do the same thing with a formula as well ([as shown in this tutorial](https://trumpexcel.com/extract-numbers-from-string-excel/)
), but that becomes complicated and hard to understand. With this UDF, you only need to pass one argument and you get the result.

Anatomy of a User Defined Function in VBA
-----------------------------------------

In the above section, I gave you the code and showed you how the UDF function works in a worksheet.

Now let’s deep dive and see how this function is created. You need to place the below code in a [module in the VB Editor](https://trumpexcel.com/visual-basic-editor/)
. I cover this topic in the section – ‘Where to put the VBA Code for a User-Defined Function’.

Function GetNumeric(CellRef As String) as Long
' This function extracts the numeric part from the string
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If IsNumeric(Mid(CellRef, i, 1)) Then Result = Result & Mid(CellRef, i, 1)
Next i
GetNumeric = Result
End Function

The first line of the code starts with the word – Function.

This word tells VBA that our code is a function (and not a subroutine). The word Function is followed by the name of the function – GetNumeric. This is the name that we will be using in the worksheet to use this function.

*   The name of the function cannot have spaces in it. Also, you can’t name a function if it clashes with the name of a cell reference. For example, you can not name the function ABC123 as it also refers to a cell in Excel worksheet.
*   You shouldn’t give your function the same name as that of an existing function. If you do this, Excel would give preference to the in-built function.
*   You can use an underscore if you want to separate words. For example, Get\_Numeric is an acceptable name.

The function name is followed by some arguments in parenthesis. These are the arguments that our function would need from the user. These are just like the arguments that we need to supply to Excel’s inbuilt functions. For example in a [COUNTIF function](https://trumpexcel.com/excel-countif-function/)
, there are two arguments (range and criteria)

![Arguments in a user defined function in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20245%20147'%3E%3C/svg%3E)

Within the parenthesis, you need to specify the arguments.

In our example, there is only one argument – CellRef.

It’s also a good practice to specify what kind of argument the function expects. In this example, since we will be feeding the function a [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
, we can specify the argument as a ‘Range’ type. If you don’t specify a data type, VBA would consider it to be a variant (which means you can use any data type).

![Argument defined as range in the user defined function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20754%20203'%3E%3C/svg%3E)

If you have more than one arguments, you can specify those in the same parenthesis – separated by a comma. We will see later in this tutorial on how to use multiple arguments in a user-defined function.

Note that the function is specified as the ‘String’ data type. This would tell VBA that the result of the formula would be of the String data type.

While I can use a numeric data type here (such as Long or Double), doing that would limit the range of numbers it can return. If I have a 20 number long string that I need to extract from the overall string, declaring the function as a Long or Double would give an error (as the number would be out of its range). Hence I have kept the function output data type as String.

![Defining the Function Output Data type in the custom function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20754%20203'%3E%3C/svg%3E)

[The second line of the code – the one in green that starts with an apostrophe – is a comment](https://trumpexcel.com/comments-excel-vba/)
. When reading the code, VBA ignores this line. You can use this to add a description or a detail about the code.

![Comment in the User Defined Function in Excel VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20786%20203'%3E%3C/svg%3E)

The third line of the code declares a variable ‘StringLength’ as an Integer data type. This is the variable where we store the value of the length of the string that is being analyzed by the formula.

The fourth line declares the variable Result as a String data type. This is the variable where we will extract the numbers from the alphanumeric string.

![Declaring Variables in the UDF custom function in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20786%20203'%3E%3C/svg%3E)

The fifth line assigns the length of the string in the input argument to the ‘StringLength’ variable. Note that ‘CellRef’ refers to the argument that will be given by the user while using the formula in the worksheet (or using it in VBA – which we will see later in this tutorial).

![Assigning length of the string to a variable](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20786%20203'%3E%3C/svg%3E)

Sixth, seventh, and eighth lines are the part of the [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
. The loop runs for as many times as many characters are there in the input argument. This number is given by the [LEN function](https://trumpexcel.com/excel-len-function/)
 and is assigned to the ‘StringLength’ variable.

So the loop runs from ‘1 to Stringlength’.

Within the loop, the [IF statement](https://trumpexcel.com/if-then-else-vba/)
 analyzes each character of the string and if it’s numeric, it adds that numeric character to the Result variable. It uses the MID function in VBA to do this.

![For Next Loop in the User Defined Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20786%20203'%3E%3C/svg%3E)

The second last line of the code assigns the value of the result to the function. It’s this line of code that ensures that the function returns the ‘Result’ value back in the cell (from where it’s called).![Assigning Result value to the custom function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20786%20203'%3E%3C/svg%3E)

The last line of the code is End Function. This is a mandatory line of code that tells VBA that the function code ends here.

![End Function as the last line of VBA code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20786%20203'%3E%3C/svg%3E)

The above code explains the different parts of a typical custom function created in VBA. In the following sections, we will deep dive into these elements and also see the different ways to execute the VBA function in Excel.

Arguments in a User Defined Function in VBA
-------------------------------------------

In the above examples, where we created a user-defined function to get the numeric part from an alphanumeric string (GetNumeric), the function was designed to take one single argument.

In this section, I will cover how to create functions that take no argument to the ones that take multiple arguments (required as well as optional arguments).

### Creating a Function in VBA without Any Arguments

In Excel worksheet, we have several functions that take no arguments (such as [RAND](https://trumpexcel.com/excel-rand-function/)
, [TODAY](https://trumpexcel.com/excel-today-function/)
, [NOW](https://trumpexcel.com/excel-now-function/)
).

These functions are not dependent on any input arguments. For example, the TODAY function would return the current date and the RAND function would return a random number between 0 and 1.

You can create such similar function in VBA as well.

Below is the code that will give you the name of the file. It doesn’t take any arguments as the result it needs to return is not dependent on any argument.

Function WorkbookName() As String
WorkbookName = ThisWorkbook.Name
End Function

The above code specifies the function’s result as a String data type (as the result we want is the file name – which is a string).

This function assigns the value of  ‘ThisWorkbook.Name’ to the function, which is returned when the function is used in the worksheet.

If the file has been saved, it returns the name with the file extension, else it simply gives the name.

The above has one issue though.

If the file name changes, it wouldn’t automatically update. Normally a function refreshes whenever there is a change in the input arguments. But since there are no arguments in this function, the function doesn’t recalculate (even if you change the name of the workbook, close it and then reopen again).

If you want, you can force a recalculation by using the keyboard shortcut – Control + Alt + F9.

To make the formula recalculate whenever there is a change in the worksheet, you need to a line of code to it.

The below code makes the function recalculate whenever there is a change in the worksheet (just like other similar worksheet functions such as TODAY or RAND function).

Function WorkbookName() As String
Application.Volatile True
WorkbookName = ThisWorkbook.Name
End Function

Now, if you change the workbook name, this function would update whenever there is any change in the worksheet or when you reopen this workbook.

### Creating a Function in VBA with One Argument

In one of the sections above, we have already seen how to create a function that takes only one argument (the GetNumeric function covered above).

Let’s create another simple function that takes only one argument.

Function created with the below code would convert the referenced text into uppercase. Now we already have a function for it in Excel, and this function is just to show you how it works. If you have to do this, it’s better to use the inbuilt [UPPER function](https://trumpexcel.com/excel-upper-function/)
.

Function ConvertToUpperCase(CellRef As Range)
ConvertToUpperCase = UCase(CellRef)
End Function

This function uses the UCase function in VBA to change the value of the CellRef variable. It then assigns the value to the function ConvertToUpperCase.

Since this function takes an argument, we don’t need to use the Application.Volatile part here. As soon as the argument changes, the function would automatically update.

### Creating a Function in VBA with Multiple Arguments

Just like worksheet functions, you can create functions in VBA that takes multiple arguments.

The below code would create a function that will extract the text before the specified delimiter. It takes two arguments – the cell reference that has the text string, and the delimiter.

Function GetDataBeforeDelimiter(CellRef As Range, Delim As String) as String
Dim Result As String
Dim DelimPosition As Integer
DelimPosition = InStr(1, CellRef, Delim, vbBinaryCompare) - 1
Result = Left(CellRef, DelimPosition)
GetDataBeforeDelimiter = Result
End Function

When you need to use more than one argument in a user-defined function, you can have all the arguments in the parenthesis, separated by a comma.

Note that for each argument, you can [specify a data type](https://trumpexcel.com/vba-data-types-variables-constants/)
. In the above example, ‘CellRef’ has been declared as a range datatype and ‘Delim’ has been declared as a String data type. If you don’t specify any data type, VBA considers these are a variant data type.

When you use the above function in the worksheet, you need to give the cell reference that has the text as the first argument and the delimiter character(s) in double quotes as the second argument.

It then checks for the position of the delimiter using the [INSTR function in VBA](https://trumpexcel.com/excel-vba-instr/)
. This position is then used to extract all the characters before the delimiter (using the LEFT function).

Finally, it assigns the result to the function.

This formula is far from perfect. For example, if you enter a delimiter that is not found in the text, it would give an error. Now you can use the [IFERROR function](https://trumpexcel.com/excel-iferror-function/)
 in the worksheet to [get rid of the errors](https://trumpexcel.com/vba-error-handling/)
, or you can use the below code that returns the entire text when it can’t find the delimiter.

Function GetDataBeforeDelimiter(CellRef As Range, Delim As String) as String
Dim Result As String
Dim DelimPosition As Integer
DelimPosition = InStr(1, CellRef, Delim, vbBinaryCompare) - 1
If DelimPosition < 0 Then DelimPosition = Len(CellRef)
Result = Left(CellRef, DelimPosition)
GetDataBeforeDelimiter = Result
End Function

We can further optimize this function.

If you enter the text (from which you want to extract the part before the delimiter) directly in the function, it would give you an error. Go ahead.. try it!

This happens as we have specified the ‘CellRef’ as a range data type.

Or, if you want the delimiter to be in a cell and use the cell reference instead of hard coding it in the formula, you can’t do that with the above code. It’s because the Delim has been declared as a string datatype.

If you want the function to have the flexibility to accept direct text input or cell references from the user, you need to remove the data type declaration. This would end up making the argument as a variant data type, which can take any type of argument and process it.

The below code would do this:

Function GetDataBeforeDelimiter(CellRef, Delim) As String
Dim Result As String
Dim DelimPosition As Integer
DelimPosition = InStr(1, CellRef, Delim, vbBinaryCompare) - 1
If DelimPosition < 0 Then DelimPosition = Len(CellRef)
Result = Left(CellRef, DelimPosition)
GetDataBeforeDelimiter = Result
End Function

### Creating a Function in VBA with Optional Arguments

There are many functions in Excel where some of the arguments are optional.

For example, the legendary [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
 has 3 mandatory arguments and one optional argument.

![Optional Argument in the VLOOKUP function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20117'%3E%3C/svg%3E)

An optional argument, as the name suggests, is optional to specify. If you don’t specify one of the mandatory arguments, your function is going to give you an error, but if you don’t specify the optional argument, your function would work.

But optional arguments are not useless. They allow you to choose from a range of options.

For example, in the VLOOKUP function, if you don’t specify the fourth argument, VLOOKUP does an approximate lookup and if you specify the last argument as FALSE (or 0), then it does an exact match.

Remember that the optional arguments must always come after all the required arguments. You can’t have optional arguments at the beginning.

Now let’s see how to create a function in VBA with optional arguments.

#### Function with Only an Optional Argument

As far as I know, there is no inbuilt function that takes optional arguments only (I can be wrong here, but I can’t think of any such function).

But we can create one with VBA.

Below is the code of the function that will give you the current date in the dd-mm-yyyy format if you don’t enter any argument (i.e. leave it blank), and in “dd mmmm, yyyy” format if you enter anything as the argument (i.e., anything so that the argument is not blank).

Function CurrDate(Optional fmt As Variant)
Dim Result
If IsMissing(fmt) Then
CurrDate = Format(Date, "dd-mm-yyyy")
Else
CurrDate = Format(Date, "dd mmmm, yyyy")
End If
End Function

Note that the above function uses ‘IsMissing’ to check whether the argument is missing or not. To use the IsMissing function, your optional argument must be of the variant data type.

The above function works no matter what you enter as the argument. In the code, we only check if the optional argument is supplied or not.

You can make this more robust by taking only specific values as arguments and showing an error in rest of the cases (as shown in the below code).

Function CurrDate(Optional fmt As Variant)
Dim Result
If IsMissing(fmt) Then
CurrDate = Format(Date, "dd-mm-yyyy")
ElseIf fmt = 1 Then
CurrDate = Format(Date, "dd mmmm, yyyy")
Else
CurrDate = CVErr(xlErrValue)
End If
End Function

The above code creates a function that shows the date in the “dd-mm-yyyy” format if no argument is supplied, and in “dd mmmm,yyyy” format when the argument is 1. It gives an error in all other cases.

#### Function with Required as well as Optional Arguments

We have already seen a code that extracts the numeric part from a string.

Now let’s have a look at a similar example that takes both required as well as optional arguments.

The below code creates a function that extracts the text part from a string. If the optional argument is TRUE, it gives the result in uppercase, and if the optional argument is FALSE or is omitted, it gives the result as is.

Function GetText(CellRef As Range, Optional TextCase = False) As String
Dim StringLength As Integer
Dim Result As String
StringLength = Len(CellRef)
For i = 1 To StringLength
If Not (IsNumeric(Mid(CellRef, i, 1))) Then Result = Result & Mid(CellRef, i, 1)
Next i
If TextCase = True Then Result = UCase(Result)
GetText = Result
End Function

Note that in the above code, we have initialized the value of ‘TextCase’ as False (look within the parenthesis in the first line).

By doing this, we have ensured that the optional argument starts with the default value, which is FALSE. If the user specifies the value as TRUE, the function returns the text in upper case, and if the user specifies the optional argument as FALSE or omits it, then the text returned is as is.

### Creating a Function in VBA with an Array as the Argument

So far we have seen examples of creating a function with Optional/Required arguments – where these arguments were a single value.

You can also create a function that can take an array as the argument. In Excel worksheet functions, there are many functions that take array arguments, such as SUM, VLOOKUP, SUMIF, COUNTIF, etc.

Below is the code that creates a function that gives the sum of all the even numbers in the specified range of the cells.

Function AddEven(CellRef as Range)
 Dim Cell As Range
 For Each Cell In CellRef
 If IsNumeric(Cell.Value) Then
 If Cell.Value Mod 2 = 0 Then
 Result = Result + Cell.Value
 End If
 End If
 Next Cell
 AddEven = Result
 End Function

You can use this function in the worksheet and provide the range of cells that have the numbers as the argument. The function would return a single value – the sum of all the even numbers (as shown below).

![Creating a User Defined Function with an array argument](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20325'%3E%3C/svg%3E)

In the above function, instead of a single value, we have supplied an array (A1:A10). For this to work, you need to make sure your data type of the argument can accept an array.

In the code above, I specified the argument CellRef as Range (which can take an array as the input). You can also use the variant data type here.

In the code, there is a [For Each loop](https://trumpexcel.com/vba-loops/)
 that goes through each cell and checks if it’s a number of not. If it isn’t, nothing happens and it moves to the next cell. If it’s a number, it checks if it’s even or not (by using the MOD function).

In the end, all the even numbers are added and teh sum is assigned back to the function.

### Creating a Function with Indefinite Number of Arguments

While creating some functions in VBA, you may not know the exact number of arguments that a user wants to supply. So the need is to create a function that can accept as many arguments are supplied and use these to return the result.

An example of such worksheet function is the [SUM function](https://trumpexcel.com/excel-sum-function/)
. You can supply multiple arguments to it (such as this):

\=SUM(A1,A2:A4,B1:B20)

The above function would add the values in all these arguments. Also, note that these can be a single cell or an array of cells.

You can create such a function in VBA by having the last argument (or it could be the only argument) as optional. Also, this optional argument should be preceded by the keyword ‘ParamArray’.

‘ParamArray’ is a modifier that allows you to accept as many arguments as you want. Note that using the word ParamArray before an argument makes the argument optional. However, you don’t need to use the word Optional here.

Now let’s create a function that can accept an arbitrary number of arguments and would add all the numbers in the specified arguments:

Function AddArguments(ParamArray arglist() As Variant)
For Each arg In arglist
AddArguments = AddArguments + arg
Next arg
End Function

The above function can take any number of arguments and add these arguments to give the result.

![Function with paramarray](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%2094'%3E%3C/svg%3E)

Note that you can only use a single value, a cell reference, a boolean, or an expression as the argument. You can not supply an array as the argument. For example, if one of your arguments is D8:D10, this formula would give you an error.

If you want to be able to use both multi-cell arguments you need to use the below code:

Function AddArguments(ParamArray arglist() As Variant)
For Each arg In arglist
For Each Cell In arg
AddArguments = AddArguments + Cell
Next Cell
Next arg
End Function

Note that this formula works with multiple cells and array references, however, it can not process hardcoded values or expressions. You can create a more robust function by checking and treating these conditions, but that’s not the intent here.

The intent here is to show you how ParamArray works so you can allow an indefinite number of arguments in the function. In case you want a better function than the one created by the above code, use the SUM function in the worksheet.

Creating a Function that Returns an Array
-----------------------------------------

So far we have seen functions that return a single value.

With VBA, you can create a function that returns a variant that can contain an entire array of values.

Array formulas are also available as inbuilt functions in Excel worksheets. If you’re familiar with array formulas in Excel, you would know that these are entered using Control + Shift + Enter (instead of just the Enter). You can read more about [array formulas here](https://support.office.com/en-us/article/guidelines-and-examples-of-array-formulas-7d94a64e-3ff3-4686-9372-ecfd5caa57c7)
. If you don’t know about array formulas, don’t worry, keep reading.

Let’s create a formula that returns an array of three numbers (1,2,3).

The below code would do this.

Function ThreeNumbers() As Variant
Dim NumberValue(1 To 3)
NumberValue(1) = 1
NumberValue(2) = 2
NumberValue(3) = 3
ThreeNumbers = NumberValue
End Function

In the above code, we have specified the ‘ThreeNumbers’ function as a variant. This allows it to hold an array of values.

The variable ‘NumberValue’ is declared as an array with 3 elements. It holds the three values and assigns it to the ‘ThreeNumbers’ function.

You can use this function in the worksheet by entering the function and hitting the Control + Shift + Enter key (hold the Control and the Shift keys and then press Enter).

![Creating a function in VBA that returns an array](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20459%20131'%3E%3C/svg%3E)

When you do this, it will return 1 in the cell, but in reality, it holds all the three values. To check this, use the below formula:

\=MAX(ThreeNumbers())

Use the above function with Control + Shift + Enter. You will notice that the result is now 3, as it is the largest values in the array returned by the [Max function](https://trumpexcel.com/excel-max-function/)
, which gets the three numbers as the result of our user-defined function – ThreeNumbers.

You can use the same technique to create a function that returns an array of Month Names as shown by the below code:

Function Months() As Variant
Dim MonthName(1 To 12)
MonthName(1) = "January"
MonthName(2) = "February"
MonthName(3) = "March"
MonthName(4) = "April"
MonthName(5) = "May"
MonthName(6) = "June"
MonthName(7) = "July"
MonthName(8) = "August"
MonthName(9) = "September"
MonthName(10) = "October"
MonthName(11) = "November"
MonthName(12) = "December"
Months = MonthName
End Function

Now when you enter the function =Months() in Excel worksheet and use Control + Shift + Enter, it will return the entire array of [month names](https://trumpexcel.com/get-month-name-from-date-excel/)
. Note that you see only January in the cell as that is the first value in the array. This does not mean that the array is only returning one value.

![Creating a function in VBA that returns an array of month names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20449%20173'%3E%3C/svg%3E)

To show you the fact that it is returning all the values, do this – select the cell with the formula, go to the formula bar, select the entire formula and press F9. This will show you all the values that the function returns.

![Array formula in VBA - All contents with F9](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20950%2063'%3E%3C/svg%3E)

You can use this by using the below [INDEX formula](https://trumpexcel.com/excel-index-function/)
 to get a list of all the month names in one go.

\=INDEX(Months(),ROW())

![Array formula in VBA - with Index Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20369'%3E%3C/svg%3E)

Now if you have a lot of values, it’s not a good practice to assign these values one by one (as we have done above). Instead, you can use the Array function in VBA.

So the same code where we create the ‘Months’ function would become shorter as shown below:

Function Months() As Variant
Months = Array("January", "February", "March", "April", "May", "June", \_
"July", "August", "September", "October", "November", "December")
End Function

The above function uses the Array function to assign the values directly to the function.

Note that all the functions created above return a horizontal array of values. This means that if you select 12 horizontal cells (let’s say A1:L1), and enter the =Months() formula in cell A1, it will give you all the month names.

![Months names in horizontal cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%2089'%3E%3C/svg%3E)

But what if you want these values in a vertical range of cells.

You can do this by using the [TRANSPOSE formula](https://trumpexcel.com/transpose-data-excel/)
 in the worksheet.

Simply select 12 vertical cells (contiguous), and enter the below formula.

![getting a vertical array of values from a VBA function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20504%20376'%3E%3C/svg%3E)

Understanding the Scope of a User Defined Function in Excel
-----------------------------------------------------------

A function can have two scopes – _Public_ or _Private_.

*   A **Public scope** means that the function is available for all the sheets in the workbook as well as all the procedures (Sub and Function) across all modules in the workbook. This is useful when you want to call a function from a subroutine (we will see how this is done in the next section).
*   A **Private scope** means that the function is available only in the module in which it exists. You can’t use it in other modules. You also won’t see it in the list of functions in the worksheet. For example, if your Function name is ‘Months()’, and you type function in Excel (after the = sign), it will not show you the function name. You can, however, still, use it if you enter the formula name.

If you don’t specify anything, the function is a Public function by default.

Below is a function that is a Private function:

Private Function WorkbookName() As String
WorkbookName = ThisWorkbook.Name
End Function

You can use this function in the subroutines and the procedures in the same modules, but can’t use it in other modules. This function would also not show up in the worksheet.

The below code would make this function Public. It will also show up in the worksheet.

Function WorkbookName() As String
WorkbookName = ThisWorkbook.Name
End Function

Different Ways of Using a User Defined Function in Excel
--------------------------------------------------------

Once you have created a user-defined function in VBA, you can use it in many different ways.

Let’s first cover how to use the functions in the worksheet.

### Using UDFs in Worksheets

We have already seen examples of using a function created in VBA in the worksheet.

All you need to do is enter the functions name, and it shows up in the intellisense.

![Public VBA function used in Worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20285%20186'%3E%3C/svg%3E)

Note that for the function to show up in the worksheet, it must be a Public function (as explained in the section above).

You can also use the Insert Function dialog box to insert the user defined function (using the steps below). This would work only for functions that are Public.

*   Go to the Data tab.
*   Click the ‘Insert Function’ option.![Insert Function option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20434%20195'%3E%3C/svg%3E)
*   In the Insert Function dialog box, select User Defined as the category. This option shows up only when you have a function in the VB Editor (and the function is Public).![Insert User Defined Function in Worksheet - dilaog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20475'%3E%3C/svg%3E)
*   Select the function from the list of all the Public User Defined functions.
*   Click the Ok button.

The above steps would insert the function in the worksheet. It also displays a Function Arguments dialog box that will give you details on the arguments and the result.

![Information dialog box when you insert the Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20200'%3E%3C/svg%3E)

You can use a user defined function just like any other function in Excel. This also means that you can use it with other inbuilt Excel functions. For example. the below formula would give the name of the workbook in upper case:

_\=UPPER(WorkbookName())_

### Using User Defined Functions in VBA Procedures and Functions

When you have created a function, you can use it in other sub-procedures as well.

If the function is Public, it can be used in any procedure in the same or different module. If it’s Private, it can only be used in the same module.

Below is a function that returns the name of the workbook.

Function WorkbookName() As String 
WorkbookName = ThisWorkbook.Name 
End Function

The below procedure call the function and then display the name in a message box.

Sub ShowWorkbookName()
MsgBox WorkbookName
End Sub

You can also call a function from another function.

In the below codes, the first code returns the name of the workbook, and the second one returns the name in uppercase by calling the first function.

Function WorkbookName() As String
WorkbookName = ThisWorkbook.Name
End Function

Function WorkbookNameinUpper()
WorkbookNameinUpper = UCase(WorkbookName)
End Function

### Calling a User Defined Function from Other Workbooks

If you have a function in a workbook, you can call this function in other workbooks as well.

There are multiple ways to do this:

1.  Creating an Add-in
2.  Saving function in the Personal Macro Workbook
3.  Referencing the function from another workbook.

#### Creating an Add-in

By [creating and installing an add-in](https://trumpexcel.com/excel-add-in/)
, you will have the custom function in it available in all the workbooks.

Suppose you have created a custom function – ‘GetNumeric’ and you want it in all the workbooks. To do this, create a new workbook and have the function code in a module in this new workbook.

Now follow the steps below to save it as an add-in and then install it in Excel.

*   Go to the File tab and click on Save As.![Create an Excel Add-in - Save as](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%20284'%3E%3C/svg%3E)
*   In the Save As dialogue box, change the ‘Save as’ type to .xlam. The name you assign to the file would be the name of your add-in. In this example, the file is saved with the name GetNumeric.
    *   You’ll notice that the path of the file where it gets saved automatically changes. You can use the default one or change it if you want.![Create an Excel Add-in - Save as drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20515'%3E%3C/svg%3E)
*   Open a new Excel workbook and Go to the Developer tab.
*   Click the Excel Add-ins option.![Create an Excel Add-in - add-in](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20133'%3E%3C/svg%3E)
*   In the Add-ins dialogue box, browse and locate the file that you saved, and click OK.![installing the addin to get function in all workbooks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20495'%3E%3C/svg%3E)

Now the add-in has been activated.

Now you can use the custom function in all the workbooks.

#### Saving the Function in Personal Macro Workbook

A Personal Macro Workbook is a hidden workbook in your system that opens whenever you open the Excel application.

It’s a place where you can store macro codes and then access these macros from any workbook. It’s a great place to store those macros that you want to use often.

By default, there is no personal macro workbook in your Excel. You need to create it by recording a macro and saving it in the Personal macro workbook.

You can find the detailed steps on how to create and save macros in [the personal macro workbook here](https://trumpexcel.com/personal-macro-workbook/)
.

#### Referencing the function from another workbook

While the first two methods (creating an add-in and using personal macro workbook) would work in all situations, if you want to reference the function from another workbook, that workbook needs to be open.

Suppose you have a workbook with the name ‘_Workbook with Formula’_, and it has the function with the name ‘_GetNumeric’_.

To use this function in another workbook (while the _Workbook with Formula_ is open), you can use the below formula:

\=’Workbook with Formula’!GetNumeric(A1)

The above formula will use the user defined function in the _Workbook with Formula_ file and give you the result.

Note that since the workbook name has spaces, you need to enclose it in single quotes.

Using Exit Function Statement VBA
---------------------------------

If you want to exit a function while the code is running, you can do that by using the ‘Exit Function’ statement.

The below code would extract the first three numeric characters from an alphanumeric text string. As soon as it gets the three characters, the function ends and returns the result.

Function GetNumericFirstThree(CellRef As Range) As Long
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If J = 3 Then Exit Function
If IsNumeric(Mid(CellRef, i, 1)) Then
J = J + 1
Result = Result & Mid(CellRef, i, 1)
GetNumericFirstThree = Result
End If
Next i
End Function

The above function checks for the number of characters that are numeric, and when it gets 3 numeric characters, it Exits the function in the next loop.

Debugging a User Defined Function
---------------------------------

There are a few techniques you can use while debugging a user-defined function in VBA:

**Debugging a Custom Function by Using the Message Box**

Use [MsgBox function](https://trumpexcel.com/vba-msgbox/)
 to show a message box with a specific value.

The value you display can be based on what you want to test. For example, if you want to check if the code is getting executed or not, any message would work, and if you want to check whether the loops are working or not, you can display a specific value or the loop counter.

**Debugging a Custom Function by  Setting the Breakpoint**

Set a breakpoint to be able to go step through each line one at a time. To set a breakpoint, select the line where you want it and press F9, or click on the gray vertical area which is left to the code lines. Any of these methods would insert a breakpoint (you will see a red dot in the gray area).

![Setting the breakpoint](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20596%20274'%3E%3C/svg%3E)

Once you have set the breakpoint and you execute the function, it goes till the breakpoint line and then stops. Now you can step through the code using the F8 key. Pressing F8 once moves to the next line in the code.

**Debugging a Custom Function by Using Debug.Print in the Code**

You can use Debug.Print statement in your code to get the values of the specified variables/arguments in the [immediate window](https://trumpexcel.com/vba-immediate-window/)
.

For example, in the below code, I have used Debug.Print to get the value of two variables – ‘j’ and ‘Result’

Function GetNumericFirstThree(CellRef As Range) As Long
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If J = 3 Then Exit Function
If IsNumeric(Mid(CellRef, i, 1)) Then
 J = J + 1
 Result = Result & Mid(CellRef, i, 1)
 Debug.Print J, Result
 GetNumericFirstThree = Result
End If
Next i
End Function

When this code is executed, it shows the following in the immediate window.

![Immediate Window result when creating a custom function in VBA Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20249%20121'%3E%3C/svg%3E)

Excel Inbuilt Functions Vs. VBA User Defined Function
-----------------------------------------------------

There are few strong benefits of using Excel in-built functions over custom functions created in VBA.

*   Inbuilt functions are a lot faster than the VBA functions.
*   When you create a report/dashboard using VBA functions, and you send it to a client/colleague, they wouldn’t have to worry about whether the macros are enabled or not. In some cases, clients/customers get scared by seeing a warning in the yellow bar (which simply asks them to enable macros).
*   With inbuilt Excel functions, you don’t need to worry about file extensions. If you have macros or user-defined functions in the workbook, you need to save it in .xlsm.

While there are many strong reasons to use Excel in-built functions, in a few cases, you’re better off using a user-defined function.

*   It’s better to use a user-defined function if your inbuilt formula is huge and complicated. This becomes even more relevant when you need someone else to update the formulas. For example, if you have a huge formula made up of many different functions, even changing a reference to a cell can be tedious and error-prone. Instead, you can create a custom function that only takes one or two arguments and does all the heavy lifting the backend.
*   When you have to get something done that can not be done by Excel inbuilt functions. An example of this can be when you want to extract all the numeric characters from a string. In such cases, the benefit of using a user-defined function gar outweighs its negatives.

Where to put the VBA Code for a User-Defined Function
-----------------------------------------------------

When creating a custom function, you need to put the code in the code window for the workbook in which you want the function.

Below are the steps to put the code for the ‘GetNumeric’ function in the workbook.

1.  Go to the Developer tab.![IF Then Else in Excel VBA - Developer Tab in ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
2.  Click on the Visual Basic option. This will open the VB editor in the backend.![Click on Visual Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
3.  In the Project Explorer pane in the VB Editor, right-click on any object for the workbook in which you want to insert the code. If you don’t see the Project Explorer go to the View tab and click on Project Explorer.
4.  Go to Insert and click on Module. This will insert a module object for your workbook.![Saving a Custom Function code in the module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20497%20420'%3E%3C/svg%3E)
5.  Copy and paste the code in the module window.![User Defined function in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20790%20227'%3E%3C/svg%3E)

**You May Also Like the Following Excel VBA Tutorials:**

*   [Working with Cells and Ranges in Excel VBA](https://trumpexcel.com/vba-ranges/)
    .
*   [Working with Worksheets in Excel VBA](https://trumpexcel.com/vba-worksheets/)
    .
*   [Working with Workbooks using VBA](https://trumpexcel.com/vba-workbook/)
    .
*   [How to use Loops in Excel VBA](https://trumpexcel.com/vba-loops/)
    .
*   [Excel VBA Events – An Easy (and Complete) Guide](https://trumpexcel.com/vba-events/)
    
*   [Using IF Then Else Statements in VBA](https://trumpexcel.com/if-then-else-vba/)
    .
*   [How to Record a Macro in Excel](https://trumpexcel.com/record-macro-vba/)
    .
*   [How to Run a Macro in Excel](https://trumpexcel.com/run-a-macro-excel/)
    .
*   [How to Sort Data in Excel using VBA (A Step-by-Step Guide)](https://trumpexcel.com/sort-data-vba/)
    .
*   [Excel VBA InStr Function &#8211; Explained with Examples](https://trumpexcel.com/excel-vba-instr/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

11 thoughts on “Creating a User Defined Function (UDF) in Excel VBA \[Ultimate Guide\]”
---------------------------------------------------------------------------------------

1.  Very Helpfull and thorough.
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-33200)
    
2.  Excellent and user-friendly teaching on vba
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-14632)
    
3.  Very clear explanations. Is there any way to add a help instruction to the new UDF, whether as an Add-in or module code, e.g. as per “Get help on is function” in the Insert Function dialogue box? Similar comments already posted, with no response
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-14117)
    
4.  Thanks.  
    It has helped knowing I can create UDF that makes an array
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-12994)
    
5.  Really thorough explanation, thanks.
    
    Would also love to see how this can be added to a function, for example in a command like:
    
    Worksheets(“4k”).Range(“C6”).Value = Worksheets(“testresults”).Range(“B19”).Value
    
    Does it go before Worksheets, or after?
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-12568)
    
6.  Thank you very much 🙂
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-12533)
    
7.  Book gives me
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-12025)
    
8.  Very comprehensive article.tanx
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-11789)
    
9.  Very comprehensive article, the best I found but you missed one thing. The documentation.  
    Example: See when you write the VLOOKUP and you arrive to the last optional argument. It tells you if you select TRUE is approximate match, FALSE is exact match.
    
    How cna I do that in my custom function??????
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-10457)
    
    *   This is what I’m looking for also.
        
        [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-12891)
        
10.  Thanks for the Article – I have a quick question – I want to write a function similar to say SUM function –
    
    Meaning function can take same function as argument (recursively) – like this
    
    mysum(10, mysum(20, mysum(30,40)))
    
    should return 100
    
    How can implement such?
    
    Can you please support.
    
    Thanks,  
    Tushar
    
    [Reply](https://trumpexcel.com/user-defined-function-vba/#comment-10206)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/user-defined-function-vba/#respond)

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