# Excel Tips, Tricks, Cheats & Hacks - Excel Ninja Edition » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-excel-ninja-edition

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

Excel Tips, Tricks, Cheats & Hacks – Excel Ninja Edition
========================================================

*   Last updated on April 30, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Last week we saw a number of Excel Tips, Tricks, Cheats & Hacks supplied by Microsoft Excel MVP’s.

This week I have invited the Chandoo.org, Excel ninjas to contribute their Excel Tips, Tricks, Cheats & Hacks.

Chandoo has Excel ninjas?  
Absolutely!

Do they have swords?  
No (sigh)

But you can read all about them here: [Chandoo.org Excel ninjas](http://chandoo.org/forum/threads/chandoo-org-ninjas.10830/)

The Chandoo.org Excel ninjas have solved in excess of 63,000 Excel questions in the 7 years that Chandoo.org Forums have been active. Hence they are imminently qualified in all areas Excel and as such the tips and tricks they will share will be essential reading.

Lets go:

001\. Find & Replace Hack No.1 – Shrivallabha
---------------------------------------------

You can use CTRL+J to simulate the Enter character in “**Find and Replace**” or “**Text to Columns**” fields.

**Example:**  
Download the sample file here: [Download sample file](https://chandoo.org/wp/wp-content/uploads/2016/04/CtrlJ.xlsx)
  
Cells B2:B4 contain text with multiple lines per cell  
There is an invisible Enter Character in those cells that can be added via use of Ctrl+J or Alt+Enter as the data is entered

To seperate each line please follow these instructions  
Select B2:B4

[![Nin001a](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001a.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001a.png)
  
Goto the Data, Text to Columns tab

Select Delimited

[![Nin001b](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001b.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001b.png)

Select Other and Type Ctrl+J in the adjacent box

Next

[![Nin001c](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001c.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001c.png)

Change the Destination to D2

[![Nin001d](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001d.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001d.png)
  
Finish

Enjoy

[![Nin001e](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001e.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Nin001e.png)

Contribution by: **[Shrivallabha](http://forum.chandoo.org/members/shrivallabha.2442/)
**

002\. Find & Replace Hack No.2 – Shrivallabha
---------------------------------------------

Using escape character ~(tilde) while replacing \*(asterisk) from text in the **Find and Replace** box.  
If someone does Find and Replace \* directly then everything gets replaced as \* acts as wildcard.

So you have to use ~\* for replacing an asterisk \* character in a string.

Contribution by: **[Shrivallabha](http://forum.chandoo.org/members/shrivallabha.2442/)
**

003\. Select All – Shrivallabha
-------------------------------

You can use the **Select All** Shortcut Ctrl + A to select all items listed below

*   Items in a List
*   Contiguous Cells in a Range
*   All cells in a worksheet, press Ctrl + A twice
*   All shapes, Select first shape, then press Ctrl + A

Contribution by: **[Shrivallabha](http://forum.chandoo.org/members/shrivallabha.2442/)
**

004\. Apply a filter to the first row of a range – Shrivallabha
---------------------------------------------------------------

Apply a filter to the first row of a range

Select any cell in a range

ALT D + F + F (Applies filter to first row of the cells contiguous with the current cell)

Contribution by: **[Shrivallabha](http://forum.chandoo.org/members/shrivallabha.2442/)
**

005\. Fill Blank cells with the value in the cell above – Asheesh
-----------------------------------------------------------------

1.  Select the range that contains blank cells you need to fill.
2.  Click **Home** > **Find & Select** > **Go To Special…**, and a **Go To Special** dialog box will appear, then check **Blanks** option.
3.  Click **OK**, and all of the blank cells have been selected.
4.  Assume that the Top Left Blank cell is A3, then input the formula _\=A2_  into active cell A3 without changing the selection.
5.  Press Ctrl + Enter, Excel will copy the respective formula to all blank cells.
6.  At this point, the filled contents are formulas, and we need to convert the formals to values.
7.  Select the whole range, copy it Ctrl + C, and then press Ctrl + Alt + V to active the **Paste Special**… dialog box. Then select **Values** option from **Paste**, and select **None** option from **Operation**.

Contribution by: **[Asheesh](http://forum.chandoo.org/members/asheesh.16065/)
**

006\. Multiple Consolidation Ranges to Pivot table – Asheesh
------------------------------------------------------------

You can use “Multiple Consolidation Ranges” of Pivot Table to generate a unique list from Multiple Sources.

Goto the worksheet where your data lists are

To achieve this you need to add the Pivot Chart Wizard to either the QAT or Tab Bar

Start the Pivot Table Wizard or use the Keyboard Shortcut ALT + D P

Select **Multiple Consolidation Ranges** then click **Next**

[![asheesh001](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh001.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh001.png)

Select **Create a single page field for me** and **Next**

[![asheesh002](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh002.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh002.png)

Select your **data range**, including a blank leading column and then click **Add** button.

[![asheesh003](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh003.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh003.png)

**Notice:** As per the excel file A1:A7 is blank.The Data is in Columns B:D.

Had this not been the case then we needed to insert a new blank column at the left of the data and that is Column A in this example

Click on **Finish** button

You will have a table like the one in the below image in a new worksheet.

[![asheesh004](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh004.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh004.png)

Now go the **Pivot Table Field options** and do the following

[![asheesh005](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh005.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh005.png)

You should have a unique list of values

[![asheesh006](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh006.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/asheesh006.png)

You can **Right Click** on the Grand Total and **DeSelect** Grand Total to remove the Grand Total if required

You can now use this list in a Named Formula, Data Validation, Chart or other use where the required Unique List is required.

**Note:** If the Source Data changes you will need to **Right Click** on the List and select **Refresh Data**

Refer to the attached file: [**Download Sample File**](https://chandoo.org/wp/wp-content/uploads/2016/04/Asheesh-Multiple-Consolidation-Ranges.xlsx)

Hui, in his second post at Chandoo.org, actually wrote about this technique in Feb 2010 but using a Single List – [Read it here](http://chandoo.org/wp/2010/02/02/data-validation-using-an-unsorted-column-with-duplicate-entries-as-a-source-list/)

Contribution by: **[Asheesh](http://forum.chandoo.org/members/asheesh.16065/)
**

007\. Hiding Rows that are blank – Faseeh
-----------------------------------------

Hiding Rows that are blank.

I have a sheet on daily basis in which certain cells in a column are blank I want to hide the rows with those blank cells.

What I do is…

1.  Select the cell range (the column).
2.  Press F5, you will get the Go To Menu.
3.  Check the option Blank.
4.  Press Ctrl+9 to hide the selected range.

Contribution by: **Faseeh**

008\. Hiding Rows that are blank – Faseeh
-----------------------------------------

To use the subtotal function to get the serial number right is the one that my accounts department loves. They were tired of creating commercial invoices with serial number created by dragging manually.  
Here is the procedure.

Serial Number list that do not change with Filter  
Assume you want to enter serial in column A and your data is present in column B. The formula look like this: \=SUBTOTAL(3,$B$4:B4)  
Drag downward. (This is only one time drag). Now if you filter the list the serial number will be changed accordingly.

Contribution by: **Faseeh**

009\. Slab Rate Formula – Faseeh
--------------------------------

This is a formula for slab rate that gives total price for a quantity with given slab rate.

[![Slab002](https://chandoo.org/wp/wp-content/uploads/2016/04/Slab002.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Tiered-Pricing2.xlsx)

So we want the price for 2,000 items

The first 1,000 will cost 0.35, the second 1,000 will cost 0.33

The total cost is found by \=SUMPRODUCT((E3>=A3:A5)\*(E3-A3:A5)\*(B3:B5-B2:B4))

Download a sample file here: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2016/04/Tiered-Pricing2.xlsx)

Contribution by: **Faseeh**

010\. Navigation tricks to get around spreadsheet faster – Luke M
-----------------------------------------------------------------

Use Ctrl+Arrow key to jump to end of range.  
Use Ctrl+Shift+Arrow key to select all data to end of range

Contribution by: **[Luke M](http://forum.chandoo.org/members/luke-m.662/)
**  
If you’d like to hire Luke for an Excel project, contact him at:  
[LukeMoraga@gmail.com](mailto:LukeMoraga@gmail.com)

011\. Select Visible Cells in a Filtered range – Luke M
-------------------------------------------------------

When dealing with filtered ranges:  
Use Alt+; to select visible cells only

Contribution by: [Luke M](http://forum.chandoo.org/members/luke-m.662/)
  
If you’d like to hire Luke for an Excel project, contact him at:  
[LukeMoraga@gmail.com](mailto:LukeMoraga@gmail.com)

012\. QAT – The Quick Access Toolbar; Shortcuts – Luke M
--------------------------------------------------------

I’ve seen many users who don’t know about, or use the the Quick Access Toolbar (QAT) very well.  
Everyone has a list of things they use often. Put these on the QAT to improve your efficiency.

My favorite thing is that all items on the QAT get auto-assigned shortcuts of Alt+\[1-9\].

On my system, I have Paste Values and Paste Formulas in the 2nd and 3rd slots, so I can easily do those by hitting Alt+2 or Alt+3.

Press Alt +

   1   2   3   4   5   6   7    8    9

[![upload_2016-4-19_10-7-48](https://chandoo.org/wp/wp-content/uploads/2016/04/upload_2016-4-19_10-7-48.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/upload_2016-4-19_10-7-48.png)

Contribution by: **[Luke M](http://forum.chandoo.org/members/luke-m.662/)
**  
If you’d like to hire Luke for an Excel project, contact him at:  
[LukeMoraga@gmail.com](mailto:LukeMoraga@gmail.com)

013\. Keyboard Shortcuts – Marc L
---------------------------------

**Insert Current Date**

Insert current date in a cell : Ctrl + ;

**Insert Current Time**

Insert current time in a cell : Ctrl + :

**Bulk enter values or formula into several cells**

To allocate same Value or Formula to several cells, Select the cells, enter the Value or Formula and

accept into all cells by Ctrl + Enter 

**Date Check also known as Toggle Values/Formula Mode**

Ctrl + ~ (English keyboard) or Ctrl + “ (3 on a French keyboard)

Is a toggle between displaying formulas or values in cells.  
But I use it as a trick to check if dates are real dates and not text :  
When displaying formulas is active, real dates appear as number,  
bad dates remain as text !

This is the reason why I won all by bets against guys who insisted

Contribution by: [**Marc L**](http://forum.chandoo.org/members/marc-l.3465/)

014\. Break Strings into Words – Hui
------------------------------------

A regular requirement in VBA is to be able to extract say the Name and Surnames from a string

Eg: Retrieve “Ian” & “Huitson” from “Ian David Huitson”

[![Hui-Shortcut1](https://chandoo.org/wp/wp-content/uploads/2016/04/Hui-Shortcut1.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Hui-Shortcut1.png)

But what if I want the Middle Name, or what if I have two middle names like my children do?

These functions quickly become very cumbersome

A technique I recently learned  simplifies this, whilst extending it to other delimiters and any number of sub-strings

You can easily parse a delimited string into an array.

You simply use the **Split** function with the appropriate delimiter as parameter.

The following code shows an example of using the Split function.

[![Hui-Shortcut2](https://chandoo.org/wp/wp-content/uploads/2016/04/Hui-Shortcut2.png)](https://chandoo.org/wp/wp-content/uploads/2016/04/Split-Sub-Strings.txt)

The above code makes an array of values of size 3, Arr(0) to arr(2)

arr(0) will contain “Ian”

arr(1) will contain “David”

arr(2) will contain “Huitson”

If you are unsure of the number of array elements you should use the Ubound() function to determine the size

Ubound(arr,1) which will return the reference number of the last element = 2 in the example

in the example of my Name which has 3 elements

arr(2) = arr(Ubound(arr,1)) and each will contain the string “Huitson”

You can download both the above sample from this [sample file](https://chandoo.org/wp/wp-content/uploads/2016/04/Split-Sub-Strings.txt)

I picked this up a few months back from [Excel Mastery](http://excelmacromastery.com/Blog/)
, my new favorite Excel VBA site

Contribution by: [**Hui**](http://chandoo.org/wp/about-hui/)

015\. Use the Camera Tool – BobHC
---------------------------------

You can sue the Camera Tool to setup dashboards that quickly combine data from a number of worksheets into a common location

Read about its use: [http://chandoo.org/wp/2008/12/02/excel-camera-tool-help/](http://chandoo.org/wp/2008/12/02/excel-camera-tool-help/)

And for fancy applications: [http://www.addictivetips.com/microsoft-office/camera-tool-function-in-excel-2010/](http://www.addictivetips.com/microsoft-office/camera-tool-function-in-excel-2010/)

Contribution by: [BobHC](http://forum.chandoo.org/members/bobhc.1896/)

Closing
-------

Many many thanks to the Chandoo.org ninjas who contributed above.

I hope you get to to revue all the tips and pass comments and appreciation back to the authors as appropriate.

Next week I have to do some ~real~ paid work and will travelling in Timor, Indonesia, but in two weeks time the Excel Tips, Tricks, Cheats & Hacks theme will continue with the **Excel Tips, Tricks, Cheats & Hacks – Notable Excel Sites (non-MVP) Edition**, so keep an eye out for that.

If you have any Excel Tips, Tricks, Cheats & Hacks that you would like to share with the community, please leave  a tip in the comments below.

All the user contributions will be combined into one final post: **Excel Tips, Tricks, Cheats & Hacks – Users Edition**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [20 Comments](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-excel-ninja-edition/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-excel-ninja-edition/#respond)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

[PrevPreviousEarth Venus cosmic dance – Animated chart in Excel](https://chandoo.org/wp/earth-venus-cosmic-dance-animated-chart-in-excel/)

[NextExcel Tips, Tricks, Cheats & Hacks – Notable Excel Websites (Non-MVP) EditionNext](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-notable-excel-websites-non-mvp-edition/)

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
    
    [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-excel-ninja-edition/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-excel-ninja-edition/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-excel-ninja-edition/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ