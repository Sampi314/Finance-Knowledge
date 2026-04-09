# How to Use VLOOKUP with Multiple Criteria in Excel

**Source:** https://trumpexcel.com/vlookup-with-multiple-criteria

---

[Skip to content](https://trumpexcel.com/vlookup-with-multiple-criteria/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vlookup-with-multiple-criteria/#below-title)

**Watch Video – How to Use VLOOKUP Function with Multiple Criteria**

[Excel VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
, in its basic form, can look for one lookup value and return the corresponding value from the specified row.

But often there is a need to use the Excel VLOOKUP with multiple criteria.

How to Use VLOOKUP with Multiple Criteria
-----------------------------------------

Suppose you have a data with students name, exam type, and the Math score (as shown below):

![VLOOKUP with Multiple Criteria - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20567%20353'%3E%3C/svg%3E)

Using the VLOOKUP function to get the Math score for each student for respective exam levels could be a challenge.

One can argue that a better option would be to restructure the data set or use a [Pivot Table](https://trumpexcel.com/pivot-table/)
. If that works for you, nothing like that. But in many cases, you are stuck with the data that you have and pivot table may not be an option.

In such cases, this tutorial is for you.

Now there are two ways you can get the lookup value using VLOOKUP with multiple criteria.

*   Using a Helper Column.
*   Using the CHOOSE function.

### VLOOKUP with Multiple Criteria – Using a Helper Column

I am a fan of helper columns in Excel.

I find two significant advantages of using helper columns over array formulas:

*   It makes it easy to understand what’s going on in the worksheet.
*   It makes it faster as compared with the array functions (noticeable in large data sets).

Now, don’t get me wrong. I am not against array formulas. I love the amazing things can be done with array formulas. It’s just that I save them for special occasions when all other options are of no help.

Coming back to the question in point, the helper column is needed to create a unique qualifier. This unique qualifier can then be used to lookup the correct value. For example, there are three Matt in the data, but there is only one combination of Matt and Unit Test or Matt and Mid-Term.

Here are the steps:

*   Insert a Helper Column between column B and C.![VLOOKUP with Multiple Criteria - Helper Column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20352'%3E%3C/svg%3E)
*   Use the following formula in the helper column:\=A2&”|”&B2
    *   This would create unique qualifiers for each instance as shown below.![VLOOKUP with Multiple Criteria - Unique Qualifiers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20367%20353'%3E%3C/svg%3E)
*   Use the following formula in G3 \=VLOOKUP($F3&”|”&G$2,$C$2:$D$19,2,0)
*   Copy for all the cells.

![VLOOKUP with Multiple Criteria - result helper](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20385'%3E%3C/svg%3E)

**How does this work?**

We create unique qualifiers for each instance of a name and the exam. In the VLOOKUP function used here, the lookup value was modified to $F3&”|”&G$2 so that both the lookup criteria are combined and are used as a single lookup value. For example, the lookup value for the VLOOKUP function in G2 is Matt|Unit Test. Now this lookup value is used to get the score from C2:D19.

**Clarifications:**

There are a couple of questions that are likely to come to your mind, so I thought I will try and answer it here:

*   **Why have I used | symbol while joining the two criteria?** – In some exceptionally rare (but possible) conditions, you may have two criteria that are different but ends up giving the same result when combined. Here is a very simple example (forgive me for my lack of creativity here):

![VLOOKUP with Multiple Criteria - Why separator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20482%20131'%3E%3C/svg%3E)

Note that while A2 and A3 are different and B2 and B3 are different, the combinations end up being the same. But if you use a separator, then even the combination would be different (D2 and D3).

*   **Why did I insert the helper column between column B and C and not in the extreme left? –** There is no harm in inserting the helper column to the extreme left. In fact, if you don’t want to temper with the original data, that should be the way to go. I did it as it makes me use less number of cells in the VLOOKUP function. Instead of having 4 columns in the table array, I could manage with only 2 columns. But that’s just me.

Now there is no one size that fits all. Some people may prefer to not use any helper column while using VLOOKUP with multiple criteria.

So here is the non-helper column method for you.

**_Download the Example File_**  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/03/VLOOKUP-Multiple-Criteria.xlsx)

### VLOOKUP with Multiple Criteria – Using the CHOOSE Function

Using array formulas instead of helper columns saves you worksheet real estate, and the performance can be equally good if used less number of times in a workbook.

Considering the same data set as used above, here is the formula that will give you the result:

\=VLOOKUP($E3&”|”&F$2,CHOOSE({1,2},$A$2:$A$19&”|”&$B$2:$B$19,$C$2:$C$19),2,0)

Since this is an array formula, use it with Control + Shift + Enter, instead of just Enter.

![VLOOKUP with Multiple Criteria - array choose](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20567%20353'%3E%3C/svg%3E)

**How does this work?**

The formula also uses the concept of a helper column. The difference is that instead of putting the helper column in the worksheet, consider it as virtual helper data that is a part of the formula.

Let me show you what I mean by virtual helper data.

![VLOOKUP with Multiple Criteria - Virtual Helper Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20668%20388'%3E%3C/svg%3E)

In the above illustration, as I select the CHOOSE part of the formula and press F9, it shows the result that the CHOOSE formula would give.

The result is {“Matt|Unit Test”,91;”Bob|Unit Test”, 52;……}

It’s an array where a comma represents next cell in the same row and semicolon represents that the following data is in the next column. Hence, this formula creates 2 columns of data – One column has the unique identifier and one has the score.

Now, when you use the VLOOKUP function, it simply looks for the value in the first column (of this virtual 2 column data) and returns the corresponding score.

**_Download the Example File_**  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/03/VLOOKUP-Multiple-Criteria.xlsx)

You can also use other formulas to do a lookup with multiple criteria (such as [INDEX](https://trumpexcel.com/excel-index-function/)
/[MATCH](https://trumpexcel.com/excel-match-function/)
 or [SUMPRODUCT](https://trumpexcel.com/excel-sumproduct-function/)
).

Is there any other way you know to do this? If yes, do share with me in the comments section.

**You May Also Like the Following LOOKUP Tutorials:**

*   [VLOOKUP Vs. INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)
    
*   [Get Multiple Lookup Values Without Repetition in a Single Cell.](https://trumpexcel.com/multiple-lookup-values-single-cell-excel/)
    
*   [How to make VLOOKUP Case Sensitive](https://trumpexcel.com/vlookup-case-sensitive/)
    .
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

16 thoughts on “How to Use VLOOKUP with Multiple Criteria”
----------------------------------------------------------

1.  Thank you. It is informative, useful and it works once I understood the structure.
    
    Thanks for your guidance
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-36164)
    
2.  I AM STILL A LITTLE CONFUSED ABOUT THIS FORMULA.. this vlookup formula is complex. can you break it down to be simpler
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-31478)
    
3.  Suppose in a same cell let say A1 I have entered multiple values using Alt+enter. Can I get a corresponding vlookup value in other cell let say B1 for each entry in A1 cell?
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-13323)
    
4.  Awesome tip. THANKS!!!!
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-12788)
    
5.  Awesome tips , Sumit , thanks alot .
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-12350)
    
6.  Hi Sumit
    
    It is found that your website is providing very good information on MS Excel.  
    I am looking for information on selection of multiple values into a dropdown list based on the selection from another dropdown list.
    
    1 1.65  
    1 2.77  
    1 2.9  
    1 3.38  
    1 4.55  
    1 6.35  
    1 9.09  
    2 1.65  
    2 2.11  
    2 2.77  
    2 3.18  
    2 3.58  
    2 3.91  
    2 4.37  
    2 4.78  
    2 5.54  
    2 6.35  
    2 7.14  
    2 8.74  
    2 11.07
    
    If 1 is selected from a dropdown list, the values against 1 to be populated in to another dropdown list. The first column may contain fractions in text format, decimals etc.,
    
    Can you please help on this?
    
    Thanking you
    
    Krishna
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-10625)
    
    *   Use define range and indirect formula
        
        [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-12124)
        
7.  thank you so much for this …..exactly what I was trying to figure out 🙂
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-10555)
    
8.  Hello, many thanks for your very useful tips, however I didn’t found any answer related to the following issue. The formula on column I should return the exchange rate for the currency on column N related to the date on column C (another sheet). If there isn’t an exchange rate to that day, it should return the immediately previous date’s exchange rate. My issue is how can I write the formula to return the exchange rate to the currency to the immediately previous date? Thanks a lot for your help.
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-10036)
    
9.  Hi Sumit! Thank you for the tip. Is there a way to use this if the info you need is to the left of the info you have? I had ran a macro to insert a column and concatenate the info to the column A. Your tip here looks easier. Will it go left too?
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-9827)
    
    *   Hey Jill, The limitation of VLOOKUP is that it can not look for the data on the left. However, you can do this using the combination of INDEX/MATCH. I cover details on the difference in these two functions here: [https://trumpexcel.com/vlookup-vs-index-match-debate-ends/](https://trumpexcel.com/vlookup-vs-index-match-debate-ends/)
        
        You can learn more about INDEX function here: [https://trumpexcel.com/excel-index-function/](https://trumpexcel.com/excel-index-function/)
        
        [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-9828)
        
10.  is there any shortcut for inserting rows after specific lines,  
    i want to insert new row after every ten lines
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-8715)
    
    *   Yes. Place your cursor on the leftmost point of the row to highlight it. Then, while holding down both the Shift and Ctrl keys, press the = key. You can repeat this process for additional rows as needed.
        
        [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-40886)
        
11.  Hi Sumit, Thanks a lot for your tips and I have started excel in excel, I have a small issue while copying a set of numbers from one other excel column. I have pasted it and tried to sort assenting order. But they have a “space in the front” and not responding to my command. How to overcome this issue.
    
    With regards
    
    JACIN
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-3354)
    
12.  For your data table setup and the resulting layout, Pivot Table should be the ideal solution. 🙂
    
    [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-3152)
    
    *   Thanks for commenting Wong.. I mentioned the same in the article too. Pivot Table works really well and are easy to use, but need to the data to be structured in a required format. And if you are looking to fetch only a couple of values (let’s say in a dashboard), then VLOOKUP (or Index/Match, Sumproduct) could be the way to go.
        
        [Reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#comment-3153)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/vlookup-with-multiple-criteria/#respond)

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