# Power BI Blog: Datamarts – Part 7

**Source:** https://sumproduct.com/blog/power-bi-blog-datamarts-part-7/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Datamarts – Part 7

*   January 4, 2023

Power BI Blog: Datamarts – Part 7
=================================

Power BI Blog: Datamarts – Part 7
=================================

5 January 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we_ _will create our own query within a datamart._

Datamarts are self-service analytics solutions, enabling users to store and explore data that is loaded in a fully managed database. Since datamarts are usually a subset of the full database, teams may be given access to the information they require only, enabling them to share relevant data and insights within those teams.

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/datamarts-part-6)
, we looked at the options to refresh available within a datamart. This week, we’ll demonstrate how to create **SQL** queries.

Clicking on the **SQL** icon (shown below), allows us to construct a query by typing in **SQL** code:

![](<Base64-Image-Removed>)

Using our example, we may add the **Sales** table and perform an inner join with the **SalesOrder** table.

![](<Base64-Image-Removed>)

**SQL** may be used to group and perform counts and aggregations directly in the web browser. In this way, analysis can be performed through external clients. The **SQL** connection string may be viewed via ‘Settings’. This option is accessible from the menu for the appropriate workspace.

![](<Base64-Image-Removed>)

In the settings windows, click on ‘Server settings’ and choose to Copy the ‘Connection string’, which is the string which will allow an external user to connect to the database:

![](<Base64-Image-Removed>)

We are now able to connect to the datamart by pasting the connection string into an **SQL** client. Once connected, we may run **DQL** (Data Query Language) queries using the **SQL** client.

![](<Base64-Image-Removed>)

Next time, we will look at creating reports using a datamart.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-datamarts-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-datamarts-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-datamarts-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-datamarts-part-7/#0)

[](https://sumproduct.com/blog/power-bi-blog-datamarts-part-7/#0 "close")

top