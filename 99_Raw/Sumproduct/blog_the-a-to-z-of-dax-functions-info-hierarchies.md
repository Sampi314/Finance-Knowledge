# The A to Z of DAX Functions – INFO.HIERARCHIES

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-hierarchies/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.HIERARCHIES

*   October 15, 2024

The A to Z of DAX Functions – INFO.HIERARCHIES
==============================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.HIERARCHIES
======================================================================

15 October 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.HIERARCHIES**._

**_The_** _**INFO.HIERARCHIES**_ **_function_**

![](<Base64-Image-Removed>)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.HIERARCHIES** function is one of the system functions. It employs the following syntax:

**INFO.HIERARCHIES()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **Hierarchy** object represents a collection of **levels** that provide a logical hierarchical drilldown path for client applications. It is a child of a **Table** object.

We can write this **INFO.HIERARCHIES** function on DAX query viewto get the sameinformation on the **TMSCHEMA\_HIERARCHIES**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_HIERARCHIES** and return an entire table with 14 columns:

![](<Base64-Image-Removed>)

*   **ID:** this is a reference to the object
*   **TableID:** this is an ID-based reference to a Table object
*   **Name:** this is the name of the object
*   **Description:** this is the description of the object
*   **IsHidden:** a Boolean that indicates whether the **hierarchy** is treated as hidden by client visualisation tools. If the hierarchy is treated as hidden by client visualisation tools, it is “true”; otherwise, it is “false”
*   **State:** this represents a value that provides information about the state of the hierarchy. The possible values and their interpretation are as follows:
    *   Ready (1) – the hierarchy is queryable and has up-to-date data
    *   NoData (3) – not applicable to **Hierarchy**
    *   CalculationNeeded – the hierarchy does not contain any data because it was not refreshed. No error is associated with the hierarchy
    *   SemanticError (5) – not applicable to **Hierarchy**
    *   EvaluationError (6) – not applicable to **Hierarchy**
    *   DependencyError (7) – a dependency associated with the hierarchy is in an error state (SemanticError, EvaluationError, or DependencyError)
    *   Incomplete (8) – Not applicable to **Hierarchy**
*   **HierarchyStorageID:** this is an ID-based reference to a **HierarchyStorage** object. The **HierarchyStorage** object is reserved for internal use only
*   **ModifiedTime:** this is the time that the object was last modified
*   **StructureModifiedTime:** this is the time that the structure of the object was last modified
*   **RefreshedTime:** this is the time that the object was last refreshed
*   **DisplayFolder:** this defines the display folder in which the hierarchy is displayed by the client applications
*   **HideMembers:** this is a value that allows the members of a ragged / unbalanced hierarchy to be hidden. Compatibility level 1400 or higher is required. The possible values are as follows:
*   o Default (0) – the members are not to be hidden
*   o HideBlankMembers (1) – the members that have blank values are to be hidden
*   **LineTag:** this is an optional tag that can be used to define the lineage of a hierarchy across different versions of a model. Compatibility level 1600 or higher is required
*   **SourceLineageTag:** An optional tag that can be used to define the lineage of a referenced hierarchy across different versions of a model. As opposed to **LineageTag**, **SourceLineageTag** can be used to define the lineage of a referenced hierarchy rather than a hierarchy itself. **SourceLineageTag** is useful when a model references other models by using a Direct Query connection. Compatibility level 1600 or higher is required.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stand for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission
*   there is also a **MDSCHEMA** for **HIERARCHIES** call **MDSCHEMA\_ HIERARCHIES** but its output is not the same as **TMSCHEMA\_HIERARCHIES** and **INFO.HIERARCHIES.**

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-hierarchies/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-hierarchies/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-hierarchies/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-hierarchies/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-hierarchies/#0 "close")

top