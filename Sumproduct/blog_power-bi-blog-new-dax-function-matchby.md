# Power BI Blog: New DAX Function MATCHBY

**Source:** https://sumproduct.com/blog/power-bi-blog-new-dax-function-matchby/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: New DAX Function MATCHBY

*   August 9, 2023

Power BI Blog: New DAX Function MATCHBY
=======================================

Power BI Blog: New DAX Function MATCHBY
=======================================

10 August 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at a new DAX function available in Power BI: **MATCHBY**._

![](https://sumproduct.com/wp-content/uploads/2025/05/4200bad05f3c473d636eb9fabe4a9737.jpg)

There is a new DAX function in town: **MATCHBY**. When used within any window function, this function defines the columns that are used to determine how to match data and identify the current row. (A window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function.)

For example, below is a query that returns **FactInternetSales** with an added column, which indicates, for each sale, the previous sales amount in descending order of sales from the same product. Using **MATCHBY**, we’re able to indicate that current sales should be identified by the **SalesOrderNumber** and **SalesOrderLineNumber**. Without **MATCHBY**, the query would return an error since there are no key columns in **FactInternetSales** table.

**EVALUATE  
ADDCOLUMNS (  
FactInternetSales,  
“Previous Sales Amount”,  
SELECTCOLUMNS (  
OFFSET (  
\-1,  
FactInternetSales,  
ORDERBY ( FactInternetSales\[SalesAmount\], DESC ),  
PARTITIONBY ( FactInternetSales\[ProductKey\] ),  
MATCHBY( FactInternetSales\[SalesOrderNumber\],  
FactInternetSales\[SalesOrderLineNumber\] )  
),  
FactInternetSales\[SalesAmount\]  
)  
)**

This function can be used within windows functions only.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-new-dax-function-matchby/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-new-dax-function-matchby/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-new-dax-function-matchby/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-new-dax-function-matchby/#0)

[](https://sumproduct.com/blog/power-bi-blog-new-dax-function-matchby/#0 "close")

top