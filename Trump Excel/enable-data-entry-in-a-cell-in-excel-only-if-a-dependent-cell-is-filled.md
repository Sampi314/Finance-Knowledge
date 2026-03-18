# Enable Data Entry in a Cell only if a Dependent Cell is Filled in Excel

**Source:** https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled

---

[Skip to content](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#below-title)

You would have seen this in various online forms, where you must fill a cell before moving to the other. This makes sure that you’re restricted unless you make certain data entry (or fill a certain field).

For example, you may not be able to choose the state unless you have selected the country first.

This construct ensures that you do not miss out on filling some of the data. Something as shown below

![Dependent Cell is Filled in Excel](https://trumpexcel.com/wp-content/uploads/2013/12/Fill-Previous-Cell-First.png)

A colleague wanted a similar construct in Excel, and the only thing that came to my mind was Data Validation.

How to Restrict Data Entry in a Cell in based on Another Cell
-------------------------------------------------------------

In this tutorial, I will show you how to restrict entries in a cell based on a formula.

#### **Here is how you can create this in Excel**

1.  Select cell A2.
2.  Go To Data –> Data Tools –> Data Validation.
3.  In the Settings tab go to the Allow drop down and select Custom.
4.  In the Formula field, type \=[NOT](https://trumpexcel.com/excel-not-function/)
    ([ISBLANK](https://trumpexcel.com/excel-is-function/)
    ($A$1)).
5.  Ensure that the Ignore blank is Unchecked.
6.  Click Ok.

![Dependent Cell is Filled in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20361'%3E%3C/svg%3E)

Now when you enter something in cell A2, and if A1 is empty, an error will be displayed.

**You May Also Like the Following Excel Tips and Tutorials:**

*   [Quickly Enter Data in Excel in a Specific Order in Non-Contiguous Cells](https://trumpexcel.com/enter-data-in-excel-in-specific-order/)
    .
*   [10 Excel Data Entry Tips You Can’t Afford to Miss](https://trumpexcel.com/excel-data-entry-tips/)
    .
*   [Creating an Excel Data Entry Form](https://trumpexcel.com/data-entry-form/)
    .
*   [Prevent Duplicate Entries in Excel](https://trumpexcel.com/prevent-duplicate-entries-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “Enable Data Entry in a Cell in Excel only if a Dependent Cell is Filled”
---------------------------------------------------------------------------------------

1.  Dan Walker, I have the same question under the same conditions as yours, and not yet solved,
    
    [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-40735)
    
2.  Thank You!!
    
    [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-12903)
    
3.  I want to enter a date in a cell and for excel to delete a date in another cell automatically – date entered in H6 will delete date entered previously in E6
    
    [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-12682)
    
4.  I want to enter/restrict data entry where the cell has drop down list
    
    [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-12673)
    
5.  I have both quantity cell and expenditure cell.  
    If there is no any value in my quentity cell, i want to blank in expenditure cell also. But if there is any amount in the quentity cell then I can put the value in the expenditure cell.  
    How can I solve this problem please help me to out.
    
    [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-12203)
    
6.  Perhaps consider replacing =not(isblank($A$1)) with =len($a$1)>0  
    Firstly it uses one function instead of 2  
    Second it avoids certain anomalies using isblank.  
    Isblank is also ambiguous… =ISBLANK(” “) → FALSE, so blanks are not blanks as far as IsBlank is concerned.  
    IsBlank should be IsEmpty  
    Further confusion:-  
    Suppose A1 contains a formula resulting in “”.then =ISBLANK(A1) → FALSE  
    Suppose A! contains the text prefix ‘ and nothing else, =ISBLANK(A1) → FALSE
    
    So all in all testing LEN 0 is preferable.  
    REgards  
    BRian
    
    [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-1831)
    
    *   Hi Brian.. Thanks for commenting.. You are right, LEN() would be a more fool-proof way for doing this 🙂
        
        [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-1915)
        
        *   This is simple enough, however, if you then want to apply data validation on what can be entered in A2 you can’t since only one validation is allowed for a cell. So how can you both prevent entry unless A1 is populated AND apply say a validation of a drop list in A2?
            
            [Reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#comment-10304)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/enable-data-entry-in-a-cell-in-excel-only-if-a-dependent-cell-is-filled/#respond)

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