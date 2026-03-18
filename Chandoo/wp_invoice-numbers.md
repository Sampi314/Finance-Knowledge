# Generating invoice numbers using excel [reader questions] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/invoice-numbers

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Generating invoice numbers using excel \[reader questions\]
===========================================================

*   Last updated on July 19, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**Michelle**_, Who is a sweet lady and regular reader of the blog sent me this question via e-mail. (**aside: why is she a sweet lady?** Because she saw [the new cell post](http://chandoo.org/wp/2009/06/18/dad-dad-dad/)
 and sent me pics of her son and told Jo and me are about to encounter most amazing experiences of our lives 🙂 )

> I handle the invoices we give to our customers (we build and sell furniture), but sometimes such customers can be stores or just regular folks that come directly to us.
> 
> For the stores I have to give an invoice that has a NCF number which is a tax related number that increases the cost in 16% but stores require this number which must be unrepeatable. Each company has a “list” of numbers that they can provide their customers. Regular customers (not stores) have no interest in this number, obviously trying to avoid the 16% increase in the price!
> 
> So far what I did was create a database of our customers with the basic info of each one. Many of our customers keep buying so this way I just have to place myself in the invoice and select from a list and with a simple vlookup I get the rest of the customer’s information: phone, address and RNC number.
> 
> Now… the RNC is the number that tells me if it’s a store or not. Stores must have their registration number (RNC) in order to receive invoices with NCF (boring, I know… I’m gonna get to the point in a sec). Ok, so if I choose my dear customer “Chandoo Enterprises” and this store has RCN, then I automatically need for the invoice to pull form “my list” of government assigned NCF numbers, the next one in line. If in my previous invoice (say invoice 1455) to another store I used NCF number A010010010100000002 (that’s how they look) for Chandoo Enterprises -invoice #1456- I am going to need the next number in line A010010010100000003 and so on. Now, say that my next invoice (1457) is not to a store but to John Doe, for him I don’t want an NCF number to show.
> 
> I keep thinking that there’s a very stupid and simple way to do this but I just can’t nail it!! My problem is to get to a formula that will work only when the RNC field has information and therefore avoiding NCF numbers to appear on non-store customers (not so complicated I think) and that it chooses the next NCF number in line, no repeating… this is the part that I have no idea how to do!! Is there a way to solve this without using VBA? VBA is scary!! Hehehe

Okay, that is a big question, but may be we can come up with a small solution for it.

![Invoice Numbers in Excel](https://chandoo.org/img/l/invoice-numbers.gif)If I understand it correct, Michelle is looking for something like this:

**So, in order to generate such numbers,**

1.  First we will make 2 named ranges – customer\_list and ncf\_numbers. You know what they mean.
2.  Now, we will enter the customer name in column B, and based on that we will fetch RNC number in column C.
3.  For this, we will use [VLOOKUP () formula](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    . The simplest formula looks like this: VLOOKUP(B5,customer\_list,4,FALSE)
4.  But, simplest formula also has problems – it doesn’t handle errors and can return 0 when the RNC number field is blank. So we will add some fat to it, mainly on the front side. It now looks like this: =IF(ISERROR(VLOOKUP(B5,customer\_list,4,FALSE)),””, VLOOKUP(B5,customer\_list,4,FALSE))
5.  In the third column, we will fetch the next available NCF number if the customer has an RNC. For this, we use a simple [IF()](http://chandoo.org/wp/2008/06/09/what-the-if-learn-6-cool-things-you-can-do-with-excel-if-functions/)
     and [COUNTIF() formulas](http://chandoo.org/wp/2008/11/12/using-countif-sumif-excel-help/)
     along with INDEX() formula. We write: =IF(OR(C5=””,C5=0),””,INDEX(ncf\_numbers,COUNTIF($C$5:C5,”RNC\*”))).
6.  Above formula simple fetches the nth NCF number from the named range ncf\_numbers if RNC number is not blank.
7.  That is all.  We now have a simple logic to generate invoice numbers that suit tax authority’s whims and fancies.

### Download the example workbook:

You can [download the excel tutorial workbook](http://chandoo.org/img/l/excel-invoice-numbers-tutorial.xls)
 and see how you can generate such invoice numbers yourself.

### More material if you are getting stuck with formulas

[50+ Excel Formulas – Explained in plain English](http://chandoo.org/excel-formulas/)
, [Excel formula tutorials](http://chandoo.org/wp/tag/formulas/)
, [Excel array formula examples](http://chandoo.org/wp/tag/array-formulas/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [17 Comments](https://chandoo.org/wp/invoice-numbers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/invoice-numbers/#respond)
    
*   Tagged under [countif()](https://chandoo.org/wp/tag/countif/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [examples](https://chandoo.org/wp/tag/examples/)
    , [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [invoice numbers](https://chandoo.org/wp/tag/invoice-numbers/)
    , [iserror()](https://chandoo.org/wp/tag/iserror/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MS](https://chandoo.org/wp/tag/ms/)
    , [named ranges](https://chandoo.org/wp/tag/named-ranges/)
    , [OR() excel formula](https://chandoo.org/wp/tag/or-excel-formula/)
    , [reader questions](https://chandoo.org/wp/tag/reader-questions/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [tutorial](https://chandoo.org/wp/tag/tutorial/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious2 Great Pieces of Advice for Chart Makers, Dashboard Designers and Story Tellers Everywhere](https://chandoo.org/wp/charting-advice/)

[NextUse burn down Charts in your project management reports \[bonus post\]Next](https://chandoo.org/wp/burn-down-charts/)

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
    
    [Reply](https://chandoo.org/wp/invoice-numbers/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/invoice-numbers/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/invoice-numbers/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ