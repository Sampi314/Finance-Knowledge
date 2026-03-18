# How to Filter Cells that have Duplicate Text Strings (Words) in it

**Source:** https://trumpexcel.com/duplicate-text-strings

---

[Skip to content](https://trumpexcel.com/duplicate-text-strings/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/duplicate-text-strings/#below-title)

One of my friends works in a healthcare analytics company. He often connects with me on some of the real-life issues he faces while working with data in Excel.

A lot of times, I convert his queries into Excel tutorials on this site, as it could be helpful for my other readers as well.

This is also one such tutorial.

My friend called me last week with the following issue:

_There is address data in a column in Excel, and I want to identify/filter cells the where the address has duplicate text strings (words) in it._

Here is the similar dataset in which he wanted to filter cells that have a duplicate text string in it (the ones with red arrows):

![Identify Duplicate Text Strings in Excel - Dataset Address](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20249'%3E%3C/svg%3E)

Now what makes this difficult is that there is no consistency in this data. Since this is a compilation of data sets that have been manually created by sales reps, there can be variations in the dataset.

Consider this:

*   Any text string could repeat in this dataset. For example, it could be the name of the area or the name of the city or both.
*   The words are separated by a space character, and there is no consistency in whether the city name would be there after six words or eight words.
*   There are thousands of records like this, and the need is to filter those records where there are any duplicate text strings.

After considering many options (such as [text to columns](https://trumpexcel.com/excel-text-to-columns-examples/)
 and formulas), I finally decided to use VBA to get this done.

So I created a custom VBA function (‘IdDuplicate’) to analyze these cells and give me TRUE if there is a duplicate word in the text string, and FALSE in case there are no repetitions (as shown below):

![Identify Duplicate Text Strings in Excel - Dataset Address Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20264'%3E%3C/svg%3E)

This custom function analyzes each word in the text string and checks how many times it occurs in the text. If the count is more than 1, it returns TRUE; else it returns FALSE.

Also, it has been created to only [count words](https://trumpexcel.com/word-count-in-excel/)
 more than three characters.

Once I have the TRUE/FALSE data, I can easily filter all the records that are TRUE.

Now let me show you how to do this in Excel.

VBA Code for the Custom Function
--------------------------------

This is done by creating a custom function in VBA. This function can then be used as any other worksheet function in Excel.

Here is the VBA code for it:

Function IdDuplicates(rng As Range) As String
Dim StringtoAnalyze As Variant
Dim i As Integer
Dim j As Integer
Const minWordLen As Integer = 4
StringtoAnalyze = Split(UCase(rng.Value), " ")
For i = UBound(StringtoAnalyze) To 0 Step -1
If Len(StringtoAnalyze(i)) < minWordLen Then GoTo SkipA
For j = 0 To i - 1
If StringtoAnalyze(j) = StringtoAnalyze(i) Then
IdDuplicates = "TRUE"
GoTo SkipB
End If
Next j
SkipA:
Next i
IdDuplicates = "FALSE"
SkipB:
End Function

_Thanks [Walter](https://trumpexcel.com/duplicate-text-strings/#comments/10129)
 for suggesting a better approach to this code!_

How to Use this VBA Code
------------------------

Now that you have the VBA code, you need to place it in the backend of Excel, so that it can work as a regular worksheet function.

Below are the steps to put the VBA code on the backend:

1.  Go to the Developer tab.![identify duplicate text strings - developer tab in ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20131'%3E%3C/svg%3E)
2.  Click on Visual Basic (you can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     ALT + F11)![Select Visual basic from the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20131'%3E%3C/svg%3E)
3.  In the VB Editor back end that opens, right-click on any of the workbook objects.
4.  Go to ‘Insert’ and click on ‘Module’. This will insert the module object for the workbook.![Insert Module for the custom VAB code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20419'%3E%3C/svg%3E)
5.  In the Module code window, copy and paste the VBA code mentioned above.![VBA Code in the backend - to identify duplicate text strings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20753%20397'%3E%3C/svg%3E)

Once you have the VBA code in the back end, you can use the function – ‘IdDuplicates’ as any other regular [worksheet function](https://trumpexcel.com/excel-functions/)
.

This function takes one single argument, which is the [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 of the cell where you have the text.

The result of the function is TRUE (if there are duplicate words in it) or FALSE (if there are no duplicates). Once you have this list of TRUE/FALSE, you can filter the ones with TRUE to get all the cells that have duplicate text strings in it.

Note: I have created the code only to consider those words that are more than three characters long.

This ensures that if there are 1, 2, or 3 character-long words (such as 12 A, K G M, or L D A) in the text string, these are ignored while counting the duplicates. If you want, you can easily change this in the code.

This function will only be available in the workbook where you have copied the code in the module. In case you want this to be available in other workbooks as well, you need to copy and paste this code in those workbooks.

Alternatively, you can also [create an add-in](https://trumpexcel.com/excel-add-in/)
 (enabling this function to be available in all the workbooks on your system).

Also, remember to save this workbook in .xlsm extension (since it has a [macro code](https://trumpexcel.com/excel-macro-examples/)
 in it).

**You May Also Like the Following Excel Tutorials:**

*   [Excel Advanced Filter – A Complete Guide with Examples.](https://trumpexcel.com/excel-advanced-filter/)
    
*   [Dynamic Excel Filter Search Box – Extract Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    
*   [Remove Duplicates Within a Cell in Excel](https://trumpexcel.com/remove-duplicates-from-cell-excel/)
    
*   [Paste into Filtered Column (Skipping Hidden Cells) in Excel](https://trumpexcel.com/paste-into-filtered-column/)
    
*   [The Ultimate Guide to Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    .
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [Check IF Cell Contains Partial Text in Excel](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

18 thoughts on “How to Filter Cells that have Duplicate Text Strings (Words) in it”
-----------------------------------------------------------------------------------

1.  Sir, I have column of integer values and they are up yo 4 decimal places. I have duplicate issue with values. how to remove duplicate in this case?
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-14652)
    
2.  Hi I have used the above code, if second word has comma, it is not setting as True. could you please help me on this.
    
    Example : test test, – False
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-13687)
    
3.  You are wonderful! So useful!
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-12527)
    
4.  Can I get VBA learning from the very basics?
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10133)
    
    *   Hey Aniruddha.. You can get some tutorials here. I am currently working on creating basic step-by-step tutorials on VBA. Will start posting in the next 2 weeks. You can subscribe to my email list to get notified.
        
        [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10135)
        
5.  Really useful. Thank you very much….!!!
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10120)
    
6.  really nice code and it does a great job. It would help us a lot if you would go a little more into detail of what the various parts of the code do – e.g. (modrng = WorksheetFunction.Substitute(rng.Value, ” “, “@”, numberofspaces + 1 – i) – so some value = some other value(some value, space, ?@?, #spaces+1-count) ???
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10117)
    
    *   Hey Rich,
        
        I have updated the code and now it’s shorter and easier to read
        
        [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10131)
        
7.  Nice you all tutorial thanks of help .
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10114)
    
    *   Glad you’re finding the tutorials useful!
        
        [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10115)
        
        *   Yes, But can you share more tutorial about SQL and Pl/SQL topics.
            
            [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10116)
            
            *   Hey Mithilesh.. I only create tutorials on MS Excel.
                
                [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10121)
                
8.  This takes advantage of the Split function in vba. It could be streamlined more.
    
    Function IdDuplicates2(rng As Range)  
    Dim StringtoAnalyze As Variant  
    Dim i As Integer  
    On Error Resume Next  
    IdDuplicates2 = “False”  
    StringtoAnalyze = Split(rng.Value, ” “)  
    i = LBound(StringtoAnalyze)  
    If UBound(StringtoAnalyze) – LBound(StringtoAnalyze) > 0 Then  
    Do While i <= UBound(StringtoAnalyze) And IdDuplicates2 = "False"  
    If StringtoAnalyze(i – 1) = StringtoAnalyze(i) Then IdDuplicates2 = "True"  
    i = i + 1  
    Loop  
    End If  
    End Function
    
    [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10113)
    
    *   Thanks for sharing Ben.. I agree, Split and Lbound/Ubound could be a cleaner approach. I tried your code but it didn’t work. returns TRUE in all cases. Also, the one I have considers that any words (at any position could repeat). So it the same word could be at 2nd and 5th position, and it will be highlighted.
        
        [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10126)
        
        *   The code of Ben needs a small change, the start value for i must be LBound(StringToAnalyze) + 1:
            
            Function IdDuplicates2(rng As Range)  
            Dim StringtoAnalyze As Variant  
            Dim i As Integer
            
            On Error Resume Next  
            IdDuplicates2 = “False”  
            StringtoAnalyze = Split(rng.Value, ” “)
            
            i = LBound(StringtoAnalyze) + 1  
            If (UBound(StringtoAnalyze) – LBound(StringtoAnalyze)) > 0 Then  
            Do While i <= UBound(StringtoAnalyze) And IdDuplicates2 = "False"  
            If StringtoAnalyze(i – 1) = StringtoAnalyze(i) Then  
            IdDuplicates2 = "True"  
            Exit Do  
            End If  
            i = i + 1  
            Loop  
            End If  
            End Function
            
            [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10127)
            
            *   Hey Wouter.. Thanks for sharing. Your code works 🙂 But it still only identifies cells where the repetition in adjacent words. In case these words are not adjacent, it returns TRUE
                
                [Reply](https://trumpexcel.com/duplicate-text-strings/#comment-10128)
                
                *   I concur on that, but made an other function to look for repeated words in any place of the cell contents:
                    
                    Function IdRepeated(rng As Range) As Boolean  
                    Dim StringtoAnalyze As Variant  
                    Dim i As Integer  
                    Dim j As Integer  
                    Const minWordLen As Integer = 4  
                    On Error Resume Next  
                    IdRepeated = False  
                    StringtoAnalyze = Split(rng.Value, ” “)  
                    ‘ remove short words from array  
                    For i = (UBound(StringtoAnalyze) – 1) To LBound(StringtoAnalyze) Step -1  
                    If Len(StringtoAnalyze(i)) < minWordLen Then  
                    For j = i To UBound(StringtoAnalyze) – 1  
                    StringtoAnalyze(j) = StringtoAnalyze(j + 1)  
                    Next  
                    ReDim Preserve StringtoAnalyze(UBound(StringtoAnalyze) – 1)  
                    End If  
                    Next  
                    j = UBound(StringtoAnalyze)  
                    If (Len(StringtoAnalyze(j)) < minWordLen) Then  
                    ReDim Preserve StringtoAnalyze(j – 1)  
                    End If  
                    ' Look for repeated words  
                    For i = LBound(StringtoAnalyze) To UBound(StringtoAnalyze) – 1  
                    For j = i + 1 To UBound(StringtoAnalyze)  
                    If (StringtoAnalyze(i) = StringtoAnalyze(j)) Then  
                    IdRepeated = True  
                    Exit Function  
                    End If  
                    Next  
                    Next  
                    End Function
                    
                *   Thanks Wouter.. I used the SPLIT function to approach this. Here is the code that’s also working (and is shorter too)
                    
                    Also made a change to identify words even if in different cases.
                    
                    Function IdDuplicates(rng As Range) As String  
                    Dim StringtoAnalyze As Variant  
                    Dim i As Integer  
                    Dim j As Integer  
                    Const minWordLen As Integer = 4  
                    StringtoAnalyze = Split(UCase(rng.Value), ” “)  
                    For i = UBound(StringtoAnalyze) To 0 Step -1  
                    If Len(StringtoAnalyze(i)) < minWordLen Then GoTo SkipA For j = 0 To i - 1 If StringtoAnalyze(j) = StringtoAnalyze(i) Then IdDuplicates = "TRUE" GoTo SkipB End If Next j SkipA: Next i IdDuplicates = "FALSE" SkipB: End Function Will update on the site soon.
                    

### Leave a Comment [Cancel reply](https://trumpexcel.com/duplicate-text-strings/#respond)

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