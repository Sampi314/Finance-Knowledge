# Excel Database Functions: Tutorial, Video, and Template

**Source:** https://breakingintowallstreet.com/kb/excel/excel-database-functions

---

Excel Database Functions: How to Use Them \[Tutorial Video\] (21:22)
====================================================================

In this lesson, you’ll learn how to query and aggregate data tables more effectively with Database Functions such as DSUM and DCOUNT – and you’ll understand how to enter complex sets of AND and OR conditions to do so.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/excel/excel-database-functions/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/excel/excel-database-functions/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/excel/excel-database-functions/#tab-signup)
    

Excel Database Functions: How to Use Them

Excel database functions
------------------------

Excel database functions fix some, but not all, of the problems with long SUMIFS and SUMPRODUCT formulas.

For example, formulas that use SUMIFS and SUMPRODUCT are often difficult to enter and understand, sometimes dates don’t work correctly, and it’s difficult to set up criteria such as orders that match a certain date range AND a certain Sales Rep but NOT a certain industry.

> **Excel Database Functions Definition:** Excel database functions allow you to sum and count data in spreadsheets based on AND and OR conditions that join together multiple sets of criteria, such as dates, amounts, geographies, industries, and product identifiers.

Database functions do require more time to set up because you must create extra rows in the spreadsheet, and you must get the syntax _exactly right_, or nothing will work.

A basic Database function setup might look like this:

![Excel Database Functions - Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201017%20328'%3E%3C/svg%3E "Excel Database Functions - Example")

Some of the key Excel database functions include the following:

**\=DSUM:** Add numbers in a field (i.e., table column) that match specific conditions

**\=DCOUNT:** Count # cells in a field (i.e., a table column) that match specific conditions

**\=DCOUNTA:** Same, but only for nonblank cells

**\=DGET:** Extracts single row from table that matches specific conditions

![Excel & VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Learn Excel Shortcuts, Formulas, Graphs, Data, and VBA for Automation

*   #### Become a shortcut, formula & formatting machine
    
    Excel will be your “native language” after you finish this course
    
*   #### Learn the skills with dozens of practice exercises
    
    Learn by doing and check your work against the solutions
    
*   #### Shave hours off your workday with VBA and macros
    
    Automate repetitive tasks, format spreadsheets quickly, and more
    

[Full Details](https://breakingintowallstreet.com/excel-vba/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Excel-VBA-Course-Outline.pdf)

How Database Functions Work
---------------------------

A few notes on the functionality in the screenshot above:

1) The **order** of the fields in this area must be the same as the order of the fields in the table itself (Order\_Table). If Order Date follows Amount in the table, Order Date must follow Amount here:

![Excel Database Functions - Order of the Fields](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20395'%3E%3C/svg%3E "Excel Database Functions - Order of the Fields")

2) You do **NOT** need to use _all_ the fields in the table – you can choose any of them. We only use a few fields from the table here.

3) And you can **repeat** the same field multiple times as long as the repeats are all entered after the first entry, with nothing in between.

4) In a single row, the conditions are joined with **AND**. In other words, for the first row here, matching entries must be in the “Industrials” industry, the “Midwest” region, AND between January 1, 2021 and December 31, 2024.

5) Multiple rows are joined with **OR**. So, in the example above, matching entries must be in the “Industrials” industry, the “Midwest” region, AND between January 1, 2021 and December 31, 2024… **OR** they must be in the “Energy” industry, the “Northeast” region, AND between January 1, 2021 and December 31, 2024.

6) The last part – Summary!$J$6:$P$8 – cannot include empty rows, or Database functions such as DSUM will sum up the entire table.

Database functions are most useful for writing queries with complex criteria, such as ones that involve multiple dates, amounts, regions, industries, and more.

They tend to be overkill for simple queries, such as summing up all orders between two dates, or summing up all orders in a certain industry; for those, SUMIFS and SUMPRODUCT are fine.

The Most Common Functions
-------------------------

The most common Database function is DSUM, which looks at all the rows in a table and sums up a specific field (column) in each matching row:

\=DSUM(Database, Field, Criteria)

The **Database** part is the **range of cell references**, which must contain the field names in the header. This range should ideally be a Data Table, but it can be any range of cells in the spreadsheet.

The **Field** part is the **column or field you want to add up or count**. You can use a column number or the exact name in text; it’s best to create a direct link to the title in the table header to avoid errors.

The **Criteria** part is the smaller range we created above: Summary!$J$6:$P$8.

It must include at least one field name that’s in the Database AND at least one other condition to be evaluated. If it does not, DSUM will sum up everything in the table.

Each function mentioned above – DSUM, DCOUNT, DCOUNTA, and DGET – accepts these same inputs: Database, Field, and Criteria.

All the normal operators, such as <, >, <=, >=, <>, =, \*, and ?, still work in the Criteria range of cells, but only if they make logical sense for the underlying data.

**The biggest problem with Database functions is that it’s extremely easy to make a small mistake that results in the entire function not working.**

For example:

![Incorrect Database Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20934%20325'%3E%3C/svg%3E "Incorrect Database Function")

Why did these functions suddenly stop working? Because we hard-coded the “Region” field in the header and added an extra space at the end:

![Incorrect Database Function - Problem Highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20905%20321'%3E%3C/svg%3E "Incorrect Database Function - Problem Highlighted")

This problem shows you why it’s best to link directly to the field names in the Order Table here.

Besides this issue, another drawback of database functions is that it’s not easy to see **trends and patterns** when you use them.

For example, how have sales to Energy companies changed over 5-10 years? What percentage of total sales did they represent each year, and which sales reps were most responsible?

For those types of tasks, you are better off using pivot tables and related functionality, such as Power Pivot, which we cover in our [Excel & Fundamentals course](https://breakingintowallstreet.com/excel-financial-modeling-fundamentals/)
.

**Excel Database Functions Multiple Criteria**
----------------------------------------------

If you want to set up a function with multiple criteria, remember the rules above: individual fields in a row are joined together with an AND, and individual rows are joined together with an OR.

Therefore, the following function:

![Excel Database Functions Multiple Criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20291'%3E%3C/svg%3E "Excel Database Functions Multiple Criteria")

Will do the following:

1) First, it will find and add all Order Amounts in the Industrials industry AND in the Midwest AND placed between January 1, 2021 and December 31, 2024 (inclusive).

2) Then, it will find and add all Order Amounts in the Industrials industry AND in the Northeast AND placed between January 1, 2021 and December 31, 2024 (inclusive).

3) Next, it will find and add all Order Amounts in the Energy industry AND in the Midwest AND placed between January 1, 2021 and December 31, 2024 (inclusive).

4) Finally, it will find and add all Order Amounts in the Energy industry AND in the Northeast AND placed between January 1, 2021 and December 31, 2024 (inclusive).

Since each row is joined with an OR, the function will then add up all these Order Amounts.

When you enter multiple rows of criteria, you always get results that match _any_ of the rows.

Database functions have their uses, but we tend to use them less than [sensitivity analysis](https://breakingintowallstreet.com/kb/excel/sensitivity-analysis-excel/)
 in financial models and less than pivot tables in data analysis.

Want to apply these skills? [Learn more about 3 statement models](https://mergersandinquisitions.com/3-statement-model/)
 here.

[Sign Up To BIWS Excel & VBA for Investment Banking](https://breakingintowallstreet.com/excel-vba/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-04-05-Database-Functions.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Database Functions - Before (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-04-05-Database-Functions-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Database Functions - After (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/XL-04-05-Database-Functions-After.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Excel & VBA](https://breakingintowallstreet.com/excel-vba/)

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[Learn More](https://breakingintowallstreet.com/excel-vba/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[BIWS Premium](https://breakingintowallstreet.com/biws-premium/)
: Get the Excel & VBA, Core Financial Modeling, and PowerPoint Pro courses together and learn everything from Excel shortcuts up through financial modeling, valuation, M&A and LBO deals, and the key PowerPoint shortcuts and commands. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/biws-premium/)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&mini=true)
[Email](mailto:?subject=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)

#### Master Excel for Investment Banking

Learn Excel shortcuts, formatting, formulas, graphs, and data analysis, and then automate your workflow with VBA.

[LEARN MORE](https://breakingintowallstreet.com/excel-vba/)

[](https://x.com/intent/tweet?text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[](https://www.linkedin.com/shareArticle?title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&mini=true)
[](mailto:?subject=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-database-functions/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[](https://api.whatsapp.com/send?text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-database-functions/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-database-functions/)
[Copy](https://breakingintowallstreet.com/kb/excel/excel-database-functions/#)
[Email](mailto:?subject=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-database-functions/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-database-functions/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&t=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-database-functions/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/excel/excel-database-functions/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/04221358/excel-database-functions.jpg&description=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[Print](https://breakingintowallstreet.com/kb/excel/excel-database-functions/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[SMS](sms:?&body=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[X](https://x.com/intent/tweet?text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fexcel%2Fexcel-database-functions%2F&title=Excel%20Database%20Functions%3A%20How%20to%20Use%20Them%20%5BTutorial%20Video%5D%20%2821%3A22%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/04221358/excel-database-functions.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand