# The A to Z of DAX Functions – INFO.ATTRIBUTEHIERARCHIES

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-attributehierarchies/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.ATTRIBUTEHIERARCHIES

*   May 14, 2024

The A to Z of DAX Functions – INFO.ATTRIBUTEHIERARCHIES
=======================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.ATTRIBUTEHIERARCHIES
===============================================================================

14 May 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.ATTRIBUTEHIERARCHIES**._

**The** **INFO.ATTRIBUTEHIERARCHIES** **function**

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs**,we would use external tools like **Tabular Editor** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

Now, we just need to write a simple **DAX** syntax-based formula to query these **TMSCHEMA** directly in DAX query view. In this instance, we are using **INFO.ATTRIBUTEHIERARCHIES** function to query the **TMSCHEMA\_ATTRIBUTE\_HIERARCHIES**.

The **INFO.ATTRIBUTEHIERARCHIES** function is one of the system functions. It employs the following syntax:

**INFO.ATTRIBUTEHIERARCHIES****()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **AttributeHierarchy** object represents the attribute hierarchy of a column in a table. It is an optional child object of a **Column** object and is implicitly created by the server. When the attribute hierarchy is present, the column becomes available as a **hierarchy** and can be queried by using the **MDX** language.

We can write this **INFO.ATTRIBUTEHIERARCHIES** function in DAX query viewto obtain the sameinformation on the **TMSCHEMA\_ATTRIBUTE\_HIERARCHIES**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_ATTRIBUTE\_HIERARCHIES** and return an entire table with six \[6\] columns:

![](<Base64-Image-Removed>)

*   **ID:** this represents a reference to the object
*   **ColumnID:** this is an ID\_based reference to a **Column** object
*   **State:** thisis a value that provides information about the state of the **AttributeHierarchy** object. The possible values are as follows:
    *   Ready (1): the Attribute Hierarchy is able to be queried and has up-to-date data
    *   NoData (3): not applicable to Attribute Hierarchies
    *   CalculationNeeded (4): the Attribute Hierarchy does not contain any data because it was not refreshed. There is no error associated with the Attribute Hierarchy
    *   SemanticError (5): not applicable to Attribute Hierarchies
    *   EvaluationError (6): not applicable to Attribute Hierarchies
    *   DependencyError (7): the column that is associated with this Attribute Hierarchy is in an error state (SemanticError, EvaluationError or DependencyError)
    *   Incomplete (8): not applicable to Attribute Hierarchies
    *   SyntaxError (9): not applicable to Attribute Hierarchies.

*   **AttributeHierarchyStorageID:** an ID-based reference to an **AttributeHierarchyStorage** object. The **AttributeHierarchyStorage** object is reserved for internal use only
*   **ModifiedTime:** this is the time that the object was last modified
*   **RefreshedTime:** this is the time that the object was last refreshed.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if you do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-attributehierarchies/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-attributehierarchies/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-attributehierarchies/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-attributehierarchies/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-attributehierarchies/#0 "close")

top