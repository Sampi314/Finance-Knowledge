# Can pivot tables save your job? | Exceljet

**Source:** https://exceljet.net/articles/can-pivot-tables-save-your-job

---

[Skip to main content](https://exceljet.net/articles/can-pivot-tables-save-your-job#main-content)

[](https://exceljet.net/articles/can-pivot-tables-save-your-job#)

*   [Previous](https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before)
    
*   [Next](https://exceljet.net/articles/pivot-table-tips)
    

Can pivot tables save your job?
===============================

by Dave Bruns · Updated 18 Jun 2024

![Keep or cut?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/keep_cut7.png "Keep or cut?")

Summary
-------

This article is for those of you who don't get pivot tables. Maybe you tried pivot tables once, and didn't see what the big deal was, or maybe you got frustrated when a pivot table wouldn't behave. They can be that way.

> [Overview](https://exceljet.net/articles/excel-pivot-tables)
>  | [Why Pivot?](https://exceljet.net/plc/why-pivot-tables)
>  | [Story](https://exceljet.net/articles/can-pivot-tables-save-your-job)
>  | [Examples](https://exceljet.net/pivot-tables)

This article is for those of you who don't get pivot tables. Maybe you tried pivot tables once, and didn't see what the big deal was, or maybe you got frustrated when a pivot table wouldn't behave. They can be that way.

I'm not going to mince words. If you use Excel on a regular basis, you need to know how to use pivot tables. Period. I'll get to some good reasons below, but first, a quick story.

When I first learned pivot tables in the late 1990s, I was working as a manager for a medium sized (US $50M) company in the translation industry that was going through a major restructuring. My boss, who had hired me 3 months earlier, had done his part in the restructuring, personally laying off about 30 people one dark week in November. A big wig from Singapore was in town, and they actually sat together in the main conference room and called people up over the PA system. It was brutal. All week, people filed past my office to the conference room, and came back stunned and upset, many in tears.

At the end of the week, the company repaid my boss for handling that miserable job by laying _him_ off too. You gotta love corporate America.

> Looking for good tips? See [23 things you should know about pivot tables](https://exceljet.net/articles/pivot-table-tips)
> .

### What's this got to do with pivot tables?

Yes, let's get to that. The upshot of my boss being suddenly sacked was that I was "promoted" to a new role, running an office with about $10M of annual revenue running through it, with less than half the original staff, most of whom were now supposed to play different roles in the company (with no job descriptions, naturally). The remaining staff were not, as you might expect, completely trusting of the company at that point. Beyond ordinary chaos, there was a deep current of fear running through the office. People thought it was just a matter of time before the axe dropped on them.

More on that in a minute...

In the meantime, of course, there was work to do. We had sales people selling new jobs, we were just starting the largest project we'd ever tackled: a 25-language job for a large computer company with a budget well over $1M. And we had lots of jobs already in progress.

As the manager, I was responsible for submitting sales forecasts, recognizing revenue on existing projects, estimating invoicing, knowing what jobs were won and lost, knowing who my top customers were, and making sure existing projects came out ok.

We had no integrated systems of any kind. No CRM system, no way to forecast sales, no project tracking app, nothing.

Luckily, I had my trusty Toshiba laptop (a brick, but running NT, thankfully, not Windows 95), and I had just discovered pivot tables. After a few very frustrating early weeks (pivot tables were quite delicate at the time and fell apart at the slightest provocation), I realized that if I could just get together the right data, I could use pivot tables to generate any report I needed for myself or my management. And, a few months later, that's just what I did.

### Pivot tables give you answers

At the most basic level, pivot tables answer important questions. For example, assume you're working with a company that sells chocolate to retailers and have some sales data that looks something like this:

![Sample chocolate sales data](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_question0.png "Sample chocolate sales data")

Here are some questions that might be going through your mind:

*   What are my best-selling products?
*   Who are my biggest customers?
*   Where are my sales coming from?
*   What are product sales by year?
*   What are customer sales by year?

In about 5 minutes, here are the answers a pivot table can give you:

![What are my best selling products?](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_question1.png "What are my best selling products?")  
_Your top selling products_

![Who are my biggest customers?](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_question2.png "Who are my biggest customers?")  
_Your biggest customers_

![Where are my sales coming from?](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_question3.png "Where are my sales coming from?")  
_Where sales are coming from_

![What are product sales by year?](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_question4.png "What are product sales by year?")  
_Product sales by year_

![What are customer sales by year?](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_question5.png "What are customer sales by year?")  
_Customer sales by year_

Notice that total sales ($278,470) is the _same_ in all pivot tables. Each table presents a different view of the same data, so they all sum to the same number.

So, first and foremost, a pivot table can help you answer questions you have about your data. And in Excel, there is no better tool for this job.

### Pivot tables are incredibly fast

Some of you might be thinking: "I could build that summary myself, without pivot tables". Yes, it's true. If you have the formula chops to do it, _you could_ create those same reports manually. However, it's going to take you a lot more time.

In his book, [Excel 2013 Pivot Table Data Crunching](http://www.amazon.com/gp/product/0789748754/?tag=exceljet-20)
, Mr. Excel Bill Jelen looks at this very question in detail with _one_ pivot table. With expert skills, he manually builds a basic summary of product sales by region. He concludes:

_It took 77 clicks or keystrokes. If you could pull all this off in 5 or 10 minutes, you would probably be fairly proud of your Excel prowess — there were some good tricks among those 77 operations._

Then, he contrasts this with a pivot table approach: a few clicks and done. Watch the video below to see a side-by-side demo of formulas versus pivot tables. No matter how fast you are in Excel, a pivot table will beat you every time.

> Video: [Formulas vs. Pivot Tables](https://exceljet.net/plc/why-pivot-tables)

### Pivot tables don't require formulas

That's right. Pivot tables don't require any formulas at all. Not just a few formulas, but zero formulas. Basically, if you can click and drag with a mouse, you can build a pivot table.

To illustrate how truly powerful this is, let's do something really hard with our pivot table. Let's group all the orders in the sales data we just looked at into buckets according to the size of the order. That is, we want to see a breakdown of all sales small and large orders.

In a couple of minutes, we have a breakdown of orders by order total. This is cool, but useless, because there's way too much data here:

![Ungrouped and useless, sales by order total](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/ptcase_no_formulas1a.png?itok=ue8M4YFl "Ungrouped and useless, sales by order total")

However, using the built-in group by feature, we can ask Excel to group the orders into buckets of $100. When we click OK, we have a new layout that does this grouping for us perfectly:

![All sales, cleanly grouped by order value](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_no_formulas2.png "All sales, cleanly grouped by order value")

This summary tells us that out of almost 3000 orders, 2106 orders are less than $100, and only 12 orders are greater than $1,000.

Now, consider the formulas it would take to create this kind of report manually. Believe me, they aren't going to be pretty. Even if you eventually work it out, you won't understand what they do after a few weeks.

Which brings us to our next point.

### Pivot tables don't make mistakes

![The Excel formula error that ruined the global economy?](https://exceljet.net/sites/default/files/images/articles/inline/excel_ruiner_ars_technica2.jpg "The Excel formula error that ruined the global economy?")

Have you ever felt the stress of worrying that your worksheet might contain errors? Maybe you've had the unpleasant experience of presenting a report to your management only to have someone find a simple mistake in one of your formulas, casting a shadow on the entire worksheet (and you)?

If so, you're not alone. These kinds of errors happen all the time, even to pros. Perhaps you read about the [spreadsheet mistake that may have impacted the global economy](http://arstechnica.com/tech-policy/2013/04/microsoft-excel-the-ruiner-of-global-economies/)
? It was a basic error. A formula that was supposed to average values for twenty countries only averaged values in 15 countries. So, instead of AVERAGE(L30:L49), the formula said AVERAGE(L30:L44). This is the kind of "silent" problem that can come back to haunt the author of a spreadsheet.

So, how does this relate back to pivot tables? Like this: because pivot tables don't require you to write formulas, there's no chance to mess one up. Your only job is to make sure the source data is correct. The pivot table takes care of the rest.

When you work with pivot tables, Excel handles 100% of the calculations and formatting for you. Whether you're working with 100, 1,000, or 100,000 rows of data, you know the results will be accurate.

### Pivot tables make you look good

You've probably noticed by now that formatting things in Excel to look good is tricky and time-consuming. And when your boss or client wants to see the report configured differently, you're back to square one, clearing and re-applying formatting.

Pivot tables are different. All of the formatting they apply is clean and automatic.

For example, let's look at this plain pivot table with minimal formatting:

![A plain pivot table without formatting](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_formatting1.png "A plain pivot table without formatting")  
_A plain pivot table without formatting_

With a few clicks, we can transform the entire table into a pro-level report:

![The same pivot table after applying a built-in style](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_formatting2.png "The same pivot table after applying a built-in style")  
_The same pivot table after applying a built-in style_

Now, if you need to rearrange the table to show cities instead of products, that's no problem. Excel automatically clears and replies formatting each time it's changed, without any effort by you:

![A new layout, but all formatting is automatically applied](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_formatting3.png "A new layout, but all formatting is automatically applied")  
_A new layout, but all formatting is automatically applied_

When you use pivot tables, you get a perfectly formatted report every time.

### Pivot tables are a great tool for prototyping

Sometimes, you don't know exactly what you need, given the data you've got to work with. A pivot table allows you to experiment fluidly. You can quickly try out different layouts until you find what you need. In fact, for just this reason, pivot tables are an awesome prototyping tool.

For example, maybe you're supposed to tell IT what kind of report your boss needs for quarterly sales because they need to code it into a web app they manage. Using a pivot table and some sample data, you start off by adding the product and sales to your pivot table:

![Step one: add products](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_proto1.png "Step one: add products")

Next you add in the date, then group by year and quarter:

![Step two: group by year and quarter](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_proto3.png "Step two: group by year and quarter")

Not bad, but this report is too wide. Maybe quarters would work better in rows?

![Step three: move quarter to rows](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_proto4.png "Step three: move quarter to rows")

This will work. Now you have something you can send to the IT guys to show them exactly what they need to build.

Pivot tables are an excellent prototyping tool. They help you understand what data you need to collect and how to present it effectively without long delays and expensive development costs.

### Pivot tables can analyze all kinds of data, not just sales data

If you look at the pivot table examples on the web, you'd think that the only thing a pivot table is good for is sales data. Not true. You can use a pivot table to analyze any kind of tabular data.

For example, Let's say you just got an employee list from HR and need to create a simple breakdown by department. Here's the data:

![Employee data](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_department1.png "Employee data")

You look at it and realize you can just push it through a pivot table. A minute later, here's your breakdown by department.

![Employee data by department in a pivot table](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_department2.png "Employee data by department in a pivot table")

Let's look at another example. Maybe you work in residential real estate and export a list of 200 properties in a certain location. The data looks like this:

![Raw property listing data](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_property0.png "Raw property listing data")

What you want to see is the number of properties that are sold, pending, and for sale. You also want to see the total value of these properties.

30 seconds later, you've got your summary:

![Property listings summarized in a pivot table](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_property1.png "Property listings summarized in a pivot table")

Do you see the pattern? You start off with raw data, most likely collected by a system of some kind. You pour it into a pivot table, Excel crunches through the data in about, oh, 1 second, and out jumps the essential truths about the data, i.e. the things you need to know.

### Pivot tables are easy to update

In the real world, data is always changing.

Unlike most other tools in Excel, pivot tables do not update automatically. This sometimes puzzles new users. They make a change in the source data, check the pivot table, and...nothing. To update a pivot table, you need to refresh the data. Once you start to "get" pivot tables, you'll realize that refreshing the data is the best part about pivot tables, because it's the moment when Excel does _a lot_ of work for you.

To illustrate, let's go back to the property-listing example. You have your summary of 200 properties, but you adjust your search a month later, run another data export, and end up with a bigger list that contains 281 properties.

To update your report, here's what you do. First, you paste over the data you collected previously. Because the data sits in an Excel table, the table range automatically adjusts to include the 81 new properties. Next, you refresh your pivot table, and you're done. Here's the result:

![Updated property listings in a pivot table](https://exceljet.net/sites/default/files/images/articles/inline/ptcase_property2.png "Updated property listings in a pivot table")

Once you've set up a pivot table, you can easily update the data at any time. All changes in the data will be reflected in the pivot table, without any work on your part.

### Summary

Hopefully, I've managed to convince you that pivot tables are a skill you need to know. As the single most powerful feature in Excel, they help you do the following:

1.  Answer key questions
2.  Work incredibly fast
3.  Avoid mistakes
4.  Build beautiful reports
5.  Quickly prototype reports
6.  Handle changes with grace
7.  Keep your job

Oh yeah. You probably want to know how the restructuring turned out :)

So, in the end the restructuring was a disaster. Senior management "bet the farm" on a radical idea inspired by the frothy internet start-ups of that era, and they lost, big-time. It took a couple of years, but eventually they ran the company out of money and up on the rocks. During that time, I had to downsize almost every quarter. Finally, a competitor in the UK bought our company at a fire-sale price and initiated their own brutal restructuring (but with a pleasant English accent). By the time that was done, I was the last person from the original office still around.

I won't say that pivot tables saved my job. It's not quite that simple. But I do think they played a big role. Because I had key business information for the office in a collection of pivot table reports, I could review these reports with my team, and management at any time. The pivot tables were honestly the only way I was able to understand and communicate what was going on during that crazy period of my career. Without them, I couldn't have done it.

> Want to learn more about pivot tables? We have [video training](https://exceljet.net/training)
> .

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Articles

*   [Pivot Table Tips](https://exceljet.net/articles/pivot-table-tips)
    
*   [5 pivot tables you probably haven't seen before](https://exceljet.net/articles/5-pivot-tables-you-probably-havent-seen-before)
    

### Training

*   [Core Pivot](https://exceljet.net/training/core-pivot)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)