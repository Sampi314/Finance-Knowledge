# Generic Macros File (Colouring and Copy to Right)

**Source:** https://edbodmer.com/excel-utilities-and-backpack/generic-macros-file

---

This page of my website describes how to use a file with a set of macros that allow you to efficiently and effectively colour you cells in an excel spreadsheet and how to quickly copy cells to the right.  The colouring techniques and the copy to the right macro comes from an excel file I have badly named file that I call generic macros. This file is meant to be your partner while constructing financial models and I generally keep this file open while I am working on models. This file includes a macro to copy to the right SHIFT, CNTL, R and it has macro name CNTL, ALT, C where you can colour cells depending on which sheet the numbers come from. To run these and other macros, all you have to do is have the generic macros file open because you run macros from other open files (e.g. say you are in mybook.xlsm, you can open generic macros and run any of the macros in your sheet). I don’t like to take change the way your excel and override short-cut keys or other things that you may want to use elsewhere. Instead, I think it is much better to just open the generic macros sheet and enable macros. Then the SHIFT, CNTL, C and the SHIFT, CNTL, R should work just fine. The generic macro file also has a lot of other macros that may be useful are included in the file that is available by clicking on the button below.  The second file below the macro file is a file named generic macro test that allows you to test the file.

.

**[Generic Macro File that Allows you to Copy to the Right (Shift, CNTL, R) and to Colour and Format Sheets (CNTL, ALT, C)](https://edbodmer.com/wp-content/uploads/2024/04/Generic-Macros.xlsm)
**

.

For every single one of the more than 1000 excel files on this website I have not put any passwords on the macros or functions. This means you can look at the code and try to improve it yourself. (If you have some good improvements I would really like it if you send me your work). You can also copy the macros from this file into your file or your personal workbook if you do not want to open generic macros every time you open your file.

**[Instructions for Downloading Files with Macros](https://edbodmer.com/downloading-files-with-macros/)
**

.

Using the Generic Macros File to Colour Cells
---------------------------------------------

I became irritated when I was going through some technical issues about circular references with a young person who seems to be very proud of the way he colours his spreadsheet.  I certainly do not claim to be a financial modelling artist.  But this seems to be important to many people. Because I get so irritated by people who see to think colouring is the most important skill in financial modelling; who do not use colouring to help structuring the model; and, who do not use colouring to make the model transparent I have made a colouring macro in the generic macro sheet.

To illustrate how you can use generic macros to stop wasting time with all of the silly spreadsheet art, I have made a few screen shots below do demonstrate how it works.  The first screen shot shows the starting point before the CNTL, ALT, C is used from the generic macro workbook.

.

![](https://edbodmer.com/wp-content/uploads/2018/05/Generic-Macros-Before-2.jpg)

.

To use the flexible colouring options in the generic macro file, open the generic file along with the file you are working on.  The press CNTL, ALT, C and a menu something like the one illustrated on the screenshot below should appear.  Note that you can use this user form to run the table of contents and do other thinks like removing links to the current sheet.  To implement the colouring macros, press the red button at the top right of the form.

![](https://edbodmer.com/wp-content/uploads/2018/05/generic-macros-1.jpg)

I hope that most of the options on the options on this menu are self-explanatory.  The key behind this process is that you can run the CNTL, ALT, C  menu as many times as you like and press the red button to re-colour. In the left column, you can select different options for colouring direct inputs. (5\*3 is not an input). The next column to the right allows you to make similar colouring selections that will apply to any item that is in the first column.  If you do not use Column A for structuring your sheet, then make sure the check box next to the “Colour Column A” is not checked.  Continuing to move to the right, the next set of inputs allows you to use different conditional options for TRUE and FALSE switches in your sheet.  Finally the column to the right allows you to use different options for numbers that come from another sheet.  When colouring cells that come from another sheet, you can use the colour of the sheet in the sheet name or you can colour anything that comes from another sheet with a green, red or blue colour.

If you want to be more flexible in colouring various cells in your sheet, you can use the flexible colouring options that are at the bottom or each section.  These options are called the flexible colouring options.  If you want to modify the flexible colouring options that are at the bottom of each section, you should go to the fist page of the generic macro sheet.  On this sheet you can use the paint brush or copy paste special as formats to put your own formats in the sheet. After making your own colouring options, you should press the button on the generic macro page that is called Initialisation.  The screenshot below illustrates the page in the generic macro sheet where you can change the colouring options.

![](https://edbodmer.com/wp-content/uploads/2018/05/generic-macros-2.jpg)

After you have pressed the red button and colour the sheets, the page in the initial screenshot should look like the screen shot below.  Note that you can keep pressing the colour sheet after you are working on your model.

.

![](https://edbodmer.com/wp-content/uploads/2018/05/Generic-Macros-After-1.jpg)

.

Using Generic Macros to Copy to the Right
-----------------------------------------

As with the colouring macro, I have tried to make the copy to the right macro flexible. So, if you have the generic macro sheet open, and if you have a row of numbers somewhere, you can press SHIFT, CNTL, R and the numbers will copy to the right for as long as your row of numbers. To see this, go to a blank sheet and press the number one somewhere near the top (for example in cell D4.  Then press either ALT, E, I, S or ALT, or ALT, H, FI, S. (In French it is a bit more complicated). You will get a little menu like the following:

![](https://edbodmer.com/wp-content/uploads/2018/08/EIS.jpg)

Then press the number 9 as the stop value and you will have a row of numbers.  Just below the row of numbers (i.e. below the number 1), enter a few more numbers.  I put in 100, 200 and then used the ALT, = short cut to add the numbers together as shown on the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/08/Shift-Cntl-R-1.jpg)

Next, select the three numbers (the 100, 200 and 300) and press SHIFT, CNTL, R.  The numbers should copy to the right as shown in the screenshot below.  If this is not working, then you probably either do not have generic macros.xls open or the file is not enabled.

![](https://edbodmer.com/wp-content/uploads/2018/08/Shift-Cntl-R-2.jpg)

I have also tried to add an undo option to the Shift, CNLT, R macro which you can access with SHIFT, CNLT, S. Test the SHIFT,CNTL,S you can enter some other formula in the third row that currently contains 300.  Then press SHIFT,CNTL,S.  You should get the original number back.

You can also adjust the SHIFT, CNTL, R to look up to different rows and test other things. To adjust the generic macro file, you go to the first sheet of the file and change the parameters. After you change the parameters however you must run the implement macros macro.

If you want to put the SHIFT,CNTL, R macro in your workbook or in your personal workbook, I suggest copying the entire module where the macro is located in the generic macros.

Videos that Illustrate use of Generic Macros File
-------------------------------------------------

The first video below demonstrates how to use the Generic Macros file that you must download to colour your sheet efficiently.

The video below is long and about carrying charges, but I have used this video to introduce features of the Generic Macros file including screen colouring with CNTL,ALT,C and copying to the right with SHIFT,CNTL,R.

Miscellaneous Other Subroutines in Generic Macros
-------------------------------------------------

The generic macros file and a workbook named fm.xls includes a lot of different functions and macros. Some of the more important macros that create table of contents and remove the current sheet name from formulas and finds the links are shown below. As explained above, none of these macros have any irritating passwords and you can copy the macros into your files. The fm.xlsm file below has some of the older macros that I made a few years ago. The example calander shows how you can create a macro that puts a password in a file and uses MATCH and INDEX over and over again with conditional formatting to make a calendar in excel (I doubt very much that you will use this).

Sub x\_replace\_sheet\_name() Takes away current name of sheet in formulas  
Sub x\_Delete\_cols() Deletes columns that are blank  
Sub x\_Delete\_rows() Deletes rows that are blank  
Sub x\_fix\_decimal() Fixes Problems with auto formatting  
Sub x\_find\_rows() Finds number of rows in sheet  
Sub x\_find\_cols() Finds number of cols in sheet  
Sub x\_colourTitles() Colours titles for the first column  
Sub x\_Create\_Table\_of\_Contents\_From\_Sheet\_Names() Creates Contents with links  
Sub x\_find\_externl\_links() Find External Links  
Sub x\_hide\_sheets\_after() Hide Sheets after Given Name

Table of Contents Example.xlsm

fm.xls

Example Calendar.xlsm

Functions in Generic Macros
---------------------------

In addition to macros, I put a bunch of user defined functions in the generic macros file. These macros do things like find the sheet name or the file name. They can also show who saved the file last and make a payback function. Unlike the subroutine macros, you cannot just have the file open the functions. Instead, you must find the functions and then copy them into your file.

Function sheet\_name(cell)  
Function sum\_labels(series)  
Function File\_name() As Variant  
Function MyUDF(LastSaved1 As Boolean) As Double  
Function Last\_save\_by() As Variant  
Function LastSaved() As String  
Function lookup\_NA(lookup\_value, test\_array, result\_array)  
Function match\_adj(lookup\_value, lookup\_array)  
Function payback(series)  
Function dpayback(d\_rate, series)  
Function period\_of\_year(period, timing)  
Function show\_formula(cell)  
Function show\_formulaR(cell)  
Function show\_formulaL(cell)

Functions for Working with Dates
--------------------------------

The files below have functions that allow you to work with dates. Excel has a nice function that can be used a lot with the SUMIF function to aggregate data by quarter. But excel does not have a similar function for the end of a quarter. Functions that deal with dates are shown below. Another function that can be useful is one that evaluates how much time has occured between a month. This is very useful if you have a monthly model and are not assuming that each project starts or ends at the beginning or the end of a month.

Half year and Quarter.txt

End of Quarter.xlsm end\_of\_qtr.bas

Creating the Colour Macro
-------------------------

The videos for various macros and the associated files are summarised in the following table:

|     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Subject |     | File |     | Video |     | Chapter Reference |     | Page Reference |
|     |     |     |     |     |     |     |     |     |     |
|     | A video showing the short-cut keys that I use |     | Short Cuts.xlsm |     | [https://www.youtube.com/watch?v=GprfRpmTPl0](https://www.youtube.com/watch?v=GprfRpmTPl0) |     | Chapter 4 |     | 40  |
|     | Short-cuts and Data Table |     | Short Cuts and Bond Valuation |     | [https://www.youtube.com/watch?v=f\_t\_hbLaVik](https://www.youtube.com/watch?v=f_t_hbLaVik) |     | Chapter 4 |     | 40  |
|     | Overview of Generic Macros – Operations |     | Generic Macros.bas |     | [https://www.youtube.com/watch?v=Hz8GfMv7VP8](https://www.youtube.com/watch?v=Hz8GfMv7VP8) |     | Chapter 5 |     | 45  |
|     | Creating an Input Colour Macro from the F5 Function |     | Colour Macro.bas |     |     |     | Chapter 5 |     | 48  |
|     | Working with macro that colours cells depending on the source tab colour |     | Colour Sheets Macro.bas |     |     |     | Chapter 5 |     | 48  |
|     | Explanation of Shift CNTL R Macro that automatically copies to right from above |     | Fill to Right.bas |     | [https://www.youtube.com/watch?v=YTZMPRt8J6I](https://www.youtube.com/watch?v=YTZMPRt8J6I) |     | Chapter 5 |     | 45  |
|     | Update and Improved SHIFT, CNTL, R |     | Fill to Right.xlsm |     | [https://www.youtube.com/watch?v=ps1cXeJN-j8](https://www.youtube.com/watch?v=ps1cXeJN-j8) |     | Chapter 5 |     | 48  |
|     | Explanation of how to use and make Table of Contents Macro |     | Table of Contents Macro.bas |     | [https://www.youtube.com/watch?v=FrPE0tJWfOA](https://www.youtube.com/watch?v=FrPE0tJWfOA) |     | Chapter 5 |     | 48  |
|     | How to make a macro that displays the comments in the sheet with check box |     | Comment box |     |     |     | Chapter 5 |     | 48  |
|     | How to create User Defined Functions |     | Financial Library.xlsm |     | [https://www.youtube.com/watch?v=QY743V2BGrw](https://www.youtube.com/watch?v=QY743V2BGrw) |     | Chapter 5 |     | 48  |
|     | Demonstrates how to make a better LOOKUP function without NA |     | Interpolate and Lookup |     |     |     | Chapter 5 |     | 48  |
|     | Shows how to create look up function with interpolation |     | Lookup-Interpolate.xlsm |     | [https://www.youtube.com/watch?v=sfokve3pRT0](https://www.youtube.com/watch?v=sfokve3pRT0) |     | Chapter 5 |     | 48  |
|     | Demonstrates making a Look up function with NA Adjustment to Zero |     | Lookup\_NA.xlsm |     |     |     | Chapter 5 |     | 48  |
|     | How to use the generic macro file with exporting and changing macros |     | Generic Macros.bas |     | [https://www.youtube.com/watch?v=JpztPJxDmOI](https://www.youtube.com/watch?v=JpztPJxDmOI) |     | Chapter 5 |     | 48  |
|     | How to make an Add Text function that combines text |     | Add Text.xlsm |     |     |     | Chapter 5 |     | 48  |
|     | Add Item to Menu in the Generic Macros file |     | Generic Macros.bas |     | [https://www.youtube.com/watch?v=vEfTv3hVPDk](https://www.youtube.com/watch?v=vEfTv3hVPDk) |     | Chapter 5 |     | 48  |
|     | Create Function for Payback Period with intermediate decimal values |     | Payback |     |     |     | Chapter 5 |     | 48  |
|     | Interpolate in Excel without Macro |     | Interpolate macro |     |     |     | Chapter 5 |     | 48  |
|     | Interpolate Macro with Selection.Cells |     | Interpolate macro |     |     |     | Chapter 5 |     | 48  |
|     | Making a calander in excel |     | Calander |     | [https://www.youtube.com/watch?v=FLtNFnnzs9Y](https://www.youtube.com/watch?v=FLtNFnnzs9Y) |     | Chapter 5 |     | 48  |
|     | Installing Macros with File Import |     | Fill to Right.bas |     | [https://www.youtube.com/watch?v=JvRndAlhp1w](https://www.youtube.com/watch?v=JvRndAlhp1w) |     | Chapter 5 |     | 48  |
|     | Overview of Generic Macros – Code |     | Generic Macros.bas |     | [https://www.youtube.com/watch?v=8-ezOD2YIkc](https://www.youtube.com/watch?v=8-ezOD2YIkc) |     | Chapter 5 |     | 45  |
|     | Installing Macros with File Import |     | Fill to Right.bas |     | [https://www.youtube.com/watch?v=JvRndAlhp1w](https://www.youtube.com/watch?v=JvRndAlhp1w) |     | Chapter 5 |     | 45  |
|     | Alternative ways to Import |     | Generic Macros.bas |     | [https://www.youtube.com/watch?v=HBNxSzFXKR8](https://www.youtube.com/watch?v=HBNxSzFXKR8) |     | Chapter 5 |     | 45  |
|     | Importing Macros to Excel |     | Generic Macros.bas |     | [https://www.youtube.com/watch?v=44Cp4cvq-LQ](https://www.youtube.com/watch?v=44Cp4cvq-LQ) |     | Chapter 5 |     | 48  |
|     | Function and Macro (fm) File |     | fm.xlsm |     |     |     | Chapter 5 |     | 48  |
|     | Shows how to make macro to clear zeros from blank rows |     | western customer list.xlsm |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |
|     | ……………………………………………………………………………………………. | ….. | ……………………………………………………….. | ….  | ……………………………………………………………………………………………… | ….  | ……………………………………………… | ….  | ……………………………………………………. |

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=768&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8568&rand=0.5156348363059521)