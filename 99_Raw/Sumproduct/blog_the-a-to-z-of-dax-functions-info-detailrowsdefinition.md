# The A to Z of DAX Functions – INFO.DETAILROWSDEFINITION

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-detailrowsdefinition/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.DETAILROWSDEFINITION

*   August 13, 2024

The A to Z of DAX Functions – INFO.DETAILROWSDEFINITION
=======================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.DETAILROWSDEFINITION
===============================================================================

13 August 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.DETAILROWSDEFINITION**._

**_The_** _**INFO.DETAILROWSDEFINITION**_ **_function_**

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](https://sumproduct.com/wp-content/uploads/2025/06/10056c9bf0bb13f57dbd6b926374060a.jpg)

The **INFO.DETAILROWSDEFINITION** function is one of the system functions. It employs the following syntax:

**INFO.DETAILROWSDEFINITION()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **DetailRowsDefinition** object represents an unnamed table expression in **DAX**. It is a child of a **Measure** or a **Table** object and requires compatibility level 1400 or higher.

We can write this **INFO.DETAILROWSDEFINITION** function in DAX query viewto get the sameinformation on the **TMSCHEMA\_DETAIL\_ROWS\_DEFINITIONS**:

![](https://sumproduct.com/wp-content/uploads/2025/06/60150e0c0cf11f7dcbae351fbcde8a12.jpg)

Itwill query the **$SYSTEM.****TMSCHEMA\_DETAIL\_ROWS\_DEFINITIONS** and return an entire table with seven \[7\] columns:

![](https://sumproduct.com/wp-content/uploads/2025/06/fe0e7866e980bb7389de33ce41989ac0.jpg)

*   **ID**: thisrepresents a reference to the object
*   **ObjectID**: this is an ID-based reference to a **Measure** or **Table** object
*   **ObjetcType**: this is the data type of the object specified by **ObjectID**. The possible values are as follows:
    *   TM\_TYPEID\_Table (3)
    *   TM\_TYPEID\_Measure (8)
*   **Expression**: this represents the DAX detail rows expression for a table type
*   **ModifiedTime**: this is the time that the object was last modified
*   **State**: this is a value that provides information about the state of the parent object or the container object. The possible values are as follows:
    *   Ready (1) – the object expression is queryable and the data is in an up-to-date state
    *   NoData (3) – not applicable
    *   CalculationNeeded (4) – not applicable
    *   SemanticError (5) – the object expression has a semantic error
    *   EvaluationError (6) – not applicable
    *   DependencyError (7) – a dependency associated with the **DetailRowsDefinition** object is in an error state (SemanticError, EvaluationError, or DependencyError)
    *   Incomplete (8) – not applicable
    *   SyntaxError (9) – the object has a syntax error in its expression.
*   **ErrorMessage**: this is a string that explains the error state that is associated with the **DetailRowsDefinition** object. It is set by the engine only when the state of the object is one of these three values:
    *   SemanticError
    *   DependencyError
    *   SyntaxError.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-detailrowsdefinition/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-detailrowsdefinition/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-detailrowsdefinition/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-detailrowsdefinition/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-detailrowsdefinition/#0 "close")

top