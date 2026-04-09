# The A to Z of DAX Functions – INFO.VARIATIONS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-variations/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.VARIATIONS

*   June 17, 2025

The A to Z of DAX Functions – INFO.VARIATIONS
=============================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions.  This week, we look at **INFO.VARIATIONS**._

**_The_** _**INFO.VARIATIONS**_ **_function_**

![](<Base64-Image-Removed>)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems.  **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model.  They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** we used external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The _**INFO.VARIATIONS**_ function is one of the system functions.  It employs the following syntax:

> **INFO.VARIATIONS (\[RestrictionName1\], \[RestrictionValue1\], …)**

There are two \[2\] main arguments in this function (excluding numbering):

*   **RestrictionName:** this argument is optional and repeatable this represents the restriction name
*   **RestrictionValue:** this argument is optional and repeatable this represents the restriction value.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas/854a72f2-d637-4be3-b60f-6a44422e80c9)
), the **Variation** object defines the references that are used in the variations of a column.  **Variation** is a child of a **Column** object and requires compatibility level 1400 or higher.

We can write this _**INFO.VARIATIONS**_ function in DAX query view to get the same information on the **TMSCHEMA\_VARIATIONS**:

![](<Base64-Image-Removed>)

It will query the **$SYSTEM.TMSCHEMA\_VARIATIONS** and return an entire table with eight \[8\] columns:

![](<Base64-Image-Removed>)

*   **ID:** this is a reference to the object
*   **ColumnID:** this is an ID-based reference to a **Column** object
*   **Name:** this is the name of the object
*   **Description:** this is the description of the object
*   **RelationshipID:** this is an ID-based reference to a **Relationship** object
*   **DefaultHierarchyID:** this is an ID-based reference to a **Hierarchy** object
*   **DefaultColumnID:** this is an ID-based reference to a **Column** object
*   **IsDefault:** this is a Boolean that indicates whether this Variation object is the column’s default variation.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-variations/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-variations/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-variations/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-variations/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-variations/#0 "close")

top