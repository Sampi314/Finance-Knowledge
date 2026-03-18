# How to Filter Strikethrough in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/filter-strikethrough-excel

---

[Skip to content](https://trumpexcel.com/filter-strikethrough-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/filter-strikethrough-excel/#below-title)

Recently I was working on a project where I had to filter all the cells that had strikethrough formatting applied to it.

The issue is…

There is no built-in way to filter cells that have strikethrough applied to them.

So we need in a workaround.

In this article, I will cover two simple ways you can use to filter cells with strikethrough in Excel (one using Find & Replace and one using VBA).

So let’s dive in!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/filter-strikethrough-excel/#)

Filter Strikethrough Using Find & Replace
-----------------------------------------

With [Find & Replace](https://trumpexcel.com/find-and-replace-in-excel/)
, we can find and then give a color to all the cells with strikethrough format.

Once this is done, we can [filter these cells based on the cell color](https://trumpexcel.com/filter-by-color-excel/)
 (which is a built-in filter in Excel).

Below I have a data set where I have some cells in column A that have the [strikethrough format](https://trumpexcel.com/strikethrough-in-excel-shortcut/)
 applied to it and I want to filter them.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20336'%3E%3C/svg%3E)

Here are the steps to filter strikethrough cells:

1.  Select all cells in column A.
2.  Hold the Control key and then press the F key. This will open the Find and Replace dialog box. Alternatively, you can also click on the Home tab, then click on the Find & Select icon in the Editing group and then click on the Find option.
3.  In the Find and Replace dialog box, click on the _Options_ button. Doing this will show you some additional options

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

4.  Click on the _Format_ button. This will open the _Find Format_ dialog box

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

5.  Go to the _Font_ tab and check the _Strikethrough_ option (listed in the Effect options).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20673'%3E%3C/svg%3E)

6.  Click OK.
7.  Click on _Find All_. Doing this will find all the cells that have the strikethrough format applied to it and show you the list of all these cells below the Find and Replace dialog box. At this point, Excel has only selected the first cell where it found the strikethrough format.

![Click on the Find All button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

8.  Now hold the Control key and press the A key. This will select all the cells that has been found with the strikethrough format.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20437'%3E%3C/svg%3E)

9.  Close the Find and Replace dialog box.
10.  Go to the Home tab and then give a _[fill color](https://trumpexcel.com/shortcuts-fill-color-excel/)
    _ to all these selected cells. In this example I’ll go with the blue color.

![Choose the color to fill the cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20675%20626'%3E%3C/svg%3E)

11.  Select and right-click on any one of the selected cells, go to the [Filter option](https://trumpexcel.com/excel-data-filter/)
    , and then click on _Filter by Selected Cell’s Color_

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20760%20597'%3E%3C/svg%3E)

And that’s will do it!

Now you’ll only see the cells that had strikethrough formatting.

So while there is no direct option in Excel to filter strike through cells we first found them using Find and Replace and then give them a color.

This allowed us to use the built-in filter by color option in Excel, that enables us to also filter all the cells with Strikethrough.

**Note**: The color you apply will overwrite any existing cell colors. So if your data already uses cell colors for other purposes, this method might interfere with that formatting. Also, this method is temporary – if you later add more strikethrough text, you’ll need to repeat the process to update the filtered view.

Also read: [Filter Cells with Bold Font Formatting in Excel](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)

Filter Strikethrough Using VBA
------------------------------

You can also filter strikethough cells by creating your own custom function with VBA.

This function can then be used in a helper column and it would return TRUE if the referenced cell has strikethrough format applied, and FALSE and if not. Once you have this, you can filter the hypercolumn thereby also filtering the cells with strike through format.

Let me show you how to do this.

Below I have a data set where I have some cells in column A that have the strikethrough format applied to it and I want to filter them.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20336'%3E%3C/svg%3E)

Here are steps to use VBA to filter strikethrough cells:

1.  Go to the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and click on _Visual Basic_ (or press _Alt + F11_)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20905%20222'%3E%3C/svg%3E)

2.  In the VB Editor that opens, click on the _Insert_ option and then click on _Module_. This will insert a new Module for your workbook.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20433%20290'%3E%3C/svg%3E)

3.  Copy the below VBA code into the module code window

    Function CheckSR(rng As Range)
    CheckSR = rng.Font.Strikethrough
    End Function

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20689%20341'%3E%3C/svg%3E)

The above steps creates the UDF ([User Defined Function](https://trumpexcel.com/user-defined-function-vba/)
) that you can now as a regular worksheet function.

4.  Add a helper column next to your data. Let’s name this column as Helper (enter the text in the top most cell).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20528%20337'%3E%3C/svg%3E)

5.  Enter the formula =CheckSR(A2) in cell C2 in the helper column. The function will return TRUE for cells with strikethrough and FALSE for those without. Copy this formula down for all the cells in the column

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20385'%3E%3C/svg%3E)

6.  Apply a filter to your dataset. To do this, select any cell in the dataset and then use the keyboar shortcut **Ctrl + Shift + L** (or click on the _Data_ tab and then click on the _Filter_ icon)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20223'%3E%3C/svg%3E)

7.  Filter the helper column to show only TRUE values

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20196'%3E%3C/svg%3E)

This will show you all rows where the cells have strikethrough formatting applied.

Note: If you want to save this code in your Excel file so that it can be reused again you need to save your file with .XLSM extenstion

Both methods work great – the Find & Replace method is quick and doesn’t require VBA, while the VBA method gives you a reusable function you can use anytime you need to check for strikethrough formatting.

I hope you found this article helpful.

If you have any questions or suggestions, kindly leave them in the comments below.

**Other Excel articles you may also like:**

*   [Dynamic Excel Filter Search Box – Extract Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    
*   [Excel Advanced Filter](https://trumpexcel.com/excel-advanced-filter/)
    
*   [Excel Filter Function](https://trumpexcel.com/filter-function/)
    
*   [Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/filter-strikethrough-excel/#respond)

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