# How to Count COLORED Cells in Excel [Step-by-Step Guide + VIDEO]

**Source:** https://trumpexcel.com/count-colored-cells-in-excel

---

[Skip to content](https://trumpexcel.com/count-colored-cells-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/count-colored-cells-in-excel/#below-title)

**Watch Video – How to Count Colored Cells in Excel**

Wouldn’t it be great if there was a function that could count colored cells in Excel?

Sadly, there isn’t any inbuilt function to do this.

BUT..

It can easily be done.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/count-colored-cells-in-excel/#)

How to Count Colored Cells in Excel
-----------------------------------

In this tutorial, I will show you three ways to count colored cells in Excel (with and without VBA):

1.  Using Filter and SUBTOTAL function
2.  Using GET.CELL function
3.  Using a Custom Function created using VBA

### #1 Count Colored Cells Using Filter and SUBTOTAL

To count colored cells in Excel, you need to use the following two steps:

*   Filter colored cells
*   Use the SUBTOTAL function to count colored cells that are visible (after filtering).

Suppose you have a dataset as shown below:

![Count Colored Cells in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20370'%3E%3C/svg%3E)

There are two background colors used in this data set (green and orange).

Here are the steps count colored cells in Excel:

1.  In any cell below the data set, use the following formula: \=SUBTOTAL(102,E1:E20)  
    ![Using Subtotal function to Count Colored Cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20383'%3E%3C/svg%3E)
2.  Select the headers.
3.  Go to Data –> Sort and Filter –> Filter. This will apply a filter to all the headers.
4.  Click on any of the filter drop-downs.
5.  Go to ‘Filter by Color’ and select the color. In the above dataset, since there are two colors used for highlighting the cells, the filter shows two colors to filter these cells.![Using Filter to Count Colored Cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20146'%3E%3C/svg%3E)

As soon as you filter the cells, you will notice that the value in the SUBTOTAL function changes and returns only the number of cells that are visible after filtering.![Count Cells with a background color - Filtered Cell Count Subtotal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20569%20165'%3E%3C/svg%3E)

**How does this work?**

The SUBTOTAL function uses 102 as the first argument, which is used to count visible cells (hidden rows are not counted) in the specified range.

If the data if not filtered it returns 19, but if it is filtered, then it only returns the count of the visible cells.

_**Try it Yourself.. Download the Example File  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/cl5s999ocjd0xll/Count-Cells-Based-on-Background-Color-TrumpExcel.xlsm?dl=1)
  
**_

Also read: [How to Count Filtered Rows in Excel?](https://trumpexcel.com/count-filtered-rows-excel/)

### #2 Count Colored Cells Using GET.CELL Function

GET.CELL is a Macro4 function that has been kept due to compatibility reasons.

It does not work if used as regular functions in the worksheet.

However, it works in [Excel named ranges](https://trumpexcel.com/named-ranges-in-excel/)
.

_See Also__:_ [Know more about GET.CELL function.](http://www.mrexcel.com/forum/excel-questions/20611-info-only-get-cell-arguments.html)

Here are the three steps to use GET.CELL to count colored cells in Excel:

*   Create a Named Range using GET.CELL function
*   Use the Named Range to get color code in a column
*   Using the Color Number to Count the number of Colored Cells (by color)

Let’s deep dive and see what to do in each of the three mentioned steps.

#### **Creating a Named Range**

*   Go to Formulas –> Define Name.![Count Colored Cells in Excel - Defined Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20127'%3E%3C/svg%3E)
*   In the New Name dialog box, enter:
    *   Name: GetColor
    *   Scope: Workbook
    *   Refers to: \=GET.CELL(38,Sheet1!$A2)  
        _In the above formula, I have used_ _Sheet1!$A2_ _as the second argument. You need to use the reference of the column where you have the cells with the background color._ ![Count Colored Cells in Excel - GetColor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20312%20242'%3E%3C/svg%3E) 

#### **Getting the Color Code for Each Cell**

In the cell adjacent to the data, use the formula \=GetColor

This formula would return 0 if there is NO background color in a cell and would return a specific number if there is a background color.

This number is specific to a color, so all the cells with the same background color get the same number.![Count Colored Cells in Excel - Color Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20390'%3E%3C/svg%3E)

#### **Count Colored Cells using the Color Code**

If you follow the above process, you would have a column with numbers corresponding to the background color in it.

To get the count of a specific color:

*   Somewhere below the dataset, give the same background color to a cell that you want to count. Make sure you are doing this in the same column that you used in creating the named range. For example, I used Column A, and hence I will use the cells in column ‘A’ only.
*   In the adjacent cell, use the following formula:

\=[COUNTIF](https://trumpexcel.com/excel-countif-function/)
($F$2:$F$20,GetColor)

This formula will give you the count of all the cells with the specified background color.![Count Colored Cells in Excel - Color Count without VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20576%20397'%3E%3C/svg%3E)

**How Does It Work?**

The COUNTIF function uses the named range (GetColor) as the criteria. The named range in the formula refers to the adjacent cell on the left (in column A) and returns the color code for that cell. Hence, this color code number is the criteria.

The COUNTIF function uses the range ($F$2:$F$18) which holds the color code numbers of all the cells and returns the count based on the criteria number.

_**Try it Yourself.. Download the Example File  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/cl5s999ocjd0xll/Count-Cells-Based-on-Background-Color-TrumpExcel.xlsm?dl=1)
  
**_

### #3 Count Colored Using VBA (by Creating a Custom Function)

In the above two methods, you learned how to count colored cells without using VBA.

But, if you are fine with using VBA, this is the easiest of the three methods.

Using VBA, we would create a custom function, that would work like a COUNTIF function and return the count of cells with the specific background color.

Here is the code:

'Code created by Sumit Bansal from https://trumpexcel.com
Function GetColorCount(CountRange As Range, CountColor As Range)
Dim CountColorValue As Integer
Dim TotalCount As Integer
CountColorValue = CountColor.Interior.ColorIndex
Set rCell = CountRange
For Each rCell In CountRange
  If rCell.Interior.ColorIndex = CountColorValue Then
    TotalCount = TotalCount + 1
  End If
Next rCell
GetColorCount = TotalCount
End Function

To create this custom function:

*   With your workbook active, press Alt + F11 (or right click on the worksheet tab and select View Code). This would open the VB Editor.
*   In the left pane, under the workbook in which you are working, right-click on any of the worksheets and select Insert –> Module. This would insert a new module. Copy and paste the code in the module code window.![How to Count Colored Cells in Excel - Insert Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20416%20417'%3E%3C/svg%3E)
*   Double click on the module name (by default the name of the module in Module1) and paste the code in the code window.![Custom function VBA code to Count Colored Cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20290'%3E%3C/svg%3E)
*   Close the VB Editor.
*   That’s it! You now have a custom function in the worksheet called GetColorCount.

To use this function, simply use it as any regular [excel function](https://trumpexcel.com/excel-functions/)
.

_Syntax:_ \=GetColorCount(CountRange, CountColor)

*   **CountRange:** the range in which you want to count the cells with the specified background color.
*   **CountColor:** the color for which you want to count the cells.

To use this formula, use the same background color (that you want to count) in a cell and use the formula. CountColor argument would be the same cell where you are entering the formula (as shown below):

![Count Colored Cells in Excel - Custom Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20390'%3E%3C/svg%3E)

_**Note:** Since there is a code in the workbook, save it with a .xls or .xlsm extension._

_**Try it Yourself.. Download the Example File  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://www.dropbox.com/s/cl5s999ocjd0xll/Count-Cells-Based-on-Background-Color-TrumpExcel.xlsm?dl=1)
  
**_

Do you know any other way to count colored cells in Excel?

If yes, do share it with me by leaving a comment.

**You May Also Like the Following Excel Tutorials:**

*   [Count Cells that Contain Text](https://trumpexcel.com/count-cells-that-contain-text/)
    
*   [How to Sum by Color in Excel (Formula & VBA)](https://trumpexcel.com/sum-by-color-excel/)
    
*   [Filter Cells with Bold Font Formatting](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [How to Format Partial Text Strings using VBA](https://trumpexcel.com/excel-vba-instr/)
    
*   [Highlight EVERY Other ROW in Excel](https://trumpexcel.com/highlight-every-other-row-excel/)
     (using conditional formatting).
*   [How to Quickly Highlight Blank Cells in Excel.](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [How to Compare Two Columns in Excel.](https://trumpexcel.com/compare-two-columns/)
    
*   [Excel Conditional Formatting Based on Another Cell](https://trumpexcel.com/conditional-formatting-based-on-another-cell-excel/)
    
*   [Count Rows Using VBA](https://trumpexcel.com/excel-vba/count-rows/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

68 thoughts on “How to Count Colored Cells in Excel?”
-----------------------------------------------------

1.  Thank you for this!
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-41348)
    
2.  I’m noticing that the VBA method doesn’t work with conditional formatting of background colors. Any workaround for hat?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14830)
    
    *   I have the same issue
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14850)
        
3.  Hi, I am using the VBA module to count preferred meeting session times, it was working OK – until I added a separate VBA module called CounxlDiagonalDown to count diagonal borders (people who have indicated they are not attending said meeting), and now I am getting a #NAME? syntax error on the GetColorCount. any suggestions on a fix? Thanks
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14813)
    
4.  Thanks, your VB macro works perfectly!!
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14686)
    
5.  Great stuff, but the VB does not work on conditional formatting.. only if you manually change the background color of cells. Have any idea to count backgrounds with conditional formating?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14611)
    
6.  Thank you so much. Just what I needed.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14597)
    
7.  Great vba function! Very useful. I change the ‘interior’ to ‘font’ and it works nicely when counting range with different font colors. However, I tried it to conditional formatting and it didn’t work. Any idea, why?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14545)
    
8.  Does this work with horizontal range. Doesnt seem to be working in mine with an horizontal range
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14543)
    
9.  Fantastic video and article. Very helpful and simple to follow. Thank you!
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14532)
    
10.  Simple and straight forward. This did the job. Thank you!
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14466)
    
11.  I have a set of two ranges with compassion:  
    Say my A2:A10 with data of  
    B2:B10 with data of  
    I applied function in C2 and draged upto C10<=if(isna(Match($A$2:$A$10,$B$2:$B$10,0)),A2," ")  
    Which give me the result as (this result says not shared number of Set A2:A10 to B2:B10)  
    Now I coloured Full set of A2:A10 and also B4 and B9 as yellow and I need the out put in C2 to C10 as
    
    Can any body help me to fix this problem
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14310)
    
12.  (VBA Solution)  
    Too good to be true…just throws the standard formula error (“not trying to type a formula etc.”
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14159)
    
13.  Thank you so much, this solve my problems.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14101)
    
14.  The code in the screen shot of the VBA has errors
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14036)
    
15.  Help! Is there anyway to modify this VBA so that it works for =max
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13658)
    
16.  GOOD TRICKS FOR COUNTING BY COLOUR
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13462)
    
17.  tried =SUBTOTAL(102,$E$2:$E$20) and didn’t work. waste of time
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13421)
    
18.  Is there a way to count the cells by color but also having a criteria?. For example I want to count the cells in a column that are colored grey but only the ones that have an specific value on them like having the word “unique” in the cell.
    
    I would really appreciate the help thanks
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13058)
    
    *   I know this is kind of a ghetto solution, but:  
        I just copied the unique cells I needed to a different worksheet and did the function there, it worked perfectly
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13084)
        
19.  Great code. However, it does not automatically update, unless I click on the cell each time. Please note, I have excel set to automatically update calculations, so not sure why not working.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12844)
    
20.  The VBA function worked great!! I’m now showing off to anyone in the office who will listen! Thanks very much
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12834)
    
21.  Hello! I cannot get my get.cell (38,…) to work. Is there any chance I could contact you?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12544)
    
    *   Can you please try with ; instead of , ? It work for me.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12950)
        
22.  Using VBA was perfect! Thanks
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12486)
    
23.  I’m using your VBA method, and it works just fine, but is there any way to make it work for cells that have RGB color values instead of the standard ones from the color palette? Using .ColorIndex only works for those types of colors
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12075)
    
24.  Hi,  
    The function option works fine, there is only one thing. As soon as one of the colours changes the sum won’t refresh, is there an way to sort this out ?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-11826)
    
    *   Delete the module > save > close and reopen file > add the module again > click on any cell with the formula > press “enter”
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12214)
        
    *   Push F2.  
        Push Enter.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13248)
        
25.  Is there a way to apply this to rows rather than columns?!
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-11507)
    
26.  The VBA formula worked great on my spreadsheet. But, I saved it and re-opened and now all the cells where I had formulas say #Name?. I checked and the code is still in the module. It comes up in the list when I begin to type =getcolorcount. I tried removing the Code and re-inserting and can’t get the formula to work any longer. I’m using Excel 2010, is there any reason this suddenly wouldn’t work now?
    
    Please help – this formula was perfect for my spreadsheet for work because I didn’t want to have to add another column to the spreadsheet to get this to work.
    
    Thanks,  
    Jana
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-11335)
    
27.  Does this work in an online excel sheet?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-11304)
    
28.  Hi,  
    Thanks for the VBA code, I used your code and it works perfect – it counts the colored cells, but it does not update automatically. If a new cell is colored, everyctime I have to click on the formula to have it update the count.  
    Is there any other way to get this automated when a new cell is colored?  
    Appreciate your response
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-11132)
    
29.  I’ve used your VB method and it works great, thank you so much! I do have an issue though that I’m having troubles resolving…
    
    I’m using your formula as part of a calendar to track equipment utilization by filling the cells with color when the equipment is used. The problem I’m having is that the formula does not automatically recalculate when new colored cells are entered. It does recalculate when you click on the cell containing the formula and press enter, but I’ve got hundreds of assets that I’m tracking and that’s not an efficient way of doing it.
    
    I’ve tried all the usual, F9, recalculate formula, recalculate worksheet, etc. nothing works. I’ve even recorded Macros of actually highlighting all formula cells and clicking enter. It works when I do it, but the macro returns a value error when used.
    
    Do you have a work around for this or another VB Macro that can be assigned to a radio button to recalculate the colored cell totals each time the calendar is updated?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-10707)
    
    *   Ctrl-Alt-F9
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-11062)
        
30.  I found this article very useful, yet the VBA functions didn’t work. I have a table with various data, I used the conditional formatting in one column and built 5 rules and based on that cells have been colored in greed, red and yellow…any thoughts?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-10471)
    
    *   I have come across 5 functions that count coloured cells such as this code, and none of them work on conditional formatting.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13249)
        
31.  I have used your following code and it works perfectly:
    
    Function GetColorCount(CountRange As Range, CountColor As Range)  
    Dim CountColorValue As Integer  
    Dim TotalCount As Integer  
    CountColorValue = CountColor.Interior.ColorIndex  
    Set rCell = CountRange  
    For Each rCell In CountRange  
    If rCell.Interior.ColorIndex = CountColorValue Then  
    TotalCount = TotalCount + 1  
    End If  
    Next rCell  
    GetColorCount = TotalCount  
    End Function
    
    But, now I want to do a little more. For the range of cells, I want to have 4 separate functions. 1) Count cells IF they are a particular color, as well as ending in “\*o” 2) Count cells IF they are a particular color, as well as ending in “\*s” 3) Count cells IF they are a particular color, as well as having 2 text characters in the cell, “??” and 4) Count cells IF they are a particular color, as well as having a number greater than zero in the cell, “>0”. How can I modify the base “GetColorCount” code to incorporate this additional parameter for each instance?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-10444)
    
32.  I tried using your 3rd option but I am thinking that I am not right in doing so. Here is what I have and what I am trying to do. I have a spreadsheet with my supervisors and their clock-in times that I export from our schedule and then copy & paste into workbook. I color each row based on if they were on time, late but the time rolled back (7 minute grace period) and late but jumped forward 1/4 hour. I then filter by the supervisor’s last name and then by the “ErrorLog” header, checking only CLOCK IN & LATE CLOCK IN. The “Clock In” option could be either green (on time) or orange (late but rolled back) and then Late Clock In is yellow. The entire ErrorLog column is K10:K118, for all supervisors. Obviously when I sort by both Last Name and ErrorLog headers it reduces the number of rows and hides all the rest. I just want the formula to count each color that is visible. Is what I am doing even possible? I want to be able to change up the filter a bit by changing the Last Name so that I can only see each supervisor individually.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-10439)
    
33.  Great video…. I do have a question for you… I used your code and it works perfect except for one thing, it counts the colored cells, but it does not update automatically. If a new cell is colored, I have to click on the formula to have it update the count. Is there a code I can add to have it update automatically once a new colored cell is added? Thanks again for a great video!!!
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-10022)
    
34.  Your VBA solution works BUT NOT with colors from “Conditional Formating.”
    
    I have 17 cells in a column, all under a conditional formatting to turn the cell color “light red” if a certain condition is met. There are only 3 cells that are “light red” (meeting the condition) but your VBA script returns an answer of “17”, meaning it considers all cells “light red”. Then I manually went in and colored one cell (not already highlighted by the conditional formatting) blue, and your VBA returned an answer of “16”. Clearly then, it does not recognize the results of conditional formatting, only “manually entered” colors.
    
    Any solution? This is critical as the colored cells will be different depending on what conditions are met. I need a way to count them per each condition.
    
    (I learned a lot about adding a custom VBA code. Thanks!)
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-10002)
    
    *   Same issue! Any suggestions?
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-12619)
        
    *   Was there any answer to this question? thanks.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-14546)
        
35.  Hi,  
    can you use both GetColorCount and Sumbycolor VBA in the same worksheet.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-9770)
    
36.  Can you please explain what is 38 mentioned in the name manager formula? What does it relate to?
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-9497)
    
    *   If you follow the link to more information about Get.Cell it tells you, I was wondering the same thing.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-13133)
        
37.  When i press ‘enter’ with you’r download exel i get #NAME? why? PS ; I am new in VBA
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-9085)
    
38.  [https://uploads.disquscdn.com/images/3f93ede176e443ec907f29b2d6cd8c3b4960f606edfc43f4bb412848e5fe379a.png](https://uploads.disquscdn.com/images/3f93ede176e443ec907f29b2d6cd8c3b4960f606edfc43f4bb412848e5fe379a.png)
     [https://uploads.disquscdn.com/images/d440cd03823e1b89b27883aa9710447c85aa338bfdeb78c6c36c755916928480.png](https://uploads.disquscdn.com/images/d440cd03823e1b89b27883aa9710447c85aa338bfdeb78c6c36c755916928480.png)
     Hello, I am trouble getting the VBE working for counting coloured cells, I have tried all the suggestions but still not getting it. The closest I got to was that it appeared “0” which did not calculate the coloured cell. That I guess is an improvement from #NAME?” or #VALUE?” messages. Please help!!
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-4308)
    
    *   Please email me at [sagsinthecity@gmail.com](mailto:sagsinthecity@gmail.com)
         or message me at [https://www.facebook.com/SAGSOFFICIAL](https://www.facebook.com/SAGSOFFICIAL)
         Thanks
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-4309)
        
39.  Hi, please assist. if the cell is in cf it doesn’t count. i am using also the standard cf for date occuring.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-3469)
    
    *   Hey Mart.. Yes this doesn’t work when conditional formatting is in play. IF you want to count based on CF rules, you can use the same rule you have used to apply conditional formatting and count the total values. For example, if you use CF to highlight cells that contain “Yes”, then use a COUNTIF function to count all these cells.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-3622)
        
40.  How can you accomplish the same thing except counting cells in a row versus column (as outlined here)? For example, I want to know how many of each color (Red, Yellow, Green, and no color) are in row 2 (range – A2:I2).  
    Side note/issue: The Subtotal function seems to only count cells that have something in them. I would like to count cells that are just a color without any text in the cell. Is that possible?  
    Thanks for your help.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-3270)
    
    *   I am looking for this answer as well. I need the count of cells from a bigger range a2:bz52. And some cells are merged. Is there a way for this? Thank you in advance! Zita
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-11516)
        
41.  I liked the VBA option, works like a charm. However if my data range is non-continuous , for example, instead of A1:A10, I need to count the cell color in A1, A4, A9, How should I modify the formula? Thanks.
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-2924)
    
    *   Hi Azz,  
        Enclose your non-continuous range within brackets inside the function, (x, y, z, a:c), so for your example, you would use:
        
        \=GetColorCount( ( A1, A4, A9 ), 50 )
        
        Where,  
        50 = Green box color index.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-3613)
        
42.  If declared strictly and with names more appealing (IMO ;)). Thank you for the code and the idea behind
    
    Public Function GetColorCount(ByRef Target As Excel.Range, ByRef rgColor As Excel.Range) As Long  
    Dim rCell As Excel.Range  
    Dim Color As Long  
    Dim lgCounter As Long
    
    Color = rgColor.Interior.ColorIndex  
    For Each rCell In Target  
    If rCell.Interior.ColorIndex = Color Then lgCounter = lgCounter + 1  
    Next rCell  
    GetColorCount = lgCounter  
    End Function
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-2631)
    
43.  Hi,
    
    I started using your Count Cells Based on Background Color in Excel #3 using VBA. This wors very good. Thanks for it.  
    But now I have a problem using the same function by checking cells where the background color is set by Conditional Formatting. I am checking for dates older than today() and mark these cells in red background; works well using conditional formatting but the count doesn’t work for these cells.  
    thank you for any idea or hint
    
    [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-2419)
    
    *   Hi Nico,
        
        Do you use a formula in your conditional formatting (CF)?  
        If you do, it returns TRUE and you are coloring the cells that meet that condition. This means that if you put the CF formula into a COUNTIF formula, you can count the cells that meet the CF conditions!
        
        Gr,  
        Raymond.
        
        [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-2420)
        
        *   Hi Raymond,
            
            No I’m not using a formula. I use a standard rule type: Cell Value “less than or equal to” =$A$1  
            In A+ I only update the day =today().  
            thx  
            Nico
            
            [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-2422)
            
            *   Nico,
                
                I did a test and I realised I needed a help column to do the job.
                
                Say that range A2:A10 has your values where you apply the CF to.  
                Formula in help column B:  
                in B2 put ‘=OR(A2<$A$1,A2=$A$1)', copy down and you will get a couple of TRUEs or FALSEs.
                
                The count formula anywhere can then be: =COUNTIF(B2:B10,TRUE).
                
                Or you can just use an IF formula in the help column, giving you 1 or 0 back. Then a simple SUM somewhere and there you are.
                
                I must be do-able without the help column but I don't know how (yet)!
                
                Raymond
                
                [Reply](https://trumpexcel.com/count-colored-cells-in-excel/#comment-2423)
                
                *   Hi Raymond,
                    
                    A help column isn’t very usefull and would need many additional help columns, so I searched and searched.  
                    On [http://www.excel-inside.de](http://www.excel-inside.de/)
                     (a german Excel & VBA site) I found an example using .Font.ColorIndex . With this information I found .Interior.ColorIndex and my day was made 🙂
                    
                    Next step: searching for the color indexes on [https://msdn.microsoft.com/en-us/library/office/ff840443.aspx](https://msdn.microsoft.com/en-us/library/office/ff840443.aspx)
                    
                    and it seems to work – refreshing manually after changes – but it works:  
                    ‘Function ColorRed(Area As Range)  
                    ‘ColorRed = 0  
                    ‘For Each cell In Area  
                    ‘If cell.Interior.ColorIndex = 3 Then  
                    ‘ColorRed = ColorRed + cell.Count  
                    ‘End If  
                    ‘Next  
                    ‘End Function  
                    Nico
                    
                *   Hi Nico,
                    
                    Thanks for the update and also for you providing the resources that led to the solution you found!
                    
                    An UDF (User Defined Function) is harmless in your case because you are using it in only one cell to get the count. So that’s great.  
                    In complex workbooks, where formulas must be in several rows, UDF’s are not recommanded unless no other choice because they make the workbook slow.  
                    And as they say, there is always another way, a simple, faster and stronger way…
                    
                    I found a non-vba solution: an array formula.
                    
                    Put the following formula adjusted to your needs where you want your count.  
                    In this example, I assume the IF statement is the same as in your conditional format that gives the cells a red color when TRUE. The formula says:  
                    for each cell in range A2:A10, if the cell value is equal or less than the value of A1, give 1, otherwise give 0. Then give a sum of all the individual results.  
                    I’ve used 1 IF with an OR but it didn’t work so it became 2 IF’s.
                    
                    Instead of just pressing ENTER, press CTRL+SHIFT+ENTER to make it an array formula, which you can recognize by the { } that Excel automatically puts around it:  
                    \=SUM(IF(A2:A10<$A$1,1,IF(A2:A10=$A$1,1,0)))
                    
                    So after CTRL+SHIFT+ENTER, you will see:  
                    {=SUM(IF(A2:A10<$A$1,1,IF(A2:A10=$A$1,1,0)))}
                    
                    No more manual refresh!
                    
                    More about the topic:  
                    [http://www.cpearson.com/excel/arrayformulas.aspx](http://www.cpearson.com/excel/arrayformulas.aspx)
                    
                    Gr,  
                    Raymond.
                    
                *   i am not a vbe user but this explanation was clear enough to take the dive;  
                    so i tried solution number 3 and it works!  
                    however, how can i make the sheet update the numbers after i changed the color of a cell? at this moment i need to go to this cell en hit enter;  
                    there must be a ‘trick’ to do this on my imac!
                    
                *   Hi Cezi,
                    
                    The only workaround I could came up with involves 2 steps:  
                    \[1\] Put ‘Application.Volatile True’ at the beginning of the the function code  
                    \[2\] Put the following code in the worksheet event area (it assumes that you want an update if you select any cell in range \[A1:A10\]; please adjust accordingly):
                    
                    Private Sub Worksheet\_SelectionChange(ByVal Target As Range)  
                    ‘Application.StatusBar = False  
                    On Error Resume Next ‘To avoid error if the selection isn’t in \[A1:A10\]  
                    If Target.Address = Intersect(Target, Range(“A1:A10”)).Address Then  
                    ActiveSheet.Calculate  
                    ‘Application.StatusBar = “Calculated”  
                    End If  
                    End Sub
                    
                    Gr,  
                    Raymond.
                    
                *   Hello Raymond, I am having the same issue but am not exactly sure how to follow the workaround you posted.
                    
                    \[1\] Should I paste ‘Application.Volatile True’ after the following row?
                    
                    ‘Function GetColorCount(CountRange As Range, CountColor As Range)’
                    
                    \[2\] Where should I put the code you have entered? I’m afraid I don’t know what the “worksheet event area” is or where I can find it.
                    
                    Thank you for your patience and a great guide!
                    
                    /Kara
                    
                *   Hello Kara,
                    
                    \[1\] Correct.  
                    \[2\] While in Excel, press ‘ALT+F11’ and that will bring you in the development environment.  
                    Then, follow the instructions I’ve put here (screenshot):
                    
                    [http://www.ehbeo.rayorganization.com/vba/screenshots/worksheets/Events\_SelectionChange.png](http://www.ehbeo.rayorganization.com/vba/screenshots/worksheets/Events_SelectionChange.png)
                    
                    Gr,  
                    Raymond.  
                    [http://www.ehbeo.com](http://www.ehbeo.com/)
                    
                *   Raymond,
                    
                    Your code for the workaround however disables copying and pasting? Do you know how to fix this?
                    
                    \-Amy
                    
                *   Hi Amy,
                    
                    Sorry about that. Yes, there is a fix. The first line of code should be:  
                    If Application.CutCopyMode Then Exit Sub
                    
                    So, the final worksheet ‘SelectionChange’ event should look like this:  
                    \[CODE\]  
                    Private Sub Worksheet\_SelectionChange(ByVal Target As Range)  
                    ‘If we are copying, do nothing and exit  
                    If Application.CutCopyMode Then Exit Sub
                    
                    On Error Resume Next ‘To avoid error if the selection isn’t in \[A1:A10\]  
                    If Target.Address = Intersect(Target, Range(“A1:A10”)).Address Then  
                    ActiveSheet.Calculate  
                    End If  
                    End Sub  
                    \[END CODE\]
                    
                    \-Raymond
                    

### Leave a Comment [Cancel reply](https://trumpexcel.com/count-colored-cells-in-excel/#respond)

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