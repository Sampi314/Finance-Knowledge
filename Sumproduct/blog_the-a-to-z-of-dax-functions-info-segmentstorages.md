# The A to Z of DAX Functions – INFO.SEGMENTSTORAGES

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-segmentstorages/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.SEGMENTSTORAGES

*   April 15, 2025

The A to Z of DAX Functions – INFO.SEGMENTSTORAGES
==================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.SEGMENTSTORAGES
==========================================================================

15 April 2025

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions. This week, we look at **INFO.SEGMENTSTORAGES**._

**_The_** _**INFO.SEGMENTSTORAGES**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/f6891f193d37d3826a39e6180a3215f4.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.SEGMENTSTORAGES** function is one of the system functions. It employs the following syntax:

**INFO.SEGMENTSTORAGES(\[RestrictionName1\],\[RestrictionValue1\],…)**

There are two \[2\] main arguments in this function (excluding numbering):

*   **RestrictionName:** this argument is optional and repeatable this represents the restriction name
*   **RestrictionValue:** this argument is optional and repeatable this represents the restriction value.

Currently, there appears to neither be documentation for this **TMSCHEMA\_SEGMENT\_STORAGES** nor **INFO.SEGMENTSTORAGES.**

We can write this _**INFO.SEGMENTSTORAGES**_ function on DAX query viewto get the sameinformation on the **TMSCHEMA\_SEGMENT\_STORAGES**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_ SEGMENT\_STORAGES** and return an entire table with four \[4\] columns:

![](<Base64-Image-Removed>)

*   **ID**
*   **ColumnPartitionStorageID**
*   **SegmentCount**
*   **StorageFileID**

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stand for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-segmentstorages/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-segmentstorages/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-segmentstorages/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-segmentstorages/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-segmentstorages/#0 "close")

top