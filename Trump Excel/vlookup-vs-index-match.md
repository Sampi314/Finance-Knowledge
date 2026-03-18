# VLOOKUP Vs. INDEX/MATCH - The Debate Ends Here

**Source:** https://trumpexcel.com/vlookup-vs-index-match

---

[Skip to content](https://trumpexcel.com/vlookup-vs-index-match/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vlookup-vs-index-match/#below-title)

When it comes to the Excel world, it’s divided into two factions – the VLOOKUP brigade and the INDEX/MATCH regiment.

If you’re wondering which one scores higher in the **VLOOKUP vs INDEX/MATCH** battle, this article will try and answer it.

But before I do that, let me make a few things clear – this article is not about praising one function and bashing the other. Both of these [Excel functions](https://trumpexcel.com/excel-functions/)
 are amazing and have their place. In some cases, one might be better than the other.

During one of my Excel Training sessions, I was surprised to find out that most of the people were aware and, in some cases, proficient in using [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
, but almost none of them knew about the powerful [INDEX](https://trumpexcel.com/excel-index-function/)
/[MATCH](https://trumpexcel.com/excel-match-function/)
 combo.

And when I mentioned it, they had a lot of queries:

*   Is it a lookup and reference formula?  – _Yes! Maybe the best of the lot_
*   Is it a new Excel 2016 function? – _Hell NO!_
*   Can it reference data between different worksheets or workbooks? – _Yes_
*   Is it better than VLOOKUP? – _It depends_

I think the VLOOKUP PR team is doing a much better job than that of INDEX/MATCH.

In this tutorial, I will try and compare these two formulas as objectively as I can.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vlookup-vs-index-match/#)

I don’t have favorites, to begin with, but I prefer using the INDEX/MATCH combo more than VLOOKUP. The choice is driven by a lot of factors including what the data looks like and how it would be used. I will cover all these in this article.

VLOOKUP Vs INDEX MATCH – An Objective Comparison
------------------------------------------------

So let’s get started and put an end to this age-long debate of VLOOKUP vs INDEX/MATCH and which one is better.

And to do this, I will compare these two functions on some parameters (some are quantifiable and some are not).

### The popularity of the function

VLOOKUP takes this hands down.

For some people, if you know how to use VLOOKUP, you know how to use Excel. And given how much can be done with this single function, I don’t blame them.

For this reason, a lot of people use VLOOKUP as it is better understood by other Excel users.

Although this is not a popularity contest, it plays a huge role in why VLOOKUP gets used so much.

Imagine you’re working with a client/manager who is proficient in using VLOOKUP but doesn’t know how to use INDEX/MATCH. It makes more sense to use a function which both you know, instead of trying to teach them about INDEX/MATCH.

Verdict: VLOOKUP is a clear winner on popularity

### **Ease of USE**

The reason VLOOKUP is so popular is that it’s easy to use (at least when compared with INDEX/MATCH).

When I take Excel training, I would always start by first covering VLOOKUP first. A lot of people find VLOOKUP hard, so I can’t even imagine trying to teach them INDEX/MATCH (unless they already know how to use VLOOKUP proficiently).

And in most cases, VLOOKUP is good enough. It can do most of the things people need when working with data. Surely you can do the same thing with INDEX/MATCH too, but why take the hard road when it’s not even needed.

VLOOKUP takes 3 arguments (fourth is optional) and is easier to understand as compared with INDEX/MATCH.

INDEX & MATCH are two separate functions that take three arguments each and should be combined to do a lookup (getting complicated already??).

While you may find INDEX/MATCH equally easy when you get a hang of it, a beginner is likely to gravitate towards VLOOKUP.

![Vlookup Vs Index](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20768%20312'%3E%3C/svg%3E)

Verdict: VLOOKUP gets the point for its ease of use.

### The flexibility of the Function

VLOOKUP is a great function but has a few limitations:

*   It can not lookup and return a value which is to the left of the lookup value.
*   It works only with data which is arranged vertically.
*   VLOOKUP would give a wrong result if you add/delete a new column in your data (as the column number value now refers to the wrong column). _You can make the column number dynamic, but if you planning to combine two or more functions, why not use INDEX/MATCH in the first place._

Before you start fuming with rage and leave a comment about how VLOOKUP can do all these things, hear me out. VLOOKUP, as a stand-alone function, is not meant to do this. Of course, you can combine it with other formulas and get around all these things, but then it loses the tag of being easy to use.

If someone can use a combination to formulas to make VLOOKUP look to the left or make columns dynamic, I am sure that person is better off using INDEX/MATCH, which is made to handle these things with ease.

So yes, VLOOKUP can get around these limitations, but that’s not worth it. With more coding and robotics, I am sure you can also make VLOOKUP fetch your favorite coffee, but remember, it’s not made for this.

INDEX-MATCH combo, on the other hand, is made to handle all these issues. It can

1.  Lookup and return a value which is to the left of the lookup value,
2.  Handle both horizontally and/or vertically structured data.
3.  Handle row/columns numbers in case you insert or delete some from the dataset

![Vlookup Lookup Value on Right](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20326%20428'%3E%3C/svg%3E)

Verdict: INDEX/MATCH combo gives you a lot more flexibility than VLOOKUP.

### Speed of the formula

The difference is hardly noticeable when you have small data sets.

But if you have thousands of rows and many columns, this can be a deciding factor.

Without reinventing the wheel, here is a post by [Charley Kyd](http://exceluser.com/blog/727/excels-fastest-lookup-methods-the-tested-results.html)
, where he clearly mentions:

At its worst, the INDEX-MATCH method is about as fast as VLOOKUP; at its best, it’s much faster.

While I have considered this as one of the factors, I believe it’s less important than others. Over the years, Microsoft has been hard at work trying to improve the speed of these functions, and they have made considerable improvements since I wrote this article first.

[Here is an update](https://techcommunity.microsoft.com/t5/Excel-Blog/Excel-performance-improvements-now-take-seconds-running-Lookup/ba-p/254199)
 where they mention how they are making formula such as VLOOKUP, [HLOOKUP](https://trumpexcel.com/excel-hlookup-function/)
, and MATCH faster.

Also, it’s a very small percentage of the number of people who can actually benefit from the speed improvement that comes with using INDEX/MATCH over VLOOKUP.

Verdict: If speed is what you are looking for, INDEX/MATCH combo is the way to go.

Overall Verdict (VLOOKUP Vs INDEX/MATCH Combo)
----------------------------------------------

Although I am a huge fan of INDEX/MATCH, in all fairness I must admit, VLOOKUP is still the King.

This doesn’t mean that you should not learn about INDEX/MATCH, but if you’re new to Excel and lookup formulas, start with VLOOKUP. Use it and master it first, and then move to INDEX/MATCH

INDEX/MATCH is a powerful combo that has more flexibility and speed than the VLOOKUP formula.

![Vlokup Vs Index Match Comparison](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20392%20199'%3E%3C/svg%3E)

That being said, VLOOKUP is not going anywhere and is likely to remain as one of the most popular functions in Excel for ages to come.

Well, the debate is not exactly over (see the comments section). Fuel the fire – leave your 2 cents in the comments section.

Also read: [VLOOKUP vs XLOOKUP Function](https://trumpexcel.com/excel-functions/vlookup-vs-xlookup/)

The Difference Between VLOOKUP and INDEX/MATCH
----------------------------------------------

Before getting to the comparison, I think it’s important to know the basic difference (and more importantly the similarities) between these two functions.

I am not going to get into the syntax and example of these functions. If you’re interested in that, I have detailed tutorials on both [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
 and [INDEX/MATCH](https://trumpexcel.com/index-match/)
.

Both VLOOKUP and INDEX/MATCH are formulas you can use to look up a value in a dataset and fetch the corresponding value (just like you scan a menu and look for the price of the dish you want to order).

![Lookup up from a dataset and fetch the corresponding value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20400'%3E%3C/svg%3E)

In most cases, you can use these interchangeably.

The main differences in these functions become more important when you need a little more than a simple lookup and fetch operation.

Here are some basic differences in these two formulas (more covered in detailed later in this article):

1.  VLOOKUP is a single formula that does all the lookup-and-fetch, but with INDEX/MATCH, you need to use both the functions in the formula.
2.  INDEX/MATCH can more advanced lookup – such as lookup to the left of the dataset, make row/column value dynamic, etc.
3.  INDEX/MATCH provides a lot more flexibility, which is better suited when building data models or working with complex data

**You May Also Like the Following VLOOKUP Tutorials:**  

*   [How to Use VLOOKUP with Multiple Criteria.](https://trumpexcel.com/vlookup-with-multiple-criteria/)
    
*   [How to make VLOOKUP Case Sensitive.](https://trumpexcel.com/vlookup-case-sensitive/)
    
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    .
*   [Use VLookup to Get the Last Number in a List in Excel](https://trumpexcel.com/get-the-last-number-in-excel-vlookup/)
    .
*   [Excel Index Match](https://trumpexcel.com/index-match/)
    
*   [Formula vs Function in Excel – What’s the Difference?](https://trumpexcel.com/formula-vs-function-excel/)
    

**Useful Excel Resources:**

*   [Free Online Excel Training](https://trumpexcel.com/)
     (7-part Video Course)
*   [100+ Excel Functions](https://trumpexcel.com/excel-functions/)
     (with examples and videos)
*   [20 Advanced Excel Functions and Formulas (for Excel Pros)](https://trumpexcel.com/advanced-excel-functions-formulas/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

51 thoughts on “VLOOKUP Vs. INDEX/MATCH – Which One is Better? (Answered)”
--------------------------------------------------------------------------

1.  I had a very complex financial forecasts model. All fetches were with vlookups and hlookups. But once i had to delete, insert columns, it became a nightmare.. I have to switch to index match, or the entire model would become almost useless!!
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-13327)
    
2.  Interested in learning excel
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-12440)
    
3.  Hi Sumit,  
    Thanks for the forum and debate. VLOOKUP and HLOOKUP are great goto functions for something the will remain static and relatively simple. In real life, that never happens, as usually just when you finish your model, there is the need to insert, add, delete, change, etc. something. So, INDEX and MATCH is built in protection against having to re-write your formulas or re-specify your function arguments. While it is easy and or lazy to grab VLOOKUP or HLOOKUP for a quick fix, you’ll thank yourself if you learn INDEX and MATCH and make it your goto solution for flexible lookups that can accommodate future changes in form and or function of your worksheet. Of course.. all this is my opinion.. to each his/her own.  
    Thanks again.. appreciate all of your wisdom and resources offered so generously to the Excel community!
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-11339)
    
4.  I used to use vlookup all the time, working with larger data sets I started using index/match, now i’m so used to it I wouldn’t go back, especially useful when you have a lot of columns, just selecting the column rather than working out what column number it is from the index is so much easier, it also requires less memory and doesn’t recalculate every time a cell value changes reducing the processing power the spreadsheet requires, overall much faster and makes you want to hit the keyboard less, I recommend using it if you work with large data sets, if not and vlookup works for you then stick with that. oh another bonus, you can match against multiple columns too pretty easily (slight modification to the formula but nothing too complicated doing =match(a2&b2,col1,col2….google the rest) so yeah its pretty cool and worth learning.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-11162)
    
5.  Have experienced the functional limitations of vlookup. Index/match is a more robust approach and is my preferred option.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-10621)
    
6.  how can I enter a formula (concatenate) in power query merging to another connection…help pls?
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-10320)
    
7.  index match function is much better than vlookup
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9965)
    
8.  …”It works only with data which is arranged vertically” – that’s when you switch to HLOOKUP.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9694)
    
9.  Lovely article.  
    I thinl VLookp scores over INDEX match when the range we are taking the data from has increased number of rows compared to the destination rows.  
    Eg: If i want to derive the values for an item say “Orange” on my new sheet which may be on row 81,  
    and in the old sheet where it is looking from : “Orange” is on row no 78( i.e the new sheet has increased rows) the formula will return the value pertaining to data on row no 78 instead of actually looking up details for “orange” per se.  
    Is there a solution for this in INDEX MATCH so that irrespective of the row number it returns values pertaining to the concerned item eg JOHN??
    
    John Verghese
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9406)
    
10.  Two points in favor of INDEX()/MATCH():
    
    When you have structured references in Excel tables INDEX()/MATCH() works/looks better because you can see what kind of data is being looked up:  
    \=INDEX(tbl\_Articles\[Price\],MATCH(\[ArticleNr\],tbl\_Articles\[ArticleNr\],0))  
    Looking up field “Price” in table “tbl\_Articles”.
    
    \=VLOOKUP(\[ArticleNr\],tbl\_Articles,8,FALSCH)  
    Looking up the eighth column in table “tbl\_Articles”.
    
    In lists with a lot of columns it might be difficult to get the correct column index for VLOOKUP().
    
    End of debate!  
    Really!  
    🙂
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9184)
    
11.  I use Index and Match combination in a different context. Forms or Payment Voucher and Summary sheet. Details in the Summary sheet and then the printing of Payment Voucher in a different sheet. The index and Match will be in the Payment Voucher sheet in reference to the summary’s Numbering system. Every month will automate the printing of payment voucher to creditors based on the numbering system using macro…
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9183)
    
12.  INDEX/MATCH is definitely more intimidating than VLOOKUP.  
    The top tip I came across is from the Contextures blog. You can use autocorrect to type up the formula structure for you with tips, and then double-click to select the data. This makes remembering the syntax easier.
    
    Link:  
    [http://blog.contextures.com/archives/2016/05/05/enter-complex-excel-formulas-fast/](http://blog.contextures.com/archives/2016/05/05/enter-complex-excel-formulas-fast/)
    
    The Complex Formula
    
    In the comment, Wyn showed the formula that he puts in AutoCorrect. It is an INDEX / MATCH formula, with placeholders for the cell references. (You can read more about that powerful function duo on my website.)
    
    If you want to try this tip (and I highly recommend it), then copy his formula. I’ll show you what to do with it in a minute.
    
    \=INDEX( DblClk\_to\_Select\_Column\_to\_return, MATCH( DblClk\_Single\_Lookup\_Cell, DblClk\_Lookup\_Column, 0),0)
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-8717)
    
13.  I have a very large data set that are currently built with vlookup. It’s very slow and takes about 10 minutes for each small change. I want to switch it to index match and see how it goes. I will keep you posted.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2731)
    
    *   Thanks for commenting Cyn.. Would love to hear about the results
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-3058)
        
14.  Definitely a good analysis of the VLOOKUP vs. INDEX MATCH debate. Especially giving some credit to still using VLOOKUP as opposed to the mass opinions out there that we should all jump to INDEX MATCH. Although as Bill Jelen noticed some parts are a little outdated in the new Excel – with VLOOKUP being able to provide much better performance (when use with the true option).
    
    What is more, I feel there is still room to exhaust this discussion i.e. I personally feel that MS Query could be added to the clash between VLOOKUP vs. INDEX MATCH. Many people don’t appreciate the simplicity and control you have with an MS Query to do complex lookup operations together with other data transformation in a single SQL query as opposed to developing complex erroneous formulas or Array Formulas.
    
    Looking forward to your opinion. Also feel free to read on my perspective in terms of analysing VLOOKUP with other alternatives in terms of performance.  
    [http://www.analystcave.com/excel-vlookup-vs-index-match-vs-sql-performance/](http://www.analystcave.com/excel-vlookup-vs-index-match-vs-sql-performance/)
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2380)
    
15.  VLOOKUP work also from right to left.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2077)
    
    *   Hello Debjit.. Vlookup works when the lookup value is in the left most column.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2079)
        
        *   Here my answer.
            
            [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2080)
            
            *   On it’s own, Vlookup can not look to the right. In the above case, you have created a long formula that can be simplified using Index/Match. Also, it is not dynamic (the column number has been hard coded). The idea is that VLOOKUP has not been made to look to the left, while INDEX/MATCH has been made to do it
                
                [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2081)
                
                *   Sumit: Your comparison of an INDEX/MATCH combo with a stand-alone VLOOKUP is as unfair as comparing apples and oranges! Both Debjit and Bob Phillips have shown how VLOOKUP can be used in combination with another function to return a value from the left. Others have shown how another function can be used to return a dynamic col\_index argument to VLOOKUP.
                    
                    Perceived problems/weaknesses of VLOOKUP dispelled! End of story.
                    
                *   Thanks for commenting.. VLOOKUP doesn’t offer the flexibility that INDEX/MATCH has. Imagine what the formula by Debjit would look like if I have 100 columns of data. Yes, you can create a big complex formula to make VLOOKUP look on the left and make the column number dynamic, but then ease of use goes out of the window. In such a case, better use INDEX/MATCH.
                    
                *   hi, Sumit Bansal,  
                    I want a formula of excel.  
                    \=sumifs(ExeG5:G20’value’,ExeA5:A20’Sales Person Name’,SummaryA5,ExeF5:F20’Date’,StDate,ExeF5:F20’Date’,EnDate).  
                    This formula i found month wise numeric value. but i want to found month wise text value.  
                    what is the formula to do this.  
                    Please it’s so much important for mine. Help me as soon as early possible.
                    
                *   I have been literally thinking the exact same thing. I know it’s a bit old now, but it makes no sense to compare a single formula with a combination formula in this context!
                    
                *   Thanks for pitching in Adam. You’re right that it’s a bit unfair. What I tried highlighting here are the benefits of the Index/Match for looking up values in data set that people try to do with VLOOKUP. No doubt VLOOKUP is an amazing function, but Index/Match cast a wider net when it comes to looking up values.
                    
                *   Hi Sumit,
                    
                    This is Arikrishnan. So pleasure to get in touch with you. I need a favour from you regarding a Tracker you updated for Attendance ([http://trumpexcel.com/2015/03/excel-leave-tracker/](http://trumpexcel.com/2015/03/excel-leave-tracker/)
                    ).  
                    In this Tracker you have made the fields “Leave this Month (Cell NJ)”, “Leaves This Year (Cell NK)” till Cell NQ as constant and only cells allocated for every month changes.
                    
                    My requirement is that, I need those aforementioned fields needs to be changed as I would like to use those fields for monthly report. Can you assist me in this !!!!
                    
                *   The point is that in order to make VLOOKUP as flexible as INDEX-MATCH, you have to add more code when you use it, thereby making it at least as complicated as INDEX-MATCH; so why not just use INDEX-MATCH in the first place?
                    
                *   Someone needs to get a pillow and a shovel and kill this debate.
                    
                    I’ve used VLOOKUP and INDEX/MATCH and continue to use both.  
                    When a client comes to me and complains that a solution broke because of VLOOKUP, then we can revive this.
                    
                    But really. The INDEX/MATCH people are like religious people who come knock on your front door looking for a problem to fit their solution. BOOOOO!
                    
                *   And the VLOOKUP fanboys are fanatical cultists like the flat earthers, if you wanna go down that road lol.
                    
16.  Great post, Sumit! I agree with majority of your commentators, given the choice, I would take the VLOOKUP route. However, I truly believe that SQL is the best way to go to accomplish these lookup tasks:  
    [http://blog.excelstrategiesllc.com/2014/11/20/vlookup-vs-indexmatch-debate-sql](http://blog.excelstrategiesllc.com/2014/11/20/vlookup-vs-indexmatch-debate-sql)
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1618)
    
17.  Nice article. First, I have to confess that I am a big fan if the INDEX MATCH. However, regarding the third point in the Flexibility section, it’s not completely fair to compare VLOOKUP with a combo INDEX MATCH. If you use INDEX and hard code the numbers for rows and columns, you are going to get a different value if the column is deleted too. That’s why it is convenient to use a combo VLOOKUP MATCH if you are going to use Vlookup at all.
    
    Why I find powerful about INDEX is that since it returns a reference it can be used in conjunction with the SUM function ( SUM(INDEX() ) to sum ranges. Another convenient feature is to choose values from different sections (sort of scenario manager) when you use it in a reference mode, using the \[area\_num\] parameter at the end.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1605)
    
    *   I am with you on this. INDEX flexibility works when used with MATCH. If row/column number are hard-coded, flexibility goes for a toss. And the feature of Index to return reference is incredible. It allows you to do so much more. I use this a lot to create a dynamic ranges and drop downs.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1606)
        
18.  Nice article Sumit! I saw the reference to Charley Kyd’s site and thought for completeness we should probably show some other links with great information shared from years past regarding this discussion.
    
    Speed:  
    [http://www.decisionmodels.com/optspeede.htm](http://www.decisionmodels.com/optspeede.htm)
      
    [http://www.excelguru.ca/forums/showthread.php?132-INDEX-MATCH-versus-VLOOKUP&p=599&viewfull=1#post599](http://www.excelguru.ca/forums/showthread.php?132-INDEX-MATCH-versus-VLOOKUP&p=599&viewfull=1#post599)
    
    General:  
    [http://mrexcel.com/articles/excel-vlookup-index-match.php](http://mrexcel.com/articles/excel-vlookup-index-match.php)
      
    [http://exceluser.com/formulas/excels-vlookup-vs-index-match-functions.htm](http://exceluser.com/formulas/excels-vlookup-vs-index-match-functions.htm)
    
    Misc:  
    [http://www.excelhero.com/blog/2011/03/the-imposing-index.html](http://www.excelhero.com/blog/2011/03/the-imposing-index.html)
    
    Take care,  
    Zack
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1601)
    
    *   Hi Zack.. Welcome to Trump Excel.. Thanks for sharing these links. Really helpful in getting a 360 degree view on Vlookup and Index.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1602)
        
19.  You say VLOOKUP cannot look left, but it can using a format that somewhat emulates INDEX/MATCH
    
    \=VLOOKUP(“z”,CHOOSE({1,2},$B$1:$B$10,$A$1:$A$10),2,FALSE)
    
    You say that … Vlookup would give a wrong result if you add/delete a new column in your data. But that is true of so many things in Excel, so a good spreadsheet developer can easily code around that
    
    \=VLOOKUP(“g”,$D$2:$H$15,MATCH(“Qtr2”,$D$2:$H$2,0),FALSE)
    
    So VLOOKUP can be/is just as flexible as INDEX/MATCH.
    
    The biggest selling point to me is that VLOOKUP is easy to teach to people, and it sticks, INDEX/MATCH less so, and even though I know all about INDEX/MATCH my first recourse is usually to VLOOKUP; I generally only use INDEX/MATCH when there is some twist in the requirement where I am adding some conditional test into the lookup.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1598)
    
    *   Hi Bob.. Welcome to Trump Excel.. Thanks for sharing your thoughts.. I agree with about Vlookup being easy to use and being popular. However, Index/Match does offer a lot more flexibility that can not be achieved using Vlookup. While we can create complex formula to look to the left and adjust for column additions, its an inherent benefit if you use Index/Match. Apart from these, you can also use Index/Match to return entire row/column, as well as a cell reference (which is useful if you create dynamic named ranges or drop downs). These things can not be done using Vlookup. I agree on ease of usage of Vlookup, but it does have limitations that can be solved by Index/Match.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1599)
        
20.  May I inquire into how large are the average data tables stored in Excel when you use VLOOKUP, HLOOKUP or INDEX(MATCH)?
    
    I developed an event/employee scheduling system back in the late 90’s using LOTUS 123 which I converted over to Excel somewhere around 2004. The system has evolved greatly since then filled with many automated functions and will continue to evolve. I once thought about incorporating one of the above methods but found my own personal coding to be more efficient for the task at hand.
    
    The reason I ask about the size of your tables is that my tables rarely reach over 250 records. Total project size over the years has shrunk from right around 1048k down to 78k with the same amount of records. This was accomplished by removing all formulas and conditional formatting from all the sheets. Everything is done in VBA code.
    
    Note: I don’t use pivot tables since the output is not to my liking and useless to our needs in case this has any affect on the use of the above functions.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1597)
    
21.  Nice article, but I’m still not convinced I should use INDEX(MATCH()) more than VLOOKUP(). Maybe I’m just too set in my ways, another group other than new Excel users who won’t switch completely, the people who have been using Excel since before there was Windows. Oh, it’s another tool in the kit, but over the years I’ve built too many skills around VLOOKUP() to abandon it.
    
    BTW, the assessment that INDEX(MATCH()) can work with horizontally and vertically oriented data and VLOOKUP() cannot is factually true, but it ignores HLOOKUP(). Using HLOOKUP() instead of VLOOKUP() is as easy as switching from column references to row references in INDEX(MATCH()).
    
    I won’t bore you here with all of the other nonsense I have to say about this, but here’s a summary of things I do with VLOOKUP(): Left-right lookup-return; Multiple criteria lookup; Bullet-proofing with Named columns and tables; Returning first/last of a criteria.
    
    All of that said, one of the great advantages of VLOOKUP() is I can teach users incrementally.
    
    I usually develop a workbook then review it with the owner, typically a business manager or director. This might be the first time they are walked-through what VLOOKUP() does. They get it most of the time. However, if I start with INDEX(MATCH()) their eyes glaze over with the first explanation.
    
    Once I have them hooked into VLOOKUP() I can add the complexity needed for bigger problems.
    
    If you care to read the rest, it’s at [http://bigdon-in-vbaland.blogspot.com/2014/11/indexmatch-v-vlookup.html](http://bigdon-in-vbaland.blogspot.com/2014/11/indexmatch-v-vlookup.html)
    .
    
    Thanks
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1591)
    
    *   Hi Don.. Welcome to Trump Excel.. Thanks for sharing your thoughts.. I am with you on this.. The ease of use is a huge factor for Vlookup. It is way easier to explain Vlookup to anyone, and there is a lot that it can be done with it. Index/Match, on the other hand, is a notch higher is terms of complexity and can be used in a specific scenario. However, if you do get a hang of it. Index/Match combo is very powerful and can do a lot more than Vlookup. But at the end of the day – as Mr Excel said – ease of use and popularity trumps everything else.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1592)
        
    *   Sorry Don, it must be the way you teach it. My opinion is that VLOOKUP and HLOOKUP are simply over-specialised legacy functions and Excel would be all the better for ‘pruning’ them out. I do use VLOOKUP occasionally when I have a 2-D range; the search array happens to be on the left; I only wish to return a single field; I am sure the data is clean and the match will always succeed. Despite that, I think the value they bring to the bloated zoo of Excel functions is not worth their keep.
        
        I would always start a MATCH/INDEX combination with a helper cell for the MATCH. That is the point at which the row index it returns may be checked visually. In many instances it will be wrong so there is no point in moving to look up further data fields until data and formula issues are corrected. Once the row index is validated then INDEX will return as many fields as are needed (including a copy of the search field for checking as in the two VLOOKUP strategy). I believe this is a far more satisfactory position than the usual plea for help of “Why does my VLOOKUP return the wrong value?”
        
        Counter to this, I believe a real strength of VLOOKUP is that it works looking up data from closed workbooks but that is not something I am likely to use.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1596)
        
    *   I know this is a year old now, but we just got around to establishing Index(Match()) as best practise and, in fact, banished vlookup() from any spreadsheet deliverables generated by my group. Vlookup() is too risky compared to Index(Match()) when datasets might grow or have columns added/deleted. We have fewer errors and our regression testing cycle is much shorter now.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2732)
        
    *   There is a lot of argument in this article about how to give VLOOKUP the advantages of MATCH-INDEX. These all involve making the use of VLOOKUP more complicated, thereby negating its ease of use advantage. Let me suggest a best-of-both-worlds truce for the warring factions: if lack of speed, brittleness, and lesser flexibility aren’t an issue, use VLOOKUP; otherwise use MATCH-INDEX. As a practical matter, it’s just that simple.
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9898)
        
        *   HELL YES. It’s that simple.
            
            [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9902)
            
22.  This is an excellent article that lays out the differences well.
    
    On the speed issue, VLOOKUP and INDEX(MATCH()) will be equally slow. If you really cared about speed, you would switch to the Charles Williams concept of using two VLOOKUP(,,,TRUE) instead of one INDEX(MATCH()) where you would see a 100-fold increase in speed.
    
    On the flexibility issue, you missed that MATCH(,,-1) can return the value “just larger” instead of the value “just smaller” when doing a range lookup. Also, if you have to do 12 columns of VLOOKUPs, then a single MATCH column with 12 INDEX columns will be faster.
    
    But ease of use and popularity here trumps everything else. People can wrap their heads around VLOOKUP, where most will be completely new to both INDEX and MATCH. Unless someone has a specific need to VLOOKUP left or VLOOKUP for the value just larger, people will continue to use VLOOKUP 99% of the time.
    
    [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1588)
    
    *   Hi Bill (aka Mr. Excel).. Super to see you here on Trump Excel. Great points on speed and flexibility.. Concept of 2 Vlookups is a learning for me too. Will check it out. Thanks for sharing 🙂
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1589)
        
        *   I demo Charles William’s formula here: [http://youtu.be/Guj\_\_8KEQD8?t=4m48s](http://youtu.be/Guj__8KEQD8?t=4m48s)
            
            [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-1590)
            
            *   Both brilliant articles. Never heard of the double vlookup. What puzzles me now is why it is not assembled in to one excel function with vlookup syntax to get the best of both?
                
                [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-2776)
                
            *   This only works if there are false right? If there are no falses, it should be a lot slower.
                
                [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-3042)
                
            *   This is so misleading. Bill you might consider removing this entire thread.
                
                Specifying TRUE for Approximate Match when the lookup column is not sorted causes the VLOOKUP function to return incorrect values (unless it just gets lucky). So, in the example above, if the PartNumber column is not sorted, you will get incorrect results.
                
                It doesn’t matter how fast it is if it ain’t right.
                
                What am I missing?
                
                [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-9945)
                
                *   The video says the lookup table has to be sorted. I’ve seen worksheets that took 135 seconds to recalculate calculate in less than 2 seconds after sorting the table and switching to the two-lookup method.
                    
                *   True requires the lookup range be sorted because it does a binary search instead of a linear search. Binary search means the search splits the list in half until it finds a match or there are no other choices. On a list of 1M entries, the binary search needs no more than 16 checks to get a result. So, it’s way faster than a linear search (False) if you have the option of sorting the lookup list.
                    
                    I explain the binary search in this video:  
                    [https://youtu.be/GllJpJxOSvM](https://youtu.be/GllJpJxOSvM)
                    
    *   Quick Question:
        
        Is the difference in computational load between vlookup and index-match still present in the newer office suites, Excel 2013?
        
        [Reply](https://trumpexcel.com/vlookup-vs-index-match/#comment-8165)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/vlookup-vs-index-match/#respond)

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