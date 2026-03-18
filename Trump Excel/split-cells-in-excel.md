# How to Split Cells in Excel (separate into multiple columns)

**Source:** https://trumpexcel.com/split-cells-in-excel

---

[Skip to content](https://trumpexcel.com/split-cells-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/split-cells-in-excel/#below-title)

There can be situations when you have to split cells in Excel. These could be when you get the data from a database or you copy it from the internet or get it from a colleague.

A simple example where you need to split cells in Excel is when you have full names and you want to split these into first name and last name.

Or you get address’ and you want to split the address so that you can analyze the cities or the pin code separately.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/split-cells-in-excel/#)

How to Split Cells in Excel
---------------------------

In this tutorial, you’ll learn how to split cells in Excel using the following techniques:

*   Using the [Text to Columns feature](https://trumpexcel.com/excel-text-to-columns-examples/)
    .
*   Using Excel Text Functions.
*   Using Flash Fill (available in 2013 and 2016).

Let’s begin!

### Split Cells in Excel Using Text to Column

Below I have a list of names of some of my favorite fictional characters and I want to split these names into separate cells.:

![Dataset that needs to be Split in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20161%20198'%3E%3C/svg%3E)

Here are the steps to split these names into the first name and the last name:

*   Select the cells in which you have the text that you want to split (in this case A2:A7).
*   Click on the Data tab
*   In the ‘Data Tools’ group, click on ‘Text to Columns’.![Click on the Text to Column option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%20127'%3E%3C/svg%3E)
*   In the Convert Text to Columns Wizard:
    *   **Step 1 of 3 of Text to Columns Wizard**: Make sure Delimited is selected (it is the default selection). This would allow you to separate the first name and the last name based on a specified separator (space bar in this case).![Click on delimited in the Text to Column wizard](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20416'%3E%3C/svg%3E)
    *   Click on Next.
    *   **Step 2 of 3 Text to Columns Wizard**: Select Space as the delimiter and deselect everything else. You can see how your result would look like in the Data preview section of the dialog box.![Select the delimiter in the Text to Column Wizard based on which you want to split cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20417'%3E%3C/svg%3E)
    *   Click on Next.
    *   **Step 3 of 3 Text to Columns Wizard**: In this step, you can specify the data format and where you want the result. I will keep the data format as General as I have text data to split. The default destination is A2 and if you continue with this, it will replace the original data set. If you want to keep the original data intact, select another cell as the destination. In this case, B2 is selected.![Specify destination in Text to Column step 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20416'%3E%3C/svg%3E)
    *   Click on Finish.

This will instantly split the cell’s text into two different columns.

![Resulting data where cells have been split into separate columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20314%20200'%3E%3C/svg%3E)

**_Note:_**

*   _Text to Column feature splits the content of the cells based on the delimiter. While this works well if you want to [separate the first name and the last name](https://trumpexcel.com/separate-first-and-last-name-excel/)
    , in the case of first, middle, and last name it will split it into three parts._
*   _The result you get from using the Text to Column feature is static. This means that if there are any changes in the original data, you’ll have to repeat the process to get updated results._

Also read: [Split Text into Multiple Rows in Excel](https://trumpexcel.com/split-text-to-rows-excel/)

### Split Cells in Excel Using Text Functions

[Excel Text functions](https://trumpexcel.com/excel-functions/)
 are great when you want to slice and dice text strings.

While the Text to Column feature gives a static result, the result that you get from using functions is dynamic and would automatically update when you change the original data.

#### Splitting Names that have a First Name and Last Name

Suppose you have the same data as shown below:

![Split Cells in Excel - Function dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20199%20191'%3E%3C/svg%3E)

**Extracting the First Name**

To get the first name from this list, use the following formula:

\=LEFT(A2,SEARCH(" ",A2)-1)

This formula would spot the first space character and then return all the text before that space character:

![LEFT function to extract the first name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20535%20217'%3E%3C/svg%3E)

This formula uses the SEARCH function to get the position of the space character. In the case of Bruce Wayne, the space character is in the 6th position. It then extracts all the characters to the left of it by using the LEFT function.

**Extracting the Last Name**

Similarly, to get the last name, use the following formula:

\=RIGHT(A2,LEN(A2)-SEARCH(" ",A2))

![Right function to extract the last name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20207'%3E%3C/svg%3E)

This formula uses the search function to find the position of the spacebar using the [SEARCH](https://trumpexcel.com/excel-search-function/)
 function. It then subtracts that number from the total length of the name (that is given by the [LEN](https://trumpexcel.com/excel-len-function/)
 function). This gives the number of characters in the last name.

This last name is then extracted by using the [RIGHT](https://trumpexcel.com/excel-right-function/)
 function.

_**Note:** These functions may not work well if you have leading, trailing or double spaces in the names. [Click here](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 to learn how to remove leading/trailing/double spaces in Excel._

#### Splitting Names that have a First Name, Middle Name, and Last Name

There may be cases when you get a combination of names where some names have a middle name as well.

![Data set with middle name that needs to be split in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20175%20173'%3E%3C/svg%3E)

The formula in such cases is a bit complex.

**Extracting the First Name**

To get the first name:

\=LEFT(A2,SEARCH(" ",A2)-1)

This is the same formula we used when there was no middle name. It simply looks for the first space character and returns all the characters before the space.

**Extracting the Middle Name**

To get the Middle Name:

\=IFERROR([MID](https://trumpexcel.com/excel-mid-function/)
(A2,SEARCH(" ",A2)+1,SEARCH(" ",A2,SEARCH(" ",A2)+1)-SEARCH(" ",A2)),"")

MID function starts from the first space character and extracts the middle name by using the difference of the position of the first and the second space character.

In cases there is no middle name, the MID function returns an error. To avoid the error, it is wrapped within the [IFERROR](https://trumpexcel.com/excel-iferror-function/)
 function.

**Extracting the Last Name**

To get the Last Name, use the below formula:

\=IF(LEN(A2)-LEN(SUBSTITUTE(A2," ",""))=1,RIGHT(A2,LEN(A2)-SEARCH(" ",A2)),RIGHT(A2,LEN(A2)-SEARCH(" ",A2,SEARCH(" ",A2)+1)))

This formula checks whether there is a middle name or not (by [counting the number of space characters)](https://trumpexcel.com/count-characters-in-excel/)
. If there is only 1 space character, it simply returns all the text to the right of the space character.

But if there are 2, then it spots the second space character and returns the number of characters after the second space.

_Note: These formula works well when you have names that have either the fist name and last name only, or the first, middle, and last name. However, if you have a mix where you have suffixes or salutations, then you’ll have to modify the formulas further._

### Split Cells in Excel Using Flash Fill

[Flash Fill](https://trumpexcel.com/flash-fill-excel/)
 is a new feature introduced in Excel 2013.

It could be really handy when you have a pattern and you want to quickly extract a part of it.

For example, let’s take the first name and the last name data:

![Data that needs to be split in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20199%20191'%3E%3C/svg%3E)

Flash fill works by identifying patterns and replicating it for all the other cells.

Here is how you can extract the first name from the list using Flash Fill:

*   In cell B2, enter the first name for Bruce Wayne (i.e., Bruce).![Enter the first expected result in the adjacent cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20257%20176'%3E%3C/svg%3E)
*   With the cell selected, you’ll notice a small square at the right end of the cell selection. Double click on it. This will fill the same name in all the cells.![Use the Autofill handle to get the result in all the cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20271%20171'%3E%3C/svg%3E)
*   When the cells are filled, at the bottom right you’ll see the Autofill Options icon. Click on it.![Click on the autofill options icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20225'%3E%3C/svg%3E)
*   Select Flash Fill from the list.![Select the Flash Fill option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20442%20293'%3E%3C/svg%3E)
*   As soon as you select Flash Fill, you’ll notice that all the cells update itself and now show the first name for each name.

**How Flash Fill Works?**

Flash Fill looks for the patterns in the data set and replicates the pattern.

Flash Fill is a surprisingly smart feature and works as expected in most of the cases. But it also fails in some cases too.

For example, if I have a list of names that has a combination of names with some having a middle name and some don’t.

If I extract the middle name in such a case, Flash Fill will erroneously [return the last name](https://trumpexcel.com/extract-last-name-excel/)
 in case there is no first name.

![How to Split Cells in Excel - Flash Fill error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20284%20203'%3E%3C/svg%3E)

To be honest, that’s still a good approximation of the trend. However, it is not what I wanted.

But it still is a good enough tool to keep in your arsenal and use whenever the need arises.

Here is another example where Flash Fill works brilliantly.

I have a set of addresses from which I want to quickly extract the city.

![Using flash fill to split cells in Excel - address dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20269%20250'%3E%3C/svg%3E)

To quickly get the city, enter the city name for the first address  (enter London in cell B2 in this example) and use the autofill to fill all the cells. Now use Flash Fill and will instantly give you the name of the city from each address.

Similarly, you can split the address and extract any part of the address.

Note that this would need the address to be a homogenous data set with the same delimiter (comma in this case).

In case you try and use Flash Fill when there is no pattern, it will show you an error as shown below:

![Flash fill error message](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20845%20134'%3E%3C/svg%3E)

_In this tutorial, I have covered three different ways to split cells in Excel into multiple columns (using Text to Columns, formulas, and Flash Fill)_

Hope you found this Excel tutorial useful.

**You May Also Like the Following Excel Tutorials:**

*   [How to Quickly Combine Cells in Excel.](https://trumpexcel.com/combine-cells-in-excel/)
    
*   [How to Extract a Substring in Excel Using Formulas](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2532881480)
    .
*   [How to Count Cells that Contain Text Strings.](https://trumpexcel.com/count-cells-that-contain-text/)
    
*   [Extract Usernames from Email Ids in Excel \[2 Methods\].](https://trumpexcel.com/extract-usernames-from-email-ids/)
    
*   [How to Split Multiple Lines in a Cell into Separate Cells/Columns](https://trumpexcel.com/split-multiple-lines/)
    
*   [Create All Possible Combinations from Lists in Excel](https://trumpexcel.com/create-all-combinations-from-lists-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

10 thoughts on “How to Split Cells in Excel (separate into multiple columns)”
-----------------------------------------------------------------------------

1.  I would like to know how to split contents of a cell vertically in excel. I mean contents in once cell, say for e.g. for words to be distributed in the below cells vertically (to the below columns). Can you help in this please/
    
    [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-14815)
    
2.  With OneDrive Excel (2020) there is no Data – Text to columns. There is now; on the Data page – Flash Fill  
    On a couple of rows, you set out how you’d like the data to display across your columns. Highlight each column in turn and click on Flash Fill  
    (ensure that there are no spaces between the rows that you want the information to flash fill in)
    
    [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-14333)
    
3.  [http://tutorialway.com/microsoft-excel-font-formatting/](http://tutorialway.com/microsoft-excel-font-formatting/)
      
    check this for excel
    
    [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-7372)
    
4.  Flash Fill is the best….
    
    [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-3738)
    
5.  To extract the last name (last word), we may use this shorter formula.  
    \=TRIM(RIGHT(SUBSTITUTE(A2,” “,REPT(” “,10)),10))  
    To make it more robust, change 10 to LEN(A2)  
    Explanation can be found at the blogpost below:  
    [https://wmfexcel.com/2014/11/17/extract-last-word-from-a-text-string/](https://wmfexcel.com/2014/11/17/extract-last-word-from-a-text-string/)
    
    [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-3514)
    
6.  the destination change is a good tip.. i used to copy the contents into a different column and perfrom text to columns. with this tip, can eliminate one step… thanks Sumit.. keep these coming.
    
    [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-3428)
    
    *   Glad it’ll save you some time Bhaskar 🙂
        
        [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-3451)
        
7.  Great idea. Thanks Sumit.  
    Francis D’Costa, Canada
    
    [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-3414)
    
    *   Thanks for commenting Francis.. Glad you liked it.
        
        [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-3419)
        
    *   Thanks for commenting Francis.. Glad you liked it.
        
        [Reply](https://trumpexcel.com/split-cells-in-excel/#comment-3450)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/split-cells-in-excel/#respond)

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