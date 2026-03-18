# Remove Formulas (but Keep Data) in Excel

**Source:** https://trumpexcel.com/remove-formulas-keep-data-excel

---

[Skip to content](https://trumpexcel.com/remove-formulas-keep-data-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-formulas-keep-data-excel/#below-title)

Once you’re done using formulas to get the desired results, you may want to remove the formulas and keep the data you got as a result of these formulas.

This is often done to remove formulas you no longer need and save processing power (as formulas recalculate every time you make a change in the worksheet).

Another scenario could be when you’re sending your spreadsheet to someone else and want to avoid confusion or protect your formulas from being accidentally changed.

In this article, I will show you some simple ways to remove the formulas but keep the data in Excel. You can do this easily using some keyboard shortcuts, the built-in Paste Special options, or even VBA.

So, let’s dive right into it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-formulas-keep-data-excel/#)

Using Keyboard Shortcuts
------------------------

The fastest and easiest way to remove formulas and convert the result of these formulas to values is by using [keyboard shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
.

In this section, we’ll discuss two key keyboard shortcuts for removing formulas and keeping the data in Excel.

### \[New Shortcut\] Control + Shift + V

If you’re using Excel for Microsoft 365 or Excel for Web, you can use this new shortcut.

This shortcut was released in October 2022 and is only made available for versions/builds of Excel for Microsoft 365 after October 2022. All Excel for Microsoft 365 users will get access to it, but the older versions of Excel won’t have this.

Below, I have an example dataset where I have the formula to calculate the commission of each sales rep in column D, and I want to remove the formulas but keep the values.

![Dataset that has the formula we want to remove](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20387'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the cell range containing the formulas you wish to remove. In this case, I would select D2:D11
2.  Press Control + C to copy the selected cells.
3.  Keep the same range selected and then use the below shortcut

**Control + Shift + V**

You need to hold the Control and the Shift key and then press the V key.

The above keyboard shortcut is meant to paste the copied data as plain text values in Excel.

You can also use this to copy data from any source, such as a web page or other Office applications such as MS Word or PowerPoint, and paste this into Excel as values without any formatting or formulas.

Note: [According to the release notes](https://insider.microsoft365.com/en-us/blog/new-paste-options-when-using-keyboard-shortcuts)
 by Microsoft, this function is available for Excel for Microsoft 365 and would also be released for Excel for Mac as well.

**Fun Fact**: This shortcut has been available in Google Sheets for many years, and many Excel fans, including myself, have been asking Microsoft to have this for Excel. Glad it happened now.

### Shortcut for All Versions

If you’re using an [older version of Excel](https://trumpexcel.com/excel-version/)
 and the Control + Shift + V shortcut doesn’t work for you, below is the shortcut that would work in any Excel version.

ALT + E + S + V + Enter

To use this shortcut:

1.  Select the cell range with the formulas you want to remove.
2.  Press Control + C to copy the cells.
3.  With the range still selected, press **ALT + E + S** (one key after the other) to open the Paste Special dialog box.

![Paste special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20499%20378'%3E%3C/svg%3E)

4.  Press the **V key** to select the Values option.

![Select the values option in the paste special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20499%20378'%3E%3C/svg%3E)

5.  **Hit Enter** to confirm and paste the values, effectively removing the formulas.

This shortcut uses the built-in paste special option to paste the copied cells as Values.

So, if the cells you selected have formulas, this shortcut would remove the formula but keep the data.

By using either of these keyboard shortcuts, you’ll be able to remove formulas in Excel while retaining the values/data.

Also read: [Excel Paste Special Shortcuts](https://trumpexcel.com/excel-paste-special-shortcuts/)

Using Paste Special Option
--------------------------

If you’re not a fan of learning new keyboard shortcuts or do not have access to the Control + Shift + V shortcut, there are still some easy ways to get rid of the formulas while keeping the data.

### Paste Special Dialog Box

Below, I have a data set where I have a formula in column D, and I want to remove the formula while keeping the result of the formula as values.

![Dataset that has the formula we want to remove](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20387'%3E%3C/svg%3E)

Here are the steps to do this using the Paste Special dialog box:

1.  Select the range that has the formulas that you want to remove.
2.  Copy the range. You can do this by right-clicking on the range and then selecting the Copy option, or use the shortcut Control + C

![Copy the column that has the formulas you want to remove](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20746%20525'%3E%3C/svg%3E)

3.  With the same range selected, right-click and then and then click on the Paste Special option. This will open the Paste Special dialog box.

![Click on paste special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20740%20432'%3E%3C/svg%3E)

4.  Select the Values option.

![Select the values option in the paste special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20499%20378'%3E%3C/svg%3E)

5.  Click Ok

The above steps would paste the copied cells on the selected range, but since we have selected the Value options in step 4, it will only paste the values.

Since the cells we selected initially had formulas, and then we pasted values over them, it resulted in the formulas getting removed while the values remained (as static values).

Also read: [How to Multiply a Column by a Number in Excel](https://trumpexcel.com/multiply-column-by-number-in-excel/)

### Paste Special Option in Ribbon

Another way to remove formulas and only retain the values is by using the paste as values option in the right-click menu.

Let’s use the below dataset, where I have a formula in column D, and I want to remove the formula and keep the values.

![Dataset that has the formula we want to remove](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20387'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the range that has the formulas that you want to remove.
2.  Copy the range. You can do this by right-clicking on the range and then selecting the Copy option, or use the shortcut Control + C
3.  Now click the Home tab.
4.  In the Clipboard group, click on the small arrow icon below the Paste option.

![Click on the paste option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20223'%3E%3C/svg%3E)

5.  Select the Paste Values option.

![Click on the paste as values icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20557'%3E%3C/svg%3E)

The above steps would paste the copied data as values on the selected range of cells, which in our example means that the formulas would be removed with static values.

Also read: [How to Remove Conditional Formatting in Excel](https://trumpexcel.com/remove-conditional-formatting-excel/)

Cursor Wiggle Trick
-------------------

This is a really cool trick that not many people know and would make you look like an Excel magician.

While this method does not have any advantage over the previous methods, it does make you look cool.

Below is a data set where I have formulas in column D that I want to remove and only keep the result of the formulas.

![Dataset that has the formula we want to remove](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20387'%3E%3C/svg%3E)

Here are the ways to use this cursor wiggle trick:

1.  Select the cells that have the formula that you want to remove
2.  Place your mouse cursor at the right edge of the selection. You will notice that your cursor changes into a four-arrow icon (as shown below)

![Cursor changes into four arrow pointed icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20346'%3E%3C/svg%3E)

3.  Hold the left mouse key (keep holding it), then move the cursor a little to the right. You will see the green outline appear in the adjacent column on the right.

![drag the cursor to the right](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20341'%3E%3C/svg%3E)

4.  Keep holding the left mouse key and bring the cursor back to where you already have the data.

![Bring the cursor back to the original column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20343'%3E%3C/svg%3E)

5.  Leave the mouse key. As soon as you do this, you will see a menu appear with some options.

![Additional options in the right click menu shows up](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20725%20485'%3E%3C/svg%3E)

6.  Select the ‘Copy Here as Values Only’ option.

![Click on copy here as values only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20725%20485'%3E%3C/svg%3E)

As soon as you click on the ‘Copy Here as Values Only’ option in step 6, the formula will be removed, and you will only have the data in the cell as static values.

Note: Personally, I find this method faster than using the built-in Paste Special options

Also read: [How to Convert Formulas to Values in Excel](https://trumpexcel.com/convert-formulas-to-values-excel/)

Using VBA
---------

If removing formulas and converting these into their resulting value is something you need to do quite often, or you need to do it for multiple worksheets in one workbook or multiple workbooks, you can consider using VBA.

Below are some of the VBA codes you can use in different scenarios:

### Removing Formulas from a Specific Range

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub RemoveFormulasInRange()
        Dim rng As Range
        Set rng = ActiveSheet.Range("D2:D11")
        rng.Value = rng.Value
    End Sub

In the above code, I have specified the range as D2:D11. You can change the range according to your needs.

### Removing Formulas from the Entire Worksheet

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub RemoveFormulasButKeepData()
        Dim ws As Worksheet
        Set ws = ActiveSheet
        ws.UsedRange.Value = ws.UsedRange.Value
    End Sub

The above code removes formulas from all cells in the “used range” of the active worksheet and replaces them with their calculated values.

### Removing Formulas from all Sheets in the Workbook

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub RemoveFormulasButKeepData()
        Dim ws As Worksheet
    For Each ws In ThisWorkbook.Worksheets
        ws.UsedRange.Value = ws.UsedRange.Value
    Next ws
    End Sub

The above code uses a [For Each loop](https://trumpexcel.com/vba-loops/)
 to go through each worksheet in the active workbook and then replace the used range with the values in the cells. This ends up removing all the formulas while keeping the data intact.

### Where to Put this VBA Code

Follow the steps below to open the VB Editor, place the VBA code, and run it:

1.  Go to the [Developer tab in the Ribbon](https://trumpexcel.com/excel-developer-tab/)
    . If you don’t see a Developer tab, you’ll need to enable it. In the Developer tab, click on the “Visual Basic” icon. Alternatively, you can press **ALT + F11** to open the VBA editor.

![Click on the visual basic icon in the developer tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20721%20195'%3E%3C/svg%3E)

2.  In the VBA editor, click on the Insert option in the menu and then click on Module. This will insert a new module into your VBA project.

![Insert a new module for the workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20353%20247'%3E%3C/svg%3E)

3.  Copy the VBA code you want to use in the new module code window that appears in the editor.

![Copy and paste the vba code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20221'%3E%3C/svg%3E)

4.  Save the VBA module by clicking the save icon or pressing Ctrl + S.
5.  Close the VBA Editor

To Run the macro code, follow the below steps:

1.  Hold the ALT key and press the F8 key. This will open the Macro dialog box.
2.  Select the Macro you want to run and click on the Run button.

![Select the macro and click on the run button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20552%20470'%3E%3C/svg%3E)

**Caveat**: Remember that the changes done by a VBA code are irreversible. So make sure that you have a backup copy of your data just in case anything goes wrong with the VBA code or you need the original data sometime later.

If you want to reuse the VBA code, you will have to save your file as a macro-enabled Excel file (with a .XLSM extension).

**Pro Tip**: If you want to use any of these VBA codes in all the Excel workbooks on your system, you should save the code in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. Once the code is in the Personal Macro Workbook, it can be used on any workbook using the steps I mentioned above.

So, these are some methods you can use to remove the formulas but keep the data in Excel. If this is something you need to do quite often, it would be best to learn the keyboard shortcuts to do this.

Or else, you can use the built-in Paste Special option to get rid of the formula and replace it with its value.

I hope you found this Excel tutorial useful.

**Other Excel articles you may also like:**

*   [Highlight Cells With Formulas in Excel](https://trumpexcel.com/highlight-cells-with-formulas-excel/)
    
*   [How to Hide Formulas in Excel (and Only Display the Value)](https://trumpexcel.com/hide-formulas-excel/)
    
*   [Formula vs Function in Excel – What’s the Difference?](https://trumpexcel.com/formula-vs-function-excel/)
    
*   [Excel Formulas Not Working](https://trumpexcel.com/excel-formulas-not-working/)
    
*   [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    
*   [Excel Showing Formula Instead of Result](https://trumpexcel.com/excel-showing-formula-instead-of-result/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-formulas-keep-data-excel/#respond)

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