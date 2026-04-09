# Interview with John Walkenbach on Excel

**Source:** https://chandoo.org/wp/interview-john-walkenbach

---

*   [blogging](https://chandoo.org/wp/category/blogging/)
    , [interviews](https://chandoo.org/wp/category/interviews/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Interview with John Walkenbach on Excel and Banjo Charts…
=========================================================

*   Last updated on March 27, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![John Walkenbach](https://i287.photobucket.com/albums/ll133/pointy-haired-dilbert/john-walkenbach.jpg)Here is the interview with John Walkenbach. John is famous excel personality. He has authored 50 excel books, numerous articles and has one of most popular excel related sites – [spreadsheetpage](http://spreadsheetpage.com/)
.

PS: Thanks to PHD readers for [suggesting interview questions to ask John](http://chandoo.org/wp/2009/02/23/johns-walkenbach-interview-questions/)
. I really appreciate your help in putting this together. Unfortunately, I couldnt ask all the questions, but I have included as many as possible.

**Q: Excel 2003 or 2007?**

I have both versions installed on my system. I keep 2003 around only to answer questions that are specific to that version. Although it has some problems, I much prefer Excel 2007. A lot of it is aesthetic. Excel 2007 looks good, Excel 2003 doesn’t. And besides, I have a difficult time remembering where the commands are located on the 2003 menu system.

**Your 3 favorite formulas?**

I hate these kinds of questions. My favorite formula is the one that gets the job done — so it changes all the time. But if you ask what is the most impressive formula I’ve ever written, it would be that [multicell array formula that displays a calendar for any month](http://spreadsheetpage.com/index.php/file/array_formula_calendar/)
. I spent hours working on that one. Click on the link to see it.

If I were going to be buried, I would like that formula inscribed on my tombstone. But it would probably be inscribed wrong, and everyone would wonder why the formula on my tombstone produces a #NAME! error.

**Which books / resources would you recommend for an excel newbie, excel intermediate user and excel pro?**

I can only recommend my own books because I’ve never read any other Excel books. I’ve paged through a few, but I’ve actually never read one. So…

_Newbie:_ [Excel Bible](http://www.amazon.com/gp/product/0470044039?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0470044039)
![](https://www.assoc-amazon.com/e/ir?t=poinhairdilb-20&l=as2&o=1&a=0470044039)

_Intermediate:_ [Excel Bible](http://www.amazon.com/gp/product/0470044039?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0470044039)
![](https://www.assoc-amazon.com/e/ir?t=poinhairdilb-20&l=as2&o=1&a=0470044039) and/or [Excel Formulas](http://www.amazon.com/gp/product/0470044020?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0470044020)
![](https://www.assoc-amazon.com/e/ir?t=poinhairdilb-20&l=as2&o=1&a=0470044020)

_Pro:_ [Excel Formulas](http://www.amazon.com/gp/product/0470044020?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0470044020)
![](https://www.assoc-amazon.com/e/ir?t=poinhairdilb-20&l=as2&o=1&a=0470044020) and/or [Excel Power Programming With VBA](http://www.amazon.com/gp/product/0470044012?ie=UTF8&tag=poinhairdilb-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0470044012)
![](https://www.assoc-amazon.com/e/ir?t=poinhairdilb-20&l=as2&o=1&a=0470044012)

**Is there a point in learning excel, in the era of web spreadsheets and powerful drag-and-drop analytical apps?**

Absolutely. Excel is going to be with us for a long time. Count on it.

**Excel is great – we would all agree – but what is the worst & best use of Excel you have seen?**

I’m of the opinion that there is no “bad” use for Excel. If you do something that’s not normally done in Excel — and it works and is adequately scalable for your needs — that’s great. It’s certainly possible that more efficient methods exist, but that needs to be balanced with the time need to learn how to use those more efficient methods. For example, I keep my customer data in an Excel workbook. Probably 90% of the experts would tell me to use Access or some other database software for this application. But it works just fine for me, and it means I don’t have to spend time learning to be proficient in Access.

**What is the future of Excel & spreadsheet software?**

I have no idea. I don’t spend much time thinking about such things. Microsoft often surprises me with what that put into Excel. But they also frustrate me by not doing things that they should have done years ago. It’s nice that Excel is finally getting some competition once again, in the form of open source and online spreadsheet apps.

**How did you learn to write such clear and easy to understand code?**

I had a few programming courses in college, but I don’t think they really helped much in terms of what I do today. I think I just have a knack for putting myself in the shoes of others, and explaining things as clearly and concisely as possible. My writing is based on two guiding principles: Keep it simple, and teach through illustrative examples that can be expanded upon by the reader.

When Excel 5 came out, I was excited about the VBA programming language, so I gave myself an assignment to learn it: Write a set of Excel utilities. And that was PUP 1.0. The first version was loosely based on the XLM-based “Barnes Utilities.” PUP is now in version 7, and I’m still learning things.

**Your tips for people learning VBA?**

Start with something simple, but also meaningful to you. Then, gradually expand it — testing at every step of the way.

When you need to use an unfamiliar property or method, create a small “experimental” procedure for testing. Play around with it until you’re comfortable. Then incorporate it you’re your actual project.

You should also take the time to learn how to use tools such as the Object Browser, the Immediate Window, and Step mode. And always declare your variables.

**When trying to display a simple dot using shapes, I only found the “msoval” object to do this, but with poor results… is there a hidden “dot” object in VBA ?**

This seems to work OK:

Sub MakeDot()

Dim Dot As Shape

Set Dot = ActiveSheet.Shapes.AddShape(msoShapeOval, 20, 20, 4, 4)

With Dot

.Fill.ForeColor.SchemeColor = 8

.Line.Visible = msoFalse

End With

End Sub

**Is there a way to add tooltips to shapes (when mouseover for example ?) ?**

Not officially, but you can sort of fake it.

Create the shape. Then run a VBA procedure that assigns an empty string to the shape’s Hyperlink.Address property, and specifies a ScreenTip for the hyperlink. For example:

Sub SetTootipForShape()

Dim s As Shape

Set s = ActiveSheet.Shapes(1)

s.Hyperlink.Address = ""

s.Hyperlink.ScreenTip = "This shape has a tooltip"

End Sub

When the mouse pointer moves over the shape, the tooltip appears. Clicking the shape has no effect.

Note that you cannot assign an empty string manually, via the Hyperlink dialog box.

**Are you still cold-brewing coffee? If not, how come?**

Off and on. I broke my original cold brew glass jar, so that put an end to it for a while. Then I bought another one and used it for a while. I’ll probably go back to it at some point, just because it’s so convenient to have fresh-tasting coffee without having to brew a pot.

**When will we see the introduction of the “banjo” chart in Excel?**

As soon as Jon Peltier stops writing about charts. He would certainly disapprove of a banjo chart because of its resemblance to a pie chart. For people who don’t read my [J-Walk Blog](http://j-walkblog.com/)
… I’ve become obsessed with learning old-time clawhammer style banjo during the past three years.

**Your tips for bloggers of the world**

I have nothing new to add. Just same old stuff: Post a lot, understand your readers, pay attention to layout and design, go easy on the ads, avoid all of those useless widgets, and don’t take yourself too seriously.

**Your advice for people who make excel add-ins, excel based products.**

I think the most common question I get from would-be add-in programmers is: “How can I protect my work so it won’t be stolen.” The answer is, you can’t. There will always be people who want to steal your work, and they will. But, for the most part, these people would not have purchased your product anyway. With my PUP add-in, I make the VBA code available for a small fee. Amazingly, I haven’t seen any other commercial add-ins that have incorporated my code. They might exist; I just haven’t seen them.

**Thank you John for your informative and entertaining interview.  
**

### **Tell me who else should be interviewed and I will ask them.**

Also, Read our earlier [interview with Charley Kyd](http://chandoo.org/wp/2008/12/11/charley-kyd-interview-excel/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/interview-john-walkenbach/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/interview-john-walkenbach/#respond)
    
*   Tagged under [blogging](https://chandoo.org/wp/tag/blogging/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [excel books](https://chandoo.org/wp/tag/excel-books/)
    , [interviews](https://chandoo.org/wp/tag/interviews/)
    , [john walkenbach](https://chandoo.org/wp/tag/john-walkenbach/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [blogging](https://chandoo.org/wp/category/blogging/)
    , [interviews](https://chandoo.org/wp/category/interviews/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousUsing Array Formulas in Excel – Find if a list has duplicate items](https://chandoo.org/wp/using-array-formulas-example1/)

[NextSearch a Spreadsheet Full of Data using Conditional FormattingNext](https://chandoo.org/wp/search-with-conditional-formatting/)

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
    
    [Reply](https://chandoo.org/wp/interview-john-walkenbach/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/interview-john-walkenbach/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/interview-john-walkenbach/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ