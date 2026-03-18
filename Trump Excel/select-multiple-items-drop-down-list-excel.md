# Select Multiple Items from a Drop Down List in Excel

**Source:** https://trumpexcel.com/select-multiple-items-drop-down-list-excel

---

[Skip to content](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#below-title)

One of my colleagues asked me if it is possible to make multiple selections in a [drop-down list in Excel](https://trumpexcel.com/excel-drop-down-list/)
.

When you create a drop-down list, you can only make one selection. If you select another item, the first one is replaced with the new selection.

He wanted to make multiple selections from the same drop down in such a way that the selections get added to the already present value in the cell.

Something as shown below in the pic:

![select multiple items from a drop down list in excel - Multiple Selections](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20180'%3E%3C/svg%3E)

There is no way you can do this with Excel in-built features.

The only way is to use a VBA code, which runs whenever you make a selection and adds the selected value to the existing value.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#)

**Watch Video – How to Select Multiple Items from an Excel Drop Down List**

How to make Multiple Selections in a Drop Down List
---------------------------------------------------

In this tutorial, I will show you how to make multiple selections in an Excel drop-down list (with repetition and without repetition).

This has been one of the most popular Excel tutorials on this site. Since I get a lot of similar questions, I have decided to create an FAQ section at the end of this tutorial. So if you have any questions after reading this, please check out the FAQ section first.

There are two parts to creating a drop-down list that allows multiple selections:

*   Creating the drop-down list.
*   Adding the VBA code to the back-end.

### Creating the Drop Down List in Excel

Here are the steps to create a drop-down list in Excel:

1.  Select the cell or range of cells where you want the drop-down list to appear (C2 in this example).![Data for which you want to create the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20129'%3E%3C/svg%3E)
2.  Go to Data –> Data Tools –> Data Validation.![make multiple selections in a drop-down list in excel - Data Validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20160'%3E%3C/svg%3E)
3.  In the Data Validation dialogue box, within the settings tab, select ‘List’ as Validation Criteria.![select multiple items from a drop down list in excel - List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20323'%3E%3C/svg%3E)
4.  In Source field, select the cells which have the items that you want in the drop down.![selecting multiple items from an Excel drop down list - Source Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20602%20401'%3E%3C/svg%3E)
5.  Click OK.

Now, cell C2 has a drop-down list which shows the items names in A2:A6.

As of now, we have a drop-down list where you can select one item at a time (as shown below).

![Drop Down in C2 allows single selections](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20180'%3E%3C/svg%3E)

To enable this drop-down to allow us to make multiple selections, we need to add the VBA code in the back end.

The next two sections of this tutorial will give you the VBA code to allow multiple selections in the drop-down list (with and without repetition).

### VBA Code to allow Multiple Selections in a Drop-down List (with repetition)  

Below is the Excel VBA code that will enable us to select more than one item from the drop-down list (allowing repetitions in selection):

Private Sub Worksheet\_Change(ByVal Target As Range)

'Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
' To make mutliple selections in a Drop Down List in Excel

Dim Oldvalue As String
Dim Newvalue As String

On Error GoTo Exitsub
If Target.Address = "$C$2" Then
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then
    GoTo Exitsub
    Else: If Target.Value = "" Then GoTo Exitsub Else
        Application.EnableEvents = False
        Newvalue = Target.Value
        Application.Undo
        Oldvalue = Target.Value
        If Oldvalue = "" Then
            Target.Value = Newvalue
        Else
            Target.Value = Oldvalue & ", " & Newvalue
        End If
    End If
End If
Application.EnableEvents = True
Exitsub:
Application.EnableEvents = True
End Sub

Now you need to place this code in a module in VB Editor (as shown below in the ‘Where to put the VBA code’ section’).

When you have placed this code in the backend (covered later in this tutorial), it will allow you make multiple selections in the drop down (as shown below).

Note that if you select an item more than once, it will be entered again (repetition is allowed).

![select multiple items from a drop down list in excel - Multiple Selections](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20180'%3E%3C/svg%3E)

_**Try it Yourself.. Download the Example File[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/8qvg9c3h3tce7db/Multiple-Selection-from-a-Drop-Down-List-in-Excel_Updated.xlsm?dl=1)
**_

### VBA Code to allow Multiple Selections in a Drop-down List (without repetition)

A lot of people have been asking about the code to select multiple items from a drop-down list without repetition.

Here is the code that will make sure an item can only be selected once so that there are no repetitions:

Private Sub Worksheet\_Change(ByVal Target As Range)
'Code by Sumit Bansal from https://trumpexcel.com
' To allow multiple selections in a Drop Down List in Excel (without repetition)
Dim Oldvalue As String
Dim Newvalue As String
Application.EnableEvents = True
On Error GoTo Exitsub
If Target.Address = "$C$2" Then
  If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then
    GoTo Exitsub
  Else: If Target.Value = "" Then GoTo Exitsub Else
    Application.EnableEvents = False
    Newvalue = Target.Value
    Application.Undo
    Oldvalue = Target.Value
      If Oldvalue = "" Then
        Target.Value = Newvalue
      Else
        If InStr(1, Oldvalue, Newvalue) = 0 Then
            Target.Value = Oldvalue & ", " & Newvalue
      Else:
        Target.Value = Oldvalue
      End If
    End If
  End If
End If
Application.EnableEvents = True
Exitsub:
Application.EnableEvents = True
End Sub

Now you need to place this code in a module in VB Editor (as shown in the next section of this tutorial).

This code will allow you to select multiple items from the drop-down list. However, you will only be able to select an item only once. If you try and select it again, nothing would happen (as shown below).

![Select Multiple Items from a Drop Down List in Excel-no repetition](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20148'%3E%3C/svg%3E)

_**Try it Yourself.. Download the Example File[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/8qvg9c3h3tce7db/Multiple-Selection-from-a-Drop-Down-List-in-Excel_Updated.xlsm?dl=1)
**_

### Where to Put the VBA Code

Before you start using this code in excel, you need to put it in the back-end, such that it gets fired whenever there is any change in the drop-down selection.

Follow the below steps to put the VBA code in the backend of Excel:

1.  Go to the [Developer Tab](https://trumpexcel.com/excel-developer-tab/)
     and click on Visual Basic (you can also use the keyboard shortcut – Alt + F11). This will open the Visual Basic Editor.![Selecting Visual basic in the Developer Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20692%20131'%3E%3C/svg%3E)
2.  There should be a Project Explorer pane at the left (if it is not there, use Control + R to make it visible). ![select multiple items from a drop down list in excel - Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20233'%3E%3C/svg%3E)
3.  Double click on Worksheet Name (in the left pane) where the drop-down list resides. This opens the code window for that worksheet.![select multiple items from a drop down list in excel - Code Window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20652%20366'%3E%3C/svg%3E)
4.  In the code window, copy and paste the above code.![Paste Code to allow multiple selections in drop downs in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20457%20323'%3E%3C/svg%3E)
5.  Close the VB Editor.

Now when you go back to the drop-down and make selections, it will allow you to make multiple selections (as shown below):

![Resulting drop down in which you can choose more than one item](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20420%20180'%3E%3C/svg%3E)

_**Try it Yourself.. Download the Example File[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/8qvg9c3h3tce7db/Multiple-Selection-from-a-Drop-Down-List-in-Excel_Updated.xlsm?dl=1)
**_

_**Note:** Since we are using a VBA code to get this done, you need to save the workbook with a .xls or .xlsm extension._

### Frequently Asked Questions (FAQs)

I have created this section to answer some of the most asked questions about this tutorial and the VBA code. If you have any questions, I request you to go through this list of queries first.

**Q: In the VBA code, the functionality is for cell C2 only. How do I get it for other cells?**

Ans: To get this multiple selection drop-down in other cells, you need to modify the VBA code in the backend. Suppose you want to get this for C2, C3, and C4, you need to replace the following line in the code:

If Target.Address = "$C$2" Then

with this line:

If Target.Address = "$C$2" Or Target.Address = "$C$3" Or Target.Address = "$C$4" Then

**Q: I need to create multiple drop-downs in entire column 'C'. How do I get this for all the cells in the columns with multi-select functionality?**

Ans: To enable multiple selections in drop-downs in an entire column, replace the following line in the code:

If Target.Address = "$C$2" Then

with this line:

If Target.Column = 3 Then

On similar lines, if you want this functionality in column C and D, use the below line:

If Target.Column = 3 or Target.Column = 4 Then

**Q: I need to create multiple drop-downs in a row. How can I do this?**

Ans: If you need to create drop-down lists with multiple selections in a row (let's say the second row), you need to replace the below line of code:

If Target.Address = "$C$2" Then

with this line:

If Target.Row = 2  Then

Similarly, if you want this to work for multiple rows (let's say second and third row), use the below line of code instead:

If Target.Row = 2  or Target.Row = 3 Then

**Q: As of now, the multiple selections are separated by a comma. How can I change this to separate these with space (or any other separator).**

Ans: To separate these with a separator other than a comma, you need to replace the following line of VBA code:

Target.Value = Oldvalue & ", " & Newvalue

with this line of VBA code:

Target.Value = Oldvalue & " " & Newvalue

Similarly, if you want to change comma with other character, such as |, you can use the following line of code:

Target.Value = Oldvalue & "| " & Newvalue

**Q: Can I get each selection in a separate line in the same cell?**

Ans: Yes you can. To get this, you need to replace the below line of VBA code:

Target.Value = Oldvalue & ", " & Newvalue

with this line of code:

Target.Value = Oldvalue & vbNewLine & Newvalue

vbNewLine inserts a [new line in the same cell](https://trumpexcel.com/start-a-new-line-in-excel-cell/)
. So whenever you make a selection from the drop-down, it will be inserted in a new line.

**Q: Can I make the multiple selection functionality work in a protected sheet?** 

Ans: Yes you can. 

To get this done, you need to do two things:

Add the following line in the code (right after the DIM statement): 

**Me.Protect UserInterfaceOnly:=True**

Second, you need to make sure the cells - that have the drop-down with multiple selection functionality - are not locked when you protect the entire sheet.

Here is a tutorial on how to do this: [Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
 

**You May Also Like the Following Excel Tutorials:**

*   [Creating Multiple Drop-down Lists in Excel without Repetition](https://trumpexcel.com/multiple-drop-down-lists-in-excel/)
    .
*   [Display Main and Subcategory in Drop Down List in Excel](https://trumpexcel.com/subcategory-in-drop-down-list-excel/)
    .
*   [Create an Excel Drop Down list with Search Suggestions](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [Get Multiple Lookup Values in a Single Cell](https://trumpexcel.com/multiple-lookup-values-single-cell-excel/)
    .
*   [How to Remove Drop-Down List in Excel?](https://trumpexcel.com/remove-drop-down-list-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

601 thoughts on “How to Make Multiple Selections in a Drop Down List in Excel”
------------------------------------------------------------------------------

1.  Thanks a lot for your helpful video! Yet, I have a problem since I got my list of items that I want in the dropdown list on one worksheet called “kritiska varor & tjänster” (in Swedish) and the actual dropdown list in the third column of another sheet. Can I modify the same code row as you mention (i.e. If Target.Address = “$C$2” Then) to make this point to the right worksheet somehow?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-42707)
    
    *   Hi Peter… to make this work in a worksheet, you need to put the code in the worksheet code window. So when you open the VB Editor, you will see all the sheet names in a property pane. If you don’t see the property pane, click the view tab and then click on ‘Properties Window’. Double click on the sheet name where you want this code to work and then paste the code in the code window. And then you can modify the code to refer to the right column or cell. Hope this helps!
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-42990)
        
2.  How to exclude the Header row or the top 3 rows from Target.Column?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-42199)
    
    *   You can use something like
        
        Target.Column = 4 AND Target.Row > 3
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-42209)
        
3.  Can a drop-down list be created just like the one in the video (Multiple Unique Selections) in multiple columns where each column has a different list.  
    How can the code be adjusted for that?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-41418)
    
4.  As of now, the multiple selections are separated by a comma. How can I change this to separate these with space in a column & comma in another column ?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-37979)
    
5.  So helpful. Thanks so much!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-36188)
    
6.  thanks for all. I can add in one cell multiple selection from list of data validation. But I have a question that, I cannot filter the cells which I added values from data validation. When I filter with the criteria under the column which I applied VB code , It seems like there is nothing at the cell. How can avoid this problem while filtering? Please could you help me
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-33436)
    
7.  Is there a way to automatically number the entries with a FOR loop as they are added to the target cell. For example, for cell c3, I enter Alpha, Bravo and Charlie. I would would like them to appear in the cell as:
    
    1\. Alpha  
    2\. Bravo  
    3\. Charlie
    
    Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-32915)
    
8.  This worked amazingly. Thank you so much for your CLEAR instructions and alteration options. Much appreciated!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-32891)
    
9.  Hi-Sumit,  
    I am using Excel 2019, and I have failed to save my workbook because I do not have .xls or .xlsm in the extension list. What should I do? please help
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-31610)
    
10.  Thank you so much Sumit for this video. I have spent a lot of time trying to create a multiple drop-down list and I had failed. But with your video, I have done it quickly.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-31609)
    
11.  AWESOME, easy peasy (non techie here!)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14922)
    
12.  In the code window, when you put in the code, the drop down on top changes from Declarations to Change. Mine is not doing that and the code is not working. Please help
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14920)
    
13.  hello thanks for great help.i have a problem. i use vlookup for my list and when choose a item in list the price of item show in other cell. now i want when choose multi item in list sum the price of item sum and show. please help me
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14909)
    
14.  How can I do for multiple drop down lists for each cells in the same column? For example, in Column A, a cell as in A1, A2, and A3.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14892)
    
15.  How to get the count of selected items instead of those values?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14876)
    
16.  How can I get the count of selected values of drop down list insted of those values?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14875)
    
17.  Need 2 multi pick list in same sheet how to use this code?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14863)
    
18.  Doesn’t work
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14862)
    
19.  Thanks Sumit for the excellent tip. Please suggest how do I apply it to multiple columns in the same work sheet?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14861)
    
20.  How do I sort the data once it its entered? If, for example, my dropdown list contained the values: One, Two, Three, Four and someone were to select them in the following order: Two, One, Four, Three. How would I go about re-ordering the entry to coincide with the list order?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14818)
    
21.  Im want to use multiple selection list in many sheets in one work book. Each list, in each workbook is in different cell but all the lists are created from same named range, eg. Multiplelist. Can I use that code for all lists created from named range Multiplelist in whole workbook?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14817)
    
22.  can i make multiple selection in different coulmn of a single sheet?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14789)
    
23.  This does not seem to work if I protect the sheet or workbook. How can I get it to work on a protected sheet
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14787)
    
24.  What happens if I want to use a multi-select in different columns and the data validation list options are different for the columns? Does the VB code for the various columns need to be on different sheets? or do the lists just need to be different names?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14772)
    
25.  How to Make Multiple Selections in a Drop Down List in Excel (non repeating)
    
    I don’t know what I am doing wrong. I cannot make this work.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14719)
    
26.  Hi, the coding has applied itself to the whole sheet instead of the target columns I have told it to use? How do I overcome this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14714)
    
27.  I want to do the same thing in each column from “B” through “R” whats the easiest way to be able to add this to the code?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14688)
    
28.  How can I remove already selected word from the drop-down list? example  
    selected: one, two, three …..now I need to remove three and  
    re-select four
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14658)
    
    *   i have the same question, did you solve it already?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14844)
        
    *   I have the same problem do you have code for this ?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14853)
        
    *   If there is a known solution I would love to hear it 🙂
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14913)
        
        *   I have the same question, any solution to this?
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-15704)
            
29.  Honestly can’t get this to work. I want to reference a list defined in Worksheet X from cells in Worksheet Y. I have a range of values in consecutive cells in Worksheet X – let’s call them A, B, C, D, E. I’ve copied the code above and no joy. First question: how do I reference Worksheet X from cells in Worksheet Y – do I need to change the $C$2 in the example code to something like =X!$A1:$A5 ? Does this VBA code need to be in Worksheet Y or X?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14657)
    
30.  Hi I just wonder if you can apply this multiple selection drop-down list to a whole column but only in specific table? Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14634)
    
31.  This is highly useful, many thanks!  
    However I do have a question: How can I achieve that in the filter function (in the headline of any column), the different options do appear separately even if multiple items have been chosen in the fields of the table ? Many thanks for any hint!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14621)
    
32.  This is so helpful thank you! I was wondering, is there any way to create a pivot table from this which give information about how often one of the options is mentioned. So for example, lets say I have a table of fruit choices for 5 people (separated below with 😉 with drop down list as above, the responses are banana, apple, orange; apple, orange; banana, orange; apple; banana, apple, is there a way to run a pivot table so that I know how many people chose banana, how many chose apple, etc. I’ve tried it but it’s only giving me numbers for their full responses. Hope that makes sense!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14619)
    
33.  Life saver! Thanks a lot Sumit!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14600)
    
34.  I restricted the code to work in a range of cells, and I added “Please select!” in the cells to apperar when you press delete to cleare it.  
    Works fine for me with the code below.  
    Good luck!
    
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Not Intersect(Target, Range(“M6:M20”)) Is Nothing Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Or Oldvalue = “Please select!” Then  
    Target.Value = Newvalue  
    Else  
    If InStr(1, Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & “, ” & Newvalue  
    Else:  
    Target.Value = Oldvalue  
    End If  
    End If  
    End If
    
    Application.EnableEvents = True  
    Exitsub:  
    If ActiveCell.Value = “” Then  
    Target.Value = “Please select!”  
    End If  
    Application.EnableEvents = True  
    Exit Sub  
    End If  
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14578)
    
35.  Removing/deleting an item in your list (eg after clicking a wrong one) and at the same time also removing leading and trailing spaces and comma’s works fine for me with the code below. Good luck.
    
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    NewValue = Target.Value  
    Application.Undo  
    OldValue = Target.Value  
    If OldValue = “” Then  
    Target.Value = NewValue  
    Else  
    If InStr(1, OldValue, NewValue) = 0 Then  
    Target.Value = OldValue & “, ” & NewValue  
    Else:  
    RemoveLocation = InStr(1, OldValue, NewValue)  
    ItemLength = Len(NewValue)  
    If Len(OldValue) Len(NewValue) Then Target.Value = Left(OldValue, RemoveLocation – 1) & Mid(OldValue, RemoveLocation + ItemLength + 2)  
    End If  
    End If  
    ‘remove leading and trailing spaces en comma’s  
    Do While True  
    If Left(Target.Value, 1) = ” ” Or Left(Target.Value, 1) = “,” Then  
    Target.Value = Mid(Target.Value, 2)  
    Else  
    Exit Do  
    End If  
    Loop  
    Do While True  
    l = Len(Target.Value)  
    If Right(Target.Value, 1) = ” ” Or Right(Target.Value, 1) = “,” Then  
    Target.Value = Left(Target.Value, l – 1)  
    Else  
    Exit Do  
    End If  
    Loop  
    End If
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14516)
    
    *   Where would I place this code relative to the original one provided by Sumit? Thanks
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14700)
        
    *   Hello, I’m getting an error on this line –  
        If Len(OldValue) Len(NewValue) Then …  
        Any thoughts? Thanks.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14771)
        
36.  i need help, please do to assist me sir.  
    my problem is how to make dropdown list in excel displayed in 3 rows.  
    eg:  
    A  
    B  
    C  
    when A (row 1) is chosen then B and C also automatically displayed in row 2 and 3.  
    please assist me sir, and thank you so much for your attention.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14462)
    
    *   Hi!  
        Try the code I posted above.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14579)
        
37.  Hi  
    This is a very useful and simply explained video. I have watched few videos. However, this one is the best and simple. like it very much. Thanks.
    
    I need to know how to apply this in multiple columns
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14460)
    
38.  Hi, the macro is working well but when I write in the cell and or erase it keeps the old and new value. How can i modify the macro to make erasing possible? thank you
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14459)
    
39.  Summit, thank you for this great VBA code. How to save this vba code with my worksheet? Everytime I close my workbook then reopen it, the VBA code is gone and I have start it all over again?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14415)
    
40.  sir  
    I need all Excel sheet in all drop down list multiply selection kindly send code or excel formula apply.  
    Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14386)
    
41.  Sumit, this an is excellent macro, thank you. One thing, I have the macro set to return the results with each item on a new line. however, the cell height is not adjusting and my responses are getting cut off. I do have the Wrap text option selected for the cells. I also have the selection macro running on more than one row however it is running all in the same column, so the macro would need to run regardless of the row the data is in. Would you be able to write/or tell me an addition to the macro that will adjust the cell height after it is filled?
    
    thank you so much for your help
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14372)
    
42.  thank you for this great tutorial! I was able to set everything up but then when I tested it , I was still only able to pick one item only. I copy pasted the exact code. can you elaborate on why this would happen? thanks  
    Sabrina
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14364)
    
43.  I used this code a year ago and it worked. Now I wanted to use it again and it isn’t working anymore. I retrieved my old file from last year and the multiple selection I used is gone, only one of the options is left. I downloaded the sample file from this webpage and it isn’t working on this file. HasExcel changed in the meantime and do I need to modify the code?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14356)
    
44.  Hi Sumit Bansal, thank you so much for your help with the coding – I cannot tell you how much it has helped me and made my life so much easier :). Please could you advise if you are able to help with creating a list box in word with the functionality to select multiple dropdowns? I have searched the web and been unsuccessful. Your help will be greatly appreciated. Many thanks.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14351)
    
45.  Can you make multi selection drop down boxes in more than one column?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14348)
    
46.  This works great until I save it and try it again. After starting the spreadsheet again, the functionality fails. I tried saving it as an .xlsm. Any ideas
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14330)
    
47.  Thank you very much for this tutorial, this was exactly what I needed. However, when I use Filter function in this column to sort results, it does not recognize individual word in cells with multiple choices. As exemple, “xxx” will be recognized if standing allone in the cell, but not in cells with two choices, like in “xxx, yyy” – it simply does not appear in filtered results at all. Is there any way to correct this? Thank you!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14320)
    
48.  My scenario. My first column displays a list. The second column displays a list depending on the first column selection. I am able to make multiple selections in the first column. However, the next column will not let me make selections off of the first columns multi-selections if i choose more than one.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14305)
    
49.  What if I select an item and then want to deselect it from list?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14242)
    
    *   Private Sub Worksheet\_Change(ByVal Target As Range)  
        ‘ To allow multiple selections in a Drop Down List in Excel (remove when selection is repeated)  
        Dim Oldvalue As String  
        Dim Newvalue As String  
        Application.EnableEvents = True  
        On Error GoTo Exitsub  
        If Target.Column = 35 Then  
        If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
        GoTo Exitsub  
        Else:  
        If Target.Value = “” Then  
        GoTo Exitsub  
        Else:  
        Application.EnableEvents = False  
        Newvalue = Target.Value  
        Application.Undo  
        Oldvalue = Target.Value  
        If Oldvalue = “” Then  
        Target.Value = Newvalue  
        Else:  
        If Oldvalue = Newvalue Then  
        Target.Value = “”  
        ElseIf InStr(1, Oldvalue, Newvalue) = 0 Then  
        Target.Value = Oldvalue & “, ” & Newvalue  
        ElseIf InStr(1, Oldvalue, Newvalue) = 1 Then  
        Target.Value = Replace(Oldvalue, Newvalue & “, “, “”)  
        Else:  
        Target.Value = Replace(Oldvalue, “, ” & Newvalue, “”)  
        End If  
        End If  
        End If  
        End If  
        End If  
        Application.EnableEvents = True  
        Exitsub:  
        Application.EnableEvents = True  
        End Sub
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14286)
        
        *   I have tried this code and it seems to remove a selected item, but only if nothing else has been selected. That is, if I select item A, and then select item A again, it will disapear. However if I select item A and item B then click item A again to remove it, it does not remove item A. I just does nothing.
            
            Would you have any further suggestions?
            
            Thank you
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14374)
            
            *   Hi Minbee,  
                In my workbook it works with this code. I can remove any item what I want. So also Item A after an item B is selected. So I am not sure why it doesn’t work in your version.  
                The only thing you have to adjust is the column number. (35 in my example) but I assume that you have done that.
                
                Maybe you can post your code here then I can have a look.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14520)
                
        *   Thank you so much! This worked great!
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14529)
            
50.  Hi,  
    I was excited to see your video on this. I have a range that I need to apply this to and it looks like this is mostly for a couple of columns or cells. I need this for a range of D17:W76. Is there a way to alter your code to accomplish this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14232)
    
51.  Hi,  
    I’ve created a worksheet with the multiple selection functionality in a protected sheet, however I can’t get the VBA code to run whilst the spreadsheet is shared with multiple users. Please could you help or provide any suggestions for a novice like me. Thanks. Dan.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14215)
    
52.  Hey! Thanks for this – super useful. Quick question; I need this code to appear twice in the same sheet. Once with “, ” and once with ” “. When I try to use them both I get compile errors. Appreciate any help!!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14212)
    
53.  How can I use the non repetition code for multiple columns on the same report?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14211)
    
54.  Works like a charm. THANK YOU!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14208)
    
55.  I am using the code that allows repetition, but when i select the same value multiple times it does not append the target.value. For instance i select 0.1, 0.2, 0.1 and the output is just 0.1, 0.2
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14183)
    
56.  Tried it in a row. Worked perfectly well . Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14180)
    
57.  when i try to enter the line ” Target.Value = Oldvalue & “, ” & Newvalue” i get an error message, it highlights the “,” and a box pops up Saying compile error “expected end of statement. What do i need to do to fix that.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14171)
    
58.  Hi, could you please provide a code for the same first example above such that I can delete a value after choosing it from the drop list?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14132)
    
59.  I have 3 columns in which I wanted to apply the multichoice option, but each column has its own options. Is it possible to do this?
    
    Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14122)
    
    *   i want to do this as well. can anybody help?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14311)
        
60.  This looks great but for some reason the code does not work here… I copy paste it but still I cannot make multiple choices from the list. :- appreciate some help!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14120)
    
    *   did you get an answer? I am having the same trouble.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14250)
        
61.  Hi,
    
    I need help modifying the code.  
    I want to appear “Please select” in the Target.Address/Target.Column.  
    I tried but i failed. 🙁
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14114)
    
62.  I love the one with no Repetition but it has a flaw I need help with. I disable error and ignore checkbox via the data Validation this way it give me the option to have a drop down with multiple selections but also the ability to still add my comments so to speak it then repeats the selected selections. The next issue is that when I select 2 options in my drop down list and then try to delete one it then duplicate and add them back to speak. Are we able to get one where I have be able to delete one of my selection if I no longer decide to have multiple selection with it then repeating. Same goes for when I want to add my own comments that is not on the drop down list source. I I’m basically looking for a drop down list to be able to pick multiple options and still be able to add my own comments in the same field with out causing any errors or it duplicating my selected options and be able to delete.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14107)
    
63.  I inserted the code so that the checklist would appear in every cell in column E but it didn’t work. I made the change:
    
    If Target.Address = “$C$2” Then
    
    with this line:
    
    If Target.Column = 5 Then
    
    My validation list is on another tab. Is that the problem?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13984)
    
64.  Hi Sumit, i have inserted the code for multiple selections (without repetition) within a column for multiple sheets (same template) but it does not work. Not sure if the cause is conditional formatting of the options (which I’ve coloured) or if it’s something else? Appreciate your help here, thank you!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13931)
    
65.  How do I create multiple selections in multiple columns in the same file? Right now, I can only get the code to apply to one column at a time.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13922)
    
66.  Hi Sumit,
    
    Thank you for your great assistance in multiple selection drop down list through a VBA code. I have used it and it is working fine for me. Only, change in the output I need per my project’s requirement is, can we have the selections in either new rows or columns rather new line? It would be a really helpful if that is possible.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13917)
    
67.  I copied and pasted your code. It does not work when I use the target.colum line. see below:
    
    If Target.Column = 3 Then
    
    The above code does not work unless I put I write with with quotation marks –>
    
    If Target.Column = “3” Then
    
    Now I can choose multiple items, however, I get a Data verification error. When I use the debugger it points to:
    
    Application.EnableEvents = True
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13891)
    
68.  Can I do this for a whole workbook?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13890)
    
69.  I have successfully created a multiple drop-down list without repetition – thank you. However, when I apply the “Me.Protect UserInterfaceOnly:=True” code, so I can use it when the sheet is protected, it doesn’t hold its password protection and by simply clicking un-protect the spreadsheet becomes exposed. Do I need more code?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13876)
    
70.  This was awesome, thank you! How do I reset a list where selections have been made 🙂 My list is LARGE – 123 unique values
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13858)
    
71.  Hi Sumit,
    
    Your code is a life saver, Thank you. It saved a lot of re-work for me.  
    However in my case, the data is getting duplicated in case I am selecting one item multiple times. Any suggestions?  
    Excel Version: MS Excel for Office 365 MSO (16.0.11929.20708) 64-bit
    
    List of values:  
    One  
    Two  
    Three  
    Four  
    Five  
    Output (upon multiple selection):  
    One, Two, Five, One
    
    Regards,  
    Dj
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13857)
    
72.  Hello, this was spectacular thank you for creating.  
    The code you provided to enable the code while protected is great – HOWEVER it is constantly protected. I cannot switch it off? Everytime I make an adjustment to a cell, I have to unlock it again. How do I make it so that it looks ONLY when I switch on protection? Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13834)
    
73.  If you want to add more than 2 column then place column numbers in below formula. I did it from column no.9 to no. 20. If and then should be used in start and end only.
    
    If Target.Column = 9 Or Target.Column = 10 Or Target.Column = 11 Or Target.Column = 12 Or Target.Column = 13 Or
    
    Target.Column = 14 Or Target.Column = 15 Or Target.Column = 16 Or Target.Column = 17 Or Target.Column = 18 Or
    
    Target.Column = 19 Or Target.Column = 20 Then
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13802)
    
74.  Hi.. thanks a lot for sharing this, it’s really helpful. But is there a way to limit the amount of selections one can make in a drop down list to say, 5? Currently there’s roughly ~25 items in the list and I only want them to be able to select a maximum of 5 of those at a time. Thanks you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13772)
    
75.  Hi,  
    Thank you for this very comprehensive tutorial!  
    I wanted to know if I can have different multiple selection drop-down menus for different columns. I explain: on a worksheet named Services provided I have in column B a drop-down menu for target clients; in column C a drop-down menu for basic services and in column F a drop-down menu for Specific areas of expertise… how can I do this?  
    I would really appreciate you explaining it to me!  
    Thanks  
    Alice
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13767)
    
76.  Very useful information and easy to follow. Thank you very much.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13755)
    
77.  Sumit,  
    Thank you very much for this tutorial. However I have a question not covered by those answered above. I would like to have the same ability in two columns. When I change your code from $C$2 to column. “38” I also want the same ability in column 40. I tried Columns. (“38 & 40”) in the command, however neither column will allow multiple drop down selection. Yours is the very first macro I’ve worked with so I know syntax is crucial. Can you offer any help.  
    Thank you  
    Mike McClure
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13749)
    
78.  Can I modify multiple selection code (no repetition) when Target.Column = 6 so that the header is not affected? Currently, the Column F header is following the “separated by a comma” rule with any edits to the header text in Cell $F$1.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13728)
    
79.  Hello and thank you for this amazing presentation! One question- how would i modify this to do multi-selects in multiple columns? For example, if i have a set of drop downs in columns B,C, D with unique selections, how do i modify the code to capture this functionality for multiple columns? best.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13726)
    
80.  Is it possible to apply this code to an entire column?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13695)
    
    *   Hi! I was wondering the same with specific columns and i did it like this and it worked, hope you can get some help of this: If Target.Column= 2 or Target.Column = 4 Then
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13706)
        
81.  How can you edit the text in the cell once selected? I tried to remove a line of text and i get an error each time.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13686)
    
82.  When the sheet is protected then the ability to add more than one selection. For example, I can select one item and it will replace whatever previous item was there instead of adding it to a comma-separated list.
    
    Thoughts?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13682)
    
83.  So, I just found this page, and am trying to get this to work. Currently, my drop down list text is located in Sheet 2, but the drop down box itself is in Sheet 1. How would I get this to work?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13679)
    
84.  This is great, works well, many thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13665)
    
85.  sir how can i create 2 rules (multiple dropdown selection) in two or more different column?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13664)
    
86.  Hello, Sir, I have tried this option for my excel report for SQL database parameters to pass multiple values for one parameter but my report showing blank when I select multiple values .is there any option for this please suggest
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13657)
    
87.  Thanks a lot, very clear, good programmer
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13641)
    
88.  Real well explained, I finally found my solution. thank you very much for explaininf and giving simple code for each cases
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13636)
    
89.  Thank you so, so, so much! This helped me a lot with some work related issues!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13625)
    
90.  Hi,  
    Can I remove existing selection by clicking on the same value in drop down list.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13541)
    
91.  The spreadsheet works when I save however this is contained within a shared folder so when my colleague accesses the code no longer works. How do I fix this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13537)
    
92.  Thank you Sumit Bansal. Question: I have another column in the same sheet I would like to put a multi select drop down list into. How can I do this? I have tried changing the Oldvalue & Newvalue to Oldvalue 4 and Newvalue4 for the additional column but it does not work. Do i need to set a range in this line “If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then” ?  
    Thank you
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13430)
    
93.  I tried emailing my spreadsheet with the added code but when they get the file the code in not there. what happens to the code when I email the excel file to someone?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13427)
    
94.  Why can’t colleagues see the multiple selections in a drop down list? It’s the same document on a shared server.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13423)
    
95.  As of now, the multiple selections are separated by a comma. How can I change this to separate and show in in different columns?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13420)
    
96.  Awesome Man!!!!!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13410)
    
97.  Hi. Thank you for this guidance it is excellent and very easy to follow. I have read all of the comments and there are many unanswered questions about subsequent filtering of data using the multi select cell information. I have encountered this issue too. Can you help? Is there a way around this? Basically I have multiple filters informed by the drop down. Where a single selection is made the filter finds it. Where multi selection is made the filter cannot since there is no exact representative value in the data (e.g. Multi select shows East, South but the data column contains East). I guess I need the filter to recognise and search for each individual selection separately. Is this possible? Would be extremely grateful for advice. Thanks in advance.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13399)
    
98.  Hi,
    
    What if the target at different worksheet?  
    Tq
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13369)
    
99.  Thank you so much! I was using the macro way which is 10x complicated than this. This is a genius method.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13366)
    
100.  Thank you so much! Your posts have got me out of sticky situations more than once!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13349)
    
101.  OOPS.. had to fix the if statement to handle rows higher than 9
    
    If Target.EntireColumn.Address = “$G:$G” And Mid(Target.Address, 4, Len(Target.Address) – 3) > 1 Then
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13333)
    
102.  this is EXACTLY what I was looking for, thank you!  
    My contribution to this: For those looking to apply the multi-select functionality to a range of cells… just replace the IF statement with this:
    
    (assuming you want this validation rule to apply to the range of cells c2 = c10)
    
    If Left(Target.Address, 2) = “$C” And Mid(Target.Address, 4, 1) > 1 And Mid(Target.Address, 4, 1) < 11Then
    
    I just tested this out successfully in my spreadsheet
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13329)
    
    *   oops – had to fix for rows past row 9, also modified to col G
        
        If Target.EntireColumn.Address = “$G:$G” And Mid(Target.Address, 4, Len(Target.Address) – 3) > 1 Then
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13334)
        
        *   I am going to apply your code but would like to thank you first!
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13365)
            
        *   Hi Charles, I am getting a syntax error when using this
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13389)
            
    *   Btw, be aware of the double quote!
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13367)
        
103.  If you want to apply this for all data vallidation on the sheet then ?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13274)
    
    *   Amit see my answer above ‘multi-select functionality  
        to a range of cells’
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13330)
        
104.  You have made my day with all of your “How To” directions on this site! Allowing for multiple selections from a drop down box is great! Is there a way to make this a bit easier by making all of my selections at once?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13250)
    
105.  How can i delete items from the list?in the above program if i want modify then i have to delete everything and select once again is there any method to just delete required items?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13237)
    
106.  This is excellent and really useful. I have one question though.. if I select multiple items from drop down and want to get back again to single or lesser item? How do we do that?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13230)
    
107.  Hi,
    
    In the multiple drop down I need each item selected to be numbered as (1), (2) etc..  
    Can someone help me by providing the VBA code for the same
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13214)
    
108.  I need to create multiple drop-downs in a range of cells example m4:m5000 . How can I do this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13179)
    
    *   see my comment on ‘multi-select on a range of cells’
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13331)
        
109.  Q: if I wanted to run a Countif function would it recognize each selection separately or think it was one long value?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13145)
    
110.  Hello, Could you please help me if I want to one dropdown in column 4 another in column 5, another in 6 and so on.  
    Please be kind to help  
    Best Regards
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13095)
    
111.  How can you correct a mistakenly added item from the drop down menu. If you were to choose multiple items and then want to remove one later, it is not allowed. Please advice
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13020)
    
112.  Thanks So much, this was much easier than adding a checkbox for selection
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12974)
    
113.  I have a table in Sheet named Abst. Range A Q 2 4 to A R 4 7
    
    Similar to Following Table:-
    
    …. A Q ……..AR
    
    24…Blank….Blank
    
    25…A……….B
    
    26…C……….D
    
    27…E……….F
    
    etc. All Values are Text.
    
    In column I & J I have multi select boxes. In Column ” I ” Drop Down List from Table A Q 24 to A Q 47 While in Column ” J ” from table AR 24 to AR 47. These boxes give comma separated values.
    
    I want in column J to select corresponding automatic comma separated values as per the table. Such as in above example:-
    
    If I select In column” I ” A,C,E  
    The column ” J ” should give B,D,F automatically
    
    Can you suggest me the proper code ?
    
    Thank you.
    
    Prakash Kulkarni
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12969)
    
114.  Hello, this question was asked below but there was no response to it, how do you use this code in a column in multiple cells and across multiple tabs?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12956)
    
115.  I entered the VIB Code, but it doesn’t work.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12952)
    
116.  How do I clear contents if they made a mistake or the item selected has changed?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12942)
    
117.  thanks for the code, work great !!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12937)
    
118.  how do I eliminate the data validation error? I can click the error message to ignore the error, but I would like to get rid of it
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12936)
    
    *   Hi Keith, were you able to finally get rid of the yellow triangle with an exclamation on the top left corner of the cell? I am assuming that was what you were also getting. Please let me know. Thanks.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13440)
        
        *   Nevermind. I got it sorted by converting it from Table to Convert to Range.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13442)
            
119.  I am trying to get the multiple selections without repeat to work in two columns next to each other. Each has their own selection list. When I do one column it seems to stop the code from the other and vice versa. Not sure, but somehow I am overriding the one with the other. Any thoughts on what I am doing wrong?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12913)
    
120.  This is great, thank you. Once I have multiple selections the filter function doesn’t seem to work – I want to be able to filter by one of the selections and see any line that contains the selection
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12905)
    
121.  Hi,  
    The is working nice, but I try to make a vlookup based upon its but it not work can you help me
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12899)
    
122.  Thanks for the multiple selection tip, the problem I has is that I would like to have multiple selection for columns 2,3,4,5,6,7,8,9 and I have tried to amend with no luck so far. Help appreciated please.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12894)
    
123.  Thank you Sumit for your instructions on multiple selections from an Excel drop-down menu without repetitions. I however found it funny that soon after protecting the sheet this function ceased working and went back to default of selecting just one item. What could be the reason?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12892)
    
124.  Hi,  
    I used your codes for the multiple selection dropdown list without repetition and I can’t get it to work on my Data Entry form combo box. I’m thinking it’s because I’m not referencing the right location of the list which is not the cell it self but the combo box. Do you have solution for this? I appreciate all the help I can get….Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12889)
    
125.  I’m using this so to reference engineer experience against applications. I have a list of global applications in the business, then a list of engineers. I’ve created three columns ‘Basic, Intermediate and Advanced’ and the engineer can place their names in the relevant columns. However, if an engineer has basic skills on one of the applications, then increases his knowledge and becomes Intermediate, how do I get it to remove him automatically from the Basic column if he selects his name under Intermediate?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12874)
    
126.  I want c2 cell is depend b2 so that I will use indirect formula or any please suggest me
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12825)
    
127.  amazing ! you really save my life with that code we can not thanks you enough ,thank you millions and more !
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12821)
    
128.  Thank you so much for this article!  
    I will try my best to explain the issue I am encountering. I don’t know if I have all the correct technical names.  
    I have successfully created dropdown lists which allow for multiple selections without repetition for three columns. These dropdown lists are within a table for which I would like to be able to sort and refine searches. Is there a way for criteria to be recognized individually in the table rather that a concatenated value for all the possible variations? Again, thank you for your this article, it has been most helpful!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12786)
    
129.  Amazing – thank you for this thread.
    
    Question: if you want to amend/remove a selection you need to remove and start again. Any way when you select the same again, it simply removes that selection?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12757)
    
130.  NOOOOOO! I got it to work, but then it stopped for some reason! I’ve tried everything! (rebooting, starting over, downloading the sample and adding my information there) I cannot get it to work again! On any excel document. I’m not even sure what to do now!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12739)
    
131.  Oops! I meant CAN’T! 🙂
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12692)
    
132.  I need to create a multiple selection drop down list for an entire column–except the first few cells. Do I have to add the thousands of cells to the formula one by one or is there a short-cut? Obviously, I can add all of them… Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12691)
    
133.  This is really cool code. If I specify a certain cell as the target address (can’t do column because there are other cells in the same column where I can only allow one option to be chosen), is there any way to use offset or relative references so that the target moves accordingly if, for example, I insert rows above the cell that is being referenced in the code? Thanks in advance!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12686)
    
134.  When I selected the the wrong entry from the drop down, it doesn’t give me the option to delete it. I am receiving an error message: “The value you entered is not from the required list.”. How do I get this fix?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12649)
    
    *   delete the cell & again select
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13157)
        
135.  This has been fantastic for me. One thing I’ve found is when I want to manually delete a selection using the backspace key it will instead delete the value I wanted to keep and insert the value I wanted to remove. Is there a way to have the backspace key actually remove the value you want deleted? I have the code for removing an item by selecting it a second time from the drop down list
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12643)
    
    *   Hi Amanda! I was looking for this code but couldn’t find it anywhere, would you mind sharing it with me? I would really appreciate it.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12651)
        
        *   Hope this is what you’re looking for.
            
            If Target.Column = 4 Or Target.Column = 6 Then  
            If oldVal = “” Or newVal = “” Then  
            ‘Do nothing  
            Else  
            lUsed = InStr(1, oldVal, newVal)  
            If lUsed > 0 Then  
            If Right(oldVal, Len(newVal)) = newVal Then  
            Target.Value = Left(oldVal, Len(oldVal) – Len(newVal) – 1)  
            Else  
            Target.Value = Replace(oldVal, newVal & Chr(10), “”)  
            ‘Allows multiple items to be selected and to deselect
            
            End If  
            Else  
            Target.Value = oldVal & Chr(10) & newVal
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12657)
            
            *   Hi Amanda,
                
                Should this be in addition to the above code or replace the entire code and use this one?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12781)
                
136.  Great tip, thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12642)
    
137.  I am using the VBA code without repetition. What code can I use to deselect a selected item when chosen again. Right now, I can’t manually delete a selected item without getting an error code. I have to start over.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12628)
    
    *   Hi Lex!
        
        I have the same issue. I was wondering if you got the fix for this that you wouldn’t mind sharing.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12650)
        
138.  Damn – What a great tip, thank you so much for sharing, not only the primary code but the options you offered in the Q&A. Truly awesome
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12623)
    
139.  How we can de-select the already selected item from the cell. Do I need to remove all and re-do the selection ? Can we un-select the few one from the list?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12608)
    
140.  I need to remove a entity by double selecting the option. How is that possible?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12567)
    
141.  I cannot get this code to work. Even when I download the file directly from this site, the cells in the downloaded file will not allow multiple selections. Any ideas?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12546)
    
142.  I have a need to allow my users to type in a value for “other”. If I do this with this formula, it appends what ever was input first, i.e. “one, two, one, two, other”. I’m sure there is something easy to prevent this. Thanks for the help and the advice!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12513)
    
143.  Hi,
    
    How to do the same in Google sheets?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12504)
    
144.  Hi, let say we have another column that we need to do drop down but with another list. so in the excel sheet we have now 2 columns where they have drop down list. how can we add the second to the first VBA code?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12503)
    
145.  hi, first of all, thank you very much for your teaching and it is very helpful… here is my question
    
    let’s say I have input the following data in  
    C2 Two, Three  
    C3 Three, Four  
    C4 One, Four  
    C5 Two
    
    then I discover I cannot count the data by “Filter”
    
    what I can do so that I can count out :  
    One x 1  
    Two x 2  
    Three x 2  
    Four x 2
    
    thank you very much for your help !!!!
    
    ruby from Japan
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12484)
    
146.  I have a mutliple drop down list in cell C3, for example, dependent on criteria entered in C1. When the value in C1 changes, how can I ensure C3 resets to blank and does not leave the old values that were relevant to the old value entered in C1?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12454)
    
147.  Hello hello hello. How do I apply this code to the whole row?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12405)
    
148.  Okay, this is super cool! Thank you for all the added code to make each selection show up on a separate line, and work in a protected file. Having the step by step instructions and the code was very useful!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12385)
    
149.  I have this code on my worksheet but when I go to another worksheet within the same workbook with the code (to allow multi-select) it turns the multi-select off on all the applicable tabs. If I save and come back in it turns it on again but when I click on another tab with the multi-select code it goes away again. HELP 🙂
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12364)
    
150.  After finish and save it but next day I open that file ,the link is not working ,means drop down list is working but related drop down list and vlookup link is not working ,equation link also.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12348)
    
151.  Thank you! This was so great and it worked perfectly! I have one question: If you selected One, Two, Three, but want to take the Three out, and maybe even go further and select Four now, is there a way to do that? or would you just press delete and start over with Selecting?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12337)
    
152.  Thanks alot, very handy code.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12336)
    
153.  How can we create multiple selection in 2 columns with dependant values. Eg. In column 1 if we have country names and column 2 states. Then in column 1 we can select 2 countries and then column 2 shows state list only for those 2 selected countries and then we can select multiple states from this drop-down list which showed dependant values, i.e. State names for those 2 countries.  
    I am facing issue where in after selecting 2 countries, the state column is not showing the list of states for these 2 selected countries.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12322)
    
154.  Great code! Does anyone know if you can count items when you have multiple items in a single cell? For example, in cell B2, I have apples, carrots, and bananas selected (apples, carrots, bananas) and cell B3 has banana, grape, and watermelon (banan, grape, watermelon). How would I be able to count the number of times the word banana is seen in the cell range B2:B3?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12317)
    
    *   use below code. It basically counts no of commas and add 1 to it. so indirectly it counts no of items  
        \=(LEN(B6)-LEN(SUBSTITUTE(B6,”,”,””))+1)
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13158)
        
        *   replace B6 by cell which u want to count
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13159)
            
    *   I have a related question! How would I count the number of dropdown selections per cell? In the example above, I’d want B2’s total number of items (apples, carrots, and bananas- so, 3 items) and B3’s total (banana, grape, watermelon- 3 items). Thanks for the help!!
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13788)
        
155.  Thank you! This was great and solved my issue.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12315)
    
156.  is it possible to do any data validation from the multiple selection drop downs ?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12303)
    
157.  Once I have values selected and now want to remove one. What do I do?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12277)
    
158.  Thanks for the great code.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12264)
    
159.  Is it working??
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12251)
    
160.  What if I want multiple drop downs in a row and columns? I want to repeat the same row of options line after line, but only the first line is adding options. The rest are single choice only. Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12248)
    
161.  Great code!
    
    If anyone would like to remove an item from the list by clicking on it again, change the following lines of code:
    
    from Target.Value = Oldvalue & ” ” & Newvalue  
    to Target.Value = Trim(Oldvalue & ” ” & Newvalue)
    
    and
    
    from Target.Value = Oldvalue  
    to Target.Value = Trim(Replace(Oldvalue, Newvalue, “”))
    
    Don’t forget to Save your workbook as “Excel macro-enabled workbook”, so you don’t lose your VBA code every time.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12130)
    
    *   Thanks Jose. However, when i use this it doesn’t delete the comma so I end up with double commas. How could I adjust the code to correct this?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12240)
        
        *   Please try this which takes care the coma as well.
            
            iPos = InStr(1, Oldvalue, Newvalue)  
            If iPos = 0 Then  
            Target.Value = Trim(Oldvalue & “, ” & Newvalue)  
            Else:  
            If iPos = 1 Then  
            If Target.Value = Newvalue Then  
            Target.Value = “”  
            Else  
            Tmpvalue = Newvalue & “,”  
            Target.Value = Trim(Replace(Oldvalue, Tmpvalue, “”))  
            End If  
            Else  
            Tmpvalue = “, ” & Newvalue  
            Target.Value = Trim(Replace(Oldvalue, Tmpvalue, “”))  
            End If  
            End If
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12263)
            
            *   I got this to mostly work. It will never remove the first item I select in the list. I had to copy this code into 2 places to make it work. Do you have the whole code what would make this work all put together?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12278)
                
                *   Dat / Kens , did u got a solution to avoid multiple commas? if yes, then pls do share.
                    
            *   Is there possibly a way to set one value from the list to be exclusive. In other words, my list has Standard, Glass, Tile, Wood. I would like the to be able to select one or more of Glass, Tile, Wood, but if I select Standard, it should prevent adding any of the other values… Or, if other values are already listed, selecting Standard should replace the text.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12586)
                
162.  This is amazing! I had literally just told a colleague this would be impossible. Is there by chance a way to go back to the cell and remove one entry without getting the error message (due to the data validation; list)?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12129)
    
163.  Not working for me
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12107)
    
164.  What is the VBA code modification to enable the drop-down in all rows and columns, not specific cells, rows or column, but the entire spreadsheet?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12098)
    
165.  Thank you for your code it helped me allot with this big project I am working on. If a user accidentally selects and item and was not needed, how do they just clear that item without starting their process all over again?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12091)
    
166.  Its Work only at once however after reopen the file its not working. So i follow the above given steps again still its not working. Im using Excel 2016
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12083)
    
167.  Hello, thanks for the above info. 🙂 Just need help on how to apply the multi drop down selection for multiple columns? I have already tried in 1 column and it works but i tried to add 1 more column and error prompts. Thanks in advance for your help. God bless. 🙂
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12080)
    
    *   I am also looking for an answer to this problem!
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12481)
        
        *   Continued scrolling through the comments, and found the answer in “Muhammad Elboreini”s post! I now realize that it is also in the FAQ, under the 2nd and 3rd questions 🙂
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12482)
            
168.  Can I have the count of the number of selections displayed in the cell and the selection list shall be shown upon clicking the cell. Is it possible.
    
    Because I am working in the construction industry and for my labor allocation I will be selecting the labor names from a list. However, I want to display only the count. The names of labors selected will be displayed upon clicking the cell.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12071)
    
169.  Thank You! Great Information and presentation!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12035)
    
170.  Great solution to a nagging problem. Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12019)
    
171.  This is really helpful. I have finally managed to activate multiple selection of items on a drop down list for more than one column.
    
    Thanks alot.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12015)
    
172.  Very useful article, thanks for sharing
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12014)
    
173.  Hi, i want make this method for 2 diferent cells in the same document but i its working just to one cell.  
    I tried use comand and/or, copy chancing the cell but doesn’t work.
    
    I am very inexperient in VBA, can help me?
    
    Best regards.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12008)
    
174.  Thanks so much for this! How to I apply it to an entire column except the header for that column in line 1? Many thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11987)
    
175.  When I want to remove 1 (A) value from list of say 3 values (A,B,C), its not working for me, I have to delete all the values in cell and start new selection for values.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11963)
    
176.  Do we have to save the file in a macro-enabled template? If so, I saved my data and the VBA code is not functional
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11930)
    
177.  Hello! Thank you very much for this tutorial. But I have one question. What if the drop-down item list is placed in another different worksheet? Is it possible to synchronize this function between different worksheets of the same workbook?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11917)
    
    *   Lea, press f3 under source in the data validation dialogue box to select your dropdown list from any sheet
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11932)
        
178.  Thanks v much .. so helpful.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11906)
    
179.  How would I run this Macro with the same purpose under multiple columns with different drop downs for each column (drop downs are already setup)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11901)
    
180.  2 things. 1.I tried using a range instead of cell address and it would not work. Can that be done. I even changed the Target.Address to Target.Range. 2. My drop down list has a default of “Select One”. How can that be replaced with the first selection? As it works now my selection is just added to the Defaulted ” Select One”.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11855)
    
181.  Vert nice 🙂
    
    How would one extend this to work when sharing via O365 ?
    
    I’ve tried& it doesn’t work. Not sure if it’s a limitation from O365 or if I need additional steps.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11754)
    
182.  I have copied the code correctly but i still cannot select multiple items at a time.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11705)
    
183.  I did exactly as per your instructions. The only difference is the cell change based on my workbook (H2 instead of C2). The dropdown still works as a single selection. New selection replace the old.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11691)
    
    *   Change  
        If Target.Address = “$K$2” Then  
        to  
        If Target.Column = “$K$2” Then
        
        This worked for me to apply to a whole column, but I have not figured out how to apply to multiple columns as yet.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12252)
        
        *   You can use the following to use it for multiple columns:
            
            If Target.Column = 2 or Target.Column = 3 Then
            
            This will make this work for column 2 and 3
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12254)
            
            *   Hi Sumit, Can the VBA code work for columns that are not consecutive? I can add VBA code for columns 14, 15, 16. But let’s say I have multiple selections in column 3 and another set of multiple selections in columns 14 and 15. How would the code look?
                
                Code below does not work:
                
                If Target.Column = 3 or Target.Column = 14 or Target.Column = 15 Then
                
                And following question, if in sheet 1 cell A1 I has vba code with multiple selections, can the same selections be returned in sheet 2 cell B2? That way the data auto populates and does not require to input the vba code for sheet 2 and manually select the second time.
                
                Thank you for taking the time and educating us.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12576)
                
                *   I have the same doubt, I was able to do it with consecutive columns, but when they are not, it no longer works, did you find a solution?
                    
184.  how to make drop down list only can choose 2 items by user. Even in drop down list have many choice
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11630)
    
    *   I was wondering the same thing
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13205)
        
185.  How to remove mistakenly selected drop down? Please suggest
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11591)
    
    *   your issue resolved? even I want the same answer
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11964)
        
        *   An easy way that requires no code is to add a blank cell to your range. when you select the blank cell it clears the rest out.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12403)
            
186.  How do I unselect the items from the drop down list? I have created the multi select no repetition?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11575)
    
    *   I am having the same exact problem. Did you find an answer?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12629)
        
187.  Hi, is it possible to add a function that unselect an item from a drop down list? I am using it to specify users of equipment, and let say we had 5 users, but now one of the users is not using equipment anymore. So I wish to remove just one user. Now i need to remove everyone and select them all over again….
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11573)
    
    *   Same problem
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11748)
        
    *   Same issue from my side, and if I also go to the cell and delete, doesn’t help because it will appear once again all the options selected previously. In my case, I just have remove all the code from VBA because it doesn’t help…It’s sad because it is a good idea, however from what it see the code doesn’t take this in consideration and anyone as provided a solution either…If someone has figure out something it would be nice to know.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12109)
        
188.  The XLSM file with VB scripts when opened in other PCs the VB script doesn’t work. Why?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11557)
    
189.  Incredibly helpful tutorial – thank you!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11540)
    
190.  Hi Sumit,  
    The code was really helpful.Thank you.But if there is an option “All” in the list, how to include that so that once this option is selected,no other option can be selected.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11508)
    
191.  Hi
    
    Thank you for this quick fix, great!
    
    How do I lock the values of a cell (data range) when I make a table of many rows?
    
    Each new row creates a new range of data values, selection +1 for each new row.
    
    Thx!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11495)
    
192.  How can I remove a selected item in a multiple drop down list?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11460)
    
193.  How do I apply this to other columns and cells within the same sheet?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11432)
    
    *   Hi Peter, I have the same question…
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11586)
        
194.  So easy to understand and replicate in my documents. Thank you!  
    Can you please help with another issue I have in regards to macros and multiple section of various sheets for PDF conversion and/or printing.  
    Can you help?  
    Mike H
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11400)
    
195.  Can I make the multiple selection functionality work in a sheet protected with a Password?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11399)
    
196.  I found this solution worked perfectly, but when I opened the workbook again the ability to make multiple selections no longer worked. I notice Rachel also commented below having the same issue. Is there a fix?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11313)
    
    *   Hi Karen. I fixed this by clicking the ‘Enable Content’ button in the yellow bar when you first open up the workbook. Otherwise the macros are disabled.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11369)
        
197.  In case of multiple columns, if dropdown is not there and user manually enter the data, that data also concatenating. For e.g. IF target column is C, now enter 1 and press enter, then press 2 and enter. Both digits concatenated(1, 2). How to stop this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11289)
    
198.  Thank you for sharing this!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11283)
    
199.  Hello! How do you make the items are sorted alphabetical in every cell?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11278)
    
200.  it doesn’t work. I went step by step few times and it does not work
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11215)
    
201.  Hi Sumit. This really great and helpful. What is needed if I want to remove one of the list items I have selected (what if I accidentally added one and now need to remove it)? Thank you for your help.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11212)
    
    *   Hi Michael, I would like to know this also, did you find a solution?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11273)
        
        *   I am too looking for a solution to remove an item from the list.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11511)
            
            *   Try deleting all the selected items and then add them again.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12111)
                
202.  HI!!  
    I need to create multiple drop-downs in all the rows. How can I do this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11204)
    
203.  Followed your video and no luck
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11198)
    
204.  how do you use this code for a range in a workbook containing multiple worksheets
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11193)
    
205.  These steps work perfectly, but when I close the file and reopen, I can no longer select multiple items. I’ve tried several fixes. Any thoughts?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11191)
    
206.  This is great but what if I make a wrong selection. How do you then remove or change it?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11170)
    
207.  Will this work for multiple sheets if I update in Module
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11169)
    
208.  Hi,  
    Thanks for the code,very helpful. Now how do i change this line to apply the macro from cell H4 to H50:  
    If Target.Address = “$H$4” Then
    
    Thanks a lot
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11149)
    
    *   Found it, need to replace the line by:  
        If Not Intersect(Target, Range(“H4:H50”)) Is Nothing Then
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11150)
        
        *   Hello, I wasn’t able to get this to work when I replaced if Target.Address=”$H$4″ Then with If Not Intersect(Target, Range(“H4:H50”)) Is Nothing Then. Any suggestions?
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12955)
            
209.  what is the code for dependent data validation. Your code desnt works in that case. Can you please help
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11139)
    
210.  Hello, I’m working with Excel Online, and do not have a developer tab. Is there a way to do this on the online version?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11111)
    
    *   You can add the developer tab by going to File>Options>Customize Ribbon>Check Developer tab> Click OK
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11470)
        
211.  This was exactly what I needed. Followed your steps and it worked perfectly! Thank you!!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11066)
    
212.  Using your multiple option list – I am trying to put in more than “one change action” on a worksheet and it wasn’t working. I tried a few more things and still no dice.
    
    Do you have the code that you could share? I am sure there is a trick to it.  
    Vanessa
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11057)
    
213.  I have followed all of the steps that you have provided and i am getting an error. – Compile error- what does this mean and what do i need to do to fix it so that i may be able to select multiple different items in the drop down menu. I am also needing this to go from R2 to R300
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10996)
    
214.  How I can have the different logic in 3 different column of same sheet. Please suggest
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10953)
    
215.  When I protect the worksheet, it will not allow users to multiselect in the cell. Is there a way to fix that?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10952)
    
216.  This is great. Thank you for sharing the code. I want to do more out of this, however, there are some problems.For eg., I cannot delete anything added by error. My teammates running this on Mac face problem where the highlighted value from the list gets added if one wishes to abort by pressing ESC.  
    Any ideas on how to implement such changes ?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10935)
    
217.  FANTASTIC! WORKED LIKE A CHARM Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10913)
    
218.  How can i make multiple selection dropdownlist work in all columns of a worbook
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10855)
    
219.  Thanks for this.
    
    how to make the list visible while selecting more than one item from the list. now if i want to select 3 items from my list, i have to click 3 times and select each one separately. would more convenient if the list stays open until i finish selecting my items.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10798)
    
    *   Yes….this!!! How to keep the drop down open?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14222)
        
220.  Thank you, this is helpful! In my list, I have a wildcard (Other: \*\*\*), that I want people to be able to replace with an additional response. However, when I do that with the above code, it copies what I have listed and then shows it again with my changes.
    
    i.e.: First choose “Option 1”, then chose “Option: \*\*\*” which I change to “Option 4”. The output is “Option 1,Option \*\*\*,Option 1, Option 4”. I want to get rid of “Option \*\*\*” and “Option 4”.
    
    Any suggestions?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10797)
    
    *   Thank you, Sumit for this very helpful instruction. I have the same issue as Benny. I have a list of stakeholder names and want to provide people with the option to write the name of a stakeholder outside of my list. Disabling the Error Alert in data validation allows me to do that. However, when someone selects an option (e.g., finance) from the list and then writes the name of a new stakeholder, I get: Finance, New Stakeholder, Finance, New Stakeholder.
        
        on the other hand, if someone types the name of the new stakeholder first and then select from the drop-down list, I get: New stakeholder, Finance
        
        Is there any way to fix this to make sure we get the same results whether people type before or after selecting from the existing list?  
        Thanks again.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11444)
        
221.  Your code has nearly got me to what i need done , Many thanks. I just need to be able to select more than one on a drop down list on spacific cells, Currently any drop down box in colum c but ideally need to just choice for eg c13, c16 ,e16 can this be done
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10778)
    
222.  I need to add multiple selection in just spacific cells can this be done
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10777)
    
223.  I need to create multiple drop-downs in multiple columns (like C and F). How do I get this for all the cells in these columns with multi-select functionality?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10776)
    
224.  dear sir,  
    very informative. can you please tell me how to apply multiple selections in multiple column in a protected sheet?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10768)
    
225.  I have Excel 2010 and cant seem to get this to work. Any ideas?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10736)
    
226.  Amazing! Thank you so much for sharing your expertise! I had never used any code of any kind in Excel and your step-by-step tutorial made this simple to execute.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10728)
    
227.  Is there any way to modify the code so that I can manually drag a cell’s contents into another part of the table? In the table I have built, each user has one entry per row, but they should be allowed to drag that cell to another column in the same row. As the code stands, the only way to do this is to delete the cell’s contents and retype it in the new column, which is not ideal.
    
    Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10727)
    
228.  I really need to know if there is a code that allows to remove the selected object in the multiple selection list. Please, it will be really helpful.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10723)
    
229.  Do you know if Excel have the function to have fillable group populate after you select from a selection list?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10713)
    
230.  Thanks Sumit for this excellent trick. This worked like a charm. Can you please advise, how can I now count the number of selections made?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10697)
    
231.  I just finished using your code for reoccurring choices. Thanks, it works great. My next task is to work on exporting it to an Access DB.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10696)
    
232.  First, Thank you. This is extremely helpful and it worked! I just have one issue. It changed my date format. My list has a date format of mmm-yyyy. When I add this VBA code it allowed multiple selection, but changed the date format from DEC-2018 to 12/01/2018. Is there someplace in this code I can specify the date format mmm-yyyy??  
    Thank you in advance! Greatly appreciative of the help.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10690)
    
233.  How can unselect item from selected?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10653)
    
234.  I have copied your VBA without repetition but it doesn’t seem to work. Note I made two changes – (1) replaced the target address to $B$9 and (2) the spacing between selections from “,” to vbNewLine.  
    Can you please give me ideas why this doesn not seem to work?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10634)
    
235.  It worked like a charm, instruction and layout is very clean and clear. thank you so much!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10619)
    
236.  Hi I have just built my spreadsheet which is perfect. Now I need to make one of my drop downs editable. When you put other and want to put in an explanation.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10596)
    
237.  I’d like to alpha sort the multi pick list results so that the list displays alphabetically, not in the order it was selected. Any suggestions?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10586)
    
238.  Hi, Thanks for this helpful guide. I copied the VB script and changed the column from C to P and it worked – however I needed to create multiple drop-downs in the entire column ‘P’ rather than C – when I followed the instructions given for this is only worked on column C – and I could not see what I needed to change to make it point to column P. Please can you advise what I need to change in the code to make this work. Many thanks,  
    Jenny
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10577)
    
    *   So I figured this out now – I just needed to replace 3 with 16. However, I can see that there is a problem trying to deselect an item. I see other queries about this – is there a way to do that please.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10578)
        
239.  Dear Sumit, thanks for the great code,it works fine with me however when i send the excel file to my college they couldn’t open the file they had the following warning ( this message had contained attached files that deleted during attachment filtering .xlsm) do you have an answer that could help me please
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10556)
    
240.  How can we delete only one selected value form multiple Drop down option
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10527)
    
    *   Try this:
        
        If InStr(1, Oldvalue, Newvalue) = 0 Then ‘ Add  
        Target.Value = Oldvalue & vbNewLine & Newvalue  
        Else ‘ Remove  
        If InStr(2, Oldvalue, Newvalue) = 0 Then ‘ 1st entry  
        If Oldvalue = Newvalue Then  
        Target.Value = “”  
        Else  
        Target.Value = Replace(Oldvalue, Newvalue & vbNewLine, “”)  
        End If  
        Else ‘ Not 1st entry  
        Target.Value = Replace(Oldvalue, vbNewLine & Newvalue, “”)  
        End If  
        End If
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10692)
        
        *   Thx Hyperion135:  
            had to make a few changes to your code.  
            Here is what your final code looks like inserted in the original “without repetition code” provided by Sumit Bansal.  
            Works like a charm!  
            ‘ To allow multiple selections in a Drop Down List in Excel (without repetition & delete selected value from dropdown list function)  
            Dim Oldvalue As String  
            Dim Newvalue As String  
            Application.EnableEvents = True  
            On Error GoTo Exitsub  
            If Target.Column = 6 Then  
            If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
            GoTo Exitsub  
            Else: If Target.Value = “” Then GoTo Exitsub Else  
            Application.EnableEvents = False  
            Newvalue = Target.Value  
            Application.Undo  
            Oldvalue = Target.Value  
            If Oldvalue = “” Then  
            Target.Value = Newvalue  
            Else:  
            If InStr(1, Oldvalue, Newvalue) = 0 Then  
            Target.Value = Oldvalue & vbNewLine & Newvalue  
            Else:  
            If Oldvalue = Newvalue Then  
            Target.Value = “”  
            Else:  
            Target.Value = Replace(Oldvalue, Newvalue & vbNewLine, “”)  
            End If  
            End If  
            End If  
            End If  
            End If  
            Application.EnableEvents = True  
            Exitsub:  
            Application.EnableEvents = True  
            End Sub
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10730)
            
241.  I need to use Multiple select drop down for Marge Column Example :–  
    I Have Marge C2 , B2 , D2  
    What address do i need to provide
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10526)
    
242.  I have managed to get each selection to be on a separate line within the same cell, however when using that cell to place on another sheet within the same workbook the two are pushed together again. Is it possible to adjust this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10521)
    
    *   Facing the same issue if you know the answer please let me know.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11113)
        
    *   Hi Hollie, how did you manage to get it on a separate line in the same cell? I really need to do this but I can’t figure out how.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-12324)
        
243.  How do you deselect an item? I used the code without repetition, but now I want to deselect and item, but nothing happens and I can not delete the item. For example I select one, two from drop down list. Now I do not want two, how do I get rid of it? Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10491)
    
244.  Hi there, this doesn’t work when I protect the worksheet. I am using this code to make a rudimentary form, so I want to protect the other cells from editing. The cells that contain the dropdown are not protected but the vba still doesn’t work. As soon as I protect the worksheet the drop downs only allow a single selection. What can I do to make this work. My apologies if this is answered somewhere and I didn’t see it.
    
    Thanks for the great site and sharing your Knowledge!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10480)
    
245.  This works great. I am having a problem counting the selections now. I have a separate count section that every time I select “white” in a column, it will then count those occurrences in another section. Now when I select “white, Black, native” the count doesn’t work. How do I fix this issue? Basically, I want to be able to select multiple options in a drop down and have them be counted separately. The code I use for the count is =COUNTIF(C:C, “BLACK,”)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10469)
    
246.  This worked and was so easy! Thank you so much!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10452)
    
247.  I’ve managed to do everything but my multiple choices still kicks out the previous choice. I have gone to address and changed it to column and on $c$2 to 4 as I want the whole column.  
    I’m doing this for a non for profit service dog trainers so we r not techies. I thought I was following the directions is my software or system too old? It really need this little thing it could change our who training program. Thank you in advance I feel you were very easy to follow but I am missing something.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10451)
    
248.  Hi Sumit – your VBA instructions are great and I love that you’ve thought about all the other uses (ie duplicates / non duplicates, separate line in cell) as it’s perfect for what I want! I’ve done some tests which all work fine and will add the code to my working spreadsheet. Fingers crossed!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10441)
    
249.  I noticed that after adding the codes that allows me to select item once, I can’t delete the last input if it was incorrectly selected. It will give me validation error message. How do I counter this issue?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10435)
    
250.  can I applied this for other columns in the same worksheet?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10414)
    
251.  You are brilliant! thank you very much for posting this. It seems to work great!!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10405)
    
252.  Thank you for this code, works great. How do you deselect an item? I used the code that does not allow selection of the same item but now I want to deselect but nothing happens and i can not delete the item. For example I select one, two from drop down list. Now i do not want two, how do i get rid of it. Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10401)
    
    *   I also want to know this
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10409)
        
253.  How do I alter this code so that there is an ending row for the multiple selections of the drop-down list?
    
    For example, I have a table on excel with a drop-down list in columns 2 and 3 (B and C). I would like to alter this function so that at the bottom of this table, the function stops. I would also like to be able to use functions, such as count in column 4 which is D, on excel.
    
    All help is appreciated, thanks so much!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10358)
    
254.  I cannot make it work. I downloaded the file to see what the problem was and I cannot make it work with that either. I can still only have one selection from my dropdown box. What am i doing wrong?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10342)
    
255.  Thanks for the tutorial but I think I must have missed something.
    
    I put information for drop down list in Sheet 2.  
    Sheet 1 – created drop down list and targetted information in Sheet 2.
    
    Pressed Alt-F11 and got the Visual Basic for Applications (VBA) screen, selected Sheet 1, pasted the code and closed VBA.
    
    Tried to select more than one item from drop down list and only got one item showing at a time.
    
    Reopened VBA, deleted code from Sheet 1 and copied the code to Sheet 2 then closed VBA.
    
    Tried to select more than one item from drop down list and only got one item showing at a time.
    
    Not sure if need to have a particular cell or sheet selected before Alt F11?
    
    Using Microsoft Office 365 ProPlus.
    
    Cheers.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10315)
    
256.  How can I get the code to choose items in a dependent dropdown list? Suppose I have a different list in each dropdown?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10314)
    
257.  Thank you. Hope this will help this old man learn and understand excel
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10295)
    
258.  I copied and pasted the code and it works!!!
    
    now, how do you sumifs multiple values from multiple drop down list using named ranges ?  
    i.e. suming multiple product groupings as well as multiple regions .
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10262)
    
259.  I copied and pasted the code and it works!!!
    
    now, how do you sumifs multiple values from multiple drop down list using named ranges ?  
    i.e. suming multiple product groupings as well as multiple regions .
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10261)
    
260.  Hi, How can i get this to apply to multiple worksheets?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10254)
    
261.  Hi,  
    i have read your drop-down multiple selection post (without repetitions). it worked perfectly fine,but whenever i am closing worksheet all data validation get deleted how to solve this problem.  
    thank you in advance.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10190)
    
262.  Hello,
    
    When making multiple selections, how do you then delete a selection you may have accidentally clicked?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10195)
    
    *   that is also what I was going to question. Only deleting entire value works currently.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10360)
        
263.  Hi,  
    If the sheet is protected, multiple drop down list is not working ? any thoughts please
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10207)
    
264.  edited code so that the list removes a duplicate element if that happens: [https://pastebin.com/N9RGFkBZ](https://pastebin.com/N9RGFkBZ)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10238)
    
    *   AWESOME! This deletes the unwanted list item via “reselecting it” in the dropdown. Thank you!
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11140)
        
        *   This worked great for me
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13373)
            
265.  I plug in the VBA code and changed it to If Target.Column = H, but it does not work. I still cannot select multiple answers.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10239)
    
    *   Hi – you need to replace H with the number of the column which in this case is 8
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10440)
        
266.  Hi, I recently changed the Columns numbers in the VBA code because the applicable Columns changed location and now I’m getting compile errors. However, it worked just fine before I changed the column numbers. After the error it highlights the “.Column” portion of the first “If Target.Column” instance. Not sure why I’m getting this error. I had changed the VBA column numbers several times before this while creating the Workbook and it worked fine, but something is messed up now. Please help.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10241)
    
267.  This code worked for a moment yesterday, then my file crashed and the code has not worked since… Incredibly frustrating…
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10235)
    
268.  Is there a way to count the items later on if they are listed in a multiple list?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10233)
    
    *   If you know please share
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11114)
        
        *   \=IF(C3=””,””,(LEN(TRIM(C3))-LEN(SUBSTITUTE(TRIM(C3),”,”,””))+1))
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11141)
            
            *   (You put that formula in a separate cell)
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11142)
                
269.  Hi Sumit
    
    I have two queries.  
    1\. I tried your solution and put the list in the same sheet (A3-A5) as the cell (E3) where I wanted the multiple selection, but its not working for some reason. It is just picking 1 value. The sheet is IssueLog.  
    2\. I have the Standard list in one Worksheet ‘ReferenceInfo’ and I want to implement the multiple selection in another worksheet ‘IssueLog’ in column E (E3 to E300). Can it be done?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10240)
    
270.  I downloaded the sample to select multiple items. When selecting items, only one displays. What needs to be done to activate the display of multiple items?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10249)
    
271.  I have to add multiple questions some that requires only one answer and other multiple. How can you create list without all of them being multiple selection.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10106)
    
    *   You will have to change the code so that only the cells where you want multiple selections are included in the code
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10125)
        
272.  I have just made my excel worksheet Marco enabled and added the code to the code window saved and closed. I went to select multiple choices from the list and still can only select one
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To allow multiple selections in a Drop Down List in Excel (without repetition)  
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Target.Address = “$C$2” Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    If InStr(1, Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & “, ” & Newvalue  
    Else:  
    Target.Value = Oldvalue  
    End If  
    End If  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10105)
    
273.  hi Sumit,  
    can you clarify the following. I have my spreadsheet with multiple columns on sheet 1 and the dropdown list choices which is to be used for column F (on sheet 1) is listed on Sheet 2. Would I paste in the code above on the VBA Editor sheet 1 or 2?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10102)
    
    *   Hey Smruti, you need to paste the code for the sheet that has the drop-down list. So in your case, it would be sheet 1
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10103)
        
        *   thank you, it worked!
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10104)
            
274.  Hello, sorry if this question has been asked before. How about selecting multiple entries in the dropdown listbox ?  
    Something like ctl + click or so to select multiple entries at once.
    
    Tia.
    
    /Dirk
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10101)
    
275.  I’m really thankful to you as this code too useful for me, but i have a one query when my sheet is protect then this code isn’t work.  
    Please help me out i just want to use this code if my sheet is protect with password.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10074)
    
276.  Hi Sumit, @sumitbansal23  
    Its very useful tutorials from your website.
    
    I have used one of your [https://trumpexcel.com/select-multiple-items-drop-down-list-excel/](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
      
    But, how can we limit in selecting only max 3 values from drop down list.
    
    Please help.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10059)
    
277.  HI, Happy 2018!! I downloaded the example file but it is not working. Any security settings in Excel that I must change? Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10052)
    
278.  If I have to use the code for two columns specifically, say column D and  
    column I which have different sets of values in the respective drop down lists, how will the code change? This is the code from your website I am using now:  
    Option Explicit
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel  
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    ‘If Target.Address = “$F” Then  
    If Not Intersect(Target, Range(“I:I”)) Is Nothing Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    If InStr(1, Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & “, ” & Newvalue  
    Else:  
    Target.Value = Oldvalue  
    End If  
    End If  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10051)
    
279.  I saw code to get this to work while the sheet is protected, and that worked great. However, when I shared the workbook it stopped working and kept giving debug pop-ups. Is there a way to use this function while sharing a protected workbook?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10049)
    
280.  I have indirect lookups off the back of a drop down and if i choose multiple options in the first cell then my lookup no longer works, is there a solution to this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10015)
    
281.  Hi Sumit
    
    How do I protect the code form getting change by other user
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10005)
    
282.  This is a little bit late, but I just came across this and have a couple questions. Is there a way to limit the amount of selections one can make in a drop down list to say, 5? Currently there’s roughly ~200 items in the list and I only want them to be able to select a maximum of 5 of those at a time. Also, say I have the same list in all of column 7 and 8, would I be able to have a command that tells the user that once something is selected in column 7 they can no longer select it in column 8 or vice versa?
    
    Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9991)
    
283.  Hi Sumit – Thank you for this great information! I have an additional question… We have a worksheet with many picklists, and I am using this code for all multi-select picklists. We do allow the user to enter a new value if needed. Then we use “circle invalid data” to find the new values that have been added. However, when using “circle invalid data” on the multi-select picklists, it ALWAYS circles the cell if there is more than one value entered, even if they are valid choices. Is there a way to get “circle invalid data” to work properly with the multi-select columns? If not, is there something we could add to the code, to “highlight” those values that the user added (that are not valid)?  
    Thanks so much for your help!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9989)
    
284.  I’m curious on how one can create dynamic multiple items list. For example… let us say we have the following:
    
    Column 1 Drop Down  
    Colors: Blue, Yellow
    
    Column 2 Drop Down  
    Blue: Light Blue, Medium Blue, Dark Blue  
    Yellow: Light Yellow, Medium Yellow, Dark Yellow
    
    Column 2 is dependent to Column 1.
    
    Thus, if I pick “Blue” in column 1 then in column 2 I have the choice to pick Light Blue and/or Medium Blue and/or Dark Blue
    
    If I picked “Blue” and “Yellow” in column 1 then in column 2 my options to pick are:  
    Light Blue and/or Medium Blue and/or Dark Blue and/or Light Yellow and/or Medium Yellow and/or Dark Yellow
    
    Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9981)
    
285.  Thanks so much! Really useful, and just saved me hours of brain hurt!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9950)
    
286.  Hi there!
    
    First off, many thanks for the code, it made my research that much easier! I was just wondering whether this will be compatible when computing statistical analysis in Studio R; can I conduct tests on excel cells with multiple items?
    
    Thanks in advance,  
    Mana
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9949)
    
287.  Hello,  
    Thanks you for this code, it works fine !  
    I used it on an entire column, and I want to filter by choice (say if i choose “one, two, three”, I want to that cell to come up if I filter for “two”). Is that possible ?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9942)
    
288.  Every time I save the workbook, my coding disappears when I reopen the document. Can someone please help???
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9941)
    
289.  Thanks for the solution..its works fine…however it is being applied to all the cells in the sheet and I am not able to edit the cells even where there is no drop down menu to choose from. Can i choose the columns to which this code should be applicable?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9920)
    
290.  This solution is OK, but what if you want to delete values? So [https://uploads.disquscdn.com/images/f49a89e68134ae908e184e590a5b4e052ec9548648b51162600b703cceefebff.jpg](https://uploads.disquscdn.com/images/f49a89e68134ae908e184e590a5b4e052ec9548648b51162600b703cceefebff.jpg)
     I have produced an advanced solution.  
    YOu can dowload the code for free. It uses check-boxes and is far more useful.  
    [http://www.vlsiip.com/exceltips.html](http://www.vlsiip.com/exceltips.html)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9915)
    
291.  I have now developed the whole VBA solution using Listboxes, uploaded it on my web site:  
    [http://www.vlsiip.com/exceltips.html](http://www.vlsiip.com/exceltips.html)
      
    [https://uploads.disquscdn.com/images/f49a89e68134ae908e184e590a5b4e052ec9548648b51162600b703cceefebff.jpg](https://uploads.disquscdn.com/images/f49a89e68134ae908e184e590a5b4e052ec9548648b51162600b703cceefebff.jpg)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9908)
    
292.  I cannot get this to work, even with the file I downloaded. I enabled the macros and still did not work. I am using Excel 2016. Could this be the issue? Do you have a solution?
    
    Thank you
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9883)
    
    *   [http://www.vlsiip.com/exceltips.html](http://www.vlsiip.com/exceltips.html)
          
        Download it from here, it is free easy to understand. It uses Listboxes and checkboxes. Will enable you to select multiple values from this drop down list menu.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9916)
        
293.  Hi,
    
    Im using the multiple selection dropdown list. I don’t know how to describe but hopefully with my example below will make you to understand :-
    
    In my dropdown list have a several option where each option have their own values.  
    grape – 4  
    apple – 3  
    banana – 2  
    orange – 1
    
    when i choose in the dropdown for Grape,Banana,Apple the excel will look for the lowest value among the option i had choose. In this case, the excel will find that Banana have the lowest value among the option i had choose hence the value showed up is 2.
    
    How can do that?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9882)
    
294.  Hi, is there any way to add scrolling feature to the drop down?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9855)
    
295.  [https://uploads.disquscdn.com/images/3d702f5a3a9b4018d71bd888549aae80b2837a66664a4dab41f92a0b2b29f6d8.png](https://uploads.disquscdn.com/images/3d702f5a3a9b4018d71bd888549aae80b2837a66664a4dab41f92a0b2b29f6d8.png)
      
    Hi, I’ve used the code successfully but now it does not work after an update of Excel version 15.39 (171010). It can only contain one value in the field. Should I change something in the code to make it work again?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9840)
    
296.  Anyway to limit the number of entries? I’d like to only be able to select a maximum of 5 entries. I have a formula in F5 on the sheet that counts the number of separators (I used “;” instead of “, “) that adds 1 since for 5 entries there would only be four semi colons. I want a message box to appear when F5 has a value of 5 and then exit the sub.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9820)
    
297.  Hi I have tried this code and still cannot select more than one drop down from my list. are you able to help.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9797)
    
298.  Thanks so much very easy to follow and worked the first time.  
    Well done!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9784)
    
299.  Is there a way to do this using a key combination instead of a comma to delimit the selections?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9775)
    
300.  Dear sir,  
    Can you help me up how to loop range till 2 to 5000 for below code
    
    Option Explicit
    
    Private Sub Worksheet\_Change(ByVal Target As Range)
    
    If Target.Count > 1 Then Exit Sub  
    Application.EnableEvents = False  
    If Target.Address = “$C$2” Or Target.Address = “$D$2” Then  
    If Target.Address = “$C$2” Then  
    Range(“E2”) = Range(“E2”) + Target  
    ElseIf Target.Address = “$D$2” Then  
    Range(“E2”) = Range(“E2”) – Target  
    End If  
    Target = “”  
    End If
    
    Application.EnableEvents = True  
    End Sub
    
    Sub Evenement()  
    Application.EnableEvents = True  
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9766)
    
301.  Hi. This has been extremely helpful, but I have my drop down list on one sheet and the cell on another. How do I code for that? I am also trying to use a date picker so that when my teachers click on a cell, they can have a calendar pop up to click on. Can you address that issue or tell me where I can find the answer? Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9765)
    
302.  If I change the address to  
    If Target.Column = 1 Then  
    The function does not work. what might I be doing wrong?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9757)
    
303.  Hi, I was able to get the code to work, but when an email marco was attached to the spreadsheet it quit working. What have I done wrong?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9750)
    
304.  How can I count the number of each selection? I tried countif but it does not seem to be working.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9747)
    
305.  I’m having a difficult time implementing this solution for my particular use case. In my spreadsheet, I am applying data validation on the fly first — in other words, every time I click on a cell in a given range on my sheet “User Lists” it checks the header of that column, looks for that value in the header row on “User Picklists” and then if it finds it it uses the list from that page as the list for data validation on User Lists. Some of the columns need to be Multi-Select though, so once that code block runs, I have used yours immediately below it.
    
    However, it’s not working the way I expect it to even though I left the code almost identical to how you are using it above. The difference is in your sheet, the code fires when I select a value from the list. In my sheet, it fires as soon as I click the cell and doesn’t re-fire when I select the value. I believe this has to do with the other code block above it, but I’m not sure how to make your block re-fire when I select the value. Do you have any tips? See full code below:
    
    Private Sub Worksheet\_SelectionChange(ByVal Target As Range)
    
    Application.ScreenUpdating = False
    
    Dim ws As Worksheet  
    Dim RefRng As Range, RngFind As Range, NewRng As Range, hdr  
    Dim RefList As Range, c As Range, rngHeaders As Range, Msg
    
    On Error GoTo ErrHandling
    
    Set ws = ThisWorkbook.Worksheets(“User Picklist”)
    
    ‘only deal with the selected cell(s)  
    Set NewRng = Application.Intersect(Me.Range(“A12:T101”), Target)  
    If Not NewRng Is Nothing Then
    
    Set rngHeaders = ws.Range(“A11:ZZ11″)
    
    For Each c In NewRng  
    c.Validation.Delete ‘delete previous validation  
    hdr = Me.Cells(11, c.Column).Value  
    If Len(hdr) > 0 Then  
    Set RngFind = rngHeaders.Find(hdr, , xlValues, xlWhole)  
    ‘matched header?  
    If Not RngFind Is Nothing Then
    
    Set RefList = ws.Range(RngFind.Offset(1, 0), \_  
    RngFind.Offset(1, 0).End(xlDown))
    
    c.Validation.Add Type:=xlValidateList, \_  
    AlertStyle:=xlValidAlertStop, \_  
    Formula1:=”='” & ws.Name & “‘!” & RefList.Address
    
    End If ‘matched header  
    End If ‘has header
    
    Next c  
    End If ‘in required range
    
    ‘Multi Select  
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Not NewRng Is Nothing Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    If InStr(1, Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & “, ” & Newvalue  
    Else:  
    Target.Value = Oldvalue  
    End If  
    End If  
    End If  
    End If
    
    Here:  
    Application.ScreenUpdating = True  
    Exit Sub
    
    ErrHandling:  
    If Err.Number 0 Then  
    Msg = “Error # ” & Str(Err.Number) & ” was generated by ” & \_  
    Err.Source & Chr(13) & “Error Line: ” & Erl & Chr(13) & Err.Description  
    Debug.Print Msg, , “Error”, Err.HelpFile, Err.HelpContext  
    End If  
    Resume Here
    
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9746)
    
306.  Hi. Nice post. I am looking for a dropdown list where I can (really) multi-select. e.g. holding the Ctrl or Shift key. Here with your solution I have to select each one-by-one. Ctrl-A to select all would be also nice.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9745)
    
307.  I have a workbook that needs different dropdowns in all columns and down 10-20 rows. Underlying data is on a separate sheet. Which sheet should the code be posted and how do I change the code to accomodate 20 different drop down lists
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9744)
    
308.  Hi VBA code is not working in my excel sheet
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel  
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Target.Address = “$C$2” Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    If InStr(1, Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & “, ” & Newvalue  
    Else:  
    Target.Value = Oldvalue  
    End If  
    End If  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    what wrong with my excel
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9742)
    
309.  Hi Sumit,
    
    This is a great code and for the most part it’s worked well for me. I’m trying to apply this to a range of cells from B3:H1012. Can you please advise what part of the code needs to be changed? I would also appreciate if you can let me know the code it needs to be changed with. Thanks a lot in advance!!!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9732)
    
310.  Hello, this code works great. Thank you for sharing this great work. Unfortunately, I’ve come across an issue not yet addressed here. I need to protect the worksheet, but once I do that the code no longer works. Is there a solution for this? Thank you!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9729)
    
311.  Hello, Both of the codes worked great! However I am trying to combine both of the codes in the same file (workbook). One column I need to select multiple item with repetition and the other I need to select multiple items without repetition. How do I combine these?
    
    Private Sub Worksheet\_Change(ByVal Target As Range)
    
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel
    
    Dim Oldvalue As String  
    Dim Newvalue As String
    
    On Error GoTo Exitsub  
    If Target.Column = 9 Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    Target.Value = Oldvalue & “, ” & Newvalue  
    End If  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    and this one
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel  
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Target.Column = 15 Or Target.Column = 16 Or Target.Column = 9 And Target.Row > 1 And Target.Row < 3000 Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = "" Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = "" Then  
    Target.Value = Newvalue  
    Else  
    If InStr(1, Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & ", " & Newvalue  
    Else:  
    Target.Value = Oldvalue
    
    End If  
    End If  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9699)
    
312.  I tried to use your code and I am getting my list from sheet 2 and I can get the drop down to allow me to pick one name but I am unable to to pick more than one. I assume it has to do with the way I am tying is into the sheet 2. Should I be using the Target.Address = “$F$6” or Sheet2!A1:A12 where my list is.  
    Thanks for the help
    
    Private Sub Worksheet\_Change(ByVal Target As Range)
    
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel
    
    Dim Oldvalue As String  
    Dim Newvalue As String
    
    On Error GoTo Exitsub  
    If Target.Address = “$F$6” Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    Target.Value = Oldvalue & “, ” & Newvalue  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9671)
    
    *   Hello Ben.. The code needs to be in the sheet in which it’s supposed to run. In this case, if you multiple selection to work in Sheet 2, you need to place the code in Sheet2 code window in VBA backend.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9674)
        
313.  This was working great and it just stopped working suddenly. Not sure why.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9669)
    
    *   Never mind, figured it out. Macro security, make sure after an office 365 update you turn your macro security trust back off otherwise it might block this code.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9670)
        
314.  Can we put multiple VBAs in the same sheet for different cells having separate dropdown lists.. I tried it does not work.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9666)
    
    *   Hey Manisha.. For this to work for different cells, you can simply modify the following line: If Target.Address = “$C$2”
        
        For example, if you want this to work for C2 and D2, make it –  
        If Target.Address = “$C$2” Or Target.Address = “$D$2”
        
        And yes, you can also add mulriple VBA codes as well, however, it may not be necessary in this case.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9675)
        
315.  I followed the instructions. How do I apply it to C2:C42? When I scroll down in my worksheet, the drop down box loses the ability to select more than one option.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9647)
    
    *   Hello Dorsey.. To make it work for multiple cells (C2:C4), replace the following line in the code:  
        If Target.Address = “$C$2”
        
        with this line:  
        If Target.Address = “$C$2” Or Target.Address = “$C$3” Or Target.Address = “$C$4” Then
        
        If you want it to work for the entire column C, use the following line:  
        If Target.Column = 3
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9686)
        
316.  I had it working then it stopped. I need to be able to select from a list into a full column.  
    Followed the direction, just changed the line If Target.Address = “$F$6:$F$156” Then
    
    In the target column did the Data -> Data validation -> List to the column holding the list (X1-155)
    
    What am I missing?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9644)
    
317.  Hello, using a VBA code similar to yours, I am selecting multiple items in a drop down list that are separated by comma. The code I am using is to edit and add multiple items in a drop down in the same cell. I am trying to create a pivot table with independent filters instead of all the line items in each cell. For example, in my drop down list, in one cell, I selected apple orange and banana, and in another cell, I have kiwi orange and banana, however, I just want to focus on the banana independently that occurred each time. Is this possible at all? Or will I have to resort to traditional excel and create a cell for every single item. (Really what I am doing is monitoring donor/patient reactions, so I am selecting for example, nausea, loss of consciousness, etc, and where the conditions were mild, moderate, and severe and how many times in a mild reaction did a donor have nausea symptoms or something). Hope there’s something to do this! I just like that the drop down feature makes one column instead of a million different columns but I really need it to analyze my data. Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9636)
    
    *   I have the same exact question.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9637)
        
        *   i’ve been looking everywhere for a solution!! I even asked on the microsoft excel community for help.. maybe there will be a glimpse hope for us!! lol!
            
            [https://answers.microsoft.com/en-us/msoffice/forum/msoffice\_excel-mso\_winother-mso\_2013\_release/help-how-do-i-create-a-pivot-table-to-filter/9f274fe3-8dba-4b95-9df0-346e8cbe1502](https://answers.microsoft.com/en-us/msoffice/forum/msoffice_excel-mso_winother-mso_2013_release/help-how-do-i-create-a-pivot-table-to-filter/9f274fe3-8dba-4b95-9df0-346e8cbe1502)
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9638)
            
318.  Hello Sumit,
    
    This is an excellent layout and step by step instruction. Thank you so much! I have been trying to change the code to where the multiple list selections appear unduplicated across the row in separate columns. Do you have the VBA code know where in the above listed one I can edit to make that happen?
    
    Thank you in advance!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9625)
    
319.  Hi Sumit .. Thanks a ton for sharing this .. the code works fine for me 🙂 on a unprotected sheet. It stops the moment the sheet is protected .. my apologies if this has already been answered as i am unable to find any threads on password related issue for this VBA command .. Please help!!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9616)
    
320.  I used the code above to allow for multiple selections, and then I used the modification from Sumit Bansal to modify it work for all of the drop downs in my worksheet. This worked great! Thanks! Now my problem is that in the header row of my table I can’t make any changes. Any time I try to make changes the text keeps multiplying instead of deleting. I am thinking that this might have to do with the fact that I had converted this spreadsheet to a table before I add the dropdowns and code. So the header row had it’s own built in sorting/filtering dropdowns that the code may be messing with?? Regardless it is huge table and now I am not sure what to do with it, and would appreciate any suggestions. My header row is mess and everything I try to do to fix it is making it worse.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9601)
    
321.  Help! I used your code for being able to do multiple selections from a drop down menu, and then I modified it to apply to all the drop downs in my worksheet as described below. This worked great. Now I am having this weird problem where if I try to delete and edit something in a cell that does NOT have a drop down it won’t allow me to delete. So every time I try to delete and add, I just end up with more and more copies of almost the same thing. The only thing I can think of is that it is somehow related to the code allowing for multiple selections. Have you ever seen this? Do you know what it might be? [https://uploads.disquscdn.com/images/4a019783ca43d6f04d60ef16990d45dd38f33690231d5cf6678d750a7576b04a.png](https://uploads.disquscdn.com/images/4a019783ca43d6f04d60ef16990d45dd38f33690231d5cf6678d750a7576b04a.png)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9599)
    
322.  Hi – thanks for providing the VBA code, seems to work great. Is it possible to limit the selections to a certain number? I.e. 5 choices w/the option of selecting a maximum of 3 without repetition. Thanks, I look forward to hearing back from you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9593)
    
323.  Thank you Sumit for your tutorial for setting up Multiple Selection Drop Down lists…it worked very well and was very helpful! I would however like to have the multiple selections I make from the Drop Down List I created in in Column 3-Row 5, to be displayed down in Column 2- Rows 5 thru 10 instead of side by side in the same cell separated by a comma…I can’t seem to find an example of the VBA Code I could use to accomplish this…Can you please provide an example for this scenario? Thanks!  
    Jim B.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9590)
    
324.  Hi, I’ve now made a list using this code. Now some cells have multiple entries but I am struggling to find a way to filter specific words in the boxes with multiple. The standard filter just showed everything in the box and advanced custom filter only allows you to filter 2 words/ phrases. So could someone help me find a way to search a list for cells containing key words/ phrases
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9588)
    
    *   hi, did you ever figure out how to do this? i’m trying to create a pivot table based on certain values in the cell even when there are multiple options selected and i can’t find a solution. :/
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9635)
        
    *   Same
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11115)
        
325.  Hi, This is exactly what I need, followed all your instructions and even downloaded your sample file, unfortunately it just is not working, I have changed the settings to allow VBA projects, am I missing something!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9587)
    
326.  thanks so much! it works beautifully!  
    Just had one problem: why does it refrain me from editing other cells?  
    Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9586)
    
327.  Rather than have the output read “one, two, three” I would like it to read “one, two and three”. Or “one and three” etc. Is this doable?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9569)
    
328.  Is there a way to tweak your code so that each drop down selection appears on a new line within the cell (rather than separated by commas)?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9561)
    
329.  What if my dropdown lists are in a different sheet than the dropdown data?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9552)
    
330.  Hi, thanks for the great code. I have it working on 4 separate columns in a file I have, but there is a strange issue I’m seeing. If I enter data in a cell directly in front of one of the columns I have the VBA code running against and then either tab into or right arrow into the coded column, the cell highlight will jump back to the cell I came from. It then also runs the VBA code against that cell now too. Example: column B has the VBA code applied to it, column A does not. If I enter any data into column A, press TAB to go to the next cell in the row which is in column B. The cell highlight moves to column B, briefly, then jumps back to column A. If I had for example entered “1” in the cell in column A prior to pressing TAB, if I then enter “2” in that same cell, the VBA code will make the data in the column A cell be: “1, 2”. Any clue on what I can change in the code to keep this from happening? Here’s my version of the code posted here, which is based on the code posted for keeping duplication of choices from happening. It looks for column headers by title to determine which columns to run the script on.
    
    Option Explicit
    
    Private Sub Worksheet\_Change(ByVal Target As Range)
    
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List  
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Cells(1, ActiveCell.Column).Value = “Vendor Type” Or \_  
    Cells(1, ActiveCell.Column).Value = “Types of data shared with Vendor” Or \_  
    Cells(1, ActiveCell.Column).Value = “Data Transferred” Or \_  
    Cells(1, ActiveCell.Column).Value = “Audit Artifacts Received” Then
    
    If Oldvalue = “” Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else:  
    If InStr(Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & “, ” & Newvalue  
    Else:  
    Target.Value = Oldvalue  
    End If  
    End If  
    End If  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9547)
    
    *   In case anybody has this same problem I figured out a different way to code this and it solved the problem:
        
        Option Explicit
        
        Private Sub Worksheet\_Change(ByVal Target As Range)
        
        ‘ To Select Multiple Items from a Drop Down List  
        Dim Oldvalue As String  
        Dim Newvalue As String  
        Dim a As Long  
        Dim b As Long  
        Dim c As Long  
        Dim d As Long
        
        ‘ Set the header values we’re looking for in the sheet  
        a = WorksheetFunction.Match(“Vendor Type”, Sheet1.Range(“A1”, Sheet1.Range(“IV1”).End(xlToLeft)), 0)  
        b = WorksheetFunction.Match(“Types of data shared with Vendor”, Sheet1.Range(“A1”, Sheet1.Range(“IV1”).End(xlToLeft)), 0)  
        c = WorksheetFunction.Match(“Data Transferred”, Sheet1.Range(“A1”, Sheet1.Range(“IV1”).End(xlToLeft)), 0)  
        d = WorksheetFunction.Match(“Audit Artifacts Received”, Sheet1.Range(“A1”, Sheet1.Range(“IV1”).End(xlToLeft)), 0)
        
        Application.EnableEvents = True  
        On Error GoTo Exitsub  
        If Target.Column = a Or \_  
        Target.Column = b Or \_  
        Target.Column = c Or \_  
        Target.Column = d \_  
        Then
        
        If Oldvalue = “” Then  
        If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
        GoTo Exitsub  
        Else: If Target.Value = “” Then GoTo Exitsub Else  
        Application.EnableEvents = False  
        Newvalue = Target.Value  
        Application.Undo  
        Oldvalue = Target.Value  
        If Oldvalue = “” Then  
        Target.Value = Newvalue  
        Else:  
        If InStr(Oldvalue, Newvalue) = 0 Then  
        Target.Value = Oldvalue & “, ” & Newvalue  
        Else:  
        Target.Value = Oldvalue  
        End If  
        End If  
        End If  
        End If  
        End If
        
        Application.EnableEvents = True  
        Exitsub:  
        Application.EnableEvents = True  
        End Sub
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9549)
        
331.  Hello. For some reason I can not get the code to work. I copied and pasted the same way you did but it still does not work. What am I doing wrong??
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9546)
    
    *   I am having the same issue. Do I need to modify any of the code for my dropdown cells?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9553)
        
        *   Yes, yes I did. I substituted $C$2 for the correct cells in my sheet, and it worked! I am new to VBA, so I’m sorry for the silly question. Thanks for the code!
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9554)
            
332.  @sumitbansal23:disqus Hi Summit, your code worked great for non repetition. I noticed the values selected appear in cell window. Besides that feature is there a way to keep the chosen values from the dropdown list highlighted and erase selected value by double clicking on them? Ultimately I am following up with a code that will hide selected columns depending on the values appearing in the cell chosen from your code. Any advice on that?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9544)
    
333.  I tried to manipulate the code to account for 2 columns to be able to select multiple items but having trouble. Can anyone help?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9542)
    
334.  Hi, this worked perfectly, thank you.  
    But I cannot remove any item from the selection unless I delete the entire entry.  
    Any suggestions ?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9511)
    
335.  hi sumit,  
    How to get the selected column header name for the selected cell.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9504)
    
336.  Hello Sumit,
    
    Is there a way to add a Sum of all the values collected? I’d like to be able to sum the value of all the items selected and then use the sum in another formula.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9501)
    
337.  Dear Sumit, thanks for the great code! I run into a problem when I lock the sheet, then the macro stops. I am going to share my sheet with others and need the lock specific cells. Do you have any suggestions how to solve this problem? Thanks for your time!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9496)
    
338.  How do you take the validation out so I can add text to the end of the cell, text that isn’t in the dropdown?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9494)
    
    *   Actually I just removed the error alert and I was able to add more choices to the end but it repeats the choices I made using the code. So if I picked A B C and added lol. It would become A,B,C,A,B,C,lol
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9495)
        
339.  Is there a way to deselect something from the list if it was clicked by accident?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9489)
    
    *   Never mind. Was able to look for a previous comment below
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9490)
        
340.  Sumit – thanks for putting this up, this was exactly what I was looking for. One question – once I’ve implemented this on my spreadsheet, I may create pivot tables using the data contained therein. Is there a way to force the pivot table to treat each selection in one cell separately instead of creating a new category defined as all multiple selections?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9488)
    
    *   let me know if you ever found a solution!
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9633)
        
341.  Hi Sumit, not sure if you are still active, but I want to thank you for this work. You are wonderful, and this material is so helpful.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9484)
    
    *   Thanks a lot for the kind words.. Glad you found it useful 🙂
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9485)
        
342.  Hi Great Post, Its very helpful,Thanks a lot.  
    I Want to know is it possible to know the selected items to be highlighted in the drop down if yes please help us to do that. thanks in advance.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9482)
    
    *   Hey Karthi.. I don’t think it’s possible to apply any kind of formatting in the drop down.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9486)
        
343.  Hello, this is super helpful, thanks! Only thing is I can only get this to work when I use it alone without any other VBA code, but as soon as I use additional code to have my sheet perform other functions, my drop-down list reverts to only accepting one option at a time. Below is the code – any ideas how I can get it all to work? My other two commands are for time stamps in two different places on the same sheet. The other two commands still work when I combine all the code, but the ability to choose more than one option from the drop-down menu stops working.
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    If Target.Column = 1 Or Target.Column > 100 Or Target.Column = 9 Then Exit Sub  
    Application.EnableEvents = False  
    Cells(Target.Row, 1) = Now  
    Application.EnableEvents = True
    
    Dim xCellColumn As Integer  
    Dim xTimeColumn As Integer  
    Dim xRow, xCol As Integer  
    xCellColumn = 8  
    xTimeColumn = 9  
    xRow = Target.Row  
    xCol = Target.Column  
    If Target.Text “” Then  
    If xCol = xCellColumn Then  
    Cells(xRow, xTimeColumn) = Now()  
    End If  
    End If
    
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel  
    Dim Oldvalue As String  
    Dim Newvalue As String  
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Target.Address = “$W$3” Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    If InStr(1, Oldvalue, Newvalue) = 0 Then  
    Target.Value = Oldvalue & “, ” & Newvalue  
    Else:  
    Target.Value = Oldvalue  
    End If  
    End If  
    End If  
    End If  
    Application.EnableEvents = True  
    Exitsub:  
    Application.EnableEvents = True  
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9466)
    
    *   I believe these codes are interfering as both sets of codes (your and mine) is fired when you try to use the drop down in W3. What are you trying to get done with your code in the beginning?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9487)
        
344.  Hello, The Code works well for the list put in other columns where I have some descriptive copy I have been having issues making changes to the content when this code is present. Have you run into this issue?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9465)
    
345.  Hi Sumit, This has been extremely helpful, thank you! I have applied the code for multiple selections to several columns which contain drop down lists. However, every cell in the entire sheet is requiring a complete clearing of contents when an edit is made. This is similar to Emily’s querry, but not quite. Thank you so much for providing this service! -Mary
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9447)
    
346.  Hello Sumit, thank you for this expansive tutorial, I used this solution now but have a follow up question: I want to use the multiple entry result cell as input for another list lookup function. E.g. My multiple entry cell looks like “Item 1, Item 4, Item 4, Item 10” so far, so good. The final result in another cell should be the sum of the values of these items ( e.g. 1$+4$+4$+10$ = 19$). Is that possible and if so, how? – Thank you very much for your time!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9440)
    
347.  Nice. You just turn a “I don’t know if I can do that” into a 2 minute chore. You rock Sumit!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9437)
    
348.  Once you select options, is there a way to edit in Excel? Example – clicked on desired drop down item, but would now like to add additional information into cell. I am getting an error message.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9435)
    
349.  I saved on format as reccomeneded. But when I reopen it it stops working. Any one know why ?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9430)
    
    *   you need to save your excel spreadsheet as a macro enabled spreadsheet. go to file, save as, and then when you see the title, it says save as type … and select excel macro enabled workbook (\*.xlsm). now the code will be saved everytime you open and close.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9632)
        
        *   Great. Thank you so much. I try to find support this solve
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13079)
            
350.  @sumitbansal23:disqus Hi, this code is superb, but can you tell me if it’s possible to ensure that once the selections are made they appear in alphabetical order? pleas reply as soon as possible
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9422)
    
351.  Hi Sumit, is there a way for to vlookup code for the multiple drop down list selection for the above code
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9410)
    
352.  Thanks for the post. What if you have more than one column in the spreadsheet that you want to set up dropdown menu with multiple data point selection?
    
    Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9397)
    
353.  I think I have looked through all the comments to find this and don’t see it, how do I point the code to look at a different sheet within the workbook for the list of options? I have created the list on Sheet 2 A2:A27 and the drop down box I need populated are on Sheet 1 C10 &D10 which is a merged cell. I have never done VBA coding so please help. Thank you.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9358)
    
    *   I pose same question; did you get an answer
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10829)
        
    *   Dan, you don’t do that in the code. When you select your list in data validation you can select a different sheet. When you get into the data validation window you just click the formula area, then click the page, and the cell set you want to use
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-14369)
        
354.  Hi, Sumit. Thanks for the code it works great. I would like to add a carriage return at the end of each selection. Is it possible ? And, is it possible to edit the selection, like adding a person name in the selection. ex: John needs to walk 15 minutes twice a day ? Tanks.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9349)
    
355.  Wonderful! Thank you!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9335)
    
356.  You’re amazing ! Thank you so much!  
    Problem: I have a excel file that i must send to many of my colleagues, my question is, how can i send it with the code so they wont have to paste it in VBA?  
    Thanks !
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9309)
    
    *   You paste the code in your file and save it with .xls or .xlsm format. Now you can send it to others and the code would work
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9311)
        
        *   Thanks for the quick reply !  
            Using XLS or XLSM format does not work for me but i succeeded using XLSXM format.  
            Thank a lot !
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9320)
            
357.  Hi, I’ve tried everyone’s version of this VBA code and no one’s is working. I have created the data validation drop down list, ez pz, but regardless of the code I paste in, I don’t get these results. I am using Excel 2013 and the worksheet/book isn’t protected. I am simply trying to get multiple choices in the same cell.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9300)
    
    *   The code I have provided above only works for cell C2. You will have to change the line Target.Address = “$C$2” to make it work for your cell.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9312)
        
        *   Yeah, I read through a million of these comments and saw that, which I changed of course. Turns out, I needed to save and exit for the code to run and work. Strange!
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9319)
            
        *   What do I use for a range of cells in place of $C$2?
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9555)
            
358.  Dear Sumit,  
    You are THE man. Thank you.  
    That is all.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9295)
    
    *   Thanks for commenting Heather! Glad it helped 🙂
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9313)
        
359.  Your posts are fantastic Sumit. Thanks. Can you help me with this issue. I have created the dropdown list with multiple entries without repetition and would like to know if each selection can be on a separate line in the cell and not separated by a , (comma). Your help would be appreciated and I am generally useless at VBA, but your info and tutorials have been super helpful.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9294)
    
    *   Glad you found the tutorial useful Lara.
        
        To get each selection in a new line, replace this line in the code (Target.Value = Oldvalue & “, ” & Newvalue) with this line of code (Target.Value = Oldvalue & vbNewLine & Newvalue)
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9314)
        
        *   You are a star…. thank you. Your help is amazing.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9317)
            
        *   This worked really well, thanks. Can you tell me how to delete an entry that is selected in error? I dont want to have to delete all the entries already selected, only one or two. If I remove all the entries in the cell, then I have to reselect all the ones I need in the cell. Thanks. 🙂
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9318)
            
            *   Sumit – I’ve used your code to set up drop down lists in three separate columns, without repetition. It works like a Boss. Now, Like Lara above, I would also like to delete accidental entries. Some code from another source was supplied in the discussion above, but it doesn’t do the line breaks. I’m a complete beginner with VBA, and can’t see how to adapt one to the other. Any advice? Thanks.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9796)
                
        *   Sumit – this is brilliant! It has really helped me. Thank you.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9795)
            
        *   This was helpful, but is there a way to have this AND have code so that the duplication in the cells stopped? I was using Spyrule’s code he posted above, which is:  
            If Oldvalue = “” Then  
            Target.Value = Newvalue
            
            ElseIf Target.Value = Oldvalue Then ‘<~~~ This prevents self-duplication.  
            GoTo Exitsub
            
            Else  
            Target.Value = Oldvalue & ";" & Newvalue  
            End If  
            but is there a way to combine both these things? I've tried combining these lines with this NewLine code but haven't been able to achieve both happening. I know almost nothing about code. Any help is much appreciated!
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9960)
            
360.  Hi Sumit,  
    Great code here. The problem is (keep in mind it may be on my end), the code is not working. I even downloaded your code, and tried running it on my machine, and I still am only able to select one of the drop list items. Is it possible there is a security setting I missed? I have enabled macro’s, and allowed trust access to VBA project object model, but again, the code doesn’t work. Please help. Also, is it possible, to have the code work on several different cells (copy and paste drop down) and have the VBA code changed to accommodate? I am trying to make a drop down selection list down over 260 line selections. I essentially need to copy the drop down to that many, and allow for selection as I go through the line items. Thanks again.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9290)
    
    *   Hello TJ.. The code I have given is made to work on cell C2 only. You can easily make it work for more cells for rows/columns. For example, to make it work for entire column C, use target.column = 3
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9310)
        
361.  Hi Sumit . Thanks a lot for this great video . In drop down tap beside the list there will be a option that will allow me to insert whatever i want to insert .Is it possible ? Please help me
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9275)
    
    *   Go to the Data tab and click on Data Validaiton. In the data validation dialog box, in the Error Alert tab, change the from Stop to Information. Now you will be able to make the changes and enter manually in the cell.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9315)
        
362.  This has been really helpful, thank you so much. Is it possible to make this VBA code work when a sheet is protected?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9208)
    
    *   You need to keep the cells with drop down unlocked. It will work fine then. Here is a tutorial on how to lock all the cells except some selected ones: [https://trumpexcel.com/lock-cells-in-excel/](https://trumpexcel.com/lock-cells-in-excel/)
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9316)
        
363.  For Protected Worksheet:
    
    Option Explicit
    
    Private Sub Worksheet\_Change(ByVal Target As Range)
    
    Dim wsh As Variant  
    For Each wsh In Worksheets(Array(“Sheet1″))  
    wsh.EnableOutlining = True  
    wsh.Protect UserInterfaceOnly:=True, Password:=””, \_  
    DrawingObjects:=False, \_  
    Contents:=True, \_  
    Scenarios:=True, \_  
    AllowFormattingCells:=False, \_  
    AllowFormattingColumns:=False, \_  
    AllowFormattingRows:=False, \_  
    AllowInsertingColumns:=False, \_  
    AllowInsertingRows:=False, \_  
    AllowInsertingHyperlinks:=False, \_  
    AllowDeletingColumns:=False, \_  
    AllowDeletingRows:=False, \_  
    AllowSorting:=False, \_  
    AllowFiltering:=False, \_  
    AllowUsingPivotTables:=False  
    Next wsh
    
    ‘Code by Sumit Bansal from [https://trumpexcel.com](https://trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel
    
    Dim Oldvalue As String  
    Dim Newvalue As String
    
    On Error GoTo Exitsub  
    If Target.Address = “$C$2” Then ‘As required  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    Target.Value = Oldvalue & “, ” & Newvalue  
    End If  
    End If  
    End If
    
    Exitsub:  
    Application.EnableEvents = True
    
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9155)
    
364.  This is a great bit of code and it’s working well for me. I have a question about whether or not I can use the code if the table I’m working in has been formatted as a table. Instead of “3” in the following line:
    
    If Target.column = 3 Then
    
    is it possible to use a reference to the table and column? Table1\[column1\]?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9124)
    
365.  Hello, I followed the instructions and it worked perfectly. Is it possible to edit the above code so that when you click multiple selections it forms a list down multiple cells in a column, rather than in one cell separated by commas?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9114)
    
366.  I have followed this to the letter and still only get one entry at a time. I have set up drop downs in every cell under column’s B,E,F. I want B to remain a single selection, but I want to have the option for E and F to have multiple entries (items) Any help would be appreciated
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8996)
    
367.  Thank you for your great work! If I need to select some Items and then add those in the cell, how can I make this?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8983)
    
    *   hi did you ever figure this out??
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9634)
        
368.  Hello, How to I create multiple selections as a list in a new column rather than getting values separated by coma in same cell?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8982)
    
369.  Hi Sumit, thanks for the codes. The multi-select list worked great but I have issue with the existing single-select list. Before I added your code, validation for the single-select list worked. I only could select the value from the list. But after I added your codes, the validation for single-select list didn’t work. I was able to enter any values to the single-select list and I didn’t get an error message. If I only select the value from the list then it’s fine. But I still could enter any value and the cell will accept it.
    
    Do you know how to fix this? Thanks so much for your help!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8979)
    
370.  Hi Sumit,
    
    If I have to delete an entry from the list, it does not behave the way it should. Have you tried that?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8922)
    
371.  awesome post, got it workin in under 5 minutes. Exactly what I wanted, thanks, keep up the good work
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8840)
    
372.  LIFE SAVER!!!! So here’s the tricky part. How do I now filter my column with multiple items so that everything with “A” appears…even though it has other names along with it “A,B”, “B,A”, “C,A”
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8766)
    
    *   I would like to know a solution for this also.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9958)
        
373.  Great macro thanks! TRUMP RULES!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8765)
    
374.  Hi Sumit, is there a modification to the code if I want the next selection from the dropdown in the next line. Like when we the ALT+Enter function : for eg  
    one  
    two  
    three  
    Instead of :  
    one, two, three
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8619)
    
375.  What is the solution to pepperleafev’s problem of duplicating values? I am facing the same problem after using the code
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8617)
    
    *   I am having the same issue…any answers???
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9192)
        
376.  Hello Sumit, thank you for supplying such helpful information, I have used the code and works well, not sure if this has been covered yet, but is there a way for the selected data to display down the column instead of in the one cell?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8565)
    
377.  I came across your code chunk, and for the most part it works well.
    
    A minor issue found:
    
    FROM:  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    Target.Value = Oldvalue & “, ” & Newvalue  
    End If
    
    TO:
    
    If Oldvalue = “” Then  
    Target.Value = Newvalue
    
    ElseIf Target.Value = Oldvalue Then ‘= 2 And Target.Row <
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8462)
    
    *   Thanks for sharing! Makes sense
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8507)
        
        *   I think I’m having the problem of duplicating values. If I make multiple selections from a drop down list for a cell and then try to put in something that is not from the drop down list, I end up with several repetitions of what I had selected in the same cell. Then when I try to delete some of the repeated values, it will repeat itself again in the same cell. So it becomes an endless cycle of repetitions until I just delete the entire cell. But I can’t figure out how to fix this. I tried to put in the code that spyrule shared but I may not be doing it right. I’m new to Vbasic so I don’t really understand the code…
            
            This is what I ended up with:
            
            Oldvalue = Target.Value  
            If Oldvalue = “” Then  
            Target.Value = Newvalue  
            Else  
            If Target.Value = Oldvalue Then  
            GoTo Exitsub  
            Else  
            Target.Value = Oldvalue & “;” & Newvalue  
            End If  
            End If  
            End If  
            Application.EnableEvents = True
            
            Thank you for posting. This was really helpful.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8598)
            
            *   Hi Sumit, id you give an solution to this problem. I cannot seem to find a solution here.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8618)
                
378.  Hi thank you for this nice tutorial. Now, instead of separating the multiple selections by a comma, I want to add the additional selections in the adjacent cells in the same row. But still have the feature of removing previously selected items. Can you please help me with that?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8300)
    
379.  How does the code need to be changed if, instead of separating the multiple selection by a comma, the additional selections are added in separate cells in the same row? But still with the replacing feature included?  
    thank you very much for your help!!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8299)
    
380.  Hi, I’ve been looking for this. This is a very great tip. Thank you so much for this advise.  
    Wish you the best,
    
    Dara from Cambodia
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-7138)
    
381.  The code worked great and I was so happy with finally being able to add my products within the same cell.  
    The next day however I went to open the file and now the code isn’t working??? It just went back to normal> I saved it as a Macro as well.  
    Does anyone know what I can do to fix this issue???  
    Please help and Thanks in advance!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-4473)
    
    *   I have had the same issue – even though the spreadsheet was saved as macro-enabled, the code never works when I close and reopen the spreadsheet
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-13843)
        
382.  What if I wish to have more than one dropdown with different multible choice
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-4046)
    
383.  Hi Sumit
    
    a great thanks for great efforts  
    I have zero VBA knowledge, so used your code to work with  
    I already saved as XLSM, however  
    every time I enter a value in droplist, then try to select another value from it, I get an error “syntax error”  
    something strange, though I ready your code worked smoothly with other readers, only sadly with me, didn’t  
    I hope you can reply to me with solution or cause of error at least
    
    thanks  
    webo [https://uploads.disquscdn.com/images/6b616b8c296f18f73245dd1ceba825bad42f3a7e5982c0ec1d7b9ddfd4275874.jpg](https://uploads.disquscdn.com/images/6b616b8c296f18f73245dd1ceba825bad42f3a7e5982c0ec1d7b9ddfd4275874.jpg)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-4036)
    
384.  Hi Sumit. I have read through all of the posts and it has helped me a lot. Just one more question if you don’t mind. I need a secondary list to select the items from that would only display the items that I selected in the first list. Please help me out as I am working for a company and this database needs this function immediately for me to start entering the data in it accordingly.  
    Thank You for your post and your help.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3995)
    
    *   hello Kevin. Have a look at this tutorial: [http://trumpexcel.com/2013/07/dependent-drop-down-list-in-excel/](http://trumpexcel.com/2013/07/dependent-drop-down-list-in-excel/)
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-4011)
        
385.  Hi Sumit,
    
    Thank you for sharing your code. I am able to get it to work except that when I make a 2nd selection (or 3rd, 4th, etc.), I get a green triangle trace error in the cell. It is saying that the value doesn’t match the data validation restrictions defined for the cell. Do you know what may be causing this and how to fix it?
    
    Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3994)
    
    *   I’ve been playing around with this some more and have realized that the error only appears when I have my spreadsheet formatted as a table. I’m not sure why, but when it is not formatted, there is no error. Is there any way to fix this or change the code to address this?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3998)
        
        *   Hey.. I tried converting the data into a table and see if I could replicate the error. It worked fine for me. Would be great if you could share your file. Can have a look and see what’s causing that.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-4012)
            
            *   Thanks, Sumit. I tried creating this in new worksheets as well, having the same problem. I would create the drop down list and it would work fine. But as soon as I “format as table” the trace error appears.
                
                How can I send you the file?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-4018)
                
                *   Hi Joe & Sumit, were you able to finally get rid of the yellow triangle with an exclamation on the top left corner of the cell? I am assuming that was what you were also getting. Please let me know. Thanks.
                    
                *   Nevermind. I got it sorted by converting it from Table to Convert to Range. Thanks again for sharing.
                    
386.  Hi Sumit, Thanks for the code, but after I close it, I cannot run it. Usually I assign the maro to a shape box, but since it is a drop down menu, I couldnt assign a macro name and it is not running. Wondering why? Thanks!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3779)
    
387.  Hi there,
    
    I’m struggling a bit with what looks like others have been able to solve below. I have a spreadsheet where I’d like to enable multiple pick lists in columns E, M, and N only (down to row 100 or so in each). I don’t want multiple pick list in the other columns. Can you tell me exactly what to enter for the code? I’d be most grateful for your guidance.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3593)
    
388.  Hi, when i attempt to filter a column that has cells with more than one value- the filtering system cannot pick out individual values, and instead picks them all per cell. Is there anyway to filter based on ONE value for all the cells(those that have many values and those that have one-separated by a comma?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3556)
    
389.  Thanks. This was very useful. Precisely what I needed.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3528)
    
390.  Hi, Can somebody help me change target is one address to one Range ==>  
    If Target.Address = “$C$2” Then
    
    Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3434)
    
391.  This is great! Thank you so much for this. I have one question though. I’ve read the comments and can’t find the same question being asked – apologize if I missed it.
    
    I am able to select multiple options from a dropdown box successfully, however I can’t find a way to them remove one of the options unless I clear the entire cell.
    
    For example, I select options such that my cell looks like: Apple, Orange, Banana.
    
    I no longer want Orange selected. If i try to delete the Orange text, it doesn’t work.
    
    The only way I’ve found to do this is to delete all contents of the cell, then go back and select Apple and Banana from the dropdown.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3416)
    
    *   Hello Shelley.. This is the drawback of using a drop-down list here. As soon as you delete an item and hit enter, Excel takes it as another entry that you are trying to make, and shows an error since that’s not a part of the drop down.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3418)
        
    *   Hello Shelley.. This is the drawback of using a drop-down list here. As soon as you delete an item and hit enter, Excel takes it as another entry that you are trying to make, and shows an error since that’s not a part of the drop down.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3449)
        
        *   Hi, this code seems to be working well for me, but can you tell me if it’s possible to ensure that once the selections are made they appear in alphabetical order?
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3499)
            
            *   Hi, am also facing this problem can you resolve this one?…
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9421)
                
            *   Me too. I need any suggestions for this case.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-11279)
                
392.  Hello I add the code to be used in C8 for 2 spreadsheets, the drop meny works only in C8 but I want it to be working until C200, please advise.
    
    Angie
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3381)
    
    *   Hello Angie.. you can replace this line: If Target.Address = “$C$2” Then  
        with this line:  
        If Target.column = 3 Then
        
        Now the drop down will work for all the cells in Column C
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3453)
        
393.  Hi there – I tried to use this code but it is not allowing me to add multiple values in 3 of my columns.
    
    Option Explicit
    
    Private Sub Worksheet\_Change(ByVal Target As Range)
    
    ‘Code by Sumit Bansal from [http://www.trumpexcel.com](http://www.trumpexcel.com/)
      
    ‘ To Select Multiple Items from a Drop Down List in Excel
    
    Dim Oldvalue As String  
    Dim Newvalue As String
    
    On Error GoTo Exitsub  
    If Target.Address = “$J$2” Or Target.Address = “$K$2” Or Target.Address = “$L$2” Then  
    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
    GoTo Exitsub  
    Else: If Target.Value = “” Then GoTo Exitsub Else  
    Application.EnableEvents = False  
    Newvalue = Target.Value  
    Application.Undo  
    Oldvalue = Target.Value  
    If Oldvalue = “” Then  
    Target.Value = Newvalue  
    Else  
    Target.Value = Oldvalue & “, ” & Newvalue  
    End If  
    End If  
    End If  
    Application.EnableEvents = True
    
    Exitsub:  
    Application.EnableEvents = True
    
    End Sub
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3349)
    
    *   Actually – it is working in all columns but only in cell 2 on each.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3350)
        
        *   Same issue???
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3352)
            
            *   Yes same issue – actually I abandoned this option because I wanted to be able to filter on just one value within the whole field (set of suburbs for the South in one and wanted to filter on just one of those suburbs) but it won’t allow me to filter that way.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3364)
                
                *   hello Ange  
                    can you tell me what option you decided to use. thanks
                    
394.  Hi Sumit,  
    This worked great thanks, this question leads on from what I have now achieved with this code. Now that I have selected multiple entries in some cell (I have applied this code to an entire column) but not all, I would like to filter down to entries within that column, ie find all entries that contain orange or blue. So I have applied the usual filter to my heading row but when I click on this I would like the options to filter to appear the same way it would if there were only one entry in each cell, but it has the lists/multiple entries as options. Basically I want filter function to comma separate my lists I guess? Does that make sense? Any suggestions? I can just type in the colour in the search option under filter but that doesn’t work if I want multiple colors at once.  
    Thanks,
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3343)
    
    *   did you find a solution? i have been looking for days and there appears to be no way…
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3555)
        
395.  I am having an issue with the code. My lists are in sheet 2, but my drop downs are in sheet 1. How do I need to change the code to accommodate this? Thank you!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3327)
    
396.  Great solution. How can I get each entry to go into an new line (issuing a line feed after the selection?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3267)
    
397.  another thing how can I defind that with in a table in excel and that it could move automaticly with the table?  
    thanx
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3264)
    
398.  hi, followed this thread found it the most helpfull, but I need to tweek it a little bit more.  
    I need the selection to be words (strings) and after the selection the return value needs to be a sum of numbers, each word get its value – a number.  
    how can I do this ?  
    please help, I have been struggling with this one for three moths now.  
    thanx.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3263)
    
399.  Thank you, this has been very helpful. I have set up multiple selection list in L5 using your code. In M5, I have a dependent selection list that recognizes a selection in L5. However, I am having trouble with this dependent list recognizing multiple selections. Any thoughts?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3209)
    
400.  This is a great solution for MS Excel, do you have any idea if something similar would work for MS Project?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3120)
    
    *   Hello Mark.. I am not sure if this can be done with MS Project. I know a guy who is an MS Project champion. Will ask him and post back
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3136)
        
401.  How do I make the macro work on a range of cells? For example cells L2 through L10000.
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3080)
    
    *   You’ll need to modify the code. Change the following line:  
        If Target.Address = “$C$2” OR Target.Address = “$D$2” Then  
        to  
        If Target.Column = 11 AND Target.Row > 1 AND Target.Row < 10001 Then
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3094)
        
        *   I was using  
            If Target.Address = “$G$2” Then
            
            This worked on the one cell – allowing multiple selections in the same cell with a comma between.  
            I need to allow this on the entire column. When I change the code to
            
            If Target.Column = 6 Then
            
            Or
            
            If Target.Column = 6 AND Target.Row > 1 AND Target.Row < 10001 Then I can not longer select multiple selections in the same cell. What am I doing wrong?
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-10271)
            
402.  I need to know how to do TWO drop down lists with multiple choice selections on both . this must happen on the same sheet. Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3028)
    
    *   Hello Khushal.. You’ll need to modify the code. Change the following line:  
        If Target.Address = “$C$2” OR Target.Address = “$D$2” Then
        
        Change the references to what you want.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3029)
        
        *   Hi. Would this allow me to do two concurrent multiple choice selectons. I am assuming I need to have 2 target address in the VBA code.Forgive my zero sense of VBA. Thanks
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3030)
            
            *   Yes this should do it. The line in my last comment specifies two target address which would enable both the drop downs in the these cells to have multiple selection functionality
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3031)
                
            *   Hi. Just tried your suggestion and it works . Your’e great . Thanks
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3032)
                
            *   Hi Sumeet. I have tried your code suggestions and it works I have even tried 4 drop down list multiple selections and it works.
                
                Just one question, when I save my work I am askes to save as a macro sheet. Is this the only way to save. What is your sugestio on the safest way to save. I may want to share this with others as well and they must be able to open the file.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3034)
                
                *   You’ll have to save it in either .XLS or .XLSM format. Since it contains a macro, you can’t save it in the .XLSX format. Once you save it, it won’t show the prompt again. You can also share it with other people and there shouldn’t be any issue.
                    
                *   Help…saved as .XLSX format but when I save, close and reopen the coding is gone!
                    
                *   Yes, I have the same issue. I tried .XLS and .XLSM. Both happens the same… the code is gone after I reopen my file. 🙁
                    
                *   Hi Sumitji, I am wondering if there is a solution to this question. I “save as” and on the copy, the code is gone and I can no longer make multiple selections from the drop down list. I am creating a mental health treatment plan template so I would like to be able to use this template over and over again for new patients. Any ideas on how I can “save as” and retain the code and formatting?
                    
403.  Hi Sumit. Is it possible to have another drop down list under a different column? If yes, how do I do it? Thank you!
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2943)
    
    *   Hello Kirsten.. You can have the same functionality for any cell/column. You would need to change this line in the code:  
        If Target.Address = “$C$2” Then
        
        If you want it for an entire column (say column D), make it:  
        If Target.Column = 4 Then
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2965)
        
404.  This is really great, I’ve been looking for this option. My question is, I’ve followed your instructions from above to modify the code and get it working on just one column, in this case column 7.
    
    However, I’d like to get it working on column 6 too but instead of having the comma seperate each value I want to use a hyphen instead. So currently on column 7 the output is “1, 2, 3, 4”. On column 6 I want the output to be “1-2-3-4”.
    
    I’ve played around with the code a bit but I can’t seem to get it right…any suggestions?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2941)
    
    *   Hello.. Kindly have a look at this file: [https://www.dropbox.com/s/7qbmv6k5ki3w0l9/Multiple-Selection-from-a-Drop-Down-List-in-Excel\_Custom%20Separator.xlsm?dl=0](https://www.dropbox.com/s/7qbmv6k5ki3w0l9/Multiple-Selection-from-a-Drop-Down-List-in-Excel_Custom%20Separator.xlsm?dl=0)
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2966)
        
405.  Can you use this concept and remove options as they are chosen. The additional tutorial above Creating Multiple Drop-down Lists in Excel without Repetition removes but its multiple cells. I want something that allows multiple selections as above tutorial but removes them as you choose them so they are not duplicated. TIA
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2900)
    
    *   Hello Emily, you can use the below code to make sure an option doesn’t get selected multiple times:
        
        Private Sub Worksheet\_Change(ByVal Target As Range)  
        ‘Code by Sumit Bansal from trumpexcel.com  
        ‘ To Select Multiple Items from a Drop Down List in Excel  
        Dim Oldvalue As String  
        Dim Newvalue As String  
        Application.EnableEvents = True  
        On Error GoTo Exitsub  
        If Target.Address = “$C$2” Then  
        If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
        GoTo Exitsub  
        Else: If Target.Value = “” Then GoTo Exitsub Else  
        Application.EnableEvents = False  
        Newvalue = Target.Value  
        Application.Undo  
        Oldvalue = Target.Value  
        If Oldvalue = “” Then  
        Target.Value = Newvalue  
        Else  
        If InStr(1, Oldvalue, Newvalue) = 0 Then  
        Target.Value = Oldvalue & “, ” & Newvalue  
        Else:  
        Target.Value = Oldvalue  
        End If  
        End If  
        End If  
        End If  
        Application.EnableEvents = True  
        Exitsub:  
        Application.EnableEvents = True  
        End Sub
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2903)
        
        *   Is this code in addition to the original code in the tutorial? You didn’t specify if this is a replacement or in addition to. TIA. Great tutorial by the way.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2922)
            
            *   Hi i am also facing the same issue how can we run the code while having the sheet protected… pls help its really urgent
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9176)
                
        *   Hi how can we run the code while having the sheet protected… pls help its really urgent
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9177)
            
406.  Great post. Followed it but can you suggest what to do if we want to delete / remove a selection made earlier. I mean suppose we select three mutiple options and i have to remove second one then how to do it? Also how to apply this to entire column (i.e from c2 till end)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2877)
    
    *   You can modify the code to automatically delete an entry when you select it again, but I believe it would be easier if you simply delete it manually (unless you have tens/hundreds of options selected. To apply this to all the cells in column C, replace the line
        
        If Target.Address = “$C$2” Then
        
        with
        
        If Target.Column = 3 Then
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2902)
        
        *   Hi Sumit, I have run into a snag. I started with your code at the top of the thread and started making changes based on your recommendations.  
            1\. Allow for multiple selections. (First code given on page) -Works.  
            2\. changed the code from Target.address = “$C$2 Then to If Target.Column = 10 And Target.Row > 3 And Target.Row < 43 – Works.  
            3\. I changed the code per your recommendation so you can't select the same option again. – Works.  
            I ran into a snag when I need to un-select a previously selected item from the list. I tried to delete the text in the cell, but it gives me the error box. (Use case is that after review with teams, we need to change the selected teams)
            
            Second Question, From a user experience perspective do you have a way to do this with Checkboxes so you can select all at once (either selecting or deselecting) the radio buttons for each item?
            
            Thanks for all your help!  
            Doug
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3247)
            
        *   Hi Sumit!  
            Thanks in advance for providing us the code for multiple selection in drop down list. I am facing the problem in deleting. As soon as I delete any wrong selection from the list and hit the enter or tab key, it re-appears on the same list. Please help
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-8981)
            
            *   Hi,  
                Were you able to find any solution for deleting/removing previously selected items?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9431)
                
                *   [https://www.youtube.com/watch?v=cRpTzOnaf48](https://www.youtube.com/watch?v=cRpTzOnaf48)
                    
                    This might help.
                    
                *   It was previously posted by Epps
                    
                *   I usually just right click on the cell and choose “clear contents” and then I can start over.
                    
        *   Hi Sumeet,  
            Thanks for the code! Can you please let me know how can i deselect an entry?I am not able to delete an entry manually.  
            Thanks in advance.  
            Regards,  
            Soumya
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9595)
            
407.  this is really cool! thanks a lot! Can I have combine with the drop down ists in Excel without Repetition?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2857)
    
    *   Hello Anu.. Below is the code you can use. If there is already a value in the cell and you select it again, it will not append it to the existing value.
        
        Private Sub Worksheet\_Change(ByVal Target As Range)  
        ‘Code by Sumit Bansal from [http://www.trumpexcel.com](http://www.trumpexcel.com/)
          
        ‘ To Select Multiple Items from a Drop Down List in Excel  
        Dim Oldvalue As String  
        Dim Newvalue As String  
        Application.EnableEvents = True  
        On Error GoTo Exitsub  
        If Target.Address = “$C$2” Then  
        If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
        GoTo Exitsub  
        Else: If Target.Value = “” Then GoTo Exitsub Else  
        Application.EnableEvents = False  
        Newvalue = Target.Value  
        Application.Undo  
        Oldvalue = Target.Value  
        If Oldvalue = “” Then  
        Target.Value = Newvalue  
        Else  
        If InStr(1, Oldvalue, Newvalue) = 0 Then  
        Target.Value = Oldvalue & “, ” & Newvalue  
        Else:  
        Target.Value = Oldvalue  
        End If  
        End If  
        End If  
        End If  
        Application.EnableEvents = True  
        Exitsub:  
        Application.EnableEvents = True  
        End Sub
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2858)
        
408.  I am working with 2010 Excel. I am right clicking on the sheet name to bring me to the “View Code” option. However, once I insert your code into the box, nothing is happening. What could I be doing incorrectly? Aside from trying code when I have no business doing that…=)
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2743)
    
    *   Hello Arielle.. I have hard coded the cell C2 in the code. You will have to change that cell reference for it to work for you. For example, if you drop down is in cell D2, then change it to D2. Or if there are multiple drop downs in column D, then use Target.Column = 4
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2757)
        
        *   hi sumit, how do I get the target.culumn = 4 to work for two different columns in the same sheet
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2983)
            
        *   hi sumit, how do I get the target.culumn = 4 to work for two different columns in the same sheet
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2984)
            
            *   Hello Edwin. You can use OR in the code to apply it to multiple columns. For example, you can use Target.Column = 4 or Target.Column = 5
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3003)
                
409.  The code to allow multiple selections works great. Do you know how to allow editing of the cells after selections are made? I can’t seem to remove previously selected items. Thanks
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2687)
    
    *   [https://www.youtube.com/watch?v=cRpTzOnaf48](https://www.youtube.com/watch?v=cRpTzOnaf48)
        
        Here is VBA code included with video for drop down list with multiple selection that also allows you to remove previously selected items by reselecting them.
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2741)
        
        *   Could you share the code as this is just what I am looking for? Thanks
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9209)
            
        *   Hi Sumit,  
            Whenever I close the excel file and re-open the code disappears. I have to re-paste the code every time. Any solution?
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9954)
            
            *   you have to enable macros when reopening. Is it saved as macro-enabeled workbook?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9955)
                
410.  Hi, followed this successfully, thanks for the tips. That said, I’m unable to replicate using this code, even when using “Or” commands along the “$C$2” line, to have the code apply to more than one drop-down list within the main workbook. Can you advise me on how I can write/adjust the code such that I can have multiple drop down lists where I am able to select more than one option?
    
    [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2660)
    
    *   For clarification, I want to build a matrix/table where I can select multiple drop-down options across 3-4 columns and 25-40 rows. So, wondering how I will need to adjust the “$C$2” part of that code to include the code for all of the cells in which I’d want to do a multi-select. That make sense?
        
        [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2661)
        
        *   Hello Jason, If you want this to be applied to all the drop downs in your worksheet, remove the following line from the code:
            
            If Target.Address = “$C$2” Then
            
            Also remove one the END IF from the end of the code.
            
            [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2664)
            
            *   Hello. This information was vital, thanks.  
                But if I don’t want to apply the code to all the drop downs in the worksheet, only in on row? For example, only in g5:g53?  
                Can you tell me how to do this?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2738)
                
                *   Hello Claudia.. In the code, you can replace the line
                    
                    If Target.Address = “$C$2” Then
                    
                    with
                    
                    If Target.Column = 7 And Target.Row > 4 And Target.Row < 54 Then
                    
                *   Hello Sumit; thank you so much, it was just what I needed.
                    
                *   I want to apply the VBA Code to cells C7:C80. Is the following correct “If Target.Column = 3 And Target.Row > 6 And Target.Row < 81 Then"? Thanks!
                    
                *   Phil thank you so much this was just what I needed
                    
                *   Thank you Sumit! It worked for me today. Happy New Year 2018!
                    
            *   When I did this it worked for the drop downs but it also caused every cell to show multiple entries. Is there a way to apply it to a specific number of cells, say 5. Thanks in advance.
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-2898)
                
                *   Hello Emily.. You can specify the cells in this line
                    
                    If Target.Address = “$C$2” Then
                    
                    For example, if you want the drop down to work on C2 and C3, use:
                    
                    If Target.Address = “$C$2” OR Target.Address = “$C$3” Then
                    
                *   Thanks so much for the assistance. Everything is working well now. I do have anther question. Is it possible to have an option for the user to add their own entry to a list? I know I can turn off the the error message and allow them to type something, but I want their to be an item on the list like “other” and then when they select it they can enter their info. How can I make this work? Any suggestions. I have spent an hour searching online without any results. TIA
                    
                *   Hi Sumit – Thank you for this wealth of knowledge! I am trying to apply this code to 3 different drop down lists in the same worksheet – cells P7:P70; AD7:AD70 and AH7:AH70. How can I do that? Thank you!
                    
                *   Never mind…figured it out! Thanks for the post/information though!
                    
                    Private Sub Worksheet\_Change(ByVal Target As Range)
                    
                    Dim RngDV As Range  
                    Dim Oldvalue As String  
                    Dim Newvalue As String  
                    If Target.Count > 1 Then GoTo Exitsub
                    
                    On Error Resume Next  
                    Set RngDV = Cells.SpecialCells(xlCellTypeAllValidation)  
                    On Error GoTo Exitsub
                    
                    If RngDV Is Nothing Then GoTo Exitsub
                    
                    If Intersect(Target, RngDV) Is Nothing Then  
                    ‘do nothing
                    
                    Else  
                    Application.EnableEvents = False  
                    Newvalue = Target.Value  
                    Application.Undo  
                    Oldvalue = Target.Value  
                    Target.Value = Newvalue  
                    If Target.Column = 16 Then  
                    If Oldvalue = “” Then  
                    ‘do nothing  
                    Else  
                    If Newvalue = “” Then  
                    ‘do nothing  
                    Else  
                    Target.Value = Oldvalue \_  
                    & “;” & Newvalue  
                    End If  
                    End If  
                    End If  
                    If Target.Column = 30 Then  
                    If Oldvalue = “” Then  
                    ‘do nothing  
                    Else  
                    If Newvalue = “” Then  
                    ‘do nothing  
                    Else  
                    Target.Value = Oldvalue \_  
                    & “;” & Newvalue  
                    End If  
                    End If  
                    End If  
                    If Target.Column = 34 Then  
                    If Oldvalue = “” Then  
                    ‘do nothing  
                    Else  
                    If Newvalue = “” Then  
                    ‘do nothing  
                    Else  
                    Target.Value = Oldvalue \_  
                    & “;” & Newvalue  
                    End If  
                    End If  
                    End If
                    
                    End If
                    
                    Exitsub:  
                    Application.EnableEvents = True
                    
                    End Sub
                    
                *   Thanks, I needed this
                    
                *   I want to apply your code (allowing one instance of multiple choices from a drop down) but it applies this code to the whole sheet so cells that are just to be typed into can have multiple entries, so if someone types into a cell then goes back and wants to over write this info it appears side by side in the one cell with a , seperating them,  
                    I only want to apply your code to cells C12 to C16 and have made the follwoing adjustments:
                    
                    Private Sub Worksheet\_Change(ByVal Target As Range)
                    
                    Dim Oldvalue As String  
                    Dim Newvalue As String  
                    Application.EnableEvents = True  
                    On Error GoTo Exitsub  
                    If Target.Address = “C12” Or Target.Address = “C13” Or Target.Address = “C14” Or Target.Address = “C15” Or Target.Address = “C16” Then  
                    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
                    GoTo Exitsub  
                    Else: If Target.Value = “” Then GoTo Exitsub Else  
                    Application.EnableEvents = False  
                    Newvalue = Target.Value  
                    Application.Undo  
                    Oldvalue = Target.Value  
                    If Oldvalue = “” Then  
                    Target.Value = Newvalue  
                    Else  
                    If InStr(1, Oldvalue, Newvalue) = 0 Then  
                    Target.Value = Oldvalue & “, ” & Newvalue  
                    Else:  
                    Target.Value = Oldvalue  
                    End If  
                    End If  
                    End If  
                    End If  
                    Application.EnableEvents = True  
                    Exitsub:  
                    Application.EnableEvents = True  
                    End Sub
                    
                *   ‘ I just swapped out Target.Address for Target.Column. Tested and working.
                    
                    Private Sub Worksheet\_Change(ByVal Target As Range)  
                    Dim Oldvalue As String  
                    Dim Newvalue As String  
                    Application.EnableEvents = True  
                    On Error GoTo Exitsub  
                    If Target.Column = “C12” Or Target.Column = “C13” Or Target.Column = “C14” Or Target.Column = “C15” Or Target.Column = “C16” Then  
                    If Target.SpecialCells(xlCellTypeAllValidation) Is Nothing Then  
                    GoTo Exitsub  
                    Else: If Target.Value = “” Then GoTo Exitsub Else  
                    Application.EnableEvents = False  
                    Newvalue = Target.Value  
                    Application.Undo  
                    Oldvalue = Target.Value  
                    If Oldvalue = “” Then  
                    Target.Value = Newvalue  
                    Else  
                    If InStr(1, Oldvalue, Newvalue) = 0 Then  
                    Target.Value = Oldvalue & “, ” & Newvalue  
                    Else:  
                    Target.Value = Oldvalue  
                    End If  
                    End If  
                    End If  
                    End If  
                    Application.EnableEvents = True  
                    Exitsub:  
                    Application.EnableEvents = True  
                    End Sub
                    
            *   Hi Sumit, This is really helpful but I’m not sure which “END IF” to remove. There’s three in the code, do I remove all three?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3150)
                
            *   Sumit – I was wonder if you could assist me. I have a column titled ‘Services’ and have created dropdown list in each cell. The worksheet has about 186 rows (and growing). I used this code to be able to select multiple and have them show up in each cell. I took out ‘IF Target.Address = “$C$2” Then and one END IF and not it works for all cells that has the dropdown list. HOWEVER, whenever I type anything in any other cell, it doubles/replicates what I already had in there plus what I was typing. I’m guessing that is because of the code I put in for the dropdowns. Could you help?
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-3506)
                
            *   thank a lot. your a life safer 🙂
                
                [Reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#comment-9350)
                

### Leave a Comment [Cancel reply](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/#respond)

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