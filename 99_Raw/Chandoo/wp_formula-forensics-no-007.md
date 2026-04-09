# Formula Forensics visits Sumproduct

**Source:** https://chandoo.org/wp/formula-forensics-no-007

---

*   [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics. No 007 – Sumproduct
======================================

*   Last updated on December 21, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

One of the most asked questions within the posts and Forums at Chandoo.org is “How Does Sumproduct work ?”.

Rahul recently asked for an example in [Excels Sumproduct Formula](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/#comment-216497 "Excels Sumproduct Formula")
 post;  Comment No. 55.

So today in Formula Forensics we will take a look at just that with a few worked examples.

Sumproduct
----------

Excels help defines Sumproduct as:

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/SP1.png "SP1")](https://chandoo.org/wp/wp-content/uploads/2011/12/SP1.png)

So what are these arrays referring to:

An array in Excel can be :

**A manual Array**:     {10;20;30}

**A Range**:              A1:A3

**A Named Range**: MyRange1

Where MyRange1 is defined as a defined range in the Name Manager.

**A Named Formula**: MyRange2

Where MyRange2 is defined as a Formula returning a range in the Name Manager.

Lets look at each

You can follow along in the [Example file](https://chandoo.org/wp/wp-content/uploads/2011/12/Sumproduct.xls "Download Sumproduct Example file")
 on Sheet1

**An Array**

In C2 type: \=SUMPRODUCT({10;20;30})

Excel will display 60, which is the Sum of the array elements =10+20+30

**A Range**

**C7**:          \=Sumproduct(C4:C6)

Excel displays 60, which is the Sum of the cells from the range C4:C6 =10+20+30

**A Named Range**

In the Name Manager or Name Box define a Named Range

**MyRange1**:         \=Sheet1!$C$4:$C$6

Then in C10 type:

**C10:** \=Sumproduct(MyRange1)

Excel displays 60, which is the Sum of the range elements =10+20+30

**A Named Formula**

In the Name Manager define a Named Formula

MyRange2          \=OFFSET(Sheet1!$C$3,1,0,3,1)

Then in C12 type:

**C12**:       \=Sumproduct(MyRange2)

Excel displays 60, which is the Sum of the range elements from cells C4:C6 =10+20+30

You may be asking why use Sumproduct when we can use a simple Sum to add up 3 numbers?

The answer is to show you what Sumproduct is doing, it is Adding up each Array element.

### What about the “Product” part of Sumproduct ?

Remember back at the start where we saw the Definition of Sumproduct,

SUMPRODUCT(array1, \[array2\], \[array3\], …)

Only Array 1 is required, Array 2, Array 3 etc are optional, that’s what the square brackets \[ \] mean.

Multiple Arrays
---------------

Goto Sheet 2 in the Example file:

We will look at a simple example using two arrays

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/SP2a.png "SP2a")](https://chandoo.org/wp/wp-content/uploads/2011/12/SP2a.png)

The data consists of Sales data.

Often we want to know what the total sales are

We do this by  adding a **Sales** column

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/SP3.png "SP3")](https://chandoo.org/wp/wp-content/uploads/2011/12/SP3.png)

Which multiplies the **Qty** and **Price** columns

And then **Sum** (Add) up this new column

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/SP4.png "SP4")](https://chandoo.org/wp/wp-content/uploads/2011/12/SP4.png)

Returning our Total Sales of 15,000

Now we can manually check the above as the numbers are simple eg: 100\*20 = 2,000 etc

And we can sum up the Sales and see that we in fact had total sales of 15,000

Well this is exactly what Sumproduct is made to do:

In a Blank cell enter: \=SUMPRODUCT(D4:D8,E4:E8)

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/SP6.png "SP6")](https://chandoo.org/wp/wp-content/uploads/2011/12/SP6.png)

Excel will return 15,000.

So what is Sumproduct doing?

Lets look inside and see what’s going on

In the [Example File](https://chandoo.org/wp/wp-content/uploads/2011/12/Sumproduct.xls "Sumproduct example File")
, **Sheet2**, **H1** there is a copy of the data laid out as below

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/sp7.png "sp7")](https://chandoo.org/wp/wp-content/uploads/2011/12/sp7.png)

Note that our formula \=SUMPRODUCT(D4:D8,E4:E8)

Has two Arrays

**Array 1**: D4:D8

**Array 2**: E4:E8

Note that each corresponding Array Element is multiplied together

100 x 20

20 x 200 etc

These are the products of the two Arrays

Finally the Products are Added together and the correct answer 15,000 is returned.

So **Sumproduct** is the **Sum** of the **Products** of the **Arrays**

Of course we can extend that to a large number of Arrays, columns in this case, if we wish.

**Sumproduct with Logic**
-------------------------

In the above two examples we saw that Sumproduct can Sum a single Array and can Sum the Product of two or more Arrays.

We can use that to our advantage and build logic into the arrays, allowing us to optionally include some array elements and leave out others.

### How?

Sumproduct will always add up the product of all Arrays.

So by including an Array where the elements within the Array that we don’t want to Sum are Zero and the Elements within the array that we do want to Sum are 1 we can control what is included in the final Summation.

Goto our [Example File](https://chandoo.org/wp/wp-content/uploads/2011/12/Sumproduct.xls "Sumproduct example File")
 on Sheet3

Lets say we only want to include the Sales from our Northern Region

One way to do this is to purely delete the other entries

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/sp8.png "sp8")](https://chandoo.org/wp/wp-content/uploads/2011/12/sp8.png)

But what if we could do that without altering our worksheet or there are thousands of rows of data?

This is where Sumproduct comes into its own.

What we need to do is add some logic to our equation, effectively doing:

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/sp9.png "sp9")](https://chandoo.org/wp/wp-content/uploads/2011/12/sp9.png)

Lets try it with Sumproduct

In Cell F12: type =SUMPRODUCT(D4:D8,E4:E8,{FALSE;TRUE;FALSE;FALSE;TRUE})

Excel displays a –

Excel doesn’t know what to do with the True/False and so converts them to 0

We can force excel to evaluate these as numbers by adding a simple “1\*”

In F14: Type \=SUMPRODUCT(D4:D8,E4:E8,1\*{FALSE;TRUE;FALSE;FALSE;TRUE})

Excel now displays **5,000** the total sales from the **North**

To see what has happened in F16 type: 1\*{FALSE;TRUE;FALSE;FALSE;TRUE}, but don’t press Enter press F9 instead.

Excel displays \={0;1;0;0;1}

The use of the 1\* has converted each of the Array elements from a True/False to a 1,0 respectively.

So our 3 arrays are now:

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/sp10.png "sp10")](https://chandoo.org/wp/wp-content/uploads/2011/12/sp10.png)

Now adding an Array of 1\*{FALSE;TRUE;FALSE;FALSE;TRUE} every time we wanted to add some numbers isn’t a practical solution.

**Excel has the ability to work construct an Array on our behalf!**

In E18: enter  \=SUMPRODUCT(D4:D8,E4:E8,1\*(C4:C8=”North”))

Excel will display 5,000

So 1\*(C4:C8=”North”) is exactly equal to our previous array 1\*{FALSE;TRUE;FALSE;FALSE;TRUE}

1\*(C4:C8=”North”) \= 1\*{FALSE;TRUE;FALSE;FALSE;TRUE}

At the heart of this is that Excel is evaluating each cell in the Range: C4:C8 against our required logic =”North” and setting up an Array for us internally.

### **Simplify**

The power of Sumproduct is therefore in that we can now simplify and extend

In cell E20 type: North

In cell F20 type: \=SUMPRODUCT(D4:D8,E4:E8,1\*(C4:C8=E20))

Excel will display 5,000

This simple addition allows us to vary the Summation based on the value in E20

We don’t need to multiply our logic array by 1, we can actually use any number or another Array.

In cell F22 type: \=SUMPRODUCT(D4:D8,(E4:E8)\*(C4:C8=E20))

This works as (C4:C8=E20) is returning an Array of True/False which get converted to an array of 1/0’s when subject to any maths.

The Math in this case is the multiplication by the 2nd Array (E4:E8)\*(C4:C8=E20)

In Cell F24 type: \=SUMPRODUCT(Qty, Price \*(Region=SalesRegion))

Excel will display 5,000

But notice that by using Named Ranges/Formula how simple the logic of the equation has now become.

Rahul’s Question (Multiple Criteria):
-------------------------------------

In Comment No. 55: Rahul asked, “Can you give an example work sheet of above example”

Sheet 4 in the [Example File](https://chandoo.org/wp/wp-content/uploads/2011/12/Sumproduct.xls "Sumproduct exanmple File")
 is the answer.

[![](https://chandoo.org/wp/wp-content/uploads/2011/12/sp11.png "sp11")](https://chandoo.org/wp/wp-content/uploads/2011/12/sp11.png)

In Cell C23: type: =SUMPRODUCT(- -(A2:A21=”Luke Skywalker”),- -(B2:B21=”West”),C2:C21)

Excel will display 141, which is the sum of the Sales made by Luke Skywalker in the West Region.

However using what was learned above, this is better simplified to:

C26: =SUMPRODUCT((Name=SalesMan)\*(Region=SalesRegion)\*Sales)

  

**The Double Unary**
--------------------

In the formula above Chandoo has used what is known as a Double Unary, which is 2 – signs next to each other (I have inserted a space above to make it more legible).

Two – signs are the same as saying

– -(A2:A21=”Luke Skywalker”) = -1 x -1 x (A2:A21=”Luke Skywalker”)

\-1 x -1 is 1

Technically this is the most efficient way for Excel to perform any maths on the Array

– -(A2:A21=”Luke Skywalker”)

So that the Array of true/Falses made by (A2:A21=”Luke Skywalker”) is converted to an Array of 1/0’s for use in Sumproduct.

At the slight expense of speed but for improved readability and understandability by others I prefer the use of **1\*** instead of **– –** and you will mostly see that convention in my posts.

**Chandoo**:            **– –**(A2:A21=”Luke Skywalker”)

**Hui**:                       **1\***(A2:A21=”Luke Skywalker”)

In fact any maths performed on the array will convert its contents to an array of 1/0’s, so long as the maths doesn’t change the Arrays values

For a real good discussion on this topic have a look at the post [The Venerable SUMPRODUCT](http://www.excelhero.com/blog/2010/01/the-venerable-sumproduct.html "The Venerable Sumproduct")
 at [ExcelHero.com](http://www.excelhero.com/blogs/ "ExcelHero.com")

**Other Links to Sumproduct**
-----------------------------

[http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)

[http://chandoo.org/wp/2011/05/26/advanced-sumproduct-queries/](http://chandoo.org/wp/2011/05/26/advanced-sumproduct-queries/)

[http://chandoo.org/wp/tag/sumproduct/](http://chandoo.org/wp/tag/sumproduct/)

[http://www.excelhero.com/blog/2010/01/the-venerable-sumproduct.html](http://www.excelhero.com/blog/2010/01/the-venerable-sumproduct.html)

DOWNLOAD
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2011/12/Sumproduct.xls "Sumproduct Example File")
.

OTHER POSTS IN THIS SERIES
--------------------------

You can learn more about how to pull Excel Formulas apart and what makes them tick in the following post:

[Formula Forensic Series:](http://chandoo.org/wp/2011/10/31/using-array-formulas-to-find-count/ "Taruns problem")

FORMULA FORENSICS NEEDS YOUR HELP !
-----------------------------------

I am running out of ideas for Formula Forensics and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post as Luke did in Formula Forensics 003. or like above.

If you have a formula that you would like explained but don’t want to write a post also send it in to [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
 or [Hui](http://chandoo.org/wp/about-hui/ "Contact Hui")
.

XMAS BREAK
----------

This will be the last Formula Forensics Post for 2011, but rest assured that we will be returning in early 2012.

I’d like to take the opportunity to thank Chandoo for allowing me the space and freedom to post pretty much what ever I’ve wanted at Chandoo.org. I hope you have enjoyed my contributions to the Chandoo.org community over the past year.

On behalf of Eva and myself I’d like to wish you all a very **Merry Xmas** and a **Happy and Safe New Year** ahead

### _Hui…_

### [![Merry Xmas](https://chandoo.org/wp/wp-content/uploads/2011/12/Animated-Gif-Christmas.gif "Merry Xmas")](https://chandoo.org/wp/wp-content/uploads/2011/12/Animated-Gif-Christmas.gif)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [29 Comments](https://chandoo.org/wp/formula-forensics-no-007/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-no-007/#respond)
    
*   Tagged under [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sum()](https://chandoo.org/wp/tag/sum/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousJoin Excel School & Become Awesome in Excel Today!](https://chandoo.org/wp/join-excel-school-become-awesome/)

[NextMerry Christmas & Happy New Year 2012Next](https://chandoo.org/wp/merry-christmas-happy-new-year-2012/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-007/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-007/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-007/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ