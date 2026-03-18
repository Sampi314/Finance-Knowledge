# The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumns/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNS

*   May 6, 2025

The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNS
======================================================

Power Pivot Principles: The A to Z of DAX Functions – INFO.STORAGETABLECOLUMNS
==============================================================================

6 May 2025

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **INFO.STORAGETABLECOLUMNS**._

**_The_** _**INFO.STORAGETABLECOLUMNS**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/29877797028ec990f0bcc0b9c020604d.jpg)

**Dynamic Management Views** (**DMVs**) are specialised queries provided by **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** that offer an administrative view into the internal state of these systems. **DMVs** are used to retrieve metadata, monitor health and performance, and diagnose problems within the database or data model. They serve as a powerful tool for administrators and developers to gain insights into the workings of the database engine and the tabular data model, covering aspects like performance metrics, configuration settings and the structure of database objects.

The **$System** schema **DMVs** in **SQL Server Analysis Services** (**SSAS**), **Azure Analysis Services** (**AAS**), and **Power BI** are categorised into four \[4\] types, each serving specific purposes:

*   **DISCOVER**: requires admin privileges and provides information about the model, including details on connected sessions and environment configuration
*   **DMSCHEMA**: focused on data mining, offering insights for predictive analytics and pattern recognition, mainly used in **SSAS/AAS**
*   **MDSCHEMA**: targets multidimensional models, delivering metadata and structure from an **MDX** perspective, relevant for **OLAP** cubes and dimensions
*   **TMSCHEMA**: designed for tabular models, it provides detailed metadata about tables, columns, measures, _etc._, using **Tabular Model Scripting Language** (**TMSL**) information, crucial for **Power BI** and tabular **SSAS/AAS** models.

In the past, if we wanted to query those **$System** schema **DMVs** weused external tools like **Tabular Editors** or **DAX Studio** to query them:

![](<Base64-Image-Removed>)

The _**INFO.STORAGETABLECOLUMNS**_ function is one of the system functions. It employs the following syntax:

**INFO.STORAGETABLECOLUMNS(\[RestrictionName1\], \[RestrictionValue1\], …)**

There are two \[2\] main arguments in this function (excluding numbering):

*   **RestrictionName:** this argument is optional and repeatable this represents the restriction name
*   **RestrictionValue:** this argument is optional and repeatable this represents the restriction value.

Based upon the _‘\[MS-SSAS\]: SQL Server Analysis Services Tabular Protocol’_ from Microsoft (which you may access [**here**](https://learn.microsoft.com/en-us/openspecs/sql_server_protocols/ms-ssas/854a72f2-d637-4be3-b60f-6a44422e80c9)
), this schema rowset contains information about the columns used for representing the columns of an in-memory table.

We can write this _**INFO.STORAGETABLECOLUMNS**_ function on DAX query viewto get the sameinformation on the **DISCOVER\_STORAGE\_TABLE\_COLUMNS**:

![](<Base64-Image-Removed>)

Itwill query the **$SYSTEM.****DISCOVER\_STORAGE\_TABLE\_COLUMNS** and return an entire table with 19 columns:

![](<Base64-Image-Removed>)

*   **DATABASE\_NAME:** this is the name of the database
*   **CUBE\_NAME:** the name of the cube
*   **MEASURE\_GROUP\_NAME:** this is the name of the measure group
*   **DIMENSION\_NAME:** this is the name of the dimension
*   **ATTRIBUTE\_NAME:** this is the name of the attribute
*   **TABLE\_ID:** this the ID of the table
*   **COLUMN\_ID:** this the ID of the column
*   **COLUMN\_TYPE:** this is the type of the column. The values are as follows:
    *   BASIC\_DATA – this column contains data provided by an external data source
    *   CALCULATED\_DATA – this column contains data created by calculations
    *   RELATIONSHIP – this column contains information about relationship between tables
    *   HIERARCHY\_POSITION\_TO\_DATAID – this column contains information mapping position of a value in the hierarchy to the Data ID
    *   HIERARCHY\_DATAID\_TO\_POSITION – this column contains information mapping a Data ID to the position of a value in the hierarchy
    *   UNKNOWN – the column type is not known
*   **COLUMN\_ENCODING:** this is the encoding method used on the column. The method can be one of the following:
    *   0 – The system automatically selects a column encoding
    *   1 – The column uses hash encoding
    *   2 – The column uses value encoding.
*   **DATATYPE:** this is the type of the column data. The values are as follows:
    *   N/A – indicates that no data type information is available
    *   DBTYPE\_EMPTY – indicates that no value was specified
    *   DBTYPE\_I2 – indicates a two-byte signed integer
    *   DBTYPE\_I4 – indicates a four-byte signed integer
    *   DBTYPE\_R4 – indicates a single precision floating-point value
    *   DBTYPE\_R8 – indicates a double precision floating-point value
    *   DBTYPE\_CY – indicates a currency value. Currency is a fixed-point number that has four digits to the right of the decimal point and that is stored in an eight-byte signed integer scaled by 10,000
    *   DBTYPE\_DATE – indicates a date value. Date values are stored as Double, the whole part of which is the number of days since December 30, 1899, and the fractional part of which is the fraction of a day
    *   DBTYPE\_BSTR – indicates a null terminated character string (Unicode)
    *   DBTYPE\_ERROR – indicates a 32-bit error code
    *   DBTYPE\_BOOL – indicates a Boolean value
    *   DBTYPE\_DECIMAL – indicates an exact numeric value with a fixed precision and scale. The scale is between 0 and 28
    *   DBTYPE\_I1 – indicates a one-byte signed integer
    *   DBTYPE\_UI1 – indicates a one-byte unsigned integer
    *   DBTYPE\_UI2 – indicates a two-byte unsigned integer
    *   DBTYPE\_UI4 – indicates a four-byte unsigned integer
    *   DBTYPE\_I8 – indicates an eight-byte signed integer
    *   DBTYPE\_UI8 – indicates an eight byte unsigned integer
    *   DBTYPE\_GUID – indicates a GUID
    *   DBTYPE\_BYTES – indicates a binary value
    *   DBTYPE\_STR – indicates a string value
    *   DBTYPE\_WSTR – indicates a null terminated Unicode character string
    *   DBTYPE\_NUMERIC – indicates an exact numeric value with a fixed precision and scale. The scale is between 0 and 38
    *   DBTYPE\_DBDATE – indicates a date value (yyyymmdd)
    *   DBTYPE\_DBTIME – indicates a time value (hhmmss)
    *   DBTYPE\_DBTIMESTAMP – indicates a date-time stamp (yyyymmddhhmmss plus a fraction in billionths)
*   **ISKEY:** this indicates whether the column is a key column
*   **ISUNIQUE:** this indicates whether the column contains unique values
*   **ISNULLABLE:** this indicates whether the column can contain NULL values
*   **ISROWNUMBER:** this indicates whether the column is a Row Number column
*   **DICTIONARY\_SIZE:** this indicates the amount of memory that is used by the dictionary data structure associated with the column, in bytes. The dictionary data structure maps column data IDs to the actual values
*   **DICTIONARY\_ISPAGEABLE:** this indicates the Vertipaq Data Paging (VDP) state of the dictionary, which specifies whether the dictionary is pageable. If the VDP state of the dictionary is unknown, the default value is NULL. Otherwise, the value is a Boolean
*   **DICTIONARY\_ISRESIDENT:** this indicates the VDP state of the dictionary, which specifies whether the dictionary is resident. If the VDP state of the dictionary is unknown, the default value is NULL. Otherwise, the value is a Boolean
*   **DICTIONARY\_TEMPERATURE:** this indicates the scaled numeric value of the frequency of dictionary access. The value is based on the most recent access time and usage. This column has a numeric value only if the dictionary is pageable and has been loaded at least once; otherwise, the value is NULL
*   **DICTIONARY\_LAST\_ACCESSED:** this indicates the most recent time the dictionary was accessed
    *   For non-pageable tables in the dictionary, the DICTIONARY\_LAST\_ACCESSED value is NULL
    *   For pageable tables in the dictionary, DICTIONARY\_LAST\_ACCESSED value NULL denotes the table has not been loaded since server startup.

It should be noted that:

*   it is used for querying the **DMV** (Dynamic Management Views) from the **$System schema** called **TMSCHEMA** where **TM** stands for ‘Tabular model’ and **TMSCHEMA** provides information from the tabular model
*   sometimes querying **DMVs** may fail if we do not have the appropriate permission.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumns/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumns/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-info-storagetablecolumns/#0 "close")

top