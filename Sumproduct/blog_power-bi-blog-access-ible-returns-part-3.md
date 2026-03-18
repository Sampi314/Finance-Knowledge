# Power BI Blog: Access-ible Returns Part 3

**Source:** https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-3/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Access-ible Returns Part 3

*   August 11, 2021

Power BI Blog: Access-ible Returns Part 3
=========================================

Power BI Blog: Access-ible Returns Part 3
=========================================

12 August 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we continue our Access-ible series of Blogs._

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-access-ible-returns-part-2)
, we extracted more meaningful table names from the imported data. We have repeated this process for the other tables:

![](<Base64-Image-Removed>)

The table names now make more sense for the star schema centred around **Response Status**. However, we have another schema to the right, which we don’t need to see in Power BI, as we will not be using the tables for reporting purposes. We can choose not to load these tables to Power BI by going back to the Power Query engine using the ‘Transform data’ tab.

In the Query pane to the left, we have a list of queries. We can right-click on the queries we don’t need to see in Power BI and disable them.

![](<Base64-Image-Removed>)

By unchecking ‘Enable load’ we can reduce the amount of processing needed to upload our data and streamline the Fields available in Power BI. When we do this, we get a warning to make sure we will not be using the Fields from these tables in Power BI.

![](<Base64-Image-Removed>)

We uncheck ‘Enable load’ for **values16**, **vartable16**, **Table Names** and **Source with Names**. This changes the query names to _italics_ which makes it easy to see which queries are set to load to Power BI.

![](<Base64-Image-Removed>)

When we ‘Close & Apply’, we only have one star schema.

![](<Base64-Image-Removed>)

We only see the tables where we left ‘Enable Load’ switched on in the Fields list:

![](<Base64-Image-Removed>)

Now our tables are tidy, we need to look at the column names. This is a complicated process, which we will be starting this week. To begin, we go back to the Power Query engine. We start by looking at **vartable16**.

![](<Base64-Image-Removed>)

We will need the original table name to link to **TableName** to pick up the column names. However, we don’t have the original table name in our renamed tables! We should have stored the original table name so that we could link. Does this mean we have to delete everything and start again? No! The beauty of the Power Query Editor is that nothing is ever actually deleted, and we can go back to a step and modify it. In this case, we need to go back to each of our loaded tables and amend one step. We will use **Custom comparison groups** as an example and look at the little gear next to the ‘Remove Other Columns’ step.

![](<Base64-Image-Removed>)

We can tick **Name** as well as **Data**, so we do this.

![](<Base64-Image-Removed>)

The next step ‘Expanded Data’ still works, and now we have the original table name on each row ready to link.

![](<Base64-Image-Removed>)

We repeat this process for all out loaded tables. Now we can go back to **vartable16** to see what columns we need to use.

![](<Base64-Image-Removed>)

We have reordered the columns to show all the required columns. We need to link to **TableName** and **varName** to extract **varTitle**. We have the **Name** column to link to **TableName**, but we will need to use the current column names to link to **varTitle**. Since we can’t merge using a column name, we need to create a function.

We start by creating a reference query from **vartable16**.

![](<Base64-Image-Removed>)

We will call the new query **vartable function**.

![](<Base64-Image-Removed>)

Next time, we will create a function which will take a table name and column heading and return the associated descriptive column heading in **varTitle**.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-3/#0)

[](https://sumproduct.com/blog/power-bi-blog-access-ible-returns-part-3/#0 "close")

top