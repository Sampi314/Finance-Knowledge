# FREE 14 Week Data Analyst Course (with videos, files and data)

**Source:** https://chandoo.org/wp/free-data-analyst-course

---

FREE Data Analyst Course
========================

![](https://chandoo.org/wp/wp-content/uploads/2024/07/free-data-analyst-course-by-chandoo.jpg)

Learn all the essential concepts of data analysis in one place with my amazing, free course.

_**In this page:**_

*   [Module 1 – DATA + SQL](https://chandoo.org/wp/free-data-analyst-course/#_module1)
    
*   [Module 2 – Microsoft Excel](https://chandoo.org/wp/free-data-analyst-course/#_module2)
    
*   [Module 3 – Microsoft Power BI](https://chandoo.org/wp/free-data-analyst-course/#_module3)
    
*   [Module 4 – Python](https://chandoo.org/wp/free-data-analyst-course/#_module4)
    
*   [Next steps with a roadmap](https://chandoo.org/wp/free-data-analyst-course/#_module5)
    

Module 1: Data & SQL
--------------------

As a data analyst, you will be working with LOTS of data. So the first and most natural thing to learn about is, how to use data. In this module, we will cover all the essential and vital concepts of working with databases, data sources and data repositories.

The key skills you will gain are,

*   What is a database
*   How to install MySQL on your computer
*   Primary key vs. Foreign key
*   CRUD operations
*   Writing SQL queries
*   Advanced SQL concepts
    *   Joins
    *   Grouping
    *   CTE (Common Table Expressions)
    *   Functions

### Lesson 1: Introduction to Databases & SQL

In the very first lesson, learn how to use a database on your computer (with MySQL).

**Resources and downloads for this lesson:**

*   [Install MySQL](https://dev.mysql.com/downloads/installer/)
    
*   [Sakila Database – ER Diagram](https://dev.mysql.com/doc/sakila/en/sakila-structure.html)
    

**Watch the lesson:**

You can watch this lesson below or [**on my YouTube channel here**](https://www.youtube.com/watch?v=Iceaqdy7mEs)
.

Introducing **Excel + Power BI on-demand course** for data analysts.

If you are looking for a one-stop place to learn all the advanced Excel, Power Query, Power Pivot and Power BI techniques to work as a data analyst, consider my online class today.

[**Click here for more information.**](https://chandoo.org/wp/power-bi-course/)

[![Introducing Excel + Power BI course for data analysts](https://chandoo.org/wp/wp-content/uploads/2024/07/excel-power-bi-course-for-da-sqr.jpg)](https://chandoo.org/wp/power-bi-course/)

### Lesson 2: Advanced SQL for Data Analysis  
(10 Examples)

Now that you have SQL concepts and database understanding, let’s examine 10 practical, everyday data analysis scenarios and build SQL queries for the same. By the end of this lesson, you will learn:

*   How to use WHERE clause in SQL
*   Work with AND / OR / LIKE / IN operators in SQL
*   Getting DISTINCT values with SQL
*   Grouping data with GROUP BY
*   Using SQL JOINS
*   Creating Common Table Expressions (CTE)
*   Business Analysis and Decision Making with SQL

10 SQL Queries + Homework (BLANK)

Here are the 10 example SQL queries and home work problems. This is a blank file. Use it to practice and improve your SQL skills.

#10 Sample queries for SAKILA Database

\# 1) All films with PG-13 films with rental rate of 2.99 or lower

\# 2) All films that have deleted scenes

\# 3) All active customers

\# 4) Names of customers who rented a movie on 26th July 2005

\# 5) Distinct names of customers who rented a movie on 26th July 2005

\# H1) How many distinct last names we have in the data?

\# 6) How many rentals we do on each day?

\# 7) All Sci-fi films in our catalogue

\# 8) Customers and how many movies they rented from us so far?

\# 9) Which movies should we discontinue from our catalogue (less than 5 lifetime rentals)

\# 10) Which movies are not returned yet?

\# H2) How much money and rentals we make for Store 1 by day?  
\# What are the three top earning days so far?

10 SQL Queries (Completed)

Here are all the 10 queries completed against SAKILA sample database in MySQL.

\# 1) All films with PG-13 RATING with rental rate of 2.99 or lower

SELECT \* FROM film f  
where f.rental\_rate <=2.99  
and f.rating = ‘PG-13’;

\# 2) All films that have deleted scenes

select f.title, f.special\_features, f.release\_year  
from film f  
where f.special\_features like ‘%Deleted Scenes%’  
and title like ‘c%’;

\# 3) All active customers

select \* from customer  
where active=1;

\# 4) Names of customers who rented a movie on 26th July 2005

select r.rental\_id, r.rental\_date, r.customer\_id,  
concat(c.first\_name,’ ‘, c.last\_name) ‘Full name’ from rental r  
join customer c on c.customer\_id = r.customer\_id  
where date(r.rental\_date) = ‘2005-07-26’;

\# 5) Distinct names of customers who rented a movie on 26th July 2005  
select distinct r.customer\_id,  
concat(c.first\_name,’ ‘, c.last\_name) ‘Full name’ from rental r  
join customer c on c.customer\_id = r.customer\_id  
where date(r.rental\_date) = ‘2005-07-26’;

\# H1) How many distinct last names we have in the data?

\# 6) How many rentals we do on each day?

select date(rental\_date) d, count(\*) from rental  
group by date(rental\_date);

\# 7) All Sci-fi films in our catalogue

SELECT \* FROM CATEGORY;

SELECT \* FROM film\_category WHERE category\_id=14;

select fc.film\_id, fc.category\_id,c.name, f.title, f.release\_year from film\_category fc  
join category c on c.category\_id = fc.category\_id  
join film f on f.film\_id = fc.film\_id  
where c.name=’Sci-Fi’;

\# 8) Customers and how many movies they rented from us so far?

select r.customer\_id, c.first\_name, c.email, count(\*) ‘Count’  
from rental r  
join customer c on c.customer\_id = r.customer\_id  
group by r.customer\_id  
order by count(\*) desc;

select c.customer\_id, c.first\_name, c.email, count(r.customer\_id)  
from customer c  
left outer join rental r on c.customer\_id = r.customer\_id  
group by c.customer\_id;

\# 9) Which movies should we discontinue from our catalogue (less than 5 lifetime rentals)

// Refer to the correct query below.

with low\_rentals as  
(select inventory\_id, count(\*)  
from rental r  
group by inventory\_id  
having count(\*)<=1)  
select low\_rentals.inventory\_id, i.film\_id, f.title  
from low\_rentals  
join inventory i on i.inventory\_id = low\_rentals.inventory\_id  
join film f on f.film\_id = i.film\_id;

// CORRECT QUERY

with low\_rentals as  
(select i.film\_id, count(\*)  
from rental r  
join inventory i on i.inventory\_id = r.inventory\_id  
group by i.film\_id  
having count(\*)<=5)  
select low\_rentals.film\_id, f.title  
from low\_rentals  
join film f on f.film\_id = low\_rentals.film\_id;

\# 10) Which movies are not returned yet?

SELECT rental\_date, customer\_id, i.film\_id, f.title  
FROM RENTAL r  
join inventory i on i.inventory\_id = r.inventory\_id  
join film f on f.film\_id = i.film\_id  
WHERE r.return\_date is null  
order by f.title;

\# H2) How much money and rentals we make for Store 1 by day?  
\# What are the three top earning days so far?

Home work solutions

\# H1) How many distinct last names we have in the data?

select count(distinct last\_name) from customer;

\# H2) How much money and rentals we make for Store 1 by day?

select date(p.payment\_date),sum(p.amount) from payment p  
join rental r on r.rental\_id = p.rental\_id  
join inventory i on i.inventory\_id = r.inventory\_id  
where i.store\_id = 1  
group by date(p.payment\_date)  
order by date(p.payment\_date);

\# What are the three top earning days so far?

select date(p.payment\_date),sum(p.amount) from payment p  
join rental r on r.rental\_id = p.rental\_id  
join inventory i on i.inventory\_id = r.inventory\_id  
where i.store\_id = 1  
group by date(p.payment\_date)  
order by sum(p.amount) desc  
limit 3

**Watch the lesson:**

Watch the lesson below or on [my Channel here](https://youtu.be/Ejxam_CBY9U)
.

#### Additional Resources on SQL

In the first two lessons of this free data analyst course, I’ve introduced the essential and necessary concepts of SQL. Please refer to below pages / videos for more on SQL.

*   [Learn SQL in one hour (with sales dataset, 50 queries)](https://chandoo.org/wp/learn-sql-for-data-analysis/)
    
*   [How to use SQL with Power BI? (with a project)](https://youtube.com/live/UQJAHUUFK-o?feature=share)
    
*   [How to use LEFT / RIGHT / ANTI joins in SQL](https://youtu.be/xkYpNfpmbGY)
    
*   [Database vs. Data Warehouse vs. Data Lake](https://youtu.be/WgIbvkyY4mI)
    
*   [SQL keywords – glossary](https://www.w3schools.com/sql/sql_ref_keywords.asp)
    

### Lesson 3: How to use Power Query  
in 30 minutes

![](https://chandoo.org/wp/wp-content/uploads/2024/08/SNAG-3680.png)

While SQL is great for data analysis, it has one serious limitation. It can only work with data in a database / datawarehouse. What if the data you want to analyze is in a PDF or webpage or SharePoint folder? In such cases, SQL is almost useless.

This is where Power Query shines.

Power Query is the _de-facto_ query language of Power BI and Excel. Using Power Query, we can connect to any kind of data and perform operations on it (like filtering data, grouping, joining, cleaning up, adding new columns or setting up automations).

So the last lesson of our data segment shall focus on Power Query and introduces how we can use it to work with business data problems.

**Topics you will learn in this lesson:**

*   What is Power Query and why it is important?
*   How to use Power Query?
*   Using Power Query to scrape web data (live example)
*   Data cleaning and transformations with Power Query
*   Adding columns with PQ
*   How to load and refresh data?
*   Working with business data (HR example)
*   Understanding “column quality”
*   Using advanced transformations
*   Creating columns based on business rules
*   Writing M code (simple example)
*   Splitting values
*   Updating data and refreshing the query

#### Sample Files - Power Query

Please grab the sample files for Power Query segment using the links below.

*   Webscraping URL: https://en.wikipedia.org/wiki/2020\_Summer\_Olympics\_medal\_table
*   [Staff Data file](https://chandoo.org/wp/wp-content/uploads/2024/08/sample-staff-data.xlsx)
    
*   [Completed Example File](https://chandoo.org/wp/wp-content/uploads/2024/08/demofile.xlsx)
    

#### Additional Resources on Power Query

Learn more about Power Query using these pages and links:

*   [Beginner to PRO Advanced Masterclass with Power Query](https://chandoo.org/wp/power-query-tutorial/)
    
*   Power Query advanced examples:
    *   [Combining multiple sheets to one dataset](https://youtu.be/k_ugshJ4wIw)
        
    *   [Combining multiple files to one dataset](https://youtu.be/SGzegma9bdY)
        
    *   [Extracting data from PDF](https://chandoo.org/wp/excel-to-pdf/)
        
    *   [Extracting complex data from spreadsheets (custom M functions)](https://chandoo.org/wp/combine-excel-files-using-power-query/)
        
*   [Power Query functions reference](https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference)
    
*   [SQL vs. Power Query – the ultimate comparison](https://chandoo.org/wp/sql-vs-power-query/)
    
*   Power Query courses:
    *   [Power Query mini-course](https://chandoo.org/wp/power-query-power-course/)
        
    *   [Advanced Excel + Power Query course](https://chandoo.org/wp/excel-school-program/)
        

Module 2: Excel
---------------

Microsoft Excel is the #1 software used by Data Analysts all over the world. That is why, in our module 2 of this free data analyst course, we are going to learn all about Excel. The skills you will gain in this module are:

*   How to use Excel for data analysis
*   Essential Excel Functions & Formulas
*   Excel Pivot Tables
*   Power Pivot & DAX in Excel
*   How to make Excel charts
*   Excel Portfolio Project – Customer Center Data Analysis + Dashboard

Technical concepts covered in this module are:

*   Excel tables
*   Writing formulas – cell references, structural referencing, spill ranges
*   Important Excel functions – SUMIFS, COUNTIFS, SUBTOTAL, IF, IFS, VLOOKUP, XLOOKUP, INDEX+MATCH, FILTER, SORT, UNIQUE, IFERROR, CHOOSECOLS, TAKE, Formula nesting.
*   Excel filters & slicers
*   Working with pivot tables
*   Data modeling
*   DAX + Power Pivot
*   Excel charts, Pivot Charts, Chart customization
*   Creating Excel dashboards
*   Conditional Formatting

Software used:

*   Excel 365 (you can follow along most of the lessons with Excel 2016+)

### Lesson 4: Essential Excel for Data Analysis

Excel has 100s of features, so learning what is important can be tricky. In this video, let me distil the essential concepts and present them in a digestible format in just under 40 minutes.

This is “Essential” Excel in 40 minutes.

_**What you will learn:**_

1.  How to use data in Excel
2.  The importance of Excel tables
3.  Working with Filters & Slicers in Excel to do quick analysis
4.  Using “Total Row” / SUBTOTAL function
5.  Understanding Excel cell references – Relative / Absolute / Structural / Spill
6.  Important and useful Excel functions – IF, IFS, SUBTOTAL
7.  Creating and using Pivot Tables
8.  Making Excel Charts – Box plots to explore salary distribution
9.  Interactive charts with slicers
10.  Next steps to improve your understanding of Excel

Watch the lesson below (or [on my YouTube channel](https://youtu.be/VT479YDPB0I)
):

#### Sample Files - Essential Excel

Please download these files to learn the Essential Excel Concepts:

*   [Essential Excel Concepts – BLANK workbook](https://chandoo.org/wp/wp-content/uploads/2024/08/essential-excel-concepts-blank.xlsx)
     (for practice)
*   [Essential Excel Concepts – Completed File](https://chandoo.org/wp/wp-content/uploads/2024/08/essential-excel-concepts-demo.xlsx)
    

#### Additional Resources: Excel basics → Advanced

Refer to these pages and videos to learn more about Essential Excel Concepts:

*   [Excel Basics – What skills and concepts you need to learn](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills – a listing of important topics and examples](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [3 Month Roadmap to Learn Advanced Excel](https://chandoo.org/wp/advanced-excel-roadmap/)
    
*   [**Full Advanced Excel Course by Chandoo**](https://chandoo.org/wp/excel-school-program/)
     \[paid program, 10k+ students\]

*   [How to Excel as a beginner](https://youtu.be/F7aPazuS8QY)
     (video, 350k views)
*   [Beginner to PRO Excel Class](https://youtu.be/v2oNWja7M2E)
     (video, 2mn views)

Introducing **Advanced Excel + Dashboards on-demand course** for data analysts.

If you are looking for a one-stop place to learn all the advanced Excel, Power Query, Power Pivot and dashboard techniques to work as a data analyst, consider my online class today.

[**Click here for more information.**](https://chandoo.org/wp/excel-school-program/)

[![advanced excel + dashboards course by chandoo](https://chandoo.org/wp/wp-content/uploads/2024/08/SNAG-3685.png)](https://chandoo.org/wp/excel-school-program/)

### Lesson 5: Excel Formulas + Functions

There are 200+ functions in Excel. But as a data analyst, you just need to know only a handful of them. In this lesson, we are going to learn the most important functions and formulas in Excel with 10 practical business problems.

Functions you will be learning are:

*   SUMIFS
*   COUNTIFS
*   MIN / MAX
*   SMALL / LARGE
*   FILTER
*   SORT
*   TAKE
*   UNIQUE
*   VLOOKUP
*   XLOOKUP
*   INDEX + MATCH
*   CHOOSECOLS
*   IFERROR
*   Nesting formulas

**Watch the lesson below ([direct YouTube link](https://www.youtube.com/watch?v=dVJFyqI_Nw4)
):**

#### Sample Files - Excel Formulas

*   [Blank file (for practice) with home work problems](https://chandoo.org/wp/wp-content/uploads/2024/08/sample-data-fx.xlsx)
    
*   [Completed Workbook (no homework solutions)](https://chandoo.org/wp/wp-content/uploads/2024/08/sample-data-fx-demo.xlsx)
    

#### Additional Resources - Excel Formulas

Individual tutorials on all the important functions:

*   [SUMIFS](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/)
    
*   [SUBTOTAL](https://chandoo.org/wp/subtotal-formula-excel/)
    
*   [VLOOKUP](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    
*   [XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
    
*   [INDEX+MATCH](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
    
*   [FILTER, SORT & Other dynamic array functions](https://chandoo.org/wp/dynamic-array-functions/)
    
*   [IFERROR](https://chandoo.org/wp/iferror-formula/)
    

Compilation articles:

*   [Top 10 formulas for data analysts](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Top 10 functions for finance people](https://chandoo.org/wp/top-10-accounting-kpis-excel/)
    
*   [Top 10 formulas for IT people](https://chandoo.org/wp/top-10-excel-formulas-for-it-people/)
    
*   [100 Excel formulas and functions](https://chandoo.org/wp/excel-formula-list/)
    

Videos:

*   [IF formula and 5 Advanced Tips](https://www.youtube.com/watch?v=15NtFld9mVM)
    
*   [IF formula + 10 Advanced Tricks](https://www.youtube.com/watch?v=-yFpzIRifK4)
    
*   [SUMIFS formula + 10 Pro tricks](https://youtu.be/YEt-aYbDTrs)
    
*   [XLOOKUP + 10 Tricks](https://youtu.be/YyhJe5tMq58)
    
*   [INDEX + 7 Tricks](https://www.youtube.com/watch?v=kly0uPIM4IU)
    
*   [Dynamic Array Formulas – Masterclass](https://youtube.com/live/8IV_W13VFkw)
    
*   [Top 10 Excel Functions](https://www.youtube.com/watch?v=HgNCvd8IbSc)
    

Courses:

*   **[Beginner to PRO Excel Functions + Advanced Excel Course](https://chandoo.org/wp/excel-school-program/)
    **

### Lesson 6: Excel Pivot Tables & Charts

While Excel formulas are powerful, you also need to plan and think hard before writing them to solve business problems. This is why I love Pivot tables. They are really easy to make and provide the biggest bang for buck. We can use Pivots to analyze data and answer business questions effectively and elegantly in short amount of time.

In this lesson, learn how to:

*   Create a pivot table from your data
*   Using the fields panel to construct your “dream” pivot
*   Work with report filters, top 10 filters and sort options
*   Change calculation in the pivot
*   Set up slicers to “interact” with pivot tables
*   Create “groups” in pivots
*   Make pivot charts to analyze trends
*   Calculate Cumulative “running” totals in Pivots
*   Use conditional formatting with Pivots
*   Percentage analysis with Pivots
*   Set up advanced pivot tables to solve business problems

**Watch the lesson below ([Excel Pivot Tables Tutorial on YouTube](https://www.youtube.com/watch?v=zuSNd1ZMfBI)
):**

#### Sample Files - Excel Pivot Tables

*   [Blank data file (with analysis themes) – use it to follow-along](https://chandoo.org/wp/wp-content/uploads/2024/09/sample-data-pivots-blank.xlsx)
    
*   [Completed Workbook (with all the pivots)](https://chandoo.org/wp/wp-content/uploads/2024/09/sample-data-pivots-2.xlsx)
    

#### Additional Resources on Pivot Tables

Check out below pages and videos to learn more about various aspects of Pivot tables.

*   [Pivot Tables in Excel – Complete Tutorial + Tips](https://chandoo.org/wp/excel-pivot-tables-tutorial/)
    
*   [13 Advanced Pivot Table Tricks you need to know](https://chandoo.org/wp/advanced-pivot-tables/)
    
*   [How to use slicers in Excel](https://chandoo.org/wp/introduction-to-slicers/)
     \[[slicers video](https://www.youtube.com/watch?v=ZZ-UGMztoqo)\
    \]
*   [How to make pivot tables when you have too much data?](https://chandoo.org/wp/pivot-tables-from-large-data-sets/)
    
*   [Make a quick dashboard with Pivot tables in Excel](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)
     \[[tutorial video](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)\
    \]
*   [Pivot Tables – More than 50 articles, tips and examples](https://chandoo.org/wp/category/pivot-tables-charts/)
    

### Lesson 7: Excel Portfolio Project

![Excel Dashboard - Complete Tutorial](https://chandoo.org/wp/wp-content/uploads/2024/09/excel-portfolio-project-demo3.gif)

In our final lesson of Excel module, we will be building a _**call centre performance dashboard**_ as show-cased above. In this portfolio project, you will learn:

*   Designing the dashboard color theme and fonts
*   How to use Data model feature of Excel to connect datasets
*   Creating KPIs and measures using Power Pivot and DAX
*   Using Pivot tables to create all the dashboard calculations
*   Making interactive Pivot Charts with slicers
*   Applying conditional formatting to charts & tables
*   Using XLOOKUP and images in Excel to show dynamic pictures

Watch the video below or by going to the [“Excel Portfolio Project – Complete Tutorial” video](https://www.youtube.com/watch?v=mYdM46FAQJY)
 on my channel.

#### Sample Files - Excel Dashboard

*   [**Blank data file (perfect for following along and practice)**](https://chandoo.org/wp/wp-content/uploads/2024/09/sample-data-excel-portfolio-project.xlsx)
    
*   [Completed Dashboard](https://chandoo.org/wp/free-call-centre-dashboard/)
    

#### Other Ideas for Excel Portfolio Projects

If you want to impress potential recruiters and clients, try out these other Excel projects.

*   Investment / Personal networth tracker \[[inspiration](https://chandoo.org/wp/budget-spreadsheet-download/)\
    \]
*   Analyze your favorite sports team performance \[[Federer vs. Murray at Wimbledon](https://chandoo.org/wp/visualizing-roger-federers-7th-wimbledon-win-in-excel/)\
    \]
*   Excel to visualize financial performance \[[finance dashboard with Excel](https://chandoo.org/wp/financial-dashboard-tutorial/)\
    \]
*   Graphically analyze your fav. comics \[[stream graph to analyze comics](https://chandoo.org/wp/stream-graph-in-excel/)\
    \]

[![](https://chandoo.org/wp/wp-content/uploads/2020/07/x-men-appearances-stream-chart-in-excel-trailer.gif)](https://chandoo.org/wp/stream-graph-in-excel/)

### Become an Excel PRO with Chandoo

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/dashboard-ex-1.png)](https://chandoo.org/wp/excel-school-program/)

If you need an end-to-end, comprehensive and real-world Excel course, please consider my **Excel School Program.**

You will learn how I use Excel to solve business problems, how I write formulas and how I make charts in this online, self-paced course.

Don’t let the lack of Excel skills hold you back at work. Unleash your full potential with my Excel School program today.

**[Click here to learn more and sign up for Excel School](https://chandoo.org/wp/excel-school-program/)
**.

Module 3: Power BI
------------------

Microsoft Power BI is the hottest and most widely sought after skill for data analysts everywhere. In this module, you will learn:

*   How to get started with Power BI
*   Understanding Power BI ecosystem
*   Data modeling with Power Pivot
*   Creating and using DAX measures
*   Working with Power BI Visuals
*   Power BI portfolio project

Technical concepts covered in this module are:

*   Using Power BI
*   Semantic / Data Modeling
*   Star Schema
*   DAX
*   Visual Interactions
*   Conditional Formatting
*   Report Design
*   Sharing & Publishing the reports

Software used:

*   Microsoft Power BI ([download for free here](https://www.microsoft.com/en-us/power-platform/products/power-bi/desktop)
    )

### Lesson 8: What is Power BI (and 60 other technical terms)

In this lesson, learn what Power BI is and what some of the other technical terms are.  This lesson has 2 videos. Watch them in the order listed.

#### Power BI Jargon (part 1)

#### Power BI Jargon (part 2)

#### Download Power BI Mind map + Glossary PDF

I made a PDF with all the important Power BI terms. Enter your email address and I will send you the file.

   

Name 

Email 

Send me the files

### Lesson 9: Getting Started with Power BI

In this video we will be covering,

*   **Introduction to Power BI:** how to get started with Power BI, including downloading and installing Power BI Desktop, loading data, and creating visuals and tables.
*   **Creating a Business Report:** step-by-step process of creating a complete business report using Power BI, from loading sample data to formatting visuals and sharing the report with others.
*   **Power BI Interface:** the main areas of the Power BI interface, including the ribbon, canvas, panels, and switching panel, and how to use these areas to construct and navigate reports.
*   **Building Visuals:** how to create various types of visuals, such as column charts, bar charts, and slicers, and how to format and customize these visuals to display data effectively.
*   **Publishing and Sharing Reports:** the process of saving, publishing, and sharing Power BI reports, including the benefits of using the Power BI online platform for collaboration and data updates.

Watch the video below or go to the [Getting Started with Power BI video](https://www.youtube.com/watch?v=al4OfLIOl2w)
 on my channel.

#### Sample Files - Introduction to Power BI

*   [Sample Data file](https://chandoo.org/wp/wp-content/uploads/2024/10/sample-chocolate-sales-data-1.xlsx)
    
*   [Completed Power BI workbook](https://chandoo.org/wp/wp-content/uploads/2024/10/power-bi-intro-demo.zip)
     \[unzip this file\]

### Lesson 10: What is Data Modeling?

Data modeling is the vital first step you need to take to fully utilize the **power** of Power BI. In this video learn,

*   What is data modeling?
*   Fact vs. Dimension
*   What is a star schema?
*   How to set up star schema in Power BI?
*   Data vs. Semantic Model
*   Types of relationships
*   Filter propagation
*   Importance of _proper_ data modeling

Watch the video below or [on my YouTube channel page](https://www.youtube.com/watch?v=4ePNrdxWtY0)
.

#### Sample Files - Data Modeling with Power BI

*   [Sample Data file for data modeling](https://chandoo.org/wp/wp-content/uploads/2024/10/sample-chocolate-sales-data-all.xlsx)
    
*   [Completed Power BI Datamodel file](https://chandoo.org/wp/wp-content/uploads/2024/10/powerbi-data-model-done.zip)
     \[unzip this file\]

#### More resources on Data Modeling

*   [Power BI Star Schema explained](https://youtu.be/1CgG0t59WcM)
    
*   [Measure vs. Column in Power BI](https://youtu.be/kgNbWOCuRCE)
    
*   [How to make calendar tables with Power Query](https://youtu.be/wN1ok8JDzrI)
    

### Lesson 11: Learn 80% of DAX in an hour

DAX makes Power BI _powerful._ It is the engine behind all the awesomeness that we see in Power BI reports.

Data Analysis eXpressions or simply DAX is the language we use to define calculations on top of our data to effectively analyze and visualize data in Power BI (and Excel too!)

In this lesson, learn all the key aspects of DAX and become confident in it.

*   How to create measures 🤔
*   Measure vs. Column ⚙
*   Measure reusability ♻
*   Evaluation Context 💻
*   Basic DAX functions – SUM, COUNTROWS, AVERAGE, DIVIDE 🧮
*   Conditional DAX functions – IF 🌿
*   Understanding and using CALCULATE function 📗
*   Multiple filters with CALCULATE 🥝
*   How to get good with DAX using ACMBU technique 💡

Watch the lesson below or on my channel’s [Learn 80% DAX in one hour video](https://youtu.be/lD7TvkoQ6rY)
.

#### All the DAX measures (code)

Here are all the DAX measures discussed and made in the video. You can copy and paste each line in to Power BI to create the measures directly.

				
					`Total Amount = SUM(shipments[Amount])  Shipment Count = countrows(shipments) Total Boxes = SUM(shipments[Boxes]) Boxes per Shipment = [Total Boxes] / [Shipment Count] Amount per Shipment = DIVIDE([Total Amount],[Shipment Count]) Barr Amount = CALCULATE([Total Amount], people[Sales_person]="Barr Faughny") Barr Amount Pct = DIVIDE([Barr Amount], [Total Amount]) Barr Bar Amount =      CALCULATE([Total Amount],          people[Sales_person] = "Barr Faughny",          products[Category]= "Bars") Total Amount (my team v1) =      CALCULATE([Total Amount],     people[Sales_person] = "Barr Faughny" ||     people[Sales_person] = "Beverie Moffet" ||     people[Sales_person] = "Ches Bonnell" ||     people[Sales_person] = "Husien Augar") Total Amount (my team v2) =      CALCULATE([Total Amount],     people[Sales_person] IN { "Barr Faughny" , "Beverie Moffet" ,"Ches Bonnell" , "Husien Augar" }) Sales Target = 2000000 Target Comparison v1 = if([Total Amount]>[Sales Target],"Yes","No") Target Comparison v2 = if(shipments[Amount] >[Sales Target], "Yes", "no") Target Comparison v3 = if([Total Amount]>[Sales Target], "thumbs up emoji", "thumbs down emoji")`
				
			

#### Sample Files - 80% DAX in an hour

*   [Sample Data file for data modeling](https://chandoo.org/wp/wp-content/uploads/2024/10/sample-chocolate-sales-data-all.xlsx)
    
*   [Blank Power BI file](https://chandoo.org/wp/wp-content/uploads/2024/10/powerbi-data-model-done.zip)
     \[unzip this file\]
*   [Completed Power BI DAX file](https://chandoo.org/wp/wp-content/uploads/2024/10/powerbi-dax-wip.zip)
     \[unzip this file\]

### Lesson 12: Working with Power BI Visuals

Charts (also called visuals) are what the end-users of Power BI see. That is why, next step of our Power BI learning focuses on how to create and use various Power BI visuals.

In this lesson, learn how to make:

*   Column chart 📊
*   Line chart 📈
*   Donut charts🍩
*   KPI Cards 💳
*   Small Multiples 🔡
*   Matrix 📰

#### Sample Files - Power BI Visuals

*   [Blank Power BI file](https://files.chandoo.org/pbix/powerbi-visuals-part1-blank.pbix)
    
*   [Canvas Background Image](https://files.chandoo.org/pbix/img/Slide2.PNG)
    

### Lesson 13: Power BI Portfolio Project

Let’s conclude the Power BI segment of this _**free data analyst course**_ by creating a complete portfolio dashboard with it.

In this lesson, we will create a hotel bookings report with Power BI.

**Key skills you will gain are:**

*   📁 Setting Up the Power BI Report: Step-by-step setup of metrics, slicers, and background for the report.
*   💡 Exploring Data Preparation Techniques: Learn about data cleaning and preparation, including the calculation of relevant columns such as booking and stay dates.
*   📊 Visualization Techniques: Key visuals such as trend lines, slicers, heat-maps, and tables are used to display booking trends, customer segments, and insights.
*   🔧 Adding Aesthetic Features: Background customization, theme setting, and color scheme creation in Power BI are demonstrated to enhance report visuals.
*   📈 Advanced Data Analysis: Insights on weekday vs. weekend bookings, loyalty levels, booking channels, and customer behavior are included.
*   📑 DAX Calculation Guidance: Overview of using DAX functions like SUM, COUNT, AVERAGE for calculating metrics and deriving insights.

#### Sample Files - Power BI Portfolio Project

*   [Blank Power BI file](https://files.chandoo.org/pbix/blank-report-v2.pbix)
    

Module 4: Python
----------------

Python is the perfect software for data analytics, machine learning, AI and general purpose programming. In this module, let’s understand how to use Python confidently. You will be learning below things:

*   Setting up Python on your computer
*   Installing & using Visual Studio Code
*   Understanding _**jupyter notebook style programming**_
*   Conditional statements, loops in Python
*   Working with lists in Python
*   Using NumPy to analyze data
*   Visualizing your data with matplotlib

**Software used:**

*   Visual Studio Code ([download here](https://code.visualstudio.com/)
    )
*   Python ([download here](https://www.python.org/downloads/)
    )

### Lesson 14: Python for Data Analysis

In our introductory Python lesson, learn how to set up and use Python on your computer confidently. You will learn below concepts:

✔ How to install Visual Studio Code & Python

✔ How to set up virtual environment for Python in VS Code

✔ How to set up and use Jupyter Notebooks with VS Code

✔ Writing and running your first python code

✔ Using “notebook” style programming to learn Python

✔ Working with Python Lists & slicing

✔ Control flow with IF conditions in Python

✔ Building a simple grade calculator with Python

✔ Next steps for Python leaning (lists, comprehension, numpy, matplotlib)

#### Code Samples - Python for Data Analysis

You can access all the **[code samples from my github profile too](https://github.com/chandoo-org/python/)
**.

				
					`name = "alice" age = 18 GPA = 3.78 plays_volleyball = True  print(name)  print(name, age, GPA, plays_volleyball)  # adding 0.07 to GPA  GPA = GPA + 0.07  print(name, age, GPA, plays_volleyball)  # Using F strings  print(f"The student name is {name} and they are {age} years old.")  age = age + 15 print(f"The student name is {name} and they will be {age} years old in 15 years.")  # using lists  sports = ["volleyball", "netball", "touch rugby", "cross country"]  sports[0]  # adding to a lists sports.append("Cricket")  print("Alice is currently playing: ", sports)  #list slicing sports[0:3] #first 3 items sports[-3:] #last 3 items sports[1:] #everything after first item   #letter grade calculator student_gpa = float(input("What is your GPA? "))  if student_gpa <= 2:     letter_grade = "D" elif student_gpa <= 3:     letter_grade = "C" elif student_gpa <= 3.8:     letter_grade = "B" else:     letter_grade = "A"  print(f"Student's letter grade is {letter_grade}")`

				
			

Next Steps
----------

Now that you have all the essential concepts ready (Excel, SQL, Power Query, Power Pivot, Power BI, Python), go ahead and practice these well with various business domains & concepts. Here is a road-map to learn:

*   **Before:** Complete the above lessons and repeat them as needed.
*   **Weeks 1 & 2:** After finishing the above lesson plan, figure out one project that you can do which incorporates all (or most of the) concepts you just learned. Here are a few ideas:
    *   **Python + Excel + Power Query + Power BI project:** Use Python to scrape data from any website. Export the data to Excel, use Excel to perform EDA. Then load the Excel file to Power BI thru Power Query to build a complex interactive data analytics report.
    *   **SQL + Excel + Power BI Project:** Use any sample SQL dataset and create auxiliary datasets in Excel (for example, customer data from SQL, survey data in Excel). Combine both datasets thru Power Query and analyze the thing in Power BI.
*   **Weeks 3 & 4:** Create the project and test it. Share your work on social media like LinkedIn / YouTube / Instagram. Understand your strengths and limitations.
*   **Weeks 5 & 6:** Fill gaps in your knowledge. May be you need more coding skills or querying or visualization. Whatever you lack, go for the deep-dive in that area.

All the best.

#### Get in touch with me

It has been a pleasure helping you with this free data analysis course. Feel free to get in touch with me for more.

*   [Join my free email newsletter](https://chandoo.org/wp/subscribe)
     (I send one email with Excel / Power BI goodness every week to over 100,000 people).
*   [Check out my YouTube channel](https://www.youtube.com/channel/UC8uU_wruBMHeeRma49dtZKA)
     (over 500 videos, 700,000 subscribers and new video every week)
*   [Say hello on LinkedIn](https://www.linkedin.com/in/purnaduggirala/)
    
*   [Check out my Instagram page](http://instagram.com/chandoo.xlsx)
     and follow for cheeky tutorials on Excel + Power BI

or you can also [join my Excel + Power BI Course](https://chandoo.org/wp/power-bi-course/)
 to learn all these concepts in detail. Over 20,000 satisfied customers and growing everyday.