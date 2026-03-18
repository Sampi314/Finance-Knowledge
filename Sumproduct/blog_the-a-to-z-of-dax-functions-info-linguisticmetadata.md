# The A to Z of DAX Functions – INFO.LINGUISTICMETADATA

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-linguisticmetadata/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.LINGUISTICMETADATA

*   November 12, 2024

The A to Z of DAX Functions – INFO.LINGUISTICMETADATA
=====================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.LINGUISTICMETADATA
=============================================================================

12 November 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.LINGUISTICMETADATA**._

**_The_** _**INFO.LINGUISTICMETADATA**_ **_function_**

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.LINGUISTICMETADATA** function is one of the system functions. It employs the following syntax:

**INFO.LINGUISTICMETADATA()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **LinguisticMetadata** object is used to hold synonym information for the Tabular model. It is a child of a **Culture** object.

We can write this _**INFO.LINGUISTICMETADATA**_ function on DAX query viewto get the sameinformation on the **TMSCHEMA\_LINGUISTIC\_METADATA**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_LINGUISTIC\_METADATA** and return an entire table with five \[5\] columns:

![](<Base64-Image-Removed>)

*   **ID:** this is a reference to the object
*   **CultureID:** thisis anID-based reference to a **Culture** object
*   **Content:** this is a string that contains the natural language synonyms
*   **ModifiedTime:** this is the time that the object was last modified
*   **ContentType:** this specifies the type of the linguistic metadata based on the Content property. Compatibility level 1500 or higher is required. The possible values are as follows:

*   XML (0) – XML content
*   Json (1) – JSON content.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stand for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-linguisticmetadata/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-linguisticmetadata/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-linguisticmetadata/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-linguisticmetadata/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-linguisticmetadata/#0 "close")

top