# Handle Volatile Functions like they are dynamite » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

Handle Volatile Functions like they are dynamite
================================================

*   Last updated on March 11, 2014

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

![Volatile functions in Excel are like dynamite. Handle them with care!](https://img.chandoo.org/g/volatile-functions-are-dynamite.jpg)

If you’re building large models, then you may want to use _volatile_ functions – including OFFSET(), INDIRECT(), and TODAY() – with caution, because unless you know what you are doing, they \*might\* slow Excel down to the point that data entry is sluggish, if not downright tedious.

In fact, you \*might\* want to consider getting out of the habit of using these functions at all if there are  alternatives, and you might want to replace volatile functions in your existing models with non-volatile alternatives…I have reduced recalculation time in large models from _minutes_ to _milliseconds_ by doing just that!

So what the heck does _volatile_ actually mean? And _why_ should you care? Let’s find out, shall we?  
   
 

How does Excel update all those cells?
--------------------------------------

Let’s take a look at how Excel ensures that each cell has the right number in it when you make a change somewhere. But first, a disclaimer: Note that this is an _introductory_ article, and so is necessarily simplistic. If you want to know more about the specifics of this complicated subject, check out the links to Excel MVP Charles Williams’ **excellent** site at the bottom of this article. Okay, disclaimer ends…

A large Excel model might have several hundred thousand cells with formulas in it. Maybe even several million. Most of these formulas will reference other cells, and many of those cells will have formulas in them that reference other cells in turn, and so on. If a formula in a Cell A2 refers directly to Cell A1, then A2 said to be _directly dependent_ on A1. Obviously if A1 changes, we need those changes to flow through to A2. And when recalculating the entire workbook, we need A2 to be recalculated AFTER A1 has been recalculated. That’s called a _dependency chain_.

Large models can have a number of very long dependency chains comprising of hundreds of thousands of cells that run across worksheets or even between workbooks. To keep track of how all these cells interrelate – and to ensure that a change in any specific cell’s value correctly flows through to any other cells that may depend on it – Excel builds and maintains what is known as a ‘dependency tree’. Think of this as a big flow-chart or circuit diagram showing how all the cells in one of these giant formulas interconnect. Excel _maintains_ this dependency tree every time you make a change to a formula in a cell, by looking at the _argument list_ of each separate function within that formula. And this dependency tree is saved along with the file itself.

Smart Recalculation
-------------------

Thanks to this dependency tree, when you change the value in _one_ cell, Excel can work out what _other_ cells might be affected. And so Excel can smartly recalculate _just those particular cells_. Meaning it doesn’t have to blindly recalculate the whole workbook just because one fairly insignificant part of it might have changed.

So let’s say you change the value of a cell  somewhere that has only **one other** cell pointing at it (and no further cells depend on that _other_ cell). Thanks to smart recalculation, Excel only recalculates the value of the cell you just changed, and the value of that ONE dependent cell. It doesn’t have to recalculate the entire workbook.

Likewise, if you change the value of a cell somewhere that has many, many cells downstream, then Excel of course has to recalculate _all_ of the cells further down that particular chain. But it can safely ignore any cells further _up_ that particular dependency chain. And it can ignore any cells elsewhere that aren’t in this _particular_ dependency chain.

If a long-enough part of a dependency chain gets recalculated, then you might well see the word ‘calculating’ in the status bar while Excel works its way through all the relevant cells in that chain. But usually, this recalculation happens so fast that the word ‘calculating’ flicks on and off so quickly that you don’t notice it.

_Not-so-smart_ recalculation thanks to volatility
-------------------------------------------------

**Now here’s the important bit:** a particular class of formulas called _volatile_ formulas get _automatically_ recalculated **_any time_ you enter data _anywhere_ in _any_ open workbook** – even if the thing you just changed had nothing to do with those volatile functions. And then this triggers Excel to then recalculate _all_ directly dependent cells downstream from those volatile formulas too. _Yikes!_

This mean that if you’ve opened a very large spreadsheet model with volatile functions in it – and if those volatile functions have a large number of formulas downstream (or a smaller amount of resource intensive formulas) – then if you are say trying to add items to a shopping list that you’ve started in another workbook it could take _minutes_ for you to add each item to that shopping list, because every time you add an item, it triggers an avalanche of unnecessary and pointless recalculation in the large spreadsheet model.

The fact that each and every cell ‘downstream’ of any volatile formulas get recalculated is an important point to get your head around. Many people think that slow calculation times due to volatility is due to the time it takes to recalculate large amounts of volatile functions in a model. But often most of that delay is in fact due to the recalculation of all the cells ‘downstream’ from those volatile functions. In other words, even just _one_ volatile formula with a very long calculation chain hanging off it could cause you grief. And if that calculation chain gets more and more complex, so does the effect of that one volatile formula.

Here’s how that looks visually:  

In fact, it’s not just _entering data_ that will trigger a volatile function to recalculate, but also these things (among others):

*   Deleting or inserting a row or column.
*   Performing certain Autofilter actions.
*   Double-clicking a row or column divider (in Automatic calculation mode).
*   Adding, editing, or deleting a defined name.
*   Renaming a worksheet.
*   Changing the position of a worksheet in relation to other worksheets.
*   Hiding or unhiding rows (but not columns)

So almost anything can set off that domino effect. Which reminds me of this:  

(And what the heck…if you enjoyed that, then [click this link too](http://www.youtube.com/watch?v=qybUFnY7Y8w&feature=share&list=RDUJKythlXAIY&index=1)
. But hurry back…this post is getting cold).

So which functions are Volatile?
--------------------------------

These ones:

*   NOW()
*   TODAY()
*   RAND() and RANDBETWEEN()
*   OFFSET()
*   INDIRECT()
*   INFO() (depending on its arguments)
*   CELL() (depending on its arguments)

If you’re an intermediate Excel user, then chances are that you already use some of these regularly. For instance:

*   **OFFSET()** is usually the function of choice to anyone who wants to create dynamic ranges
*   Many large models make use of the **INDIRECT()** function to construct cell or range references “on the fly” in response to some choice that a user makes
*   Many large models make use of the **TODAY()** function to check if a date entered by a user occurs in the past, present, or future.

When does this matter?
----------------------

Most of the spreadsheets you use these functions in are so small that you probably don’t even notice any extra volatility-related recalculation. So no harm done. However, if you’ve ever had that a large spreadsheet that seems _particularly sluggish_ when you’re trying to enter new data – or that seems to impact the performance of other open workbooks – then chances are you know _exactly_ what I mean.

I’ve seen frustrated-looking users waiting for as long as one to two minutes for particularly large models to recalculate after each and every change they make to it, even if those changes are relatively insignificant, such as changing the spelling of a column header.

Often spreadsheets like this get so sluggish that users switch Excel’s calculation setting to Manual, just so they can make changes in a timely fashion, and then switch it on again when they’re done in order to have the model calculate the correct answer. **This is dangerous**…I’d **never** set calculation to manual if I could help it. There’s just too much chance that someone someday will use output of such a model without remembering to set calculation to Auto. What’s worse, when you open two workbooks, one saved in manual mode and one saved in automatic mode, they will both have the calculation mode of the first workbook opened. I have seen many cases in my career where analysts have done just that…opened a workbook with calc set to manual, opened a whole bunch of others where calc was set to auto, and then done an entire day’s work without realizing that calculation was subsequently turned off for _all_ of them. Doh!

Here’s a slide from my Excel Efficiency presentation that warns users not to do this:  
[![Chandoo_Big Trouble in Little Spreadsheet_Slide](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Slide.gif)](https://chandoo.org/wp/wp-content/uploads/2014/01/Chandoo_Big-Trouble-in-Little-Spreadsheet_Slide.gif)

Previously you might have thought that you had _no choice_ but to switch calculation to Manual, because you might have thought that this sluggishness is an _unavoidable consequence_ of the size and complexity of your spreadsheet. But now you know that it _\*might\*_ be caused by use of volatile functions, and that volatile functions _might not be suitable_ for some occasions…_particularly_ if you’re building large models that utilize these functions at key points within your model. Replace those Volatile functions with some non-Volatile alternatives, and you’ll likely find that your model stops being a slow dog, and starts being a much faster greyhound. To the point that you can switch calculation back to Automatic again.

What are the alternatives to Volatile functions?
------------------------------------------------

While volatile functions like OFFSET() and INDIRECT() are incredibly useful, you can usually achieve the same thing by using other _non-volatile_ formulas such as INDEX or CHOOSE, as well as through leveraging off the dynamic references that Excel Tables allow.

And instead of the TODAY() function, you can use VBA to populate today’s date as a hard-coded value in big models, as you’ll see in the download file below. Check out the **Alternative Functions** tab of that file to see some examples of common use of volatile functions, as well as some non-volatile alternatives.

If you’re struggling to find a non-volatile replacement for an existing volatile formula, then you can always post a question on the [Chandoo Forum](http://forum.chandoo.org/)
 asking for some advice on non-volatile alternatives.

Am I being over-zealous here?
-----------------------------

As we’ve seen, too much reliance on volatile functions _\*might\*_ trigger large parts of a model to be recalculated needlessly. But it’s worth remembering that _this is only going to be noticeable in particularly big spreadsheets_. So perhaps I’m being a little overzealous here. So if you know what you’re doing, then maybe you don’t want to dismiss volatile functions outright. After all, you can always assess your options on a case by case basis: try them out, test, test, test, test again, and then make a balanced decision.

However, if you know of an alternative formula combination that does exactly the same thing as a _volatile_ formula, then I’d suggest that you get into the habit of using that instead whenever you can. That way you won’t _inadvertently_ have issues when it really matters. And I’d suggest that if you don’t have much experience of functions and performance, then perhaps it’s safest to simply err on the side of caution and **steer clear of volatile functions altogether**.

So not only do I see little down side to avoiding volatile formulas, but I see a significant upside: I’ve seen _plenty_ of large models built by the likes of the big 4 accounting/consulting firms that make heavy use of volatile functions, and that consequently have recalculation times so long that they are effectively unusable. Stripping out the volatile formulas from these models has resulted in delays from data entry falling from upwards of two minutes to well under a second. Not to mention that users can now work on **other** files while these models are open, without fear of triggering an avalanche of unnecessary and pointless recalculation. Had these model builders known to avoid volatile functions, they would have saved users a lot of grief.

Excel MVP and Recalculation Expert [Charles Williams says](http://msdn.microsoft.com/en-us/library/ff700515.aspx#Office2007excelPerf_FindingPrioritizingCalculationBottlenecks)
:

> The better use you make of smart recalculation in Excel, the less processing has to be done every time that Excel recalculates, so avoid volatile functions like INDIRECT and OFFSET where you can, unless they are significantly more efficient than the alternatives. (Well-designed use of OFFSET is often fast.)

In fact, on Charles’ website he goes so far as to say [avoid volatile functions wherever possible.](http://www.decisionmodels.com/calcsecretsi.htm)

With all that in mind, I’ve made a personal choice to steer clear of volatile functions where I can. Your mileage may differ. Regardless, the subject of volatility is definitely something that intermediate users **should** be made aware of. What they **do** with that awareness is up to them. But forewarned is forearmed.

Fancy a demonstration?
----------------------

Sometimes it’s most helpful to see something with your own eyes. So download this file, open it, and enable macros: [Volatility-demo-using-TODAY-20140230](https://chandoo.org/wp/wp-content/uploads/2014/03/Volatility-demo-using-TODAY-20140230.xlsm)
  
You’ll see it has a dropdown in it, where you can choose to either populate a cell with the volatile TODAY function or with a hard-coded date:  
[![Chandoo_VolatileFormulas_Dropdown](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_VolatileFormulas_Dropdown.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_VolatileFormulas_Dropdown.gif)
  
Downstream of that drop-down output cell are 20,000 formulas spread across two columns:  
[![Chandoo_VolatileFormulas_Formulas](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_VolatileFormulas_Formulas.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_VolatileFormulas_Formulas.gif)

If you choose the **Use Volatile TODAY() Function** option from the dropdown, then whenever you enter data in that 3rd **‘Completely independent cells’** column then you should notice a significant delay. Change that dropdown to ‘Use Hard-Coded Date’ and you should experience significantly _less_ delay, if any.

You’ll also see a blue button you can click, that will time how long the delay is under each option:  
On my system, there’s about a 1 second delay when using the TODAY() option, and almost no delay when using the hard-coded date. (Note that you have to click the blue button twice after you change that dropdown to get the ‘proper’ reading. The first reading will be artificially high.)  
[![Chandoo_Volatility_Test](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Volatility_Test.png)](https://chandoo.org/wp/wp-content/uploads/2014/03/Chandoo_Volatility_Test.png)

Why _are_ some functions volatile?
----------------------------------

The reason for _some_ of these functions being volatile this is fairly obvious. For example:

*   NOW() should always return the time as at the last calculation, so needs to be refreshed any time new data is put into the workbook, in case one of your formulas does something specific based on the time of day.
*   TODAY() similarly must be refreshed to ensure than the day hasn’t changed since the last time something was entered into the workbook  (which will be the case, if someone works past midnight, or if they come in in the morning and make a change to a file that they had left open the previous night.)

But the reasons for others being volatile – such as OFFSET and INDIRECT, which are often used by modellers to create dynamic named ranges – are less clear. First, let’s look at what OFFSET and INDIRECT actually do:

*   Offset Returns a reference to a cell or a multi-cell range that is a given number of rows and columns from a given reference. So OFFSET($A$1,1,2,5,3) says “Go one cell down from $A$1 (which takes us to $A$2), then two cells across (which takes us to $C$2) and then return a block of cells 5 down from $C$2 and 3 across from $C$2 (which gives us the range $C$2:$D$6)
*   Indirect Returns the reference specified by a text string. References are immediately evaluated to display their contents. So Indirect(“$A1”) tells Excel “Go look in cell $A$1, and tell me what’s in it”.

So why would that mean they need to be volatile? Because Excel constructs dependency trees based on cell references.

*   INDIRECT() has an argument that is constructed out of _text_ – e.g.  INDIRECT( “$A1”). This might look like a cell reference, but it is not. In fact, the argument of an INDIRECT function might equally look something like this:  INDIRECT(“$B”&$C$9-2)**.**
*   OFFSET() takes _numerical_ arguments, which point to a cell reference, but are still just numbers.
*   In order for these to form part of Excel’s dependency tree, the Excel dependency tree algorithm would have to first evaluate **text** like INDIRECT( **“$A1”**) or the numerical arguments like OFFSET($A$1,**1,2,5,3**) in order to determine what the associated cell reference actually is, before adding it to the dependency tree. Maybe the Excel obviously made the call that rather than introduce this extra step where these two functions are concerned, they may as well just make both functions fully volatile.

But given that you can set up INDEX() do much the same thing as OFFSET(), why doesn’t INDEX need to be volatile too? I imagine it’s because INDEX uses _range_ arguments, whereas OFFSET uses _numerical_ arguments. So Excel can extract these range arguments directly from an INDEX() function when building/amending the calculation dependency tree.

Note that INDEX() is what’s called semi-volatile, meaning it gets recalculated when the workbook opens.

And also note that any formulas used in conditional formatting effectively become what Charles Williams calls _super-volatile_: they are evaluated each time the cell that contains them is repainted on the screen (which happens say if you use the scroll bar to move the ‘view’ up/down or left/right), even in Manual calculation mode. But because no other formulas are ‘downstream’ from conditional formats, then only the conditional format formulas themselves get recalculated. So if you’ve got simple conditional formatting rules, you won’t notice any delay.

More info:
----------

I’ll talk about alternatives to using volatile functions in a series of upcoming posts. But meanwhile…if you’re not feeling too sluggish…then check out these great links from Excel MVP Charles Williams.

*   [Excel 2010 Performance: Improving Calculation Performance](http://msdn.microsoft.com/en-us/library/ff700515.aspx#Office2007excelPerf_FindingPrioritizingCalculationBottlenecks)
    
*   [Smart Recalculation](http://www.decisionmodels.com/calcsecrets.htm)
    
*   [Volatile Excel Functions](http://www.decisionmodels.com/calcsecretsi.htm)
    
*   [Excel Dependencies](http://www.decisionmodels.com/calcsecretsd.htm)
    
*   E[valuation Circumstances](http://www.decisionmodels.com/calcsecretsb.htm)
    
*   [Writing efficient VBA UDFs Part 10 – Volatile Functions and Function Arguments](http://fastexcel.wordpress.com/2012/02/02/writing-efficient-vba-udfs-part-10-volatile-functions-and-function-arguments/)
    

Pretty much everything I’ve covered in this post came from Charles’ writings, so I’d like to acknowledge the work he has done in explaining this complex subject to countless Excel users over the years. Charles also sells a great add-in called [FastExcel](http://www.decisionmodels.com/fastexcelD.htm)
 for profiling Excel calculation performance and memory useage – so be sure to check that out if you want to get serious about diagnosing volatility issues with your own Excel models.

You may also be interested in Jan Karel Pieterse’s [RefTreeAnalyser](http://www.jkp-ads.com/RefTreeAnalyser01.asp)
 utility, which among other things allows for easy Auditing of formula dependents and precedents, helps you trace errors, and will let you time your workbook calculation for each worksheet to find bottlenecks as well as check columns for formula inconsistencies. Jan Karel has a free demo version with limited functionality, if you’d like to take it for a spin.

Let me know your thoughts in the comments
-----------------------------------------

This has been a particularly taxing post to write. So if you found this article helpful, please let me know below in the comments. If you’re not following something I said, or can think of a better way to say it, then let me know that too.

### About the Author.

**Jeff Weir** – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure #VALUE!

Find out more at [http://www.heavydutydecisions.co.nz](http://www.heavydutydecisions.co.nz/ "http://www.heavydutydecisions.co.nz")

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [67 Comments](https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [excel optimization](https://chandoo.org/wp/tag/excel-optimization/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [now()](https://chandoo.org/wp/tag/now/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [today()](https://chandoo.org/wp/tag/today/)
    , [volatile functions](https://chandoo.org/wp/tag/volatile-functions/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    

[PrevPreviousCan you extract first name & last name from email address? \[Formula Challenge\]](https://chandoo.org/wp/extract-first-name-last-name-from-email/)

[NextChandoo.org Podcast: Launching on March 6thNext](https://chandoo.org/wp/chandoo-org-podcast-launching-on-march-6th/)

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
    
    [Reply](https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ