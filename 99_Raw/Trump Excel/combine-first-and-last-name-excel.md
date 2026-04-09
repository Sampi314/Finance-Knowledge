# How to Combine First and Last Name in Excel (4 Easy Ways)

**Source:** https://trumpexcel.com/combine-first-and-last-name-excel

---

[Skip to content](https://trumpexcel.com/combine-first-and-last-name-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/combine-first-and-last-name-excel/#below-title)

Excel is an amazing tool to store and analyze data. And many of the times, you will have to deal with text data types such as names, regions, departments, or product names.

In such cases, it’s good to know how to manipulate text data and get the desired result.

One of the most common tasks most Excel users have to do is work with a dataset of names. Often you’ll find that the first name and the last name are in separate columns, and you may have a need to combine these first and last names and get these as a combined name in a cell.

In this Excel tutorial, I’ll show you multiple different ways to combine the first and the last name in Excel.

You can easily do that using simple formulas (such as Concatenate or TextJoin) and features such as [Flash Fill](https://trumpexcel.com/flash-fill-excel/)
 and Power Query

This Tutorial Covers:

[Toggle](https://trumpexcel.com/combine-first-and-last-name-excel/#)

4 Ways to Combine First and Last Name in Excel
----------------------------------------------

Suppose you have a dataset as shown below and you want to combine the first name in column A and the Last Name in column B.

![First and Last Name Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20371'%3E%3C/svg%3E)

Let’s have a look at some of the ways to do this.

### Using CONCATENATE Function (or Ampersand)

Combining different text strings from different cells is quite easy in Excel. There is an in-built [Concatenate formula](https://trumpexcel.com/excel-concatenate-function/)
 in Excel that’s made for this purpose only.

Below is the formula that will combine the first and the last name (separated by a space character):

\=CONCAT(A2," ",B2)

![CONCAT formula to combine first and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20424'%3E%3C/svg%3E)

CONCAT is a new function that was introduced in Excel 2016 and is made to replace the CONCATENATE function. But as of now, both the functions continue to be available and you can either function.

Below is the CONCATENATE formula if you wish to use that:

\=CONCATENATE(A2," ",B2)

The above formula simply takes the first and the last name and combines it. And since I want these to be separated by a space character, I have used ” ” (space in double-quotes) as the second argument.

You can also use the ampersand operator to do the concatenation.

Assuming you have the same dataset, you can use the below formula to combine the first and the last name:

\=A2&" "&B2

![Ampersand to combine first and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20423'%3E%3C/svg%3E)

The ampersand operator combines the text before and after it. In the above example, I have combined three parts – first name, a space character, and last name.

Now that you understand the concept, you can combine the names in different formats if you want. For example, you may want to have the last name and then the first name, or a comma instead of the space between the names.

_In case you only want the combined name and want to get rid of the first and the last name, you should first [convert the formula values to static values](https://trumpexcel.com/convert-formulas-to-values-excel/)
. Once done, you can then remove/delete the first and the last name._

### Using the TEXTJOIN function

TEXTJOIN is a function that’s available in Excel 2019 and Office 365.

In case you have access to this function, it’s best to use it for [combining cells](https://trumpexcel.com/combine-cells-in-excel/)
 and columns (as it’s a lot better than the above CONCATENATE and ampersand methods).

Suppose you have the dataset as shown below and you want to combine the first and the last name.

![First and Last Name Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20371'%3E%3C/svg%3E)

Below is the formula to do this:

\=TEXTJOIN(" ",TRUE,A2:B2)

![TEXTJOIN formula to combine first and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20421'%3E%3C/svg%3E)

The above TEXTJOIN function takes three arguments:

1.  The delimiter, which is a space character in double-quotes in this example (since we want the first and the last name to be separated by a space character)
2.  A Boolean value where TRUE means that in case there are any [blank cells](https://trumpexcel.com/select-blank-cells-in-excel/)
    , the formula will ignore it
3.  The range that has the cells that you want to combine

It’s faster than the regular concatenate formula and is also easier to create and manage. So if you have access to the TEXTJOIN function in Excel, it’s better to use it over any other formula.

### Using Flash Fill

Flash Fill is a smart functionality that tries to understand the pattern and give you the result.

Let me explain how it works.

Suppose you have a dataset as shown below and you want to combine the first and the last name.

![First and Last Name Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20371'%3E%3C/svg%3E)

Below are the steps you can use to do this using Flash Fill

1.  In cell C2, enter the result you want. In our example, it would be ‘Bobby Baker’
2.  In cell C3, start typing the expected result. You will notice that Excel shows you the expected result in all the cells (in the light gray text). This is Flash Fill in action

![Flash fill shows the combined names result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20522%20370'%3E%3C/svg%3E)

3.  Hit the Enter key

The above steps would instantly fill all the cells with the combined name.

In some cases, it’s possible that you won’t see flash fill while you are typing in the second cell.

Don’t worry, it happens sometimes.

In such a scenario, below other steps you can use to make Flash Fill work:

1.  In cell C2, enter the result you want. In our example, it would be ‘Bobby Baker’
2.  Select select C3
3.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20367%20200'%3E%3C/svg%3E)

4.  In the Editing group, click on the Fill icon
5.  Click on Flash Fill

![Flash Fill option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20341%20378'%3E%3C/svg%3E)

The above steps would instantly pick the pattern from the cell above and fill the entire column with the combined name.

In case Flash fill isn’t able to pick up the right pattern and gives incorrect result, fill two cells manually and then do the above steps.

You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 **Control + E** to fill using Flash fill.

Combining the first and the last name (or even the first, middle, and last name) is a simple operation that Flash Fill can easily handle.

Keep in mind that Flash Fill is not perfect. It works by identifying patterns and using the same pattern to fill all the cells in the column. While it’s most likely to work as expected, it’s a good idea to double-check the result of Flash Fill.

### Using Power Query

[Power Query](https://trumpexcel.com/category/power-query/)
 is an amazing tool that used to extract and transform data.

You can also use this to quickly merge columns and combine the first and the last name.

For Power Query to work, your data needs to be in an [Excel Table](https://trumpexcel.com/excel-table/)
 (or at least a [Named Range](https://trumpexcel.com/named-ranges-in-excel/)
).

For the purpose of this tutorial, I will convert the data set that has the 1st and the last name into an Excel Table.

Suppose you have a data set as shown below and you want to merge the two columns to get the full name.

![First and Last name data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20310%20370'%3E%3C/svg%3E)

Below are the steps to convert the data into an Excel Table:

1.  Select any cell in the dataset
2.  Click on the Insert tab

![Click the Insert tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20356%20202'%3E%3C/svg%3E)

3.  Click the Table icon

![Click the Table icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20307%20201'%3E%3C/svg%3E)

4.  In the Create Table dialog box, make sure the range is correct

![Create Table dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20161'%3E%3C/svg%3E)

5.  Click on Ok

The above steps would convert the data range into an Excel Table.

Now let’s see how to combine the first and last name using Power Query:

1.  Select any cell in the table
2.  Click the Data tab

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20199'%3E%3C/svg%3E)

3.  In the Get & Transform Data group, click on the ‘From Sheet’ option. This will open the Power Query Editor

![Click on From Sheet option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20559%20199'%3E%3C/svg%3E)

4.  In the Power Query Editor, make sure the right table is selected in the left pane. If you just have one table, you will only see one option in the left pane
5.  Select the columns that you need to merge (hold the Control key and then click on the column header to select the column)

![Select the columns you want to merge](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20347'%3E%3C/svg%3E)

6.  Right-click and then click on the ‘Merge Columns’ option

![Right click and then click on Merge Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20437%20527'%3E%3C/svg%3E)

7.  In the Merge Columns dialog box that opens, select Space as the delimiter (from the drop-down)

![Select Space as the delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20261'%3E%3C/svg%3E)

8.  Enter a name for the new merged column. I will go with ‘Full Name’

![Enter the name of the new merge column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20261'%3E%3C/svg%3E)

9.  Click OK. This would remove the two columns that we already have and replace them with the new column that has the full name.

![Full name column that has the merged names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20346'%3E%3C/svg%3E)

10.  Click the File tab and then click on Close and Load.

![Close and Load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20169'%3E%3C/svg%3E)

The above steps would insert a new worksheet in the workbook with a table that has one column that has the full name.

In case you want the original columns as well as a new column that contains the full name, instead of selecting the columns and Merge them, first select the Add Column tab in the Power Query Editor, then select the columns, and then click on Merge Columns. This will add a new column that will have the full name.

Compared to the formula methods and Flash Fill, Power Query is definitely a bit longer.

But the benefit of using this method is that in case your original data changes, you can quickly refresh the query and your resulting data would automatically update.

Also, Power Query is widely used to combine different tables and data from [multiple worksheets](https://trumpexcel.com/combine-multiple-worksheets/)
 and workbooks. So, in case you have the name data you want to combine, it’s one single step in your already existing power query workflow.

In this tutorial, I have covered how to **combine the first name and the last name in Excel**. But in case you have the first, middle, and last name, you can use the same methods to do it.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How to Sort by the Last Name in Excel](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [Extract Usernames from Email Ids in Excel](https://trumpexcel.com/extract-usernames-from-email-ids/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [Extract Last Name in Excel (5 Easy Ways)](https://trumpexcel.com/extract-last-name-excel/)
    
*   [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    
*   [How to Switch First and Last Name in Excel with Comma?](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Combine First and Last Name in Excel (4 Easy Ways)”
-------------------------------------------------------------------------

1.  hey bro,
    
    your page was a lifesaver, im taking an excel course and I’m working on my final project, I literally could not join the two columns under any circumstances, but after following your page i found out my flash fill wasn’t selected, and once i clicked on it all those columns populated, so thanks man , i appreciate it
    
    [Reply](https://trumpexcel.com/combine-first-and-last-name-excel/#comment-54985)
    
    *   Thanks Ben, glad the article helped 🙂
        
        [Reply](https://trumpexcel.com/combine-first-and-last-name-excel/#comment-54995)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/combine-first-and-last-name-excel/#respond)

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