# 10 Advanced IF formula tricks you must know » Formulas & Functions

**Source:** https://chandoo.org/wp/advanced-if-tricks

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

10 Advanced IF formula tricks you must know
===========================================

*   Last updated on March 31, 2021

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

IF is the most used Excel function out there. Here are 10 **advanced IF tricks** to take your formulas to next-level 🚀

**In this article, you will learn:**

*   Only one of, two out of three type rules
*   Between condition check with MEDIAN
*   Replacing Nested IF with shorter function
*   Using boolean logic to replace IF formulas
*   Arrays with IF function
*   Wildcard checks with IF function
*   How to use IF formula in other places
    *   Conditional formatting
    *   Data validation
    *   Charts

Sample data for the examples
----------------------------

All examples in this article use below sample data. Assume it is **in the range C8:G23**![sample-data-if-formula-advanced-tricks](https://chandoo.org/wp/wp-content/uploads/2021/03/sample-data-if-formula-advanced-tricks.png)

You can download this data alone for practice purpose from here.

[Download Example File](https://chandoo.org/wp/wp-content/uploads/2021/03/IF-formula-adv-tricks.xlsx)

Includes sample data for practice, completed Excel workbook

#1 - Only one of condition
--------------------------

Situation

Identify employees who are **only one of** gender=male or salary under $85,000

Formula

				
					`=IF(XOR(D8="Male",G8<85000),"Include", "Exclude")`
				
			

Explanation

XOR function will return TRUE if an _odd number_ inputs are TRUE, else FALSE. 

So, our XOR(D8=”Male”, G8<85000) will be useful for checking **only one of condition.**

**Note:** XOR doesn’t work when you want to check **only one of** when you have more than 2 conditions. For that refer to next trick.

**Also read:** [Either Or formula in Excel](https://chandoo.org/wp/either-or-formula-in-excel/)

#2 - Two out of Three Check
---------------------------

Situation

Flag employees when they meet _any two out of below three conditions._

*   Department is Website
*   Year of join is 2019
*   Salary is above $90,000

Formula

				
					`=IF((E8="Website")+(YEAR(F8)=2019)+(G8>90000)>=2,         "Include", "Exclude")`
				
			

Explanation

The trick is in understanding Excel treats TRUE as 1 and FALSE as 0.

So, the expression (E8=”Website”)+(YEAR(F8)=2019)+(G8>90000)

will be converted a bunch of 1s & 0s and added up, depending on the details of employee.

We can then simply check if such number is >=2 to see **if any two out of three conditions** are met.

More: [Two out of three – other ways to do it](https://chandoo.org/wp/two-out-of-three-conditions-excel/)

#3 - Using MEDIAN for Between Condition
---------------------------------------

Situation

Identify employees joined between 1-Jan-2019 and 30-Jun-2019.

Formula

				
					`=IF(MEDIAN(F8,DATE(2019,1,1),DATE(2019,6,30))=F8,         "Review","")`
				
			

Explanation

Normally, we use AND() function to check for between condition. But, you can also use MEDIAN for this. 

The pattern goes like,

\=MEDIAN(your value, above, below) = your value

The above will be TRUE if _**your value**_ is between **above** and **below** values.

For example, =MEDIAN(7, 3,9) = 7 is TRUE.

Read more: [How to write BETWEEN formula in Excel](https://chandoo.org/wp/between-formula-excel/)

#4 - Replacing Nested IF functions
----------------------------------

Situation

Calculate staff bonus based on below rules:

*   1% for Website staff
*   3 % for Sales staff joined in 2018
*   2% for others

Formula

				
					`=IFS(E8="Website",1%,         AND(E8="Sales",YEAR(F8)=2018),3%,         TRUE,2%)`
				
			

Explanation

Nested IF functions can be hard to write and tricky to maintain. That is why, you should use the newly introduced IFS() function. 

The syntax for IFS goes like this:

\=IFS(condition1, value1, condition2, value2…)

**But, IFS() doesn’t have ELSE option…?**

Well, you can use TRUE as last condition to fix this.

In the above formula TRUE, 2% part handles the ELSE case beautifully.

#5 - Boolean Logic to avoid IF formulas
---------------------------------------

Situation

Calculate staff bonus based on below rules, **but don’t use any IF formulas**:

*   1% for Website staff
*   3 % for Sales staff joined in 2018
*   2% for others

Formula

				
					`=2% - (E8="Website")*1% + AND(E8="Sales",YEAR(F8)=2018)*1%`
				
			

Explanation

You can use boolean logic checks to _altogether avoid IF formulas._ This works well when your outputs are numbers.

The above formula calculates staff bonus by using TRUE=1 & FALSE=0 notion.

Let’s test it out for below staff:

![boolean-replacement-if-sample-data](https://chandoo.org/wp/wp-content/uploads/2021/03/boolean-replacement-if-sample-data.png)

**For Gigi:**

*   2% – (FALSE)\*1% + (TRUE)\* 1% = 3%

**For Curtice:**

*   2% – (FALSE)\*1% + (FALSE)\*1% = 2%

Read more: [Daniel Ferry’s excellent I heart IF](http://www.excelhero.com/blog/2010/01/i-heart-if.html)

#6 - Checking if a value is in another list
-------------------------------------------

Situation

Check if an employee is part of on call support team  
(range: C32:C36)

Formula

				
					`=IF(COUNTIFS($C$32:$C$36,C8),"On call","Not on call")`
				
			

Explanation

We can use COUNTIFS or MATCH functions to do this. I prefer COUNTIFS.

Just count if a given data point is in another list.

**Why don’t we check >0?**

Remember, Excel treats any number other than 0 as TRUE. So we don’t need to write COUNTIFS($C$32:$C$36,C8)>0. 

#7 - Arrays with IF formula
---------------------------

Situation

Calculate median salary of website staff

Formula

				
					`=MEDIAN(IF(E8:E23="Website",G8:G23))`
				
			

Explanation

When you use arrays in the IF formula, it will return an array of outcomes too.

So for eg. =IF({TRUE,TRUE,FALSE}, {1, 2, 3}, {“A”,”B”,”C”}) will return {1, 2, “C”} 

We can use this powerful idea to calculate median salary of website staff too.

**What about ELSE part? It’s missing no?**

If you don’t mention the ELSE part of IF formula, it will simply return FALSE for those values.

So, in our case, we get 

{FALSE;90700;48950;FALSE;FALSE;107700;…FALSE}

When MEDIAN reads those values, it will ignore the FALSEs and calculate MEDIAN for rest.

Read more: [Calculating RANKIFS with Excel](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/)

Situation 2

Show all names of “Finance” staff in one cell, comma seperated.

Formula

				
					`=TEXTJOIN(",",,IF(E8:E23="Finance",C8:C23,""))`
				
			

Explanation

This works same as the MEDIAN(IF()) structure. For more applications of this technique, see the [Excel Risk Map](https://chandoo.org/wp/excel-risk-map-template/)

#8 - Wildcard based conditions
------------------------------

Situation

Identify if an employee’s name contains letters **bo**

Formula

				
					`=IF(COUNTIFS(C8,"*bo*"),"bo person","not a bo person")`
				
			

Explanation

IF function is not aware of wildcards. But we can use one of the other wildcard aware functions inside IF to solve the problem. You can use either of XLOOKUP, XMATCH, MATCH, VLOOKUP, COUNTIFS for this. 

I prefer COUNTIFS.

The COUNTIFS(C8, “\*bo\*”) will be 1 if name in C8 has **bo** in it, else 0.

Rest is self-explanatory.

Read more: [Making VLOOKUP formula go wild](https://chandoo.org/wp/using-wildcards-with-vlookup/)
 | [Not so wild lookups](https://chandoo.org/wp/not-so-wild-lookups/)

#9 - IF formula with Conditional Formatting
-------------------------------------------

Situation

Highlight employees that meet conditions specified in below cells.

![input-rules for conditional formatting](https://chandoo.org/wp/wp-content/uploads/2021/03/input-rules-for-conditional-formatting.png)

Rule

				
					`=AND($E8=$J$50,$D8=$J$51)`
				
			

Explanation

When checking rules in **conditional formatting** you don’t need to use IF formula. Just use the **condition** part of the formula alone.

Here is the result of our rule.

![result of conditional formatting](https://chandoo.org/wp/wp-content/uploads/2021/03/result-of-conditional-formatting.png)

Read more: [5 simple & useful conditional formatting tricks](https://chandoo.org/wp/5-useful-conditional-formatting-tricks/)

#10 - Using IF with Charts
--------------------------

Situation

Make a chart with employee salaries, but highlight staff making **above average salary** in a different color.

Process

1.  Add an extra column in your data and use IF formula to check if a person’s salary is above average.
2.  Make chart with both original salary & the new column.
3.  Overlap the bars (or columns) 100%
4.  Color them accordingly. 

Formula

				
					`=IF(G8>AVERAGE($G$8:$G$23),G8,NA())`
				
			

Outcome

This is how my chart looks.

![highlighting staff with above average salary](https://chandoo.org/wp/wp-content/uploads/2021/03/highlighting-satff-with-above-average-salary.png)

Read more: [How to highlight important points on your chart](https://chandoo.org/wp/how-to-highlight-maximum-value-in-excel-charts/)

Resources - File & Video
------------------------

[Download Example File](https://chandoo.org/wp/wp-content/uploads/2021/03/IF-formula-adv-tricks.xlsx)

Includes sample data for practice, completed Excel workbook

### Watch the video & learn these techniques

More on IF formula
------------------

Resources

Check out below tutorials to master IF formulas & business logic

*   [Business logic with Excel](https://chandoo.org/wp/cp028-how-to-tell-business-logic-rules-to-excel/)
     – podcast episode
*   [CHOOSE formula – an excellent replacement for IF](https://chandoo.org/wp/introduction-to-choose-function/)
    
*   [IFERROR – dealing with errors in your worksheet](https://chandoo.org/wp/iferror-formula/)
    

Homework problems

Use these homework problems to sharpen your if muscle.

*   [Blood pressure category problem](https://chandoo.org/wp/bp-category-problem/)
    
*   [Sumerian voter problem](https://chandoo.org/wp/sumerian-voter-problem/)
    
*   [Check if two dates are in same month](https://chandoo.org/wp/two-dates-in-month-check/)
    

What is your favorite IF formula trick?
---------------------------------------

Share it in the comments. Let’s learn from each other.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [16 Comments](https://chandoo.org/wp/advanced-if-tricks/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/advanced-if-tricks/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [between formula](https://chandoo.org/wp/tag/between-formula/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel formulas](https://chandoo.org/wp/tag/excel-formulas/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [ifs](https://chandoo.org/wp/tag/ifs/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [median](https://chandoo.org/wp/tag/median/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousWrite a formula to get Department Budget for a Month \[Homework\]](https://chandoo.org/wp/department-budget-problem/)

[NextExtract data from PDF to Excel – Step by Step TutorialNext](https://chandoo.org/wp/extract-data-from-pdf-to-excel/)

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
    
    [Reply](https://chandoo.org/wp/advanced-if-tricks/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/advanced-if-tricks/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/advanced-if-tricks/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ