# The A to Z of DAX Functions – INFO.TABLEPERMISSIONS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-tablepermissions/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.TABLEPERMISSIONS

*   June 3, 2025

The A to Z of DAX Functions – INFO.TABLEPERMISSIONS
===================================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions.  This week, we look at **INFO.TABLEPERMISSIONS**._

**_The_** _**INFO.TABLEPERMISSIONS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/image-4.png)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems.  **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model.  They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** we used external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The _**INFO.TABLEPERMISSIONS**_ function is one of the system functions.  It employs the following syntax:

> **INFO.TABLEPERMISSIONS (\[RestrictionName1\], \[RestrictionValue1\], …)**

There are two \[2\] main arguments in this function (excluding numbering):

*   **RestrictionName:** this argument is optional and repeatable this represents the restriction name
*   **RestrictionValue:** this argument is optional and repeatable this represents the restriction value.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas/854a72f2-d637-4be3-b60f-6a44422e80c9)
), this is object defines the security rules of the **Role** object on the **Table** object.  It is a child of a **Role** object.

We can write this _**INFO.TABLEPERMISSIONS**_ function in DAX query view to get the same information on the **TMSCHEMA\_TABLE\_PERMISSIONS**:

![](https://sumproduct.com/wp-content/uploads/2025/06/image-6.png)

Itwill query the **$SYSTEM.TMSCHEMA\_TABLE\_PERMISSIONS** and return an entire table with eight \[8\] columns:

![](https://sumproduct.com/wp-content/uploads/2025/06/image-7.png)

*   **ID:** this isa reference to the object
*   **RoleID:** this is an ID-based reference to a **Role** object
*   **TableID:** this is an ID-based reference to a **Table** object
*   **FilterExpression:** this represents the DAX expression that filters the rows in the table when this security role is in effect
*   **ModifiedTime:** this represents the time that the object was last modified
*   **State:** this represents a value that provides information about the state of the permission.  The possible values are as follows:
    
    *   Ready (1) – the permission has a valid expression
    
    *   NoData (3) – not applicable
    
    *   CalculationNeeded (4) – not applicable
    
    *   SemanticError (5) – the expression of the **TablePermission** object has a semantic error.  The table expression cannot be executed, and the role will not have access to the table
    
    *   EvaluationError (6) – not applicable
    
    *   DependencyError (7) – a dependency associated with this **TablePermission** object is in an error state (SemanticError, EvaluationError, or DependencyError).  The table expression cannot be executed, and the role will not have access to the table
    
    *   Incomplete (8) – not applicable
    
    *   SyntaxError (9) – the **TablePermission** object is in an error state because of a syntax error in its expression.  The **TablePermission** object is not queryable.  This state applies only to **TablePermission** objects of the type Calculated.  The table expression cannot be executed, and the role will not have access to the table
*   **ErrorMessage:** this is a string that explains the error state associated with the current object.  It is set by the engine only when the state of the object is one of these three values: SemanticError, DependencyError, or EvaluationError
*   **MetadataPermission:** this is a value that establishes the permission level that is granted to a user in a particular role in accessing a table’s metadata and the data it defines.  The possible values are as follows:
    
    *   Default (0) – The access that is granted is derived from the **Model** object’s permission of the role
    
    *   None (1) – No access is granted
    
    *   Read (2) – Read access is granted.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-tablepermissions/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-tablepermissions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-tablepermissions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-tablepermissions/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-tablepermissions/#0 "close")

top