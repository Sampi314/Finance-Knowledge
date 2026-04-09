# Excel Advanced Filter - A Complete Guide with Examples

**Source:** https://trumpexcel.com/excel-advanced-filter

---

[Skip to content](https://trumpexcel.com/excel-advanced-filter/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-advanced-filter/#below-title)

**Watch Video – Excel Advanced Filter**

Excel Advanced Filter is one of the most underrated and under-utilized features that I have come across.

If you work with Excel, I am sure you have used (or at least heard about the regular excel filter). It quickly filters a data set based on selection, specified text, number or other such criteria.

In this guide, I will show you some cool stuff you can do using the Excel advanced filter.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-advanced-filter/#)

But First… What is Excel Advanced Filter?
-----------------------------------------

Excel Advanced Filter – as the name suggests – is the advanced version of the regular filter. You can use this when you need to use more complex criteria to filter your data set.

Here are some differences between the regular filter and Advanced filter:

*   While the regular data filter will filter the existing dataset, you can use Excel advanced filter to extract the data set to some other location as well.
*   Excel Advanced Filter allows you to use complex criteria. For example, if you have sales data, you can filter data on a criterion where the sales rep is Bob and the region is either North or South (we will see how to do this in examples). [Office support](https://support.office.com/en-us/article/Filter-by-using-advanced-criteria-4c9222fe-8529-4cd7-a898-3f16abdff32b?ui=en-US&rs=en-US&ad=US&fromAR=1)
     has some good explanation on this.
*   You can use the Excel Advanced Filter to extract unique records from your data (more on this in a second).

EXCEL ADVANCED FILTER (Examples)
--------------------------------

Now let’s have a look at some example on using the Advanced Filter in Excel.

### Example 1 – Extracting a Unique list

You can use Excel Advanced Filter to quickly extract unique records from a data set (or in other words remove duplicates).

In Excel 2007 and later versions, there is an option to [remove duplicates](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
 from a dataset. But that alters your existing data set. To keep the original data intact, you need to create a copy of the data and then use the Remove Duplicates option. Excel Advanced filter would allow you to select a location to get a unique list.

Let’s see how to use an advanced filters to get a unique list.

Suppose you have a dataset as shown below:

![Excel Advanced Filter - Sales Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20314%20432'%3E%3C/svg%3E)

As you can see, there are duplicate records in this data set (highlighted in orange). These could be due to an error in [data entry](https://trumpexcel.com/excel-data-entry-tips/)
 or result of data compilation.

In such a case, you can use Excel Advanced Filter tool to quickly get a list of all the unique records in a different location (so that your original data remains intact).

Here are the steps to get all the unique records:

*   Select the entire data set (including the headers).
*   Go Data tab –> Sort & Filter –> Advanced. (You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     _– Alt + A + Q_). This will open the Advanced Filter dialog box.![Excel Advanced Filter - Data Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20363%20145'%3E%3C/svg%3E)
*   In the Advanced Filter dialog box, use the following details:
    *   _Action:_ Select the ‘Copy to another location’ option. This will allow you to specify the location where you can get the list of unique records.
    *   _List Range:_ Make sure it refers to the dataset from which you want to find unique records. Also, make sure headers in the data set are included.
    *   _Criteria Range:_ Leave this empty.
    *   _Copy To:_ Specify the cell address where you want to get the list of unique records.
    *   _Copy Unique Records Only:_ Check this option.![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20236%20238'%3E%3C/svg%3E)
*   Click OK.

This will instantly give you a list of all the unique records.

![Excel Advanced Filter - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20760%20600'%3E%3C/svg%3E)

**_Caution:_** When you are using Advanced Filter to get the unique list, make sure you have also selected the header. If you don’t, it would consider the first cell as the header.

### Example 2 – Using Criteria in Excel Advanced Filter

Getting unique records is one of the many things you can do with Excel advanced filter.

Its primary utility lies in its ability to allow using complex criteria for filtering data.

Here is what I mean by complex criteria. Suppose you have a dataset as shown below and you want to quickly get all the records where the sales are greater than 5000 and the region is the US.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20414%20374'%3E%3C/svg%3E)

Here is how you can use Excel Advanced Filter to filter the records based on the specified criteria:

*   The first step when using Excel Advanced Filter with complex criteria is to specify the criteria. To do this, copy the headers and paste it somewhere in the worksheet.![Excel Advanced Filter - criteria copy](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20373'%3E%3C/svg%3E)
*   Specify the criteria for which you want to filter the data. In this example, since we want to get all the records for the US with sales more than 5000, enter ‘US’ in the cell below Region and >5000 in the cell below Sales. This would now be used as an input in Advanced Filter to get the filtered data (as shown in the next steps).![Excel Advanced Filter - criteira Specify](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20751%20369'%3E%3C/svg%3E)
*   Select the entire data set (including the headers).
*   Go Data tab –> Sort & Filter –> Advanced. This will open the Advanced Filter dialog box.![Excel Advanced Filter - Data Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20363%20145'%3E%3C/svg%3E)
*   In the Advanced Filter dialog box, use the following details:
    *   _Action:_ Select the ‘Copy to another location’ option. This will allow you to specify the location where you can get the list of unique records.
    *   _List Range:_ Make sure it refers to the dataset from which you want to find unique records. Also, make sure headers in the data set are included.
    *   _Criteria Range:_ Specify the criteria we constructed in the steps above. In this example, it would be F1:I3.
    *   _Copy To:_ Specify the cell address where you want to get the list of unique records.
    *   _Copy Unique Records Only:_ Check this option.
*   Click OK.

This would instantly give you all the records where the region is the US and the sales are more than 5000.

![Excel Advanced Filter - complex criteria demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20544'%3E%3C/svg%3E)

The above example is a case where the filtering is done based on two criteria (US and sales greater than 5000).

Excel Advanced filter allows you to create many different combinations of criteria.

Here are some examples of how you can construct these filters.

#### Using the AND Criteria

When you want to use AND criteria, you need to specify it below the header.

For example:

*   To filter records when the region is the US AND the sales rep is Joe.![Excel Advanced Filter - AND Criteria 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20330%2075'%3E%3C/svg%3E)
*   To filter records when the region is the US AND the sales value is greater than 5000.![Excel Advanced Filter - AND Criteria 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20328%2075'%3E%3C/svg%3E)
*   When the region is the US AND the sales are recorded after 31-03-2017.![Excel Advanced Filter - AND Criteria 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20346%2079'%3E%3C/svg%3E)

#### Using the OR Criteria

When you want to use OR criteria, you need to specify the criteria in the same column.

For example:

*   To filter records when the region is the US OR the region is Asia.![Excel Advanced Filter - OR Criteria 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20347%2098'%3E%3C/svg%3E)
*   To filter records when the Sales rep is Bob OR Martha.![Excel Advanced Filter - OR Criteria 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20344%2095'%3E%3C/svg%3E)

By now, you must have realized that when we have the criteria in the same row, it is an **AND** criteria, and when we have it in different rows, it is an **OR** criteria.

### Example 3 – Using WILDCARD Characters in Advanced Filter in Excel

Excel Advanced Filter also allows the usage of wildcard characters while constructing the criteria.

There are three [wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
 in Excel:

1.  **\* (asterisk)** – It represents any number of characters. For example, ex\* could mean excel, excels, example, expert, etc.
2.  **? (question mark)** – It represents one single character. For example, Tr?mp could mean Trump or Tramp.
3.  **~ (tilde)** – It is used to identify a wildcard character (~, \*, ?) in the text.

Now let’s see how we can use these wildcard characters to do some advanced filtering in Excel.

*   To filter records where the sales rep name starts from J. ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20343%2075'%3E%3C/svg%3E)

Note that \* represent any number of characters. So any rep with the name starting with J would be filtered with these criteria.

Similarly, you can use the other two wildcard characters as well.

_Note: In case you’re using Office 365, you should check out the [FILTER function](https://trumpexcel.com/filter-function/)
. It can do a lot of things that advanced filter can do with a simple formula._

NOTE:

1.  _Remember, the headers in the criteria should be exactly the same as that in the data set._
2.  _Advanced filtering cannot be undone when copied to other locations.  
    _

**You May Also Like the Following Excel Tutorials:**

*   [Dynamic Excel Filter – Extract Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    .
*   [Filtering Cells with Bold Font Formatting](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    .
*   [How to Filter Cells that have Duplicate Text Strings (Words) in it.](https://trumpexcel.com/duplicate-text-strings/)
    
*   [How to Filter Data in a Pivot Table in Excel](https://trumpexcel.com/filter-data-pivot-table-excel/)
    
*   [MS Guide for Advanced Filter in Excel](https://support.office.com/en-ie/article/Filter-by-using-advanced-criteria-4c9222fe-8529-4cd7-a898-3f16abdff32b)
    .
*   [How to Compare Two Columns in Excel.](https://trumpexcel.com/compare-two-columns/)
    
*   [Excel VBA Autofilter](https://trumpexcel.com/vba-autofilter/)
    
*   [20 Advanced Excel Functions and Formulas (for Excel Pros)](https://trumpexcel.com/advanced-excel-functions-formulas/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

20 thoughts on “Excel Advanced Filter – A Complete Guide with Examples”
-----------------------------------------------------------------------

1.  hi  
    my question : how to use’ wild card’ when we have ‘between ‘ in the advance filter.  
    question: if we want to find a product whos purchasing number is between 2000 to 5000 dollar or the salesperson is David
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-14391)
    
2.  Am looking to filter out (that is, \*exclude\*) from the results any value in the data containing the letters ‘cul’ in a specific column. I don’t see here how to do that.
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-14184)
    
3.  I want to filter a data set using advanced filter on “ram”. But the result includes not only “ram” but also the row containing “raman”. How do I get only the result for “ram”?
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-13773)
    
4.  your explanation of advance filter option is great.  
    Thank You So much.
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-13689)
    
5.  Hi, I have two columns A&B I need to see where column A data has different numbers in column B. So if column A has 123 and column B has two different numbers associated with 123 I need to see those highlighted in some way. Does anybody know how to do this?
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-13635)
    
6.  you can only copy filtered data to the active sheet; you cannot copy to a different tabbed sheet
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-13122)
    
7.  List out Different between filter and advance filter
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-12873)
    
8.  I am trying to use formulas in my advanced-filter criteria where my database is in a separate (external) workbook from my extract sheet. It works if I don’t use a formula. Is this possible and, if so, what is the syntax?
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-12616)
    
9.  I have a data containing score of students. I wish to obtain names of those students who have scored between 50 and 70 marks.
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-12606)
    
10.  Advance filter not working in ms office 2007. what to do ?
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-12323)
    
11.  thanks for your explanation I have how to use some of tool in excel
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-12049)
    
12.  Hi, I have a query regarding excel. I want to filter with multiple items in a single column so can I do that without going into the dropdown? Please help
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-11452)
    
13.  Hi advance filter is not working in close workbook,I want to apply advance filter in close workbook please help
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-10796)
    
14.  Your Tutorial is Mind blowing  
    You Explained in detail and it is most useful.  
    Please describe is you can, If there is a column of ‘Date of Birth’ and I want to extract only records that having their date of birth in November Month.  
    Thanking You
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-10751)
    
    *   Suppose A2:A10 contains your dates, with the header in A1. Find a pair of blank cells, one below the other — I’ll assume E2 and E3. Leave E2 blank, and in E3 enter the formula \`=MONTH(A2)=11\` (specifically, A2 is the first data cell in the date column, and November is the 11th month). Apply an advanced filter, using A1:A10 as the list range, and E2:E3 as the criteria range.
        
        [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-12046)
        
15.  Nice Tutorial of Advance Filter
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-10408)
    
16.  dude you are awesome. Thank you. I was just searching the shortcut for search option in filter which A+ down arrow+ E… but here I learned some thing highly valuable.
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-2349)
    
17.  Well explained, it is most useful in the day to work. Thanks a lot.
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-2215)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-2218)
        
18.  How to Create the Volookup Table in Excel with VBA
    
    [Reply](https://trumpexcel.com/excel-advanced-filter/#comment-1509)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-advanced-filter/#respond)

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