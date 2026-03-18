# The A to Z of DAX Functions – INFO.LEVELS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-levels/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.LEVELS

*   November 5, 2024

The A to Z of DAX Functions – INFO.LEVELS
=========================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.LEVELS
=================================================================

5 November 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.LEVELS**._

**_The_** _**INFO.LEVELS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/39b3034e2358bf219a3d256d90737988.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.LEVELS** function is one of the system functions. It employs the following syntax:

**INFO.LEVELS()**

_**INFO.LEVELS()**_

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **Level** object represents a **level** in a **hierarchy** that provides a logical hierarchical drilldown path for client applications. It is a child of a **Hierarchy** object. The level is based on the values in a column.

We can write this _**INFO.LEVELS**_ function on DAX query viewto get the sameinformation on the **TMSCHEMA\_LEVELS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_LEVELS** and return an entire table with nine \[9\] columns:

![](<Base64-Image-Removed>)

*   **ID:** this is a reference to the object
*   **HierarchyID:** this is ID-based reference to a **Hierarchy** object
*   **Ordinal:** this is the position of the level within the hierarchy. The levels in the hierarchy MUST be properly ordered, starting with 0 and increasing monotonically
*   **Name:** this is the name of the object
*   **Description:** this is the description of the object
*   **ColumnID:** this is an ID-based reference to a **Column** object
*   **ModifiedTime:** this is thetime that the object was last modified
*   **LineageTag:** this is an optional tag that can be used to define the lineage of a level across different versions of a model. Compatibility level 1600 or higher is required
*   **SourceLineageTag:** this is an optional tag that can be used to define the lineage of a referenced level across different versions of a model. As opposed to **LineageTag**, **SourceLineageTag** can be used to define the lineage of a referenced level rather than a level itself. **SourceLineageTag** is useful when a model references other models by using a Direct Query connection. Compatibility level 1600 or higher is required.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stand for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission
*   there is also a **MDSCHEMA** for **LEVELS** call **MDSCHEMA\_ LEVELS** but its output is not the same as **TMSCHEMA\_LEVELS** and **INFO.LEVELS.**

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-levels/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-levels/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-levels/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-levels/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-levels/#0 "close")

top