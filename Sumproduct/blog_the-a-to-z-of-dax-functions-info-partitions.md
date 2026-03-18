# The A to Z of DAX Functions – INFO.PARTITIONS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-partitions/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.PARTITIONS

*   December 17, 2024

The A to Z of DAX Functions – INFO.PARTITIONS
=============================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.PARTITIONS
=====================================================================

17 December 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.PARTITIONS**._

**_The_** _**INFO.PARTITIONS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/05/9d2134a8b0ed556a04f4820b63459b4f.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.PARTITIONS** function is one of the system functions. It employs the following syntax:

**INFO.PARTITIONS()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the Partition object represents a partition in a table. It is a child of a Table object. The partitions in a table define the data from external data sources that become available when the table is queried.

We can write this **INFO.PARTITIONS** function on DAX query viewto get the sameinformation on the **TMSCHEMA\_PARTITIONS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_PARTITIONS** and return an entire table with 23 columns:

![](<Base64-Image-Removed>)

*   **ID:** this is a reference to the object
*   **TableID:** this is an ID-based reference to a **Table** object
*   **Name:** this is the name of the object
*   **Description:** this is the description of the object
*   **DataSourceID:** this is an ID-based reference to a **DataSource** object
*   **QueryDefinition:** this is the text of the query to be executed when populating data into the partition
*   **State:** this is a value that provides information about the state of the partition. The possible values and their interpretation are as follows:
    *   Ready (1) – the partition is queryable and has up-to date data
    *   NoData (3) – the partition is queryable but has no data. This state applies only to partitions with a type other than Calculated
    *   CalculationNeeded (4) – the partition is not queryable and needs to be refreshed (that is, recalculated) to become functional. This state applies only to partitions of the type Calculated
    *   SemanticError (5) – the partition is in an error state because of an invalid expression and is not queryable. this state applies only to partitions of the type Calculated
    *   EvaluationError (6) – the partition is in an error state because of an error during expression evaluation. The partition is not queryable. This state applies only to partitions of the type Calculated
    *   DependencyError (7) – the partition is in an error state because some of its calculation dependencies are in an error state. The partition is not queryable. This state applies only to partitions of the type Calculated
    *   Incomplete (8) – some parts of the partition have no data, and the partition needs to be refreshed to bring the data in. The partition is queryable. This state applies only to partitions of a type other than Calculated
    *   SyntaxError (9) – the partition is in an error state because of a syntax error in its expression. The partition is not queryable. This state applies only to partitions of the type Calculated
*   **Type:** this is the type of partition. The possible values are as follows:
    *   Query (1) – the data in this partition is retrieved by executing a query against a DataSource
    *   Calculated (2) – the data in this partition is populated by executing a calculated expression
    *   None (3) – the data in this partition is populated by pushing a rowset of data to the server as part of the Refresh operation
    *   M (4) – the data in this partition is retrieved by using an M (Power Query Formula Language) expression. Compatibility level 1400 or higher is required
    *   Entity (5) – the data in this partition is retrieved by executing a query against the named entity of the underlying data source. Compatibility level 1400 or higher is required
    *   CalculationGroup (7) – the partition uses CalculationGroup as a source. Compatibility level 1500 or higher is required
*   **PartitionStorageID:** this is an ID-based reference to a PartitionStorage object. The PartitionStorage object is reserved for internal use only
*   **Mode:** this defines the method for making data available in the partition. The possible values are as follows:
    *   Import (0) – data is imported from a data source
    *   DirectQuery (1) – data is queried dynamically from a data source
    *   Default (2) – only partitions can use this value. When set, the partition inherits the **DefaultMode** of the **Model**
    *   Push (3) – data is pushed into the partition
*   **DataView:** this is the value that determines which partitions are selected for use in queries that are run against the **Model** object. The possible values are as follows:
    *   Full (0) – partitions with **DataView** set to “Default” or “Full” are selected
    *   Sample (1) – partitions with **DataView** set to “Default” or “Sample” are selected
    *   Default (3) – the default **DataView** of the **Model** object is inherited
*   **ModifiedTime:** this is the that the object was last modified
*   **RefreshedTime:** this is the time that the object was last refreshed
*   **SystemFlags:** this is a bitmask used to identify the type of object. The possible values are as follows:
    *   Bit 0 is set to 1: the object is a partition that belongs to a system table that is not accessible to users through **data definition language (DDL)**
    *   Bit 1 is set to 1: the object is a partition that belongs to a calculated table
*   **ErrorMessage:** this is the string that explains the error state associated with the current object. It is set by the engine only when the state of the object is one of these three values: SemanticError, DependencyError, or EvaluationError. This element applies only to partitions of the type **Calculated**
*   **RetainDataTillForceCalculate:** this is a Boolean that indicates whether a calculated partition is allowed to contain data that is not affected by a RefreshCalculate command when only data changes have been made. Compatibility level 1400 or higher is required
*   **RangeStart:** this is not mentioned in the current MS-SSAS-T (14 May 2024) document
*   **RangeEnd:** this is not mentioned in the current MS-SSAS-T (14 May 2024) document
*   **RangeGranularity:** this is not mentioned in the current MS-SSAS-T (14 May 2024) document
*   **RefreshBookmark:** this is not mentioned in the current MS-SSAS-T (14 May 2024) document
*   **QueryGroupID:** this is an ID-based reference to a QueryGroup object. Compatibility level 1500 or higher is required
*   **ExpressionSourceID:** this is an ID-based reference to an Expression object. Compatibility level 1600 or higher is required
*   **MAttributes:** this is a set of optional properties that can be used to define the literal attributes on the section members of the M queries. This set of properties is meaningful only if the type of the partition is M. Compatibility level 1600 or higher is required.

It should be noted that:

it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model

sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-partitions/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-partitions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-partitions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-partitions/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-partitions/#0 "close")

top