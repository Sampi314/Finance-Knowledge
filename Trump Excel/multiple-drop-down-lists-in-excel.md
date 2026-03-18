# Creating Multiple Drop-down Lists in Excel without Repetition

**Source:** https://trumpexcel.com/multiple-drop-down-lists-in-excel

---

[Skip to content](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#below-title)

**Watch Video – Creating Multiple Drop-down Lists in Excel without Repetition**

[Excel Drop Down Lists](https://trumpexcel.com/excel-drop-down-list/)
 are intuitive to use and extremely useful in when you are creating an [Excel Dashboard](https://trumpexcel.com/creating-excel-dashboard/)
 or a [data entry form](https://trumpexcel.com/data-entry-form/)
.

You can create multiple drop-down lists in Excel using the same source data. However, sometimes, it is needed to make the selection exclusive (such that once selected, the option should not appear in other drop-down lists). For example, this could be the case when you are assigning meeting roles to people (where one person takes one role only).

##### Creating Multiple Drop-down Lists in Excel without Repetition

In this blog post, learn how to create multiple drop-down Lists in Excel, where there is no repetition. Something as shown below:

![Multiple Drop-Down Lists in Excel - No Repeat](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20408%20220'%3E%3C/svg%3E)

To create this, we need to create a [dynamic named range](https://trumpexcel.com/named-ranges-in-excel/)
 that would update automatically to remove a name if it has already been selected once. Here is how the back-end data looks like (this is in a separate tab while the main drop-down is in a tab named ‘Drop Down No Repetition’).

![Multiple Drop-Down Lists in Excel - Backend Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20173'%3E%3C/svg%3E)

Here is how you can create this back-end data:

1.  Column B (Member List) has the list of all the members (or items) that you want to show in the drop-down list
2.  Column C (Helper Column 1) uses a combination of [IF](https://trumpexcel.com/excel-if-function/)
     and [COUNTIF](https://trumpexcel.com/excel-countif-function/)
     functions. This gives the name if the name has not already been used, else it gives a blank.

\=IF(COUNTIF('Drop Down No Repetition'!$C$3:$C$7,B3)>0,"",B3)

1.  Column D (Helper Column 2) uses a combination of IF and [ROWS](https://trumpexcel.com/excel-rows-function/)
     functions. This gives the serial number if the name has not been repeated, else it gives a blank.

\=IF(C3<>"",ROWS($C$3:C3),"")

1.  Column E (Helper Column 3) uses a combination of [IFERROR](https://trumpexcel.com/excel-iferror-function/)
    , [SMALL](https://trumpexcel.com/excel-small-function/)
    , and [ROWS](https://trumpexcel.com/excel-rows-function/)
    . This stacks all the available serial numbers together.

\=IFERROR(SMALL($D$3:$D$9,ROWS($D$3:D3)),"")

1.  Column F (Helper Column 4) uses a combination of IFERROR and [INDEX](https://trumpexcel.com/excel-index-function/)
     functions. This gives the name that corresponds to that serial number.

\=IFERROR(INDEX($B$3:$B$9,E3),"")

1.  Use the following steps to create a dynamic named range
    *   Go to Formula –> Name Manager
    *   In the Name Manager dialogue box, select New
    *   In the New Name Dialogue Box, use the following details
        *   Name: DropDownList
        *   Refers to: \=List!$F$3:INDEX(List!$F$3:$F$9,COUNTIF(List!$F$3:$F$9,”?\*”))  
            _This formula gives a range that has all the names in column F. It is dynamic and updates as the names change in Column F.![Multiple Drop-Down Lists in Excel - Dynamic Named Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20190'%3E%3C/svg%3E)_
2.  Go to Tab Drop Down No Repetition, and create a data validation drop-down list in cell range C2:C6. Here are the steps to do this:
    *   Go to Data –> Data Tools –> Data Validation
    *   In the Data Validation dialogue box, use the following:
        *   Validation Criteria: List
        *   Source: =DropDownList
    *   Click OK

Now your drop down list is ready, where once an item is selected, it does not appear in subsequent drop-downs.

_**Try it yourself.. Download the file  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Multiple-Drop-Down-Lists-without-Repetition.xlsx)
**_

**Other Useful Articles on Drop-Down Lists in Excel:**

*   [How to Create a Dependent Drop-Down List in Excel](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    .
*   [Extract Data from Drop-Down List Selection in Excel](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [Disguise Numbers as Text in a Drop-Down List](https://trumpexcel.com/format-numbers-as-text-excel/)
    .
*   [Create a Drop-Down List with Search Suggestions](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [Multiple Selection from a Drop-Down List in a Single Cell](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    .
*   [How to Make a Yes/No Drop-Down in Excel?](https://trumpexcel.com/make-yes-no-drop-down-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “Creating Multiple Drop-down Lists in Excel without Repetition”
------------------------------------------------------------------------------

1.  also, right now it is delimited by a comma. and i want to apply the new line to all the cells it 4 columns and and i have 504 lines for each unit person
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-13752)
    
2.  Question, So lets say i orginally set up for mulitple colums to select form a drop down. 1. how can i apply the next line to all the cells without haveing to reselect? and 2 how can it auto alphabitized the list ( ie i hae trust names for my drop donw\_ so if i have ABC Trust, KMJ Trust and YXF Trust but I selected them in different order so it KMJ, ABC adn YXF but i want it to be ABC, KMJ adn YXF.
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-13751)
    
3.  Hi,
    
    I am using multiple drop down lists but they are from different sources. It is for a rota where some people have more skills and therefore can be used more than others.
    
    The rota lists all the roles needed so each role has a drop down which comes from its own independent source list.
    
    What I am trying to do is when I have selected one person they either:  
    do not appear in the other drop down lists or  
    An error message comes up when a name has been selected more than once.
    
    By using different source lists, this is complicating the issue but as not all people can do all roles, i cannot see another option.
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-10711)
    
    *   Did you ever figure this out? I am trying to do the exact same thing.
        
        [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-14296)
        
4.  Thanks! Having trouble though. When I add a name everything works fine all the way to the numbers re-stacking (in helper column 3) but then all the names on the list get repeated in helper column 4.
    
    i.e.
    
    I Start with Bill, Jo, Frank and Susan. The first person assigned is Susan, In Column 4 the following shows up.
    
    Bill  
    Jo  
    Frank  
    Bill
    
    Jo
    
    Frank  
    Susan
    
    Any ideas? Im working in Google docs. Maybe that’s the problem?
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-3789)
    
    *   I think it’s the Google Sheets issue.
        
        [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-3793)
        
5.  Invaluable writing ! For my two cents , if someone require to merge PDF or PNG files , We discovered a service here [http://goo.gl/1widdK](http://goo.gl/1widdK)
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-3066)
    
6.  I am working on a simple form using excel. I have 4 cells with drop  
    down lists where I have the following code (with your help) to allow for multiple  
    selections without repetition.
    
    Private Sub Worksheet\_Change(ByVal Target As Range)  
    ‘Code by Sumit Bansal from [http://www.trumpexcel.com](http://www.trumpexcel.com/)
    
    ‘ To Select Multiple Items from a Drop Down List in Excel  
    Dim Oldvalue As String  
    Dim Newvalue As String
    
    Application.EnableEvents = True  
    On Error GoTo Exitsub  
    If Target.Address = “$C$10” Or Target.Address = “$C$16” Or Target.Address = “$C$17” Or Target.Address = “$C$19” Then
    
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
    
    My problem is that I need to protect the sheet. When I do this, the  
    user can still access the drop down list but the option for multiple  
    selections without repetition quits working. How can I fix this issue.  
    Thanks in advance for any assistance.
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-2927)
    
    *   I have the same issue Emily, did you find the answer?
        
        [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-10287)
        
        *   Hey Julie,
            
            To make sure the code works on protected sheets, add the following line of code to the macro (right after the Dim statement).  
            Me.Protect UserInterfaceOnly:=True
            
            Also, make sure the cell that has the drop-down list is not protected (when you protect the entire sheet. You can do that by changing the Locked property). You can read more about it here: [https://trumpexcel.com/lock-cells-in-excel/](https://trumpexcel.com/lock-cells-in-excel/)
            
            [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-10289)
            
7.  How can you expand this to use for say 100 items in your drop down list.
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-2899)
    
    *   Hello Emily.. You can expand this to 100 items by changing the references in the formulas and the named range. Here is a template where I have added 100 options in the drop down: [https://www.dropbox.com/s/5b9ksmkim4ynv6g/Multiple%20Drop%20Down%20Lists%20without%20Repetition%20-%20100%20Options.xlsx?dl=0](https://www.dropbox.com/s/5b9ksmkim4ynv6g/Multiple%20Drop%20Down%20Lists%20without%20Repetition%20-%20100%20Options.xlsx?dl=0)
        
        [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-2904)
        
8.  Love this! It’s possible to do with only three helper columns, though. You can remove the first helper column if you use this in the second:
    
    \=IF(ISERROR(MATCH(B3,’Drop Down No Repetition’!C$3:C$7,0)),MATCH(B3,B$3:B$9,0),””)
    
    Always a fan of reducing helper columns!
    
    [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-1490)
    
    *   Thanks for sharing Shanks 🙂 Glad you liked it. And you are right, the first helper column could have been avoided. Just wanted to make it simple to follow in the article.
        
        [Reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#comment-1493)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/multiple-drop-down-lists-in-excel/#respond)

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