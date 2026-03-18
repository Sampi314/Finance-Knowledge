# How to use SQL - Telugu materials and files » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-to-use-sql-telugu

---

How to use SQL: Instructions, files & queries
=============================================

![How to use SQL - telugu instructions and files](https://chandoo.org/wp/wp-content/uploads/2024/06/how-to-use-sql-telugu.jpg)

In this page, please find all the files, installation instructions, resources and sample queries for my [**Telugu SQL video course on YouTube**](https://youtu.be/IkUTX9WerXA)
.

Software Installation (MySQL)
-----------------------------

Before you can use MySQL, you must install and start the MySQL community server (and workbench software) on your computer. Please use below links for the software.

*   **[MySQL Windows Installer](https://dev.mysql.com/downloads/installer/)
    **
*   [_MySQL Community server for all operating systems_](https://dev.mysql.com/downloads/mysql/)
    
*   Help: [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/)
    

Installing Sample Database in MySQL
-----------------------------------

### **STEP 1:** Open MySQL workbench and create a new database.

1.  After installing the software, restart your computer if needed.
2.  Open MySQL Workbench.
3.  If needed, start the MySQL service in your computer (by going to start menu and searching for services)
4.  Locate the “localhost” connection in MySQL Workbench and click on it to start a session.
5.  Once inside, right click in the navigator area and create a new schema for our sample data. Name it “ac\_telugu” and apply to create the new database.

![create schema - mysql](https://chandoo.org/wp/wp-content/uploads/2024/06/SNAG-3615.png)

### STEP 2: Download sample data

I am providing 5 CSV files to use with SQL. Download them and use the below screenshot to add these files to your MySQL.

[**Download the CSV files for Awesome Chocolates sample data.**](https://chandoo.org/wp/wp-content/uploads/2024/06/awesome-telugu.zip)

Unzip the file to extract 5 CSV files.

### STEP 3: Create tables from CSV files in MySQL

![table data import wizard - mysql](https://chandoo.org/wp/wp-content/uploads/2024/06/SNAG-3616.png)

1.  Right click on the newly created “ac\_telugu” schema (database) and select the “Table data import wizard”.
2.  Browse and select the first CSV file (for ex: people-tel.csv)
3.  In the next screen, create a new table. Give it a name (for ex: people)
4.  Optionally, set data types for the import columns.
5.  Click next button until done.
6.  Repeat the process for all the CSV files.

Using MySQL and Writing Queries
-------------------------------

Now that we have sample data, you can write queries to explore and analyze it.

In the MySQL workbench, click on File > New Query tab (CTRL T) and write SQL.

Use the below SQL to see all the shipment records from the shipments table.

				
					`SELECT * FROM ac_telugu.shipments;`
				
			

[**Watch the SQL Beginner to PRO video**](https://youtu.be/IkUTX9WerXA)
 to learn more SQL.

Practice Queries (10 examples)
------------------------------

Blank Queries (for practice)

Completed Queries

Homework Solutions

Blank Queries (for practice)

\# SQL Examples

\# 1 – See all shipments

\# 2 – All shipments by SP02

\# 3 – All shipments by SP02 to G3

\# 4 – All shipments in Jan 2023

\# 5 – All shipments by SP02, SP03, SP12, SP15

\# 6 – Products that have the word choco in them

\# 7 – Sales persons whose name begins with S

\# 8 – Sales per box of chocolates in Feb 2023

\# 9 – All shipment data for Subbarao

\# 10 – All shipment data for Subbarao by month

\# H1 – All shipment data for Subbarao to USA  
\# H2 – What is the maximum amount in each month?  
\# H3 – How many shipments we do by each country in the month of March 2023

Completed Queries

**\# SQL Examples**

**\# 1 – See all shipments**

SELECT Product, s.Date, Amount, Boxes FROM shipments s;

**\# 2 – All shipments by SP02**

select \* from shipments s  
where s.\`Sales Person\` = ‘SP02’;

  
**\# 3 – All shipments by SP02 to G3**

select \* from shipments s  
where s.\`Sales Person\` = ‘SP02’ and s.Geo = ‘G3’  
order by s.amount desc;

  
**\# 4 – All shipments in Jan 2023**

SELECT \* FROM ac\_telugu.shipments\_new s  
where s.Date between ‘2023-1-1’ and ‘2023-1-31’;

select \* from shipments\_new s  
where Extract(year\_month from s.Date) = 202301;

**\# 5 – All shipments by SP02, SP03, SP12, SP15**

select \* from shipments\_new s  
where s.\`Sales Person\` = “SP02”  
or s.\`Sales Person\` = “SP03”  
or s.\`Sales Person\` = “SP12”  
or s.\`Sales Person\` = “SP15”;  
  
select \* from shipments\_new s  
where s.\`Sales Person\` in (“SP02”, “SP03”, “SP12”, “SP15”);

**\# 6 – Products that have the word choco in them**

select \* from products  
where product like ‘%choco%’;

**\# 7 – Sales persons whose name begins with S**

select \* from people  
where \`Sales Person\` LIKE ‘S%’;

**\# 8 – Sales per box of chocolates in Feb 2023**

SELECT S.DATE, s.Amount, s.Boxes, round(S.Amount / S.Boxes, 1) as ‘Amount per Box’ FROM SHIPMENTS\_NEW S  
WHERE extract(year\_month from s.Date) = 202302;

**\# 9 – All shipment data for Subbarao**

select \* from people  
where \`sales person\` like ‘subba%’;

select \* from shipments\_new  
where \`sales person\` = ‘sp11’;

select p.\`sales person\`, s.Date, s.Amount, s.boxes from shipments\_new s  
join people p on p.\`sp id\` = s.\`sales person\`  
where p.\`sales person\` LIKE ‘Subba%’;

  
**\# 10 – All shipment data for Subbarao by month**

  
select extract(year\_month from s.Date), sum(s.Amount), sum(s.boxes)  
from shipments\_new s  
join people p on p.\`sp id\` = s.\`sales person\`  
where p.\`sales person\` LIKE ‘Subba%’  
group by extract(year\_month from s.Date);

  
\# H1 – All shipment data for Subbarao to USA  
\# H2 – What is the maximum amount in each month?  
\# H3 – How many shipments we do by each country in the month of March 2023

Homework Solutions

**\# SQL Homework Hints:  
**

\# H1 – All shipment data for Subbarao to USA  
_\# use 2 joins_

\# H2 – What is the maximum amount in each month?  
_\# You need to group_

\# H3 – How many shipments we do by each country in the month of March 2023  
_\# Join and then group with a where_

**\# SQL Homework Solutions:**

\# H1 – All shipment data for Subbarao to USA

select p.\`sales person\`, g.Geo, s.Date, s.Amount, s.boxes from shipments\_new s  
join people p on p.\`sp id\` = s.\`sales person\`  
join geo g on g.GeoID = s.Geo  
where  
p.\`sales person\` LIKE ‘Subba%’ and  
g.Geo = “USA”;

  
\# H2 – What is the maximum amount in each month?

select extract(year\_month from s.Date), max(s.Amount), min(s.amount)  
from shipments\_new s  
group by extract(year\_month from s.Date);  
  
\# H3 – How many shipments we do by each country in the month of March 2023

select g.geo, count(\*), sum(s.Amount)  
from shipments\_new s  
join geo g on g.GeoID = s.Geo  
where extract(year\_month from s.Date) = 202303  
group by g.Geo;

Additional SQL Material
-----------------------

*   [Learn SQL for Data Analysis – More examples](https://chandoo.org/wp/learn-sql-for-data-analysis/)
    
*   [SQL vs. Power Query](https://chandoo.org/wp/sql-vs-power-query/)
    
*   [Advanced SQL video (in English)](https://www.youtube.com/watch?v=l8DCPaHc5TQ)
    
*   [SQL Joins and Advanced concepts (English)](https://www.youtube.com/watch?v=xkYpNfpmbGY)
    

Happy learning.