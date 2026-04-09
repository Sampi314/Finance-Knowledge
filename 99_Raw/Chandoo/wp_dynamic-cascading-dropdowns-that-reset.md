# Create dynamic (cascading) dropdowns with Data Validation

**Source:** https://chandoo.org/wp/dynamic-cascading-dropdowns-that-reset

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Dynamic (Cascading) Dropdowns that reset on change
==================================================

*   Last updated on August 22, 2014

![Picture of Jeff Weir](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=300&d=mm&r=g)

#### Jeff Weir

Share

Facebook

Twitter

LinkedIn

Dynamic dropdowns are a handy way to get your users to make choices based on what they’ve previously chosen, while steering them away from making _invalid_ choices. Today we’re going to look at one that easily handles **multiple** levels, and we’ll take a look at what could go wrong. Let’s see one in action, shall we?

Right, what’s on the (dropdown) menu?  
[![Chandoo_CascadingDropdowns_NoChoices](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_NoChoices.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_NoChoices.png)

Fruit, anyone?  
[![Chandoo_CascadingDropdowns_First Choice](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_First-Choice.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_First-Choice.png)

_**\*BING!\***_  
[![Chandoo_CascadingDropdowns_Not Done](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Not-Done.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Not-Done.png)
  
Cool…check it out…as you can see from the above, the user gets prompted with “Choose…” whenever a subsequent choice must be made.

Ok, what _kind_ of fruit should I have? Hmmm, let me see….eeny, meeny, miny, _STRAWBERRIES!!!_…**MO!**  
[![Chandoo_CascadingDropdowns_Strawberries](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Strawberries.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Strawberries.png)

_**\*BING!\***_  
[![Chandoo_CascadingDropdowns_Still not finished](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Still-not-finished.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Still-not-finished.png)

Ok, so what delights does _Sub Category 2_ have in store for me?  
[![Chandoo_CascadingDropdowns_Earliglow](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Earliglow.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Earliglow.png)

_Earliglow?_ Never heard of it. Sounds delicious…I’ll have those, please.

_**\*BING!\***_  
[![Chandoo_CascadingDropdowns_Done](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Done.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Done.png)

There, all done. Pretty nifty eh**…**users only get to see valid choices depending on what they chose last. So users simply can’t screw up!  **Or _can_ they?**

**\[Evil user, determined to prove me wrong\]:** _Wait a minute…I just remembered that mother expects me to eat my vegetables first, before I move on to dessert. So I better change that initial selection:_

[![Chandoo_CascadingDropdowns_Change Initial Selection](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Change-Initial-Selection.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Change-Initial-Selection.gif)

_**\*BING!\***_  
[![Chandoo_CascadingDropdowns_Embarrassing](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Embarrassing.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Embarrassing.png)
  
_**What the…**_Strawberries are _vegetables???_

_**Damn**_…changing _upstream_ dropdowns later on means those _downstream_ choices can be flat out wrong! So how can we make this bulletproof?

Macros to the rescue
====================

Yep, we’ll use some code to clear out any ‘downstream’ choices if anything ‘upstream’ changes. Let’s go back to that original strawberry fest:  
[![Chandoo_CascadingDropdowns_Done](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Done.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Done.png)

Now watch what happens when our user subsequently decides they better vege out first:

_**\*BING!\***_  
[![Chandoo_CascadingDropdowns_Downstream Reset](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Downstream-Reset.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Downstream-Reset.png)

Ahh…look at that: the code realized that all those downstream choices are no longer valid. So it deleted them, and prompted the user to choose again. There. Now that IS bulletproof.

So let’s see…hmmm…for an appetizer, I’ll have baby carrots:  
[![Chandoo_CascadingDropdowns_Baby Carrots](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Baby-Carrots.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Baby-Carrots.png)

And I already decided on Strawberries for pudding…  
[![Chandoo_CascadingDropdowns_Pudding](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Pudding.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Pudding.png)

But what about my main course. Ah, yes, of course…  
[![Chandoo_CascadingDropdowns_Human](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Human.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Human.png)

_MEAT!_ **Yummy. _BURP!_**  

What’s the recipe?
==================

My approach draws on [Roger Govier’s excellent sample file on the Contextures](http://www.contextures.com/xlDataVal15.html)
 website. Be sure to check out that link to see Roger’s in-depth discussion of the formula magic behind this puppy…It’s genius.

In my [Dynamic-Dependent-dropdowns-20140214](https://chandoo.org/wp/wp-content/uploads/2014/02/Dynamic-Dependent-dropdowns-20140214.xlsm)
, you’ll see that all the different categories used by the dropdowns are hosted in an **Excel Table**, that has the _initial_ categories down the left hand side, and _subsequent_ categories across the top:  
[![Chandoo_CascadingDropdowns_val list](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_val-list.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_val-list.gif)

So how do these categories get used by the data validation dropdowns? Roger’s approach uses two dynamic named ranges to feed the data validation lists, one called **MainList** and one called **SubList**:  
[![Chandoo_CascadingDropdowns_Name Manager](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Name-Manager.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Name-Manager.gif)

Here’s the **MainList** formula:  
`=INDEX(Table1[[Choose…]],1):INDEX(Table1[[Choose…]],COUNTA(Table1[[Choose…]]))`

…and here’s the **SubList** formula:  
`=IF(OR(Sheet1!B8="Choose…",Sheet1!B8=""),"",INDEX(Table1,1,MATCH(Sheet1!B8,Table1[#Headers],0)):INDEX(   Table1,COUNTA(INDEX(Table1,,MATCH(Sheet1!B8,Table1[#Headers],0))),MATCH(Sheet1!B8,Table1[#Headers],0)))`

The **SubList** formula has a _relative_ reference in it: whatever cell you use it in, it retrieves the value of the cell to the immediate left, and then it scans the column headers of our validations table (Table1) looking for the heading that matches that value. Once it’s found it, it simply uses the items listed underneath that heading.

Because this formula is relative, **before you enter it into the Name Manager, you will need to first select cell C8**, because the above relative formula refers to B8 – the cell to the left. (Note that it doesn’t matter what is in C8 or where your actual dropdown are…rather it’s just that the above formula happens to refer to B8, and because we want our formula to always reference the cell on the immediate left, then we’ve got to select the cell to the immediate right before we enter this relative formula into the Name Manager.

Also note that my version of Roger’s approach uses **Excel Tables** and the associated **Structured References** that Table functionality allows. My table is called Table1. **Your validation lists MUST be held within an Excel Table (which requires Excel 2007 or greater) and you MUST change the Table1 references in the above formula to match the name of your table.**

Excel Tables – known as ListObjects to VBA developers – were introduced in Excel 2007, and are a very powerful _and simple_ way to store things like lists, chart data, and PivotTable data…especially if you might need to add more data to your spreadsheet at a later date, and want to avoid having to repoint all your formulas to include the additional data. If you’re not familiar with Excel Tables – or you don’t know what that **Table1\[#Headers\]** guff above means – then I **strongly suggest** you check out Chandoo’s [Introduction to Structural References](http://chandoo.org/wp/2013/06/26/introduction-to-structural-references/ "Introduction to Structural References")
 and [this great video he did with MrExcel.](http://www.youtube.com/watch?v=cQermVuEc78&feature=youtu.be "MrExcel")

The way these two formulas work is very clever. That **MainList** named range only gets used by dropdowns in that very first ‘Main Category’ column:  
[![Chandoo_CascadingDropdowns_MainList2](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_MainList2.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_MainList2.png)

…and all other ‘downstream’ dropdowns – no matter what level they are – are fed by the **SubList** named range:  
[![Chandoo_CascadingDropdowns_SubList2](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_SubList2.png)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_SubList2.png)

The beauty of Roger’s approach is that it can handle _any number of cascading levels_, **provided all the category names are unique**. All you need to do is simply add the new subcategories to the right hand side of our validations table (Table1).

Let’s look at an example. If you look at the below screenshot, you’ll see that users can choose from a number of different kinds of meat:  
[![Chandoo_CascadingDropdowns_Meat List](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Meat-List.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Meat-List.gif)

Let’s add a further level that would give meat eaters some further choices relating to _how their meat is prepared_.

To set this up, all we need to do is take the individual items from that ‘Meat’ column and add each one as a new column header:  
[![Chandoo_CascadingDropdowns_New Headers](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_New-Headers.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_New-Headers.gif)

Then we simply list the new options for each type of meat below the relevant header:  
[![Chandoo_CascadingDropdowns_Flesh out](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Flesh-out.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Flesh-out.gif)

Now here’s the magic: as soon as we add another column to our input table and set it up with data validation – which I did simply by clicking on the bottom right corner of the cell with the word ‘Human’ and dragging it across – then Excel picks up on the fact that there’s a sub-subcategory, and serves it up to us. _**\*BING!\***_ **Order up!**  
[![Chandoo_CascadingDropdowns_Raw Person](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Raw-Person.gif)](https://chandoo.org/wp/wp-content/uploads/2014/02/Chandoo_CascadingDropdowns_Raw-Person.gif)

Add code, and stir-fry for 10 milliseconds
------------------------------------------

As mentioned earlier, in addition to Roger’s great method, I’ve written some code that clears out any downstream entries in the event that an upstream entry is changed. It’s in the sample workbook already, all set to go. But here’s the actual code, for you VBA nerds. (Special thanks to Gabor Madacs for some enhancement suggestions)  

`Option Explicit  Const CHOOSE = "Choose…"  Private Sub Worksheet_Change(ByVal Target As Range)     On Error GoTo ErrorHandler     Dim targetCell As Range     Dim nextCell As Range     Dim oldCalc As Excel.XlCalculation          If Not Intersect(Target, [DataEntryTable]) Is Nothing Then         If [Radio_Choice] = 1 Then             With Application                 .EnableEvents = False                 .ScreenUpdating = False                 oldCalc = .Calculation                 .Calculation = xlCalculationManual             End With                          For Each targetCell In Target                 'Clear any cells that use 'SubList' to the right of targetCell in the current table.                 If targetCell.Column < (targetCell.ListObject.ListColumns.Count + targetCell.ListObject.Range.Column - 1) Then 'there are table cells to the right                     For Each nextCell In targetCell.Offset(, 1).Resize(, targetCell.ListObject.ListColumns.Count + targetCell.ListObject.Range.Column - targetCell.Column - 1)                         If HasValidationFormula(nextCell) Then                             If nextCell.Validation.Formula1 = "=SubList" Then nextCell.Value = ""                         End If                     Next nextCell                 End If                                  'Perform different action depeding on whether we're dealing with a 'MainList' dropdown                 ' or a 'SubList' dropdown                 If HasValidationFormula(targetCell) Then                     Select Case targetCell.Validation.Formula1                     Case "=MainList"                         If targetCell.Value = "" Then                             targetCell.Value = CHOOSE                         ElseIf targetCell.Value = CHOOSE Then                             'Do nothing.                         Else                             targetCell.Offset(, 1).Value = CHOOSE                         End If                                              Case "=SubList"                         If targetCell.Value = "" Then                             targetCell.Value = CHOOSE                         ElseIf targetCell.Offset(, -1).Value = CHOOSE Then                             targetCell.Value = ""                         ElseIf targetCell.Value = CHOOSE Then                             'Do nothing                         Else                             Set nextCell = targetCell.Offset(, 1)                             If HasValidationFormula(nextCell) Then                                 If nextCell.Validation.Formula1 = "=SubList" Then nextCell.Value = CHOOSE                             End If                         End If                     End Select                 End If             Next targetCell             With Application                 .EnableEvents = True                 .ScreenUpdating = True                 .Calculation = oldCalc             End With         End If     End If     Exit Sub ErrorHandler:     With Application         .EnableEvents = True         .ScreenUpdating = True         If oldCalc <> 0 Then .Calculation = oldCalc     End With     MsgBox Err.Description, vbCritical, Name & ".Worksheet_Change()" End Sub  Private Function HasValidationFormula(cell As Range) As Boolean     On Error GoTo ValidationNotExistsError     If cell.Validation.Formula1 <> "" Then         HasValidationFormula = True     Else         HasValidationFormula = False     End If     Exit Function ValidationNotExistsError:     HasValidationFormula = False End Function`
 

  

Hungry for more?
================

  
Here’s some related Posts at Chandoo.org:

*   [Advanced Data Validation Techniques in Excel](http://chandoo.org/wp/2008/11/25/advanced-data-validation-techniques-in-excel-spreadcheats/ "Advanced Data Validation Techniques in Excel [spreadcheats]")
    
*   [Make your data validations dynamic!](http://chandoo.org/wp/2010/09/13/dynamic-data-validation-excel/ "Make your data validations dynamic! [quick tip]")
    
*   [](http://chandoo.org/wp/2011/02/07/data-entry-forms-with-conditional-formatting-and-validation/ "Make Awesome Data Entry Forms by using Conditional Formatting + Data Validation")
    

Download the file
-----------------

To see how this is done, download this file and enable macros:  
[Dynamic-Dependent-dropdowns-20140214](https://chandoo.org/wp/wp-content/uploads/2014/02/Dynamic-Dependent-dropdowns-20140214.xlsm)

About the Author.
-----------------

Jeff Weir – a local of Galactic North up there in Windy Wellington, New Zealand – is more volatile than INDIRECT and more random than RAND. In fact, his state of mind can be pretty much summed up by this:

\=NOT(EVEN(PROPER(OR(RIGHT(TODAY())))))

That’s right, pure **_#VALUE!_**

Find out more at [http:www.heavydutydecisions.co.nz](http://heavydutydecisions.co.nz/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [108 Comments](https://chandoo.org/wp/dynamic-cascading-dropdowns-that-reset/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/dynamic-cascading-dropdowns-that-reset/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [drop down lists](https://chandoo.org/wp/tag/drop-down-lists/)
    , [dynamic named ranges](https://chandoo.org/wp/tag/dynamic-named-ranges/)
    , [excel tables](https://chandoo.org/wp/tag/excel-tables/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Jeff](https://chandoo.org/wp/category/posts-by-jeff/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousPower Pivot course is now open, Please join to become awesome](https://chandoo.org/wp/power-pivot-course-is-now-open/)

[NextLearn how to create these 11 amazing dashboardsNext](https://chandoo.org/wp/dashboard-training-course/)

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
    
    [Reply](https://chandoo.org/wp/dynamic-cascading-dropdowns-that-reset/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/dynamic-cascading-dropdowns-that-reset/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/dynamic-cascading-dropdowns-that-reset/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ