# The A to Z of DAX Functions – INFO.OBJECTTRANSLATIONS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-objecttranslations/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.OBJECTTRANSLATIONS

*   December 3, 2024

The A to Z of DAX Functions – INFO.OBJECTTRANSLATIONS
=====================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.OBJECTTRANSLATIONS
=============================================================================

3 December 2024

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.OBJECTTRANSLATIONS**._

**_The_** _**INFO.OBJECTTRANSLATIONS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/426c82e49ae0115e8dff63db02d81983.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The **INFO.OBJECTTRANSLATIONS** function is one of the system functions. It employs the following syntax:

**INFO.OBJECTTRANSLATIONS()**

This function has no parameters.

Based upon the _‘\[MS-SSAS-T\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas-t/f85cd3b9-690c-4bc7-a1f0-a854d7daecd8)
), the **ObjectTranslation** object represents the translations of metadata properties for the **Culture** parent object. Properties such as the name and description of a metadata object can be translated. If they are not translated, the properties specified on the main object are used. The **ObjectTranslation** object has a weakly typed reference to the object that it is translating. For information on the distinction between strongly typed and weakly typed

We can write this **INFO.OBJECTTRANSLATIONS** function on DAX query viewto get the sameinformation on the **TMSCHEMA\_OBJECT\_TRANSLATIONS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****TMSCHEMA\_OBJECT\_TRANSLATIONS** and return an entire table with seven \[7\] columns:

![](<Base64-Image-Removed>)

*   **ID:** this is a reference to the object
*   **CultureID:** this is an ID-based reference to a **Culture** object
*   **ObjectID:** this is an ID-based reference to the object
*   **ObjectType:** this is the data type of the object specified by **ObjectID**. The possible values are as follows:
    *   TM\_TYPEID\_Model (1)
    *   TM\_TYPEID\_Table (3)
    *   TM\_TYPEID\_Column (4)
    *   TM\_TYPEID\_Measure (8)
    *   TM\_TYPEID\_Hierarchy (9)
    *   TM\_TYPEID\_Level (10)
    *   TM\_TYPEID\_KPI (12)
    *   TM\_TYPEID\_Perspective (29)
    *   TM\_TYPEID\_Role (34)
    *   TM\_TYPEID\_Variation (37) Requires compatibility level 1400 or higher
    *   TM\_TYPEID\_Expression (41) Requires compatibility level 1400 or higher
*   **Property:** this specifieswhich property of the object is being translated. The possible values are as follows:
    *   Invalid (-1) – the property is invalid. This is the default value
    *   Caption (1) – the caption for the object is shown instead of the name of the object, if a caption is available
    *   Description (2) – this value is the description of the object
    *   DisplayFolder (3) – this value is the DisplayFolder property
*   **Value:** this represents the value of the translation
*   **ModifiedTime:** this is thetime that the object was last modified.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-objecttranslations/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-objecttranslations/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-objecttranslations/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-objecttranslations/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-objecttranslations/#0 "close")

top