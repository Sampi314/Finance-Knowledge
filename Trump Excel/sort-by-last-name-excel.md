# How to Sort by the Last Name in Excel (Easy Guide)

**Source:** https://trumpexcel.com/sort-by-last-name-excel

---

[Skip to content](https://trumpexcel.com/sort-by-last-name-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sort-by-last-name-excel/#below-title)

**Watch Video – How to Sort By Last Name In Excel**

If you work with names datasets, sorting it is one of the common tasks you would have to do often.

It’s quite easy to sort data alphabetically based on the full name, where Excel uses the first character of the name to sort.

But what if you want to **sort data by the last name in Excel**?

While it’s not as straightforward, it can still be done (a lot also depends on the way names data is structured).

No matter what method you use, you will have to, somehow, extract the last name from the full name and put it in a separate column. You can then use this column to sort your data by the last name alphabetically.

In this Excel tutorial, I will show you how to sort a column with names based on the last name.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sort-by-last-name-excel/#)

Extract and Sort by Last Name Using Find and Replace
----------------------------------------------------

The first step to sorting by the last name is to get the last name in a separate column.

You can do that by replacing everything before the last name with a blank so that you only have the last name left.

Suppose you have a dataset as shown below and you want to sort this data alphabetically using the last name.

![Names to Sort by Last Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20248%20307'%3E%3C/svg%3E)

Below are the steps to sort by the last name:

1.  Select the dataset including the header (in this example, it would be A1:A10)
2.  Copy it in the adjacent column (if the adjacent column is not empty, insert a new column and then copy these names)![Copy Names dataset in Adjacent column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20306'%3E%3C/svg%3E)
3.  Rename the copied column header. In this example, I will name is ‘Last Name’
4.  Select all the copied names (don’t select the header)
5.  Hold the Control key and then press the H key. This will open the Find and Replace dialog box.![Control H to open find and replace dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20268'%3E%3C/svg%3E)
6.  In the Find what field, enter \*  (asterisk symbol followed by a space character)![Enter asterisk followed by a space character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)
7.  Leave the Replace with field empty![Leave the replace with field blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)
8.  Click on Replace All. This would instantly replace all the first name and you will be left with last names only.![Click on Replace All](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

The above steps would keep the last name and remove everything before it. This works well even when you have middle names or prefixes (such as Mr. or Ms).

![You get the last names only using Find and Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20412%20310'%3E%3C/svg%3E)

Once you have the last names in the adjacent column, you can easily sort the dataset (including the full names) alphabetically based on the last name.

Below are the steps to sort by the last name:

1.  Select the entire dataset with headers (including the full names and the extracted last names). You can also include other columns that you want to sort along with the names
2.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20197'%3E%3C/svg%3E)
3.  Click on Sort![Click on the Sort tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20282%20153'%3E%3C/svg%3E)
4.  In the Sort dialog box, make sure ‘My data has headers’ is selected.
5.  In the ‘Sort by’ option, select the name of the column that just has the last name![Select Last name in Sort by options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20275'%3E%3C/svg%3E)
6.  In the ‘Sort On’, select ‘Cell Values’![Select Cell Values in Sort Based on](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20275'%3E%3C/svg%3E)
7.  In the Order option, select ‘A to Z’![Select the order - A to Z or Z to A](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20275'%3E%3C/svg%3E)
8.  Click OK

The above steps would sort the entire selected dataset based on the last name.

![Sorted based on last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20308'%3E%3C/svg%3E)

Once done, you can delete the column that has the last name.

**Pro Tip**: At any point in time, if you think you may need the original data back, you need to have a way to un-sort this dataset. To do this, in an adjacent column (left or right), have serial numbers before the sorting. Now, if you need the original data back, you get it by sorting based on the numbers.

Also read: [Sort Dates By Month in Excel](https://trumpexcel.com/sort-dates-by-month-excel/)

Extract and Alphabetize by Last Name Using Formula
--------------------------------------------------

While the method that’s shown above (using Find and Replace) is what I prefer to get all the last names and sort based on it, one limitation of it is that the resulting data in static.

This means that if I add more names to my list, I will have to do the same process again to get the last names.

If this is something you don’t want, you can use the formula method to sort data by last names.

Suppose you have the dataset as shown below.

Below is the formula that will extract the last name from the full name:

\=RIGHT(A2,LEN(A2)-FIND(" ",A2))

![Excel Formula to get the last name from full name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20368'%3E%3C/svg%3E)

The above formula relies on the pattern with a full name (that contains only the first and last name in this example). The pattern is that there would be a space character between the first and last name.

The FIND function is used to get the position of the space character. This value is then subtracted from the total length of the name to get the total number of characters in the last name.

This value is then used in the RIGHT function to get the last name.

Once you have the last name column, you can sort this data (this is covered in the first method in detail).

The above formula would work when you only have first and last names.

But what if you have a middle name as well. Or may there is a salutation before the name (such as Mr or Ms.)

In such a case, you need to use the below formula:

\=RIGHT(A2,LEN(A2)-FIND("@",SUBSTITUTE(A2," ","@",LEN(A2)-LEN(SUBSTITUTE(A2," ","")))))

The above formula finds the position of the last space character and then uses it to extract the last name.

I recommend you use the second formula in all the cases, and it’s more fool-proof and can handle all cases (as long as the last name is at the end of the name).

Note: These two formulas rely on the condition that there is only one space character between every name element. In case there are double spaces, or leading/trailing spaces, this formula will give incorrect results. In such a case, it’s best to use the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 to first [get rid of any leading, trailing and double spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
, and then use the above formula.

While this may seem like a complicated method, the benefit of using a formula is that it makes the results dynamic. If you add more names to your list, all you have to do is copy the formula and it will give you the last name.

Also read: [How to Sort by Length in Excel? Easy Formulas!](https://trumpexcel.com/sort-by-length-excel/)

Using Text to Columns
---------------------

[Text to Columns](https://trumpexcel.com/excel-text-to-columns-examples/)
 is again a simple and easy way to split cells in Excel.

You can specify the delimiter (such as comma or space) and use it to split the content of the cell. Once you have the split elements in separate columns, you can use the column that has the last name to alphabetize the data.

Suppose you have a dataset as shown below:

Below are the steps to use Text to Column to sort by the last name:

1.  Select the column that has the name (excluding the header)
2.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20197'%3E%3C/svg%3E)
3.  In the ‘Data Tools’ group, click on the Text to Columns option. This will open the Text to Columns wizard![Click on Text to Columns option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20140'%3E%3C/svg%3E)
4.  In Step 1 of the ‘Convert Text to Columns Wizard’, select ‘Delimited’ and click on Next![Select Delimited in Step 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)
5.  In Step 2, select ‘Space’ as the Delimiter (and uncheck anything else if selected) and then click on the Next button.![Select the Space option and then click on Next](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)
6.  In Step 3, select the first name column in the Data preview and then select the ‘Do not import columns (skip)’ option. This ensures that the first name is not a part of the result and you only get the last name.![Select Do no import column in Step 3 of Text to Column wizard](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)
7.  Also in Step 3, change the destination cell to the one which is adjacent to the original data. This will make sure you get the last name separately and original names data is intact.![Specify the destination cells for text to columns resulting data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20428'%3E%3C/svg%3E)
8.  Click on Finish

Once you have the result, you can sort by the last name.

![Result of Text to Columns to extract the last name and then sort by it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20307'%3E%3C/svg%3E)

You can also Text to Columns to [separate first and last names](https://trumpexcel.com/separate-first-and-last-name-excel/)
 when you have a comma as the separator.

Also read: [How to Switch First and Last Name in Excel with Comma?](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/)

Using Flash Fill
----------------

Another quick and fast way to get the last names is using the Flash Fill feature.

Flash Fill was introduced in Excel 2013 and it helps manipulate the data by identifying patterns. For this to work, you need to show Flash Fill the result you expect a couple of times.

Once it identifies the pattern, it will quickly do the rest of the work for you.

Suppose you have the below names dataset.

![Names data to sort by last name using flash fill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20306'%3E%3C/svg%3E)

Below are the steps to use Flash Fill to get the last name and then sort using it:

1.  In cell B2, enter the text ‘Maury’. This is the result you expect in the cell.
2.  Go to the next cell and enter the last name for the name in the adjacent cell (Elliot in this example).
3.  Select both the cells
4.  Hover the cursor over the bottom-right part of the selection. You will notice that the cursor changes to a plus icon.![Green square at the bottom right of the selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20309'%3E%3C/svg%3E)
5.  Double-click on it (or click and drag it down). This will give you some result in the cells (not likely to be the result you want)
6.  Click on the AutoFill Options icon.![Click on the Autofill option icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20458%20350'%3E%3C/svg%3E)
7.  Click on Flash Fill![Select Flash Fill option to get all the last names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20467'%3E%3C/svg%3E)

This will give you the result which will likely be the last names in all the cells.

I say likely, as Flash Fill may not work in some cases. Since it depends on identifying a pattern, it may not be able to do that always. Or sometimes, the pattern it deciphers may not the right one.

In such cases, you should enter an expected result in one or two more cells and then do steps 4-7.

Once you have all the last names in a column, you can sort the data based on these last names.

So these are four different ways that you can use to sort data by the last name. The best method would be to use the Find and Replace technique, but if you want to make your results dynamic, the formula method is the way to go.

Hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [How to Sort By Color in Excel](https://trumpexcel.com/sort-by-color/)
    
*   [How to Unsort Data in Excel](https://trumpexcel.com/undo-sort-excel/)
    
*   [How to Sort Worksheets in Excel](https://trumpexcel.com/sort-worksheets/)
    
*   [How to Sort Data in Excel using VBA](https://trumpexcel.com/sort-data-vba/)
    
*   [Automatically Sort Data in Alphabetical Order using Formula](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    
*   [How to do a Multiple Level Data Sorting in Excel](https://trumpexcel.com/multiple-level-sorting-excel/)
    
*   [Flip Data in Excel | Reverse Order of Data in Column/Row](https://trumpexcel.com/flip-data-in-excel/)
    
*   [How to Combine First and Last Name in Excel](https://trumpexcel.com/combine-first-and-last-name-excel/)
    
*   [How to Shuffle a List of Items/Names in Excel? 2 Easy Formulas!](https://trumpexcel.com/shuffle-list-excel/)
    
*   [Extract Last Name in Excel (5 Easy Ways)](https://trumpexcel.com/extract-last-name-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Sort by the Last Name in Excel (Easy Guide)”
-----------------------------------------------------------------

1.  Good thing nobody has two words for either their first or last names. Otherwise that could be a problem.
    
    [Reply](https://trumpexcel.com/sort-by-last-name-excel/#comment-14926)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/sort-by-last-name-excel/#respond)

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