# Power Query: Good Relations

**Source:** https://sumproduct.com/blog/power-query-good-relations/

---

[Home](https://sumproduct.com/)

\> Power Query: Good Relations

*   September 11, 2018

Power Query: Good Relations
===========================

Power Query: Good Relations
===========================

12 September 2018

_Welcome to our Power Query blog. This week, I consider how to upload data from a relational database._

Power Query can be used to upload data from a wide range of sources; truly, it is an excellent tool for cleaning up and formatting data. However, data is rarely static, so there are some good habits that I can adopt when deciding what to upload, particularly from a relational database.

**_Upload Views, not Tables (usually)_**

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-569.jpg)

If I have a table of static or standing data that has come from a relational database like Oracle, then it’s probably fine to upload the underlying table. By this I mean data like countries or towns, which are unlikely to change much. Other data is likely to change a great deal, and this can mean that whole columns may appear and disappear.

The database administrator (DBA) is busy keeping track of in-house programs that might break every time a column is changed, and there is no tool (yet!) that can indicate whether a particular column is used in Power Query. As a programmer, I spent many happy (!) hours trying to track down every possible repercussion when I needed to make a change to a column in a database to enable my new development work to go ahead.

Since I understand the problem, I can make the DBA’s life easier. A view is a virtual table which is created by an SQL statement. It appears just like a normal database table as far as the users of Power Query are concerned. If views are created that helpfully have something in their title to indicate that they are in use by Power Query, _e.g._ ‘Power\_Product\_Details’, this makes it clear that if the column appears in the view, it is being used by Power Query (the same approach can be used for Power BI).

The views can be put into a schema that cover all of the Power Query data, or if the Power Query reports are extensive, into several schema that cover different reporting areas, for example ‘Power\_Accounting’. The view names can be designed to be useful to the DBA, since I can rename them as I import them if I wish.

Also, I should avoid using ‘select \* from _table’_. This is very unpopular with DBA’s as it’s draining and usually lazy! I should select the specific columns that will be used rather than selecting everything just in case. It makes for a much more efficient system – all round.

**What’s in a Name?**

In Power Query, the end user is more important than the programmer. I’ve already mentioned above that views can and often should be renamed when importing to Power Query so that their contents and not their origins are clear. The data may have been cleaned up beautifully, but if the columns are not easy to identify then it’s not going to be useful.

Cleaning titles is important too – **_AcctSuppliers_** is better labelled as **_Suppliers_**, unless I really need to create separate **_Suppliers_** and **_AccountSuppliers_** columns, in which case writing it in full is better, even if the programmer has to type for a little longer. Adopting the use of a capital for each new word is in keeping with **M** language too, an anything which makes **M** seem friendlier has to be a good thing! However, some end users are happier to see words separated by spaces, so it depends on the audience.

Although this is a Power Query blog, I think it best to mention implications elsewhere too. If the data being cleaned up is destined for PowerPivot (or Power BI), then it pays to think ahead. If it is likely that a measure to calculate ‘CostAmount’ will be created further down the line, then having a **_CostAmount_** column will cause issues as the column and the measure can’t have the same name. In this case, **_LineCostAmount_** could be a better choice to allow for a sum to be done later.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-good-relations/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-good-relations/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-good-relations/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-good-relations/#0)

[](https://sumproduct.com/blog/power-query-good-relations/#0 "close")

top