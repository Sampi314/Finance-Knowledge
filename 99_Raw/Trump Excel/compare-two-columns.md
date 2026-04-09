# How to Compare Two Columns in Excel (for matches & differences)

**Source:** https://trumpexcel.com/compare-two-columns

---

[Skip to content](https://trumpexcel.com/compare-two-columns/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/compare-two-columns/#below-title)

**Watch Video – Compare two Columns in Excel for matches and differences**

The one query that I get a lot is – ‘how to compare two columns in Excel?’.

This can be done in many different ways, and the method to use will depend on the data structure and what the user wants from it.

For example, you may want to compare two columns and find or highlight all the matching data points (that are in both the columns), or only the differences (where a data point is in one column and not in the other), etc.

Since I get asked about this so much, I decided to write this massive tutorial with an intent to cover most (if not all) possible scenarios.

If you find this useful, do pass it on to other Excel users.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/compare-two-columns/#)

Note that the techniques to compare columns shown in this tutorial are not the only ones.

Based on your dataset, you may need to change or adjust the method. However, the basic principles would remain the same.

If you think there is something that can be added to this tutorial, let me know in the comments section

Compare Two Columns For Exact Row Match
---------------------------------------

This one is the simplest form of comparison. In this case, you need to do a row by row comparison and identify which rows have the same data and which ones does not.

### Example: Compare Cells in the Same Row

Below is a data set where I need to check whether the name in column A is the same in column B or not.

![Compare Columns - row by row - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20442%20308'%3E%3C/svg%3E)

If there is a match, I need the result as “TRUE”, and if doesn’t match, then I need the result as “FALSE”.

The below formula would do this:

\=A2=B2

![Compare Lists in Excel - matches are shown as TRUE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20582%20366'%3E%3C/svg%3E)

### Example: Compare Cells in the Same Row (using IF formula)

If you want to get a more descriptive result, you can use a [simple IF formula](https://trumpexcel.com/excel-if-function/)
 to return “Match” when the names are the same and “Mismatch” when the names are different.

\=IF(A2=B2,"Match","Mismatch")

![If formula to compare columns in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20581%20365'%3E%3C/svg%3E)

Note: In case you want to make the comparison case sensitive, use the following IF formula:

\=IF(EXACT(A2,B2),"Match","Mismatch")

With the above formula, ‘IBM’ and ‘ibm’ would be considered two different names and the above formula would return ‘Mismatch’.

### Example: Highlight Rows with Matching Data

If you want to highlight the rows that have matching data (instead of getting the result in a separate column), you can do that by using [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
.

Here are the steps to do this:

1.  Select the entire dataset.
2.  Click the ‘Home’ tab.![Click the Home Tab in the Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20352%20159'%3E%3C/svg%3E)
3.  In the Styles group, click on the ‘Conditional Formatting’ option.![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20390%20136'%3E%3C/svg%3E)
4.  From the drop-down, click on ‘New Rule’.![Click on the New Rule option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20242%20460'%3E%3C/svg%3E)
5.  In the ‘New Formatting Rule’ dialog box, click on the ‘Use a formula to determine which cells to format’.![Click on Use Formula option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
6.  In the formula field, enter the formula: =$A1=$B1![Formula to compare columns in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
7.  Click the Format button and specify the format you want to apply to the matching cells.![Set Formatting in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
8.  Click OK.

This will highlight all the cells where the names are the same in each row.

![Compare two columns and highlight matching rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20310'%3E%3C/svg%3E)

Compare Two Columns and Highlight Matches
-----------------------------------------

If you want to compare two columns and highlight matching data, you can use the duplicate functionality in conditional formatting.

Note that this is different than what we have seen when comparing each row. In this case, we will not be doing a row by row comparison.

### Example: Compare Two Columns and Highlight Matching Data

Often, you’ll get datasets where there are matches, but these may not be in the same row.

Something as shown below:

![Compare two columns and highlight macthes - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20395'%3E%3C/svg%3E)

Note that the list in column A is bigger than the one in B. Also some names are there in both the lists, but not in the same row (such as IBM, Adobe, Walmart).

If you want to highlight all the matching company names, you can do that using conditional formatting.

Here are the steps to do this:

1.  Select the entire data set.
2.  Click the Home tab.
3.  In the Styles group, click on the ‘Conditional Formatting’ option.![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20390%20136'%3E%3C/svg%3E)
4.  Hover the cursor on the Highlight Cell Rules option.
5.  Click on Duplicate Values.![Select Duplicate Values in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20499'%3E%3C/svg%3E)
6.  In the Duplicate Values dialog box, make sure ‘Duplicate’ is selected.![Duplicate in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20159'%3E%3C/svg%3E)
7.  Specify the formatting.![Specify the formatting in conditional formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20159'%3E%3C/svg%3E)
8.  Click OK.

The above steps would give you the result as shown below.

![Highlighted matching data when comparing lists in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20395'%3E%3C/svg%3E)

Note: Conditional Formatting duplicate rule is not case sensitive. So ‘Apple’ and ‘apple’ are considered the same and would be highlighted as duplicates.

### Example: Compare Two Columns and Highlight Mismatched Data

In case you want to highlight the names which are present in one list and not the other, you can use the conditional formatting for this too.

1.  Select the entire data set.
2.  Click the Home tab.
3.  In the Styles group, click on the ‘Conditional Formatting’ option.![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20390%20136'%3E%3C/svg%3E)
4.  Hover the cursor on the Highlight Cell Rules option.
5.  Click on Duplicate Values.![Select Duplicate Values in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20499'%3E%3C/svg%3E)
6.  In the Duplicate Values dialog box, make sure ‘Unique’ is selected.![Select Unique to highlight differences](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20159'%3E%3C/svg%3E)
7.  Specify the formatting.![Specify the formatting to highlight differences in two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20159'%3E%3C/svg%3E)
8.  Click OK.

This will give you the result as shown below. It highlights all the cells that have a name that is not present on the other list.

![Compare Two columns and highlight differences](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20441%20396'%3E%3C/svg%3E)

Compare Two Columns and Find Missing Data Points
------------------------------------------------

If you want to identify whether a data point from one list is present in the other list, you need to use the lookup formulas.

Suppose you have a dataset as shown below and you want to identify companies that are present in column A but not in Column B,

![Compare two columns and highlight macthes - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20440%20395'%3E%3C/svg%3E)

To do this, I can use the following [VLOOKUP formula](https://trumpexcel.com/excel-vlookup-function/)
.

\=ISERROR(VLOOKUP(A2,$B$2:$B$10,1,0))

This formula uses the VLOOKUP function to check whether a company name in A is present in column B or not. If it is present, it will return that name from column B, else it will return a #N/A error.

These names which return the #N/A error are the ones that are missing in Column B.

ISERROR function would return TRUE if there is the VLOOKUP result is an error and FALSE if it isn’t an error.

![compare lists and find missing data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20337'%3E%3C/svg%3E)

If you want to get a list of all the names where there is no match, you can filter the result column to get all cells with TRUE.

You can also use the MATCH function to do the same;

\=NOT(ISNUMBER(MATCH(A2,$B$2:$B$10,0)))

Note: Personally, I prefer using the Match function (or the [combination of INDEX/MATCH](https://trumpexcel.com/index-match/)
) instead of VLOOKUP. I find it more flexible and powerful. You can read the [difference between Vlookup and Index/Match here](https://trumpexcel.com/vlookup-vs-index-match/)
.

Compare Two Columns and Pull the Matching Data
----------------------------------------------

If you have two datasets and you want to compare items in one list to the other and fetch the matching data point, you need to use the lookup formulas.

### Example: Pull the Matching Data (Exact)

For example, in the below list, I want to fetch the market valuation value for column 2. To do this, I need to look up that value in column 1 and then fetch the corresponding market valuation value.

![Compare two lists in Excel and fetch matching data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20682%20364'%3E%3C/svg%3E)

Below is the formula that will do this:

\=VLOOKUP(D2,$A$2:$B$14,2,0)

or

\=INDEX($A$2:$B$14,MATCH(D2,$A$2:$A$14,0),2)

![Lookup and Pull matching data - market valuation Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20689%20418'%3E%3C/svg%3E)

### Example: Pull the Matching Data (Partial)

In case you get a dataset where there is a minor difference in the names in the two columns, using the above-shown lookup [formulas is not going to work](https://trumpexcel.com/excel-formulas-not-working/)
.

These lookup formulas need an exact match to give the right result. There is an approximate match option in VLOOKUP or [MATCH function](https://trumpexcel.com/excel-match-function/)
, but that can’t be used here.

Suppose you have the data set as shown below. Note that there are names that are not complete in Column 2 (such as JPMorgan instead of JPMorgan Chase and Exxon instead of ExxonMobil).

![Pull matching Data - partial match](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20360'%3E%3C/svg%3E)

In such a case, you can use a partial lookup by using [wildcard characters](https://trumpexcel.com/excel-wildcard-characters/)
.

The following formula will give is the right result in this case:

\=VLOOKUP("\*"&D2&"\*",$A$2:$B$14,2,0)

or

\=INDEX($A$2:$B$14,MATCH("\*"&D2&"\*",$A$2:$A$14,0),2)

![Partial comparison in columns with wildcard characters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20682%20414'%3E%3C/svg%3E)

In the above example, the asterisk (\*) is a wildcard character that can represent any number of characters. When the lookup value is flanked with it on both sides, any value in Column 1 which contains the lookup value in Column 2 would be considered as a match.

For example, \*Exxon\* would be a match for ExxonMobil (as \* can represent any number of characters).

**You May Also Like the Following Excel Tips & Tutorials:**

*   [How to Compare Two Excel Sheets (for differences)](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Highlight Blank Cells in Excel.](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [How to Compare Text in Excel (Easy Formulas)](https://trumpexcel.com/compare-text-excel/)
    
*   [Highlight EVERY Other ROW in Excel.](https://trumpexcel.com/highlight-every-other-row-excel/)
    
*   [Excel Advanced Filter: A Complete Guide with Examples](https://trumpexcel.com/excel-advanced-filter/)
    .
*   [Highlight Rows Based on a Cell Value in Excel](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    
*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    
*   [Compare Two Lists (Free Online Tool)](https://trumpexcel.com/tools/compare-two-lists/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

59 thoughts on “How to Compare Two Columns in Excel (for matches & differences)”
--------------------------------------------------------------------------------

1.  Fantastic tutorial video! Thank you so much for your help.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14914)
    
2.  best explain
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14907)
    
3.  Need help. Here is my problem.  
    ID Rate ID Months Rate  
    R000034567 00 51287 R000034567 12  
    R000034565 00 4587 R000034565 6  
    R000034562 00 6528 R000034562 8
    
    Trying to fill the rates to the last column based on the ID. What would the formula be to compare the two ID column.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14891)
    
4.  Can you please show matching with recurring values in both data sets?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14884)
    
5.  Hi, I have another question about “Compare Two Columns and Highlight Mismatched Data”. This helps to identify unique values in 2 columns A and B , but it fails if suppose there are 2 similar values in Column A and that value doesn’t exits in Column B, it should highlight it because it is a mismatch in Column A and Column B but it doesn’t do that. It should not check for duplicates within same column as that is not my goal. I want to strictly compare Column A and Column B
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14814)
    
6.  I have a question , I have set of values (separated by new line in notepad), and I want to highlight those column which matches those set of values.  
    Suppose I have in my notepad each in new line following value – ABC, XYZ, MTX, LAB etc.  
    And I have a column which has 200 entries with some of the entries contains above values. How do I highlight those columns?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14808)
    
7.  The example where you highlight matches in both columns where the values are in different positions using the duplicates option unfortunately also highlights duplicates within the same column and does not need to exist at all in the other column.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14649)
    
8.  Hi Sir, is it possible to assist me on how to get the top importer who has the most entries/transactions for a certain period? Can I send the sample file to you? Thanks
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14580)
    
9.  You made it very easy to compare two columns, thanks!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14416)
    
10.  Thank you soo much
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14338)
    
11.  Is there a way to compare data with a “contains similar” type of lens? I want to be able to find names like, “Harry & Son” and “Harry and Son” and “Harry and Son LTD.” ETC.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14307)
    
12.  excellent summary, not too much not too little , with excellent visuals, mission accomplished thanks
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14292)
    
13.  I cannot get any of the above to work accurately when looking for matches in every row across two columns when using dates – I can see matching dates but the formula gives a negative instead of a positive match. Any help to resolve?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-14274)
    
14.  Hi there – I’ve been looking but I don’t think I have yet found a tutorial for my use-case. I wonder if you have one or can answer my question. I have two sets of two columns of non-matching data (1st set has a set of names and values across date period 1, 2nd set has a set of names and values across date period 2) but whilst some of the names repeat in both data sets there are also names that are unique to set 1 and set 2. I wish to put those names (and their corresponding values) that are common to both data sets on the same row and then, beneath these common names, list those that are unique to each list. Is there a route to this?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13771)
    
15.  It did the job 🙂 very helpful. Thank you
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13601)
    
16.  Very Helpful.  
    Thank You
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13598)
    
17.  Thank you! Helped me a lot! 🙂
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13585)
    
18.  Very resourceful please share your email, I send my problem for help. Thanks keep it up. Best regards.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13509)
    
19.  I really liked your simple explanation to excel but still can’t find a tool to edit my numbers. Thanks
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13507)
    
20.  Thank you. This was helpful
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13206)
    
21.  I have two columns. I need copy item name that same name or diferent name from that columns  
    . please
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13115)
    
22.  This was extremely helpful. Thank You.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-13002)
    
23.  I have some values in first column and some values in second column I want all the values that are duplicate in first column and second column in other column in other sheet
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12744)
    
24.  I have 3 columns. One is on the first tab and the other 2 are on the second tab. I want the column on the first tab to find any matching values in the column in the second tab. If there is a match/multiple matches, I want it to grab the values in the 3 column on the second tab and return the sum. Hope this makes sense and there is someone that can assist!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12717)
    
25.  any option to delete unique data in two column..
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12700)
    
26.  Thank you. This was helpful!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12627)
    
    *   Is this your real name 🙂
        
        [Reply](https://trumpexcel.com/compare-two-columns/#comment-12807)
        
27.  You are absolutely the hero of the day. Your tutorial shows me the way to cross reference thousands of data points and pull over the missing data I needed, in just a matter of minutes. THANK YOU!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12517)
    
28.  This is a great article, thanks a lot.  
    Many people don’t know that one can use SQL statements to access Excel spreadsheets. I wrote a tool called SelectCompare that facilitates comparison of data sets, among others Excel spreadsheets. There is quite a bit of documentation on the website how to set up data connection and write SELECT statements.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12516)
    
    *   Where can one find your “SELECTCOMPARE” tool?
        
        [Reply](https://trumpexcel.com/compare-two-columns/#comment-13642)
        
29.  I have 2 lists:  
    1) One has names with scores. The names are in alphabetical order.
    
    2)The other has the same names. No scores and the names are in groups. Not in the alphabetical order.
    
    Is there away I can combine the two lists so the score appears next to the name; without affecting the groups?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12450)
    
    *   Hello, you can try using the Vlookup function in order to get your scores for the requested names.
        
        [Reply](https://trumpexcel.com/compare-two-columns/#comment-12502)
        
30.  A great article! Elaborately explained which makes easy to understand. Thanks  
    a lot!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-12272)
    
31.  This was extremely helpful. Thanks!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11998)
    
32.  I find this quite helpful. Thank you!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11990)
    
33.  Great examples. Helped me alot !!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11897)
    
34.  This seems to be handy book for any serious data analyst
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11896)
    
35.  Will, that helped me a lot . Big thanks to you guys
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11838)
    
36.  I’ve tried each of your formulas. None work, so I have to be doing something wrong — this can’t be a unique problem.
    
    I have 433 names in Column A, and 298 in Column B. All the names in Column B are also in A, and I formatted all of them to be identical spellings, all surnames. So what I want are the 135 names in Column A that are not in Column B to appear in Column C.
    
    If Excel can’t do that (which would astonish me), even just highlighting either all the duplicates (that is, names in BOTH columns), and NOT the unique names in Column A, would help.
    
    The best I can get instead is duplicates WITHIN a column — that is, it will highlight “Bishop Bishop” (two different people with the same name) in each column. But not matter what I do, I can’t get Excel to highlight “Adams” because it is in both columns, nor “Abraham” because it is only in Column A.
    
    Help?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11818)
    
    *   You can use vlookup or index/match to look for those names in B which also appear in A, then it will return #N/A for those names that are not found. And you can sort/filter as applicable.
        
        [Reply](https://trumpexcel.com/compare-two-columns/#comment-12506)
        
37.  Good Job. it is very useful to save our time. if your can help me on the following also appreciated.  
    I want to find same value in two column as debit and credit. how to select those value in excel formula( this is just reconciling debit credit entries updated in Excel)
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11805)
    
38.  Thank you!! This gave me exactly what I wanted to know after searching other places for ten minutes.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11764)
    
39.  I need help comparing two columns for duplicates and unique values. I know I can do this using conditional formatting however my issue is that for example in column 1 I have duplicates so when I apply the conditional formatting it is picking the duplicates up in the same column however I only want to pick up the duplicates against the two columns. E.g.
    
    Column 1 could have:  
    Red  
    Yellow  
    Red  
    Green
    
    Column 2 could have:  
    Yellow  
    Blue  
    Purple  
    Green
    
    When I apply the conditional formatting it picks up Red as a duplicate as it appears twice in column one but only want to find duplicates comparing the two columns so I would like it to pick up: Yellow and Green.
    
    How can I achieve this?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-11393)
    
    *   Hi Tricia, I have the same problem as you.If by now you do know how to solve it please let me know. Thanks a ton!
        
        [Reply](https://trumpexcel.com/compare-two-columns/#comment-12309)
        
40.  I need help on how to compare everyday Item that we’re sold. Then I need to put the comparison price list. How do I check if Price was already there so I do not have to do it again?
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10990)
    
41.  thanks a lot for your support which has given me great support in my work and please share the formulas to pullout the duplicates separate from the data.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10602)
    
42.  Wonderful!
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10584)
    
43.  nice tips
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10369)
    
44.  Like you read my mind and know that this is what I am already searching for.  
    Thanks
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10339)
    
45.  Genius
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10333)
    
46.  Thank you, nice work
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10330)
    
47.  Very useful to solve two columns comparison..  
    Thanks
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10324)
    
48.  Well done
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10323)
    
49.  Usefull Excell tips for me.  
    Thanks.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10319)
    
50.  usefull, thankss
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10317)
    
51.  Excellen
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10316)
    
52.  Very Use full Excel Trick.
    
    [Reply](https://trumpexcel.com/compare-two-columns/#comment-10310)
    
    *   Glad you found the tutorial useful Virendra!
        
        [Reply](https://trumpexcel.com/compare-two-columns/#comment-10311)
        
        *   very useful, thank you Sumit. If you can assist on another similar case. I need to use conditional formation where, if I want to compare two numbers and use colour to identify the difference, be it positive or negative. For an example: If value is cell A is lower than a value in cell B, then highlight be in Red, otherwise highlight cell B in green. I need to use this to highlight variances in sales targets vs actual sales on different product lines.
            
            [Reply](https://trumpexcel.com/compare-two-columns/#comment-10352)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/compare-two-columns/#respond)

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