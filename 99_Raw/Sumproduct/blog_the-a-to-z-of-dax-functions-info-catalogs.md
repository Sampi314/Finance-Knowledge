# The A to Z of DAX Functions – INFO.CATALOGS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-catalogs/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.CATALOGS

*   August 27, 2024

The A to Z of DAX Functions – INFO.CATALOGS
===========================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.CATALOGS
===================================================================

27 August 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions. This week, we look at **INFO.CATALOGS**._

**_The_** _**INFO.CATALOGS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/d66017c7be23f1b5655d63e59fba75be.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

Now, we just need to write a simple **DAX** syntax to query those **DBSCHEMA** directly in DAX query view. In this instance, we are using **INFO.CATALOGS** function to query the **DBSCHEMA\_CATALOGS**.

The **INFO.CATALOGS** function is one of the system functions. It employs the following syntax:

**INFO.CATALOGS()**

This function has no parameters.

Based upon the _‘\[MS-SSAS\]: SQL Server Analysis Services Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas/854a72f2-d637-4be3-b60f-6a44422e80c9)
), the **DBSCHEMA\_CATALOGS** schema rowset the catalogues that are accessible on the server.

We can write this **INFO.CATALOGS** function on DAX query viewto get the sameinformation on the **DBSCHEMA\_CATALOGS**:

![](<Base64-Image-Removed>)

Itwill query **$SYSTEM.****DBSCHEMA\_CATALOGS** and return an entire table with 15 columns:

![](<Base64-Image-Removed>)

*   **CATALOG\_NAME:** this is thecatalogue name
*   **DESCRIPTION:** this is the catalogue description
*   **ROLES:** this is a comma-delimited list of roles to which the current user belongs
*   **DATE\_MODIFIED:** this is the date that the catalogue was last modified
*   **COMPATIBILITY\_LEVEL:** this represents the compatibility level of the database
*   **TYPE:** this is a mask with the following flags
    *   **(0x0) Multidimensional:** if the other bits are not set, the database is a Multidimensional database
    *   **(0x1) TabularMetadata:** the Tabular model is built by using Tabular metadata
    *   **(0x2) TabularModel:** this is a Tabular model, including those built using Tabular or Multidimensional metadata
*   **VERSION:** this is a database that uses Tabular Metadata will return the current version of the database. Otherwise, the value will be zero \[0\]
*   **DATABASE\_ID:** this is the ID of the database object
*   **DATABASE\_GUID:** this is not mentioned in the MS-SSAS document as at the time of writing (14 May 2024)
*   **DATE\_QUERIED:** thisis unused
*   **CURRENTLY\_USED:** thisis unused
*   **POPULARITY:** this is a measure of how frequently the database is used. The value is empty for the system tracker
*   **WEIGHTEDPOPULARITY:** this isa measure of how frequently the database is used, expressed as a fraction with respect to the other databases. The value is empty for the system tracker
*   **CLIENTCACHEREFRESHPOLICY:** thisis a hint to the client applications about when their data caches, if any SHOULD be refreshed after a **Refresh** command changes the data on the server. The possible values are as follows:
    *   **0:** client applications are notified to refresh their caches only if a user query/interaction needs newer data
    *   **\-1 (default):** client applications are notified to allow all background cache refreshes
*   **ENCRYPTION\_LEVEL:** this is not mentioned in the current MS-SSAS document as at the time of writing (14 May 2024).

Here are two \[2\] remarks about function come with **INFO** prefix:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema**.
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_[_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-catalogs/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-catalogs/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-catalogs/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-catalogs/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-catalogs/#0 "close")

top