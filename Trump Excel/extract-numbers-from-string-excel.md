# Extract Numbers from a String in Excel (Using Formulas or VBA)

**Source:** https://trumpexcel.com/extract-numbers-from-string-excel

---

[Skip to content](https://trumpexcel.com/extract-numbers-from-string-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/extract-numbers-from-string-excel/#below-title)

**Watch Video – How to Extract Numbers from text String in Excel (Using Formula and VBA)**

There is no inbuilt function in Excel to extract the numbers from a string in a cell (or vice versa –  remove the numeric part and extract the text part from an alphanumeric string).

However, this can be done using a cocktail of [Excel functions](https://trumpexcel.com/excel-functions/)
 or some simple [VBA code](https://trumpexcel.com/excel-vba/)
.

Let me first show you what I am talking about.

Suppose you have a data set as shown below and you want to extract the numbers from the string (as shown below):

![Extract Number from String in Excel - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20385%20165'%3E%3C/svg%3E)

The method you choose will also depend on the version of Excel you’re using:

*   For versions prior to Excel 2016, you need to use slightly longer formulas
*   For Excel 2016, you can use the newly introduced TEXTJOIN function
*   VBA method can be used in all the versions of Excel

This Tutorial Covers:

[Toggle](https://trumpexcel.com/extract-numbers-from-string-excel/#)

[**Click here to download the example file**](https://www.dropbox.com/s/gzscwa8a8biqwr5/Get-Numeric-or-Text-Part-from-a-String-Using-Excel-Formulas.xlsm?dl=1)

Extract Numbers from String in Excel (Formula for Excel 2016)
-------------------------------------------------------------

This formula will work only in Excel 2016 as it uses the newly introduced TEXTJOIN function.

Also, this formula can extract the numbers that are at the beginning, end or middle of the text string.

Note that the TEXTJOIN formula covered in this section would give you all the numeric characters together. For example, if the text is “The price of 10 tickets is USD 200”, it will give you 10200 as the result.

Suppose you have the dataset as shown below and you want to extract the numbers from the strings in each cell:

Below is the formula that will give you numeric part from a string in Excel.

\=TEXTJOIN("",TRUE,IFERROR((MID(A2,ROW(INDIRECT("1:"&LEN(A2))),1)\*1),""))

![Formula to get all number from a string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20230'%3E%3C/svg%3E)

This is an array formula, so you need to use ‘**Control + Shift + Enter**‘ instead of using Enter.

In case there are no numbers in the text string, this formula would return a blank (empty string).

**How does this formula work?**

Let me break this formula and try and explain how it works:

*   ROW(INDIRECT(“1:”&LEN(A2))) – this part of the formula would give a series of numbers starting from one. The [LEN function](https://trumpexcel.com/excel-len-function/)
     in the formula returns the total number of characters in the string. In the case of “The cost is USD 100”, it will return 19. The formulas would thus become ROW([INDIRECT](https://trumpexcel.com/excel-indirect-function/)
    (“1:19”). The [ROW function](https://trumpexcel.com/excel-row-function/)
     will then return a series of numbers – {1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19}
*   (MID(A2,ROW(INDIRECT(“1:”&LEN(A2))),1)\*1) – This part of the formula would return an array of #VALUE! errors or numbers based on the string. All the text characters in the string become #VALUE! errors and all numerical values stay as-is. This happens as we have multiplied the [MID function](https://trumpexcel.com/excel-mid-function/)
     with 1.
*   IFERROR((MID(A2,ROW(INDIRECT(“1:”&LEN(A2))),1)\*1),””) – When [IFERROR function](https://trumpexcel.com/excel-iferror-function/)
     is used, it would remove all the #VALUE! errors and only the numbers would remain. The output of this part would look like this – {“”;””;””;””;””;””;””;””;””;””;””;””;””;””;””;””;1;0;0}
*   \=TEXTJOIN(“”,TRUE,IFERROR((MID(A2,ROW(INDIRECT(“1:”&LEN(A2))),1)\*1),””)) – The TEXTJOIN function now simply combines the string characters that remains (which are the numbers only) and ignores the empty string.

**Pro Tip:** If you want to check the output of a part of the formula, select the cell, press F2 to get into the edit mode, select the part of the formula for which you want the output and press F9. You will instantly see the result. And then remember to either press Control + Z or hit the Escape key. DO NOT hit the enter key.

**Download the Example File**  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/gzscwa8a8biqwr5/Get-Numeric-or-Text-Part-from-a-String-Using-Excel-Formulas.xlsm?dl=1)

You can also use the same logic to extract the text part from an alphanumeric string. Below is the formula that would get the text part from the string:

\=TEXTJOIN("",TRUE,IF(ISERROR(MID(A2,ROW(INDIRECT("1:"&LEN(A2))),1)\*1),MID(A2,ROW(INDIRECT("1:"&LEN(A2))),1),""))

A minor change in this formula is that [IF function](https://trumpexcel.com/excel-if-function/)
 is used to check if the array we get from MID function are errors or not. If it’s an error, it keeps the value else it replaces it with a blank.

Then TEXTJOIN is used to combine all the text characters.

**Caution**: While this formula works great, it uses a [volatile function](https://trumpexcel.com/excel-volatile-formulas/)
 (the INDIRECT function). This means that in case you use this with a huge dataset, it may take some time to give you the results. It’s best to create a backup before you use this formula in Excel.

Also read: [How To Convert Text To Number In Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)

Extract Numbers from String in Excel (for Excel 2013/2010/2007)
---------------------------------------------------------------

If you have Excel 2013. 2010. or 2007, you can not use the TEXTJOIN formula, so you will have to use a complicated formula to get this done.

Suppose you have a dataset as shown below and you want to extract all the numbers in the string in each cell.

![Extract Number from String in Excel - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20385%20165'%3E%3C/svg%3E)

The below formula will get this done:

\=IF(SUM(LEN(A2)-LEN(SUBSTITUTE(A2, {"0","1","2","3","4","5","6","7","8","9"}, "")))>0, SUMPRODUCT(MID(0&A2, LARGE(INDEX(ISNUMBER(--MID(A2,ROW(INDIRECT("$1:$"&LEN(A2))),1))\* ROW(INDIRECT("$1:$"&LEN(A2))),0), ROW(INDIRECT("$1:$"&LEN(A2))))+1,1) \* 10^ROW(INDIRECT("$1:$"&LEN(A2)))/10),"")

In case there is no number in the text string, this formula would return blank (empty string).

Although this is an array formula, you **don’t need** to use ‘Control-Shift-Enter’ to use this. A simple enter works for this formula.

_Credit to this formula goes to the amazing [Mr. Excel forum](https://www.mrexcel.com/forum/excel-questions/443983-extract-only-numbers-text-string.html)
._

Again, this formula will extract all the numbers in the string no matter the position. For example, if the text is “The price of 10 tickets is USD 200”, it will give you 10200 as the result.

**Caution**: While this formula works great, it uses a volatile function (the INDIRECT function). This means that in case you use this with a huge dataset, it may take some time to give you the results. It’s best to create a backup before you use this formula in Excel.

Separate Text and Numbers in Excel Using VBA
--------------------------------------------

If separating text and numbers (or extracting numbers from the text) is something you have to often, you can also use the VBA method.

All you need to do is use a simple VBA code to [create a custom User Defined Function (UDF) in Excel](https://trumpexcel.com/user-defined-function-vba/)
, and then instead of using long and complicated formulas, use that VBA formula.

Let me show you how to create two formulas in VBA – one to extract numbers and one to extract text from a string.

### Extract Numbers from String in Excel (using VBA)

In this part, I will show you how to create the custom function to get only the numeric part from a string.

Below is the VBA code we will use to create this custom function:

Function GetNumeric(CellRef As String)
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If IsNumeric(Mid(CellRef, i, 1)) Then Result = Result & Mid(CellRef, i, 1)
Next i
GetNumeric = Result
End Function

Here are the steps to create this function and then use it in the worksheet:

*   Go to the Developer tab.![Developer Tab in Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20131'%3E%3C/svg%3E)
*   Click on Visual Basic (You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     ALT + F11)![Visual Basic in the Ribbon in Excel - To create custom function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20131'%3E%3C/svg%3E)
*   In the VB Editor backend that opens, right-click on any of the workbook objects.![Right click on VBA Backend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20406'%3E%3C/svg%3E)
*   Go to Insert and click on Module. This will insert the module object for the workbook.![Insert a module in VBA Back end](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20411'%3E%3C/svg%3E)
*   In the Module code window, copy and paste the VBA code mentioned above.![Custom function to get the numeric part from the text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20190'%3E%3C/svg%3E)
*   Close the VB Editor.

Now, you will be able to use the GetText function in the worksheet. Since we have done all the heavy lifting in the code itself, all you need to do is use the formula \=GetNumeric(A2). 

This will instantly give you only the numeric part of the string.

![Using Custom VBA Function to get only the numeric part from a string in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20423%20205'%3E%3C/svg%3E)

Note that since the workbook now has VBA code in it, you need to save it with .xls or .xlsm extension.

**Download the Example File**  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/gzscwa8a8biqwr5/Get-Numeric-or-Text-Part-from-a-String-Using-Excel-Formulas.xlsm?dl=1)

In case you have to use this formula often, you can also save this to your [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. This will allow you to use this custom formula in any of the Excel workbooks that you work with.

### Extract Text from a String in Excel (using VBA)

In this part, I will show you how to create the custom function to get only the text part from a string.

Below is the VBA code we will use to create this custom function:

Function GetText(CellRef As String)
Dim StringLength As Integer
StringLength = Len(CellRef)
For i = 1 To StringLength
If Not (IsNumeric(Mid(CellRef, i, 1))) Then Result = Result & Mid(CellRef, i, 1)
Next i
GetText = Result
End Function

Here are the steps to create this function and then use it in the worksheet:

*   Go to the Developer tab.![Developer Tab in Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20131'%3E%3C/svg%3E)
*   Click on Visual Basic (You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     ALT + F11)![Visual Basic in the Ribbon in Excel - To create custom function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20131'%3E%3C/svg%3E)
*   In the VB Editor backend that opens, right-click on any of the workbook objects.![Right click on VBA Backend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20406'%3E%3C/svg%3E)
*   Go to Insert and click on Module. This will insert the module object for the workbook.
    *   If you already have a module, double-click on it (no need to insert a new one if you already have it).![Insert a module in VBA Back end](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20411'%3E%3C/svg%3E)
*   In the Module code window, copy and paste the VBA code mentioned above.![Custom function to get the Text part from the string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20174'%3E%3C/svg%3E)
*   Close the VB Editor.

Now, you will be able to use the GetNumeric function in the worksheet. Since we have done all the heavy lifting in the code itself, all you need to do is use the formula \=GetText(A2).

This will instantly give you only the numeric part of the string.

![Using Custom VBA Function to get only the Text part from a string in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20431%20204'%3E%3C/svg%3E)

Note that since the workbook now has VBA code in it, you need to save it with .xls or .xlsm extension.

In case you have to use this formula often, you can also save this to your [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. This will allow you to use this custom formula in any of the Excel workbooks that you work with.

In case you’re using Excel 2013 or prior versions and don’t have

**You May Also Like the Following Excel Tutorials:**

*   [CONCATENATE Excel Ranges (with and without separator)](https://trumpexcel.com/concatenate-excel-ranges/)
    .
*   [A Beginner’s Guide to Using For Next Loop in Excel VBA](https://trumpexcel.com/for-next-loop-excel-vba/)
    .
*   [Using Text to Columns in Excel.](https://trumpexcel.com/excel-text-to-columns-examples/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    .
*   [Excel Macro Examples for VBA Beginners.](https://trumpexcel.com/excel-macro-examples/)
    
*   [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    
*   [REGEX Functions in Excel](https://trumpexcel.com/excel-functions/regex-excel/)
    
*   [Convert Number to Words in Excel](https://trumpexcel.com/number-to-words-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “Extract Numbers from a String in Excel (Using Formulas or VBA)”
-------------------------------------------------------------------------------

1.  Perfect Approaches well articulated.
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-14710)
    
2.  it does not exist in 2016. i think it is n 360. i have 2016 and it is not there. had to use your VBA method which worked. so thank you
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-13148)
    
3.  Very useful. Really helped. Thanks.
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-12538)
    
4.  Hi, I want to extract Alphanumeric number from the string for whole workbook having entries in thousands. And all the entries are of different type, please help. Entries are as shown below.  
    1). “2019-06-12 18:05:18– One RAX Card Faulty; card P Code: ROJ 119 2329/1 R18 Sr. No: (S)AE56819158. Reason: RED LED Continue on card, After Slot change, No change in status.”  
    from this entry i want A) “part code i.e “ROJ1192329/1” & B)Serial number i.e “AE56819158”  
    2). 2019-07-16 17:40:34– Two Nos of RU21 Card faulty at Fatehpur Kalan Node-B 3G BTS Both Card are checked replaced with working sector but card remain down with permanent RED LEG on card same has been conformed by JTO NAGAR Serial No:-1)AE56669151 , 2)CB47479036 Part Code:1)KRC118 16/3 R2A ,2) KRC 121 154/1 R3A  
    from this entry i want A) part code KRC121154/1 & B) Serial number AE56669151 & CB47479036  
    Every thing in different column. Please help me !!!!!
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-12534)
    
5.  how do we extract decimal values?
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-12113)
    
6.  Hi Summit,
    
    You might want to also consider the decimal symbol (period/dot “.” for North America, or comma “,” depending on the locale/country)
    
    In most cases of a get numeric, you’ll want the decimal  
    I was processing US$1,425K and I would get 1425 (the comma isn’t relevant)  
    But when I had US$250.5K, I would get 12505. In this case, the desired number is 250.5 (the decimal is relevant)
    
    So, I added Or Mid(CellRef, i, 1)=”.” for my purposes
    
    Note that other countries would have US$1.425,5K
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-11599)
    
7.  DONT WORK FAGGOT
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-11107)
    
8.  Dear, These cells have codes (? \*) and (?) and (“Low Vol”) and numbers with code (67,306,444 \*) how can I separate the numbers and use them for calculating. Unfortunately, function Getnumber not helping especially when all codes in the same column with more than 2 thousand cells.
    
    Here the challenging
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-10624)
    
9.  I’m using Excel 2016. The textjoin function is only available in 365. I put in the VBA formulas to no avail. Not only that, but now no functions or calculations will work on the spreadsheet. Please help.
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-10265)
    
10.  Hi Sumit i watch all the published video of yours and find it interesting and useful….i need your small help today i wanted to convert numeric value in words without using macro if there is any formula for the same please help.
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-9739)
    
11.  UDF with a modification:-  
    ———————————————————————-  
    Function GetNumeric(CellRef As String)  
    Dim StringLength As Integer  
    Dim Result ””””””””””””””””””””’  
    Result = “”  
    StringLength = Len(CellRef)  
    For i = 1 To StringLength  
    If IsNumeric(Mid(CellRef, i, 1)) Then Result = Result & Mid(CellRef, i, 1)  
    Next i  
    GetNumeric = Result \* 1 ””””””””””””””””””””  
    End Function  
    —————————————————————————-  
    Function GetText(CellRef As String)  
    Dim StringLength As Integer  
    StringLength = Len(CellRef)  
    Dim Result As String ””””””””””””””””””””  
    Result = “”  
    For i = 1 To StringLength  
    If Not (IsNumeric(Mid(CellRef, i, 1))) Then Result = Result & Mid(CellRef, i, 1)  
    Next i  
    GetText = Result  
    End Function
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-9720)
    
12.  If the numeric part is always at the end, like in your examples, I think is more efficient the following formula to extract the numeric part: =VALUE(TRIM(MID(A2,FIND(“|”,SUBSTITUTE(A2,” “,”|”,LEN(A2)-LEN(SUBSTITUTE(A2,” “,””)))),9999999))) and the following one to extract just the text =TRIM(LEFT(A2,FIND(“|”,SUBSTITUTE(A2,” “,”|”,LEN(A2)-LEN(SUBSTITUTE(A2,” “,””))))))
    
    [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-9718)
    
    *   Thanks for sharing Franz.. This formula doesn’t work if there are no spaces. For example, if the text is “ABC123”, then it would return an error.
        
        [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-9719)
        
        *   Hey @Sumit, need your help on creating an Attendance tracker using formulas in Excel.
            
            [Reply](https://trumpexcel.com/extract-numbers-from-string-excel/#comment-9758)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/extract-numbers-from-string-excel/#respond)

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