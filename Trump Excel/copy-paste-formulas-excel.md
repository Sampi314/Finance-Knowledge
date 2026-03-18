# Copy and Paste Formulas in Excel without Changing Cell References

**Source:** https://trumpexcel.com/copy-paste-formulas-excel

---

[Skip to content](https://trumpexcel.com/copy-paste-formulas-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/copy-paste-formulas-excel/#below-title)

**Watch Video – Copy and Paste Formulas in Excel without Changing Cell References**

When you copy and paste formulas in Excel, it automatically adjusts the cell references.

For example, suppose I have the formula =A1+A2 in cell B1. When I copy the cell B1 and paste it in B2, the formula automatically becomes =A2+A3.

![Copy and Paste Formulas in Excel - Reference change demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%20192'%3E%3C/svg%3E)

This happens as Excel automatically adjusts the references to make sure the rows and columns now refer to the adjusted rows and columns.

Note: This adjustment happens when you’re using relative references or mixed references. In the case of absolute references, the exact formula gets copied.

Copy and Paste Formulas in Excel without Changing Cell References
-----------------------------------------------------------------

When using relative/mixed references in your formulas, you may – sometimes – want to copy and paste formulas in Excel without changing the cell references.

Simply put, you want to copy the exact formula from one set of cells to another.

In this tutorial, I will show you how you can do this using various ways:

*   Manually Copy Pasting formulas.
*   Using ‘Find and Replace’ technique.
*   Using the Notepad.

### Manually Copy Paste the Exact Formula

If you only have a handful of formulas that you want to copy and paste without changing the cell references, doing it manually would be more efficient.

To copy paste formulas manually:

*   Select the cell from which you want to copy the formula.
*   Go to the [formula bar](https://trumpexcel.com/show-hide-formula-bar-excel/)
     and copy the formula (or press F2 to get into the edit mode and then copy the formula).![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%2056'%3E%3C/svg%3E)
*   Select the destination cell and paste the formula.

Note that this method works only when you have a few cells from which you want to copy formulas.

If you have a lot, use the find and replace technique shown below.

### Using Find and Replace

Here are the steps to copy formulas without changing the cell references:

*   Select the cells that have the formulas that you want to copy.
*   Go to Home –> Find & Select –> Replace.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20193%20146'%3E%3C/svg%3E)
*   In the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
     dialog box:
    *   In the ‘Find what’ field, enter =
    *   In the ‘Replace with’ field, enter #![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20194'%3E%3C/svg%3E)
*   Click OK. This will replace all the equal to (=) sign with the hash (#) sign.
*   Copy these cells.
*   Paste it in the destination cells.
*   Go to Home –> Find & Replace –> Replace.
*   In the Find and Replace dialog box:
    *   In the ‘Find what’ field, enter #
    *   In the ‘Replace with’ field, enter =![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20194'%3E%3C/svg%3E)
*   Click OK.

This will convert the text back into the formula and you will get the result.

Note: If you use the # character as a part of your formula, you can use any other character in Replace with (such as ‘ZZZ’ or ‘ABC’).

Also read: [Remove Formulas (but Keep Data) in Excel](https://trumpexcel.com/remove-formulas-keep-data-excel/)

### Using Notepad to Copy Paste Formulas

If you have a range of cells where you have the formulas that you want to copy, you can use a Notepad to quickly copy and paste the formulas.

Here are the steps to copy formulas without changing the cell references:

*   Go to Formulas –> Show Formulas. This will [show all the formulas](https://trumpexcel.com/show-formulas-in-excel/)
     in the worksheet.![Copy and Paste Formulas in Excel - show formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20692%20117'%3E%3C/svg%3E)
*   Copy the cells that have the formulas that you want to copy.
*   Open a notepad and paste the cell contents in the notepad.
*   Copy the content on the notepad and paste in the cells where you want the exact formulas copied.
*   Again go to Formulas –> Show formulas.

Note: Instead of Formulas –> Show formulas, you can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 Control + \` (this is the same key that has the tilde sign).

**You May Also Like the Following Tutorials:**

*   [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)
    .
*   [Show Formulas in Excel Instead of the Values](https://trumpexcel.com/show-formulas-in-excel/)
    .
*   [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)
    .
*   [Understanding Absolute, Relative, and Mixed Cell References in Excel](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
    .
*   [How to reference another sheet in Excel](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    .
*   [How to Remove Cell Formatting in Excel](https://trumpexcel.com/remove-cell-formatting-in-excel/)
    
*   [How to Copy Excel Table to Word](https://trumpexcel.com/copy-excel-table-to-word/)
    
*   [How to Copy and Paste Column in Excel?](https://trumpexcel.com/copy-paste-column-excel/)
    
*   [How to Multiply a Column by a Number in Excel](https://trumpexcel.com/multiply-column-by-number-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

31 thoughts on “How to Copy and Paste Formulas in Excel without Changing Cell References”
-----------------------------------------------------------------------------------------

1.  Thank you for your help.  
    “Using Find and Replace” is very good option. it really works.
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-14735)
    
2.  Thank you very much
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-14624)
    
3.  BROOOOOO! This was so smart and easy. Thanks my friend!
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-14429)
    
4.  Excellent. That has made my work today so much easier!!
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-13651)
    
5.  Thanks you so much! This Helped me a lot!!
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-13431)
    
6.  Great! Thanks for the teaching! Loving the Notepad method
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-13424)
    
7.  Amazing….such a nice n easy way to do it with replace..thanks a lot
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-13207)
    
8.  Thanks alot. really helpful
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12947)
    
9.  Nice. Very well explained, thank you.
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12870)
    
10.  OH. MY. GOSH. I’m 10 hours of copying and pasting formulas but this has saved me at least a few more and countless future hours! Replacing = with #, pasting, then replacing # with =. It’s so simple… why didn’t I think of it. 🙂 Thank you!
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12750)
    
11.  Thanks a lot Simple & Eazy
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12594)
    
12.  \# is best and easiest solution, thanks a lot!!! very clever!
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12593)
    
13.  thanks a lot
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12485)
    
14.  This saved me tonnes of work. Thanks so much!
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12417)
    
15.  For a copying and pasting a large array of formulas comprising both relative and absolute references to different cells, sheets and workbooks, the ‘find and replace’ has proven to be convoluted, time consuming and problematic. One has to ‘cherry pick’ through the array to ensure which of one’s relative cell references are not to be changed.  
    I migrated to excel from lotus-123; as a comparison using ‘123’ back then, one would simply ‘highlight rows (or columns)’, ‘copy’, ‘insert’ equal rows (or columns), then ‘paste’ – quick and most importantly no cherry picking errors.  
    Excel’s ‘insert copied cells’ command hides the ‘insert row or column’ command, therefore one cannot emulate the ‘123’ way. Even if one tries the ‘insert sheet rows (or columns)’ command then attempt to paste directly from ‘clipboard’, only text and not formulas are pasted.
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12383)
    
16.  amazing!  
    thanks  
    saved me 20 min. of work…
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12229)
    
17.  THIS IS AWESOME! – THE # = TRICK. GENIUS!  
    THANK U VERY MUCH!
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-11679)
    
    *   Agree! This is so simple, but very helpful. Thanks!
        
        [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-12093)
        
18.  I have a cell reference issue I hope someone can help me with. I have a cell outside of a range that I always want to refer to a specific cell inside of the range, even when cells are inserted or deleted from the range. For example, cell A10 refers to C10 in the range B1:D200. If someone inserts cells B7:D13, I still want A10 to refer to C10, not C17. I think I need a helper column that has the text “C10” in cell E10. What is the Function that gets A10 to use the static text in E10 to refer to cell C10?
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8955)
    
    *   You can use the INDIRECT function. This should work =INDIRECT(“C10”). If you have text C10 in cell E10, just use =INDIRECT(E10)
        
        [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8956)
        
        *   Thanks. That is the Function I was looking for, but could not remember.
            
            [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8958)
            
        *   Even though INDIRECT is less complicated, can you tell me why CELL(“contents”,ADDRESS(10,3)) didn’t work?
            
            [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8959)
            
            *   Jim,  
                although these are functions I’ve never had cause to use, I think this might be because the $C$10 from the ADDRESS function is seen as text, not a cell reference  
                CELL(“contents”,”$C$10″) certainly does not work  
                regards,  
                t’other jim
                
                [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8960)
                
        *   although INDIRECT is the way to go with this, you could also use OFFSET:  
            \=OFFSET(A10,,2) should work  
            both are volatile formulae (will recalculate on every worksheet change), which you might be able to avoid by using =INDEX(C:C,10) which would only fail your requirements if a whole column were inserted or deleted somewhere between A:A and C:C
            
            [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8961)
            
            *   taking this a step further, =INDEX(1:1048576,10,3) will always refer to C10 – but it’s very clumsy-looking
                
                [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8962)
                
    *   I’ve made a step in the right direction. ADDRESS(10,3) results in $C$10 and it does not change when cell C10 is moved. CELL(“contents”,$C$10) gives me the proper result. However, CELL(“contents”,ADDRESS(10,3)) is not even accepted. What is wrong with the nested formula?
        
        [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8957)
        
        *   you should use “=CELL(“contents”, INDIRECT(ADDRESS(10,3,1,1,”Sheet1″),1))” as there are certain arguments to ADDRESS function which ADDRESS(10,3) is not capturing and those arguments are not optional.
            
            [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8963)
            
19.  I think Bansal’s point was that sometimes you can have a range of dynamic formulae that you want to replicate elsewhere  
    I’ve had this situation occur before but I never thought of using the Notepad method – thanks for that, another weapon in my arsenal
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8954)
    
20.  Absolute cell reference is the best. i.e. =A$1$ + B$1$ this cell is locked in that way.
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8953)
    
21.  I use absolute/Dynamic references for doing this
    
    [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-8949)
    
    *   I love method 3. Thanks you.
        
        [Reply](https://trumpexcel.com/copy-paste-formulas-excel/#comment-13269)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/copy-paste-formulas-excel/#respond)

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