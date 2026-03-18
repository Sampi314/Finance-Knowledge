# Learn SQL for Data Analysis in one hour » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/learn-sql-for-data-analysis

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [SQL](https://chandoo.org/wp/category/sql/)
    

Learn SQL for Data Analysis in one hour
=======================================

*   Last updated on June 6, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

SQL (Structured Query Language) is one of the most important skills for us, data people. So in this article + video, get the _**necessary SQL skills**_ you need for Data Analysis work.

Step 0: Install MySQL software
------------------------------

![Install MySQL](https://chandoo.org/wp/wp-content/uploads/2022/08/SNAG-2245.png)

I am using the FREE MySQL Community Edition software to learn & practice SQL at home. [You can get it from here](https://dev.mysql.com/downloads/installer/)
.

If you have any other database software available (such as SQL Server or Oracle), you can use them to follow this tutorial.

Step 1: Import Awesome Chocolates Dataset
-----------------------------------------

![Awesome Chocolates Dataset](https://chandoo.org/wp/wp-content/uploads/2022/08/SNAG-2244.png)

You need some data to practice SQL. So I prepared a sample dataset for a fictional (but yummy) company called **Awesome Chocolates**.

[Download the .SQL file from here](https://files.chandoo.org/sql/awesome-chocolates-data.sql)
.

After you have the file, 

0.  Open MySQL Workbench, login if necessary
1.  Click on the “server administration” tab (see illustration, click to expand)
2.  Click on “Data Import/Restore”
3.  Select the option “Import from self-contained file”
4.  Specify the path of the downloaded awesome-chocolates-data.sql file
5.  Start import

[![Steps to import SQL file to MySQL workbench](https://chandoo.org/wp/wp-content/uploads/2022/08/SNAG-2243.png)](https://chandoo.org/wp/wp-content/uploads/2022/08/SNAG-2243.png)

At the end of these steps, your MySQL should have _the **awesome chocolates** database._ Congratulations 🎉🥳

You can see this from “Schemas” tab on the workbench

Using SQL Server?
-----------------

You can also use SQL Server to practice SQL. If you are using SQL Server Management Console, then follow below steps to import the data.

1.  [Download this SQL Server Backup file](https://chandoo.org/wp/wp-content/uploads/2023/06/ac-sql-server-backup.zip)
    
2.  Unzip the file
3.  Open SSMS & right click on the databases and chose “Restore Database” option. Follow the steps on that screen using below screenshots.

![Restore Database - SQL Server Management Console](https://chandoo.org/wp/wp-content/uploads/2023/06/SNAG-2680.png)

![Steps to restore a database from backup in SQL Server](https://chandoo.org/wp/wp-content/uploads/2023/06/SNAG-2681.png "Steps to restore a database from backup in SQL Server")

Step 2: Learn SQL for Data Analysis with this video
---------------------------------------------------

Everything is ready. Time to learn SQL.

I made an hour long tutorial to explain all the necessary SQL concepts for you. In this video, you will learn:

*   How to use SELECT statement to answer business questions
*   Working with WHERE clause
*   Using AND, OR, NOT and combining them to create complex queries.
*   Sorting query results using ORDER BY
*   Combining data from two or more tables using JOINS
*   Creating reports with GROUP BY
*   More than 50 example queries, tips and ideas

Please watch the video below or [on **my YouTube Channel**](https://youtu.be/l8DCPaHc5TQ)
.

The Queries
-----------

Here are some of the example queries covered in the video lesson. Feel free to copy paste them in to SQL console to see how they work.

				
					`-- Select everything from sales table  select * from sales;  -- Show just a few columns from sales table  select SaleDate, Amount, Customers from sales; select Amount, Customers, GeoID from sales;  -- Adding a calculated column with SQL  Select SaleDate, Amount, Boxes, Amount / boxes  from sales;  -- Naming a field with AS in SQL  Select SaleDate, Amount, Boxes, Amount / boxes as 'Amount per box'  from sales;  -- Using WHERE Clause in SQL  select * from sales where amount > 10000;  -- Showing sales data where amount is greater than 10,000 by descending order select * from sales where amount > 10000 order by amount desc;  -- Showing sales data where geography is g1 by product ID &  -- descending order of amounts  select * from sales where geoid='g1' order by PID, Amount desc;  -- Working with dates in SQL  Select * from sales where amount > 10000 and SaleDate >= '2022-01-01';  -- Using year() function to select all data in a specific year  select SaleDate, Amount from sales where amount > 10000 and year(SaleDate) = 2022 order by amount desc;  -- BETWEEN condition in SQL with < & > operators  select * from sales where boxes >0 and boxes <=50;  -- Using the between operator in SQL  select * from sales where boxes between 0 and 50;  -- Using weekday() function in SQL  select SaleDate, Amount, Boxes, weekday(SaleDate) as 'Day of week' from sales where weekday(SaleDate) = 4;  -- Working with People table  select * from people;  -- OR operator in SQL  select * from people where team = 'Delish' or team = 'Jucies';  -- IN operator in SQL  select * from people where team in ('Delish','Jucies');  -- LIKE operator in SQL  select * from people where salesperson like 'B%';  select * from people where salesperson like '%B%';  select * from sales;  -- Using CASE to create branching logic in SQL  select 	SaleDate, Amount,  		case 	when amount < 1000 then 'Under 1k' 				when amount < 5000 then 'Under 5k'                 when amount < 10000 then 'Under 10k' 			else '10k or more' 		end as 'Amount category' from sales;  -- GROUP BY in SQL  select team, count(*) from people group by team`
				
			

SQL Practice Problems
---------------------

Once you understand the concepts I’ve demoed in the video, try to solve below homework problems.

If you want to cheat, use the solutions tab to see the answers.

Homework Problems

Solutions (cheating)

Homework Problems

**INTERMEDIATE PROBLEMS**  
👉 You need to combine various concepts covered in the video to solve these

1\. Print details of shipments (sales) where amounts are > 2,000 and boxes are <100?  
2\. How many shipments (sales) each of the sales persons had in the month of January 2022?  
3\. Which product sells more boxes? Milk Bars or Eclairs?  
4\. Which product sold more boxes in the first 7 days of February 2022? Milk Bars or Eclairs?  
5\. Which shipments had under 100 customers & under 100 boxes? Did any of them occur on Wednesday?

**HARD PROBLEMS**  
👉 These require concepts not covered in the video

1\. What are the names of salespersons who had at least one shipment (sale) in the first 7 days of January 2022?  
2\. Which salespersons did not make any shipments in the first 7 days of January 2022?  
3\. How many times we shipped more than 1,000 boxes in each month?  
4\. Did we ship at least one box of ‘After Nines’ to ‘New Zealand’ on all the months?  
5\. India or Australia? Who buys more chocolate boxes on a monthly basis?

Solutions (cheating)

**INTERMEDIATE PROBLEMS:**

— 1. Print details of shipments (sales) where amounts are > 2,000 and boxes are <100?  
  
select \* from sales where amount > 2000 and boxes < 100;  
  
— 2. How many shipments (sales) each of the sales persons had in the month of January 2022?  
  
select p.Salesperson, count(\*) as ‘Shipment Count’  
from sales s  
join people p on s.spid = p.spid  
where SaleDate between ‘2022-1-1’ and ‘2022-1-31’  
group by p.Salesperson;  
  
— 3. Which product sells more boxes? Milk Bars or Eclairs?  
  
select pr.product, sum(boxes) as ‘Total Boxes’  
from sales s  
join products pr on s.pid = pr.pid  
where pr.Product in (‘Milk Bars’, ‘Eclairs’)  
group by pr.product;  
  
— 4. Which product sold more boxes in the first 7 days of February 2022? Milk Bars or Eclairs?  
  
select pr.product, sum(boxes) as ‘Total Boxes’  
from sales s  
join products pr on s.pid = pr.pid  
where pr.Product in (‘Milk Bars’, ‘Eclairs’)  
and s.saledate between ‘2022-2-1’ and ‘2022-2-7’  
group by pr.product;  
  
— 5. Which shipments had under 100 customers & under 100 boxes? Did any of them occur on Wednesday?  
  
select \* from sales  
where customers < 100 and boxes < 100;  
  
select \*,  
case when weekday(saledate)=2 then ‘Wednesday Shipment’  
else ”  
end as ‘W Shipment’  
from sales  
where customers < 100 and boxes < 100;

**HARD PROBLEMS:**

— What are the names of salespersons who had at least one shipment (sale) in the first 7 days of January 2022?

select distinct p.Salesperson  
from sales s  
join people p on p.spid = s.SPID  
where s.SaleDate between ‘2022-01-01’ and ‘2022-01-07’;

— Which salespersons did not make any shipments in the first 7 days of January 2022?

select p.salesperson  
from people p  
where p.spid not in  
(select distinct s.spid from sales s where s.SaleDate between ‘2022-01-01’ and ‘2022-01-07’);

— How many times we shipped more than 1,000 boxes in each month?

select year(saledate) ‘Year’, month(saledate) ‘Month’, count(\*) ‘Times we shipped 1k boxes’  
from sales  
where boxes>1000  
group by year(saledate), month(saledate)  
order by year(saledate), month(saledate);

— Did we ship at least one box of ‘After Nines’ to ‘New Zealand’ on all the months?

set @product\_name = ‘After Nines’;  
set @country\_name = ‘New Zealand’;

select year(saledate) ‘Year’, month(saledate) ‘Month’,  
if(sum(boxes)>1, ‘Yes’,’No’) ‘Status’  
from sales s  
join products pr on pr.PID = s.PID  
join geo g on g.GeoID=s.GeoID  
where pr.Product = @product\_name and g.Geo = @country\_name  
group by year(saledate), month(saledate)  
order by year(saledate), month(saledate);

— India or Australia? Who buys more chocolate boxes on a monthly basis?

select year(saledate) ‘Year’, month(saledate) ‘Month’,  
sum(CASE WHEN g.geo=’India’ = 1 THEN boxes ELSE 0 END) ‘India Boxes’,  
sum(CASE WHEN g.geo=’Australia’ = 1 THEN boxes ELSE 0 END) ‘Australia Boxes’  
from sales s  
join geo g on g.GeoID=s.GeoID  
group by year(saledate), month(saledate)  
order by year(saledate), month(saledate);

Resources to Learn More
-----------------------

![SQL Resources](https://chandoo.org/wp/wp-content/uploads/2022/08/SNAG-2250.png)

SQL is a great skill to have if you work with data. Please use below courses, books, articles & websites to learn more.

### SQL BOOKs 📚

[![SQL Quick Start Guide by Walter Shields](https://chandoo.org/wp/wp-content/uploads/elementor/thumbs/SNAG-2247-ptoa8vjadeexdhq5gag3yj2wray4b9sfss6vzqrwla.png "SQL Quick Start Guide by Walter Shields")](https://amzn.to/3pDSihk)

I recommend getting these SQL books.

*   [SQL Quick Start Guide by Walter Shields](https://amzn.to/3pDSihk)
    
*   [SQL for Data Analysis by Cathy T](https://amzn.to/3wnNIHX)
    
*   [SQL All-in-One for Dummies by Allen G. Taylor](https://amzn.to/3PIbc18)
    

### SQL COURSEs 💻

[![SQL 101 course by Alvin Wan](https://chandoo.org/wp/wp-content/uploads/elementor/thumbs/SNAG-2248-ptoayhmzkyhwo36ay4s39qss13b4z1gqy7g32xyi90.png "SQL 101 course by Alvin Wan")](https://amzn.to/3pDSihk)

I recommend trying out these courses on SkillShare academy.

*   [SQL 101 by Alvin Wan](https://skl.sh/3KivwFm)
    
*   [SQL Database & Queries](https://skl.sh/3R4GobS)
    

### SQL WEBSITEs 🌐

Do check out these helpful websites to learn and understand various SQL concepts.

*   [W3Schools SQL](https://www.w3schools.com/sql/)
    
*   [Introduction to SQL by Khan Academy](https://www.khanacademy.org/computing/computer-programming/sql)
    
*   [Introduction to T-SQL by Microsoft Docs](https://docs.microsoft.com/en-us/learn/paths/get-started-querying-with-transact-sql/)
    

If you use my links to purchase the books or courses, I get a small affiliate commission.

There is no extra cost to you, obviously.

SQL Alternatives
----------------

If you want an alternative to SQL, consider learning Power Query.

[Here is an article](https://chandoo.org/wp/power-query-tutorial/)
 and [here is a video](https://youtu.be/PiFAa_jjaEI)
 to help you with that.

All the best 👍
---------------

I wish you all the best with your SQL learning. Do let me know in the comments below if you have enjoyed this article and the video.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [23 Comments](https://chandoo.org/wp/learn-sql-for-data-analysis/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/learn-sql-for-data-analysis/#respond)
    
*   Tagged under [data analyst](https://chandoo.org/wp/tag/data-analyst/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [sql](https://chandoo.org/wp/tag/sql/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [SQL](https://chandoo.org/wp/category/sql/)
    

[PrevPreviousHow to create interactive tooltips in Power BI (step by step)](https://chandoo.org/wp/how-to-create-tooltips-in-power-bi/)

[NextMortgage Calculator with Extra Payments – Excel DownloadNext](https://chandoo.org/wp/mortgage-calculator-with-extra-payments-excel-download/)

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
    
    [Reply](https://chandoo.org/wp/learn-sql-for-data-analysis/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/learn-sql-for-data-analysis/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/learn-sql-for-data-analysis/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ