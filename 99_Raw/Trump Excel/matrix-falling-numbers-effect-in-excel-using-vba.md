# Matrix Falling Numbers Effect in Excel using VBA

**Source:** https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba

---

[Skip to content](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#below-title)

I am a huge fan of the Matrix movie series. It an amazing piece of work of its time and one of my favorites science fiction movie series.

If you have seen Matrix, there is no way you wouldn’t remember the falling code sequence.

I thought of creating this in Excel, but someone beat me to it. It has already been created and is available [here](http://www.engineers-excel.com/Apps/Digital_Rain/Description.htm)
.

Nitin Mehta, who created this, used a couple of [Excel functions](https://trumpexcel.com/excel-functions/)
, [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
, and a [scroll bar](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
 to create this effect.

I have modified it to remove the scroll bar and have used a VBA code instead. Now you can simply click on the play button and the numbers would start falling by itself. Something as shown below:

![Matrix Falling Numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20556'%3E%3C/svg%3E)

#####  Matrix Falling Numbers Effect in Excel

Here are the steps to create the matrix falling numbers effect in excel:

*   In the first row in the range A1:AP1, enter random numbers between 0 to 9. You can either manually enter these numbers of use the [RANDBETWEEN](https://trumpexcel.com/excel-randbetween-function/)
     function. Remember to convert these numbers into values.
    *   Reduce the column width so that it is visible in a single screen.

![Matrix Falling Numbers - first row](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%2095'%3E%3C/svg%3E)

*   In the range A2:AP32, enter the formula: \=[INT](https://trumpexcel.com/excel-int-function/)
    ([RAND](https://trumpexcel.com/excel-rand-function/)
    ()\*10)

*   Copy and paste the below code in a module in VBA
    
    #If VBA7 Then
    Public Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As Long) 'For 64 Bit Systems
    #Else
    Public Declare Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As Long) 'For 32 Bit Systems
    #End If
    
    Sub MatrixNumberRain()
    i = 1
    Do While i <= 40
    DoEvents
    Range("AR1").Value = i
    i = i + 1
    Sleep 50
    Loop
    End Sub
    

This above code would enter the number from 1 to 4o in cell AR1. The code Sleep 50 would delay the entering of numbers by 50 milliseconds. If you run this code, you would be able to see the value in AR1 go from 1 to 40.

Now we need to specify three conditional formatting rules to give color to these numbers.

**Conditional Formatting Rule #1**

*   Select the range A2:AP32, go to Home –> Conditional Formatting –> New Rule

![Matrix Falling Numbers - New Rule in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20195%20374'%3E%3C/svg%3E)

*   In the New Formatting Rule dialogue box, click on ‘Use a formula to determine which cells to format’ and enter the following formula:  
    \=[MOD](https://trumpexcel.com/excel-mod-function/)
    ($AR$1,15)=MOD([ROW()](https://trumpexcel.com/excel-row-function/)
    +A$1,15)

![Matrix Falling Numbers - Conditional Formatting formula 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20370'%3E%3C/svg%3E)

*   Click on format button and set the font color to white

![Matrix Falling Numbers - Conditional Formatting color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20405'%3E%3C/svg%3E)

*   Click OK

**Conditional Formatting Rule #2**

*   With the range A2:AP32 selected, go to Home –> Conditional Formatting –> Manage Rule
*   In the Conditional Formatting Rules Manager dialogue box, click on New Rule
*   In the New Formatting Rule dialogue box, click on ‘Use a formula to determine which cells to format’ and enter the following formula:  
    \=MOD($AR$1,15)=MOD(ROW()+A$1+1,15)
*   Click on format button and set the font color to light green
*   Click OK

**Conditional Formatting Rule #3**

*   With the range A2:AP32 selected, go to Home –> Conditional Formatting –> Manage Rule
*   In the Conditional Formatting Rules Manager dialogue box, click on New Rule
*   In the New Formatting Rule dialogue box, click on ‘Use a formula to determine which cells to format’ and enter the following formula:  
    \=OR(MOD($AR$1,15)=MOD(ROW()+A$1+2,15),MOD($AR$1,15)=MOD(ROW()+A$1+3,15), MOD($AR$1,15)=MOD(ROW()+A$1+4,15),MOD($AR$1,15)=MOD(ROW()+A$1+5,15))
*   Click on format button and set the font color to light green.
*   Click OK.

Based on the row number and value in the first row, conditional formatting would color the text green, light green or white.

Now select the entire range of cells (A1:AP32) and make the background black.

As a final step, insert a shape/button and assign this macro to that shape/button.

_Note__:_ Since this has a VBA code in it, save the file with .xls or .xlsm extension.

That’s it! Now get yourself a cup of coffee, stand in the shade, and enjoy the Matrix falling numbers digital rain 🙂

_**Download the Example File**_  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/wzbm9y3v4hf7teh/Matrix-Falling-Numbers-Effect.xlsm?dl=1)

**You May Also Like the Following Excel Tutorials:**

*   [Useful Excel VBA Macro Examples (Ready-to-use)](https://trumpexcel.com/excel-macro-examples/)
    .
*   [How to Sort Data in Excel using VBA (A Step-by-Step Guide)](https://trumpexcel.com/sort-data-vba/)
    .
*   [How to Select Every Third Row in Excel (or select every Nth Row).](https://trumpexcel.com/select-every-third-row/)
    
*   [How to Use Excel VBA InStr Function (with practical EXAMPLES)](https://trumpexcel.com/excel-vba-instr/)
    .
*   [Make VBA Code Pause or Delay (Using Sleep / Wait Commands)](https://trumpexcel.com/vba-sleep-wait/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Matrix Falling Numbers Effect in Excel using VBA”
----------------------------------------------------------------

1.  This is great! I wonder if there is a way to have the Shape act as a Start/ Stop button?
    
    [Reply](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#comment-10814)
    
    *   Got it:  
        `   Public iMatrix As Boolean`
        
        `   #If VBA7 Then   ...   `
        
        `Sub MatrixNumberRain()   If iMatrix = False Then   iMatrix = True   i = 1   Do While iMatrix = True   DoEvents   Range("AW1").Value = i   i = i + 1   Sleep 100   Loop   Else   iMatrix = False   End If   End Sub   `
        
        [Reply](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#comment-10815)
        
2.  Hi Sumit, glad to see you found this app useful and good work with the macro!
    
    Nice site, keep up the good work!
    
    Best wishes,  
    Nitin
    
    [Reply](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#comment-2630)
    
3.  If I could think of any justification for using this in my work, I would totally do it.
    
    [Reply](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#comment-2556)
    
    *   I wish the same Richard.. Chart Animations can be created in the same way, but even that has a limited use (if any) in day to day work.
        
        [Reply](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#comment-2557)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/matrix-falling-numbers-effect-in-excel-using-vba/#respond)

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