# Excel VBA Split Function - Explained with Examples

**Source:** https://trumpexcel.com/vba-split-function

---

[Skip to content](https://trumpexcel.com/vba-split-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-split-function/#below-title)

When working with VBA in Excel, you may have a need to split a string into different parts based on a delimiter.

For example, if you have an address, you can use the VBA Split function to get different parts of the address that are separated by a comma (which would be the delimiter in this case).

SPLIT is an inbuilt string function in Excel VBA that you can use to split a text string based on the delimiter.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-split-function/#)

Excel VBA SPLIT Function – Syntax
---------------------------------

Split ( Expression, \[Delimiter\], \[Limit\], \[Compare\] )

*   **Expression:** This is the string that you want to split based on the delimiter. For example, in case of the address example, the entire address would be the ‘expression’. In case this is a zero-length string (“”) SPLIT function would return an empty array.
*   **Delimiter:** This is an optional argument. This is the delimiter that is used to split the ‘Expression’ argument. In case of our address example, a comma is a delimiter that is used to split the address into different parts. If you don’t specify this argument, a space character is considered the default delimiter. In case you give a zero-length string (“”), the entire ‘Expression’ string is returned by the function.
*   **Limit:** This is an optional argument. Here you specify the total number of substrings that you want to return. For example, if you only want to return the first three substrings from the ‘Expression’ argument, this would be 3. If you don’t specify this argument, the default is -1, which returns all the substrings.
*   **Compare:** This is an optional argument. Here you specify the type of comparison you want the SPLIT function to perform when evaluating the substrings. The following options are available:
    *   **When Compare is 0**: This is a Binary comparison. This means that if your delimiter is a text string (let’s say ABC), then this would be case-sensitive. ‘ABC’ would not be equal to ‘abc’.
    *   **When Compare is 1**: This is a Text comparison. This means that if your delimiter is a text string (let’s say ABC), then even if you have ‘abc’ in the ‘Expression’ string, it would be considered as a delimiter.

Now that we have covered the basics of the SPLIT function, let’s see a few practical examples.

### Example 1 – Split the Words in a Sentence

Suppose I have the text – “The Quick Brown Fox Jumps Over The Lazy Dog”.

I can use the SPLIT function to get each word of this sentence into as a separate item in an array.

The below code would to this:

Sub SplitWords()
Dim TextStrng As String
Dim Result() As String
TextStrng = "The Quick Brown Fox Jumps Over The Lazy Dog"
Result() = Split(TextStrng)
End Sub

While the code does nothing useful, it will help you understand what the Split function in VBA does.

Split function splits the text string and assigns each word to the Result array.

So in this case:

*   Result(0) stores the value “The”
*   Result(1) stores the value “Quick”
*   Result(2) stores the value “Brown” and so on.

In this example, we have only specified the first argument – which is the text to be split. Since no delimiter has been specified, it takes space character as the default delimiter.

**Important Note:**

1.  VBA SPLIT function returns an array that starts from base 0.
2.  When the result of the SPLIT function is assigned to an array, that array must be declared as a String data type. If you declare it as a Variant data type, it will show a type mismatch error).  In the example above, note that I have declared Result() as a String data type.

Also read: [Split Text into Different Rows in Excel](https://trumpexcel.com/split-text-to-rows-excel/)

### Example 2 – Count the Number of Words in a Sentence

You can use the SPLIT function to get the total number of words in a sentence. The trick here is to count the number of elements in the array that you get when you split the text.

The below code would show a [message box](https://trumpexcel.com/vba-msgbox/)
 with the word count:

Sub WordCount()
Dim TextStrng As String
Dim WordCount As Integer
Dim Result() As String
TextStrng = "The Quick Brown Fox Jumps Over The Lazy Dog"
Result = Split(TextStrng)
WordCount = UBound(Result()) + 1
MsgBox "The Word Count is " & WordCount
End Sub

![VBA Split Function - Getting the Word Count message](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20184%20186'%3E%3C/svg%3E)

In this case, the UBound function tells us the upper bound of the array (i.e., the maximum number of elements the array has). Since the base of the array is 0, 1 is added to get the total word count.

You can use a similar code to create a custom function in VBA that will take the text as input and return the word count.

The below code will create this function:

Function WordCount(CellRef As Range)
Dim TextStrng As String
Dim Result() As String
Result = Split(WorksheetFunction.Trim(CellRef.Text), " ")
WordCount = UBound(Result()) + 1
End Function

Once created, you can use the WordCount function just like any other regular function.

![VBA Split Function - word count formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20713%20138'%3E%3C/svg%3E)

This function also handles leading, trailing and double spaces in between words. This has been made possible by using the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 in the VBA code.

In case you want to learn more about how this formula works to count the number of words in a sentence or want to learn about a non-VBA formula way to get the word count, [check out this tutorial](https://trumpexcel.com/word-count-in-excel/)
.

### Example 3 – Using a Delimiter Other than Space Character

In the previous two examples, we have only used one argument in the SPLIT function, and the rest were the default arguments.

When you use some other delimiter, you need to specify that in the SPLIT formula.

In the below code, the SPLIT function returns an array based on a comma as the delimiter, and then shows a message with each word in a separate line.

Sub CommaSeparator()
Dim TextStrng As String
Dim Result() As String
Dim DisplayText As String
TextStrng = "The,Quick,Brown,Fox,Jump,Over,The,Lazy,Dog"
Result = Split(TextStrng, ",")
For i = LBound(Result()) To UBound(Result())
DisplayText = DisplayText & Result(i) & vbNewLine
Next i
MsgBox DisplayText
End Sub

![VBA Split Function - comma delimiter separate line](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%20338'%3E%3C/svg%3E)

In the above code, I have used the [For Next loop](https://trumpexcel.com/vba-loops/)
 to go through each element of the ‘Result’ array assign it to the ‘DisplayText’ variable.

### Example 4 – Divide an Address into three parts

With the SPLIT function, you can specify how many numbers of splits you want to get. For example, if I don’t specify anything, every instance of the delimiter would be used to split the string.

But if I specify 3 as the limit, then the string will be split into three parts only.

For example, if I have the following address:

_2703 Winifred Way, Indianapolis, Indiana, 46204_

I can use the Split function in VBA to divide this address into three parts.

![VBA Split Function - Specifying number of elements](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20698%2086'%3E%3C/svg%3E)

It splits the first two based on the comma delimiter and remaining part becomes the third element of the array.

The below code would show the address in three different lines in a message box:

Sub CommaSeparator()
Dim TextStrng As String
Dim Result() As String
Dim DisplayText As String
TextStrng = "2703 Winifred Way, Indianapolis, Indiana, 46204"
Result = Split(TextStrng, ",", 3)
For i = LBound(Result()) To UBound(Result())
DisplayText = DisplayText & Result(i) & vbNewLine
Next i
MsgBox DisplayText
End Sub

![Resulting Address in separate lines in a message box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20176%20223'%3E%3C/svg%3E)

One of the practical uses of this could be when you want to divide a single line address into the format shown in the message box. Then you can create a custom function that returns the address divided into three parts (with each part in a new line).

The following code would do this:

Function ThreePartAddress(cellRef As Range)
Dim TextStrng As String
Dim Result() As String
Dim DisplayText As String
Result = Split(cellRef, ",", 3)
For i = LBound(Result()) To UBound(Result())
DisplayText = DisplayText & Trim(Result(i)) & vbNewLine
Next i
ThreePartAddress = Mid(DisplayText, 1, Len(DisplayText) - 1)
End Function

Once you have this code in the module, you can use the function (ThreePartAddress) in the workbook just like any other Excel function.

![Split Function in VBA- address in separate lines formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20755%20371'%3E%3C/svg%3E)

This function takes one argument – the cell reference that has the address.

Note that for the resulting address to appear in three different lines, you need to apply the wrap text format to the cells (it’s in the Home tab in the Alignment group). If the ‘Wrap Text’ format is not enabled, you’ll see the entire address as one single line.

### Example 5 – Get the City Name from the Address

With Split function in VBA, you can specify what part of the resulting array you want to use.

For example, suppose I am splitting the following address based on the comma as the delimiter:

2703 Winifred Way, Indianapolis, Indiana, 46204

The resulting array would look something as shown below:

{"2703 Winifred Way", "Indianapolis", "Indiana", "46204"}

Since this is an array, I can choose to display or return a specific part of this array.

Below is a code for a custom function, where you can specify a number and it will return that element from the array. For example, if I want the state name, I can specify 3 (as it’s the third element in the array).

Function ReturnNthElement(CellRef As Range, ElementNumber As Integer)
Dim Result() As String
Result = Split(CellRef, ",")
ReturnNthElement = Result(ElementNumber - 1)
End Function

The above function takes two arguments, the cell reference that has the address and the element number you want to return. The Split function splits the address elements and assigns it to the Result variable.

Then it returns the element number that you specified as the second argument. Note that since the base is 0, ElementNumber-1 is used to return the correct part of the address.

![VBA Split Function - address element by number](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20663%20230'%3E%3C/svg%3E)

This custom formula is best suited when you have a consistent format in all the address – i.e., the city is always mentioned after the two commas. If the data is not consistent, you’ll not get the desired result.

In case you want the city name, you can use 2 as the second argument. In case you use a number that is higher than the total number of elements, it would return the #VALUE! error.

You can further simplify the code as shown below:

Function ReturnNthElement(CellRef As Range, ElementNumber As Integer)
ReturnNthElement = Split(CellRef, ",")(ElementNumber - 1)
End Function

In the above code, instead of using the Result variable, it only returns the specified element number.

So if you have Split(“Good Morning”)(0), it would only return the first element, which is “Good”.

Similarly, in the above code, it only returns the specified element number.

**You May Also Like the Following Excel Tutorials:**

*   [Excel VBA InStr Function – Explained with Examples.](https://trumpexcel.com/excel-vba-instr/)
    
*   [How to Sort Data in Excel using VBA (A Step-by-Step Guide)](https://trumpexcel.com/sort-data-vba/)
    .
*   [7 Amazing Things Excel Text to Columns Can Do For You](https://trumpexcel.com/excel-text-to-columns-examples/)
    .
*   [How to Get the Word Count in Excel](https://trumpexcel.com/word-count-in-excel/)
    .
*   [VBA TRIM Function](https://trumpexcel.com/vba-trim/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “Excel VBA Split Function – Explained with Examples”
------------------------------------------------------------------

1.  This is just not true!!!Split function does not exist!!!  
    It returns “wrong number of arguments or invalid property assignment” !
    
    so…
    
    [Reply](https://trumpexcel.com/vba-split-function/#comment-37682)
    
2.  Name&Mark Name1 Mark Name2 Mark Name3 Mark  
    john:60,max:50,jeni:75 john 60 max 50 jeni 75  
    Need to split like this above can you help me guys pls.
    
    [Reply](https://trumpexcel.com/vba-split-function/#comment-13107)
    
3.  I can’t get example threepartaddress to work. I would like to use it to place address into three separate cells.
    
    [Reply](https://trumpexcel.com/vba-split-function/#comment-11625)
    
    *   You need to apply the wrap text format on the cell to make it appear in three different lines in the same cell
        
        [Reply](https://trumpexcel.com/vba-split-function/#comment-11924)
        
    *   Sub Separate\_cells()
        
        Dim TextStrng As String
        
        Dim Result() As String
        
        Dim n As Integer ‘ n number of rows.
        
        For n = 2 To 10 ‘ 2 because of the header.
        
        TextStrng = Cells(n, 1).Value ‘ 1 : 1st column.
        
        Result = Split(TextStrng, “,”)
        
        For i = LBound(Result()) To UBound(Result())
        
        Cells(n, 2 + i).Value = Result(i) ‘ Each value its placed in ordered cells.
        
        Next i
        
        Next n
        
        End Sub
        
        [Reply](https://trumpexcel.com/vba-split-function/#comment-12543)
        
4.  I’m totally stuck on that example #2 WordCount function.This just doesn’t make any sense to put a hard coded variable TextStrng = “The Quick Brown Fox Jumps Over The Lazy Dog” inside the function. The result will always be 9??? If I run this from a sub and reference an actual vba range like this it works as expected:
    
    Sub testing()  
    Dim result As Integer  
    result = WordCount(Sheet1.Range(“d5”))  
    Debug.Print (result)  
    End Sub
    
    But in an excel sheet formula:
    
    \=WordCount(D5)
    
    results in 0 every time
    
    [Reply](https://trumpexcel.com/vba-split-function/#comment-11347)
    
    *   Just change  
        TextStrng = CellRef.Text
        
        [Reply](https://trumpexcel.com/vba-split-function/#comment-11391)
        
    *   Function WordCount(CellRef As Range)  
        Dim TextStrng As String  
        Dim Result() As String
        
        TextStrng = CellRef.Text  
        ‘——————————————–
        
        Result = Split(TextStrng)  
        WordCount = UBound(Result()) + 1  
        End Function
        
        [Reply](https://trumpexcel.com/vba-split-function/#comment-11392)
        
        *   Horrible miss on my part. I have corrected the code for the formula. Also, have used the TRIM function to make sure it also account for any leading, trailing or double spaces in between words
            
            [Reply](https://trumpexcel.com/vba-split-function/#comment-11925)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-split-function/#respond)

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