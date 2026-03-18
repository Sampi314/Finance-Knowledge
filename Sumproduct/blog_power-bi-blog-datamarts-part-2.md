# Power BI Blog: Datamarts – Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-datamarts-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Datamarts – Part 2

*   November 30, 2022

Power BI Blog: Datamarts – Part 2
=================================

Power BI Blog: Datamarts – Part 2
=================================

1 December 2022

Datamarts are self-service analytics solutions, enabling users to store and explore data that is loaded in a fully managed database. Since datamarts are usually a subset of the full database, teams can be given access only to the information they require, enabling them to share relevant data and insights within those teams.

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/datamarts-part-1)
, we looked at the differences between a datamart and a dataset, and the advantages of using a datamart.

This week, we’ll look at the most common forms of datamarts:

1.  the first is a dependent datamart. This is the best solution for huge corporations, as this method allows for the establishment of a consolidated and easy-to-manage system. In This model, all datamarts connect to single centralised database that contains the data.
2.  the second type is an independent datamart, which means decentralised. This structure is ideal for smaller businesses, who may access their data from a variety of sources. The datamart isn’t linked to a warehouse in any way. All the data is queried from other sources, using ETL tools
3.  the third type is a hybrid, which can acquire information from various warehouses as well as other datamarts. All data required to run the business successfully is organised into a schema. Datamarts can use one of two different schemas:

a. a star schema, which implies there is only one fact table that links to data from multiple dimension tables

![](<Base64-Image-Removed>)

b. a snowflake schema, which is a modified star schema in which dimension tables link to further tables in a normalised structure. Normalised means that data is not repeated in different tables, for example an address would only be stored once, even if it was associated with different customers or transactions.

![](<Base64-Image-Removed>)

Next time, we will look in more detail at the differences between a datamart and a data warehouse.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-datamarts-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-datamarts-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-datamarts-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-datamarts-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-datamarts-part-2/#0 "close")

top