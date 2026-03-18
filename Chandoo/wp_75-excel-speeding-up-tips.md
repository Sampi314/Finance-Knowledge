# 75 Excel Speeding up Tips - How to speed-up & optimize slow Excel workbooks?

**Source:** https://chandoo.org/wp/75-excel-speeding-up-tips

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

75 Excel Speeding up Tips Shared by YOU! \[Speedy Spreadsheet Week\]
====================================================================

*   Last updated on March 27, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

As part of our Speedy Spreadsheet Week, I have asked you to share your favorite tips & techniques for speeding up Excel. **And what-a-mind-blowing response you gave. 75 of you** responded with lots of valuable tips & ideas to speed-up Excel formulas, VBA & Everything else.

![75 Excel Speeding up Tips - How to speed-up & optimize slow Excel workbooks?](https://img.chandoo.org/optimize/excel-speeding-up-tips-by-you.jpg "75 Excel Speeding up Tips - How to speed-up & optimize slow Excel workbooks?")

**How to read this post?**

Since this is a very large article, I suggest reading few tips at a time & practicing them. Consider bookmarking this page so that you can refer to these wonderful ideas when you are wrestling with a sluggish workbook.

Thanks to all the contributors
------------------------------

Many thanks to everyone who shared their tips & ideas with us. If you like the tips, please say thanks to the contributor.

Please note that I am not able to share some of the files you emailed as they contained personal / sensitive data.

Read Excel Speeding-up tips by area
-----------------------------------

This page is broken in to 3 parts, click on any link to access those tips.

[Formula Speeding-up Tips](https://chandoo.org/wp/75-excel-speeding-up-tips/#formulas)
  
[VBA / Macros Optimization Tips](https://chandoo.org/wp/75-excel-speeding-up-tips/#vba)
  
[Everything Else](https://chandoo.org/wp/75-excel-speeding-up-tips/#ee)
  
[Share your tips](http://chandoo.org/wp/2012/03/27/75-excel-speeding-up-tips/#comment)

Formula Speeding-up Tips
------------------------

**Tips for Formula speeding up by Adam B of Perth**

I use Formula-Calculation Options-Manual to disable calculations when setting up complex inter-relating formula pages. This stops Excel from churning through calculations every time I change a cell, saving my time. I just hit F9 to recalculate when I want to see the results.

I use  
Application.ScreenUpdating = False and  
Application.Calculation = xlManual  
to speed up macros, and  
Application.StatusBar = LoopNum  
so I can see the status of my macro and estimate how long there is left to calculate. Don’t forget to switch these back at the end of the macro!

When I have complex formulas with results that won’t change, I hard-code these to save calculation time, but I keep the formula only in the first cell, or pasted in a comment.

**Tips for Formula speeding up by Adi**

Hi Chandoo,  
In spreadsheets that have vlookups, if the source file is not going to change; I have realized that it is better to paste-special the vlookup values. This is because even a couple of vlookup slows down the file massively on account of recalculating of values.  
Another step I take (this depends on the criticality of data and other factors) is to set the auto-save function in excel to an infrequent duration.  
Adi

**Tips for Formula speeding up by Andrew Carpenter**

Replace sum products with count ifs or sum ifs where possible – they calculate a million times faster!!

[About Andrew Carpenter](http://facebook.com/carpy1985)

**Tips for Formula speeding up by Andy Creager**

Avoid large number of SUMIFS, instead, aggregate data into a PivotTalble, then use the Index(Match) combo to locate the sums.

I have dramatically sped up large worksheets doing this.

**Tips for Formula speeding up by Arpit Patni**

1\. Change Calculation to Manual mode. Calculate manually only when required.  
2\. Delete all name ranges, unused area, unnecessary formatting.

[About Arpit Patni](http://www.linkedin.com/in/arpitpatni)

**Tips for Formula speeding up by Brad Autry**

I think some of the more basic, but highly effective tips to speed up larger workbooks are:

1.) Avoid array formulae, where possible. Everyone knows there are a million ways to skin the proverbial Excel cat. Find alternatives to array.

2.) Adjust the calculation options, if necessary. Frequent calculations = sluggishness. A word of warning, though – people need to know if calculations aren’t automatic, or it can/will cause confusion.

3.) If all else fails, copy and paste as value. If the recipients of your data don’t need the flexibility to enter new data and update values with calculations, take formulae out of the equation (no pun intended) all together.

**Tips for Formula speeding up by Brian**

I replaced all my SUMPRODUCT formulas with SUMIFS and calculation time went from about 50sec to instantaneous. My system is a AMD 6 processor with 8gig memory, Excel 2007.

**Tips for Formula speeding up by Conor**

Stay away from array formulas (unless to have calculations on Manual).

**Tips for Formula speeding up by Crisu**

A simple, little tip/trick for speeding up calculating:  
Sometimes in a workbook you have so many formulas that for effective work you have no other choice but to turn off the auto-calculating. Still you work on your workbook, writing new formulas, there is no problem if you just wrote one formula in one cell – it can be calculated by just F2-Enter combo. Problem is when you created a new formula for a whole column – you don’t have to calculate whole workbook now or “F2-enter” every cell – just select the column you want to calculate, Ctrl+H and change “=” for … “=”. It’s a known trick, still some people may not know it yet. Cheers.  
PS. I don’t work on English version of Excel so my translations may not be accurate.

**Tips for Formula speeding up by Dan**

I use templates with formulas in them that I add data to every month, and once I paste the next months data I copy down the formulas recalculate and then copy and paste the formulas except for one line of formulas for next month. In this way my spreadsheet of 200-300k & growing lines doesnt have to recalculate all the rows everytime.

[About Dan](http://www.linkedin.com/pub/dan-silecchia/38/a47/142)

**Tips for Formula speeding up by Darryl**

I set the Automatic Calculation option to manual make any changes in Excel and then hit F9 to calculate as and when required or set back to Automatic once I have completed any large or slow spreadsheets. Save me so much time and frustration. I would love to hear any other tips on speeding up spreadsheets.

**Tips for Formula speeding up by David**

Cut down on the use of Array formulas – particularly if they are nested in IF statements.

**Tips for Formula speeding up by J Thamizh Irai**

Speed tips for formulae  
1 As you type formula after the =sign, when the prompt appears select the down arrow key and press Tab key so that the function is inserted. Then press the fx in the formula bar to bring up the prompts and start filling the blanks  
2 Use f4 key for referencing  
3 When using the Rept formula use “l” which is L in small caps and then type the number of times you want to rept.  
4 can combine 2 rept commands by shrinking the column width than doing long formulae  
5 Rept formula is a powerful tool and can used to show both negative and positive values For e.g. profit and loss A/C can be shown in rept formula  
another use of rept formula is to use it for confidence interval with mean in the middle.  
6 To make Vlook up to look up values in the right side: copy and paste the columns next to each other and perform vlook up. it is easy and there is no need for another formula For eg;Name and Phone number in two columns  
Vlook up will look up the name and will return the phone number. If we have phone number and want the name then we need to write a match and index, Instead if you copy name and phone next to each other then for the phone number vlook up will return the name. That is easy.  
I am feeling sleepy after this. More later

**Tips for Formula speeding up by Jan Karel Pieterse**

Nice subject!  
My 2 cts.

A. Formulas

1\. If you need to turn off recalc, it is time for a redesign.  
2\. Avoid array formulas (this includes sumproduct), instead use helper columns which have intermediate results. Easier to debug and very often much faster  
3\. Avoid VLOOKUP, especially on large tables, instead, use INDEX combined with MATCH, where you use a helper column for the match so you only ask Excel to search your table once for each row instead of once for each column in a row.  
4\. Do your summarizing with Pivot tables instead of functions  
5\. Be prudent with range names. Use them sparingly and limit them to constants. Formulas with range names are harder to audit because of the extra layer between your formula and the grid.  
6\. Visit www.decisionmodels.com, the site contains a wealth of information on recalculation in Excel.

**Tips for Formula speeding up by Jason**

I work with files that use a lot of data tables. In order to avoid excessive delays I will turn off the automatic setting under calculation options and select automatic except for data tables. In addition, I have noticed that excessive conditional formatting can really bog down the spreadsheet as well. Thus, I try to limit and consolidate formatting needs where I can.

[About Jason](http://www.gunnisonenergy.com/)

**Tips for Formula speeding up by Jon**

Use as many array formulas as possible on the staging worksheet. That way the Excel or UDF functions are called as few times as possible.

[About Jon](http://www.spreadsheetbudget.com/)

**Tips for Formula speeding up by Kate Phelps**

The way I speed up my workbooks is by pasting values (instead of keeping the formulas) once the data is no longer going to be updated. For example, I have files that track activity that has happened each quarter. The sheets often have 35,000 rows of data and formulas in each of the 10 columns (for each row). As soon as the quarter is over, I paste the values over the formulas since things won’t be changing any longer.

[About Kate Phelps](http://www.taylorreportingsolutions.com/)

**Tips for Formula speeding up by Kien Leong**

Perform paste down macros for all calculations. These use dynamic named ranges to select a row of formulas, then paste them in against a table of data. This way you can calculate formulas against thousands of rows and then copy-paste special with values. Removing live formulas seriously reduces calculations times for workbooks with 1K+ rows of data.

Perform Sorts and then use range formula (OFFSET, INDEX) to select a subset of rows, rather than using conditional formula on whole columns. SUMIF, COUNTIF, array formulas etc are very slow on big columns of data. Sorting can filter a table to records that share the same attribute and range formulas can pick up row numbers to only select a sorted block of values.

[About Kien Leong](http://www.linkedin.com/in/kienleong)

**Tips for Formula speeding up by Konrad**

Keep use of array formulas to a minimum. Keep calculations running sequentially from top left to bottom right when possible. Break up larger internal formula calculations into smaller bites (more columns etc). Look for formula parts shared by formulas. Use offset to keep lookup formulae to the minimum required ranges. Use built-in formulas whenever possible.

**Tips for Formula speeding up by Krishna Khemraj**

I work with large workbooks with extensive formula throughout. I used to use VBA to paste in formulas then I would value them out, but my clients couldn’t easily modify the formulas if they desired a change. Since then I would place a formula row at the top of the data and use VBA to copy that row and paste formulas below, calculate then value them out. The client can then modify the initial row of data to suit their needs. This greatly improved save and load times.

[About Krishna Khemraj](http://facebook.com/SuperKrishna)

**Tips for Formula speeding up by Larry**

When I have thousands of rows of equations (all the same), I convert all but the top row to values. Then I create a macro that spreads the equations from the top row down to all the necessary rows and makes them values again. Saves a lot of excel recalculating.

**Tips for Formula speeding up by Marco**

use iferror instead of if(iserror(…

**Tips for Formula speeding up by Mark**

I have Excel 2003 files of 45 Mb plus that track daily shift performance that have lots of vlookups, conditional formats, data validation, event triggered VBA. To speed things up I cheat! The historic data is copy-special pasted over itself to turn it into values only – so when auto updates happen they only process the “current data”.

**Tips for Formula speeding up by Mark W.**

One thing I do where there are multiple columns with formulas is this:  
Once my formulas have all calculated and I know the the results won’t change, I copy the formula and put it at the top of my spreadsheet. Then put a red top & bottom border around the formula so I can easily find them.

I then copy the data set full of formulas and re-paste it on itself (keyboard shortcut – copy/file/paste special/values). The spreadsheet calculates much faster.

When I need to update the data I just copy the row of formulas and paste them over the data rows.

**Tips for Formula speeding up by Matthew Strehl**

save as .xlsb to speed up opening time/decrease file size. also changed =if(iserror) to =iferror to speed up processing. changed from vlookups to pivot table/=getpivotdata format to speed up processing

**Tips for Formula speeding up by Michelle Forrest**

a) Delete/or clear contents on all blank cells under & to the right of my data. b) On old inherited files, clear out old range names. c) use specific cell references for vlookups (rather than entire columns) d) remove as many calc’s as possible (copy-paste-special values) e) keep pivot tables in separate file from data file f)Stopped using arrays & sumproduct() completely 🙁 g) now considering upgrading to 64 bit OS & 64 bit MSOffice 2010 (currently using 32 bit MSExcel 2010 on XP)

**Tips for Formula speeding up by Mohit Jaiswal**

1\. Define name of ranges and Use it in the Formula if data is flowing from database.  
2\. Remove the unused name or name resulted any error or scope outside the workbook.( Formulas—>name manager)

**Tips for Formula speeding up by Ramesh**

Reduce Images / Shapes that reduces the performance

**Tips for Formula speeding up by Rubén Huapaya**

Linking all my dashboards with pivot tables and queries for to update complex data with one click.

**Tips for Formula speeding up by Steve**

My array formulas used to reference an entire row or column (e.g. A:A or 1:1), and I’m pretty sure that slowed down the sheet. I shrunk the reference to go through, say, row 5000, and it appears to have helped the problem.

**Tips for Formula speeding up by Tayyab Hussain**

No doubt excel is a powerful analytical tool but most of the people do not plan before designing there spreadsheet. One should plan the Start and End in mind, and the assumption that the spreadsheet will never be used again should kept out of mind. Perhaps this is might be the number one rule. Spreadsheets are about giving correct information to the user, not possible erroneous information that looks good.

Excel Best Practices & Design

Formatting  
Your spreadsheet should be easy to read and follow. Most of the users spend about 30%, or more, of their time formatting their spreadsheets. Use the cell format of Text if really necessary. Any cell containing a formula, that is referencing a Text formatted cell, will also become formatted as Text. This format is not usually needed but very much used. If you apply a number format to specific cells avoid applying the format to the entire column. If you do, Excel will assume you are using these cells.

Layout  
Try and ensure all related raw data is on one Worksheet and in one workbook. When putting in headings bold the font. This will help Excel recognize them as headings when you use one of its functions. When putting data into the data area of your spreadsheet try to avoid blank rows and columns. This is because a lot of Excels built-in features will assume a blank row or column is the end of your data. Use real dates for headings and format them appropriately. If you want the names of the months as headings type them in as 1/1/2001, 1/2/2001, 1/3/2001 etc then format them as “mmmm”. This is a very simple procedure that is all too often overlooked by many. Don’t put in one cell what could go in more than one cell, i.e. the names of 100 people to put into your spreadsheet, don’t put their full name in one cell. Instead, put the First name in one cell and their surname in the next cell to the right.

Formulas  
This is the biggest part of any spreadsheet! Without them you really only have a document. Excel has over 300 built in Functions (with all add-ins installed), but chances are you will only use a handful of these.  
The usual practice in regards to formulae in Excel is the referencing of entire columns, this is a big mistake! This forces Excel to look through potentially millions, of cells which it need not be concerned with at all. One of the very best ways to overcome this is to familiarize you with the use of dynamic named ranges.

Speeding up Re-calculations  
A common problem with poorly designed spreadsheets is that they become painfully slow in recalculating. Some people will suggest that a solution to this problem is putting a calculation into Manual via Tools>Options>Calculations. A spreadsheet is all about formulas and calculations and the results that they produce. If you are running a spreadsheet in manual calculation mode, sooner or later you will read some information off your spreadsheet which will not have been updated, this means using F9 on regular intervals, which can cause bad results, because Pressing F9 can be overlooked.  
Arrays, Sumproduct (used for multiple condition, summing or counting), UDFs, Volatile Functions and Lookup functions, can slow down the recalculations of spreadsheet.

Array Formulas  
The biggest problem with array formulas is that they look efficient. An Array must loop through each and every cell they reference (one at a time) and check them off against a criteria. Arrays are best suited to being used on single cells or referencing only small ranges. A possible alternative are the Database functions. Another very good alternative which is mostly overlooked is the Pivot tables. Pivot Tables can be frightening at the first site but it is the most powerful feature of Excel.

UDF (User Defined Functions)  
These are written in VBA and can be used the same way as built in functions can be, but unfortunately, no matter how good the UDF is written the, it will perform at the same speed as one of Excel’s built-in functions, even if it would be necessary to use several nested functions to get the same result. UDFs should only be used if an Excel function is not available

Volatile Functions.  
Volatile functions are simple functions that will recalculate each time a change of data occurs in any cell on any worksheet. Most functions which are non-Volatile will only recalculate if a cell that they are referencing has changed. Some of the volatile functions are NOW(), TODAY(), OFFSET(), CELL(),INDIRECT(), ROWS(), COLUMNS() . If you are using the result of these functions frequently throughout your spreadsheet, avoid nesting these functions within other functions to get the desired result especially in array formulas and UDF’s. Simply use the volatile function into a single cell on your spreadsheet and reference that cell from within other functions.

Lookup Functions  
The Famous Vlookup(). Excel is very rich in lookup functions. These functions can be used to extract data from just about any table of data. The biggest mistake made by most, is the forcing of Excel to look in thousands, if not millions of cells superfluously. The other mistake is that the lookup functions are told to find an exact match. This means that Excel will need to check all cells until it finds an exact match. If possible, always use True for VLOOKUP and HLOOKUP. So, whenever possible, sort your data appropriately. Sorting the lookup columns is the single best way to speed up lookup functions. Another Bad practice is the double use of the Lookup Function nested within one of Excels Information functions. Like =if(isna(vlookup(cell ref,Range,2,false))=true, “Please check”, (vlookup(cell ref,Range,2,false)))  
This is used to prevent the #N/A error from displaying when no match can be found. This forces Excel to use the VLOOKUP twice. As you can imagine, this doubles the number of Lookup functions used. The best approach is to live with the #N/A, or hide it via CONDITIONAL FORMATTING.

LAST WORDS  
Lean to us e database functions. They are very easy to use and are often much faster than their Lookup & Reference counterpart.  
Microsoft Tips  
Organize your worksheets vertically. Use only one or two screens of columns, but as many rows as possible. A strict vertical scheme promotes a clearer flow of calculation.

When possible, a formula should refer only to the cells above it. As a result, your calculations should proceed strictly downward, from raw data at the top to final calculations at the bottom.

If your formulas require a large amount of raw data, you might want to move the data to a separate worksheet and link the data to the sheet containing the formulas.

Formulas should be as simple as possible to prevent any unnecessary calculations. If you use constants in a formula, calculate the constants before entering them into the formula, rather than having Microsoft Excel calculate them during each recalculation cycle.

Reduce, or eliminate, the use of data tables in your spreadsheet or set data table calculation to manual.

If you only need a few cells to be recalculated, replace the equal signs (=) of the cells you want to be recalculated. This is only an improvement if you are calculating a very small percentage of the formulas on your worksheet.

**Tips for Formula speeding up by Umesh**

By changing formulas to manual from automatic

**Tips for Formula speeding up by Vinod**

If my model has lot of formulas in the data sheets and working on the summary tab – then I will Keep my formula calculation option as “Manual”.

If you are doing calculation in one sheet Pls use Shift+F9 (to get refresh the formula in the active sheet).

F9 – to refresh the complete workbook.

**Tips for Formula speeding up by wintermute**

1\. arrange source data before linking to dashboard / report with macros and other aggregate functions  
2\. separate results into several charts & link list boxes to just one calculation  
3\. avoid volatile and array functions

VBA / Macros Optimization Tips
------------------------------

**Tips for VBA optimization by Alok Joshi**

First. I find your site awesome.  
Well I speedup my VBA code by setting  
Application.ScreenUpdating to false  
Application.EnableEvents to false and  
Application.Calculation to xlCalculateManual  
and then setting those values back to whatever they were before I made the changes. I do EnableEvents when I use a Event Driven actions and I know that I do not need them during those calculation/operations.

**Tips for VBA optimization by Bruce Mcpherson**

Two approaches.  
a) Profile both worksheet calculations, and if necessary VBA code using the profilers downloadable here to identify and report on slower performing calculations and code.  
http://ramblings.mcpher.com/Home/excelquirks/optimizationlink

b) in VBA, always abstract data from the worksheet and work on the abstracted object model.

http://ramblings.mcpher.com/Home/excelquirks/classeslink/data-manipulation-classes/howtocdataset

[About Bruce Mcpherson](http://ramblings.mcpher.com/)

**Tips for VBA optimization by David KABUTE**

We design macros which we run across the many worksheets. If formulas are generated, we do final macros to save the formula results as numbers. This retains our worksheets as light.

Regards

David

**Tips for VBA optimization by Debbie**

1\. Disable screen updating in VBA.  
2\. Set calculation to Manual, use Shift-F9 to calculate each sheet as needed. Is a pain, but I have found it is a major time saver on a couple of my largest files.

[About Debbie](http://happytrailstlh.com/)

**Tips for VBA optimization by Eloy Caballero**

Recently, I’ve been busy with a project to emulate software for seeking secret messages in classical texts using EXCEL. I need to write hundreds of thousands of single letters each in a cell, and I’ve found it faster to operate internally VBA and finally write as a block in a declared range, rather than doing it via a loop writing individually each cell.  
I haven’t measured times, but I would venture it’s a lot faster.

[About Eloy Caballero](http://ideasexcel.com/)
 | [Excel file with this example](https://img.chandoo.org/optimize/ArtificialTextGeneration.xlsm)

**Tips for VBA optimization by Jayshreee**

Not sure if this is what you are looking for – but here is what I do to speed up my excel workbook –

Along with all standard keyboard shortcuts – I have been creating a lot of Macros. I ran out of shortcut keys I can use with Ctrl – so now started using Ctrl+Shift to create my own shortcuts. (May be I don’t know any existing shortcut- and tried to reinvent the wheel for some of them)

I have Macros for – Green/Yellow/Pink Highlight – Merge + Wrap Text – Enter TB Link (Entering specific formula to cell) – Single Underline Cell

Just thought to share this as you asked for – considering all the entries I have seen from others on your website, I am just a newbie in the Excel World.

[About Jayshreee](http://www.linkedin.com/pub/jayshree-bhakta/7/989/38a)

**Tips for VBA optimization by John Hackwood**

VBA: One powerful one is to use “Destination:” in your copying and pasting which bypasses the clipboard. Or if only values are wanted simply assign values.

So instead of:  
Sheet1.Range(“A1:A100”).Copy  
Sheet2.Range(“B1”).pasteSpecial  
Application.CutCopyMode=False  
‘Use:  
Sheet1.Range(“A1:A100”).Copy Destination:=Sheet2.Range(“B1”)

If values only required ditch copy and simply assign values from one place to another:  
Sheet2.Range(“B1:B200”).Value= Sheet1.Range(“A1:A100”).Value

[About John Hackwood](http://au.linkedin.com/pub/john-hackwood/14/31a/7b)

**Tips for VBA optimization by Manoj Kapashi**

Avoid loops like the plague while writing macros, unless absolutely necessary.

**Tips for VBA optimization by Mark Heptinstall**

A tip which is well documented when searching for ways to improve performance when using VBA/Macros is to turn off screen updating, calculations and setting PivotTables to manual update.  
Most of the procedures I create in VBA start with:  
With Application  
.ScreenUpdating = False  
.Calculation = xlCalculationManual  
End With

And will end with the following statements:  
With Application  
.ScreenUpdating = True  
.Calculation = xlCalculationAutomatic  
End With

If PivotTables are involved then I include the following in procedure:  
With PivotTable  
.ManualUpdate = True  
End With

And will end with the following statement  
With PivotTable  
.ManualUpdate = False  
End With

**Tips for VBA optimization by Martin**

Planning carefully before coding.  
Passing the entire SQL query into the code, leaving no connection on sheets.

[About Martin](http://ar.linkedin.com/in/martincanosa)

**Tips for VBA optimization by Matt Nuttall**

This is a very general tip, but when using VBA — AVOID LOOPS!

Use the “Find” and “Search” methods rather than looping through cells. Loops work quick when you are using less than 100, or sometimes less than 1000 cells — but start adding more and you will be in for a waiting game.

[About Matt Nuttall](http://www.linkedin.com/in/matthewnuttall)

**Tips for VBA optimization by Ray Martin**

If you have VBA code that writes updates to the screen, this slows down the code (I/O is slow). If you have a lot of screen writes, the code can be painfully slow. You can turn off screen writes while your code is running and then do one massive screen write at the end of the macro. Up at the beginning of your code, maybe just after you declare variables, add the line “Application.ScreenUpdating = False”. At the end of your code, you need to turn screen writes back on so add the line “Application.ScreenUpdating = True” just before you exit the macro.

If you have a load of screen writes, the speed difference can be dramatic.

**Tips for VBA optimization by Stef@n**

Hey Chandoo

VBA-speed

at the beginning of the macro  
…  
Application.ScreenUpdating = False  
Application.Calculation = xlCalculationManual

at the end of the macro  
….  
Application.ScreenUpdating = True  
Application.Calculation = xlCalculationAutomatic  
Call Calculate  
end sub

regards Stef@n

**Tips for VBA optimization by Victor Andrade**

With Application.ScreenUpdating = False / True  
With Application.Calculation = xl.CalculationManual  
Using the statement with wherever is possible  
and release memory when the objects variable are not used anymore

[About Victor Andrade](http://mx.linkedin.com/in/vmandrade)

Everything Else
---------------

**Tips for Everything else by Aarthi**

1\. I list out the things required and will imagine the plan of my task.  
2\. I try to minimize the calculation for speedy calculation. So, I am trying to learn new formulas.  
3\. In each and every step, I consider about the others who use that excel. So that I can make the workbook user-friendly to others also.

**Tips for Everything else by Benoy**

I close MS Outlook when working on heavy files. Basically I exit all the programs that will eat into process speed. It helps to an extent.  
Also, I try and minimize cross linking of files.

[About Benoy](http://in.linkedin.com/pub/benoy-paul-jose/18/a6/388)

**Tips for Everything else by Bonnie**

Power Pivot from Microsoft. This looks like it would solve the problem of large amounts of data.

http://office.microsoft.com/en-us/excel/powerpivot-for-microsoft-excel-2010-FX101961857.aspx

**Tips for Everything else by Danielle**

I wrote a blog article on my favorite tips here: http://www.plumsolutions.com.au/articles/excel-model-file-size-getting-out-hand

[About Danielle](http://www.plumsolutions.com.au/)

**Tips for Everything else by Dominic**

I haven’t done this myself, but a consultant we used sped up our dashboard by writing VBA code which “dumped” a lot of the back data after it was loaded. This greatly reduced the amount of data stored, thus reducing file size, thus sped up the dashboard.

**Tips for Everything else by Fred**

1\. Many database download from whatever system may include blank data occupying cells from the last row of data to the last possible row Excel can provide. So I would look at the data set and delete those rows (or columns, but I see more blank rows than blank columns).

2\. Too many pivot tables: I’d ask the person who create multiple pivot table on the same workbook to see if there is a need to maintain those pivot tables. If the answer is  
a) no need to maintain: I’d delete.  
b) need to maintain but may not be in a pivot table. I’d convert pivot tables into just text/data (thereby removing the pivot function) table.

3\. Try to reduce the number of worksheet. I found out that the size of a workbook (I can’t prove it but it’s my general observation) would expand if there are more worksheets.

[About Fred](http://www.linkedin.com/pub/sheng-frederick-lim/1/650/742)

**Tips for Everything else by Glenn Reed**

Standardize, standardize, standardize! The more you are “boring” the quicker it will be to set up work with (and have others) use your formats!  
Items to standardize:  
– Font  
– Color scheme  
– Headers  
\-Colors for “input” (font color or fill color)  
\-tab color scheme (answers, data input, analytics)  
– Color for “answer/solution”  
– Lead with a recap page (easy and quick to find the solution)  
\-Configure to print (courtesy to others – if you need to print an answer – set up the parameters before sharing)

**Tips for Everything else by govind soni**

by using single sheet in work book & using alt,clt short key

**Tips for Everything else by Heidi B**

Oddly enough, the best thing I have found to speed up Excel is to completely disconnect internet access for my computer. I don’t know why, but Excel is unbelievably slow when I am otherwise online, and speeds up immediately when I disconnect. I’d love it if someone could help me understand why this is the case.

**Tips for Everything else by Jim**

Even though I’ve been using Excel for quite some time, I learn and love your site. You teach me the impossible. The simplest way I at least save data space is to save it in .xlsb format. I read somewhere that even a .xlsx is basically a number of zipped or compressed files that need to open and save. Not sure about that, but know the binary file is much smaller in size than the others. Not sure if macro enabled workbooks will save as binary. Thanks. Always look forward to what the next email will hold…scary sometimes. -Jim

**Tips for Everything else by kamran butt**

I’m not an expert but try to keep the dashboard as much simple as possible.

**Tips for Everything else by krunal**

I use access to have the main table and from that table we create different dashboards and reports and pivots to analyze data

**Tips for Everything else by Louise Nickerson**

I break any links to the spreadsheet that I am not using.

**Tips for Everything else by Marcus**

Try to avoid adding formatting over an area larger than you need, I’ve found that if you format a whole row, column or worksheet it can slow the workbook down and create large files

**Tips for Everything else by Misca**

Dumping out as much unnecessary data as I possibly can, converting formulas to values whenever possible and making sure the empty space on each sheet is empty.

Also I’m using lots of pivot tables on my spreadsheets so I’m trying to use as few pivot caches as possible and trying to use external data sources for my PTs whenever possible (or deleting the original data once the PT is created).

**Tips for Everything else by Nagessh Volety**

Most of the time, to increase speed & size. what I do is  
1) simply copy the used data cells to a new sheet, (by selecting from A1 to the end of the data cell),  
2) if there are too much of borders decorated around more cells, then try replacing these borders with minimum dotted lines (just to highlight the difference)  
3) Avoid using too many fonts in the sheet  
4) Cut short complicated formulas or multiple linked formulas,

[About Nagessh Volety](http://in.linkedin.com/pub/nagesh-volety/30/183/0)

**Tips for Everything else by Pankaj Gupta**

I have Liked based models. I try to make my links as small as possible. I try to put all the sheets in one file and interlink them so that they take less storage space and react much speedy in working.

**Tips for Everything else by Pete**

Create a view in SQL and set a scheduled task to run to generate the view before you update the dashboard.

Do we get some SWAG for sharing??

**Tips for Everything else by Ron007**

Here are some tips I’ve collected, although they repeat some points they provide different viewpoints:

10 WAYS TO IMPROVE EXCEL PERFORMANCE  
http://www.techrepublic.com/blog/10things/10-ways-to-improve-excel-performance/2842?tag=nl.e072

EXCEL 2010 PERFORMANCE: IMPROVING CALCULATION PERFORMANCE  
http://msdn.microsoft.com/library/ff700515.aspx

CLEAN UP YOUR MACRO LIST  
http://excelribbon.tips.net/T008037\_Clean\_Up\_Your\_Macro\_List.html

OPTIMIZE MACROS – VBA CODE CLEANER  
http://www.appspro.com/Utilities/CodeCleaner.htm

**Tips for Everything else by Subash TPM**

I recently happened to work on a report which has 1.5 lac rows of data in 16 columns. The requirement was that in the main report as soon as a change is made say for a dept or month the numbers should accordingly change. I tried most known formulas like Sumifs, Sumproduct, Vlookup, Index and Match. How ever the calculation time these formulae took was much more compared to one formulae that I felt was the fastest in terms of calculation. That was Getpivot data.  
I basically used the “show all report filter” option in the Pivot options to generate summary data in around 500 tabs using the my base data. Then I used get pivot data formula in my report file. Though the file size was a bit huge still my formula get calculated almost instantaneously.

Also one strange thing I noticed in one other file of mine was that when I press Ctrl+end the last cell it stopped was in some 2 lac row or something, how ever the data was only in some 10k rows. I used clear all option from the last cell from where I have data to the last cell it went when I pressed Ctrl+end .By doing this my file size came down from 12 MB to some 600kb.. 🙂

Hope this helps someone.

**Tips for Everything else by Terry**

Hi,  
Great topic (as usual).  
One thing I like to do is minimize links between workbooks. Instead of using live links to import data I like to use import and export sheets. These are identical sheets on the origin workbook (for export) and the receiving workbook (for import). Values are calculated in the origin workbook and pasted to the receiver as values only.  
This gets rid of messy links and keeps spreadsheets smaller and tidier.  
One thing to be careful of is that if one changes the other has to change so they stay identical.  
Thank you again for your excellent material.

**Tips for Everything else by teth**

That’s my problem too I would love to hear what others say. For  
me closing other spread sheets and unnecessary opened tasks in your PC helps.

**Tips for Everything else by Timothy Sutherland**

– remove external data links – better to import a large data table – or use an SQL statement if possible.  
– especially don’t use INDIRECT to anything external

**Tips for Everything else by Tyler Bushnell**

1) Limit color use in Excel  
2) Hide gridlines (with “View Gridlines” function) rather than color the cells white  
3) Create smart Vlookup formulas (Arrange data in the lookup tab so the range is as small as possible – 3 columns vs. 20 columns)  
4) Link multiple tabs using the same data to one data tab. Ie.. Dates, headers, etc…the links will eliminate having to update each tab.  
5) Extract only the needed data from the database (10 columns of needed data vs. 40 columns available data.  
6) If the Database report does not allow the user to choose what is exported, export the data, organized the needed data into a consolidated area (rows x columns), Copy & paste into a new tab and delete the original tab. Many people leave the original data in the file, which slows down the file and adds to the file size.

**Tips for Everything else by Umang**

1) Don’t create different pivots from same data. Copy the old and slice into the new one.

2) Go to special –> Check Last known cell and delete unnecessary data and formulae.

3) Set Calculation option to manual. Do all the dirty work and finally make it automatic and go for a coffee break 🙂

4) Use excel tables as far as possible.

**Tips for Everything else by Uwe**

To speed up workbooks, the reduction of formulas within the workbooks should be the main aim.  
If the data is being pulled from an external database into the worksheet:  
– Do not start calculations on that data in the workbook which could have been done before, e.g. using formulas to split up the dates like mm-dd-yyyy, weekdays a.s.o..  
– Reduce the amount of sources if possible and combine the data in one sheet  
– Use name ranges  
– Split up the workbooks for different purposes (Dashboard for CEO, Dashboard for CFO a.s.o..).  
– Try to use only one format for importing (I prefer \*.csv or \*.txt)  
– If you connect your Workbook directly to a SQL database, make sure the connection is high-speed

If the modeling is too complex, think of using a a (semi-) professional data ETL tool in between or use the additional add-ons like PALO or Pentaho available as open source to rise the power of multidimensional databases for your BI-tools.

This can and will save time in calculating for the necessary functions of the workbooks. Stay with KISS (Keep it simple, stupid).

[About Uwe](http://www.ukconsulting.info/)

**Tips for Everything else by Vasim (Indian)**

I use name range for multiple pivots, basically the offset function, this not only speeds up my calculation but also reduces the size of the workbook.

More on Excel Optimization & Speeding up:
-----------------------------------------

Read these articles too,

*   [Optimization & Speeding-up Tips for Excel Formulas](http://chandoo.org/wp/2012/03/20/optimize-speedup-excel-formulas/ "Speed up your Excel Formulas [Speedy Spreadsheet Week]")
    
*   [Charting & Formatting Tips to Optimize & Speed up Excel](http://chandoo.org/wp/2012/03/21/excel-optimization-charting-formatting-tips/ "Speeding up & Optimizing Excel – Tips for Charting & Formatting [Speedy Spreadsheet Week]")
    
*   [Optimization Tips & Techniques for Excel VBA & Macros](http://chandoo.org/wp/2012/03/22/vba-macros-optimization-techniques/ "Optimization Tips & Techniques for Excel VBA & Macros [Speedy Spreasheet Week]")
    
*   [Excel Optimization tips submitted by Experts](http://chandoo.org/wp/2012/03/26/excel-speedup-optimization-tips-by-experts/ "Excel Speedup & Optimization Tips by Experts [Speedy Spreadsheet Week]")
    
*   **Excel Optimization tips submitted by our readers**

Want to become better in Excel? Join Chandoo.org courses
--------------------------------------------------------

|     |     |
| --- | --- |
| ### Excel School<br><br>Learn Excel from basics to advanced level. Create awesome reports, dashboards & workbooks.<br><br>**[Click here to know more](http://chandoo.org/wp/excel-school/)<br>** | ### VBA Classes<br><br>Learn VBA & Macros step-by-step. Build complex workbooks, automate boring tasks and do awesome stuff.<br><br>**[Click here to know more](http://chandoo.org/wp/vba-classes/)<br>** |

How do you speed-up Excel? Share your tips
------------------------------------------

Between these 75 ideas & and previously written articles, we have covered a lot of optimization & speeding-up techniques. What are your favorite methods? How do you optimize & deal with sluggish workbooks? **Please share your ideas & tips with us using comments.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [37 Comments](https://chandoo.org/wp/75-excel-speeding-up-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/75-excel-speeding-up-tips/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel optimization](https://chandoo.org/wp/tag/excel-optimization/)
    , [formatting](https://chandoo.org/wp/tag/formatting/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [ssw](https://chandoo.org/wp/tag/ssw/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousExcel Speedup & Optimization Tips by Experts \[Speedy Spreadsheet Week\]](https://chandoo.org/wp/excel-speedup-optimization-tips-by-experts/)

[NextFormula Forensics 016. Suzannes DJIA AverageNext](https://chandoo.org/wp/formula-forensics-016-suzannes-djia-average/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/75-excel-speeding-up-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/75-excel-speeding-up-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/75-excel-speeding-up-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ