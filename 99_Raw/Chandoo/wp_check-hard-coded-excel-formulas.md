# How to check for hard-coded values in Excel formulas? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/check-hard-coded-excel-formulas

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

How to check for hard-coded values in Excel formulas?
=====================================================

*   Last updated on January 14, 2015

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_Here is a common problem._ Imagine you are looking a complex spreadsheet, aptly titled “Corporate Strategy 2020.xlsx” which as 17 tabs, umpteen formulas and unclean structure. Whoever designed it was in insane hurry. The workbook has formulas like this, =SUM(Budget!A2:A30, 3600)+7925 .

It was as if Homer Simpson created it while Peter Griffin oversaw the project.

_**So how do you go about detecting all cells containing formulas with hard-coded values?**_

![Finding hardcoded formula values in Excel - how to?](https://img.chandoo.org/vba/finding-hard-coded-values-in-excel-formulas.png)

### Alas, the usual methods fail

The usual methods to audit formulas are of no help here. Let’s see:

**Show formulas (CTRL+\`):** Since we have way too many formulas, this approach requires a lot of squinting and gallons of coffee.

**Go to special > Constants:** This will only detect constant cells (ie input cells), but not cells containing formulas like =IF(2=2, Budget2014!A2, Budget2015!A2)

**Trace Precedents:** This can be used only for formulas that contain all hard-coded values (ex: SUM(1,2,3) will have no arrows, where as SUM(A1,A2, 7) will have some arrows

**FORMULATEXT():** There is a new function called as FORMULATEXT() introduced in Excel 2013. This can tell us what is the formula in a cell. But we still need to develop additional logic to see if the formula text contains any constants.

### Let’s build ‘Detect hard-coded formulas’ feature for Excel

The beauty of Excel is that, if there is something you can’t do with on screen features, you can build it. This is where [VBA](http://chandoo.org/wp/excel-vba/)
 comes handy.

So we can create a hasConstants() user defined function that takes a cell as input and tells us TRUE or FALSE. True if the cell has constants (or hard-coded values) as formula parameters and False otherwise.

**But what should be the logic for hasConstants()?**

The process for detecting hard-coded values can be defined like this:

1.  Read the formula from left to right
2.  For each argument of the formula
    1.  See if the argument is a valid reference or name
    2.  If not, break the loop and return TRUE
3.  Return FALSE

**How do we detect only the parameters?**

There is no direct way to extract only the parameters of a formula. So what we do is we split the formula in to an array using the delimiter COMMA.

And we check each item of this array to see if it is

*   a function call (like SUM, COUNT, VLOOKUP)
*   a valid name or reference

**What about nested functions?**

The approach works the same way.

**What about arithmetic, text or comparison operations?**

For example, a formula like =A1+A2+17 should throw TRUE as it has hard-coded value.

So what we do is, we replace all such operators with delimiter (COMMA) before splitting the formula text.

We can consider +-\*/%&><= as operators.

### So how does the code look like?

Here is how it looks like:

    
    Const COMMA = ","
    Const OPERATORS = "+-*/%^&><="
    
    Public Function hasConstants(thisCell As Range) As Boolean
        'finds out if thisCell has a formula with constants in it
        'i.e. hardcoded values
        
        Dim formula As String, args As Variant, i As Long
        Dim testRange As Range
        
        formula = replaceOperators(Mid(thisCell.formula, 2))
        
        args = Split(formula, COMMA)
        
        For i = LBound(args) To UBound(args)
            If Not (Len(args(i)) = 0 Or Right(args(i), 1) = "(" Or args(i) = ")") Then
                'not a function or null, must be one of the parameters
                'see if it is a valid name or reference
                If Not nameExists(CStr(args(i))) Then
                    'name or reference doesn't exist, must be a constant / hard-coded value
                    hasConstants = True
                    Exit Function
                End If
           End If
        Next i
    End Function
    
    Function replaceOperators(formula As String) As String
        'replace operators such as +-/%^&>< with COMMA
        Dim char As Long
        
        For char = 1 To Len(OPERATORS)
            formula = Replace(formula, Mid(OPERATORS, char, 1), COMMA)
        Next char
        formula = Replace(formula, "(", "(" & COMMA)
        formula = Replace(formula, ")", COMMA & ")")
        replaceOperators = formula
        
    End Function
    
    Function nameExists(name As String) As Boolean
        'Check if a name or reference is valid
        Dim testR As Range
        
        On Error GoTo last
        
        Set testR = Range(name)
        nameExists = True
        Set testR = Nothing
    last:
    
    End Function
    

### How to use this code?

Simple. Copy this code and add it to your personal macros workbook. (Tip: [how to setup personal macros workbook?](http://chandoo.org/wp/2013/11/18/using-personal-macro-workbook/)
)

![Conditional formatting to check hardcoded formula values](https://img.chandoo.org/vba/conditional-formatting-hardcoded-formulas.png)Then use it in your complex workbook like this:

*   To check if a cell contains hardcoded formulas, write =hasConstants(A1)
*   To check if an entire range has hardcoded values,
    1.  Select the range
    2.  Go to home > conditional formatting > new rule
    3.  Select formula type rule
    4.  Type =hasConstants(top-left-cell relative reference)
    5.  Format by filling a color or changing font style to detect easily
    6.  Done

### Does it work in all cases?

For most normal formulas this approach should work. I have tested it with various combinations and it seems to hold up good. I suggest you to **double check the results** for any type II errors (ie missed hard coded formulas) during initial few rounds.

Also, please share your observations in the comments so that we can improve this code.

### Download Example Workbook

**[Click here to download this VBA code](https://img.chandoo.org/vba/check-formula-constants.xlsm)
.** After downloading the file, go to Module 1 (press ALT+F11) to see the code. Copy it or modify it as you see fit.

### Your comments please?

I never had the need to check for hard-coded values until recently. But once I had that need, I found there is no simple way to do it. I believe this kind of check can be very useful for people in modeling, risk management or auditing positions.

**What about you?** How do you check for hard coded formulas? What methods do you use? Please share your thoughts and tips in the comments section.

**More on spreadsheet auditing & risk management:**

Check out below articles to learn more about how to audit spreadsheets and prevent risk of miscalculation:

*   [Spreadsheet risk management – 4 part series](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/)
    
*   [Show all names & references](http://chandoo.org/wp/2010/09/20/show-all-names-excel/)
    
*   [Go to special, a powerful way to navigate your workbooks](http://chandoo.org/wp/2012/03/12/go-to-special/)
    

  

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [40 Comments](https://chandoo.org/wp/check-hard-coded-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/check-hard-coded-excel-formulas/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [spreadsheet audit](https://chandoo.org/wp/tag/spreadsheet-audit/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPrevious8 Reasons you must get better at Excel in 2015](https://chandoo.org/wp/get-better-at-excel-this-year/)

[NextHow can I help you become awesome this year?Next](https://chandoo.org/wp/2015-survey/)

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
    
    [Reply](https://chandoo.org/wp/check-hard-coded-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/check-hard-coded-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/check-hard-coded-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ