# Power Query: Expanding on Aggregating

**Source:** https://sumproduct.com/blog/power-query-expanding-on-aggregating/

---

[Home](https://sumproduct.com/)

\> Power Query: Expanding on Aggregating

*   November 7, 2017

Power Query: Expanding on Aggregating
=====================================

Power Query: Expanding on Aggregating
=====================================

8 November 2017

_Welcome to our Power Query blog. This week I look at bringing in two tables of data and summarising some of that data. At the same time._

I have two tables of data which give me information about my items and charges, as shown below. I have several goals: I need report on the key item data and work out the total and average sales for each item.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

I am going to create two queries, one to extract data from my Access database for each of my tables. As I am now using Excel 2016, I use the ‘New Query’ dropdown from the ‘Get and Transform’ section on the ‘Data’ tab:

![](<Base64-Image-Removed>)

I choose to upload my data from the ‘Microsoft Access Database’ option, and having selected my database, the tables available are shown below.

![](<Base64-Image-Removed>)

Since I am getting both my tables from this database, I check the ‘Select multiple items’ box.

![](<Base64-Image-Removed>)

Checkboxes appear next to my tables, and I can select both tables that I am interested in: ‘**ACCT\_Order\_Charges**‘ and ‘**Items**‘. I can create both queries at once! I choose to ‘Edit’:

![](<Base64-Image-Removed>)

My two queries have been created. I will merge them, using the option ‘Merge Queries’ in the ‘Combine’ section on the ‘Home’ tab in the editor.

![](<Base64-Image-Removed>)

I choose to create a new query with my merged data, by choosing the ‘Merge Queries as New’ option.

![](<Base64-Image-Removed>)

I need to select the field **_Item\_Key_** from both queries, as this is how my queries are linked. Not all my charges data is related to items – some are delivery charges, so not all the charges will be merged. I choose the ‘Left Outer’ join as I want all my items, and only the charge data that relates to my items:

![](<Base64-Image-Removed>)

A new query, ‘Merge1’ has been created.

![](<Base64-Image-Removed>)

Next to my item data, there is a table column, which holds the data from the charges query under the heading ‘**ACCT\_Order\_Charges**‘. I can click on the icon next to the ‘**ACCT\_Order\_Charges**‘ heading and expand my data – but that’s not all I can do.

![](<Base64-Image-Removed>)

I want to find out the total and average sales for each item, so I can choose to ‘Aggregate’, rather than ‘Expand’. I could expand and then group my data if I needed more information from ‘**ACCT\_Order\_Charges**‘, but in this case, I am only interested in the ‘Amount’. When I select the ‘Aggregate’ option I can see a number of calculations including ‘Sum of Amount’. I also choose not to have a prefix. However, there are more options next to the ‘Sum of Amount’, as shown below:

![](<Base64-Image-Removed>)

I can also see other calculations associated with the amount, so I choose the ‘Average’ too. This selection changes the ‘Sum of Amount’ title on the Expand / Aggregate screen.

![](<Base64-Image-Removed>)

I choose ‘OK’ (I can click anywhere on the Expand / Aggregate screen to hide the ‘Aggregates of Amount’ dropdown) to see my results. I have deleted some of the irrelevant columns below to make the results easier to view:

![](<Base64-Image-Removed>)

All I need to do now is make my headings and query name more useful, and I have my results ready to load to Excel, using the ‘Close & Load’ option.

![](<Base64-Image-Removed>)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-expanding-on-aggregating/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-expanding-on-aggregating/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-expanding-on-aggregating/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-expanding-on-aggregating/#0)

[](https://sumproduct.com/blog/power-query-expanding-on-aggregating/#0 "close")

top