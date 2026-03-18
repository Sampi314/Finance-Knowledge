# Use Excel Tables

**Source:** https://www.fullstackmodeller.com/blog/use-excel-tables

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/Excel%20tables.png)

Using Excel Tables to transform the way you model
=================================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Oct 15, 2023 10:28:02 AM

Discover the benefits of using Excel Tables in your models

Microsoft has been busy releasing lots of new and powerful functionality into Excel recently. The rate of change is pretty mind blowing. It's very easy to be distracted and overwhelmed by all this new shiny stuff.

For most modellers however it is much more important to focus on your core skills and ensure that you master them.

In this article I am going to focus on Excel Tables which is remarkably underused despite being part of Excel since 2007.

What are Excel Tables?  

-------------------------

Excel Tables, are a tool for defining your worksheet data as a named object that can be referenced directly by formulae, charts, Pivot Tables and PowerQuery. Excel Tables represent a move away from cell based referencing (ie = A1) towards a more database style of referencing.

Using Excel Tables will transform the way that you model and result in better structured, clearer, less risky models.

To put it simply, Excel Tables are a complete game-changer. If you only have time to learn one new thing in Excel, learn Excel Tables.

Here are my top five reasons for using Excel Tables in your modelling.

1\. Simple, clear and consistent formulae  

--------------------------------------------

In modelling we strive for simple, clear and consistent formulae. This is a common thread among all [Best Practice Standards](https://www.fullstackmodeller.com/blog/an-introduction-to-financial-modelling-standards)
.

Excel Tables use structured reference formulae which refer into the table name and field name rather than a range of cells.

This formula    \=F2 \* J2

becomes this   \=\[@Quantity\] \* \[@Price\]

and this formula   \=SUMIFS(Data!$J$2:$J$5001,Data!$E$2:$E$5001,$B4,Data!$I$2:$I$5001,C$3)

becomes this   \=SUMIFS(tbl\_Data\[Value\],tbl\_Data\[Product\],$B4,tbl\_Data\[Location\],C$3)

Hopefully you agree that the formulae using structured referencing are much simpler and clearer and therefore easier to understand.

Furthermore the formula that you enter into a column in an Excel Table is automatically copied down the whole column. When new data is added at the bottom of an Excel Table the formulae automatically extend. This means that all of the formulae in your table are by default consistent and therefore anyone reviewing your model just needs to review one formula in the whole column.

2\. Remove the need for future proofing your formulae  

--------------------------------------------------------

Ever found yourself future proofing the formulae in your model? Selecting a much wider range than you need, even a whole column? Building formulae down empty rows just in case your data gets bigger?

I certainly used to do it. And I still come across Excel models with this formulae latency built in on a regular basis.

As we have seen above using structured reference formulae over Excel Tables means that we are referencing the table and the field name within the table. This means that if a table grows or shrinks the formulae automatically react to the change.

Excel Tables therefore completely remove the need for this "formula fudging".

3\. A safer source for Pivot Tables
-----------------------------------

When you first create a Pivot Table Excel takes a snap shot of the data and holds it in cache memory, it also holds the range of data that you first selected (eg: A1:G5000).

An issue that users often experience is that when they add new data to their original data, either in rows or columns, the Pivot Table doesn't pick up this new data. Even after a refresh of the cache.

When you base a Pivot Table on an Excel Table this issue is instantly resolved. The Pivot Table references the Excel Table which expands automatically when new data is added. No more time spent editing the Data Source.

4\. Seamless integration with PowerQuery  

-------------------------------------------

PowerQuery loves an Excel Table. Excel Tables are a core source for the Get Data stage and make the handling of data brought through into the Transform stage much more straightforward.

The default Load To option for PowerQuery is to an Excel Table. It's almost like Microsoft want us to use this amazing piece of functionality that no one knows about!

5\. Six other reasons to use Excel Tables  

--------------------------------------------

And finally six other quick wins when using Excel Tables:

*   Sorting and filtering is built in
*   Column headers are always visible (like a freeze pane)
*   Add a total row with a click of the button
*   Remove duplicates with ease
*   You can use slicers on Excel Tables for even easier filtering
*   Excel tables come with a wide range of preset formats to select from 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fuse-excel-tables)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fuse-excel-tables)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fuse-excel-tables)
    

![Award_Winning](https://www.fullstackmodeller.com/hubfs/badge.jpg)

Become a Modelling Pro
----------------------

Join us and we'll unlock your full potential.

Our award-winning training programme, and exclusive global community, will guide you on your way to Excel, Financial Modelling, data visualisation & analytics mastery.

[Join as an Individual](https://www.fullstackmodeller.com/full-stack-membership)
 [Register Your Team](https://www.fullstackmodeller.com/team-training)

Latest Blogs
------------

*   [New Year, New You?](https://www.fullstackmodeller.com/blog/full-stack-modeller-new-year-new-you)
    
*   [New Import Functions](https://www.fullstackmodeller.com/blog/excel-importtext-importcsv)
    
*   [Best Practice Confessions & Terminology Overload](https://www.fullstackmodeller.com/blog/unpivot-episode-40-full-stack-modeller)
    
*   [Excel Meetup Groups](https://www.fullstackmodeller.com/blog/excel-meetup-groups)
    
*   [New Features and Common Data Problems](https://www.fullstackmodeller.com/blog/unpviot-episode-39)
    
*   [More AI Hype and Traps to avoid when modelling](https://www.fullstackmodeller.com/blog/unpviot-episode-38)
    
*   [The Excel World Championship Song](https://www.fullstackmodeller.com/blog/excel-world-championship-song)
    
*   [The Advanced Financial Modeler Certificate from FMI](https://www.fullstackmodeller.com/blog/advanced-financial-modeler)
    
*   [The history of Microsoft Excel](https://www.fullstackmodeller.com/blog/history-of-excel)
    
*   [My main learning from the FMI AFM exam](https://www.fullstackmodeller.com/blog/financial-modeling-institute-fmi-afm-learnings)
    

#### Subscribe to our monthly modelling newsletter