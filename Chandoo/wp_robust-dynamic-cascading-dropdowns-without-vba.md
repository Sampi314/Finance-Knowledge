# Robust Dynamic (Cascading) Dropdowns Without VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/robust-dynamic-cascading-dropdowns-without-vba

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

Robust Dynamic (Cascading) Dropdowns Without VBA
================================================

*   Last updated on February 14, 2024

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

Recently I posted about how you could [construct dynamic (cascading) dropdowns](http://chandoo.org/wp/2014/02/13/dynamic-cascading-dropdowns-that-reset/ "Dynamic (Cascading) Dropdowns that reset on change")
 that could easily handle multiple levels, like this:  
[![Chandoo_CascadingDropdowns_Earliglow](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Earliglow.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Earliglow.png)

…and we saw that users could subsequently change _upstream_ dropdowns in a way that would make _downstream_ choices invalid, like this:  
[![Chandoo_CascadingDropdowns_Embarrassing](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Embarrassing.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Embarrassing.png)
  
In my previous post I used some VBA to clear out any ‘downstream’ choices if anything ‘upstream’ changed:  
[![Chandoo_CascadingDropdowns_Downstream Reset](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Downstream-Reset.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Downstream-Reset.png)

Updated for 2024:
-----------------

[**Please see my latest article on Dependent Drop-downs**](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/)
 using XLOOKUP to implement a simpler and scalable technique. It works great when you have two or multiple levels and can be expanded to an entire table column or sheet column.

A much simpler alternative
--------------------------

My sample file drew on [Roger Govier’s excellent approach on the Contextures](http://www.contextures.com/xlDataVal15.html)
 website, which used two dynamic named ranges to feed the data validation lists, one called **MainList** and one called **SubList**. [Roberto commented](http://chandoo.org/wp/2014/02/13/dynamic-cascading-dropdowns-that-reset/#comment-471050)
 that you could achieve pretty much the same thing with **no** VBA and with just **one** validation formula. His approach is pure genius!

Here’s a sample file that utilizes Roberto’s approach:

**[Click here to download the file](https://chandoo.org/wp/wp-content/uploads/2014/02/Dynamic-Dependent-dropdowns_One-Formula-with-no-VBA-20140226.xlsm)
**

This approach uses a validation formula with a couple of **relative references** in it. Relative references look for cells that are some predetermined distance left/right and up/down from the active cell. Here’s his formula, which was entered into the Name Manager while cell B8 was selected:  
\=IF(ISBLANK(Sheet1!C8),IF(DataEntry\[#Headers\] Sheet1!B:B = DataEntry\[\[#Headers\],\[Main Category\]\],OFFSET(ValidationLists\[\[#All\],\[Main Categories\]\],1,,COUNTA(ValidationLists\[Main Categories\])),OFFSET(ValidationLists,0,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,COUNTA(OFFSET(ValidationLists,,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,,1)),1)))

This formulas assumes:

*   You use **Excel Tables** for both the Validation List and the data entry area, and so uses the associated Structured References that Table functionality allows.
*   Your validation table is called ValidationLists
*   Your data entry table where the dropdowns are is called table is called DataEntry.
*   The column containing your initial dropdowns is called ‘Main Category’
*   The validation list in your validation table that contains your initial categories is called ‘Main Categories’

You will have to amend this formula accordingly if your tables or initial columns have different names.

The **relative** reference in this formula checks both the cell to the immediate left AND the cell to the immediate right of your current selection. Entering relative references into the Name Manager can be tricky…**you first need to select the cell where the formula was originally created** – in this case B8 – **_before_** you fire up the Name Manager dialog box. (Note that it doesn’t actually matter whether your own file has anything in C8 or not, or whether in fact your dropdowns are somewhere else entirely…rather it’s just that the above formula happens to refer to A8 and C8, and because we want our formula to always reference the cell on the immediate left and immediate right, then we’ve got to select the cell B8 which is in the middle.

Excel Tables – known as ListObjects to VBA developers – were introduced in Excel 2007, and are a very powerful and simple way to store things like lists, chart data, and PivotTable data…especially if you might need to add more data to your spreadsheet at a later date, and want to avoid having to repoint all your formulas to include the additional data. If you’re not familiar with Excel Tables – or you don’t know what that Table1\[#Headers\] guff above means – then I strongly suggest you check out Chandoo’s [Introduction to Structural References](http://chandoo.org/wp/introduction-to-structural-references/ "Introduction to Structural References")
 or give GOOGLE a spin.

How does this awesome beast work?
---------------------------------

Let’s step through it, bit by bit. Note that I’ve put some extra spaces in after each opening formula bracket, purely so this formula will wrap nicely on your monitor. Excel just ignores these extra spaces, so don’t bother taking them out.

\=**IF(ISBLANK(Sheet1!C8)**,IF(DataEntry\[#Headers\] Sheet1!B:B = DataEntry\[\[#Headers\],\[Main Category\]\],OFFSET(ValidationLists\[\[#All\],\[Main Categories\]\],1,,COUNTA(ValidationLists\[Main Categories\])),OFFSET(ValidationLists,0,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,COUNTA(OFFSET(ValidationLists,,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,,1)),1)))

That first bit in bold above checks the cell on the immediate right. If that cell on the right is **_not_ blank**, then that means that the user has already made ‘downstream’ selections. We don’t want the user to change this ‘upstream’ dropdown without clearing those out. Thanks to the IF statement, if that’s the case then none of the rest of the formula gets executed, and the formula just returns FALSE. Data validation can’t handle this FALSE, so users can click on the dropdown button all they like, but nothing will come up. Consequently, the user simply can’t change this ‘upstream’ selection until they’ve first cleared out any selections they previously made in the cells to the right. Pure genius.

Here’s what that looks like:  
[![Chandoo_Robust Dropdowns without VBA_No dropdown](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_Robust-Dropdowns-without-VBA_No-dropdown.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_Robust-Dropdowns-without-VBA_No-dropdown.gif)
  
[![Chandoo_Robust Dropdowns without VBA_Retrospective change](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_Robust-Dropdowns-without-VBA_Retrospective-change.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_Robust-Dropdowns-without-VBA_Retrospective-change.gif)
  
_Sweet!_ Okay, let’s take a look at the rest of the formula:

\=IF(ISBLANK(Sheet1!C8),**IF(DataEntry\[#Headers\] Sheet1!B:B = DataEntry\[\[#Headers\],\[Main Category\]\]**,OFFSET(ValidationLists\[\[#All\],\[Main Categories\]\],1,,COUNTA(ValidationLists\[Main Categories\])),OFFSET(ValidationLists,0,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,COUNTA(OFFSET(ValidationLists,,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,,1)),1)))

That bit in bold above checks whether the dropdown is the _Main Category_ column. It does this using the INTERSECT operator, which is a space between two references (in this case of DataEntry\[#Headers\] B:B the INTERSECT operator is the space between **DataEntry\[#Headers\]** and the column reference **B:B**. Such a space tells Excel to go to the _overlap_ or _intersection_ of those two references, which in this case is the junction between the header row and the column that our dropdown is in.

*   If the current dropdown **is** in the Main Category column, then _this_ bold bit:  
    \=IF(ISBLANK(Sheet1!C8),IF(DataEntry\[#Headers\] Sheet1!B:B = DataEntry\[\[#Headers\],\[Main Category\]\],**OFFSET(ValidationLists\[\[#All\],\[Main Categories\]\],1,,COUNTA(ValidationLists\[Main Categories\]))**,OFFSET(ValidationLists,0,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,COUNTA(OFFSET(ValidationLists,,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,,1)),1)))  
    …serves up just the list containing our initial categories (i.e. ‘Fruit’, ‘Vegetables’, or ‘Other Stuff’ in this example).
*   If the current dropdown **is _not_** in the Main Category column, then _this_ bold bit:  
    \=IF(ISBLANK(Sheet1!C8),IF(DataEntry\[#Headers\] Sheet1!B:B = DataEntry\[\[#Headers\],\[Main Category\]\],OFFSET(ValidationLists\[\[#All\],\[Main Categories\]\],1,,COUNTA(ValidationLists\[Main Categories\])),**OFFSET(ValidationLists,0,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,COUNTA(OFFSET(ValidationLists,,MATCH(Sheet1!A8, ValidationLists\[#Headers\],0)-1,,1)),1)**))  
    …serves up the particular list relevant given the previous choice made in the dropdown to the left.

Wicked, eh!

Normally I don’t advocate the use of volatile functions such as OFFSET if there is a non-volatile alternate (and you’ll hear more about volatility from me in a forthcoming post). But as Roberto points out in his original comment, in this case it doesn’t matter…choices made via dropdowns are not considered volatile by Excel, even if the formulas used to populate that dropdown _are_ volatile.

Like Roger’s approach, Roberto’s approach can handle any number of cascading levels, provided all the category names are unique. All you need to do is simply add the new subcategories to the right hand side of the validations table.

Thanks Roberto…I learned a lot from those comments. Readers, be sure to [visit the Frankens Team](https://sites.google.com/site/e90e50charts/)
 and check out the crazy things Roberto, Kris & Gábor get up to with Excel.

Download the sample file
------------------------

Here’s a sample file that utilizes Roberto’s approach:

**[Click here to download the file](https://chandoo.org/wp/wp-content/uploads/2014/02/Dynamic-Dependent-dropdowns_One-Formula-with-no-VBA-20140226.xlsm)
**

Updates
-------

Check out the updated **[2024 version of this technique](https://chandoo.org/wp/how-to-create-dependent-drop-downs-in-excel-dynamic-multiple/)
** with XLOOKUP. The formulas are much simpler and it works with any level of validations.

You may also want to check out my good pal [Doug Glancy’s approach to this](http://yoursumbuddy.com/user-friendly-survey-without-vba/)
. His version of dependent dropdowns uses Conditional Formatting to alert the user, and ultimately, the analyst, that something is amiss. Be sure to say hi to him in the comments while you’re there, and to subscribe to his blog. Anyone who makes up sample files about fictional International Pie Lovers Associations deserves our eyeballs!

About the Author.
-----------------

Jeff Weir – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure **_#VALUE!_**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [59 Comments](https://chandoo.org/wp/robust-dynamic-cascading-dropdowns-without-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/robust-dynamic-cascading-dropdowns-without-vba/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [drop down lists](https://chandoo.org/wp/tag/drop-down-lists/)
    , [dynamic named ranges](https://chandoo.org/wp/tag/dynamic-named-ranges/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

[PrevPreviousWhat should we call our Podcast?](https://chandoo.org/wp/podcast-announcement/)

[NextCan you extract first name & last name from email address? \[Formula Challenge\]Next](https://chandoo.org/wp/extract-first-name-last-name-from-email/)

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

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ