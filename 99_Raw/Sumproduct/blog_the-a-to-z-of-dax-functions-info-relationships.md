# The A to Z of DAX Functions – INFO.RELATIONSHIPS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-relationships/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.RELATIONSHIPS

*   March 11, 2025

The A to Z of DAX Functions – INFO.RELATIONSHIPS
================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.RELATIONSHIPS
========================================================================

11 March 2025

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions. This week, we look at **INFO.RELATIONSHIPS**._

**_The_** _**INFO.RELATIONSHIPS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/b34e43fc7c165f4956a8a96d478b5a20.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The _**INFO.RELATIONSHIPS**_ function is one of the system functions. It employs the following syntax:

**INFO.RELATIONSHIPS(\[RestrictionName1\], \[RestrictionValue1\], …)**

There are two \[2\] main arguments in this function (excluding numbering):

*   **RestrictionName:** this argument is optional and repeatable this represents the restriction name
*   **RestrictionValue:** this argument is optional and repeatable this represents the restriction value.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **Relationship** object represents a logical relationship between two **Table** objects. It is a child of a **Model** object.

We can write this _**INFO.RELATIONSHIPS**_ function in DAX query viewto get the sameinformation on the **TMSCHEMA\_RELATIONSHIPS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_RELATIONSHIPS** and return an entire table with 20 columns:

![](<Base64-Image-Removed>)

*   **ID:** this isa reference to the object
*   **ModelID:** this is an ID-based reference to a **Model** object
*   **Name:** this is the name of the object
*   **IsActive:** this is a Boolean that indicates whether the relationship is marked as Active or Inactive. An Active relationship is automatically used for filtering across tables. An Inactive relationship can be used explicitly by **DAX** calculations with the **USERELATIONSHIP** function
*   **Type:** this represents the type of **Relationship**. At present, the only possible value is as follows:
    *   SingleColumn (1) – normal column-column relationship
*   **CrossFilteringBehavior:** this indicates how relationships influence filtering of data. The enumeration defines the possible behaviours. The possible values are as follows:
    *   OneDirection (1) – the rows selected in the “To” end of the relationship automatically filter scans of the table in the “From” end of the relationship
    *   BothDirections (2) – filters on either end of the relationship; automatically filters the other table
    *   Automatic (3) – the engine analyses the relationships and chooses one of the behaviours by using heuristics
*   **JoinOnDateBehavior:** when joining two date time columns, indicates whether to join on date and time parts or on date part only
*   **RelyOnReferentialIntegrity:** this is unused; reserved for future use
*   **FromTableID:** this is an ID-based reference to a table at the “From” end of the relationship
*   **FromColumnID:** this is an ID-based reference to a column at the “From” end of the relationship
*   **FromCardinality:** this indicates whether the “From” end of the relationship has a cardinality of **One (1)** or **Many (2)**
*   **ToTableID:** this is an ID-based reference to a table at the “To” end of the relationship
*   **ToColumnID:** this is an ID-based reference to a column at the “To” end of the relationship
*   **ToCardinality:** this indicates whether the “To” end of the relationship has a cardinality of **One (1)** or **Many (2)**
*   **State:** this is a value that provides information about the state of the relationship. The possible values and their interpretation are as follows:
    *   Ready (1) – the relationship is queryable and has up-to-date data
    *   NoData (3) – not applicable to **Relationship**
    *   CalculationNeeded (4) – the relationship does not contain any data because it was not refreshed. There is no error associated with the relationship
    *   SemanticError (5) – not applicable to **Relationship**
    *   EvaluationError (6) – not applicable to **Relationship**
    *   DependencyError (7) – a dependency associated with this relationship is in an error state (SemanticError, EvaluationError, or DependencyError)
    *   Incomplete (8) – not applicable to **Relationship**
    *   SyntaxError (9) – not applicable to **Relationship**
*   **RelationshipStorageID:** this is an ID-based reference to a **RelationshipStorage** object. The **RelationshipStorage** object is reserved for internal use only
*   **RelationshipStorage2ID:** this is an ID-based reference to a second **RelationshipStorage** object
*   **ModifiedTime:** this represents the time that the object was last modified
*   **RefreshedTime:** this represents the time that the object was last refreshed
*   **SecurityFilteringBehavior:** this indicates how relationships influence filtering of data when evaluating row-level security expressions. The possible values are as follows:
    *   OneDirection (1) – the rows selected in the “To” end of the relationship automatically filter scans of the table in the “From” end of the relationship
    *   BothDirections (2) – filters on either end of the relationship automatically filter the other table
    *   None (3) – no filtering occurs from either end of the relationship. Compatibility level 1600 or higher is required.

It should be noted that:

*   *   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
    *   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-relationships/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-relationships/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-relationships/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-relationships/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-relationships/#0 "close")

top