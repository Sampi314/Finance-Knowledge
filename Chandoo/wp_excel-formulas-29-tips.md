# Excel Formulas for all Occasions - 29 Excel formula tips for everyday use

**Source:** https://chandoo.org/wp/excel-formulas-29-tips

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

29 Excel Formula Tips for all Occasions \[and proof that PHD readers truly rock\]
=================================================================================

*   Last updated on September 21, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

It is no exaggeration that knowing excel formulas can give you a career boost. From someone starting at the long list of numbers, you can become a data god who can lookup, manipulate and analyze any spreadsheet by [learning few excel formulas](http://chandoo.org/excel-formulas/)
.

So when our little excel blog hit the 5000 RSS Subscriber milestone, I celebrated the occasion by [asking you to share an excel formula through twitter or comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/)
 with rest of us. And boy, what an excellent list of formula tips you have shared with us all.

_**Here is the complete list of entries for the twitter formula contest.**_

Follow the links next to contributor’s name to see the original twitter post or comment

To return the full Path+Filename of your (saved) workbook
---------------------------------------------------------

_by Dmurphy on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72387)
_

To return the full Path+Filename of your (saved) workbook (and dropping the \[\] characters) to get, for example, C:\\Data\\ExcelFiles\\MyWorkbook.xls: =SUBSTITUTE(SUBSTITUTE(LEFT(CELL(”filename”,$A$1), FIND(”\]”,CELL(”filename”,$A$1))),”\[“,””),”\]“,””)

Create a Dynamic Range that Grows and Shrinks with Data
-------------------------------------------------------

_by ps62 on [twitter](http://twitter.com/ps62/status/3127905481)
 \[[@ps62](http://twitter.com/ps62)\
\]_

IF($A6=””,””, SUM(OFFSET(Data,$A6-1,StartDateIndex-1,1,NumCols))) – makes stuff dynamic

Find the last cell in a row
---------------------------

_by govi on [twitter](http://twitter.com/govi/status/3102901135)
 \[[@govi](http://twitter.com/govi)\
\]_

Return last filled cell in a row: =LOOKUP(9,999E+307;A1:IV1)

Cleaning your data (Example, changing the values in a column)
-------------------------------------------------------------

_by artjohnson on [twitter](http://twitter.com/artjohnson/status/3111938996)
 \[[@artjohnson](http://twitter.com/artjohnson)\
\]_

Excel. Cust name header in C9 and text datalist below. Formula in B9 moves name from C9 to B9. Copy down. =if(isblank(C8),c9,b8)

Extract the month from a date
-----------------------------

_by Alan on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72898)
_

Probably a easier way of doing this , extracting the month from a date as text. A1 is date =TEXT(DATE(0,MONTH(a1),1),”mmmm”)

Clean your text before you lookup
---------------------------------

_by rushikul on [twitter](http://twitter.com/rushikul/status/3143743979)
 \[[@rushikul](http://twitter.com/rushikul)\
\]_

\=VLOOKUP(CLEAN(TRIM(E20)),F5:G18,2,0). To make sure you are using clear text, as text is most used in vookup\_value

Find if two ranges are statistically different
----------------------------------------------

_by nandoaires on [twitter](http://twitter.com/nandoaires/status/3155166434)
 \[[@nandoaires](http://twitter.com/nandoaires)\
\]_

\=IF((1-(1-NORMSDIST(ABS(A1-A2)/SQRT((2\*AVERAGE(A1:A2)\*(1-AVERAGE(A1:A2)))/(A3))))\*2)>0,95;”Different”;”Equals”)

Lookup 3 criteria and return the match
--------------------------------------

_by Alan\_xls on [twitter](http://twitter.com/Alan_xls/status/3192134445)
 \[[@Alan\_xls](http://twitter.com/Alan_xls)\
\]_

\=Index(return,Match(1,(1stRange=criteria1)\*(2ndRange=criteria2)\*(3rdRange=criteria3),0)) Return result where 3 values match,Array Form

Offset with Match, get data from somewhere else
-----------------------------------------------

_by Arnab Bose on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-73773)
_

This formula looks up data from another sheet considering three parameters keeping into account the column A and column B with sub-components (both on another sheet) and matching them up with the heading on both sheets. =OFFSET(’Data Sheet’!$C$1,MATCH(D$2,’Data Sheet’!$A$2:$A$140,0)+MATCH($B5,’Data Sheet’!$B$2:$B$20,0)-1,MATCH(D$3,’Data Sheet’!$C$1:$J$1,0)-1)

Using SUM with multiple conditions
----------------------------------

_by ps62 on [twitter](http://twitter.com/ps62/status/3128021908)
 \[[@ps62](http://twitter.com/ps62)\
\]_

{=SUM(IF(shoes=”nike”,Units,0))} – array formula – two conditions

VLOOKUP but get values from the left
------------------------------------

_by bsamson on [twitter](http://twitter.com/bsamson/status/3104007783)
 \[[@bsamson](http://twitter.com/bsamson)\
\]_

VLookup to return values to the left of the lookup range: =INDEX(SearchRange,MATCH(LookupValue,LookupRange,FALSE))

Getting data from a dynamic range
---------------------------------

_by Arnab Bose on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-73775)
_

This formula extracts data from a dynamic data range and returns a zero value if there is an #N/A error. =IF(ISNA(HLOOKUP($A14,Data!$AB$2:$AW$9,MATCH(”P”,Data!$AB$2:$AB$2,0),0)), 0,HLOOKUP($A14,Data!$AB$2:$AW$9,MATCH(”P”,Data!$AB$2:$AB$2,0),0))

Find the difference between maximums of two ranges
--------------------------------------------------

_by PreetAulakh on [twitter](http://twitter.com/PreetAulakh/status/3115713262)
 \[[@PreetAulakh](http://twitter.com/PreetAulakh)\
\]_

{=MAX(K5:M5-K4:M4)}, one step formula to determine the max of difference of two ranges! No curly brackets in excel, Cltr+Shift+Enter

Find the top 3 values of a range
--------------------------------

_by JassiAulakh on [twitter](http://twitter.com/JassiAulakh/status/3119146544)
 \[[@JassiAulakh](http://twitter.com/JassiAulakh)\
\]_

Large(A1:A100,{1,2,3}). Gives you 3 highest values of a range. Select three cells and enter this formulas. Then Cltr+Shift+Enter

SUMPRODUCT with multiple conditions
-----------------------------------

_by Martin on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72273)
_

Here’s my little contribution (previously posted 😉 Named Ranges (should be dynamic, but….) Ship $A$2:$A$8 Captain $B$2:$B$8 flights $C$2:$C$8 in F:F Summary\_ship $F$2:$I$2 this 3:3 Summary\_Captain $E$3:$E$6 data is in range A1:C8, and summary is in E1:I6. =SUMPRODUCT((Ship=in Summary\_ship)\*(Captain=this Summary\_Captain)\*(flights))

Get the name of the workbook
----------------------------

_by Dmurphy on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72391)
_

To return the name of the workbook only, e.g. MyWorkbook.xls: =MID(CELL(”filename”,$A$1),FIND(”\[“,CELL(“filename”,$A$1))+1,FIND(“\]“,CELL(”filename”,$A$1))-FIND(”\[”,CELL(”filename”,$A$1))-1)\
\
Excel Formula Fun – Should we fight… ?\
--------------------------------------\
\
_by chrismelck on [twitter](http://twitter.com/chrismelck/status/3133463856)\
 \[[@chrismelck](http://twitter.com/chrismelck)\
\]_\
\
\=IF(ISERROR(VLOOKUP(WOMD,Iraq,1,FALSE)),”Declare war”,”Declare war anyway”)\
\
More ways to use IF and Then formula\
------------------------------------\
\
_by Olu D. on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72309)\
_\
\
This formula determines the Active (=”T”) status or otherwise of Employees in an Excel spreadsheet: =IF(AC2=””,”X”,IF(AND(AC2=500000,AD2=””),”T”,IF(AND(AC2500000,AD2?”),”F”,”Pls Enter Leaving Reason!!”)))\
\
Using INDIRECT along with VLOOKUP to make dynamic lookups\
---------------------------------------------------------\
\
_by squash86 on [twitter](http://twitter.com/squash86/status/3104259854)\
 \[[@squash86](http://twitter.com/squash86)\
\]_\
\
\=VLOOKUP(B3, INDIRECT(B36), COLUMN()-1,FALSE) The INDIRECT returns the name of a named range that holds the data table.\
\
Calculate the p-value of a t-statistic \[Don’t ask me what it is 😛 \]\
----------------------------------------------------------------------\
\
_by David on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72280)\
_\
\
\=NORMDIST(-1\*ABS((Z27-AE27)/AG27),0,1,TRUE). Calculate p-value for t-statistic based on means in Z27 and AE27 and the std err of mean in AG27.\
\
What is on the right side of that string\
----------------------------------------\
\
_by aniVy on [twitter](http://twitter.com/aniVy/status/3107949809)\
 \[[@aniVy](http://twitter.com/aniVy)\
\]_\
\
\=RIGHT(A1,LEN(A1)-FIND(“-“,A1,1)) – Extracts right side string after a hyphen.\
\
Find frequency distribution of a range of values\
------------------------------------------------\
\
_by Cody on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72312)\
_\
\
\=FREQUENCY(DY5:DY118,EU4:EU14) for creating frequency distributions. I can’t believe I went so long before discovering that there’s an easy built-in array function that does this. Constructing the distribution by hand was always a pain.\
\
In-cell bar graph\
-----------------\
\
_by JohnCorp on [twitter](http://twitter.com/JohnCorp/status/3104159281)\
 \[[@JohnCorp](http://twitter.com/JohnCorp)\
\]_\
\
\=REPT(“|”,A1/MAX($A$1:$A$5)\*30) creates a bar graph from the data in the range a1:a5, change the font to change the look of the graph\
\
Get the name of the current worksheet\
-------------------------------------\
\
_by Dmurphy on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72388)\
_\
\
To return the name fo the current worksheet, e.g. “Sheet1?: =MID(CELL(”filename”,$A$1),FIND(”\]”,CELL(”filename”,$A$1))+1, LEN(CELL(”filename”,$A$1))-FIND(”\]”,CELL(”filename”,$A$1)))

Excel formula fun – Usetheforce()
---------------------------------

_by \_mikii on [twitter](http://twitter.com/_mikii/status/3104270743)
 \[[@\_mikii](http://twitter.com/_mikii)\
\]_

\=usetheforce(choke,”Moff Jerjerrod”)

UDF to calculate to royalty, I am not getting any
-------------------------------------------------

_by chrislbs on [twitter](http://twitter.com/chrislbs/status/3126789183)
 \[[@chrislbs](http://twitter.com/chrislbs)\
\]_

\=TieredRoyalty($R$16:$T$19,I5) @r1c1 Uses a UDF to calculate royalty on I5 based on a TierTable in R16:T19, saving nested vlookups

Find the Next Friday the 13th
-----------------------------

_by S3bast1an on [twitter](http://twitter.com/S3bast1an/status/3110759935)
 \[[@S3bast1an](http://twitter.com/S3bast1an)\
\]_

ARRAYformula – Next Friday 13th is =MIN(IF(((WEEKDAY(TODAY()+ROW(1:1000);2)=5)\*(DAY(TODAY()+ROW(1:1000))=13))=1;TODAY()+ROW(1:1000)))

Split first name and last name
------------------------------

_by Mahmut on [PHD comments](http://chandoo.org/wp/2009/08/03/twitter-formula-contest/#comment-72282)
_

\=LEFT(A1,FIND(” “,A1)-1) =RIGHT(A1,LEN(A1)-FIND(” “,A1)) Split first names and last names.

IF with a VLOOKUP
-----------------

_by m4th1337 on [twitter](http://twitter.com/m4th1337/status/3107667137)
 \[[@m4th1337](http://twitter.com/m4th1337)\
\]_

\=IF(VLOOKUP(C1,’Historical Data’!$A$2:$S$332,4,FALSE)>F1,”-“,IF(VLOOKUP(C1,’Historical Data’!$A$2:$S$332,4,FALSE)

And now for the winners
-----------------------

I wish I had more prizes to give. All the tips are truly marvelous. I have learned several cool uses of excel formulas. But alas, we have only 2 prizes in this contest.

**[Dashboard bundle from Bonavista Systems](http://www.bonavistasystems.com/Products_Purchase.html)
 goes to Govi**

**[The excel formulas 2007 book](http://www.amazon.com/gp/product/0470044020?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0470044020)
 by John Walkenbach goes to DMurphy**

Both the winners are randomly selected. I have already sent them an e-mail with the further instructions to claim the prizes.

Big thank you to Bonavista Systems, the contest sponsor
-------------------------------------------------------

**I would like to thank Andreas from [Bonavista systems](http://www.bonavistasystems.com/)
 for sponsoring the dashboard bundle.** Bonavista systems makes some really cool tools for excel dashboards, spark-lines and helps you make cleaner and better looking charts. Checkout their products and know more about them from [their site](http://www.bonavistasystems.com/)
.

Further Resources if you want to learn Excel Formulas
-----------------------------------------------------

*   [15 Excel formulas to transform you from beginner to pro](https://chandoo.org/wp/excel-formulas-29-tips/chandoo.org/wp/2008/08/13/15-microsoft-excel-formulas/)
    
*   Important excel formulas: [IF and Then](http://chandoo.org/wp/2008/06/09/what-the-if-learn-6-cool-things-you-can-do-with-excel-if-functions/)
    , [Vlookup](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    , [Offset](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    , [Sumif](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)
    , [Countif](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)
    , [Working with date and time](http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/)
    
*   [Debug excel formula errors](https://chandoo.org/wp/excel-formulas-29-tips/chandoo.org/wp/2009/04/20/excel-formula-errors/)
    
*   [50 Everyday excel formulas explained in plain English](http://chandoo.org/excel-formulas/)
    

* * *

[![](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-formula-ebook-ad.png)](http://chandoo.org/wp/excel-formula-helper-e-book/ "E-book to learn excel formulas")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/excel-formulas-29-tips/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-formulas-29-tips/#respond)
    
*   Tagged under [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [cell](https://chandoo.org/wp/tag/cell/)
    , [countif()](https://chandoo.org/wp/tag/countif/)
    , [Excel Howtos](https://chandoo.org/wp/tag/excel-howtos/)
    , [find](https://chandoo.org/wp/tag/find/)
    , [frequency()](https://chandoo.org/wp/tag/frequency/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [INDIRECT()](https://chandoo.org/wp/tag/indirect/)
    , [isblank()](https://chandoo.org/wp/tag/isblank/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [left()](https://chandoo.org/wp/tag/left/)
    , [len()](https://chandoo.org/wp/tag/len/)
    , [lists](https://chandoo.org/wp/tag/lists/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [mid()](https://chandoo.org/wp/tag/mid/)
    , [MIN()](https://chandoo.org/wp/tag/min/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [right()](https://chandoo.org/wp/tag/right/)
    , [small](https://chandoo.org/wp/tag/small/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [substitute()](https://chandoo.org/wp/tag/substitute/)
    , [sum()](https://chandoo.org/wp/tag/sum/)
    , [sumif()](https://chandoo.org/wp/tag/sumif/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    , [udf](https://chandoo.org/wp/tag/udf/)
    , [user content](https://chandoo.org/wp/tag/user-content/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious50 Best Cities for Finding a Job \[Incell Dashboard using Excel\]](https://chandoo.org/wp/incell-job-finding-dashboard/)

[NextMake a Pivot Table in Excel \[15 Second Tutorial\]Next](https://chandoo.org/wp/make-a-pivot-table-in-excel-15-second-tutorial/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/excel-formulas-29-tips/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-formulas-29-tips/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-formulas-29-tips/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ