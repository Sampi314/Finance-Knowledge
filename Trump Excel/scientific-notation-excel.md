# How to Write Scientific Notation in Excel? 4 Simple Ways!

**Source:** https://trumpexcel.com/scientific-notation-excel

---

[Skip to content](https://trumpexcel.com/scientific-notation-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/scientific-notation-excel/#below-title)

Scientific notation is a format that allows us to write very large or very small numbers in a consistent decimal format.

This can be useful when you are working with large numbers and you do not want them to take up a lot of space in your Excel worksheet.

In such a case, you can convert the format of that number so that it is shown in the scientific notation.

In this article, I am going to show you some methods you can use to write scientific notation in Excel. I will also show you how you can format the numbers in an Excel chart to show them in scientific notation and save space.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/scientific-notation-excel/#)

What is Scientific Notation?
----------------------------

As I mentioned, scientific notation allows us to write very large or very small numbers in a decimal format, which is compact and more manageable.

It’s a commonly used number format when working with engineering, chemistry, financial, or mathematics data.

Suppose you have a number 12485769 and you want to show it in scientific format, then it could be written as

1.2485769 x 10^7

or

1.25 x 10^7

When working with Excel, the format becomes **1.25E+07**, where E+07 is equivalent to multiplying the preceding value with 10^7

Similarly, a small number such as 0.000321 can be changed to **3.21E-04** in Excel.

Below, I have examples where the numbers in column A are shown as scientific notation in column B. Note that both of these columns have the exact same numbers (it’s just the format that has been changed)

![Decimal notation and scientific notation in Excel in table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20538%20223'%3E%3C/svg%3E)

In the following few sections, I will show you multiple methods you can use to write scientific notation in Excel. This can quickly be done by changing the format of the cell so that the numbers are shown in scientific notation or using the [TEXT function](https://trumpexcel.com/excel-text-function/)
. I will also cover how to do this using VBA.

**Fun fact**: If you enter a number longer than 11 digits in a cell in Excel, it will automatically be converted into the scientific notation format. However, this does not happen in Google Sheets.

Also read: [Convert Scientific Notation to Number in Excel](https://trumpexcel.com/convert-scientific-notation-to-number-text/)

Converting Number of Scientific Notations by Changing Cell Format
-----------------------------------------------------------------

The easiest way to change a number into a scientific notation in Excel is by changing the format of the cell.

You can either use the readily available scientific notation format in the ribbon in Excel, or you can use the Format Cells dialog box that gives you a little more control over how the format should be designed.

### Using Format Drop Down in Ribbon

Below, I have a data set where I have the distance from Earth to different celestial bodies in miles in column C. I want to show the values in column C in scientific notation.

![Dataset with numbers that needs to be converted into scientific notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20250'%3E%3C/svg%3E)

Here are the steps to convert these numbers to scientific notation:

1.  Select the cells that have the numbers that you want to convert into scientific notation
2.  Click the Home tab in the ribbon

![Click on the home tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20223'%3E%3C/svg%3E)

3.  In the Number group, click on the **Number** Format drop-down
4.  Select the **Scientific** option from the drop-down

![Select the scientific format from the number format dropdown](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20458%20753'%3E%3C/svg%3E)

The above steps would change the format of the cells so that the numbers are now shown in the scientific notation format.

![Numbers converted into scientific format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20253'%3E%3C/svg%3E)

**Note**: As I’ve already mentioned, this only changes how the numbers are shown to you in the cell. It does not change the actual value in the cell. You can confirm this by selecting any of the cells, and you will see the actual value in the [Formula Bar](https://trumpexcel.com/show-hide-formula-bar-excel/)
.

This method would always give you the same format for the scientific notation – 0.00E+00 (such as in 3.84E+05), i.e., one digit before the decimal and two digits after the decimal, followed by E

If you want to decide how many digits after the decimal place should be shown, then you’ll have to use the next method that uses the ‘Format Cells’ dialog box.

### Using Format Cells Dialog Box

Below, I have the same data set where I have numbers in column C that I want to get in scientific format.

![Dataset with numbers that needs to be converted into scientific notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20250'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the cells with the numbers that you want to change into scientific notation
2.  Hold the Control key and then press the 1 key. Alternatively, you can right-click on the selected range of cells and then click on the ‘Format Cells’ option.

![Click on the format cells option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20580%20700'%3E%3C/svg%3E)

3.  In the Format Cells dialog box that opens, select the **Number** tab, and then click on the ‘**Scientific**‘ option.

![Select the Scientific option in the Format cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

4.  Specify the number of decimal places you want before the E in the scientific notation.

![Specify the decimal places you want in the scientific format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20557'%3E%3C/svg%3E)

5.  Click OK

The above steps would change the format of the cells and show the numbers in scientific notation.

![Numbers converted into scientific format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20253'%3E%3C/svg%3E)

**Note**: In case you need even more control over how the scientific notation should be shown, you can create your own format by clicking on the ‘Custom’ option in the Format cells dialog box.

Also read: [How to Write Fractions in Excel](https://trumpexcel.com/display-numbers-as-fractions-excel/)

### Shortcut to Get Scientific Notation in Excel (Windows and Mac)

If you need to use scientific notation format in Excel frequently, it would be good to learn the shortcut to do that.

Below is the shortcut to do scientific notation in Excel:

**Control + Shift + ^**

This shortcut would work in Windows as well as Mac.

To use this shortcut, first select the cells that have the numbers that you want to convert to scientific notation, then hold the Control and the Shift key together, and then press the ^ key.

**Bonus Tip**: This shortcut also works in Google Sheets

Using TEXT Function to Converting Number of Scientific Notations
----------------------------------------------------------------

Another method to convert numbers into scientific notation is by using the TEXT function, where you can specify the format in which you want to show the numbers.

Below, I have the same data set where I have numbers in column C that I want to write in scientific notation:

![Dataset with numbers that needs to be converted into scientific notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20250'%3E%3C/svg%3E)

Below is the TEXT formula we can use to change these numbers into scientific format:

\=TEXT(C2,"0.00E+00") 

Enter this formula in cell D2 and copy it for all the other cells in the column.

![TEXT function to get scientific notation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20298'%3E%3C/svg%3E)

The above TEXT formula takes two arguments:

*   The reference of the cell that has the number
*   The format in which you want to show that number (which is 0.00E+00 in our example). Ensure that the format is always in double quotes.

One major difference between using the TEXT function method and changing the cell format method (covered earlier) is that with the TEXT function method, the **output you get is a text string**.

This means that you won’t be able to use scientific notation as a number in other numeric calculations.

**Note**: In case you want to remove/delete the original data set, you’ll first have to [convert the formula into static values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 before deleting the original data set

Manually Enter Scientific Notation in Excel
-------------------------------------------

If you only want to enter scientific notation values in a couple of cells, you can also do this manually.

Just enter the number in the below format:

0.00E+00

Here, instead of zero, you need to use the actual digits in your number (such as 4.87E+07)

When you enter this scientific notation in a cell, Excel recognizes that you want this to be shown as the scientific notation but have the actual number in the back end.

So when I enter 4.87E+07 in a cell, while it shows me what I entered, the actual value in the cell would be 48700000.

**Note**: One obvious drawback of this method is that it is manual, so it’s best suited in situations where you want to enter the scientific notations in a few cells only

Using VBA to Write Scientific Notations in Excel
------------------------------------------------

VBA is another way you can use to quickly convert numbers in cells into scientific notation:

Below is the VBA code to do this:

    'Code from https://trumpexcel.com
    Sub ConvertToScientificNotation()
    
        Dim cell As Range
        Dim selectedRange As Range
        
        'Prompt the user to select a range
        On Error Resume Next
        Set selectedRange = Application.InputBox("Select a range", Type:=8)
        On Error GoTo 0
        
        'Check if the user canceled or didn't select a range
        If selectedRange Is Nothing Then
            MsgBox "Canceled or invalid range selected"
            Exit Sub
        End If
        
        'Loop through each cell in the range sleected by the user
        For Each cell In selectedRange
            ' Change the format to scientific notation
            cell.NumberFormat = "0.00E+00"
        Next cell
    
    End Sub

When you run the above VBA code, it is going to ask the user to select the range of cells that has the numbers, and then format the cells to show these numbers in scientific notation.

Here are the steps on where to put this VBA code and how to use it:

1.  Hold the ALT key and then press the F11 key. This will open the VB Editor, where we will be putting this code. Alternatively, you can also click on the ‘[Developer tab](https://trumpexcel.com/excel-developer-tab/)
    ‘ and then click on the Visual Basic icon to open the VB editor
2.  Click on the Insert option in the menu
3.  Click on Module. This will insert a new module

![Insert a new module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20304'%3E%3C/svg%3E)

4.  Copy and Paste the above VBA code in the module code window.

![Copy paste the code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20381'%3E%3C/svg%3E)

5.  To [run the VBA macro code](https://trumpexcel.com/run-a-macro-excel/)
    , place the cursor anywhere within the code and then hit the F5 key on your keyboard. Alternatively, you can also click on the Run Sub/Userform icon in the toolbar.

![Run the VBA code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20129'%3E%3C/svg%3E)

As soon as you run the above VBA code, it is going to open an Input box where you can select the range and then click on the ok button.

So, these are some of the methods you can use to write scientific notation in Excel.

If you want to do this for a couple of cells, you can manually write the scientific notation, and if you already have a set of numbers that you want to convert into scientific notation, then you can use the formatting methods covered in this article.

Frequently Asked Questions about Scientific Notation in Excel
-------------------------------------------------------------

In this section, I have answered some common questions people usually have about working with scientific notation in Excel.

### Can you have Scientific Notation Without E in Excel?

I don’t think this can be done. Scientific notation in Excel only works when an E is added to it (where the E+ works like 10^). For example, 1.25 x 10^7 is written as 1.25E+07 in Excel.

I tried finding a workaround, but I couldn’t. In case you know it, or you find a workaround, do let me know in the comments section.

### Can you use cells with numbers in the scientific format in the calculation?

Yes, you can use the cells with numbers in scientific format in calculations. When you show a number in scientific format, it only changes the way the number is being displayed, not the actual number in the cell.

One exception to this would be when your scientific notation is a result of a formula that gives text string or when you have manually entered it where it is preceded by an apostrophe.

### Why do I see the hash/pound symbol (#) instead of the Scientific Notation?

Most likely, this is because your column width is not big enough to accommodate the entire notation. To fix this, try increasing the column width.

### Can Scientific Notation Format be Turned Off in Excel?

No, it can’t be turned off. However, if you’re importing numbers into your Excel worksheet and you do not want these numbers to be converted into scientific notation, a workaround would be to first format the cells as Numbers or Text and then copy these large numbers.

**Other Excel articles you may also like:**

*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    
*   [Convert Fraction to Decimal in Excel](https://trumpexcel.com/convert-fraction-to-decimal-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/scientific-notation-excel/#respond)

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