# Highlight Active Row and Column in Excel (Easy Steps)

**Source:** https://trumpexcel.com/highlight-active-row-column-excel

---

[Skip to content](https://trumpexcel.com/highlight-active-row-column-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/highlight-active-row-column-excel/#below-title)

One of the Excel queries I often get is – “How to highlight the Active Row and Column in a data range?”

And I got one last week too.

![Reader Query - How to Highlight Active Row and Column](https://trumpexcel.com/wp-content/uploads/2017/06/Reader-Query-How-to-Highlight-Active-Row-and-Column.png)

So I decided to create a tutorial and a video on it. It will save me some time and help the readers too.

Below is a video where I show how to highlight the active row and column in Excel.

In case you prefer written instructions, below is a tutorial with exact steps on how to do it.

Let me first show you what we are trying to achieve.

![A Demo to Show how to highlight the active row and column on selection change](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20724%20316'%3E%3C/svg%3E)

In the above example, as soon as you select a cell, you can see that the row and column also get highlighted. This can be helpful when you’re working with a large dataset and can also be used in Excel Dashboards.

Now let’s see how to create this functionality in Excel.

**[Download the Example File](https://www.dropbox.com/s/jxcu38sm4brip8z/Highlight-the-Active-Row-and-Column.xlsm?dl=0)
**

Highlight the Active Row and Column in Excel
--------------------------------------------

Here are the steps to highlight the active row and column on selection:

*   Select the data set in which you to highlight the active row/column.
*   Go to the Home tab.
*   Click on Conditional Formatting and then click on New Rule.
*   In the New Formatting Rule dialog box, select “Use a formula to determine which cells to format”.
*   In the Rule Description field, enter the formula: **\=OR(CELL(“col”)=COLUMN(),CELL(“row”)=ROW())**
*   Click on the Format button and specify the formatting (the color in which you want the row/column highlighted).
*   Click OK.

The above steps have taken care of highlighting the active row and active column (with the same color) whenever there is a [selection change event](https://trumpexcel.com/vba-events/)
.

However, to make this work, you need to place a simple VBA code in the backend.

Here is the VBA code that you can copy and paste (exact steps also listed below):

'Code developed by Sumit Bansal from https://trumpexcel.com
Private Sub Worksheet\_SelectionChange(ByVal Target As Range)
If Application.CutCopyMode = False Then
Application.Calculate
End If
End Sub

The above VBA code is run whenever there is a selection change in the worksheet. It forces the workbook to recalculate, which then forces the conditional formatting to highlight the active row and the active column.

Normally (without any VBA code), a worksheet refreshes only when there is a change in it (such as [data entry](https://trumpexcel.com/excel-data-entry-tips/)
 or edit).

Also, an IF statement is used in the code to check if the user is trying to copy-paste any data in the sheet.

During copy-paste, the application is not refreshed, and it is allowed.

Here are the steps to copy this VBA code in the backend:

*   Go to the Developer tab _(can’t find the developer tab? – [read this](https://trumpexcel.com/excel-developer-tab/)
    ).![Developer tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20128'%3E%3C/svg%3E)_
*   Click on Visual Basic.![Visual Basic icon in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20127'%3E%3C/svg%3E)
*   In the VB Editor, on the left, you will see the project explorer that lists all the open workbooks and the worksheets in it. If you can’t see it, use the keyboard shortcut Control + R.![Vb Editor Project Explorer - Highlight Selected Row or Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20306'%3E%3C/svg%3E)
*   With your workbook, double-click on the sheet name in which you have the data. In this example, the data is in Sheet 1 and Sheet 2.
*   In the code window, copy and paste the above VBA code. You’ll have to copy and paste the code for both sheets if you want this functionality in both sheets.![Vb Code in the backend to highlight the active row and column in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20798%20211'%3E%3C/svg%3E)
*   Close the VB Editor.

Since the workbook has VBA code in it, save it with a .XLSM extension.

**[Download the Example File](https://www.dropbox.com/s/jxcu38sm4brip8z/Highlight-the-Active-Row-and-Column.xlsm?dl=0)
**.

Note that in the steps listed above, the active row and column would get highlighted with the same color. If you want to highlight the active row and column in different colors, use the below formulas:

*   \=COLUMN()=CELL(“col”)
*   \=CELL(“row”)=ROW()

In the download file provided with this tutorial, I have created two tabs, one each for single color and dual color highlighting.

Since these are two different formulas, you can specify two different colors.

#### Useful Notes:

1.  This method would not impact any formatting/highlighting you have done manually to the cells.
2.  [Conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
     is volatile. If you use it on very large datasets, it may lead to a slow workbook.
3.  The VBA code used above would refresh the workbook every time there is a change in selection.
4.  CELL Function is available in Excel 2007 and above version for Windows and Excel 2011 and above for Mac. In case you’re using an older version, use [this technique](http://chandoo.org/wp/2012/07/11/highlight-row-column-of-selected-cell-using-vba/)
     by Chandoo.

Want to Level-up your [Excel Skills](https://trumpexcel.com/excel-skills/)
? Consider joining one of my Excel courses:

*   **[Excel Dashboard Course](https://www.youtube.com/playlist?list=PLm8I8moAHiH1hBVHlq956Jq4qkcCCk8hn)
    **
*   [**Excel VBA Course  \
    **](https://www.youtube.com/playlist?list=PLm8I8moAHiH2n5HC4ZXBgS-cBLjxWDreu)
    

**You May Also Like the Following Excel Tutorials:**

*   [How to Highlight Blank Cells in Excel](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    .
*   [Highlight Rows Based on a Cell Value in Excel.](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [Highlight EVERY Other ROW in Excel](https://trumpexcel.com/highlight-every-other-row-excel/)
    .
*   [How to Move Rows and Columns in Excel.](https://trumpexcel.com/move-rows-columns/)
    
*   [Creating Heatmap in Excel](https://trumpexcel.com/heat-map-excel/)
    .
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    .
*   [24 Useful Macro Examples](https://trumpexcel.com/excel-macro-examples/)
    .
*   [Using Loops in Excel VBA](https://trumpexcel.com/vba-loops/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

81 thoughts on “Highlight Active Row and Column in Excel (VBA)”
---------------------------------------------------------------

1.  Very Good and thank you.  
    One small issue was that i found copying the formula in it’s BOLD format caused it not to work. I had to re-write it in normal text and it worked fine.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14799)
    
2.  Very good book. Useful for excel beginners
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14582)
    
3.  Searching this long grt tutorial and suffer one error also but with someone comment i change according n its work
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14385)
    
    *   here he typed:  
        \=OR(CELL(“col”)=COLUMN(),CELL(“row”)=ROW())
        
        everything needs to be caps so:  
        \=OR(CELL(“COL”)=COLUMN(),CELL(“ROW”)=ROW())
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-33297)
        
4.  thanks for your efforts, but i think Microsoft should add this as a basic excel services , no need to do this long steps
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14030)
    
    *   How to enable that please tell me.
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14334)
        
5.  Forgot one important thing. I am using Windows 10, 64 bit, Excel office 365.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13825)
    
6.  This is what I wanted. But, it only works on 1 worksheet in my workbook of 10 sheets. I have copied the VBA code on 2 or 3 sheets to see if that works, but still only works on 1 sheet. I would like to be able to not only work on all sheets, but also any other workbook file I need to use it in. Can you help me? Also, is it possible to make this an Excel Add-in, so it would work in any file I open?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13824)
    
7.  I’ve noticed that it’s not possible to use ctrl+z if you make a change in a cell and then selet another cell. Is it possible to Work around this with an additional code of VBA?
    
    Thank you in advance!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13787)
    
8.  Awesome explanation .It helps lot .
    
    Can you post how to work in timing  
    Ex : 1,1.30,1.0,1.30 ,Sum=5 hrs  
    If we call calculate in excel it comes =4.60 hrs  
    Pls support
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13684)
    
9.  FIXED:  
    1\. Change to UPPERCASE — (Replace “row” and “col” with “ROW” and “COL”)  
    2\. MANUALLY replace the quotes — (copy paste from browser inserts curly quotes)
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13678)
    
10.  jamshaid
    
    can you help me to do this in google sheet ?  
    thanks
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13557)
    
11.  can you help me to do this in google sheet ?  
    thanks
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13556)
    
12.  Guys,  
    If it does not work for you then in the conditional formating formula delete the quotation marks and type them in again.
    
    Replace below:  
    \=OR(CELL(“col”)=COLUMN(),CELL(“row”)=ROW())
    
    With below:  
    \=OR(CELL(“col”)=COLUMN(),CELL(“row”)=ROW())
    
    If you look closely you see it is a different type of quotation mark: “ ”
    
    Let me know if it worked for you 🙂
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13425)
    
    *   It doesn’t work for me 🙁 I need to put ‘ infront of it or my excel doesn’t know what im trying to do or something, is there any solution?
        
        Thanks!
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-17043)
        
13.  Hi there,  
    Thanks for the code.
    
    My doubt is code is getting failed when its have background colour applied on the sheet
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13396)
    
14.  Doesn’t work
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13324)
    
15.  It is not working in my excel
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13241)
    
16.  Pure Gold, pure gold. Thank you!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13231)
    
17.  you are just awesome !!! I always wanted to do this !!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13218)
    
18.  Hello,  
    Is it possible to just highlight the active cell, and not the entire row & column?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13182)
    
    *   In the conditional formatting rules, change =OR(…) to =AND(…)
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14352)
        
19.  How to highlight active range in conditional formatting?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13013)
    
20.  sumit
    
    thanks for your effort … it is very helpful.
    
    is one improvement possible – have the highlight work in the middle of cut-paste?
    
    an example …  
    i am copying data from one person (row) to another person (other row)  
    when i select row 3, cols b+c, and copy … the proper row and col b highlight.  
    when i select a cell in row 7 col b to paste, (another person) the highlight does not change (since cutcopymode = false )  
    until i paste the data into the selected cell , then the highlight changes correctly.
    
    it would be helpful to see the highlight change when i selected the cell – before i paste the data – so i could be sure i had selected the right person/row.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12814)
    
21.  Hi,  
    Excactly what I need but I type the formula and VBA and it is not working. it is save as .xlsm. Could I send you my file? Thanks for your help
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12677)
    
22.  How can I highlight the row depending on a cell entry?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12655)
    
23.  THANK YOU! Your tutorial worked perfectly!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12644)
    
24.  My workbook has multiple sheets. I’m able to follow your instructions and get it to work on the first time. Is there a way to apply this set of instruction for all the sheets? Right now, I’m having to repeat the instructions multiple times for the entire workbook.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12271)
    
25.  Thank you for being so helpful and articulate. It’s people like you who I really appreciate!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12173)
    
26.  What a useful tip! I would love it if I could click over to another workbook without affecting the highlighting. Is there a way to accomplish this?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12145)
    
27.  SOLUTION:  
    For anyone who tries this and it doesn’t work – as the comment above me mentioned….. RE-TYPE the QUOTATION MARKS ” ” for “col” and “row”. And it should solve the problem.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11996)
    
    *   Thank you!!
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12316)
        
    *   Thank yoU!
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12734)
        
    *   Thank you!!!
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-12809)
        
    *   Thanks Boss u r grt since 30 min i m trying n jst i type quotation mark n its worked
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14384)
        
    *   thank you!!!!!!
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-14810)
        
28.  Thank you so much for posting this tutorial. I am a lament user and i was able to follow this tutorial and set up the macro in the developers tab and the conditional formatting in my spreadsheet. It is so much easier to navigate now. You are awesome! Keep doing what you do, it is much appreciated!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11912)
    
    *   Thank you so much for the kind words.. Glad you found the tutorial useful 🙂
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11913)
        
29.  Awesome!! Did exactly what I wanted it to do! Thank you!!!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11864)
    
30.  Exactly what I needed except one serious issue: My spreadsheet is CPU intensive. Therefore I’ve turned off auto calculation. This VBA code (as you do note) forces recalculation. Will there be any way around this issue?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11765)
    
31.  Thank you for simple and best explanation given.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11687)
    
32.  Hi Submit, Thanks for your clear & accurate instructions… I had no problems setting this up. Years ago I looked for a Col-Row Highlighter like this but never found it. Today I checked again and found your solution. Great job on both instructions and execution. Thank you!!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11683)
    
33.  You have curly quotes in your example text!! (e.g. “ and ”)  
    You need normal quotes! (e.g. “)  
    Otherwise the formulas won’t work if you copy and paste.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11622)
    
    *   Ok well apparently this website automatically formats quotes as curly quotes. So don’t copy anything directly from here. You need to type the quotes into your code manually.
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11623)
        
    *   Thanks! Couldn’t figure out why I wasn’t able to get mine to work. 🙂
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11832)
        
34.  this formula isn’t working for me! Excel 2016
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11559)
    
35.  Hi! How can I activate the undo and redo button?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11442)
    
36.  I had to replace the “,” for a “;” for the formula to work (to be accepted by Excel). Must be a french Excel version whim…
    
    If you’re interested: =OU(CELLULE(“col”)=COLONNE();CELLULE(“row”)=LIGNE())
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11286)
    
37.  I, like others, had problems getting this to work, and solved it following the suggestion to type the entire formula by hand into the conditional formatting screen. However, I still had a weird problem. Sometimes when I changed the cell selection, it would not update the highlighting in some of the adjacent blocks and not highlight some of the correct blocks. It seemed to be a screen updating problem on my PC, since scrolling down and back again would fix the problem. Finally, I changed the VBA code to:
    
    Private Sub Worksheet\_SelectionChange(ByVal Target As Range)  
    If Application.CutCopyMode = False Then  
    Application.ScreenUpdating = “False”  
    Application.Calculate  
    Application.ScreenUpdating = “True”  
    End If  
    End Sub
    
    to force the screen to update, but I’m not sure why I had to do this.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11176)
    
    *   Thank you!!! Mine wasn’t working at first, but this solved my problem!
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13088)
        
38.  HI, I followed these tips exactly. But it does not work. I think my conditional formatting may be the issue. I have had similar challenges using CF in the past.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11155)
    
39.  This worked great for me. Just what I needed. Thank you!
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11153)
    
40.  For spanish people:
    
    \=O(CELDA(“columna”)=COLUMNA();CELDA(“fila”)=FILA())
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11032)
    
41.  Nice of course, but a little more should be told.  
    A little more efforts are needed if you intend to use it for highlighting different rows/columns in multiple workbooks/worksheets.  
    The CELL function works on “Application level” – it provides information for the currently active cell (regardless of worksheet or workbook).  
    For example if you apply this trick to sheet1 in workbook A, and then you edit cell C3 in workbook B row 3 and column C in workbook A sheet1 will be highlighted. Of course situations exist when this may be exactly what one needs.  
    I thought it is good to mention this.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10882)
    
42.  I followed all the steps but no highlight is seen.  
    Not sure what I’m doing wrong.  
    The example file works for me even though it popped up an VB error, oddly only the 1st time when I opened it.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10840)
    
43.  I downloaded the excel example (and from what I can tell) – everything is the same. It’s still not working. I assume since saving as a .XLSM extension is not an option it’s set as a default??
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10837)
    
    *   Never mind – I read other comments and typed in everything manually. Works like a charm!!
        
        Also, when typing in the conditional formatting code use ALL CAPS. 🙂
        
        Thank you for this!!
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10838)
        
44.  Thanks for sharing this. I only have a problem when i’m using 2 excel windows side by side. Because when I swicht to the other window the cell formating in the first window changes. I there any solution for this?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10733)
    
45.  Hi, it is not working for me, I have Office 365 and have enabled the macros copying all the details but nothing gets highlighted. Any idea what I’m doing wrong?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10703)
    
46.  Doesn’t work for me. VBA code is identical, conditional formatting is identical. It’s Excel 2016. Any suggestions?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10654)
    
47.  Hi,
    
    Is there a way to make this work with a dynamic selection ? I would like this to work after I paste in a new set of data/selection (The selection will have the same columns, but the rows varies.
    
    Thanks
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10540)
    
48.  \=OR(CELL(“COL”)=COLUMN(),CELL(“ROW”)=ROW()) worked for me instead of =OR(CELL(“col”)=COLUMN(),CELL(“row”)=ROW())
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10388)
    
49.  Hi, I loved this highlight, but I need to keep using the “COPY” and “PAST” function as numbers and formulas. It is possible?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9551)
    
    *   You can use the following VBA code:
        
        Private Sub Worksheet\_SelectionChange(ByVal Target As Range)  
        If Application.CutCopyMode = False Then  
        Application.Calculate  
        End If  
        End Sub
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10285)
        
        *   How to do the trick with Mac? Because I just keep getting message: Variable uses an Automation type not supported in Visual Basic. And I can’t go around it.
            
            [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-13819)
            
50.  Hi Sumit,  
    I am trying to use my spreadsheet with your modification. A problem I have found is that although I can copy a range of cells which are highlighted as normal, the paste function is greyed out. Ctrl+V also doesn’t work. Any ideas why?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9518)
    
51.  Me again,  
    Maybe I should have read the instructions more carefully!! ;-)) I missed out the VBA code. Added it and now working brilliantly.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9515)
    
52.  Hi again, Just discovered that it works if I just select a cell and then press either page up or page down.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9514)
    
53.  Hi Sumit, I have tried to introduce this trick into a spreadsheet using Excel 2016. I used the conditional format method without the macro. Is it necessary to write the macro as well? The only way I can get it to work is to select a cell, press F2, and then press enter. In your example it is not necessary to go the F2 then enter route. Is there an option setting I am missing? Something to do with automatic screen updating?
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9513)
    
54.  General Copy and Past not working
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9473)
    
    *   is there a way to fix it? and make genera copy and paste work?
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10284)
        
        *   Use the following VBA code:
            
            Private Sub Worksheet\_SelectionChange(ByVal Target As Range)  
            If Application.CutCopyMode = False Then  
            Application.Calculate  
            End If  
            End Sub
            
            [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10286)
            
55.  Like the tip very much. but it is not working for me. i am using office 2010.  
    cells remain without highlight. cannot make out what’s wrong.
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9468)
    
    *   Hey Sunil, Did you copy the formula as is? I noticed that the quotation marks get copied in a different format. Try entering the formula manually and it should work
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9469)
        
        *   great. after few hits and trial it worked. now to replicate it in all my worksheets??? any shortcuts or just copy the conditional formatting and vba to the other sheets.  
            Thanks for the help – greatly appreciated.
            
            [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9471)
            
            *   Hi Sumit, is there any way to apply this to all worksheets in a workbook? Also, how to make it easily applicable to a new workbook?  
                thanks
                
                [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9472)
                
        *   Thanks – had to type it out myself (the quotations were the issue), works like a charm on my huge spreadsheets.
            
            [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-10710)
            
56.  Nice trick
    
    to the VBA i have added some lines.  
    With Application  
    .ScreenUpdating = False  
    .EnableEvents = False  
    .Calculate  
    .ScreenUpdating = True  
    .EnableEvents = True  
    End With
    
    screenupdating will help speeding up the highlighting  
    enableevents will prevent the triggering Worksheet\_Change
    
    [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9462)
    
    *   Thanks for sharing Miaousse 🙂 It sure will make the code better
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-9470)
        
        *   Hi – that’s great – can you give the revised vba code please, as I’m not sure if this is an add-on to the one you gave earlier. thanks
            
            [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11072)
            
    *   Where do you add those lines?
        
        [Reply](https://trumpexcel.com/highlight-active-row-column-excel/#comment-11084)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/highlight-active-row-column-excel/#respond)

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