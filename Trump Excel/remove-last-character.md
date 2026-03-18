# Remove Last Character in Excel

**Source:** https://trumpexcel.com/remove-last-character

---

[Skip to content](https://trumpexcel.com/remove-last-character/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-last-character/#below-title)

Most of my work involves getting data from various sources, such as databases, webpages, or other people.

In most cases, the first step is to [clean the data](https://trumpexcel.com/clean-data-in-excel/)
 and make it usable for my analysis.

Sometimes, I get datasets that have an additional character in the end that I want to remove. Thanks to some amazing features and formulas in Excel, this is a cakewalk.

In this article, I will show you some easy ways to remove the last character in a cell in Excel.

Remove Last Character in Excel

[Toggle](https://trumpexcel.com/remove-last-character/#)

Using the LEFT Formula to Remove the Last Character
---------------------------------------------------

Let’s start with an easy formula.

Below, I have a dataset where I have some product IDs in column A, and I want to remove the last character, which is a number.

![Dataset to remove last character in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20385'%3E%3C/svg%3E)

To do this, I can use the below formula in column B:

\=LEFT(A2,LEN(A2)-1)

I entered this formula and cell B2 and then copied it for all the other cells in the column.

![Left formula to remove the last character from cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20545%20438'%3E%3C/svg%3E)

The [LEFT function](https://trumpexcel.com/excel-left-function/)
 allows us to extract a specific number of characters from the left.

It takes two arguments:

*   **Text** – This is the first argument that refers to the cell from which we want to extract the characters from the left. In our example, I’ve given A2 as the cell reference.
*   **Num\_Chars** – this is the number of characters I want to extract from the left from the [given cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
    . In our example, since the overall length of the string in each cell varies, I have used the [LEN function](https://trumpexcel.com/excel-len-function/)
     first to calculate the length of the string in each cell and then subtract 1 from it to give us the number of characters that should be extracted from the left.

Once you have the result, you can [remove the formula and keep the data](https://trumpexcel.com/remove-formulas-keep-data-excel/)
 (by copying the cells and pasting it over itself as values)

Also read: [Remove Characters From Left in Excel](https://trumpexcel.com/remove-characters-from-left-excel/)

Flash Fill To Remove Last Character in Excel
--------------------------------------------

Another quick and easy way to do this is by using the [Flash Fill feature in Excel](https://trumpexcel.com/flash-fill-excel/)
.

To use Flash Fill, you need to give it one or two instances of the result that you want. It then analyzes these results, identifies the pattern, and then repeats the same to give you the result for all the other cells in the column.

Let me show you how it works.

Below, I have a dataset where I have some product IDs in column A, and I want to remove the last character, which is a number.

![Dataset to remove last character in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20385'%3E%3C/svg%3E)

Here are the steps to do this using Flash Fill:

1.  In cell B2, enter the result you want. In this example, I will manually enter AUT.

![Enter the expected result in the first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20388'%3E%3C/svg%3E)

2.  Hit the Enter key. This will bring the cursor to the cell below.
3.  Hold the Control key and press the E key. This is the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     to run Flash Fill. You can also run Flash Fill by going to the Home tab, then clicking on the Fill icon, and then clicking on the Flash Fill option.

As soon as you run Flash Fill, it tries to identify the pattern based on the manual entry unit in cell B2 and gives you the result based on this pattern in all the other cells in the column.

![Flash fill fails the entire column with the result after removing the last character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20386'%3E%3C/svg%3E)

While Flash Fill Worked as expected in our case, you should always double-check the results of Flash Fill as it can sometimes get the pattern wrong. If that happens, you can manually enter the results in two or three cells and then use Flash Fill so it would have more results to get the pattern right.

Also read: [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)

VBA to Remove Last Character
----------------------------

If your work involves removing the last character from a range of cells frequently, you can also consider using a VBA code to do this.

While setting up the VBA code may involve a couple of additional steps, once you are done setting it up, you can reuse the VBA code again and again in the file in which it is stored.

Below is the VBA code that would remove the last character from all the cells in the selected range

    Sub RemoveLastCharacter()
    
        Dim rng As Range
        Dim cell As Range
    
        Set rng = Selection
    
        For Each cell In rng
            If Len(cell.Value) > 0 Then
                cell.Value = Left(cell.Value, Len(cell.Value) - 1)
            End If
        Next cell
    
    End Sub

This above VBA code [loops through each cell](https://trumpexcel.com/vba-loops/)
 in the selected range and uses the LEFT function to return the string without the last character.

Here are the steps to put the VBA code in Excel:

1.  Hold the Alt key and then press the F11 key. This will open the VB editor for your Excel workbook. If you’re using a Mac, you can use _Opt + F11_.
2.  In the VB Editor, click on the Insert option and then click on Module. This will insert a new module for the workbook.

![Insert a new module for the workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20269%20215'%3E%3C/svg%3E)

3.  Copy and paste the above VBA macro code into the module code window.

![Copy and paste the vba code to remove last character in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20291'%3E%3C/svg%3E)

4.  Click on the Save button and close the VB Editor. It may ask you to save the file as a .XLSM (macro-enabled) file (as you can not store macros in an XLSX file)

![save the VBA code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20418%20161'%3E%3C/svg%3E)

The above steps would put the VBA code in your workbook, and now you can use the steps below to run the macro code:

1.  Select the cells from which you want to remove the last character.
2.  Click on the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on the Macros icon. This will open the Macro dialog box.

![Click on the macros icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20173'%3E%3C/svg%3E)

3.  Select the Macro from the list (our macro is called _RemoveLastCharacter_)

![Select the macro from the list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)

4.  Click on the Run button.

![Click on the run button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)

As soon as you click on the run button, it will execute the macro in the back end, and the last character from each cell in the selected range will be removed.

Keep in mind that the result you get after running a VBA code is irreversible, and the changes cannot be undone. So I strongly recommend you create a backup copy of your dataset before running any VB macro script.

If you want to reuse this VB macro code in all the workbooks on your system, you can save this in your Personal macro workbook (follow the steps shown here to activate and use the Personal Macro workbook)

So these are three simple ways you can use to quickly remove the last character from a cell or selected range of cells in Excel.

I hope you found this article helpful. If you know of any other method to remove the last character or if you have any feedback or suggestions for me, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [Remove the First Character from a String in Excel](https://trumpexcel.com/remove-first-character-from-string/)
    
*   [Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [Find Position of the Last Occurrence of a Character in a String in Excel](https://trumpexcel.com/find-characters-last-position/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-last-character/#respond)

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