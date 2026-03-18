# Get a List of All the Comments in a Worksheet in Excel

**Source:** https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel

---

[Skip to content](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#below-title)

If you work with Excel worksheets that have a lot of cell comments in a worksheet, this tutorial could be useful. Sometimes you may insert cell comments to highlight or explain data, or your boss may insert comments in cells while reviewing your work.

If you have a huge dataset and the comments are scattered all over the worksheet, it may help to have all comments in a single place as a list.

Get a List of All the Comments in a Worksheet
---------------------------------------------

In this tutorial, I will show you how to use a VBA code to get a list of all the comments in a Worksheet in a separate worksheet.

Something as shown below:

![Get a List of All the Comments in a worksheet in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20468'%3E%3C/svg%3E)

There is a VBA code in the backend that does the following things:

*   It checks whether there are any comments in the active worksheet or not. If there are no comments, it quietly bows out and does nothing.
*   If there are comments in the worksheet, it creates a new worksheet (“Comments”) and extract a list of all the comments in the following structure:
    *   Column A has the cell address that has the comment.
    *   Column B has the commenter name. This comes in handy if there are multiple reviewers of the same file. It will also help filter/sort based on reviewers name.
    *   Column C has the comment.

**Download the Example File  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/i4ng77pnqqdvy21/Extract-Comments.xlsm?dl=1)
**

The VBA Code
------------

Here is the VBA code that does all the heavy lifting here.

Sub ExtractComments()
Dim ExComment As Comment
Dim i As Integer
Dim ws As Worksheet
Dim CS As Worksheet
Set CS = ActiveSheet
If ActiveSheet.Comments.Count = 0 Then Exit Sub

For Each ws In Worksheets
  If ws.Name = "Comments" Then i = 1
Next ws
    
If i = 0 Then
  Set ws = Worksheets.Add(After:=ActiveSheet)
  ws.Name = "Comments"
Else: Set ws = Worksheets("Comments")
End If

For Each ExComment In CS.Comments
  ws.Range("A1").Value = "Comment In"
  ws.Range("B1").Value = "Comment By"
  ws.Range("C1").Value = "Comment"
  With ws.Range("A1:C1")
    .Font.Bold = True
    .Interior.Color = RGB(189, 215, 238)
    .Columns.ColumnWidth = 20
  End With
  If ws.Range("A2") = "" Then
    ws.Range("A2").Value = ExComment.Parent.Address
    ws.Range("B2").Value = Left(ExComment.Text, InStr(1, ExComment.Text, ":") - 1)
    ws.Range("C2").Value = Right(ExComment.Text, Len(ExComment.Text) - InStr(1, ExComment.Text, ":"))
  Else
    ws.Range("A1").End(xlDown).Offset(1, 0) = ExComment.Parent.Address
    ws.Range("B1").End(xlDown).Offset(1, 0) = Left(ExComment.Text, InStr(1, ExComment.Text, ":") - 1)
    ws.Range("C1").End(xlDown).Offset(1, 0) = Right(ExComment.Text, Len(ExComment.Text) - InStr(1, ExComment.Text, ":"))
  End If
Next ExComment
End Sub

How to Use this Code
--------------------

There are a couple of ways you can use this code to get a list of comments from your worksheet:

### #1 Copy Paste Data in the Example File

Copy paste your data (as is) in the Data tab of the download file and then run this macro.

To run this:

*   Go to the Developer tab and click on Macros. It will open the Macro dialogue box.![Get a List of All the Comments in a worksheet in Excel - Macro Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20147'%3E%3C/svg%3E)
*   Select ExtractComment and click on Run. Make sure you are in the sheet that has the comments that you wish to extract.![Get a List of All the Comments in a worksheet in Excel - Run Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20373'%3E%3C/svg%3E)

### #2 Copy Paste the Code in Your Workbook

Copy the code and paste it in the workbook from which you want to extract the comments.

To do this:

*   Activate the workbook in which you are working and press Alt + F11. This will open the VB Editor window.![Get a List of All the Comments in a worksheet in Excel - VBE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20691%20337'%3E%3C/svg%3E)
*   In the Project Explorer on the left, right-click on any of the objects for that workbook, go to Insert –> Module.![Get a List of All the Comments in a worksheet in Excel - Insert Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20402%20340'%3E%3C/svg%3E)
*   Paste the code in the Module code window.
*   Close the VB Editor Window (or press Alt + F11 to go back to the worksheet).

Now you have the macro in your workbook. To run the macro, go to Developer Tab –> Macros. In the Macro dialogue box, select the ExtractComment macro and click in Run.

_Note: Make sure you save the workbook_ with ._XLS or .XLSM extension._

### #3 Create an Add-in

If you need to use this code often, it’s best to [create an add-in](https://trumpexcel.com/excel-add-in/)
 out of it. That way you can easily use it in any workbook (without the additional effort of copy pasting the code again and again).

Here is how to create an Add-in:

*   Go to File –> Save As.![Get a List of All the Comments in a worksheet in Excel - Save As](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%20284'%3E%3C/svg%3E)
*   In the Save As dialogue box, change the Save as type to .xlam.
    *   You’ll notice that the path of the file where it gets saved automatically changes. You can change it if you want.![Get a List of All the Comments in a worksheet in Excel - Save as xlam](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20629%20515'%3E%3C/svg%3E)
*   Open an Excel workbook and Go to Developer –> Add-ins –> Excel Add-ins.![Get a List of All the Comments in a worksheet in Excel - Addin](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20133'%3E%3C/svg%3E)
*   In the Add-ins dialogue box, browse and locate the file that you saved, and click OK.![Get a List of All the Comments in a worksheet in Excel - Activate Addin](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20291%20405'%3E%3C/svg%3E)

Once an add-in has been activated, you can use it in any workbook. To do that, go to Developer –> Macros. In the Macro dialogue box, select the ExtractComment macro and run it.

**Download the Example File  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/i4ng77pnqqdvy21/Extract-Comments.xlsm?dl=1)
**

Hope this code will save you some time. Let me know your thoughts in the comments section.

If you work with Excel, VBA could be a powerful ally. Take your Excel Skills to the next level with the [Excel VBA Course](https://trumpexcel.com/excel-vba-jetpack-course/)
.

**You May Also Like the Following Excel Tutorials:**

*   [How to Insert a Picture in Excel Comment.](https://trumpexcel.com/insert-picture-in-excel-comment/)
    
*   [How to Print Comments in Excel](https://trumpexcel.com/print-comments-excel/)
    
*   [How to Insert a Picture in Excel Comment](https://trumpexcel.com/insert-picture-in-excel-comment/)
    
*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

18 thoughts on “Get a List of All the Comments in a Worksheet in Excel”
-----------------------------------------------------------------------

1.  Able To Extract starts with the initial measurable data set and generates derived values ​.Users can insert and customize their numbers to professionally index business.  
    Philip  
    patchhere.com
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-14893)
    
2.  Here is the corrected code and will print out comments (notes) and threaded comments (review-style comments) in excel – you’re welcome! 😉 :
    
    Sub USEFUL\_PrintCommentsAndNotes()
    
    If MsgBox(“Create a summary of comments and notes from the current workbook?”, vbOKCancel) = vbCancel Then Exit Sub
    
    ‘ “Review” type comments  
    Dim AllCommentsThreaded As Excel.CommentsThreaded  
    Dim OneCommentThreaded As Excel.CommentThreaded  
    Dim AllReplies As Excel.CommentsThreaded  
    Dim OneReply As Excel.CommentThreaded
    
    ‘ “Yellow” notes in excel  
    Dim AllNotes As Excel.Comments  
    Dim OneNote As Excel.Comment
    
    Dim WS, sh As Worksheet  
    Dim r As Range  
    Dim Flag As Boolean  
    Dim i, totalsheets As Integer  
    Dim LinkLocation As String  
    Dim Linkloc, DataLoc, ComBy, ComIn, ComText, ComType As Integer ‘column locations
    
    ‘Create a comments work sheet or append to existing comments  
    Flag = True ‘True if there is not already a worksheet with this name
    
    ‘Create a column location refernce for the data  
    Linkloc = 1  
    DataLoc = 2  
    ComBy = 3  
    ComText = 4  
    ComType = 5
    
    For Each sh In Worksheets  
    If sh.Name = “Comments\_Notes” Then  
    Flag = False  
    Set WS = sh ‘sets the reference worksheet to write comments to  
    i = WS.Range(“A1”).CurrentRegion.Rows.Count + 1 ‘ get last row  
    End If  
    Next sh
    
    If Flag Then  
    Set WS = Worksheets.Add(After:=Worksheets(Worksheets.Count))  
    WS.Name = “Comments\_Notes”  
    WS.Cells(1, Linkloc).Value = “Location Link”  
    WS.Cells(1, DataLoc).Value = “Data at Location”  
    WS.Cells(1, ComBy).Value = “Comment By”  
    WS.Cells(1, ComText).Value = “Comment Text”  
    WS.Cells(1, ComType).Value = “Type”  
    i = 2 ‘new sheet, set comment row
    
    ‘Freeze panes for viewing  
    ‘ActiveWindow.FreezePanes = True  
    End If
    
    ‘Loop through each worksheet to gather comments and notes  
    For Each sh In Worksheets  
    If sh.Name = WS.Name Then  
    ‘MsgBox (“No Comments Here”)  
    ‘Exit For  
    GoTo MoveAlong
    
    End If
    
    Set AllCommentsThreaded = sh.CommentsThreaded  
    Set AllNotes = sh.Comments
    
    ‘ loop over all threaded comments of a worksheet and get their info  
    For Each OneCommentThreaded In AllCommentsThreaded  
    With OneCommentThreaded  
    ‘Debug.Print .Parent.Address .Author.Name, .Date, OneReply.Text  
    LinkLocation = “‘” & sh.Name & “‘!” & .Parent.Address ‘name of corresponding test tab”  
    WS.Cells(i, Linkloc).Hyperlinks.Add \_  
    Anchor:=WS.Cells(i, 1), \_  
    Address:=””, \_  
    SubAddress:=LinkLocation, \_  
    TextToDisplay:=sh.Name & .Parent.Address  
    WS.Cells(i, DataLoc) = “=” & LinkLocation  
    WS.Cells(i, ComBy) = .Author.Name  
    WS.Cells(i, ComText) = .Text  
    WS.Cells(i, ComType) = “Comment”  
    i = i + 1
    
    For Each OneReply In .Replies  
    With OneReply  
    ‘Debug.Print .Author.Name, .Date, OneReply.Text  
    ‘WS.Cells(i, 1) = sh.Name & OneCommentThreaded.Parent.Address  
    WS.Cells(i, Linkloc).Hyperlinks.Add \_  
    Anchor:=WS.Cells(i, 1), \_  
    Address:=””, \_  
    SubAddress:=LinkLocation, \_  
    TextToDisplay:=sh.Name & OneCommentThreaded.Parent.Address  
    WS.Cells(i, DataLoc) = “=” & LinkLocation  
    WS.Cells(i, ComBy) = .Author.Name  
    WS.Cells(i, ComText) = .Text  
    WS.Cells(i, ComType) = “Comment Reply”  
    i = i + 1  
    End With  
    Next OneReply  
    End With  
    Next OneCommentThreaded
    
    ‘ loop over all Notes of a worksheet and get their info  
    For Each OneNote In AllNotes  
    With OneNote  
    ‘WS.Cells(i, 1) = sh.Name & .Parent.Address  
    LinkLocation = “‘” & sh.Name & “‘!” & .Parent.Address ‘name of corresponding test tab”  
    WS.Cells(i, Linkloc).Hyperlinks.Add \_  
    Anchor:=WS.Cells(i, Linkloc), \_  
    Address:=””, \_  
    SubAddress:=LinkLocation, \_  
    TextToDisplay:=sh.Name & .Parent.Address  
    WS.Cells(i, DataLoc) = “=” & LinkLocation  
    WS.Cells(i, ComBy) = .Author  
    WS.Cells(i, ComText) = .Text  
    WS.Cells(i, ComType) = “Note”  
    i = i + 1  
    End With  
    Next OneNote
    
    MoveAlong:  
    Next sh
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-13947)
    
3.  this is great question I have a number of sheet how can I see all across 12 different sheet at the same time
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-13116)
    
4.  Hello sir i want see my all comments in list so that i can easily read all the comment but ther is no more difference between cell. is there any solution to look it
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-12748)
    
5.  I get an error in the last two rows of the code. Anyone else encounter this?
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-12690)
    
6.  Is it possible to make it run automatically? I mean to discover when a new comment was insert and to copy it automatically to another sheet?
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-12452)
    
7.  This macro does not catch all my comments. It stops at row 1531, but I have comments to row 1554.
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-12154)
    
8.  Thanks for the script, it’s very useful. Could you tell me please how I may append the worksheet name to the cell address, since I have many worksheets.
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-11306)
    
9.  Very Helpful!!
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-11014)
    
10.  pixelfollow.com
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-10892)
    
11.  In case there is a picture for the comment Box, how to get the same in another column
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-10187)
    
12.  Is there a way of including the first column cell data for the comment address? This
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-8289)
    
    *   Hey.. Have a look at this file: [https://www.dropbox.com/s/anu1srirmy41ubb/Extract-Comments%20with%20comment%20for%20column.xlsm?dl=0](https://www.dropbox.com/s/anu1srirmy41ubb/Extract-Comments%20with%20comment%20for%20column.xlsm?dl=0)
        
        I have modified the code but you will need to adjust it based on your requirements.
        
        [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-8512)
        
    *   i need vlookup vba
        
        [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-10378)
        
13.  is it possible without VBA ?
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-3922)
    
    *   Hello Deepak.. I don’t think this it can be done without VBA.
        
        [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-3923)
        
14.  You might prefer using the property: ExComment.Author
    
    [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-2835)
    
    *   Thanks for commenting Frank.. .Author property does makes sense here
        
        [Reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#comment-2836)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/#respond)

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