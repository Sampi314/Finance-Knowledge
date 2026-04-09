# How to Merge Cells in Excel Without Losing Data (Step-by-Step)

**Source:** https://trumpexcel.com/how-to-merge-cells-in-excel

---

[Skip to content](https://trumpexcel.com/how-to-merge-cells-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/how-to-merge-cells-in-excel/#below-title)

There are various ways you can merge cells in Excel.

One of the most used ways is using the _Merge & Center_ option in the Home tab.

![How to Merge Cells in Excel - Merge and Center Icon](https://trumpexcel.com/wp-content/uploads/2015/10/How-to-Merge-Cells-in-Excel-Merge-and-Center-Icon.png)

The issue with using _Merge & Center_ is that it can merge the cells, but not the text within these cells (i.e., you lose some data when you merge the cells).

Let’s say we have a data set as shown below:

![How to Merge Cells in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20240%20147'%3E%3C/svg%3E)

If I select cell A1 and B1 and use the Merge & Center option, it will keep the text from the left-most cell (A1 in this case) and but you will lose the data from all other cells.

Excel is not completely ruthless though – it warns you before this happens.

If you try and merge cells which have text in it, it shows a warning pop-up letting you know of this (as shown below).

![How to Merge Cells in Excel - Pop Up Message](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20892%20476'%3E%3C/svg%3E)

If you go ahead and press OK, it will merge the two cells and keep the text from the leftmost cell only. In the above example, it will merge A1 and B1 and will show the text John only.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/how-to-merge-cells-in-excel/#)

Merge Cells in Excel Without Losing the Data
--------------------------------------------

If you don’t want to lose the text in from cells getting merged, use the [CONCATENATE](https://trumpexcel.com/excel-concatenate-function/)
 formula. For example, in the above case, enter the following formula in cell C1: \=CONCATENATE(A1,” “,B1)

Here we are combining the cells A1 and B1 and have a space character as the separator. If you don’t want any separator, you can simply leave it out and use the formula \=CONCATENATE(A1,B1).

Alternatively, you can use any other separator such as comma or semi-colon.

This result of the CONCATENATE function is in a different cell (in C1). So you may want to copy it (as values) in the cell which you wanted to merge.

You can also use the ampersand sign to combine text. For example, you can also use \=A1&” “&B1

The Benefit of Not Merging Cells in Excel
-----------------------------------------

When you use Merge & Center option to merge cells, it robs you of the ability to [sort that data set](https://trumpexcel.com/sort-excel/)
.

If you try and sort a data set that has any merged cells, it will show you a pop-up as shown below:

![How to Merge Cells in Excel - Sort Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20159'%3E%3C/svg%3E)

Also read: [Find Merged Cells in Excel](https://trumpexcel.com/find-merged-cells/)

Alternative to Using Merge & Center
-----------------------------------

If you want to merge cells in different columns in a single row, here is an alternative of _Merge & Center_ – the _Center Across Selection_ option.

Here is how to use it:

*   Select the cells that you want to merge.
*   Press Control + 1 to open the format cells dialogue box.
*   In the Alignment tab, in the Horizontal drop-down, select Center Across Selection.

![How to Merge Cells in Excel - Center across selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20361'%3E%3C/svg%3E)

*   Click OK.

This would merge the cells in a way that whatever you enter in the leftmost cell gets centered.

However, you can still select each cell individually. This also does not show an error when you try and sort the data.

_NOTE: For Center to Across to work, make sure only the leftmost cell has data._

**You May Also Like the Following Excel Tutorials:**

*   [How to Unmerge Cells in Excel (3 Easy Ways + Shortcut)](https://trumpexcel.com/unmerge-cells-excel/)
    
*   [CONCATENATE Excel Range (with and without separator)](https://trumpexcel.com/concatenate-excel-ranges/)
    .
*   [How to Find Merged Cells in Excel](https://trumpexcel.com/find-merged-cells/)
    .
*   [How to Combine Cells in Excel](https://trumpexcel.com/combine-cells-in-excel/)
    .
*   [How to Combine Multiple Workbooks into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)
    .
*   [How to Write Text Vertically in Excel](https://trumpexcel.com/write-vertically-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

18 thoughts on “How to Merge Cells in Excel Without Losing Data”
----------------------------------------------------------------

1.  Great jobs sir
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-14191)
    
2.  Hi, I am trying to merge two cells (a4 & a5) into another worksheet and for the formula to copy down (i.e. cell a1 has merged a4/a5, a2 has merged b4/b5, a3 has merged c4/d4 etch
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-12259)
    
3.  I AM TRYING TO MERGE AREA CODES FROM ONE COLUMN AND PHONE NUMBER IN ANOTHER AND THEN BE ABLE TO DELETE THE TWO COLUMNS I DONT NEED ! HOW DO I SAVE TH INFORMATION IN CELL 3?
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-10467)
    
    *   Copy merged information from the third column, paste special as values into the 4th column. Now you can delete columns 1,2 and 3.
        
        [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-12647)
        
4.  I’m a beginner in Concatenate formula. I need a help to make a line break or change line when concatenate the two cells. Like put the content of the cells not to side by side, but above/under inside the same cell. There is a way to do that?
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-3475)
    
    *   yeah, add a carriage return character, which would look like this:  
        \=CONCATENATE(cellref1,CHAR(10),cellref2)  
        or  
        \=cellref1&CHAR(10)&cellref2
        
        [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-3610)
        
5.  This is just brilliant! Too good! Going to use this everyday now!
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2571)
    
    *   Thanks for commenting Rushabh.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2576)
        
6.  hi Sumit,
    
    what is this “video like” screenshot called and also how to make it?  
    Regards Rudra
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2568)
    
    *   Hello Rudra.. Its a GIF image.. I use Camtasia to make it
        
        [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2575)
        
7.  The Center Across Selection button/icon can be directly added to the QAT.  
    QAT – (click drop down) select More Commands – Choose Commands from: All Commands – scroll to Center (Not Merge) Across Selection. Select and add to your QAT.
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2565)
    
    *   Thanks for dropping by and commenting.. The Center Icon from the list would centre the content in the cells but would not Center Across Selection. Unfortunately, there is no option in that list that can do that. The only way is to create a macro and add it in QAT.
        
        [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2566)
        
        *   Excel 2010 (ver 14.0, 64 bit). In my Customize QAT, there is Center (that you refer to) and right below it, I have “Center (Not Merge) Across Selection”. It does exactly that.
            
            [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2569)
            
8.  What if I would like to merge cells in different rows in a single column?
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2564)
    
    *   Thanks for commenting Izabela.. In case of rows, there is no other way. You need to use Merge & Center. The drawback is that it will keep the content of the top cell only.
        
        [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2567)
        
        *   Thank you! I love your articles! They are so useful!
            
            [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2572)
            
9.  Good post. Thanks for sharing. I use ‘Center Across selection’ sometimes. I wish that it was easier to apply it without having to go through format dialog box. 🙂
    
    [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2548)
    
    *   I wish the same. The only option I can think of is to write a macro and have it in the QAT.
        
        [Reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#comment-2555)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/how-to-merge-cells-in-excel/#respond)

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