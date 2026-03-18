# The A to Z of DAX Functions – INFO.MODEL

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-model/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.MODEL

*   November 26, 2024

The A to Z of DAX Functions – INFO.MODEL
========================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.MODEL
================================================================

26 November 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.MODEL**._

**_The_** _**INFO.MODEL**_ **_function_**

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.MODEL** function is one of the system functions. It employs the following syntax:

**INFO.MODEL()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **Model** object represents the Tabular data model. It is a child of the **Database** object as defined in \[MS-SSAS\]. All other Tabular metadata objects are descendants of the **Model** object.

We can write this **INFO.MODEL** function on DAX query viewto get the sameinformation on the **TMSCHEMA\_MODEL**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_MODEL** and return an entire table with 20 columns:

![](<Base64-Image-Removed>)

*   *   **ID:** this is a reference to the object
    *   **Name:** this is the name of the object
    *   **Description:** this is the description of the object
    *   **StorageLocation:** this is the location on disk to place the model
    *   **DefaultMode:** this is the default method for making data available in the partition
    *   **DefaultDataView**: this determines which partitions are to be selected to run queries against the model. The possible values are as follows:
        *   Full (0) – partitions with **DataView** set to ‘Default’ or ‘Full’ are selected
        *   Sample (1) – partitions with **DataView** set to ‘Default’ or ‘Sample’ are selected
        *   Default (3) – not applicable to **Model**
    *   **Culture:** this is the culture name to use for formatting
    *   **Collation:** this is the collation sequence
    *   **ModifiedTime:** this is the time that the object was last modified
    *   **StructureModifiedTime**: this is the time that the structure of the object was last modified
    *   **Version:** this is the current version of the **Model** object. The version number is incremented when any transaction on the **Model** is committed. This version number is set to one \[1\] for any newly created Tabular databases and is always set to one \[1\] for all Tabular databases when the server is restarted
    *   **DataAccessOptions:** this is a **JSON** property bag that contains the following three Boolean properties:
        *   fastCombine – a Boolean that indicates the ability to override privacy levels to share data across data sources and queries
            *   if set to “true”, data from data sources is allowed to be sent in queries to other data sources, regardless of the other data sources’ privacy levels
            *   if set to “false”, possible data sharing is controlled by the data source’s privacy levels
        *   legacyRedirects – a Boolean that indicates whether unsafe redirects to a different site and from HTTPS to HTTP are enabled
            *   if set to “true”, unsafe redirects are enabled; otherwise, it is “false”
        *   returnErrorValuesAsNull – a Boolean that indicates whether individual cell errors are returned as null values or the query fails
            *   if set to “true”, individual cell errors are returned as null values
            *   if set to “false”, the query fails

The default value for these Boolean properties is “false”. Compatibility level 1400 or higher is required

*   *   **DefaultMeasureID:** this is an ID-based reference to the default measure of the **Model** object. Compatibility level 1400 or higher is required
    *   **DefaultPowerBIDataSourceVersion:** this is not mentioned in MS-SSAS-T document from Microsoft
    *   **ForceUniqueNames:** this is a Boolean that determines whether a measure can have the same name as any column in the model
        *   if set to “true”, a measure cannot have the same name as any column in the model
        *   if set to “false”, this restriction is not enforced

Compatibility level 1500 or higher is required

*   *   **DiscourageImplicitMeasures:** this is a Boolean that determines whether to discourage the implicit measures
        *   if set to “true”, implicit measures are discouraged
        *   if set to “false”, implicit measures are not discouraged

Compatibility level 1500 or higher is required

*   **DataSourceVariablesOverrideBehavior:** this is not mentioned in MS-SSAS-T document from Microsoft
*   **DataSourceDefaultMaxConnections:** this is the default value for the **MaxConnections** property of the **DataSource** object when the object does not specify that value explicitly. Compatibility level 1600 or higher is required
*   **SourceQueryCulture:** this is the name of the culture to be used when formatting during refresh through M. Compatibility level 1600 or higher is required
*   **MAttributes:** this is a set of optional properties that can be used to define the literal attributes on the section members of the M queries. Compatibility level 1600 or higher is required.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stand for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission
*   there is also a **MDSCHEMA** for **MEASURES** call **MDSCHEMA\_MEASURES** but its output is not the same as **TMSCHEMA\_MODEL** and **INFO.MODEL.**

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-model/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-model/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-model/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-model/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-model/#0 "close")

top