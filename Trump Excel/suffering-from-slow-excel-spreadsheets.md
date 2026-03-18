# 10 Tricks to Fix Slow Excel Spreadsheets (Speed-up Excel)

**Source:** https://trumpexcel.com/suffering-from-slow-excel-spreadsheets

---

[Skip to content](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#below-title)

If there is one thing that unites us all, it has to be the frustration to keep up with a slow excel spreadsheets.

While the impact on the performance may be negligible when there is less data, it becomes more profound as you add more and more data/calculations to the workbook.

9 out of 10 times, an Excel user would complain about the slow Excel spreadsheets. And there is hardly anything you can do about it.

Well, that’s **NOT** completely true.

The way Excel has been made, it does get slow with large data sets. However, there are many speed-up tricks you can use to improve the performance of a slow Excel spreadsheet.

10 Tips to Handle Slow Excel Spreadsheets
-----------------------------------------

Here are 10 tips to give your slow Excel spreadsheet a little speed boost, and save you some time and frustration (click to jump to that specific section).

1.  [Avoid Volatile Functions (you must)](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#1)
    .
2.  [Use Helper Columns](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#2)
    .
3.  [Avoid Array Formulas (if you can)](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#3)
    .
4.  [Use Conditional Formatting with Caution](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#4)
    .
5.  [Use Excel Tables and Named Ranges](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#5)
    .
6.  [Convert Unused Formulas to Values](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#6)
    .
7.  [Keep All Referenced Data in One Sheet](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#7)
    .
8.  [Avoid Using Entire Row/Column in References](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#8)
    .
9.  [Use Manual Calculation Mode](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#9)
    .
10.  [Use Faster Formula Techniques](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#10)
    .

### 1\. Avoid Volatile Formulas

[Volatile formulas](https://trumpexcel.com/excel-volatile-formulas/)
 are called so because of a reason. Functions such as NOW, TODAY, INDIRECT, RAND, OFFSET etc. recalculate every time there is a change in the workbook.

For example, if you use NOW function in a cell, every time there is a change in the worksheet, the formula would be recalculated and the cell value would update.

This takes additional processing speed and you end up with a slow excel workbook.

As a rule of thumb, avoid volatile formulas. And if you can’t, try and minimize its use.

### 2\. Use Helper Columns

Helper columns are one of the most under-rated design constructs in Excel. I have seen many people shy away from creating helper columns.

**DON’T DO That.**

The biggest benefit of using ‘Helper Columns’ is that it may help you avoid array formulas.

Now don’t get me wrong. I am not against array formulas. Rather I believe these could be awesome in some situations. But it when you try to do it all with one long formula, it does impact the performance of your Excel workbook. A couple of array formulas here and there shouldn’t hurt, but in case you need to use it in many places, consider using helper columns.

Here are some Examples where helper columns are used:

*   [Automatically Sort Data in Alphabetical Order using Formula.](https://trumpexcel.com/sort-data-in-alphabetical-order-formula/)
    
*   [Dynamic Excel Filter – Extract Data as you Type.](https://trumpexcel.com/dynamic-excel-filter/)
    
*   [Creating Multiple Drop-down Lists in Excel without Repetition.](https://trumpexcel.com/multiple-drop-down-lists-in-excel/)
    

### 3\. Avoid Array Formulas

Array formulas have its own merits – but speed is not one of those.

As explained above, array formulas can take up a lot of data (cell references), analyze it, and give you the result. But doing that takes time.

If there is a way to avoid array formulas (such as using helper column), always take that road.

### 4\. Use Conditional Formatting with Caution

I absolutely love conditional formatting. It makes bland data look so beautiful. Instead of doing the comparison yourself, now you can simply look at a cell’s color or icon and you’d know how it compares with others.

But.. here is the problem.

Not many Excel users know that [Excel Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 is volatile.

While you may not notice the difference with small data sets, it can result in a slow excel spreadsheet if applied on large data sets, or applied multiple times.

Word of advice – Use it Cautiously.

Also read: [How to Remove Conditional Formatting in Excel (Shortcut + VBA)](https://trumpexcel.com/remove-conditional-formatting-excel/)

### 5\. Use Excel Tables and Named Ranges

[Excel Table](https://trumpexcel.com/excel-table/)
 and [Named Ranges](https://trumpexcel.com/named-ranges-in-excel/)
 are two amazing features that hold your data and makes referencing super easy. It may take a while to get used to it, but when you start using it, life becomes easy and fast.

In creating data-driven dashboards, it is almost always a good idea to convert your data into an Excel Table.

It also has an added advantage of making your formulas more comprehensible.

For example, what’s easier to understand?

\=Sales Price-Cost Price _OR_ \=SUM(A1:A10)-SUM(G1:G10)

### 6\. Convert Unused Formulas to Static Values

This is a no-brainer. When you don’t need it, don’t keep it.

Lots of formulas would result in a slow Excel workbook. And if you have formulas that are not even being used – you know who to blame. As a rule of thumb, if you don’t need formulas, it’s better to convert them into a static value (by pasting as values).

**Read More**: [How to quickly convert formulas to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

### 7\. Keep All Referenced Data in One Sheet

This may not always be possible, but if you can do this, I guarantee your Excel sheet would become faster.

The logic is simple – [formulas](https://trumpexcel.com/excel-functions/)
 in your worksheet don’t have to go far to get the data when it is right next to it in the same sheet.

### 8\. Avoid Using the Entire Row/Column as Reference (A:A)

The only reason I have this one on the list is that I see a lot of people using the entire row/column reference in formulas. This is a bad practice and should be avoided.

While you may think that the row/column only has a few cells with data, Excel doesn’t think that way. When you reference an entire row/column, Excel acts as a good servant and checks it anyway.

That takes more time for calculations.

Also read: [How to Open Excel in Safe Mode?](https://trumpexcel.com/safe-mode-excel/)

### 9. Use Manual Calculation Mode

I am just repeating what million people have already said in various forums and blogs.

Using Manual calculation gives you the flexibility to tell excel when to calculate, rather than Excel taking its own decisions.

This is not something that speeds up your Excel workbook, but if you have a slow Excel spreadsheet, it definitely saves time by not making Excel recalculate again and again.

*   To switch to manual mode, go to Formula Tab –> Calculation Options –> Manual (press F9 key to recalculate)

![Slow Excel spreadsheets - Manual Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20792%20152'%3E%3C/svg%3E)

### 10\. Use Faster Formulas Techniques

Excel gives you a lot of formulas and formula-combos to do the same thing. It is best to identify and use the fastest ones.

Here are a couple of examples:

*   Use [IFERROR](https://trumpexcel.com/excel-iferror-function/)
     instead of IF and ISERROR combo (unless you are using Excel 2003 or earlier, which does not have IFERROR).
*   Use [MAX](https://trumpexcel.com/excel-max-function/)
    (A1,0) instead do IF(A1>0,A1,0) – This is a cool tip that I learned from [Mr. Excel](http://www.mrexcel.com/)
     aka Bill Jelen. His research shows that MAX option is 40% faster than IF option (and I am ready to take this stat on his face value).
*   Use the [INDEX](https://trumpexcel.com/excel-index-function/)
    /[MATCH](https://trumpexcel.com/excel-match-function/)
     combo, instead of [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
     – This may raise a lot of eyebrows, but the truth is, there is no way VLOOKUP can be faster if you have 100’s of columns of data. The world is moving towards INDEX/MATCH, and you should make the shift too.  
    _\[If you are still confused about what to use, here is a head-on-head comparison of [VLOOKUP Vs. INDEX/MATCH](https://trumpexcel.com/vlookup-vs-index-match/)\
    _\].
*   Use — (double negatives) to convert TRUE’s and FALSE’s to 1’s and 0’s (instead of multiplying it by 1 or adding 0 to it). The speed improvement is noticeable in large data sets.

Is this an exhaustive list? Absolutely NOT. These are some good ones that I think are worth sharing as a starting point. If you are looking to master Excel-Speed-Up techniques, there is some good work done by a lot of Excel experts.

Here are some sources you may find useful:

*   [75 Speed-up tips by Chandoo](http://chandoo.org/wp/2012/03/27/75-excel-speeding-up-tips/)
     (smartly done by crowdsourcing).
*   [Decision Models Website](http://www.decisionmodels.com/)
    .
*   [Mr. Excel Message Board](http://www.mrexcel.com/forum/excel-questions/501497-how-speed-up-excel-processing.html)
     (explore this and you would find tons of tips).

I am sure you also have many tips that can help tackle slow excel spreadsheets. Do share it with us here in the comment section.

I also have one request. The pain of working with a slow excel spreadsheet is something many of us experience on a daily basis. If you find these techniques useful. share it with others. Ease their pain, and earn some goodness 🙂

**You May Also Like the Following Excel Links:**

*   [24 Excel Tricks to Make You Sail through Day-to-day work](https://trumpexcel.com/24-excel-tricks/)
    .
*   [10 Super Neat Ways to Clean Data in Excel Spreadsheets.](https://trumpexcel.com/clean-data-in-excel/)
    
*   [10 Excel Data Entry Tips You Can’t Afford to Miss.](https://trumpexcel.com/excel-data-entry-tips/)
    
*   [Creating and Using a drop-down List in Excel](https://trumpexcel.com/excel-drop-down-list/)
    .
*   [Reduce Excel File Size](https://trumpexcel.com/reduce-excel-file-size/)
    .
*   [How to Recover Unsaved Excel Files](https://trumpexcel.com/recover-unsaved-excel-files/)
    .
*   [Free Online Excel Training](https://trumpexcel.com/)
     (7-part video course)
*   [Arrow Keys not Working in Excel | Moving Pages Instead of Cells](https://trumpexcel.com/arrow-keys-not-working-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

30 thoughts on “10 Tricks to Fix Slow Excel Spreadsheets (Speed-up Excel)”
--------------------------------------------------------------------------

1.  I’ve noticed my Excel runs extremely slow when I have lots of formulae and am playing around with filters. Every change in filter results in formulae recalculating, which is unexpected because the filters are simply showing/hiding data and not changing contents. Is there a way to turn this off (other than switching to manual calc)
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-13623)
    
2.  Sir, 24th Feb.2020.  
    I must thankful to you find such useful notes.  
    Hoping to receive such valuable notes in future too.
    
    Kanhaiyalal Newaskar.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-13397)
    
3.  Those are all great suggestions. To help know what parts of your spreadsheet are slow you can also download this add-in to help you measure how long it takes to calculate your spreadsheet.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-13190)
    
4.  Hi! This helps a lot, thanks for putting it all in one place! 🙂
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-12735)
    
5.  That was very helpful content, but i will add something to it.  
    if you use IFERROR instead of IF the problem it will cause is, Iferror first evaluate the value which is formula and if it cause an error then it evaluate the false argument which is waste of resources and time.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-12223)
    
6.  Thanks a lot for your support
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-11352)
    
7.  So in other words, don’t use Excel! You just wiped out most of the most convenient tools. I love Excel but they didn’t think this through, I say so as an Electronics Engineer (both s/w & h/w).
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-10959)
    
8.  i had a super slow (but <1MB) file and i could not figure out why…. it was #8! completely fixed it when i got rid of entire column references on one of the sheets.  
    T-Y!
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-9819)
    
    *   Glad you found the tips useful Sean!
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-9824)
        
    *   how did you find which sheet and column ?/
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-14755)
        
9.  The Formula shown above was really helpful for me learn Excel. Everest offers Microsoft Excel Tutorials: Our administrations are Microsoft Excel Training, Online Excel Training,Excel Courses, Excel Classes, Learn Excel.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-8964)
    
10.  l like this blog [Excel Everest](https://exceleverest.com/)
    offers Microsoft ExcelTutorials: Our administrations are Microsoft Excel Training, Online Excel Training,Excel Courses.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-8697)
    
11.  Hi Sumit  
    Thanks for the list. I agree to most of your points. But especially no. 8 doesn’t make a difference (at least not any more). Also the effect of most of the points under no. 10 are very small (VLOOKUP vs. INDEX/MATCH for instance).  
    I measured the difference in calculation time: There seem to be other factors even more relevant. The whole study is linked here: [http://professor-excel.com/performance-excel-study/](http://professor-excel.com/performance-excel-study/)
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-7037)
    
    *   No.8 makes a massive difference and has thankfully stopped all of my company’s large sheets repeatedly hanging and then crashing excel.
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-11232)
        
12.  My dear friend. Thankyou.  
    Conditional formula was the culprit.  
    Best regards.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-4208)
    
13.  Hallo Mr. Sumit. Its really helpful but how its possible in match/index function to avoid selection of whole column and row when data will be aded in next time. As it is not possible to change formula anytime.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-3376)
    
14.  What is helper Column, Can you please describe…. ?
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-3259)
    
15.  Useful but this seems aimed at “its the users fault”, which might be true for people using particular worksheets. Its not aimed at a problem where EVERY worksheet has slow entry, which is usually do to poor or hostile software development by Microsoft and requires monkeying with kernel settings and disabling features like network and help settings, product activation etc, and generally other garbage M$ and NSA uses for its various protectionist schemes and to spy illegally on its users.
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-3036)
    
    *   Thanks for commenting Selcuk.. It’s interesting what you have shared here. Definitely, there are a lot of systemic issues that are practically user independent and makes the workbook slow. I really hope MS will come up with more powerful Excel that can handle large data sets and still be fast.
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-3060)
        
        *   Thanks. Yes basically i7 processors and GHz speeds, our computers software should have lightning fast with data entry, saves, folder transfers, etc…todays computers have real processing power of the supercomputers of yesteryear…yet somehow they don’t. Why? Well, the reason is simple…M$ maximizes this extra power for its own purposes, rather than the users, which on the scale it is doing it, is basically theft on a scale much larger than so-called software pirates which is all you hear about in the media. The real pirates (of our CPU cycles and zombified computers) is M$ itself and whatever third party they are acquiescing to (RIAA,NSA,etc). The practice should be considered illegal by any reasonable definition of the law, however M$ just cowardly hides behind proprietary kernel code and encrypted data transfers to Redmond and elsewhere. Recently, I found M$ downloading 3GB of Winn10 software onto my personal computer. Did they pay for the bandwidth…no..did they let me know they were doing this illegal thing…no. They even place it in a hidden protected file. Its a huge waste of economic productivity, which depends so critically on computers today. Things are so rotten at M$, the governement really should consider breaking them up. All those talented software engineers just producing one garbage product after another because all the brass cares about is money and ruining the competition by its resting on its laurels with patent thickets and protectionism rather than concentrating on making a better product.
            
            [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-3065)
            
            *   chill pill time?
                
                [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-9361)
                
                *   There is no time to chill. I’ve literally spent “years” of wasted time and so have many others working with Microsofts user hostile software which waste and steal the users purchased hardware for its own purposes. The cost to our economy is far more than their market share. The company should be dismantled for everyones benefit, as the antitrust judges orderered over a decade ago. Its long overdue.
                    
                *   You are off your rocker.  
                    Move to Open or Libre Office, then you may find peace and tranquility in knowing it is not Microsoft taking your sanity…
                    
16.  Hi Sumit
    
    In regards to #8, I recently learned that whole column/row references are ok for some of the functions. Some of the functions like SUM or SUMIF will automatically recognize the last used row/column. The following Microsoft article explains this in more detail.
    
    [http://msdn.microsoft.com/en-us/library/ff726673(v=office.14).aspx](http://msdn.microsoft.com/en-us/library/ff726673(v=office.14).aspx)
    
    I still agree with your suggestion though. As a best practice I still don’t recommend referencing whole rows/columns because I am not exactly sure how the function determines the “last used row/column”. As we know with VBA, this can sometimes be misleading. The last used row/column could be much farther down on the sheet if data has been deleted. And this means the function could be including unused rows/columns in the calculation.
    
    However, I think it’s good to know that some of the functions do consider this. I will have to see if there is a full list of the functions that do recognize the last used row/column.
    
    Thanks for the great tips!
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-1360)
    
    *   Jon – That’s good learning for me too.. Thanks for sharing 🙂  
        You are right, its good to know of formulas that can handle this
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-1361)
        
    *   I’m right there with Jon on #8. I always use whole column/row references with Vlookups and SumIfs. This ensures that if my data range changes, my formulas are guaranteed to pick up the added data. I have run into too many headaches with formulas not picking up all the data (especially with repetitive data extractions). But NEVER use entire column/row references with SumProduct!!! I found out the hard way this that function 🙁
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-1363)
        
    *   Hi,  
        This is where Table comes to the picture.
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-2289)
        
        *   Either “Tables” as you mention or else dynamic named ranges would also work
            
            [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-12308)
            
17.  Hi Sumit
    
    As you’ve stated this list is not exhaustive, but it is a very good start. Microsoft has several very good articles about performance optimization and calculation speed (written by the team at Decision Models) that are worth reading.  
    Having said that, I think this article could be improved with some explanation as to WHY each of these ideas make a difference to speed. For example:  
    1\. Helper columns (and rows) >> breaks up formulae that can save recalculation due to the way Excel builds the ‘calculation tree’.  
    2\. Array formulae >> typically reference large ranges of cells and therefore need to evaluate each one, when this can be avoided with a different choice of formula.  
    3\. Volatile functions >> by definition must be recalculated each, but the real issue is related to where they appear in the calculation tree. If at the bottom then no big deal, but if right at the top, then very dependent formula must also be recalculated. (See the Decision Models website for discussion about this.)  
    7\. It’s not clear what you mean by this one.  
    8\. Whole columns/rows >> Ditto re calculation tree issue.  
    Regards
    
    [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-1357)
    
    *   Thanks Colin.. Very Insightful.. Calculation Tree is indeed one of the biggest reasons that determines excel speed  
        #7 – The idea is to keep all the data in one sheet, so it is easier to reference in formulas (instead of having it dispersed in various sheets). Based on my experience in excel dash boarding, it is faster this way
        
        [Reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#comment-1358)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/#respond)

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