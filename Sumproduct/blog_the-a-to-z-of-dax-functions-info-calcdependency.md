# The A to Z of DAX Functions – INFO.CALCDEPENDENCY

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calcdependency/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.CALCDEPENDENCY

*   July 23, 2024

The A to Z of DAX Functions – INFO.CALCDEPENDENCY
=================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.CALCDEPENDENCY
=========================================================================

23 July 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions. This week, we look at **INFO.CALCDEPENDENCY**._

**_The_** _**INFO.CALCDEPENDENCY**_ **_function_**

![](<Base64-Image-Removed>)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

Now, we just need to write a simple **DAX** syntax to query those **DISCOVER** directly in DAX query view. In this instance, we are using **INFO.CALCDEPENDENCY** function to query the **DISCOVER\_CALC\_DEPENDENCY**.

The **INFO.CALCDEPENDENCY** function is one of the system functions. It employs the following syntax:

**INFO.CALCDEPENDENCY****()**

This function has no parameters.

Based upon the _‘\[MS-SSAS\]: SQL Server Analysis Services Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas/854a72f2-d637-4be3-b60f-6a44422e80c9)
), the **DISCOVER\_CALC\_DEPENDENCY** schema rowset returns information about the calculation dependency for an object that is specified in a Tabular database or in a **DAX** query that is executed against a Tabular database.

We can write this **INFO.CALCDEPENDENCY** function on DAX query viewto get the sameinformation on the **DISCOVER\_CALC\_DEPENDENCY**:

![](<Base64-Image-Removed>)

Itwill query **$SYSTEM.DISCOVER\_CALC\_DEPENDENCY** and return an entire table with 10 columns:

![](<Base64-Image-Removed>)

*   **\[DATABASE\_NAME\]:** this represents the name of the database
*   **\[OBJECT\_TYPE\]:** this represents the type of the object for which dependency analysis is requested
    *   for object that are in Tabular models at compatibility level 1100 or 1103, the following are the possible types:
        *   **QUERY:** a query
        *   **COLUMN:** a regular column
        *   **CALC\_COLUMN:** a calculated column
        *   **HIERARCHY:** a hierarchy
        *   **MEASURE:** a measure
        *   **ACTIVE\_RELATIONSHIP:** an active relationship
        *   **RELATIONSHIP:** a relationship
        *   **ROWS\_ALLOWED:** the number of rows allowed
    *   for objects that are in Tabular models at compatibility level 1200 or higher, the following are the possible types:
        *   **CALC\_COLUMN:** a calculated column
        *   **MEASURE:** a measure
        *   **RELATIONSHIP:** a relationship
        *   **ACTIVE\_RELATIONSHIP:** an active relationship
        *   **CALC\_TABLE:** a calculated table
        *   **HIERARCHY:** a hierarchy
        *   **ATTRIBUTE\_HIERARCHY:** an attribute hierarchy
        *   **ROWS\_ALLOWED:** the number of rows allowed
        *   **DETAIL\_ROWS\_EXPR:** a detail rows definition
        *   **PARTITION:** a partition
        *   **M\_EXPRESSION:** an **M** expression, as defined in [\[MS-SSAS-T\]](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
            . Requires compatibility level 1400 or higher
        *   **QUERY:** a query
*   **\[TABLE\]:** this is the name of the table that contains the object for which dependency information is sought
*   **\[OBJECT\]:** this is the name of the object for which dependency information is sought
*   **\[EXPRESSION\]:** this is the formula of the object for which dependency information is sought
*   **\[REFERENCED\_OBJECT\_TYPE\]:** this returns the type of the object that has a dependency on the referenced object
    *   for objects that are returned by Tabular models at compatibility level 1100 or 1103, the following are the possible types:
        *   **CALC\_COLUMN:** a calculated column
        *   **COLUMN:** a column of data
        *   **MEASURE:** a measure
        *   **RELATIONSHIP:** a relationship
        *   **HIERARCHY:** a hierarchy.
    *   for objects that are returned by Tabular models at compatibility level 1200 or higher, the following are the possible types:
        *   **COLUMN:** a column of data
        *   **CALC\_COLUMN:** a calculated column
        *   **MEASURE:** a measure
        *   **RELATIONSHIP:** a relationship
        *   **ACTIVE\_RELATIONSHIP:** an active relationship
        *   **TABLE:** a table
        *   **CALC\_TABLE:** a calculated table
        *   **ATTRIBUTE\_HIERARCHY:** an attribute hierarchy
        *   **DETAIL\_ROWS\_EXPR:** a detail rows definition
        *   **DATASOURCE:** a data source
        *   **M\_EXPRESSION:** an **M** expression, as defined in [\[MS-SSAS-T\]](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
            . Requires compatibility level 1400 or higher
        *   **HIERARCHY:** a hierarchy
        *   **CALCULATION\_ITEM:** a calculation item
        *   **CALCULATION\_ITEM\_FORMAT\_STRING:** a calculation item format string
*   **\[REFERENCED\_TABLE\]:** this is the name of the table that contains the dependent object
*   **\[REFERENCED\_OBJECT\]:** this is the name of the object that has a dependency on the referenced object
*   **\[REFERENCED\_EXPRESSION\]:** this is a formula that is dependent on the referenced object. In a calculated table, a calculated column, or a measure, the formula can be a **DAX** expression. In a partition, the formula can be a provider data source expression or an **M** languageexpression
*   **\[QUERY\]:** given a specific **DAX** query, if the query contains a measure, the rowset shows each object on which the **DAX** query has a dependency.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema**
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_.__If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_[_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calcdependency/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calcdependency/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calcdependency/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calcdependency/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calcdependency/#0 "close")

top