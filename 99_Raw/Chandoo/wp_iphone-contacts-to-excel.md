# Export / import iPhone contacts to Excel workbook using this FREE template

**Source:** https://chandoo.org/wp/iphone-contacts-to-excel

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

Export iPhone contacts to Excel using this free template
========================================================

*   Last updated on December 2, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![Export iPhone contacts to Excel - FREE Template](https://img.chandoo.org/f/export-iphone-contacts-to-excel-howto.png)

Recently my iPhone 4 crashed. It is 3.5 years old. And just like any other 3 year old, it started acting weird & crazy one night. The next morning it went silent. It won’t go beyond the Apple logo whenever I start it. Since I couldn’t wait for the phone to start, I took out the SIM card (the phone is unlocked, if you are wondering) and placed it in my old Nokia phone. But alas, none of my contacts are on the SIM. They are in “cloud”.

After a day of answering phone calls from everyone including my mom as “Chandoo here”, I’ve decided to get my contacts back. So I logged in to iCloud to download a backup. And the backup was a .VCF file. It has my phone numbers in this format:

![Example VCF file format - how to export iPhone contacts to Excel](https://img.chandoo.org/f/sample-vcf-file-format.png)

Since I wanted to have all my contact numbers in a spreadsheet, I did what any Excel nerd would do. I built a template for that.

### Template for exporting iPhone contacts to Excel

As a first step, [**download the template**](https://img.chandoo.org/f/export-iphone-contacts-to-excel.xlsx)
.

This template can,

*   Export iPhone contacts to Excel
*   Create iPhone import format from a list of names & phone numbers in Excel

### Exporting contacts from iPhone to Excel

To export the contacts from your iPhone to Excel, follow below steps

1.  First back up all the contacts on your phone to iCloud
2.  Now, visit [iCloud](https://www.icloud.com/#contacts)
     and select **all** of your contacts.
3.  Using the settings gear icon at the bottom, export your contacts to a .VCF file.
4.  Open the vcf file in notepad & copy everything.
5.  Paste the data in Data column of “export” tab of the download file.
6.  Names & phone numbers will be extracted in column D:J
7.  Filter the table so no blanks are shown in Name column
8.  Copy the values from Name & phone number columns and paste in a separate sheet or file
9.  Save.

### Importing spreadsheet contacts to iPhone

To copy all your spreadsheet contacts to iPhone,

1.  Go to “Import” tab of the download file.
2.  Type or paste your contact information in the columns B,C & D.
3.  Select “VCF to copy” range (from H4 to last cell)
4.  Copy
5.  Open notepad and paste.
6.  Save the notepad file as contacts.vcf
7.  Import the VCF file to your iCloud
8.  Done

### Confused about the process? See this video

Since the process of exporting or importing contacts thru iCloud can be a little confusing, I made a small video explaining how the template works. See it below:  
([click here to see the video on our YouTube channel](http://youtu.be/IgAtuBcysBQ)
)

### How does the template work?

The vCard format files are simple text files. So when pasted in Excel, all we need to do is figure out where the contact name & phone numbers are and extract them using, _what else… Excel formulas._

**Exporting VCF to Excel:**

*   This uses [MATCH formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/ "How to Lookup Values to Left?")
     to find the line in VCF data that has the information we want.
*   Then [OFFSET formula](http://chandoo.org/wp/2012/09/17/offset-formula-explained/ "OFFSET formula – Explained")
     to extract the corresponding line of VCF data
*   And then [SUBSTITUTE](http://chandoo.org/excel-formulas/substitute.shtml)
    , [MID](http://chandoo.org/excel-formulas/mid.shtml)
    , [LEFT](http://chandoo.org/excel-formulas/left.shtml)
     & [TRIM](http://chandoo.org/excel-formulas/trim.shtml)
     formulas to extract the text portions

You can examine all these formulas by **unhiding columns C & K:Q** in the export tab of the template.

**Importing Excel data to VCF:**

*   This uses [INDEX formula](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/ "7 reasons why you should get cozy with INDEX()")
     to get a name & phone number from entered data.
*   Then uses [CHOOSE](http://chandoo.org/wp/2014/07/16/introduction-to-choose-function/ "CHOOSE() me, an introduction to Excel CHOOSE function")
     & SUBSTITUTE formulas to create the corresponding VCF lines
*   Finally [TODAY](http://chandoo.org/excel-formulas/today.shtml)
     & [NOW](http://chandoo.org/excel-formulas/now.shtml)
     formulas to create the timestamp element of the VCF

You can examine these formulas in **columns F,G & H in the import tab**.

### Do you like this template?

It was fun building something useful & immediate like this in Excel. Although, soon after I created the template, my iPhone magically sprung back to life, I will be ready next time I need to look at my contacts or load them to another phone.

**How do you like this template?** Would you use this or some other app to export / import your contacts? Please share your thoughts and tips using comments.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [26 Comments](https://chandoo.org/wp/iphone-contacts-to-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/iphone-contacts-to-excel/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [iphone](https://chandoo.org/wp/tag/iphone/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [left()](https://chandoo.org/wp/tag/left/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [mid()](https://chandoo.org/wp/tag/mid/)
    , [OFFSET()](https://chandoo.org/wp/tag/offset/)
    , [substitute()](https://chandoo.org/wp/tag/substitute/)
    , [templates](https://chandoo.org/wp/tag/templates/)
    , [text processing](https://chandoo.org/wp/tag/text-processing/)
    , [trim](https://chandoo.org/wp/tag/trim/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Templates](https://chandoo.org/wp/category/templates-2/)
    

[PrevPreviousCalculate Pi by throwing Frozen Hotdogs !](https://chandoo.org/wp/calculate-pi-by-throwing-frozen-hotdogs/)

[NextCreating In-cell charts with markers for average (or target) valuesNext](https://chandoo.org/wp/in-cell-charts-with-markers/)

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
    
    [Reply](https://chandoo.org/wp/iphone-contacts-to-excel/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/iphone-contacts-to-excel/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/iphone-contacts-to-excel/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ