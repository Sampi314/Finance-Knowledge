# How to Add Leading Zeroes in Excel - All You Need to Know

**Source:** https://trumpexcel.com/add-leading-zeroes-excel

---

[Skip to content](https://trumpexcel.com/add-leading-zeroes-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-leading-zeroes-excel/#below-title)

There are situations when you need to add leading zeroes to a dataset in Excel. This could be the case if you maintain records in Excel, such as Employee Ids or Transaction Ids.

For example, you may want to get a consistent look in your data set as shown below:

![Add Leading Zeroes in Excel - Transaction Ids](https://trumpexcel.com/wp-content/uploads/2016/10/pasted-image-0-13.png)

In this tutorial, you’ll learn various ways to add leading zeroes in Excel (i.e., add a 0 in front of a number):

*   Converting the Format to Text
*   Using Custom Number Formatting
*   Using Text Function
*   Using REPT/LEN functions
*   Using VBA

Each of these methods has some merits and drawbacks (covered in each section).

Let’s see how each of these works.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-leading-zeroes-excel/#)

Add Leading Zeros by Converting the Format to Text
--------------------------------------------------

**When to Use:** When you have a small numeric data set, and you plan to do this editing manually.

Suppose you have employee Ids of the marketing department as shown below and you want to make these Ids look consistent by adding leading zeroes.

![how-to-add-leading-zeroes-in-excel-employee-ids](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20144%20287'%3E%3C/svg%3E)

So you try and change the id by entering leading zeroes (00001 instead of 1).

But to your amazement, Excel converts it back to 1.

![Add Leading Zeroes in Excel Removes Zeroes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20236%20112'%3E%3C/svg%3E)

This happens as Excel understands that 00001 and 1 are the same numbers and should follow the same display rules.

Now as frustrating as it may be for you, Excel has its reasons.

So, to get the work done without bending Excel rules, you’ll have to take advantage of the fact that this rule doesn’t apply to text formatting.

So here is what you need to do:

1.  Select the cells in which you want to manually add leading zeroes.
2.  Go to Home → Number Group and select Text from the drop-down.

![Add Leading Zeroes in Excel - Select Number Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20168%20384'%3E%3C/svg%3E)

That’s it!

Now, when you enter leading zeroes manually, Excel would readily comply.

_Caution: When you convert the format to Text, some Excel functions will not work properly. For example, SUM/COUNT function would ignore the cell since it’s in the text format._

Add Leading Zeros by Using Custom Number Formatting
---------------------------------------------------

**When to Use**: When you have a numeric dataset, and you want the result to be numeric (not text).

When you display a number in a specific format, it doesn’t change the underlying value of the number. For example, I can display the number 1000 as 1000 or 1,000 or 1000.00 or 001000 or 26-09-1902 (even dates are numbers in the backend in Excel).

In all the different ways to display the number, the value of the number never changes. It’s only the way it’s displayed that is changed.

To add leading zeroes, we can format it to show it that way, while the underlying value would remain unchanged.

Here are the steps to use this technique to add leading zeroes in Excel:

1.  Select the cells in which you want to add leading zeroes.
2.  Go to Home → Number Group and click on the dialog launcher (a small tilted arrow in the bottom right). This will open the Format Cells dialog box. Alternatively, you can also use the keyboard shortcut: Control + 1.![Add Leading Zeroes in Excel - Dialog Box Launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20163%20109'%3E%3C/svg%3E)
3.  In the Format Cells dialog box, within the Number tab, select Custom in the Category list.![Add Leading Zeroes in Excel - Format Cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20535%20468'%3E%3C/svg%3E)
4.  In the Type field, enter 00000![Add Leading Zeroes in Excel - Format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20534%20469'%3E%3C/svg%3E)
5.  Click OK.

Doing this will always display all the numbers as five digits, where leading 0’s are automatically added if the number is less than 5 digits. So 10 would become 00010 and 100 would become 00100.

In this case, we have used six zeroes, but if your data has numbers with more digits, then you need to use the format accordingly.

_Note: This technique would work only for a numeric dataset. In case you have employee ids like A1, A2, A3 and so on, then these are text and would not change when you apply the custom format as shown above._

Add Leading Zeros by Using TEXT Function
----------------------------------------

**When to Use:** When you want the result to be text.

[TEXT](https://trumpexcel.com/excel-text-function/)
 function allows you to change the value to the desired format.

For example, if you want 1 to be displayed as 001, you can use the TEXT function for that.

However, remember that the TEXT function would change the format and make it TEXT. This means that when you make 1 as 001, Excel treats the new result as text with three characters (just like abc or xyz).

Here is how to add leading zeroes using the TEXT function:

1.  If you have the numbers in column A (say from A2:A100), then select B2:B100 and enter the following formula:  
    \=TEXT(A2,”00000″)
2.  Press Control + Enter to apply the formula to all the selected cells.

This will display all the numbers as five digits, where leading 0’s are automatically added if the number is less than 5 digits.

One benefit of converting data into text is that you can now use it in lookup formulas such as [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 or [INDEX](https://trumpexcel.com/excel-index-function/)
/[MATCH](https://trumpexcel.com/excel-match-function/)
 to fetch the details of an employee using his/her employee id.

_Note: This technique would work only for a numeric dataset. In case you have employee ids like A1, A2, A3 and so on, then these are text and would not change when you apply the custom format as shown above_.

Add Leading Zeros by Using REPT and LEN Functions
-------------------------------------------------

**When to Use:** When you have a data set that is numeric/alphanumeric, and you want the result to be text.

The drawback of using the TEXT function was that it would only work with numeric data. But in case you have an alphanumeric dataset (say A1, A2, A3, and so on), then the TEXT function would fail.

In such cases, a combination of [REPT](https://trumpexcel.com/excel-rept-function/)
 and [LEN](https://trumpexcel.com/excel-len-function/)
 function does the trick.

Here is how to do it:

1.  If you have the numbers in column A (say from A2:A100), then select B2:B100 and enter the following formula:  
    \=REPT(0,5-LEN(A2))&A2
2.  Press Control + Enter to apply the formula to all the selected cells.

This would make all the numbers/strings 5 characters long with leading zeroes wherever needed.

**Here is how this formula works:**

*   LEN(A2) gives the length of the string/numbers in the cell.
*   \=REPT(0,5-LEN(A2)) would give the number of 0 that should be added. Here I have used 5 in the formula as that was the maximum length of string/numbers in my dataset. You can change this according to your data.
*    =REPT(0,5-LEN(A2))&A2 would simply add the number of zeroes to the value of the cell. For example, if the value in the cell is 123, this would return 00123.

Add Leading Zeros by Using Custom Function (VBA)
------------------------------------------------

If adding leading zeroes in Excel is something you are required to do quite often, using a custom function is a good idea.

Here is the VBA code that will create a simple function for adding leading zeroes:

'Code by Sumit Bansal from http://trumpexcel.com
Function AddLeadingZeroes(ref As Range, Length As Integer)
Dim i As Integer
Dim Result As String
Dim StrLen As Integer
StrLen = Len(ref)
For i = 1 To Length
If i <= StrLen Then
Result = Result & Mid(ref, i, 1)
Else
Result = "0" & Result
End If
Next i
AddLeadingZeroes = Result
End Function

Simply add this code to the module code window, and you’ll be able to use it just like any other worksheet function.

Or create an [add-in](https://trumpexcel.com/excel-add-in/)
 for it and be able to share it with your colleagues.

In this tutorial, I covered five ways to add a 0 in front of numbers in Excel. These are called leading zeros and while Excel removes them by default, you can still put a 0 in front of a number by using the formatting and formula methods covered in this tutorial.

**You May Also Like the Following Excel Tutorials:**

*   [How to Remove Leading Zeros in Excel](https://trumpexcel.com/remove-leading-zeros-excel/)
    
*   [Remove Spaces in Excel – Leading, Trailing, and Double](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
    
*   [Six Awesome Things Excel Custom Number Format can Do for You](https://trumpexcel.com/excel-custom-number-formatting/)
    .
*   [10 Ways to Clean Data in Excel Spreadsheets](https://trumpexcel.com/clean-data-in-excel/)
    .
*   [How to Lock Cells in Excel.](https://trumpexcel.com/lock-cells-in-excel/)
    
*   [How to Add Decimal Places in Excel (Automatically)](https://trumpexcel.com/add-decimal-places-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Add Leading Zeros in Excel (5 Easy Ways)”
---------------------------------------------------------------

1.  Perfect……What i wanted from long time
    
    [Reply](https://trumpexcel.com/add-leading-zeroes-excel/#comment-12582)
    
2.  I cannot get the leading zeros to stick when I save a sheet using VBA.  
    I have a sheet called “Input” and in the W5:Wn (“W5:W” & LastRow) are numbers. I want all of them to be 3-digits with leading zeros as needed and then copy that column to “TimeSheet” worksheet in the same workbook, rows B2:Bn (“B2:B” & LastRow – 3). But the leading zeros vanish when the “TimeSheet” is saved as a separate, stand-alone workbook.
    
    I have tried a wide variety of approaches and nothing works. HELP, please.
    
    [Reply](https://trumpexcel.com/add-leading-zeroes-excel/#comment-10546)
    
3.  Hello Sumit,  
    I find your content useful and easy to read. Thanks for sharing your knowledge.
    
    The TEXT function works the best for numbers, but not for actual text, for example if I get a part number like QJE and it needs to be 00QJE, Text doesn’t work.  
    For the QJE example, =REPT(0,5-LEN(A2))&A2 works, but in my experience sometimes the part number is longer than 5 characters, in which case the formula fails (#VALUE! error). Unusual, but possible.
    
    So the solution is to use CONCATENATE, like this: =RIGHT(CONCATENATE(“00000”,A2),5), using as many zeros as the total expected length of the part number. This provides full flexibility and it handles and corrects part numbers than are anywhere from 1 to 5 or more characters.  
    Using “&” instead of the CONCATENATE function also works: =RIGHT(“00000″&A2,5) and makes the formula shorter.
    
    Thanks,  
    Pablo
    
    [Reply](https://trumpexcel.com/add-leading-zeroes-excel/#comment-4219)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-leading-zeroes-excel/#respond)

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