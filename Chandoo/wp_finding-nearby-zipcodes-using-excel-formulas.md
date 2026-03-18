# Finding Nearby Zipcodes using Excel Formulas » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Finding Nearby Zipcodes using Excel Formulas
============================================

*   Last updated on March 18, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Finding nearby zipcodes using Excel 2013 Web formulas](https://img.chandoo.org/excel2013/find-nearby-zipcodes-using-excel-formulas.png)

Recently, I had a peculiar problem. _**I have a list of zip codes and I wanted to find out nearest zip codes for each of them.**_

Now, If I wanted to find out near by zip codes for one area, I could go and search in Google. But, how to do it for dozens of them?

**Today, lets understand how you can use Excel (that’s right) to do this automatically**. We will be using Excel 2013 for this.

![Excel 2013 Web Formulas - an overview](https://img.chandoo.org/excel2013/excel-2013-web-formulas.png)

### A little background – Excel 2013 Web Formulas

In Excel 2013, Microsoft has introduced 3 powerful new formulas. These will help you fetch & parse XML / HTML data from web. The formulas are,

*   ENCODEURL: to encode web URLs (replaces special characters in URLs with % codes like space becomes %20, / becomes %2F etc…)
*   WEBSERVICE: connects to a webservice / website and fetches response as XML / HTML.
*   FILTERXML: extracts a portion of XML/HTML using specified XPATH.

Using these formulas and web services, we can quickly fetch near by zipcodes for any input value.

### Step 1: Find a web-service that can tell us near by zipcodes

I am sure there are many web sites that can offer a service like this. After searching a while, I came across a website called as **geonames.org** which has many webservices around address / zip code search. The service I have used is,

_[Find nearby postal codes](http://www.geonames.org/export/web-services.html#findNearbyPostalCodes)
._

This service is available as XML & JSON. Since Excel 2013 formulas only process XML data, I went with XML service. The service API url is this:

http://api.geonames.org/findNearbyPostalCodes?postalcode=ZIPCODE&country=US&radius=15&username=UNAME&maxRows=10

ZIPCODE is where you enter the zipcode from which you want to find nearby zipcodes

UNAME is where you enter your user name for geonames.org. [Click here to register with geonames.org](http://www.geonames.org/login)
.

### Step 2: List all original Zip codes in a column

This is simple. Just paste all original zip codes in a column.

### Step 3: Write WEBSERVICE Formula

First enter the API URL in a cell like B1. (Make sure your user name is included in the service url)

Now write WEBSERVICE formulas so that we can fetch XML listing for each of the zip codes. Assuming zip codes are in A3:Ax, in adjacent column write =WEBSERVICE(SUBSTITUTE($B$1,”ZIPCODE”,A3))

And drag it down to fill down the formula for all zipcodes.

### Step 4: Write FILTERXML formulas

Now that we have full XML corresponding to each zip code, we need to parse this XML to extract the nearby zip code numbers. The original XML looks something like this:

![XML output provided by geonames.org - Finding nearby zip codes using Excel 2013 Web formulas](https://img.chandoo.org/excel2013/xml-provided-by-geonames.png)

To extract the zipcodes alone, we need to use FILTERXML formula.

FILTERXML takes 2 inputs – XML text, Xpath.

XML text is what WEBSERVICE has generated.  
XPATH will tell Excel, which portion of XML to extract.

**What is XPATH?**

If you imagine XML as a tree, then XPATH is the language you use to tell how to navigate to a certain node in that tree. Since XPATH is a complex world, I think explaining all the syntax & nuances can be hard. So I will leave you with 2 useful links.

*   [What is XPATH and how to use it – Wikipedia](http://en.wikipedia.org/wiki/XPath)
    
*   [XPATH examples & simulator – W3Schools](http://www.w3schools.com/xpath/)
    

**So what is the XPATH for nearby zip code.**

As you can see in above image, the response from geonames has 10 code nodes, each containing one zip code (in the postalcode child node).

If we write =FILTERXML(b3,”/geonames/code/postalcode”) we will get all the postalcodes as an array.

_Since Excel cannot show arrays in cells, it will show one of the 10 values._

So we need 10 cells to show these 10 zip codes. Once you have 10 cells, you can use either INDEX formula or alternative XPATH syntax (/geonames/code\[1\]/postalcode for first code, ../code\[2\]/.. for second code etc.) to extract all the 10 zip codes.

### Things to keep in mind

Web formulas (WEBSERVICE formula to be specific) can be really slow depending on your net connection and webserver speeds. Since for most data, we do not need a live connection once the data is fetched, it would be good idea to replace WEBSERVICE formula with results once you have the XML.

Also, working with XPATH can be frustrating if the source XML is not correctly formatted or you are not familiar with right XPATH commands. In such cases, use SUBSTITUE or Text formulas to strip away un-necessary portions of webservice text before feeding it to FILTERXML.

Last but not least, Web formulas are compatible only with Excel 2013 or above. So you need to replace all formulas with results when emailing the workbooks to colleagues who are using older versions of Excel.

### Download Example File – Finding Nearby Zipcodes

[**Click here to download the Excel workbook**](https://img.chandoo.org/excel2013/nearby-zipcodes.xlsx)
. Play with it to understand how the formulas are working. Please note that this file is protected as I do not want you to use my username for geonames.org.

### Do you use Excel Web formulas?

Although Excel 2013 includes only 3 web formulas, they can let us do several interesting things. I am playing with them often to see what additional uses we can put them to.

**What about you?** Have you used Excel 2013 web formulas? What is your experience like? Please share using comments.

### More on using Excel to get data from web

If you often need data from external websites for your Excel analysis work, check out below articles too:

*   [Fetching stock quotes from Yahoo Finance using Excel & VBA](http://chandoo.org/wp/2010/06/02/excel-stock-quotes/)
    
*   [Using REST API from Excel VBA – Posting to Twitter (deprecated)](http://chandoo.org/wp/2009/02/05/twitter-from-excel/)
    
*   [Using web formulas in Google Spreadsheets to monitor product prices in Amazon](http://www.labnol.org/internet/monitor-web-pages-changes-with-google-docs/4536/)
     \[Guest post on Labnol.org\]

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [20 Comments](https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [encodeurl()](https://chandoo.org/wp/tag/encodeurl/)
    , [excel 2013](https://chandoo.org/wp/tag/excel-2013/)
    , [excel web services](https://chandoo.org/wp/tag/excel-web-services/)
    , [filterxml()](https://chandoo.org/wp/tag/filterxml/)
    , [geonames.org](https://chandoo.org/wp/tag/geonames-org/)
    , [web queries](https://chandoo.org/wp/tag/web-queries/)
    , [webservice()](https://chandoo.org/wp/tag/webservice/)
    , [xml](https://chandoo.org/wp/tag/xml/)
    , [xpath](https://chandoo.org/wp/tag/xpath/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousHow to remove all cells containing John (or anything else) \[Quick tip\]](https://chandoo.org/wp/remove-all-rows-with-specific-value-excel/)

[NextHow well do you know your Lookups? \[Quiz\]Next](https://chandoo.org/wp/how-well-do-you-know-your-lookups-quiz/)

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
    
    [Reply](https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/finding-nearby-zipcodes-using-excel-formulas/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ