# The A to Z of DAX Functions – INFO.CALCULATIONITEMS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationitems/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.CALCULATIONITEMS

*   June 4, 2024

The A to Z of DAX Functions – INFO.CALCULATIONITEMS
===================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.CALCULATIONITEMS
===========================================================================

4 June 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.CALCULATIONITEMS**._

**_The_** _**INFO.CALCULATIONITEMS**_ **_function_**

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we want to query those **$System** schema **DMVs** weuse external tool like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

Now, we just need to write a simple **DAX** syntax to query those **TMSCHEMA** directly in DAX query view. In this instance, we are using **INFO.CALCULATIONITEMS** function to query the **TMSCHEMA\_CALCULATION\_ITEMS**.

The **INFO.CALCULATIONITEMS** function is known as one of the system functions. It employs the following syntax:

**INFO.CALCULATIONITEMS****()**

_i.e._ this function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **CalculationItem** object represents a value that is calculated based upon an expression. It is a child of a **CalculationGroup** object and requires compatibility level 1500 or higher.

We can write this **INFO.CALCULATIONITEMS** function in DAX query viewto get the sameinformation on the **TMSCHEMA\_CALCULATION\_ITEMS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_CALCULATION\_ITEMS** and return an entire table with ten \[10\] columns:

![](<Base64-Image-Removed>)

*   **ID:** thisrepresents a reference to the object
*   **CalculationGroupID:** this represents an ID-based reference to a **CalculationGroup** object
*   **FormatStringDefinitionID:** this represents an ID-based to a **FormatStringDefinition** object
*   **Name:** this presents the name of the object
*   **Description:** this represents the description of the object
*   **ModifiedTime:** this is the time that the object was last modified
*   **State:** this isavalue that provides information about the state of the calculation item. The possible values are as follows:
    *   Ready (1): the calculation item is able to be queried and has up-to-date data
    *   NoData (3): not applicable to **CalculationItem**
    *   CalculationNeeded (4): not applicable to **CalculationItem**
    *   SemanticError (5): the **CalculationItem** expression has a semantic error
    *   EvaluationError (6): not applicable to **CalculationItem**
    *   DependencyError (7): a dependency associated with this calculation item is in an error state (SemanticError, EvaluationError or DependencyError)
    *   Incomplete (8): not applicable to **CalculationItem**
    *   SyntaxError (9): the **CalculationItem** has a syntax error in its expression
*   **ErrorMessage:** this represents the string that explains the error state associated with the current object. It is set by the engine only when the state of the object is one of these three values: SemanticError, DependencyError or EvaluationError
*   **Expression:** this represents the **DAX** expression that is evaluated for the calculation item
*   **Ordinal:**this represents the zero-based ordinal value that is associated with a calculation item. This value is meant to be used as the ordering column in the **DAX** query.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular Model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationitems/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationitems/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationitems/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationitems/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-calculationitems/#0 "close")

top