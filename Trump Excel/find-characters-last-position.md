# Find Position of the Last Occurrence of a Character in Excel

**Source:** https://trumpexcel.com/find-characters-last-position

---

[Skip to content](https://trumpexcel.com/find-characters-last-position/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-characters-last-position/#below-title)

_In this tutorial, you’ll learn how to find the position of the last occurrence of a character in a string in Excel._

A few days ago, a colleague came up with this problem.

He had a list of URLs as shown below, and he needed to extract all the characters after the last forward slash (“/”).

So for example, from https://example.com/archive/**January** he had to extract ‘January’.

![Find Position of the Last Occurrence of a Character in a String - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20541%20288'%3E%3C/svg%3E)

It would have been really easy has there been only one forward slash in the URLs.

What he had was a huge list of thousands on URLs of varying length and a varying number of forward-slashes.

In such cases, the trick is to find the position of the last occurrence of the forward slash in the URL.

In this tutorial, I will show you two ways to do this:

*   Using an Excel formula
*   Using a custom function (created via VBA)

Getting the Last Position of a Character using Excel Formula
------------------------------------------------------------

When you have the position of the last occurrence, you can simply extract anything on the right of it using the [RIGHT function](https://trumpexcel.com/excel-right-function/)
.

Here is the formula that would find the last position of a forward slash and extract all the text to the right of it.

\=RIGHT(A2,LEN(A2)-FIND("@",SUBSTITUTE(A2,"/","@",LEN(A2)-LEN(SUBSTITUTE(A2,"/",""))),1))

#### ![Find Position of the Last Occurrence of a Character in a String - Formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20364'%3E%3C/svg%3E)

#### **How does this formula work?**

Let ‘s break down the formula and explain how each part of it works.

*   _SUBSTITUTE(A2,”/”,_“”_)_ – This part of the formula replaces the forward slash with an empty string. So for example, In case you want to find the occurrence of any string other than the forward slash, use that here.
*   _LEN(A2)-LEN(SUBSTITUTE(A2,”/”,_“”_))_ – This part would tell you how many forward slashes are there in the string. It simply subtracts the length of the string without the forward slash from the length of the string with forward-slashes.
*   _SUBSTITUTE(A2,”/”,”@”,LEN(A2)-LEN(SUBSTITUTE(A2,”/”,””)))_ – This part of the formula would replace the last forward slash with @. The idea is to make that character unique. You can use any character you want. Just make sure it’s unique and doesn’t appear in the string already.
*   _FIND(“@”,SUBSTITUTE(A2,”/”,”@”,LEN(A2)-LEN(SUBSTITUTE(A2,”/”,””))),1)_ – This part of the formula would give you the position of the last forward slash.
*   _LEN(A2)-FIND(“@”,SUBSTITUTE(A2,”/”,”@”,LEN(A2)-LEN(SUBSTITUTE(A2,”/”,””))),1)_ – This part of the formula would tell us how many characters are there after the last forward slash.
*   _\=RIGHT(A2,LEN(A2)-FIND(“@”,SUBSTITUTE(A2,”/”,”@”,LEN(A2)-LEN(SUBSTITUTE(A2,”/”,””))),1))_ – Now this would simply give us the string after the last forward slash.

Also read: [Remove Last Character in Excel](https://trumpexcel.com/remove-last-character/)

Getting the Last Position of a Character using Custom Function (VBA)
--------------------------------------------------------------------

While the above formula is great and works like a charm, it’s a bit complicated.

If you’re comfortable using VBA, you can use a [custom function](https://trumpexcel.com/user-defined-function-vba/)
 (also called a User Defined Function) created via VBA. This can simplify the formula and can save time if you have to do this often.

Let’s use the same data set of URLs (as shown below):

![Find Position of the Last Occurrence of a Character in a String - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20541%20288'%3E%3C/svg%3E)

For this case, I have created a function called LastPosition, that find the last position of the specified character (which is a forward slash in this case).

Here is the formula that will do this:

\=RIGHT(A2,LEN(A2)-LastPosition(A2,"/")+1)

![Find Position of the Last Occurrence of a Character in a String VBA formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20648%20346'%3E%3C/svg%3E)

You can see that this is a lot simpler than the one we used above.

Here is how this works:

*   LastPosition – which is our custom function – returns the position of the forward-slash. This function takes two arguments – the cell reference that has the URL and the character whose position we need to find.
*   RIGHT function then gives us all the characters after the forward slash.

Here is the VBA code that created this function:

Function LastPosition(rCell As Range, rChar As String)
'This function gives the last position of the specified character
'This code has been developed by Sumit Bansal (https://trumpexcel.com)
Dim rLen As Integer
rLen = Len(rCell)
For i = rLen To 1 Step -1
If Mid(rCell, i - 1, 1) = rChar Then
 LastPosition = i
 Exit Function
End If
Next i
End Function

To make this function work, you need to place it in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
. Once done, you can use this function like any other regular Excel function.

Here are the steps to copy and paste this code in the VB back-end:

Here are the steps to place this code in the VB Editor:

1.  Go to the Developer tab.![Find Last match Occurrence of an item in a list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
2.  Click on the Visual Basic option. This will open the VB editor in the backend.![Find Last match Occurrence of an item in a list - Visual Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20708%20162'%3E%3C/svg%3E)
3.  In the Project Explorer pane in the VB Editor, right-click on any object for the workbook in which you want to insert the code. If you don’t see the Project Explorer go to the View tab and click on Project Explorer.
4.  Go to Insert and click on Module. This will insert a module object for your workbook.![Last Position of a Character in a String - Insert Module in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20423'%3E%3C/svg%3E)
5.  Copy and paste the code in the module window.![Code in the Module window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20790%20235'%3E%3C/svg%3E)

Now the formula would be available in all the worksheets of the workbook.

Note that you need to save the workbook as the .XLSM format as it has a macro in it. Also, if you want this formula to be available in all the workbooks you use, you can either save it the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
 or [create an add-in](https://trumpexcel.com/excel-add-in/)
 from it.

**You May Also Like the Following Excel Tutorials:**

*   [How to Get the Word Count in Excel](https://trumpexcel.com/word-count-in-excel/)
    .
*   [How to Use VLOOKUP with Multiple Criteria](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    .
*   [Find the Last Occurrence of a Lookup Value a List in Excel](https://trumpexcel.com/find-last-occurrence/)
    .
*   [Extract Substring in Excel.](https://trumpexcel.com/extract-a-substring-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

25 thoughts on “Find Position of the Last Occurrence of a Character in a String in Excel”
-----------------------------------------------------------------------------------------

1.  Here is the non-VBA using LET  
    \=LET(  
    Rmv\_F\_Slash, SUBSTITUTE($B10,””,””),  
    Num\_F\_Slash, LEN($B10)-LEN(Rmv\_F\_Slash),  
    Rplc\_Last, SUBSTITUTE($B10,””,”@”,Num\_F\_Slash),  
    Psntn\_Last, FIND(“@”,Rplc\_Last),  
    Num\_Chr\_Aftr, LEN($B10)-Psntn\_Last,  
    Full\_Formula, RIGHT($B10, Num\_Chr\_Aftr),  
    Result, Full\_Formula,  
    Result)
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-14775)
    
2.  thank you
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-14345)
    
3.  If you are searching for more than one character, for example “5.)”, in place of “/” in the equation example above, be sure to divide the length subtraction by the number of characters. This is because for every instance of that character string, that many characters are being removed from the string per instance, so the length subtraction equation gives you a difference that is \*length of desired character string\* greater than the number of instances.  
    E.g.,  
    \=RIGHT(A2,LEN(A2)-FIND(“@”,SUBSTITUTE(A2,”/”,”@”,LEN(A2)-LEN(SUBSTITUTE(A2,”/”,””))),1)) \[original\]
    
    \=RIGHT(A2,LEN(A2)-FIND(“@”,SUBSTITUTE(A2,”5.)”,”@”,(LEN(A2)-LEN(SUBSTITUTE(A2,”5.)”,””)))/3),1)) \[new\]
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-13877)
    
4.  Perfect! Thank you so much!! Saved me a lot of time:)
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-13592)
    
5.  thank you
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-13150)
    
6.  Thank you – used the cell formula and it worked a treat !
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12906)
    
7.  Or Excel specific:
    
    InStrRev(rCell, rChar) + 1
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12767)
    
8.  Is the LastPosition() function not replaceable with…
    
    InStrRev(MyString, “/”) + 1
    
    ?
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12765)
    
9.  I am so grateful. I was very hungry to get the formula. It will save a hundred hours of mine.
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12719)
    
10.  Works great! Thanks!
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12676)
    
11.  You guys just saved me a bunch of time – thank you!
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12233)
    
12.  Need help on formula to reverse the above process in reverse way,
    
    Example:  
    Input: ABC123BCDSample.txt
    
    Expected output: ABC123BCD
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12126)
    
    *   Using the example above, I used =MID(A2, 1, FIND(“@”,SUBSTITUTE(A2,”/”,”@”,LEN(A2)-LEN(SUBSTITUTE(A2,”/”,””))),1)-1)  
        You can remove “-1” if you want to include the last / in the output
        
        [Reply](https://trumpexcel.com/find-characters-last-position/#comment-13416)
        
    *   This will remove everything after the final / in A1. Put this in in B1:  
        \=SUBSTITUTE(A1,TRIM(LEFT(RIGHT(SUBSTITUTE(A1,”/”,REPT(” “,100)),100),100)),””)
        
        [Reply](https://trumpexcel.com/find-characters-last-position/#comment-13992)
        
13.  Love it! Worked quick and easy !
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-12005)
    
14.  Great explanation. Well Done and Thank you.
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-11979)
    
15.  Thank you for this formula, this has saved me so much time today!
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-11879)
    
16.  Excellent – thanks!
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-11712)
    
17.  thanks for this, works great
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-11641)
    
18.  sorry, doesn’t work
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-11361)
    
    *   It does work you dummy, if you change the cell addresses correctly
        
        [Reply](https://trumpexcel.com/find-characters-last-position/#comment-11362)
        
19.  Thanks so much for this — very helpful!
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-11076)
    
20.  Worked great for me! Thank you!
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-10988)
    
21.  The Excel formula is clever. But the VBA solution can be simplified by using the InStrRev function.
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-10659)
    
22.  Works pretty well, but breaks if there’s only one of the separator character (“/”) in the string.
    
    [Reply](https://trumpexcel.com/find-characters-last-position/#comment-9943)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-characters-last-position/#respond)

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