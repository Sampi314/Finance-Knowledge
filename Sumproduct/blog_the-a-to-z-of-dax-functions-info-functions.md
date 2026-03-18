# The A to Z of DAX Functions – INFO.FUNCTIONS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-functions/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.FUNCTIONS

*   September 24, 2024

The A to Z of DAX Functions – INFO.FUNCTIONS
============================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.FUNCTIONS
====================================================================

24 September 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.FUNCTIONS**._

**_The_** _**INFO.FUNCTIONS**_ **_function_**

![](<Base64-Image-Removed>)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

Now, we just need to write a simple **DAX** syntax to query those **MDSCHEMA** directly in DAX query view. In this instance, we are using **INFO.FUNCTIONS** function to query the **MDSCHEMA\_FUNCTIONS**.

The **INFO.FUNCTIONS** function is one of the system functions. It employs the following syntax:

**INFO.FUNCTIONS()**

This function has no parameters.

Based upon the _‘\[MS-SSAS\]: SQL Server Analysis Services Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas/854a72f2-d637-4be3-b60f-6a44422e80c9)
), the **MDSCHEMA\_FUNCTIONS** schema rowset returns information about the functions that are currently available for use in the **DAX** and **MDX** languages.

We can write this **INFO.FUNCTIONS** function on DAX query viewto get the sameinformation on the **MDSCHEMA\_FUNCTIONS**:

![](<Base64-Image-Removed>)

Itwill query **$SYSTEM.****MDSCHEMA\_FUNCTIONS** and return an entire table with 15 columns:

![](<Base64-Image-Removed>)

*   **FUNCTION\_NAME:** this is the name of the function
*   **DESCRIPTION:** this is a description of the function
*   **PARAMETER\_LIST:** this is a description the parameters accepted by the function
*   **RETURN\_TYPE:** this is the OLE DB data type that is returned by the function
*   **ORIGIN:** the possible values are as follows:
    *   (0x1) MSOLAP
    *   (0x2) UDF
    *   (0x3) RELATIONAL
    *   (0x4) SCALAR
*   **INTERFACE\_NAME:** this is a logical classification of the type of function. For example:
    *   DATETIME
    *   LOGICAL
    *   FILTER
*   **LIBRARY\_NAME:** this is the library that implements the function
*   **DLL\_NAME:** this isunused
*   **HELP\_FILE:** this isunused
*   **HELP\_CONTEXT:** this isunused
*   **OBJECT:** this is thetypeof object on which this function can be called. For example, the **Children** MDX function can be called on a **Member** object
*   **CAPTION:** this is the caption of the function
*   **PARAMETERINFO:** this is the parameters that can be provided to this function
*   **DIRECTQUERY\_PUSHABLE:** this is a bitmask that indicates the scenarios in which this function can be used when the model is in DirectQuery mode. The possible values are as follows:
    *   **(0x1) MEASURE:** This function can be used in measure expressions
    *   **(0x2) CALCCOL:** This function can be used in calculated column expressions
*   **VISUAL\_CALCULATIONS\_INFO:** this is not mentioned in the current MS-SSAS (14 May 2024) document.

Here are a few remarks about function come with **INFO** prefix:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema**.
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-functions/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-functions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-functions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-functions/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-functions/#0 "close")

top