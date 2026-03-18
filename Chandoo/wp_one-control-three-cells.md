# One Control Three Cells » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/one-control-three-cells

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

One Control Three Cells
=======================

*   Last updated on March 5, 2018

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

A few weeks back I was asked “_Is it possible to setup a control and then drag it down a range, so that it links to all the cells below it?_”

The answer is, of course, No.

But it got me thinking about why not allow one control to control a number of cells.

This post describes the solution, **One Control Three Cells**.

But it could just as easily be applied to a larger group of controls in a much larger system.

I have attached a sample file demonstrating the technique: [Download sample file](https://chandoo.org/wp/wp-content/uploads/2018/03/3-Cells-1-Control.xlsm)

### The Old

In the sample file select the **Old** worksheet.

Typically if you had 3 cells and wanted to add automation, you would add a control to each cell.

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c1.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c1.png)

Here I have added 3 controls. Each Control in Column E controls the Cells value to the left of it.

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c2.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c2.png)

Each Control is independent and has no relationship to other cells or other controls.

Each control is setup and linked as shown below to a single cell.

This whole setup has to be applied individually to each control and associated cell.![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c3.png)

The Cell link: dialog above cannot have a range

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c4.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c4.png)

Well it can hold a range, but it only links the control to the upper left cell of the range, **C3** in the example above.

But this got me thinking, why not link the control’s Cell Link to a **Named Formula**, which would return the range based on say where the active cell was.

### The New

Change to the New Worksheet.

Notice how we now have a single control next to the 3 cells we wish to control.

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c7.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c7.png)

You can see that in action here

[https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c1.mp4](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c1.mp4)

Lets first examine what has been setup, then we will work through how it works.

First, Goto the **Name Manager** in the **Formulas**, **Name Manager** tab.

There are 3 Named Formula setup

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c5.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c5.png)

**SelectedRow** : is a direct Link to cell **A1**

**ControlRange**: is a direct Link to cells **C3:C5**

**ControlLink** : is a named Formula containing a formula \=OFFSET(New!$C$1,SelectedRow-1,0)

Next Right click on the Control and notice that it is linked to the **ControlLink** Named Formula.

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c6.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c6.png)

There is more, but lets follow this through first.

Cell **A1** “**SelectedRow**” contains the value 4.

The Named Formula **ControlLink** has a formula \=OFFSET(New!$C$1, SelectedRow-1, 0)

which evaluates to =OFFSET(New!$C$1, 4-1, 0)

which simplifies to \=OFFSET(New!$C$1, 3, 0)

The offset of **C1** by **3** rows and **0** columns is **C4**

so the Named Formula **ControlLink** \=OFFSET(New!$C$1, SelectedRow-1, 0)

returns the address of **C4**

So the Control uses an Address of **C4** when the value of **A1** is **4**

But we didn’t change cell **A1** ?

I did say there was more, and the more is a small piece of VBA code, which does some checking for us and places an appropriate value in **A1**

Goto VBA by pressing **Alt**+**F11**

Double click on the **Sheet1(New)** object and you should now see the code in the Code Pane

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c8.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c8.png)

This tiny piece of code is the secret behind what makes this technique work.

Lets look at what it does

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)  
  If Intersect(Target, Range(“ControlRange”)) Is Nothing Then  
    Range(“SelectedRow”).Value = 0  
    Exit Sub  
  End If  
Range(“SelectedRow”).Value = Target.Row  
Application.CalculateFull  
End Sub

The code is encapsulated in what is known as a **Worksheet** event.

Worksheet events, as the name implies, are events that occur on the worksheet.

In this case it is the **SelectionChange** event. That is every time you change the cell by clicking on it or using the keyboard arrows etc to change the active cell, this event is triggered and the enclosed code executed.

When the event is triggered the code starts and a variable **Target** is assigned to the new active cell. It is the **Target** of the events occurrence, ie: Your click on another cell.

The next piece of code handles what happens next

If Intersect(Target, Range(“ControlRange”)) Is Nothing Then  
    Range(“SelectedRow”).Value = 0  
    Exit Sub  
End If

It basically says If the **Target** and the **ControlRange** Don’t Intersect then do the enclosed code

That is if the **Target** doesn’t intersect with the **ControlRange**, then set the **SelectedRange** cell **A1** to 0

Then exit the subroutine

This is done so that cells that are selected whilst using the worksheet don’t interfere with the control.

But the important thing is what happens if the **Target** and **ControlRange** do intersect

The code says If there is not an intersection do what is inside the **If** / **End If** statements

If Intersect(Target, Range(“ControlRange”)) Is Nothing Then  
    Range(“SelectedRow”).Value = 0  
    Exit Sub  
End If

But if the two ranges **Do Intersect**, the code simply passes over the included code and continues past to the next code.

The next code is

Range(“SelectedRow”).Value = Target.Row  
Application.CalculateFull

This is where the **SelectedRow** cell **A1** is assigned the value which is the Row number of the **Target** cell.

That is if we click in a cell in the **ControlRange**, the **SelectedRow** is assigned the value of the Target cells Row.

The worksheet is then calculated. This simply forces the named Formula to update.

Then the VBA finishes executing.

When the Worksheet was recalculated just above, the **LinkedCell** was updated.

Now when a user presses the Spin Button Control, it will use the new value in the **LinkedCell** named range as the Link cell and update the value of the cell according to whether you pressed the Up or Down arrow.

### **Final**

This code can be applied to any number of controls as well as to complex ranges

If you wanted to control the values in the 9, dashed green, cells shown below highlighted

[![](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c9.png)](https://chandoo.org/wp/wp-content/uploads/2018/03/3c1c9.png)

You would change the formula for **ControlRange** to

**ControlRange** :  \=New!$B$8:$B$10,New!$C$11:$C$13,New!$B$14:$B$16

### Comments:

What do you think about this technique?

Let me know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [3 Comments](https://chandoo.org/wp/one-control-three-cells/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/one-control-three-cells/#respond)
    
*   Tagged under [Controls](https://chandoo.org/wp/tag/controls/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousStay on top of money with this awesome household budget spreadsheet \[downloads\]](https://chandoo.org/wp/budget-spreadsheet-download/)

[NextQuick tip: Rename headers in pivot table so they are presentableNext](https://chandoo.org/wp/quick-tip-rename-headers-in-pivot-table-so-they-are-presentable/)

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
    
    [Reply](https://chandoo.org/wp/one-control-three-cells/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/one-control-three-cells/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/one-control-three-cells/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ