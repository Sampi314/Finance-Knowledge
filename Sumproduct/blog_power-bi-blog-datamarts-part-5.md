# Power BI Blog: Datamarts – Part 5

**Source:** https://sumproduct.com/blog/power-bi-blog-datamarts-part-5/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Datamarts – Part 5

*   December 21, 2022

Power BI Blog: Datamarts – Part 5
=================================

Power BI Blog: Datamarts – Part 5
=================================

22 December 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we_ _will look at generating queries using the user interface (UI) available for datamarts._

Datamarts are self-service analytics solutions, enabling users to store and explore data that is loaded in a fully managed database. Since datamarts are usually a subset of the full database, teams may be given access to the information they require only, enabling them to share relevant data and insights within those teams.

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/datamarts-part-4)
, we began looking at how Power BI supports datamarts. This week, let’s take a look at how we may create queries within a datamart.

![](<Base64-Image-Removed>)

The design icon on the bottom left-hand side allows us to select, drag and filter tables, remove columns and merge or append queries. In this example, we want to find the top sales order, thus the **Sales** and **SalesOrder** tables have been selected and dragged to the stage screen. Then, we can press the plus icon (**+**) as shown below:

![](<Base64-Image-Removed>)

We may then select to ‘Merge queries as new’.

![](<Base64-Image-Removed>)

Like transforming data in Power BI desktop, merging queries allows us to select the tables to merge (_i.e._ incorporate additional columns / fields). We must specify the matching columns and the ‘Join kind’, by choosing the appropriate icon.

![](<Base64-Image-Removed>)

With our tables merged, we can click the plus icon in the merged table, and select ‘Group by’:

![](<Base64-Image-Removed>)

In the dialog that pops-up, we select **Sales Order** in the ‘Group by’ section and call the new column **Total Sales**. We select Sum as the Operation and **Sales Amount** as the Column to be summed:

![](<Base64-Image-Removed>)

After pressing OK, we have a table of each **Sales Order** and the total corresponding **Sales Amount**:

![](<Base64-Image-Removed>)

Next time, we will look at the refresh options for datamarts.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-datamarts-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-datamarts-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-datamarts-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-datamarts-part-5/#0)

[](https://sumproduct.com/blog/power-bi-blog-datamarts-part-5/#0 "close")

top