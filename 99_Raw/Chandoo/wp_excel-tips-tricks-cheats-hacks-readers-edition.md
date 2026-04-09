# Excel Tips, Tricks, Cheats & Hacks – Readers Edition » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

Excel Tips, Tricks, Cheats & Hacks – Readers Edition
====================================================

*   Last updated on May 26, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Over the last month we have seen some 52, Excel Tips, Tricks, Cheats & Hacks presented by some of the best Excel practitioners on the net:

[Excel Tips, Tricks, Cheats & Hacks – Microsoft MVP Edition](http://chandoo.org/wp/2016/04/21/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/)

[Excel Tips, Tricks, Cheats & Hacks – Chandoo.org Excel Ninja Edition](http://chandoo.org/wp/2016/04/28/excel-tips-tricks-cheats-hacks-excel-ninja-edition/)

[Excel Tips, Tricks, Cheats & Hacks – Notable Excel Sites Edition](http://chandoo.org/wp/2016/05/05/excel-tips-tricks-cheats-hacks-notable-excel-websites-non-mvp-edition/)

[Excel Tips, Tricks, Cheats & Hacks – Readers Prequil](http://chandoo.org/wp/2016/05/12/excel-tips-tricks-cheats-hacks-readers-edition-prequil/)

In this final post I am presenting a compilation of Readers Contributions.

These have been compiled from comments on the above 4 posts and submissions sent directly to me.

I hope you enjoy the following Excel Tips, Tricks, Cheats & Hacks – Readers Edition

### 001\. Toggle the Absolute/Relative $ Sign in Formulas using F4 – Desk Lamp

Instead of typing $AA$12 simply type AA12 then press F4.

Press **F4** to Toggles through the sequence: AA12 -> $AA$12 -> AA$12 -> $AA12 \-> AA12

[![Abs Rel Address](https://chandoo.org/wp/wp-content/uploads/2016/05/Abs-Rel-Address.gif)](https://chandoo.org/wp/wp-content/uploads/2016/05/Abs-Rel-Address.gif)

You can [read about Absolute vs Relative Cell References here](http://chandoo.org/wp/2008/11/04/relative-absolute-references-in-formulas/)

### 002\. Current Region – Peter Carr

My favorite tip is the **CurrentRegion** of a range.

**CurrentRegion** is the contiguous range of cells starting from a cell, and moving out in all directions until an entire blank row or column is reached.

[![EHRO08](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO08.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO08.png)

The current Region of the Yellow Cell above is the Red Outlined Area

**Keyboard**  
From the keyboard you can do this by pressing Ctrl+\* or Ctrl+A, which is a shortcut for **GoTo**, **Special**, **Current Region**.

**VBA**

In VBA you can use the Range.CurrentRegion property

If there is a block of data in B4:F10 with blank rows & columns around it

Dim myRange  as Range

myRange = Range(“C8”).CurrentRegion

will set myRange to $B$4:$F$10

To identify the number of rows in a contiguous region.  
e.g. intNumberOfRows = Range(“FirstCell”).CurrentRegion.Rows.Count

### 003\. Select the Current Region using the QAT – Christine

In addition to the techniques described by Peter above, you can select the Current Region by adding an Icon to the Quick Access Toolbar.

[![EHRO06](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO06.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO06.png)

Click on any cell and then click on the icon or use Alt+4

### 004\. Find the Alt-Shortcut Key Number for the QAT – Hui

In the “Select the Current Region using the QAT” post above, Christine showed us how to use the Current Region Icon [![CurrentRegionIcon](https://chandoo.org/wp/wp-content/uploads/2016/05/CurrentRegionIcon.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CurrentRegionIcon.png)  to quickly select the current Region. But how do we know it is the 4th Icon?

The Alt Number is Position dependent, in the example above the Current Region Icon is the 4th Icon from the Left in the QAT and so it is accessed by Alt+4  

But by simply pressing the Alt key, Excel will show you the shortcut numbers for the QAT and all other Tabs

[![Alt_Keyboard Shortcuts](https://chandoo.org/wp/wp-content/uploads/2016/05/Alt_Keyboard-Shortcuts.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/Alt_Keyboard-Shortcuts.png)

So we can see that the Select the Current Region icons is yes, No **4** and so Alt+4 is required to activate it

We can also see that the Record a Macro icon is number **08**. To use that You use Alt+08 (Using the Number keys, not the numeric keypad)

Using Alt also shows you all the Tab shortcuts as well

### 005\. Stay on the Current Cell after you press Enter – MF

Typically when entering data as you press the Enter key, Excel advances the current cell to the next cell as defined in the **File**, **Options**, **Advanced**, **Editing Options** menu

To stay on the current cell Simply press Ctrl+Enter instead of Enter

You can set your default move direction or disable Move Selection permanently by changing the option in the **File**, **Options**, **Advanced**, **Editing Options** menu:

[![EHRO01](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO01.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO01.png)

### 006\. Close a File Shortcut – Johnathan Cooper

Simply pressing Ctrl+W closes the current file

If the file has changed since the last save you are given the option to Save the file before it closes

### 007\. Keyboard Shortcuts – Chirayu

Hide columns – CTRL + 0  
Apply Filter (alternative) – SHIFT + CTRL + L  
Clear Filter – ALT + D + F + S  
Drag Down – CTRL + D  
Drag Right – CTRL + R  
Drag Up – ALT + E + I + U  
Drag Left – ALT + E + I + L  
Value Paste – ALT + E + S + V  
Format Paste – ALT + E + S + T

You can find a comprehensive list of Keyboard Shortcuts at: [Chandoo.org Keyboard Shortcuts](http://chandoo.org/wp/2010/02/22/complete-list-of-excel-shortcuts/)

### 008\. Use AutoCorrect to write formula – Wynn Hopkins

My favorite trick is using AutoCorrect to help write INDEX MATCH formulas..

Copy the following line into AutoCorrect and then use iii as the text to replace

\=INDEX( DblClk\_to\_Select\_Column\_to\_return, MATCH( DblClk\_Single\_Lookup\_Cell, DblClk\_Lookup\_Column, 0),0)

This way whenever you need INDEX MATCH you just type iii and AutoCorrect kicks in and you are 3 double clicks away from a robust formula.

AutoCorrect is found in the **File**, **Options**, **Proofing** Menu

[![EHRO02](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO02.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO02.png)

Contributor: [Wyn Hopkins](https://www.linkedin.com/pulse/stop-using-vlookup-wyn-hopkins)

### 009\. Fill Blanks in a Data Table before use in a Pivot Table – RobD

When building pivot tables, it helps to have a full column of like values, so if you have a set up such as:

Where the data area has blank cell

[![EHRO03a](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO03a.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO03a.png)

Use this handy VBA

[![EHRO03b](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO03b.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO03.txt)

‘Change the MyCol value to match your value

Becomes…

[![EHRO03c](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO03c.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO03c.png)

**Note**: The code copies the text above the blank cell, and so the user must be careful that this is a valid assumption

### 010\. Fill Blanks in a Data Table before use in a Pivot Table II – Jomili

Extending the technique shown above, Jomili supplied some VBA code that does the same as 007 above, except that it handles Multiple Columns at once as well as allowing Formulas to be converted to Values in the final result

So

[![EHRO04a](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO04a.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO04a.png)

becomes

[![EHRO04b](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO04b.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO04b.png)

by using this code:

[![EHRO04d](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO04d.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO04.txt)

### 011\. QAT Copy/Paste Shortcut – Ian Watkins

By assigning the Copy, Paste Values and Paste Formulas Icons to positions 1, 2 & 3 of the Quick Access Toolbar

Instead of doing a big move of my hand from Ctrl+C to Alt+2, I can just move a finger from Alt+1 t copy

Click on the new cell and press Alt+2 or Alt+3 without moving my hand

[![EHRO05](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO05.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO05.png)

Speeds things up quite a bit!

### 012\. Customize Markers in a Chart – Chandeep

Customizing markers in a chart – [http://www.goodly.co.in/customize-markers-in-a-chart/](http://www.goodly.co.in/customize-markers-in-a-chart/)

### 013\. Charting Hacks to work faster – Chandeep

Charting Hacks to work faster – [http://www.goodly.co.in/5-charting-hacks-to-help-you-work-faster/](http://www.goodly.co.in/5-charting-hacks-to-help-you-work-faster/)

### 014\. Seven Date formulas to make life easy – Chandeep

7 Date formulas to make life easy – [http://www.goodly.co.in/date-formulas-in-excel/](http://www.goodly.co.in/date-formulas-in-excel/)

### 015\. Customised scrollbar using VBA – Chandeep

Customised scrollbar using VBA – [http://www.goodly.co.in/customized-scroll-bar-in-excel/](http://www.goodly.co.in/customized-scroll-bar-in-excel/)

### 016\. Adding Direct Legends – Chandeep

Adding Direct Legends – [http://www.goodly.co.in/how-to-add-direct-legends-to-the-chart/](http://www.goodly.co.in/how-to-add-direct-legends-to-the-chart/)

### 017\. Excel Ninja Menu – Krishna Khemraj

Select a cell or range then move till the 4-way cross appears.

Then **Right-Click and drag** the selection to another place in the worksheet then, like a ninja, a menu full of skills and throwing stars pops up allowing me to do all kinds of awesomeness.

[![EHRO06a](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO06a.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO06a.png)

When you click the fill box on a Date and **Right Click and Drag** it down, a lot of amazing Date options pop up.

[![EHRO06b](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO06b.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO06b.png)

### 018\. Copy & Paste Filtered Data Only – Patricia

If you try to copy subtotaled data (and in earlier Excel versions filtered data), when you paste it all the data displays instead of just the summarized data.  
To get around this, select your summarized data, click on **Find** and **Select** tab and then select **Go to Special**.

Click **Visible cells Only** and click **Ok**.

Now paste and you will see that only the summarized data has been copied.  
You can also go **CTRL+G** and then click the Special icon at the bottom of the dialog box.

### 019\. Clear Filters for the Current Column – Graham

With a table that is filtered, ensure the active cell is in the header of a filtered column and hit **ALT + Down Arrow + C** to clear the filter for the current column

### 020\. Names Formula Tips – Pedro Paulo

You can bring up the Name Manager in Excel by pressing Ctrl+F3.

This lists the names used in your current workbook, and you can also define new names, edit existing ones or delete names from the Name Manager.

You can define several named ranges using data that’s arranged in neat tables. Excel creates named ranges from your selection and uses your data headings as the new names.

Make sure your data has headings (top row, left column, bottom row or right column) as these will turn into the names of your named ranges  
Select the data including headings, press Ctrl+Shift+F3, in the dialog box select where your headings are (top row, left column, bottom row or right column) and click Ok.

Field Names which include spaces will be replaced with underscores

eg: **Account Code** will become the **Account\_Code** named formula

### 021\. Avoid Division by Zero – Ian Wilson

If a formula returns a number value, the Iferror() function can be used to isolate a returned value of zero.

You just need to utilize reciprocals:  
1/(1/x) = x, however, if x = 0, then the function is an error.  
My most common use of this feature is to return a blank instead of a 0.  
\=iferror(1/(1/sum(range)),””)  
This could also be used to avoid division by 0 or replace 0s with a string.

### 022\. Text to Columns Shortcut – Vishal Onkar

When working with lots of Text or CSV Files you invariably end up using the Text to Columns function repeatedly

This can be accessed by the ALT+D+E  keyboard shortcut

### 023\. Convert a Month in Words to a Month Number – Denys calvin

To convert a month in words (i.e., “August”) to its number (i.e., “8”), use, at least, the first three letters of the word in the following formula: \=MONTH(“mmm”&1)

\=Month(“March”&1) returns 3

\=Month(“Mar”&1) returns 3

### 024\. Trace Precedent/Dependents – Prashant99

Trace precedent cells Ctrl+\[  \
Trace dependent cells F5+Enter or Ctrl+\]  

### 025\. Resize Columns – Target

I routinely get sheets with data all smashed up which I hate and I’ve never been able to find a shortcut to do this.

To get around this I use the following VBA and assign a shortcut key (CTRL+Q)

[![EHRO07](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO07.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO07.txt)

It can be a nuisance if I’ve intentionally hidden columns, but the convenience far outweighs the inconvenience

### 026\. Format Table Header Row – Ronnie

I use Tables many times a day and have a simple macro to give me a consistent Table format

[![EHRO09b](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO09b.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO09b.png)

The VBA Code:

[![EHRO09aaa](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO09aaa.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO09aaa.txt)

### 027\. Quickly Jump to Range – Efand

Type the range address directly in the Name Box and then press **Enter** to select it.

e.g: type **A3:A6** will select its ranges without using any clicking and dragging

[![EHRO10a](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO10a.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO10a.png)

If you select a Range say **B3:B6**, then type a Name in the Name Box “**From\_Date**“, Excel sets up a Named Formula referring to that range

[![EHRO10b](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO10b.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO10b.png)

If the Named Formula already exists, eg: From\_Date, Typing **From\_Date** into the box will take you to it.

You can also use the Drop Down next to the Name Box to select existing Named Ranges

[![EHRO10b2](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO10b2.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO10b2.png)

### 028\. Easily delete all Non-Formula cells – Martin

To easily delete all none-formula entries in a worksheet in one go:

Goto **Home, Find & Select, Constants**

This selects all cells that do not contain a formula.

Then just hit the delete button and you are done!

### 029\. Reset all Cell Comments to the Same Style – Hui

To Reset all Cell Comments to the Same Style simply copy this code into a code module in your workbook

Edit the style parameters to suit your need

Run the code with **F5**

[![EHRO11b](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO11b.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/EHRO11b.txt)

Closing
-------

Many many thanks to the [Microsoft Excel MVPs](http://chandoo.org/wp/2016/04/21/excel-tips-tricks-cheats-hacks-microsoft-mvp-edition/)
, [Chandoo.org Ninja’s](http://chandoo.org/wp/2016/04/28/excel-tips-tricks-cheats-hacks-excel-ninja-edition/)
 & [My Favorite Excel Websites](http://chandoo.org/wp/2016/05/05/excel-tips-tricks-cheats-hacks-notable-excel-websites-non-mvp-edition/)
 Authors for the 52 and You for the 29 Excel Tips, Tricks, Cheats & Hacks that have been showcased over these past 5 posts.

I hope you get to to revue all the tips and pass comments and appreciation back to the authors as appropriate.

I will re-run this series in May 2017 so keep a list of your new Excel Tips, Tricks or Hacks handy.

If you have any Excel Tips, Tricks or Hacks, Don’t be afraid to share them below in the comments:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [14 Comments](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition/#respond)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
    

[PrevPreviousSUMPRODUCT – Beginner to Advanced \[Master Class\]](https://chandoo.org/wp/sumproduct-mmc/)

[NextFish Eye Effect for highlighting selection – Is it effective? \[Advanced Charting\]Next](https://chandoo.org/wp/pay-gap-chart/)

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
    
    [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ