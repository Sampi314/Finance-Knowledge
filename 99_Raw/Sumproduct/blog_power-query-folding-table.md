# Power Query: Folding Table

**Source:** https://sumproduct.com/blog/power-query-folding-table/

---

[Home](https://sumproduct.com/)

\> Power Query: Folding Table

*   May 18, 2021

Power Query: Folding Table
==========================

Power Query: Folding Table
==========================

19 May 2021

_Welcome to our Power Query blog. This week, I look at Query Folding._

I am going to talk about query folding this week. **Query folding**, in essence, is the ability for a routine to generate a single query statement to retrieve and transform source data. This technique is used to reduce the number of times a query is read when loading to the data model.

**Please Note**: at the time of writing, query folding was available on my Access database and I was able to use it to demonstrate some of the concepts.  Query folding is no longer available on this database.  Since Access is a file-based database and not a true database server, query folding may be highly limited or not available. The information in this blog is still valid for databases that can use query folding.

To illustrate, I have some sales data from an Access database that holds the data for my imaginary tent hire business:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-196.jpg)

I am going to use this query to see how query folding works with data sources that are associated with a query language. This is a new record for the number of times “query” occurs in one sentence!

If a query is going to be used in Power Pivot or Power BI, then it’s important to know what query folding is, and how it can help make the data model more efficient. Query folding will help with suitable data models used by Power Pivot or Power BI because refreshes will be more efficient. The incremental refresh, available in Power BI, is only advised if query folding is in place. In Power BI, DirectQuery and Dual storage mode tables may only be used for queries that can be folded.

According to Microsoft:

Query folding is the ability for a Power Query query to generate a single query statement to retrieve and transform source data. The Power Query mashup engine strives to achieve query folding whenever possible for reasons of efficiency.

Most data sources that have the concept of a query language support query folding. These data sources can include relational databases, OData feeds (including SharePoint lists), Exchange, and Active Directory. However, data sources like flat files, blobs and web typically do not.

For queries performed upon database data, the first steps of Power Query look like normal steps but are actually performed in the database using **SQL** (**S**tructured **Q**uery **L**anguage). The single **SQL** query can be listed in the query as multiple **M** steps, which helps the user to understand the actions of the query. If the user adds steps that can be done directly in the database, these will be added to the **SQL** query. Communicating directly with the database in this way is faster and means that any “real” power query steps are dealing with the subset of data, rather than the whole database.

Query folding works by default with supported sources. It can be stopped by implementing a user-created **SQL** query to connect to the database. This effectively stops the Power Query steps that would have been directly in the database. This is an area of ongoing development, and in some cases, the user can add a parameter to allow query folding – but I will cover this in a future blog.

The steps that have taken place in the database may be identified by right-clicking. If a “native query” is available, this will give the **SQL** query behind the **M** step. The database steps will always be at the beginning of the query and will stop once Power Query encounters a step which cannot be carried out in **SQL**. It’s possible, and desirable in terms of efficiency, for every step to be part of the **SQL** query.

However, the “native query” is not always available, even if the query is folded. Therefore, back to Microsoft:

It doesn’t work for OData based connectors, for example, even though there is folding occurring on the backend. The Query Diagnostics feature is the best way to see what folding has occurred for non-**SQL** connectors (although the steps that fold aren’t explicitly called out—you just see the resulting URL that was generated).

If the whole query could be written logically as a single **SQL** select statement (including Where, Group By and Join), then the whole query can be folded. This can also extend to include columns that have been created using functions that could also be specified in **SQL**.

Therefore, looking at the ‘Expanded NewColumn’ step in my query, I can right click and see if the “native query” (Native Query) option is available:

![](<Base64-Image-Removed>)

Note that Native Query was not available for the ‘Source’ step because the **SQL** for that step has been combined with the ‘Expanded NewColumn’ step.

![](<Base64-Image-Removed>)

This step clearly includes the join from the ‘Source’ step. These steps cannot be distinct in **SQL**.

When creating new steps, Microsoft provides the following list of transformations that may be included in query folding. The descriptions in brackets \[**()**\] indicate the **SQL** syntax that the Power Query transformation corresponds to:

*   _Removing columns_
*   _Renaming columns (SELECT column aliases)_
*   _Filtering rows, with static values or Power Query parameters (WHERE clause predicates)_
*   _Grouping and summarizing (GROUP BY clause)_
*   _Expanding record columns (source foreign key columns) to achieve a join of two source tables (JOIN clause)_
*   _Non-fuzzy merging of fold-able queries based on the same source (JOIN clause)_
*   _Appending fold-able queries based on the same source (UNION ALL operator)_
*   _Adding custom columns with simple logic (SELECT column expressions). Simple logic implies uncomplicated operations, possibly including the use of **M** functions that have equivalent functions in the SQL data source, like mathematic or text manipulation functions. For example, the following expressions returns the year component of the **OrderDate** column value (to return a numeric value)_

_powerquery-mCopy_

_Date.Year(\[OrderDate\])_

*   _Pivoting and unpivoting (PIVOT and UNPIVOT operators)._

They also provide a list of transformations that cannot be folded:

*   _Merging queries based on different sources_
*   _Appending (union-ing) queries based on different sources_
*   _Adding custom columns with complex logic. Complex logic implies the use of **M** functions that have no equivalent functions in the data source. For example, the following expressions formats the **OrderDate** column value (to return a text value)_

_powerquery-mCopy_

_Date.ToText(\[OrderDate\], “yyyy”)_

*   _Adding index columns_
*   _Changing a column data type._

If these steps need to be done in a query with query folding, they should be undertaken after the foldable steps if possible.

In my query, the first step that is not folded is the second sort:

![](<Base64-Image-Removed>)

Clearly, it’s not as simple as a particular transformation type being ‘foldable’. The first sort was fine, but the second sort has come at a point in the **SQL** query when it was not possible to create the syntax. The **SQL** for my query ends at the previous step ‘Grouped Rows’.

![](<Base64-Image-Removed>)

Adding another sort to this isn’t possible. The first sort had been added as an ‘order’ by section:

![](<Base64-Image-Removed>)

This was then incorporated into the ‘Group By’ section, and another ‘order by’ is not possible. In this case it isn’t the only reason stopping my query from being completely folded since the ‘Changed Type’ step is in the list of non-foldable transformations. If it were the only step preventing my query from being completely foldable, then I ought to consider whether it was necessary.

There are other ways to interrupt query folding in sources used in Power BI Desktop: if a query is built from multiple data sources, even if they all support query folding, the data source privacy levels need to be compatible.

I’ll look more at using query folding with Power BI next time.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-folding-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-folding-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-folding-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-folding-table/#0)

[](https://sumproduct.com/blog/power-query-folding-table/#0 "close")

top