# Extract Last Name in Excel (5 Easy Ways)

**Source:** https://trumpexcel.com/extract-last-name-excel

---

[Skip to content](https://trumpexcel.com/extract-last-name-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/extract-last-name-excel/#below-title)

When working with the names dataset in Excel, often there is a need to slice and dice the dataset and extract a part of it.

One common task many Excel users have to do is to **extract the last name from the full name**.

While it may seem like an easy task, it can get complicated (especially when you’re dealing with data that is not consistent).

In this tutorial, I will show you five different ways to extract the last name from the full name in Excel. I will cover different scenarios, where you only have the first and the last name in the dataset, or the first, middle, and last name.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/extract-last-name-excel/#)

Extract Last Name Using Find and Replace
----------------------------------------

Extracting the last name from a full name essentially means you’re replacing everything before the last name with a blank.

And this can easily be done using [Find and Replace in Excel](https://trumpexcel.com/find-and-replace-in-excel/)
 (and it takes less than 3 seconds).

Below I have a names data set from which I want to extract only the last name.

![Dataset to extract last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20649%20416'%3E%3C/svg%3E)

Below are the steps to use Find and Replace to remove everything before the last name:

1.  Copy the name data from Column A and paste it in Column B. I am doing this to keep the original data intact. If you only need the last name, you can skip this step.

![Copy the names in column B](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20416'%3E%3C/svg%3E)

2.  Select all the names in column B

![Select the names in column B](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20647%20417'%3E%3C/svg%3E)

3.  Hold the Control key and press the H key (Command + H if using Mac). This will open the Find and Replace dialog box.

![Find and replace dialog box opens](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

4.  In the Find and Replace dialog box, enter the following in the Find what field: **\*** (an asterisk symbol followed by a space character)

![Enter asterisk followed by space in find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

5.  Leave the Replace with field empty/blank
6.  Click on Replace All

![Click on Replace all](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)

The above steps food remove anything before the last space character, which would leave us with the last names only.

![Last names remain in the dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20415'%3E%3C/svg%3E)

The above method would also work in case you have an inconsistent names dataset. For example, if you have names that may or may not have a middle name/initial, or may have a prefix such as Mr or Ms. The only condition is that the last name should be at the end of the name

**How does this work?**

In the ‘Find what’ field in the Find and Replace dialog box, I have used an asterisk sign (\*) followed by a space character.

Asterisk is a [wild card character](https://trumpexcel.com/excel-wildcard-characters/)
 that represents any number of characters in Excel.

So when I ask it to find an asterisk followed by the space character, it will find the last space character in the cell and everything before that space character would be considered a part of the asterisk.

And when I replace it with a blank, everything before the last space character is removed.

Note: For this method to work you need to make sure that there are no trailing spaces in your data. In case there is a space character after the last name, doing the above Find and Replace operation would remove everything from the cell. To make sure there are no trailing spaces, you can use the [TRIM formula](https://trumpexcel.com/excel-trim-function/)
 (read – [how to remove trailing spaces in Excel](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
)

Extract Last Name Using Formulas (When you Have Only First and Last name)
-------------------------------------------------------------------------

Suppose you have a data set as shown below where you have the first name and the last name in column A, and you only want to extract the last name from it.

![Dataset with first and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20418'%3E%3C/svg%3E)

Below is the formula that will do that:

\=RIGHT(A2,LEN(TRIM(A2))-FIND(" ",TRIM(A2)))

![Extracting last name from full names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20466'%3E%3C/svg%3E)

Let me quickly explain how this formula works.

The above formula uses the [FIND function](https://trumpexcel.com/excel-find-function/)
 to get the position of the space character in the name.

Since the position of the space character would be between the first and the last name, once we have the position of the space character, we can use that to extract everything to the right of it (which would be the last name)

But how many characters from the right should it extract?

Since we have the position of the space character, we can subtract that value from the length of the name (which is given by the [LEN function)](https://trumpexcel.com/excel-len-function/)
. This tells us how many characters are there after the space character in the name.

And this value is then used in the RIGHT formula to extract the last name from the full name.

Note that I have used TRIM(A2) instead of A2 in this formula. This is because there is a possibility that the cells containing the names may have leading, trailing, or double spaces in them. Using the TRIM function makes sure that all these extra spaces are ignored and only one space character between the first name and the last name is considered.

Extract Last Name Using Formulas (When you Have First, Middle, and Last name)
-----------------------------------------------------------------------------

In case you have the first, middle, and last name, the formula becomes a little bit longer.

Below I have a data set where I have the first, middle, last name in column A, and I want to extract the last name from it.

![Dataset with first middle and last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20576%20416'%3E%3C/svg%3E)

Here is a formula that can do that:

\=RIGHT(TRIM(A2),LEN(TRIM(A2))-SEARCH(" ",TRIM(A2),SEARCH(" ",TRIM(A2))+1))

![Formula to get last name from first middle and last names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20372'%3E%3C/svg%3E)

The above function uses the same concept where we have to find out the position of the last space character, and then extract everything to the right of that space character.

But since there are two space characters, in this case, the challenge is to find out the position of this second space character.

To do this, I have used the below-nested [SEARCH function](https://trumpexcel.com/excel-search-function/)
 (i.e., Search function within a search function)

\=SEARCH(" ",TRIM(A2),SEARCH(" ",TRIM(A2))+1)

This part of the formula gives us the position of the second space character, which is then used within the RIGHT formula to extract the last name.

Note that this formula would only work when you have a consistent names dataset – i.e., all the names have the first, middle, and last names.

In case you have a mix of names where some may have middle names but some may not, this formula is not going to work.

If that is the case, use the formula in the next section.

### When You Have Incosistent Data (Names with and Without Middle Name)

Below I have a named data set where the format is not consistent – in some cells, we only have the first and last name, and in some cells, there are a middle name and/or prefixes as well.

![Mixed dataset with names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20577%20415'%3E%3C/svg%3E)

While you can still use excel formulas to extract the last name in this case, the formula we’ll get a little bit complicated.

Below is the formula that will extract the last name in this inconsistent data set:

\=RIGHT(SUBSTITUTE(A2," ","|",LEN(A2)-LEN(SUBSTITUTE(A2," ",""))),LEN(SUBSTITUTE(A2," ","|",LEN(A2)-LEN(SUBSTITUTE(A2," ",""))))-FIND("|",SUBSTITUTE(A2," ","|",LEN(A2)-LEN(SUBSTITUTE(A2," ","")))))

![Formula to get last name from mixed names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20802%20510'%3E%3C/svg%3E)

Also read: [How to Switch First and Last Name in Excel with Comma?](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/)

Extract Last Name using Flash Fill
----------------------------------

Another really fast way to extract the last name from full names is by using the [Flash Fill feature](https://trumpexcel.com/flash-fill-excel/)
 in Excel.

Introduced in Excel 2013, Flash Fill works by identifying patterns based on user input and giving you the same results for all the cells in the column.

Below I have a data set where I have the names in column A and I want to extract the last name in column B.

![Names Dataset for Flash Fill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20467%20385'%3E%3C/svg%3E)

Here are the steps to do this Flash Fill:

1.  In cell B2, manually enter the last name from the name in cell A2

![Enter the expected result in first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20386'%3E%3C/svg%3E)

2.  Select the range in column B where you want the last names (B2:B10 in this example)

![Select the entire column B](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20387'%3E%3C/svg%3E)

3.  Hold the Control key and press the E key (or Command + E if using Mac)

![Flash Fill result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20466%20385'%3E%3C/svg%3E)

_Note: You can also get the same option when you go to the Home tab, click on the Fill icon, and then click on Flash Fill_

The above steps would fill the selected range with the last names from names in Column A.

As I mentioned, Flash Fill works by identifying the pattern in one or two cells where you have manually entered the data and then replicates it for all the other select cells.

In this example, when I entered “Hans” in cell B2, and then used Flash Fill, it recognized that I’m trying to extract the last word from the text string in column A. So we did the same for all the cells I selected.

In case you have a dataset where you have a mix of names with and without a middle name, you can still use Flash Fill to extract the last name.

This is because the pattern that the flash fill has identified is to extract the last word from the text string, so it doesn’t matter how many words are there, it will give you the last name in any case.

Caution: While the flash fill method has worked perfectly in our case, its accuracy is dependent on how well it can identify the pattern. In some cases, it may not be able to identify the right pattern, so it’s important that you double-check the data to make sure it’s correct. In some cases, you may need to enter the data in two or three cells for flash fill to identify the pattern correctly

Compared with the formula method covered above, the flash fill method is a lot faster and more convenient.

One big difference however is that the result of the formula method is dynamic, which means that in case you change the original name, the result in the cell that has the formula would also update.

In the case of Flash Fill, you will have to repeat the same process again to get the updated data

Extract Last Name Using Power Query
-----------------------------------

If you want to automate the process of extracting the last names from full names, Power Query is the way to go.

For example, if you often have a need to separate names in Excel or to extract the first or last name, you can do that once using Power Query, and the next time you need to do it again, you can simply refresh the query with a single click.

Below I have a data set of names and I want to extract the last name from these. Note that I have a mix of names where there are middle names and prefixes in some of the cells.

![Names in an Excel Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%20417'%3E%3C/svg%3E)

Note: When using Power Query, it is best to convert your data into an Excel Table. Doing this would make it a lot easier to work with Power Query, and also allow you to perform the same steps with a single click the next time you add new data set.

To convert your data into an [Excel Table](https://trumpexcel.com/excel-table/)
, select the data and use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 Control + T (or Command + T if using Mac)

Below are the steps to use Power Query to get the last name from this dataset:

1.  Select any cell in the dataset
2.  Click the Data tab in the ribbon

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20223'%3E%3C/svg%3E)

3.  In the ‘Get and Transform Data’ group, click on ‘From Selection’. This will open the Power Query editor

![Click on From Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20656%20223'%3E%3C/svg%3E)

4.  In the PQ Editor, right-click on the column header

![Right click on the column header](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20690%20377'%3E%3C/svg%3E)

5.  Go to the ‘Split Column’ option
6.  Click on By Delimiter option.

![Select By delimiter option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20734%20595'%3E%3C/svg%3E)

6.  In the ‘Split Column by Delimiter’ dilaog box, select Space as the delimiter (if not selected already)

![Make sure Space is selected as the delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20448'%3E%3C/svg%3E)

7.  In the Split at options, select ‘Right-most delimiter’

![Select Right Most Delimiter](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20448'%3E%3C/svg%3E)

8.  Click OK. This will close the dialog box and you will see the result in the PQ Editor

![Names have been split](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20334'%3E%3C/svg%3E)

9.  Rename the columns the way you want (I am going with ‘Full Name’ and ‘Last Name’)

![Rename the columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20325'%3E%3C/svg%3E)

10.  Click on Close and Load option in the ribbon

![Click on Close and Load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20571%20141'%3E%3C/svg%3E)

The above steps would [insert a new worksheet](https://trumpexcel.com/insert-new-worksheet-excel/)
 in your workbook that would have the resulting table.

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20308%20311'%3E%3C/svg%3E)

Note that in the above example, the first name column has the first name as well as the middle name in some cases. In case you only want the last names, you can delete the first column in Power Query, so it will only give you the last name column as the result in the worksheet.

Now if you’re thinking that this is a long method and you’re better off using Flash Fill or formula method instead, you’re probably right.

The scenario where Power Query really shines is when you get a file that has the data and you need to do multiple modifications to it (say delete some [columns, delete blank rows](https://trumpexcel.com/delete-blank-rows-excel/)
, extract the last name, etc).

The next time you get a new file, you won’t have to repeat all these steps again. simply connect your query to the new file and refresh the query.

In such scenarios, Power Query is a far better solution than using flash fill or formulas or even VBA.

So these are three different methods that you can use to extract the last name from full name in Excel. Personally, I prefer using the Flash Fill method in most cases, as it’s fast and quite reliable.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Shuffle a List of Items/Names in Excel?](https://trumpexcel.com/shuffle-list-excel/)
    
*   [How to Combine First and Last Name in Excel)](https://trumpexcel.com/combine-first-and-last-name-excel/)
    
*   [How to Sort by the Last Name in Excel](https://trumpexcel.com/sort-by-last-name-excel/)
    
*   [Extract Usernames from Email Ids in Excel](https://trumpexcel.com/extract-usernames-from-email-ids/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/extract-last-name-excel/#respond)

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