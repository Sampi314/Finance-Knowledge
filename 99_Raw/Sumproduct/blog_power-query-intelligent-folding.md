# Power Query: Intelligent Folding

**Source:** https://sumproduct.com/blog/power-query-intelligent-folding/

---

[Home](https://sumproduct.com/)

\> Power Query: Intelligent Folding

*   May 25, 2021

Power Query: Intelligent Folding
================================

Power Query: Intelligent Folding
================================

26 May 2021

_Welcome to our Power Query blog. This week, I look at how Power BI Desktop uses query folding in the Power Query engine._

[Last time](https://sumproduct.com/blog/power-query-folding-table/)
, I looked at what query folding in Power Query is and how it can make queries more efficient.

**Please Note**: at the time of writing, query folding was available on my Access database and I was able to use it to demonstrate some of the concepts.  Query folding is no longer available on this database.  Since Access is a file-based database and not a true database server, query folding may be highly limited or not available. The information in this blog is still valid for databases that can use query folding.

This time, I wish to consider some of the circumstances where Power BI Desktop needs query folding to take place. The requirements for query folding depend upon the **storage mode** for the table linked to the query.

The storage mode describes how Power BI caches the data. It can be viewed or set from the Model view in Power BI Desktop.

For example, in the image below, I have the table ‘**Customers Access**‘, which I have created by importing it from an Access database. Whilst I can view the current storage mode by hovering over the table, the option to potentially change it is hidden in the Properties pane under the Advanced options.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-191.jpg)

I can see that the options for Storage are **Import**, **DirectQuery** and **Dual**:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-249.jpg)

_Microsoft describes the three options as follows:_

1.  **Import**: imported tables with this setting are cached. Queries submitted to the Power BI dataset that return data from Import tables can be fulfilled only from cached data
2.  **DirectQuery**: tables with this setting aren’t cached. Queries that you submit to the Power BI dataset (for example, **DAX** queries) and that return data from **DirectQuery** tables can be fulfilled only by executing on-demand queries to the data source. Queries that you submit to the data source use the query language for that data source, for example, **SQL**
3.  **Dual**: tables with this setting can act as either cached or not cached, depending upon the context of the query that’s submitted to the Power BI dataset. In some cases, you fulfil queries from cached data. In other cases, you fulfil queries by executing an on-demand query to the data source.

The reason that the other options appear greyed out for the ‘Customers Access’ query is because once set to **Import**, a table cannot be changed to **DirectQuery** or **Dual**. **DirectQuery** and **Dual** are only available for databases where Power Query supports the native database query. MS Access is supported for query folding, but you are unable to access the database using a native query.

If I have a table that is **DirectQuery** or **Dual,** then the associated Power Query query must achieve query folding. This means that the whole query can be defined by one **SQL** statement.

Queries are most commonly in **Import** mode, and the recommendations from [last week’s blog](https://sumproduct.com/blog/power-query-folding-table/)
 apply here. Ideally the whole query should be foldable.

If there is a step which is preventing query folding, then there are a couple of approaches that may be taken. It may be possible to transform the data in the original data source so that the step is not needed. If this is not possible, that step could be moved to a native query. There are some limitations to this according to Microsoft:

*   for a **DirectQuery** model table, the query must be a **SELECT** statement, and it can’t use Common Table Expressions (**CTE**s) or a stored procedure
*   incremental refresh cannot use a native **SQL** query; it would force the Power Query mashup engine to retrieve all source rows, and then apply filters to determine incremental changes.

Native **SQL** queries have the potential to change or delete data. In order to prevent this, the account running the query should only have read access.

In summary, when using relational databases as a source for Power BI then query folding is desired, but for **DirectQuery** and **Dual** mode, it is **required**.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-intelligent-folding/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-intelligent-folding/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-intelligent-folding/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-intelligent-folding/#0)

[](https://sumproduct.com/blog/power-query-intelligent-folding/#0 "close")

top