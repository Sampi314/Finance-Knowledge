# Excel Tips, Tricks, Cheats & Hacks - Microsoft MVP Edition » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

Excel Tips, Tricks, Cheats & Hacks – Microsoft MVP Edition
==========================================================

*   Last updated on May 1, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

I was recently asked, What is my most recommended Excel Tip?

My quick response was to regularly press **Ctrl+S**, Yes simply Save.

I have been caught out a number of times developing large excel systems where I haven’t saved data and after 2 or 3 hours of work I have lost that work when Excel or the Computer has crashed etc.

Close behind **Ctrl+S** is setting up the printer and page size as early in a project as you can.

But this got me thinking what would other Microsoft MVP’s Excel suggestions be ?

So I shot off an email to all the other Microsoft Excel MVP’s asking for their favorite Excel Tip, Trick, Cheat, VBA Code, Excel Formula or Function, Algorithm or Hack.

This post will now present these in the order they were received.

001\. Assign Sequential Numbers – Bob Umlas
-------------------------------------------

There are many ways to assign successive numbers using VBA, but I believe this one is the quickest.

If I know I have a range, referenced by the object variable Rg, for example, I could assign successive numbers parallel to that range by this statement:  
Rg.Offset(, 1).Value = \[row(1:10000)\]  
If Rg is 10 rows long, this will assign the values 1-10 (not 1-10000).

[![001 Sequential Numbers](https://chandoo.org/wp/wp-content/uploads/2016/04/001-Sequential-Numbers.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/001.-Assign-Sequential-Numbers.txt)

Tip contributed by: **Bob Umlas**  
Website: [This isn’t Excel it’s Magic!](http://tinyurl.com/j39o6vy)

002\. Format This Object – Jon Peltier
--------------------------------------

With any object selected, be it a Cell, Range, Worksheet, Chart, Chart Component, Text Box or other shape, Hyper Link, anything, Select the Object and press **Ctrl+1**. The Format Properties Dialog will be shown.

Tip contributed by: **Jon Peltier**

Website: [http://peltiertech.com](http://peltiertech.com/)

003\. Stop Cell Change by Color – Rick Rothstein
------------------------------------------------

Rick has provided a piece of VBA Code that stops a user entering data into a Yellow colored cell.

It is event code, so all of it should be placed in a sheet module (right click the sheet’s name tab, select “View Code” and copy/paste it into the code window that opens up… remember to save the sheet as an “Excel Macro-Enabled Workbook” if using XL2007 or above).

What the code does is, without having to protect the sheet, prevent a user from selecting any cell that has been manually colored yellow (you can, of course, change the color as desired). If the user attempts to select such a cell, the previously active cell will become re-selected. While the code works with yellow-filled cells, the If condition can be changed to test for any cell property (for example, bold text) or set of cell properties (red, underlined text) and it will work just as well.

Here is the code…

[![003. Stop Cell Change by Color_Code_2](https://chandoo.org/wp/wp-content/uploads/2016/04/003.-Stop-Cell-Change-by-Color_Code_2.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/003.-Stop-Cell-Change-by-Color_Code_2.png)

Tip contributed by: **Rick Rothstein**  
Website: [http://www.excelfox.com/forum/f22/](http://www.excelfox.com/forum/f22/)

004\. Double Click Copy – Bill Jelen
------------------------------------

Double click the fill handle to quickly copy a formula to the bottom of the adjacent data set.

[![004 Douible click](https://chandoo.org/wp/wp-content/uploads/2016/04/004-Douible-click.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/004-Douible-click.png)

This is the Mouse Version of **Copy Down** as presented in Point 013 below.

Tip contributed by: **Bill Jelen**  
Website: [MrExcel.com](http://www.mrexcel.com/)

005\. VBA Code Check – Felipe Costa Gualberto
---------------------------------------------

It is widely known that you should use Option Explicit in the declaration section of all components, and I agree with that.

The tip I give needs Option Explicit in the declaration section:

You should often compile your project. Use the **Alt+D** and press **Enter** to ensure your code is correct and you’ll have no surprises while running your macro. **A VBA project that doesn’t compile is a bad project**.

When you request to compile the code, VBE passes through all your code, checking if there aren’t undeclared variables, missing references, bad syntax, etc.

I’m heavily addicted compiling my code and I do it **every minute** when developing an Excel Application.

Take advantage the fact that compiling speed in VBA is blazing fast!

Tip contributed by: **Felipe Costa Gualberto**  
Website: [http://www.ambienteoffice.com.br](http://www.ambienteoffice.com.br/)

006\. Name Manager – Henk Vlootman
----------------------------------

For me the Name box and the Name manager prove to be of priceless value.

Since I only work with ranges. I use the Name functionality as the place where I control my ranges.

If I have a complex model I can use the name box to down-drill my output by my formulas until I arrive at the input. Without this functionality maintaining Excel models proofs to be very difficult.

Tip contributed by: **Henk Vlootman**  
Website: [Vlootman.nl](http://www.vlootman.nl/ "See my website")

007\. Show Pivot tables in Classical Form – Mynda Treacy
--------------------------------------------------------

If you find yourself regularly editing the PivotTable options to get the Classic PivotTable Layout back, you know the useful layout where the row labels aren’t nested, then you might like to add the ‘**Show in Tabular Form’** icon to your Quick Access Toolbar.

To do this Right Click on the Quick Access Toolbar and select Customize Quick Access Toolbar  

[![007 Show in Tabular Form](https://chandoo.org/wp/wp-content/uploads/2016/04/007-Show-in-Tabular-Form.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/007-Show-in-Tabular-Form.png)

The Show in Tabular Form Icon in the QAT

[![007 Show in Tabular Form-2](https://chandoo.org/wp/wp-content/uploads/2016/04/007-Show-in-Tabular-Form-2.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/007-Show-in-Tabular-Form-2.png)

And while you’re there you’ll probably want to add the ‘Do Not Show Subtotals’ icon too

Tip contributed by: **Mynda Treacy**  
Web site: [http://www.myonlinetraininghub.com/blog](http://www.myonlinetraininghub.com/blog)

008\. Easily add a Table of Contents to a File – Jan Karel Pieterse
-------------------------------------------------------------------

The lowest level of documentation I add to a spreadsheet model is a table of content.

With many sheets in a workbook, this can be a tedious chore however. Lets have some tips around this.

**1\. Getting the list of sheets.**  
– Open the VBA editor (alt+F11):  
– open the immediate pane (control+g or View, Immediate pane)  
– Paste this line of code and hit enter:

For Each s in Worksheets: Debug.Print s.Name: Next

– Hold down the shift key and press arrow up until you’ve selected all sheetnames:  
– control+c  
– Go to your Excel TOC worksheet and press control+v:

**2\. Create hyperlinks to the worksheets**

Enter this formula in cell B2:  
\=HYPERLINK(“#'”&A2&”‘!A1”,A2)  
Note the hash, it ensures the link actually works! The single quote is there in case your worksheet  
name has special characters like spaces.  
– Drag the formula down (double-click the fill handle)  
– Format the linked cells (hit control+1) like so:  
o A fat black line along the right-hand side and the bottom:  
o An equally fat grey line along the left-hand side and the top:  
o A darker grey fill:  
o Change the Font to black, increase the font size, make it Bold and white and remove the underline:  
o Which makes your links look like this:

I have created a small utility that automates the process of updating the table of content: [Download Link](http://jkp-ads.com/download.asp#sheettools)

Tip contributed by: **Jan Karel Pieterse**  
Website: [http://www.jkp-ads.com/](http://www.jkp-ads.com/)

009\. Jump to the last cell of a contiguous range – Mike Alexander
------------------------------------------------------------------

Did you know you can quickly jump to the last cell in a column or a row with a simple double-click of the mouse?

**Columns:**

[![cap1](https://chandoo.org/wp/wp-content/uploads/2016/04/cap1.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/cap1.png)

**Rows:**

[![Cap2](https://chandoo.org/wp/wp-content/uploads/2016/04/Cap2.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Cap2.png)

**Caution:** Be careful of blank cells. If you have a blank cell in the column or row, the cursor will jump to the last cell before the blank cell.

_“There are two types of Excel users – Keyboard people and Mouse people._ 

_I’m a mouse person.  I hate taking my hand off the mouse.  If there is away I can doe something with the mouse, I’ll find it._

_That why I love this tip so much._ 

_Hot Keys are for nerds.”_

_Mike Alexander  
_

Tip contributed by: **Mike Alexander**  
Website: [http://www.datapigtechnologies.com/](http://www.datapigtechnologies.com/)

010\. Jump to a Filter’s search box – Jon Acampora
--------------------------------------------------

**Alt+Down Arrow, E** will jump the mouse cursor to the search box in the filter drop-down menus.

[![index](https://chandoo.org/wp/wp-content/uploads/2016/04/index.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/index.png)

Tip contributed by: **Jon Acampora**

Website: [excelcampus.com](http://www.excelcampus.com/)

011\. Use Ctrl+Enter – Tom Ogilvy
---------------------------------

My favorite tip is to use **Ctrl+Enter** rather than Enter to fill any selection of contiguous or non-contiguous cells with whatever is in the active cell of the selection.

This can be a formula such as to generate random data to using in testing.

For example if I need integer data in  C2:C10; E2:G10 then I select that range, go to the formula bar and enter  \=Trunc(rand()\*100+1)  and complete with **Ctrl+Enter**. If I want to fix those numbers, I can then select the rectangular area doing a copy and then Paste Values.

A second tip using this technique is to build a pivot table to produce a subset of my data. Then do a copy and paste values to leave the values and removed the pivot table.  Select the area of row fields which will have many blank values. Do F5 (goto) and choose special, then blanks. This will select all the blank fields that need to be filled in.  Look at the active cell of the selection. Say it is B4. We can see that we want to fill each blank with the next value directly above it.  Go to the formula bar and type in =B3 which refers to the non-blank cell above B4, then use **Ctrl+Enter**. Your data base is completed but we need to remove the formulas.  Select all the row field area; do copy and then paste values to remove the formulas and replace them with the values they produce.

Tip contributed by: **Tom Ogilvy**  
Website: [http://www.allexperts.com/ep/1059-2697/Excel/Tom-Ogilvy.htm](http://www.allexperts.com/ep/1059-2697/Excel/Tom-Ogilvy.htm)

012\. Keep Dummy Data nearby – Oz du Soleil
-------------------------------------------

Because my work involves testing and building examples, I use lots of random data.

1.  In Dropbox, I keep a pinned workbook called “Random Names and Cities”

Having it pinned and stored in Dropbox allows me to access that file wherever I’m at.

[![pinned items](https://chandoo.org/wp/wp-content/uploads/2016/04/pinned-items.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/pinned-items.png)

2.  The workbook has thousands of bits of data including cocktail names, colors, fish names, professional designations, cities, etc.

One sheet has a name-randomizing section where I can hit F9 and get more names.

Thus, if I need a few rows of random data, or thousands, I can create them myself.

[![pinned names workbook](https://chandoo.org/wp/wp-content/uploads/2016/04/pinned-names-workbook.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/pinned-names-workbook.png)

Tip contributed by: **Oz du Soleil  
**Website: [DataScopic.net](http://datascopic.net/)

013\. Copy Down / Copy Right – Zack Barresse
--------------------------------------------

You can Copy Down or Copy Right using CTRL+D, CTRL+R (Fill Down, Right)

**Copy Down**

[![014 Ctrl+D](https://chandoo.org/wp/wp-content/uploads/2016/04/014-CtrlD.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/014-CtrlD.png)

**Copy Right**

[![014 Ctrl+R](https://chandoo.org/wp/wp-content/uploads/2016/04/014-CtrlR.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/014-CtrlR.png)

This is the Keyboard Version of **Double Click Copy** as presented in Point 004 above.

Tip contributed by: **Zack Barresse  
**Website: [http://exceltables.com/](http://exceltables.com/)

014\. Learn to use Google Search – Ian Huitson
----------------------------------------------

I have answered nearly 10,000 posts at the [http://forum.chandoo.org/](http://forum.chandoo.org/)
 and one thing I have found is that it is very rare to get asked questions that haven’t been answered before, very rare.

Learn to use Google Search and some common websites like [http://chandoo.org/wp/](http://chandoo.org/wp/)
 and the other websites shown by the authors above. These websites all have search boxes which search the local website.

These websites have a wealth of Excel history, with worked and solved examples in posts and forums

Sometime the example might be of a mine feasibility study where you are after data on DNA Sequencing, but the solution to the data manipulation maybe very similar, so learn to think laterally about your problem and you’ll be amazed at the solutions that can be found

Tip contributed by: **Ian Huitson “Hui”  
**Website: [http://chandoo.org/wp/about-hui/](http://chandoo.org/wp/about-hui/)

015\. Trim with any delimiter – Rick Rothstein
----------------------------------------------

Excel’s TRIM function is neat in that it collapses all multiple internal contiguous space characters down to a single space…

Did you ever wish there was a simple way to do that for any delimiter other than a space?

Here is a function that will do it for you…

[![Delim2](https://chandoo.org/wp/wp-content/uploads/2016/04/Delim2.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Delim2.txt)

This function must be saved in a Code Module, not a Worksheet Module

The first argument is the text you want to parse. The second argument is the delimiter (which can be one or more characters long). The third argument, which is optional, let’s you specify whether you want to keep or delete any leading or trailing delimiters which may end up in the result (Excel’s TRIM function automatically deletes leading and trailing spaces, but I decided to let it be an option). The default is False which means leading and trailing delimiters will be deleted. So, let’s say you had a concatenation function of some sort which produced the following output…

If in Cell A1 you had: one, , , two, three, , , , , , , four, , ,\_

Note there is a trailing space at the end of the above text string. Passing this text into the Reduce function, and specifying “, ” (comma space) as the delimiter, would result in the following text being returned from the function…

Using the function: =Reduce(A1, “, ” ) or \=Reduce(A1, “, “, False )

Excel will return: one, two, three, four

**Note:** For those of you who may be wondering about those numbers in the Array function call, here is a link to the thread where they originally came from…

[https://groups.google.com/ forum/#!topic/microsoft. public.vb.general.discussion/ TqZHK9cPnpU](https://groups.google.com/%20forum/#!topic/microsoft.%20public.vb.general.discussion/%20TqZHK9cPnpU)

Tip contributed by: **Rick Rothstein**  
Website: [http://www.excelfox.com/forum/f22/](http://www.excelfox.com/forum/f22/)

016\. The Bad Find Example – Stephen Gersuk
-------------------------------------------

Dating back to as early as 2002, VBA Help has contained an awful example of how to use the Find method. It continued until as recently as Excel 2010.

[![Badfind1](https://chandoo.org/wp/wp-content/uploads/2016/04/Badfind1.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Badfind1.png)

On the merely bad side, you should explicitly set LookIn, LookAt, SearchOrder (if you care), and MatchByte arguments in the initial invocation of the Find method, as all persist each time Find is invoked via VBA or Find is invoked from the user interface. (MatchCase and SearchFormat persist from invocation to invocation in the UI, but not in VBA; both default to False).

But this line,

[![Badfind2](https://chandoo.org/wp/wp-content/uploads/2016/04/Badfind2.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Badfind2.png)

… should NEVER be used, because

1.  If c Is Nothing, then c.Address will give a run-time error; and
2.  If c.Address doesn’t error, then c Is Nothing must be False.

You might think that VBA would stop evaluating the expression if “c Is Nothing“, but it doesn’t; VBA always evaluates all arguments to a logical expression.  
What to do instead?

That depends on what else the loop does.

If it causes the values to eventually not be found (e.g., because you are changing the values, or hiding the rows in which they appear), then the c is Nothing test is what you need. If the same values will be found forever (e.g., because you are changing some other cell in the same row where the value is found), then c.Address <> firstAddress is golden.

The one-size-fits-all solution is to just do both:

[![Badfind3](https://chandoo.org/wp/wp-content/uploads/2016/04/Badfind3.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Bad-Find-3.txt)

Tip contributed by: **Stephen Gersuk**  
Website: [http://www.stephensexcel.info/](http://www.stephensexcel.info/)

Closing
-------

Many many thanks to the Microsoft Excel MVPs who contributed above.

I hope you get to to revue all the tips and pass comments and appreciation back to the authors as appropriate.

Next week the Excel Tips, Tricks, Cheats & Hacks theme will continue with the **Excel Tips, Tricks, Cheats & Hacks – Chandoo.org Excel Ninja Edition**, so keep an eye out for that.

If you have any Excel Tips, Tricks, Cheats & Hacks that you would like to share with the community, please leave  a tip in the comments below.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [18 Comments](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/#respond)
    
*   Tagged under [Cheat](https://chandoo.org/wp/tag/cheat/)
    , [Hack](https://chandoo.org/wp/tag/hack/)
    , [hui](https://chandoo.org/wp/tag/hui/)
    , [Huis](https://chandoo.org/wp/tag/huis/)
    , [keyboard shortcuts](https://chandoo.org/wp/tag/keyboard-shortcuts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [mouse shortcuts](https://chandoo.org/wp/tag/mouse-shortcuts/)
    , [Tip](https://chandoo.org/wp/tag/tip/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

[PrevPreviousFigure out slot from given time \[quick tip\]](https://chandoo.org/wp/excel-time-slot-formula/)

[NextSumerian Voter Problem \[IF formula homework\]Next](https://chandoo.org/wp/sumerian-voter-problem/)

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
    
    [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ