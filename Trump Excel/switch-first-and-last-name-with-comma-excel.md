# How to Switch First and Last Name in Excel with Comma?

**Source:** https://trumpexcel.com/switch-first-and-last-name-with-comma-excel

---

[Skip to content](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/#below-title)

When working with name data sets in Excel, you may want the names to be in a specific format.

Usually, the names are either in the ‘First Name Last Name’ format (such as Joe Davis or Sumit Bansal).

In some specific situations, you may want the names data to be formatted as _Last Name, First Name_ (i.e., last name followed by a comma and then the first name)

In this tutorial, I will show you how to **switch the first and the last name in Excel with a comma in between** (when you have your data in the First Name Last Name format)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/#)

Switch First and Last Name Using Flash Fill
-------------------------------------------

One of the easiest and fastest ways to switch the first and the last name with a comma in between is by using the [Flash Fill feature in Excel](https://trumpexcel.com/flash-fill-excel/)
.

Flash Fill is an amazing tool that works by identifying patterns in your data set (where you need to enter one or two expected result entries for it to identify the pattern).

Let me show you how it works.

Below I have a data set where I have the names in column A, and I want to change this data set by switching the first and the last name and adding a comma in between the names.

![Names data set with first and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20405'%3E%3C/svg%3E)

Here are the steps to do this using Flash Fill:

1.  In cell B2, enter the expected result (which would be Miller, Flora)

![enter the expected result in the first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20476%20404'%3E%3C/svg%3E)

2.  Press the Enter key

![press the enter key to go to the cell below](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20476%20405'%3E%3C/svg%3E)

3.  Click the Home tab
4.  In the Editing group, click on the Fill option

![click on the fill icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20663%20223'%3E%3C/svg%3E)

5.  Click on the Flash Fill option

![click on flash fill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20421'%3E%3C/svg%3E)

That’s it!

As soon as you click the Flash Fill option, you should see the entire column automatically get filled with the correct result.

![result after using flash fill names switched](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20401'%3E%3C/svg%3E)

Let me quickly explain how this works.

When I entered the expected result in cell B2 and then used Flash Fill, it used the value in cell B2 to identify the pattern and replicated it for all the cells in the column.

So it was able to correctly identify that I wanted to change the names data set by switching the first and the last name and adding a comma in between.

**Pro Tip**: You can use the keyboard shortcut **Control + E** to run the Flash Fill. So as instead of going to the Home tab and then clicking on the Flash Fill icon, enter the expected result in one cell, hit the Enter key, and then hold the Control key and press the E key.

**Caution**: Since Flash Fill works by identifying the pattern in your data set, it is important that you have a consistent data set. Also, cross-check the result from Flash Fill to ensure that it has picked up the correct pattern.

_Note – The result that you get from Flash Fill is static. So if your original data changes, the resulting data will not automatically update, and you will have to repeat the process._

Switch First and Last Name Using Formula
----------------------------------------

Let me now show you how you can switch the first and the last name by using a simple formula.

While there is no inbuilt function to do this, it can quickly be done by using a combination of text functions.

Below I have the names data set where I want to switch the first and the last name and add a comma in between.

![Names data set with first and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20405'%3E%3C/svg%3E)

Here is the formula that will do this:

\=CONCAT(RIGHT(A2,LEN(A2)-FIND(" ",A2)),", ",LEFT(A2,FIND(" ",A2)-1))

Enter this formula in cell B2 and copy it for all the other cells in the column.

![Formula to reverse the first and the last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20625%20438'%3E%3C/svg%3E)

Let me explain how this formula works.

In the formula, I have used the [LEFT](https://trumpexcel.com/excel-left-function/)
 and the [RIGHT function](https://trumpexcel.com/excel-right-function/)
 to extract the first name and the last name, respectively.

This is made possible by identifying the position of the space character (using the [FIND function](https://trumpexcel.com/excel-find-function/)
).

Using the position of the space character, I extracted all the characters on the left, which would be the first name, using the LEFT function.

And similarly, I extracted all the characters to the right of the space character using the RIGHT function (which gave me the last name).

And then, I combined the last name and the first name by using the CONCAT function. Also, since I wanted the last name and the first name to have a comma in between, I added a comma followed by a space character as the second argument in the CONCAT function.

You can also use the below formula, which uses the & operator instead of the CONCAT function:

\=RIGHT(A2,LEN(A2)-FIND(" ",A2))&", "&LEFT(A2,FIND(" ",A2)-1) 

**Beware of the Extra Spaces**: For this formula to work correctly, you have to make sure that there is only one space character between the first name and the last name. In case there is a possibility that there could be multiple spaces in between the names or there could be a [leading or trailing space](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
, then it would be best to use TRIM(A2) instead of A2 in the above formulas.

Also, note that since we are using a formula to switch the names, in case you change the original data set, the resulting data will automatically update to give you the correct result.

And if you do not need the original data anymore, do not just delete the original data without first [converting the formulas into values](https://trumpexcel.com/convert-formulas-to-values-excel/)
. To do this, select the cells that have the result, copy the cells right-click and then paste them as values.

Switch First and Last Name Using Text to Columns with CONCAT Function
---------------------------------------------------------------------

You can also use the [Text to Columns feature](https://trumpexcel.com/excel-text-to-columns-examples/)
 to split the first name and last name into separate columns and then combine them in the order you want with the delimiter you want.

Let me show you how this works.

Below I have the names data set where I want to switch the position of the first name and the last name and add a comma in between.

![data set for text to columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20630%20312'%3E%3C/svg%3E)

Here are the steps to split the first name and the last name into separate columns using the Text to Columns feature:

1.  Select the names data set in column A

![select the names data and column A](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20313'%3E%3C/svg%3E)

2.  Click the **Data** tab

![click the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20503%20181'%3E%3C/svg%3E)

3.  In the Data Tools group, click on the **Text to Columns** option. This will open the Convert Text to Columns wizard.

![click on text to columns icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20164'%3E%3C/svg%3E)

4.  In Step 1 of 3, make sure that the **Delimited** option is selected, and then click on the **Next** button.

![select the delimited option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20427'%3E%3C/svg%3E)

5.  In Step 2 of 3, select **Space** as the delimiter option (and uncheck any other option if selected already), and then click on **Next**

![select the space option and click on next](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20427'%3E%3C/svg%3E)

6.  In Step 3 of 3, specify the destination cell (where you want to get the results). In this example, I would select cell B2 as the destination cell. If you do not select the destination cell, your existing name data will be overwritten by the result.

![specify the destination cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20427'%3E%3C/svg%3E)

7.  Click on the **Finish** button.

The above steps would split the names data set into two separate columns – one with first names and the other with last names.

![first name and last name split into different columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20311'%3E%3C/svg%3E)

Once you have the first and the last name in separate columns, you can use the formula below to combine these names in the desired order (i.e., the last name followed by a comma and then the first name)

\=CONCAT(C2,", ",B2)

Enter the formula in cell D2 and copy it for all the cells in the column to get all the names.

![concat Formula to combine last name and first name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20357'%3E%3C/svg%3E)

The above formula uses the CONCAT function to combine three elements:

*   The last name, which is in cell B2
*   A comma followed by a space character (which needs to be in double quotes)
*   The first name, which is in cell B2

Switch First and Last Name Using Power Query
--------------------------------------------

Power Query is another way to switch the first and the last name and add the desired delimiter in between.

The Power Query method should only be used if you are already using It to transform your data and, as a part of it, also wants to change the names data set. Or if you have to do this quite often so, instead of doing it using the Flash Fill method or the formula method every time, you can use Power Query to do it once and then use the same query over and over again with different data sets.

But if this is a one-time activity where you want to reverse the position of the first name and the last name, it is best to use the other methods such as Flash Fill or formula (covered earlier in this tutorial)

Below I have the names data set where I want to switch the first and the last name and separate them by a comma and a space character.

![Names data set with first and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20405'%3E%3C/svg%3E)

Below are the steps to do this using Power Query:

1.  Select the range that contains the names
2.  Click the Data tab
3.  In the **Get & Transform Data** group, click on the **From Table/Range** option

![click on from table range option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20223'%3E%3C/svg%3E)

4.  In the **Create Table** dialog box that opens up, click on the OK button. This will convert our current range of cells into an Excel Table which can then be used in Power Query.

![click OK in the create table dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20161'%3E%3C/svg%3E)

5.  In the Power Query editor that opens up, right-click on the **Names** column and then hover the cursor over the **Split Column** option, and then click on **By Delimiter**

![split column by delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20626'%3E%3C/svg%3E)

6.  In the ‘Split Column by Delimiter’ dialog box, select **Space** as the delimiter and then click on OK. This will split the names column into first name and last name

![select space as the delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20448'%3E%3C/svg%3E)

7.  Select both the Names columns, right-click on the column header and then click on **Merge Columns**

![click on merged columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20459'%3E%3C/svg%3E)

8.  In the merge columns dialog box, click on the Separator drop-down and then select the **Custom** option

![select the custom option from the separator drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20288'%3E%3C/svg%3E)

9.  Enter a comma followed by a space character (, ) in the field below the Custom option

![specify the custom separator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20288'%3E%3C/svg%3E)

10.  Enter the name for the new merged column. I will go with the name ‘Full Names’

![enter the name of the new column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20288'%3E%3C/svg%3E)

11.  Click OK. This will merge the two columns, and you will now have one column with the last name followed by a comma and the first name.

![column where the names have been reversed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20505%20417'%3E%3C/svg%3E)

12.  Click on the **Close and Load** option in the ribbon

![click on close and load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20659%20140'%3E%3C/svg%3E)

The above steps would insert a new worksheet in your workbook and give you the resulting data in an Excel Table.

![Resulting table inserted in a new sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20400'%3E%3C/svg%3E)

I’m sure you’re thinking about how long this method is and whether this is worth it or not.

As I mentioned at the beginning of this section, if you only want to do this once or twice, it’s best not to use Power Query.

But if this is something you need to do quite often, then you can follow all the above steps to create the query once, and the next time you have a new data set, you can connect your query to that table and get the result instantly.

Or if you make any changes to the already existing names data set, you don’t need to repeat the process.

All you need to do is right-click on the resulting Excel Table that we got and then click on refresh, and it will perform all the steps in the back end for you and give you the result.

![click the refresh option to refresh the query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20365%20578'%3E%3C/svg%3E)

Switch First and Last Name Using VBA
------------------------------------

Now let me show you how to reverse the first and the last name using a simple VBA code.

Below is the VBA macro code that would switch the first and the last name position and add a comma in between

    'Code by Sumit Bansal from https://trumpexcel..com
    Sub ReverseNames()
    Dim FindSpace As Long
    For Each Cell In Selection
        FindSpace = InStr(Cell.Value, " ")
        If FindSpace > 0 Then
            Cell.Value = Trim$(Mid$(Cell.Value, FindSpace + 1)) _
            & ", " & Left$(Cell.Value, FindSpace - 1)
        End If
    Next Cell
    End Sub

The above VBA code uses a [For Each Next loop](https://trumpexcel.com/vba-loops/)
 to go through each cell in the column and then uses the [INSTR function](https://trumpexcel.com/excel-vba-instr/)
 to find out the position of the space character in the cell.

Once it knows the position of the space character, it uses the MID function and the LEFT function to extract the last name and the first name, respectively, and combine them using an & operator.

Here are the steps to use this code:

1.  Select the names dataset (excluding the header)

![select the names data set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20237%20313'%3E%3C/svg%3E)

2.  Click the Developer tab in the ribbon and then click on the visual basic icon (if you [do not see the Developer tab](https://trumpexcel.com/excel-developer-tab/)
    , you can also use the keyboard shortcut ALT + F 11)

![click on visual basic icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20698%20190'%3E%3C/svg%3E)

3.  In the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
     that opens up, click on the **Insert** option in the menu
4.  Click on the **Module** option. This will insert a new module for the workbook

![insert a module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20353'%3E%3C/svg%3E)

4.  Copy and paste the above VBA code into the module code window

![copy and paste the code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20673%20279'%3E%3C/svg%3E)

5.  To run the code, place the cursor anywhere within the code and then press the F5 key on your keyboard or click on the green triangle icon in the toolbar

![Run the macro by clicking on the green play button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%2032'%3E%3C/svg%3E)

The above steps would instantly change your original data set and give you the result as shown below:

![Result of the VBA code is run](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20387%20333'%3E%3C/svg%3E)

While there is some initial setup required to use the VBA method, it is helpful in case you want to change the names data set in multiple locations in your existing workbook.

You can also save this macro code in the Personal Macro Workbook so that it can be used in any workbook on your system.

This would be quite a time saver as you can open any Excel workbook where you have the names data and then run this code to switch the first and the last name (separated by a comma).

_[Click here to learn about Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
 and how you can save your code there to reuse on any workbook in your system_

**Pro Tip**: if you save the macro in your Personal Macro Workbook, you can save more time by adding the macro icon to the [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
. Once added, you can run the code with a single click by clicking on the macro icon in the QAT

So these are the five methods you can use to reverse the first name and the last name and add a comma in between the names.

If you need to do it once in a while, you can use the Flash Fill method, the formula method, or the Text to Columns method.

And if you need to do this quite often, consider using the Power Query or the VBA method.

**Other Excel articles you may also like:**

*   [How to Shuffle a List of Items/Names in Excel? 2 Easy Formulas!](https://trumpexcel.com/shuffle-list-excel/)
    
*   [Extract Last Name in Excel (5 Easy Ways)](https://trumpexcel.com/extract-last-name-excel/)
    
*   [How to Combine First and Last Name in Excel (4 Easy Ways)](https://trumpexcel.com/combine-first-and-last-name-excel/)
    
*   [How to Sort by the Last Name in Excel (Easy Guide)](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/#respond)

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