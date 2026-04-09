# Power Query Functions

**Source:** https://trumpexcel.com/power-query/functions

---

[Skip to content](https://trumpexcel.com/power-query/functions/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/power-query/functions/#below-title)

If you’ve been using [Power Query](https://trumpexcel.com/power-query/)
 for a while, you’ve probably noticed something magical happening behind the scenes.

Every time you click a button in the Power Query interface – whether you’re removing duplicates, splitting columns, or changing data types – Power Query is automatically writing function code for you.

Those seemingly simple clicks are actually calling powerful, built-in functions that handle all the heavy lifting of data transformation. And here’s the exciting part:

Power Query comes packed with **over 800 built-in functions** that can handle virtually any data transformation challenge you can imagine.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/power-query/functions/#)

Discovering All Available Functions in Power Query (using #shared)
------------------------------------------------------------------

Here’s a neat trick that many Power Query users don’t know about: you can actually see every single function available in Power Query using a simple technique.

In the Power Query Editor, you can use the `#shared` keyword to access a record that contains all the built-in functions, constants, and identifiers available in the current Power Query environment.

**Here’s how to do it:**

1.  Open Power Query Editor
2.  Click _Get Data_ → _Other Sources_ → _Blank Query_ (this opens Power Query Editor)
3.  In the formula bar, simply type: **#shared**

![shared keyword in formula bar in power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201527%20888'%3E%3C/svg%3E)

4.  Press Enter

What you’ll see is a record containing every single function that Power Query has available. You’ll notice there are hundreds of them, organized by their function category prefixes (like Text., Date., Number., etc.).

![List of all functions in power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202380%202003'%3E%3C/svg%3E)

**Converting the Function List to a Table**

If you want to get this into a more usable format, you can convert it to a table:

1.  After entering _\=#shared_, you’ll see a Record with all the functions
2.  Click on the “Table” button in the ribbon to convert the record to a table

![Convert function list to table power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201272%20782'%3E%3C/svg%3E)

3.  Power Query will create a two-column table with function names and their details
4.  You can then filter this table to explore specific function categories
5.  Load this table into Excel if you want to keep it as a reference

This gives you a complete catalog of every function available, which is incredibly useful for discovery and reference.

Along with the functions, this will also give you a list of all the queries you already have in your Power Query Editor.

List of All Power Query Functions
---------------------------------

Below I have a list of all the power query functions in Excel at the time of writing this article. New functions are often released to Power Query on a periodic basis. So I’ll keep on adding them as and when they are released.

There could be some additional functions in Power Query for Power BI.

### Accessing Data Functions

These functions are primarily used for accessing and importing data from various sources into Power Query. Most of these functions return navigation tables that will help you explore and select the specific data you need.

| Function Name | Description |
| --- | --- |
| AccessControlEntry.ConditionToIdentities | Gets a list of user identities that meet specific access control conditions |
| Access.Database | Connects to and retrieves the structure of a Microsoft Access database |
| ActiveDirectory.Domains | Finds Active Directory domains within the same forest as a specified domain, or uses your current machine’s domain if none is specified |
| AdobeAnalytics.Cubes | Retrieves available report suites from your Adobe Analytics account |
| AdoDotNet.DataSource | Gets the schema information for any ADO.NET compatible data source |
| AdoDotNet.Query | Runs a custom SQL query against an ADO.NET data source and returns the results |
| AnalysisServices.Database | Connects to an Analysis Services database and retrieves available cubes or tabular models |
| AnalysisServices.Databases | Lists all Analysis Services databases available on a specific server |
| AzureStorage.BlobContents | Downloads and retrieves the actual content of a specific blob from Azure Storage |
| AzureStorage.Blobs | Creates a navigation table showing all containers in an Azure Storage account, with links to explore each container’s blobs |
| AzureStorage.DataLake | Provides a navigation table of documents and folders within an Azure Data Lake Storage container |
| AzureStorage.DataLakeContents | Downloads the content of a specific file from Azure Data Lake Storage |
| AzureStorage.Tables | Creates a navigation table listing all tables in an Azure Storage account with links to access each table |
| Cdm.Contents | Currently unavailable – requires .NET 4.5 framework |
| Csv.Document | Reads a CSV file and converts it into a table format using the encoding you specify |
| Cube.AddAndExpandDimensionColumn | Integrates a dimension table into a cube and expands the analysis to include additional dimension attributes |
| Cube.AddMeasureColumn | Adds a new column to your cube containing calculated measure values for each row |
| Cube.ApplyParameter | Updates a cube by applying specific parameter values to it |
| Cube.AttributeMemberId | Extracts the unique identifier for dimension attribute members |
| Cube.AttributeMemberProperty | Gets specific properties of dimension attributes in your cube |
| Cube.CollapseAndRemoveColumns | Simplifies your cube view by collapsing and removing specified dimension columns |
| Cube.Dimensions | Returns a table listing all available dimensions in your cube |
| Cube.DisplayFolders | Shows the organizational folder structure for cube objects like dimensions and measures |
| Cube.MeasureProperties | Lists all available properties for measures that are currently expanded in your cube |
| Cube.MeasureProperty | Retrieves a specific property value for a measure (also called a cell property) |
| Cube.Measures | Returns a table containing all available measures in your cube |
| Cube.Parameters | Shows all parameters that you can apply to modify your cube |
| Cube.Properties | Lists available properties for dimensions that are currently expanded in your cube |
| Cube.PropertyKey | Gets the key identifier for a specific property |
| Cube.ReplaceDimensions | Substitutes the current set of dimensions with a new set |
| Cube.Transform | Applies multiple cube transformation functions in sequence |
| DB2.Database | Connects to a DB2 database and retrieves available tables and views |
| DeltaLake.Metadata | Accesses the transaction log entries for a Delta Lake table to see its history |
| DeltaLake.Table | Reads and returns the data from a Delta Lake table |
| Essbase.Cubes | Retrieves cubes from an Essbase instance, organized by server |
| Excel.CurrentWorkbook | Accesses all sheets, named ranges, and tables within the current Excel workbook |
| Excel.Workbook | Reads the contents of any Excel workbook file |
| Exchange.Contents | Connects to a Microsoft Exchange account and retrieves email content as a table |
| File.Contents | Reads any file and returns its content as binary data |
| Folder.Contents | Scans a folder and returns a table with details about all files and subfolders found |
| Folder.Files | Recursively searches through a folder and all its subfolders to find files, returning their properties and content links |
| GoogleAnalytics.Accounts | Retrieves Google Analytics accounts associated with your current credentials |
| Hdfs.Contents | Explores a Hadoop file system folder and returns information about its files and subfolders |
| Hdfs.Files | Recursively searches through Hadoop file system folders to find all files with their properties |
| HdInsight.Containers | Creates a navigation table of containers in an Azure HDInsight storage account |
| HdInsight.Contents | Lists containers in an Azure HDInsight storage account with navigation to their contents |
| HdInsight.Files | Shows all files within a specific HDInsight container along with their properties |
| Html.Table | Extracts tables from HTML content using CSS selectors you specify |
| Identity.From | Creates a new identity object for access control purposes |
| Identity.IsMemberOf | Checks whether a specific identity belongs to a group of identities |
| IdentityProvider.Default | Gets the default identity provider for your current environment |
| Informix.Database | Connects to an Informix database and lists available tables and views |
| Json.Document | Parses JSON content (either as text or binary) and converts it into a structured format |
| Json.FromValue | Converts any Power Query value into JSON text format with specified encoding |
| MySQL.Database | Connects to a MySQL database and retrieves tables, views, and scalar functions |
| OData.Feed | Connects to an OData service and returns available data feeds as a table |
| Odbc.DataSource | Connects to any ODBC-compatible data source and lists its tables and views |
| Odbc.InferOptions | Tests an ODBC driver to determine what SQL capabilities it supports |
| Odbc.Query | Executes a custom SQL query against an ODBC data source |
| OleDb.DataSource | Connects to an OLE DB data source and retrieves its tables and views |
| OleDb.Query | Runs a native SQL query against an OLE DB data source |
| Oracle.Database | Connects to an Oracle database and lists available tables and views |
| Pdf.Tables | Scans a PDF file and extracts any tables it finds |
| PostgreSQL.Database | Connects to a PostgreSQL database and retrieves tables and views |
| RData.FromBinary | Reads an R data file and extracts data frames from it |
| Salesforce.Data | Connects to your Salesforce account and retrieves data objects |
| Salesforce.Reports | Accesses reports from your Salesforce account |
| SapBusinessWarehouse.Cubes | Connects to SAP Business Warehouse and retrieves InfoCubes and queries organized by InfoArea |
| SapHana.Database | Connects to an SAP HANA database and lists available packages |
| SharePoint.Contents | Explores a SharePoint site and returns a table of all content with file/folder properties |
| SharePoint.Files | Specifically retrieves documents from a SharePoint site with their properties |
| SharePoint.Tables | Accesses data from SharePoint Lists as tables |
| Soda.Feed | Reads data from a SODA 2.0 API compliant URL (must end with .csv extension) |
| Sql.Database | Connects to a SQL Server database and lists tables, views, and stored functions |
| Sql.Databases | Shows all databases available on a SQL Server instance |
| Sybase.Database | Connects to a Sybase database and retrieves available tables and views |
| Teradata.Database | Connects to a Teradata database and lists tables and views |
| WebAction.Request | Creates a web request action that will perform an HTTP method against a URL when executed |
| Web.BrowserContents | Downloads HTML content from a URL as it would appear in a web browser |
| Web.Contents | Downloads raw content from a URL as binary data |
| Web.Headers | Retrieves HTTP headers from a URL as a record |
| Web.Page | Parses an HTML page and breaks it down into its structural components, plus provides clean text |
| Xml.Document | Reads XML content and converts it into a hierarchical table structure |
| Xml.Tables | Converts XML content into a nested collection of flattened tables |

### Binary Functions

Binary functions are essential for working with files, network data, and any scenario where you need to read or manipulate raw data at the byte level.

#### Binary Formats

##### Reading numbers

These functions are essential for reading structured binary files, network protocols, or any custom binary format where you need to parse specific data types in a particular order.

| Function Name | Description |
| --- | --- |
| BinaryFormat.7BitEncodedSignedInteger | Reads a 64-bit signed number that’s stored using a space-saving 7-bit encoding technique (can handle positive and negative values) |
| BinaryFormat.7BitEncodedUnsignedInteger | Reads a 64-bit unsigned number that’s stored using a space-saving 7-bit encoding technique (positive values only) |
| BinaryFormat.Binary | Creates a format for reading raw binary data without any specific interpretation |
| BinaryFormat.Byte | Reads a single byte as an 8-bit unsigned number (values from 0 to 255) |
| BinaryFormat.Choice | Creates a smart format that decides which reading format to use next based on data you’ve already processed |
| BinaryFormat.Decimal | Reads a .NET decimal value (16 bytes) – perfect for precise financial calculations where accuracy matters |
| BinaryFormat.Double | Reads an 8-byte double-precision floating point number (high-precision decimal numbers) |
| BinaryFormat.Group | Reads a collection of items where each item has a unique identifier, returning only the item values as a list |
| BinaryFormat.Length | Sets a maximum limit on how many bytes can be read – useful for preventing over-reading of data |
| BinaryFormat.List | Reads a sequence of items one after another and collects them into a list |
| BinaryFormat.Null | Reads nothing (zero bytes) and returns null – useful as a placeholder in complex formats |
| BinaryFormat.Record | Creates a format for reading structured data where each field can be a different data type |
| BinaryFormat.SignedInteger16 | Reads a 2-byte signed integer (values from -32,768 to 32,767) |
| BinaryFormat.SignedInteger32 | Reads a 4-byte signed integer (values roughly from -2 billion to +2 billion) |
| BinaryFormat.SignedInteger64 | Reads an 8-byte signed integer (extremely large range of positive and negative values) |
| BinaryFormat.Single | Reads a 4-byte single-precision floating point number (standard precision decimal numbers) |
| BinaryFormat.Text | Reads text data from binary format, with optional encoding specification (like UTF-8, ASCII, etc.) |
| BinaryFormat.Transform | Applies a custom transformation to values after they’re read from the binary data |
| BinaryFormat.UnsignedInteger16 | Reads a 2-byte unsigned integer (values from 0 to 65,535) |
| BinaryFormat.UnsignedInteger32 | Reads a 4-byte unsigned integer (values from 0 to roughly 4 billion) |
| BinaryFormat.UnsignedInteger64 | Reads an 8-byte unsigned integer (extremely large positive values only) |

##### Controlling Byte Order

|     |     |
| --- | --- |
| BinaryFormat.ByteOrder | Controls the byte order (endianness) when reading multi-byte numbers from binary data – lets you specify whether bytes are read left-to-right (big-endian) or right-to-left (little-endian) |
| Table.PartitionValues | Analyzes how a table’s data is divided into partitions and returns details about the partitioning structure |

#### Binary Data

| Function Name | Description |
| --- | --- |
| Binary.ApproximateLength | Gets a rough estimate of how many bytes are in a binary value – useful for very large files where exact counting might be slow |
| Binary.Buffer | Loads binary data into memory to make it stable and faster to work with – ensures the data won’t change unexpectedly |
| Binary.Combine | Takes multiple separate binary values and joins them together into one combined binary file |
| Binary.Compress | Shrinks binary data using compression algorithms (like ZIP) to reduce file size and save storage space |
| Binary.Decompress | Expands previously compressed binary data back to its original, uncompressed form |
| Binary.From | Converts other types of data (like text or numbers) into binary format |
| Binary.FromList | Takes a list of numbers (typically 0-255) and converts them into binary data where each number becomes a byte |
| Binary.FromText | Converts text data (like Base64 encoded strings) back into its original binary form |
| Binary.InferContentType | Analyzes binary data and tries to automatically detect what type of file it is (like PNG, PDF, MP3, etc.) |
| Binary.Length | Counts and returns the exact number of bytes in a binary value |
| Binary.Range | Extracts a specific portion of binary data starting from a particular position – like cutting out a section |
| Binary.Split | Breaks up large binary data into smaller, more manageable chunks of a specified size |
| Binary.ToList | Converts binary data into a list of numbers where each byte becomes a number (0-255) |
| Binary.ToText | Converts binary data into text format using encoding methods like Base64 for safe text transmission |
| Binary.View | Creates a custom binary object with your own handlers that can intercept and modify how binary operations work |
| Binary.ViewError | Creates a special type of error for custom binary views that won’t trigger automatic fallback behaviors |
| Binary.ViewFunction | Creates a function that can be customized and intercepted by handlers in a binary view |
| #binary | Creates binary data directly from numbers or text – a quick shortcut for building binary values |

### Combiner Functions

These functions create other functions that merge text values in different ways. They’re commonly used with Table.ToList and Table.CombineColumns to process table rows.

| Function Name | Description |
| --- | --- |
| Combiner.CombineTextByDelimiter | Creates a function that joins text values together using a separator you specify (like commas, spaces, or pipes) |
| Combiner.CombineTextByEachDelimiter | Creates a function that joins text values using different separators for each position (first separator between items 1&2, second separator between items 2&3, etc.) |
| Combiner.CombineTextByLengths | Creates a function that combines text by cutting each text value to specific lengths you define, then joining them together |
| Combiner.CombineTextByPositions | Creates a function that places text values at exact positions you specify in the final combined text |
| Combiner.CombineTextByRanges | Creates a function that combines text by placing each value at specific positions with defined lengths – giving you precise control over where each piece goes |

### Comparer Functions

These functions test whether values are equal and determine their order for sorting operations.

| Function Name | Description |
| --- | --- |
| Comparer.Equals | Tests whether two values are exactly equal and returns true or false |
| Comparer.FromCulture | Creates a comparison function that follows specific cultural rules and case-sensitivity settings (useful for international text sorting) |
| Comparer.Ordinal | Creates a comparison function that compares values based on their character codes (ASCII/Unicode values) – strict computer-style comparison |
| Comparer.OrdinalIgnoreCase | Creates a comparison function that compares character codes but treats uppercase and lowercase letters as the same |

### Date Functions

These functions work with the date portion of date, datetime, and datetimezone values for calculations, formatting, and analysis.

| Function Name | Description |
| --- | --- |
| Date.AddDays | Adds or subtracts a specific number of days to a date (automatically handles month/year rollovers) |
| Date.AddMonths | Adds or subtracts a specific number of months to a date |
| Date.AddQuarters | Adds or subtracts quarters (3-month periods) to a date (automatically handles year rollovers) |
| Date.AddWeeks | Adds or subtracts weeks (7-day periods) to a date (automatically handles month/year rollovers) |
| Date.AddYears | Adds or subtracts a specific number of years to a date |
| Date.Day | Gets the day number (1-31) from a date |
| Date.DayOfWeek | Gets the day of the week as a number (0=Sunday, 1=Monday, etc.) |
| Date.DayOfWeekName | Gets the day of the week as text (like “Monday”, “Tuesday”) |
| Date.DayOfYear | Gets which day of the year it is (1-366) |
| Date.DaysInMonth | Gets how many days are in the month (28-31) |
| Date.EndOfDay | Gets the very end of the day (11:59:59 PM) |
| Date.EndOfMonth | Gets the last day of the month |
| Date.EndOfQuarter | Gets the last day of the quarter |
| Date.EndOfWeek | Gets the last day of the week |
| Date.EndOfYear | Gets December 31st of the year |
| Date.From | Converts various data types into a date value |
| Date.FromText | Converts text strings into dates using local, universal, or custom date formats |
| Date.IsInCurrentDay | Checks if a date is today |
| Date.IsInCurrentMonth | Checks if a date is in the current month |
| Date.IsInCurrentQuarter | Checks if a date is in the current quarter |
| Date.IsInCurrentWeek | Checks if a date is in the current week |
| Date.IsInCurrentYear | Checks if a date is in the current year |
| Date.IsInNextDay | Checks if a date is tomorrow |
| Date.IsInNextMonth | Checks if a date is in next month |
| Date.IsInNextNDays | Checks if a date falls within the next N days |
| Date.IsInNextNMonths | Checks if a date falls within the next N months |
| Date.IsInNextNQuarters | Checks if a date falls within the next N quarters |
| Date.IsInNextNWeeks | Checks if a date falls within the next N weeks |
| Date.IsInNextNYears | Checks if a date falls within the next N years |
| Date.IsInNextQuarter | Checks if a date is in the next quarter |
| Date.IsInNextWeek | Checks if a date is in next week |
| Date.IsInNextYear | Checks if a date is in next year |
| Date.IsInPreviousDay | Checks if a date was yesterday |
| Date.IsInPreviousMonth | Checks if a date was in last month |
| Date.IsInPreviousNDays | Checks if a date was within the previous N days |
| Date.IsInPreviousNMonths | Checks if a date was within the previous N months |
| Date.IsInPreviousNQuarters | Checks if a date was within the previous N quarters |
| Date.IsInPreviousNWeeks | Checks if a date was within the previous N weeks |
| Date.IsInPreviousNYears | Checks if a date was within the previous N years |
| Date.IsInPreviousQuarter | Checks if a date was in the previous quarter |
| Date.IsInPreviousWeek | Checks if a date was in last week |
| Date.IsInPreviousYear | Checks if a date was in last year |
| Date.IsInYearToDate | Checks if a date is between January 1st and today of the current year |
| Date.IsLeapYear | Checks if the year is a leap year (has 366 days instead of 365) |
| Date.Month | Gets the month number (1-12) from a date |
| Date.MonthName | Gets the month name as text (like “January”, “February”) |
| Date.QuarterOfYear | Gets which quarter (1-4) the date falls in |
| Date.StartOfDay | Gets the very beginning of the day (12:00:00 AM) |
| Date.StartOfMonth | Gets the first day of the month |
| Date.StartOfQuarter | Gets the first day of the quarter |
| Date.StartOfWeek | Gets the first day of the week (typically Sunday or Monday) |
| Date.StartOfYear | Gets January 1st of the year |
| Date.ToRecord | Breaks a date into a record with separate Year, Month, and Day fields |
| Date.ToText | Converts a date into text format |
| Date.WeekOfMonth | Gets which week of the month the date falls in |
| Date.WeekOfYear | Gets which week of the year (1-53) the date falls in |
| Date.Year | Gets the year number from a date |
| #date | Creates a date value directly from year, month, and day numbers |

### DateTime Functions

These functions work with datetime and datetimezone values, handling both date and time components together.

| Function Name | Description |
| --- | --- |
| DateTime.AddZone | Adds timezone information to a datetime value (converts datetime to datetimezone) |
| DateTime.Date | Extracts just the date part from a datetime, ignoring the time portion |
| DateTime.FixedLocalNow | Gets the current date and time once and keeps it fixed (won’t change during query execution) |
| DateTime.From | Converts various data types into a datetime value |
| DateTime.FromFileTime | Converts a 64-bit file timestamp number (used by Windows) into a readable datetime |
| DateTime.FromText | Converts text strings into datetime values using local, universal, or custom formats |
| DateTime.IsInCurrentHour | Checks if a datetime falls within the current hour (like 2:00-2:59 PM) |
| DateTime.IsInCurrentMinute | Checks if a datetime falls within the current minute (like 2:30:00-2:30:59) |
| DateTime.IsInCurrentSecond | Checks if a datetime falls within the current second |
| DateTime.IsInNextHour | Checks if a datetime falls within the next hour (excludes current hour) |
| DateTime.IsInNextMinute | Checks if a datetime falls within the next minute (excludes current minute) |
| DateTime.IsInNextNHours | Checks if a datetime falls within the next N hours (excludes current hour) |
| DateTime.IsInNextNMinutes | Checks if a datetime falls within the next N minutes (excludes current minute) |
| DateTime.IsInNextNSeconds | Checks if a datetime falls within the next N seconds (excludes current second) |
| DateTime.IsInNextSecond | Checks if a datetime falls within the next second (excludes current second) |
| DateTime.IsInPreviousHour | Checks if a datetime was in the previous hour (excludes current hour) |
| DateTime.IsInPreviousMinute | Checks if a datetime was in the previous minute (excludes current minute) |
| DateTime.IsInPreviousNHours | Checks if a datetime was within the previous N hours (excludes current hour) |
| DateTime.IsInPreviousNMinutes | Checks if a datetime was within the previous N minutes (excludes current minute) |
| DateTime.IsInPreviousNSeconds | Checks if a datetime was within the previous N seconds (excludes current second) |
| DateTime.IsInPreviousSecond | Checks if a datetime was in the previous second (excludes current second) |
| DateTime.LocalNow | Gets the current date and time right now (updates each time it’s called) |
| DateTime.Time | Extracts just the time part from a datetime, ignoring the date portion |
| DateTime.ToRecord | Breaks a datetime into separate fields (Year, Month, Day, Hour, Minute, Second) in a record |
| DateTime.ToText | Converts a datetime into text format for display or export |
| #datetime | Creates a datetime value directly from year, month, day, hour, minute, and second numbers |

### DateTimeZone Functions

These functions work with datetimezone values, which include date, time, and timezone information together.

| Function Name | Description |
| --- | --- |
| DateTimeZone.FixedLocalNow | Gets the current date, time, and timezone once and keeps it fixed throughout query execution |
| DateTimeZone.FixedUtcNow | Gets the current date and time in UTC/GMT timezone once and keeps it fixed throughout query execution |
| DateTimeZone.From | Converts various data types into a datetimezone value |
| DateTimeZone.FromFileTime | Converts a 64-bit file timestamp number (Windows format) into a datetimezone value |
| DateTimeZone.FromText | Converts text strings into datetimezone values using local, universal, or custom formats |
| DateTimeZone.LocalNow | Gets the current date and time in your local timezone (updates each time it’s called) |
| DateTimeZone.RemoveZone | Strips away the timezone information, leaving just a regular datetime value |
| DateTimeZone.SwitchZone | Changes a datetimezone to a different timezone while keeping the same moment in time |
| DateTimeZone.ToLocal | Converts a datetimezone to your local timezone |
| DateTimeZone.ToRecord | Breaks a datetimezone into separate fields (Year, Month, Day, Hour, Minute, Second, ZoneHours, ZoneMinutes) |
| DateTimeZone.ToText | Converts a datetimezone into text format for display or export |
| DateTimeZone.ToUtc | Converts a datetimezone to UTC/GMT timezone |
| DateTimeZone.UtcNow | Gets the current date and time in UTC/GMT timezone (updates each time it’s called) |
| DateTimeZone.ZoneHours | Gets the hour part of the timezone offset (like +5 or -8 for timezones) |
| DateTimeZone.ZoneMinutes | Gets the minute part of the timezone offset (like :30 or :45 for some timezones) |
| #datetimezone | Creates a datetimezone value directly from year, month, day, hour, minute, second, and timezone offset |

### Duration Functions

These functions work with duration values, which represent spans of time (like “3 days and 2 hours” or “45 minutes”).

| Function Name | Description |
| --- | --- |
| Duration.Days | Gets just the days portion of a duration (ignores hours, minutes, seconds) |
| Duration.From | Converts various data types into a duration value |
| Duration.FromText | Converts text strings (like “2.03:30:45”) into duration values |
| Duration.Hours | Gets just the hours portion of a duration (ignores days, minutes, seconds) |
| Duration.Minutes | Gets just the minutes portion of a duration (ignores days, hours, seconds) |
| Duration.Seconds | Gets just the seconds portion of a duration (ignores days, hours, minutes) |
| Duration.ToRecord | Breaks a duration into separate fields (Days, Hours, Minutes, Seconds) in a record |
| Duration.TotalDays | Converts the entire duration into total days (including fractional days) |
| Duration.TotalHours | Converts the entire duration into total hours (including fractional hours) |
| Duration.TotalMinutes | Converts the entire duration into total minutes |
| Duration.TotalSeconds | Converts the entire duration into total seconds |
| Duration.ToText | Converts a duration into text format like “d.h:m:s” (days.hours:minutes:seconds) |
| #duration | Creates a duration value directly from days, hours, minutes, and seconds numbers |

### Error Handling Functions

These functions help with debugging, tracing, and error handling in Power Query operations.

| Function Name | Description |
| --- | --- |
| Diagnostics.ActivityId | Gets a unique identifier for the current query execution – useful for tracking specific operations in logs |
| Diagnostics.CorrelationId | Gets an identifier that links related requests together – helps trace how data flows between different operations |
| Diagnostics.Trace | Writes a debug message to the trace log (if tracing is enabled) and returns the original value unchanged |
| Error.Record | Creates a custom error record with your own reason, message, details, and error code for better error handling |

### Expression Functions

These functions allow you to dynamically build and execute M code during runtime – essentially letting your queries write and run other queries.

| Function Name | Description |
| --- | --- |
| Expression.Constant | Converts a value into its M code representation (like turning the number 42 into the text “42”) |
| Expression.Evaluate | Takes M code as text and executes it, returning the result (like running “2 + 3” to get 5) |
| Expression.Identifier | Converts a name into its proper M code identifier format (handles special characters and keywords) |

### Function Values

These functions work with other M functions – creating, calling, and modifying how functions behave.

| Function Name | Description |
| --- | --- |
| Function.From | Takes a function that expects one parameter (a list) and wraps it to accept multiple separate parameters instead |
| Function.Invoke | Calls any function with the arguments you provide and returns the result |
| Function.InvokeAfter | Calls a function but waits for a specified duration before executing it (adds a delay) |
| Function.InvokeWithErrorContext | Internal Power Query function – not intended for general use |
| Function.IsDataSource | Checks whether a function is classified as a data source function (like connecting to databases) |
| Function.ScalarVector | Converts a function that works on multiple rows into one that works on a single row at a time |

### Lines Functions

These functions work with text files and data by splitting and joining lines, converting between text lists, single text values, and binary data.

| Function Name | Description |
| --- | --- |
| Lines.FromBinary | Converts binary data into a list where each line break creates a new list item |
| Lines.FromText | Splits text into a list where each line becomes a separate list item |
| Lines.ToBinary | Combines a list of text lines into binary data, adding line breaks between each item with specified encoding |
| Lines.ToText | Combines a list of text lines into a single text value, adding line breaks between each item |

### List Functions

These functions allow you to work with lists where you can create and manipulate lists.

#### Information & Analysis

Functions that tell you about the properties and characteristics of lists

| Function Name | Description |
| --- | --- |
| [List.Count](https://trumpexcel.com/power-query/functions/list-count/) | Gets the total number of items in a list (including null values) |
| List.IsEmpty | Checks whether a list has no items at all and returns true or false |
| List.NonNullCount | Gets the number of items in a list that actually have values (excludes null/empty items) |
| [List.IsDistinct](https://trumpexcel.com/power-query/functions/list-isdistinct/) | Checks whether all items in a list are unique (no duplicates) |
| List.MatchesAll | Checks if every item in the list meets a specific condition |
| List.MatchesAny | Checks if at least one item in the list meets a specific condition |

#### Selection & Filtering

Functions that get specific items or subsets from lists

| Function Name | Description |
| --- | --- |
| List.First | Gets the first item in a list, or a default value if the list is empty |
| List.Last | Gets the last item in a list, or a default value if the list is empty |
| List.FirstN | Gets the first N items from a list, or items that meet a condition |
| List.LastN | Gets the last N items from a list, or items that meet a condition |
| List.Single | Gets the one item from a list that has exactly one item (errors if more or less than one) |
| List.SingleOrDefault | Gets the one item from a list with exactly one item, or default value if empty |
| List.Select | Gets all items from a list that meet a specific condition |
| List.FindText | Gets all items (including record fields) that contain specific text |
| List.Range | Gets a portion of a list starting from a specific position |
| List.Skip | Gets a list with the first N items removed |
| List.Positions | Gets a list of index positions for all items in the original list |
| List.PositionOf | Gets the index position(s) where a specific value appears in the list |
| List.PositionOfAny | Gets the first index position where any of the specified values appears |

#### Transformation & Manipulation

Functions that change, modify, or restructure lists

| Function Name | Description |
| --- | --- |
| List.Transform | Creates a new list by applying a function to each item in the original list |
| List.TransformMany | Creates a flattened list by applying functions that can return multiple items per input |
| List.Accumulate | Builds up a single result by processing each list item in sequence (like a running calculation) |
| List.Combine | Joins multiple lists together into one combined list |
| List.Zip | Combines items at the same positions from multiple lists into pairs or groups |
| List.Split | Breaks a list into smaller lists of a specified size |
| List.Repeat | Creates a new list by repeating the original list a specified number of times |
| List.Reverse | Creates a new list with items in the opposite order |
| List.Buffer | Loads the list into memory for faster repeated access |
| List.Distinct | Creates a new list with duplicate values removed |
| List.Alternate | Creates a new list with only the odd-positioned items (1st, 3rd, 5th, etc.) |
| List.InsertRange | Adds new items to a list at a specific position |
| List.ReplaceRange | Replaces a section of items in a list with new items |
| List.ReplaceValue | Replaces all occurrences of a specific value with a new value |
| List.ReplaceMatchingItems | Replaces items that meet certain conditions with new values |
| List.RemoveFirstN | Creates a new list with the first N items removed |
| List.RemoveLastN | Creates a new list with the last N items removed |
| List.RemoveItems | Removes all items that appear in a second list |
| List.RemoveMatchingItems | Removes all items that match specified values |
| List.RemoveNulls | Creates a new list with all null values removed |
| List.RemoveRange | Removes a specific section of items from a list |

#### Generation

Functions that create new lists from scratch

| Function Name | Description |
| --- | --- |
| List.Generate | Creates a list using custom logic (start value, condition, next value function) |
| List.Random | Creates a list of random numbers |
| List.Numbers | Creates a list of sequential numbers (like 1, 2, 3, 4…) |
| List.Dates | Creates a list of sequential dates with specified intervals |
| List.DateTimes | Creates a list of sequential datetimes with specified intervals |
| List.DateTimeZones | Creates a list of sequential datetimezone values with specified intervals |
| List.Times | Creates a list of sequential time values with specified intervals |
| List.Durations | Creates a list of sequential duration values with specified intervals |

#### Membership & Set Operations

Functions that test membership and perform mathematical set operations

| Function Name | Description |
| --- | --- |
| [List.Contains](https://trumpexcel.com/power-query/functions/list-contains/) | Checks whether a list includes a specific value |
| List.ContainsAll | Checks whether a list includes every value from another list |
| List.ContainsAny | Checks whether a list includes at least one value from another list |
| List.AllTrue | Checks if all boolean values in a list are true |
| List.AnyTrue | Checks if at least one boolean value in a list is true |
| List.Union | Combines two lists and removes duplicates (mathematical union) |
| List.Intersect | Gets only values that appear in both lists (mathematical intersection) |
| List.Difference | Gets values that appear in the first list but not the second (mathematical difference) |

#### Statistics & Math

Functions that perform calculations and statistical analysis

| Function Name | Description |
| --- | --- |
| List.Sum | Adds up all numbers in a list |
| List.Product | Multiplies all numbers in a list together |
| List.Average | Calculates the average (mean) of numbers, dates, or durations |
| List.Median | Finds the middle value when the list is sorted |
| List.Mode | Finds the most frequently occurring value |
| List.Modes | Gets all values that occur most frequently (in case of ties) |
| List.Min | Finds the smallest value, or default if list is empty |
| List.Max | Finds the largest value, or default if list is empty |
| List.MinN | Gets the N smallest values |
| List.MaxN | Gets the N largest values |
| List.Percentile | Calculates specific percentiles (like 25th, 50th, 75th percentile) |
| List.StandardDeviation | Calculates how spread out the values are from the average |
| List.Covariance | Measures how two lists of numbers vary together |

#### Sorting & Ordering

Functions that arrange lists in specific orders

| Function Name | Description |
| --- | --- |
| List.Sort | Arranges list items in ascending or descending order, with custom sorting options |

### Logical Functions

These functions work with logical (true/false) values, converting between different data types and boolean values.

| Function Name | Description |
| --- | --- |
| Logical.From | Converts various data types into true or false values using standard conversion rules |
| Logical.FromText | Converts the text strings “true” and “false” into actual boolean values |
| Logical.ToText | Converts boolean values into the text strings “true” or “false” |

### Number Functions

These functions create and manipulate number values for calculations, conversions, and mathematical operations.

#### Information

Functions that test properties and characteristics of numbers

| Function Name | Description |
| --- | --- |
| Number.IsEven | Checks if a number is even (divisible by 2) and returns true or false |
| Number.IsNaN | Checks if a value is “Not a Number” (NaN) – usually from invalid calculations |
| Number.IsOdd | Checks if a number is odd (not divisible by 2) and returns true or false |

#### Conversion and Formatting

Functions that convert between different number types and formats

| Function Name | Description |
| --- | --- |
| Byte.From | Converts a value to an 8-bit integer (0-255 range) |
| Currency.From | Converts a value to currency format for financial calculations |
| Decimal.From | Converts a value to a high-precision decimal number (best for exact calculations) |
| Double.From | Converts a value to a double-precision floating point number (standard decimal) |
| Int8.From | Converts a value to a signed 8-bit integer (-128 to 127 range) |
| Int16.From | Converts a value to a 16-bit integer (-32,768 to 32,767 range) |
| Int32.From | Converts a value to a 32-bit integer (about -2 billion to +2 billion range) |
| Int64.From | Converts a value to a 64-bit integer (very large number range) |
| Number.From | Converts various data types into a general number value |
| Number.FromText | Converts text strings into numbers (like “123” becomes 123) |
| Number.ToText | Converts numbers into text format for display or export |
| Percentage.From | Converts a value to percentage format (like 0.5 becomes 50%) |
| Single.From | Converts a value to single-precision floating point number (less precise than double) |

#### Rounding

Functions that round numbers in different ways

| Function Name | Description |
| --- | --- |
| Number.Round | Rounds a number to the nearest integer or specified decimal places |
| Number.RoundAwayFromZero | Rounds positive numbers up and negative numbers down (away from zero) |
| Number.RoundDown | Always rounds down to the nearest integer (floor function) |
| Number.RoundTowardZero | Rounds positive numbers down and negative numbers up (toward zero) |
| Number.RoundUp | Always rounds up to the nearest integer (ceiling function) |

#### Operations

Functions that perform mathematical calculations and operations

| Function Name | Description |
| --- | --- |
| Number.Abs | Gets the absolute value (removes negative sign, distance from zero) |
| Number.Combinations | Calculates how many ways to choose items from a group (combinations formula) |
| Number.Exp | Calculates e raised to a power (exponential function) |
| Number.Factorial | Calculates factorial (like 5! = 5×4×3×2×1 = 120) |
| Number.IntegerDivide | Divides two numbers and returns only the whole number part (no remainder) |
| Number.Ln | Calculates the natural logarithm (base e) |
| Number.Log | Calculates the logarithm with a specified base |
| Number.Log10 | Calculates the base-10 logarithm (common logarithm) |
| Number.Mod | Divides two numbers and returns only the remainder |
| Number.Permutations | Calculates how many ways to arrange items in order (permutations formula) |
| Number.Power | Raises a number to a specified power (like 2^3 = 8) |
| Number.Sign | Returns 1 for positive numbers, -1 for negative numbers, or 0 for zero |
| Number.Sqrt | Calculates the square root of a number |

#### Random

Functions that generate random numbers

| Function Name | Description |
| --- | --- |
| Number.Random | Generates a random decimal number between 0 and 1 |
| Number.RandomBetween | Generates a random number between two specified values |

#### Trigonometry

Functions that perform trigonometric calculations

| Function Name | Description |
| --- | --- |
| Number.Acos | Calculates the arccosine (inverse cosine) in radians |
| Number.Asin | Calculates the arcsine (inverse sine) in radians |
| Number.Atan | Calculates the arctangent (inverse tangent) in radians |
| Number.Atan2 | Calculates the arctangent of y/x, handling quadrants correctly |
| Number.Cos | Calculates the cosine of an angle (in radians) |
| Number.Cosh | Calculates the hyperbolic cosine |
| Number.Sin | Calculates the sine of an angle (in radians) |
| Number.Sinh | Calculates the hyperbolic sine |
| Number.Tan | Calculates the tangent of an angle (in radians) |
| Number.Tanh | Calculates the hyperbolic tangent |

#### Bytes

Functions that perform bitwise operations on numbers

| Function Name | Description |
| --- | --- |
| Number.BitwiseAnd | Performs bitwise AND operation (compares bits: 1&1=1, others=0) |
| Number.BitwiseNot | Performs bitwise NOT operation (flips all bits: 0→1, 1→0) |
| Number.BitwiseOr | Performs bitwise OR operation (compares bits: 0\|0=0, others=1) |
| Number.BitwiseShiftLeft | Shifts binary digits left (multiplies by powers of 2) |
| Number.BitwiseShiftRight | Shifts binary digits right (divides by powers of 2) |
| Number.BitwiseXor | Performs bitwise XOR operation (compares bits: same=0, different=1) |

### Record Functions

These functions create and manipulate record values (structured data with field names and values).

#### Information

Functions that provide information about record properties

| Function Name | Description |
| --- | --- |
| Record.FieldCount | Gets the total number of fields (columns) in a record |
| Record.HasFields | Checks whether a record contains specific field names and returns true or false |

#### Transformations

Functions that modify, combine, or restructure records

| Function Name | Description |
| --- | --- |
| Geography.FromWellKnownText | Converts geographic text data in WKT format (like “POINT(-122.4 37.8)”) into a structured geographic record |
| Geography.ToWellKnownText | Converts a structured geographic record back into WKT text format |
| GeographyPoint.From | Creates a geographic point record from separate latitude, longitude, and other components |
| Geometry.FromWellKnownText | Converts geometric text data in WKT format into a structured geometric record |
| Geometry.ToWellKnownText | Converts a structured geometric record back into WKT text format |
| GeometryPoint.From | Creates a geometric point record from separate coordinate components |
| Record.AddField | Adds a new field with a specified name and value to an existing record |
| Record.Combine | Merges multiple records from a list into a single combined record |
| Record.RemoveFields | Creates a new record with specified fields removed |
| Record.RenameFields | Creates a new record with field names changed to new names (supports swapping field names) |
| Record.ReorderFields | Rearranges the order of fields in a record to match a specified list of field names |
| Record.TransformFields | Applies transformation functions to specific fields, creating a new record with modified values |

#### Selection

Functions that extract or access specific parts of records

| Function Name | Description |
| --- | --- |
| Record.Field | Gets the value of a specific field by name (dynamic version of record\[fieldname\] syntax) |
| Record.FieldNames | Gets a list of all field names in the record, in their current order |
| Record.FieldOrDefault | Gets the value of a specific field, or returns a default value if the field doesn’t exist |
| Record.FieldValues | Gets a list of all field values in the record, in the same order as the field names |
| Record.SelectFields | Creates a new record containing only the specified fields from the original record |

#### Serialization

Functions that convert records to/from other data structures

| Function Name | Description |
| --- | --- |
| Record.FromList | Creates a record from a list of values and a separate list of field names |
| Record.FromTable | Creates a record from a table that has field names in one column and values in another |
| Record.ToList | Converts a record into a list of its field values (loses field names) |
| Record.ToTable | Converts a record into a table with two columns: field names and field values |

### Replacer Functions

These functions create replacement logic that other functions use to find and replace values in lists and tables.

| Function Name | Description |
| --- | --- |
| Replacer.ReplaceText | Creates a text replacement function that can be used with List.ReplaceValue or Table.ReplaceValue to find and replace text strings |
| Replacer.ReplaceValue | Creates a general value replacement function that can be used with List.ReplaceValue or Table.ReplaceValue to find and replace any type of values |

### Splitter Functions

Splitter functions in Power Query are specialized tools that break apart text into smaller pieces based on different criteria like delimiters, positions, or character patterns. These functions are essential for cleaning and transforming data, especially when working with messy text that needs to be separated into individual columns or components.

| Function Name | What It Does |
| --- | --- |
| Splitter.SplitByNothing | Creates a function that doesn’t actually split anything – it just returns the original text as a single item in a list. Useful when you need a splitter function but don’t want any splitting to occur. |
| Splitter.SplitTextByCharacterTransition | Creates a function that splits text whenever the character type changes, such as going from letters to numbers, numbers to symbols, or uppercase to lowercase. Great for separating mixed content like “ABC123DEF”. |
| Splitter.SplitTextByAnyDelimiter | Creates a function that can split text using any of the common delimiter characters (like commas, semicolons, pipes, etc.). Power Query automatically detects which delimiter to use. |
| Splitter.SplitTextByDelimiter | Creates a function that splits text using a specific delimiter character or string that you define. This is your go-to function when you know exactly what separates your data (like commas in CSV files). |
| Splitter.SplitTextByEachDelimiter | Creates a function that applies multiple different delimiters one after another to split your text. Each delimiter gets applied to the results of the previous split. |
| Splitter.SplitTextByLengths | Creates a function that cuts text into pieces based on specific lengths you define. For example, you could split a 10-character string into pieces of 3, 4, and 3 characters. |
| Splitter.SplitTextByPositions | Creates a function that splits text at exact character positions you specify. If you want to split at positions 5 and 10, it will cut the text at those exact spots. |
| Splitter.SplitTextByRanges | Creates a function that extracts specific character ranges from your text. You define which characters you want (like characters 1-5, 8-12, etc.) and it pulls out just those sections. |
| Splitter.SplitTextByRepeatedLengths | Creates a function that repeatedly cuts text into chunks of the same length. Perfect for fixed-width data where every field is always the same number of characters. |
| Splitter.SplitTextByWhitespace | Creates a function that splits text wherever it finds spaces, tabs, line breaks, or other whitespace characters. Handy for separating words or cleaning up text with inconsistent spacing. |

### Table Functions

Table functions in Power Query are the core tools for creating, manipulating, and transforming table data structures. These functions allow you to build tables from scratch, modify existing tables, perform data operations like joins and aggregations, and convert tables to and from other data types.

#### Table Construction

Functions that create new tables from various data sources and structures.

| Function Name | What It Does |
| --- | --- |
| #table | Creates a table from scratch using column definitions and row data. Think of it as building a table manually by specifying exactly what columns you want and what data goes in each row. |
| ItemExpression.From | Returns the underlying code structure (AST) for a function’s body. This is mainly used for advanced meta-programming scenarios. |
| ItemExpression.Item | Represents an item reference in the code structure. Another advanced function for meta-programming. |
| RowExpression.Column | Creates code that represents accessing a specific column within a row. Used in advanced scenarios for building dynamic expressions. |
| RowExpression.From | Returns the code structure for a function’s body related to row operations. Advanced meta-programming function. |
| RowExpression.Row | Represents a row reference in the code structure. Used for advanced expression building. |
| Table.FromColumns | Builds a table by organizing your data as separate lists for each column, then combining them into a table structure. |
| Table.FromList | Takes a simple list and converts it into a table by applying a function that decides how to split each list item into columns. |
| Table.FromRecords | Converts a list of records (like mini-databases with field names and values) into a proper table where each record becomes a row. |
| Table.FromRows | Creates a table from a list of rows, where each row is represented as a list of values. You can optionally specify column names. |
| Table.FromValue | Takes a single value or list of values and creates a simple one-column table from it. |
| Table.WithErrorContext | Internal function used by Power Query’s engine for error handling. Not meant for direct use. |
| Table.View | Creates a virtual table with custom handlers that define how operations like filtering or sorting should work. Advanced function for building custom data sources. |
| Table.ViewError | Creates special error messages that work with virtual tables created by Table.View. Advanced error handling function. |
| Table.ViewFunction | Creates functions that can be customized by virtual table handlers. Works with Table.View for advanced scenarios. |

#### Conversions

Functions that transform tables into other data types and vice versa.

| Function Name | What It Does |
| --- | --- |
| Table.ToColumns | Converts a table into a list of lists, where each inner list contains all the values from one column. |
| Table.ToList | Transforms a table into a simple list by applying a function to combine each row’s values into a single item. |
| Table.ToRecords | Converts each row of a table into a record, resulting in a list of records where each record has field names matching the column names. |
| Table.ToRows | Converts a table into a list of lists, where each inner list represents one row’s values. |

#### Information

Functions that provide details and metadata about tables.

| Function Name | What It Does |
| --- | --- |
| Table.ApproximateRowCount | Gives you a rough estimate of how many rows are in the table, useful for very large datasets where exact counting would be slow. |
| Table.ColumnCount | Tells you exactly how many columns your table has. |
| Table.IsEmpty | Checks whether your table has any data rows or if it’s completely empty. |
| Table.PartitionValues | Provides information about how a table is divided into partitions, useful for understanding data distribution in large datasets. |
| Table.Profile | Analyzes your table and gives you a detailed summary of each column, including data types, null counts, and value distributions. |
| Table.RowCount | Tells you exactly how many rows of data your table contains. |
| Table.Schema | Returns a table that describes the structure of your original table – showing column names, data types, and other metadata. |
| Tables.GetRelationships | Analyzes multiple tables and identifies how they’re related to each other, useful for understanding data model connections. |

#### Row Operations

Functions that work with individual rows or sets of rows.

| Function Name | What It Does |
| --- | --- |
| Table.AlternateRows | Keeps some rows and skips others in a pattern. You can start at any position and then alternate between keeping and skipping rows. |
| Table.Combine | Takes multiple tables and stacks them on top of each other to create one larger table. |
| Table.FindText | Searches through your entire table and returns only the rows that contain specific text anywhere in their cells. |
| Table.First | Gets the very first row from your table, or returns a default value if the table is empty. |
| Table.FirstN | Returns the first several rows from your table – you specify how many you want. |
| Table.FirstValue | Gets the value from the first column of the first row, useful when you know your table should have just one result. |
| Table.FromPartitions | Combines multiple partitioned tables back into a single table. |
| Table.InsertRows | Adds new rows to your table at a specific position, pushing existing rows down. |
| Table.Last | Gets the very last row from your table, or returns a default value if the table is empty. |
| Table.LastN | Returns the last several rows from your table – you specify how many you want. |
| Table.MatchesAllRows | Checks if every single row in your table meets a specific condition you define. |
| Table.MatchesAnyRows | Checks if at least one row in your table meets a specific condition you define. |
| Table.Partition | Splits your table into multiple smaller tables based on grouping criteria. |
| Table.Range | Returns a specific range of rows starting from a position you specify. |
| Table.RemoveFirstN | Removes a specified number of rows from the beginning of your table. |
| Table.RemoveLastN | Removes a specified number of rows from the end of your table. |
| Table.RemoveRows | Removes a specific number of rows starting from a position you choose. |
| Table.RemoveRowsWithErrors | Cleans up your table by removing any rows that contain error values in their cells. |
| Table.Repeat | Creates multiple copies of all your table’s rows – useful for generating test data or expanding datasets. |
| Table.ReplaceRows | Replaces a specific range of rows with new rows you provide. |
| Table.ReverseRows | Flips your table upside down so the last row becomes first and vice versa. |
| Table.SelectRows | Keeps only the rows that meet a condition you specify, filtering out all others. |
| Table.SelectRowsWithErrors | Returns only the rows that contain error values, useful for identifying data quality issues. |
| Table.SingleRow | Ensures your table has exactly one row and returns it, or throws an error if there are zero or multiple rows. |
| Table.Skip | Skips over a specified number of rows from the beginning and returns the rest. |
| Table.SplitAt | Divides your table into two parts at a specific row number, returning both parts as separate tables. |

#### Column Operations

Functions that manipulate, organize, and work with table columns.

| Function Name | What It Does |
| --- | --- |
| Table.Column | Extracts all the values from a specific column and returns them as a simple list. |
| Table.ColumnNames | Returns a list of all your column names, useful for understanding table structure. |
| Table.ColumnsOfType | Finds all columns that match specific data types you’re looking for. |
| Table.DemoteHeaders | Takes your column headers and pushes them down to become the first row of data instead. |
| Table.DuplicateColumn | Creates an exact copy of a column with a new name, preserving all values and data types. |
| Table.HasColumns | Checks whether your table contains specific columns you’re looking for. |
| Table.Pivot | Transforms attribute-value pairs into separate columns – like turning a tall, narrow table into a wide one. |
| Table.PrefixColumns | Adds the same text prefix to all your column names, useful for avoiding name conflicts when combining tables. |
| Table.PromoteHeaders | Takes the first row of data and promotes it to become your column headers. |
| Table.RemoveColumns | Deletes specific columns from your table permanently. |
| Table.ReorderColumns | Rearranges your columns in the exact order you specify. |
| [Table.RenameColumns](https://trumpexcel.com/power-query/functions/table-renamecolumns/) | Changes the names of your columns to new names you provide. |
| Table.SelectColumns | Keeps only the specific columns you want and removes all others. |
| Table.TransformColumnNames | Applies a function to modify all column names at once, like making them all uppercase or adding prefixes. |
| Table.Unpivot | Transforms multiple columns into attribute-value pairs – like turning a wide table into a tall, narrow one. |
| Table.UnpivotOtherColumns | Unpivots all columns except the ones you specify to keep as identifiers. |

#### Transformation

Functions that modify table structure and data content.

| Function Name | What It Does |
| --- | --- |
| Table.AddColumn | Creates a new column where each row’s value is calculated using a function you provide. |
| Table.AddFuzzyClusterColumn | Adds a column that groups similar values together using fuzzy matching, great for cleaning messy data. |
| Table.AddIndexColumn | Adds a column with sequential numbers (like 1, 2, 3…) to give each row a unique identifier. |
| Table.AddJoinColumn | Performs a join operation and puts the results in a new column instead of expanding them horizontally. |
| Table.AddKey | Defines which columns serve as unique identifiers for your table rows. |
| Table.AggregateTableColumn | Takes a column that contains tables and summarizes them into regular columns with aggregated values. |
| Table.CombineColumns | Merges multiple columns into one new column using a function you specify for combining values. |
| Table.CombineColumnsToRecord | Combines multiple columns into a single column where each cell contains a record with the original column values. |
| Table.ConformToPageReader | Internal function for Power Query’s data processing engine. Not meant for direct use. |
| Table.ExpandListColumn | Takes a column containing lists and creates separate rows for each item in those lists. |
| Table.ExpandRecordColumn | Takes a column containing records and expands them into separate columns for each record field. |
| Table.ExpandTableColumn | Takes a column containing tables and expands them into multiple columns in the main table. |
| Table.FillDown | Copies values from above to fill in empty cells below in a column. |
| Table.FillUp | Copies values from below to fill in empty cells above in a column. |
| Table.FilterWithDataTable | Internal function for filtering operations. Not meant for direct use. |
| Table.FuzzyGroup | Groups rows together based on similar (but not necessarily identical) key values using fuzzy matching. |
| Table.FuzzyJoin | Joins two tables based on similar key values rather than requiring exact matches. |
| Table.FuzzyNestedJoin | Performs a fuzzy join and puts the results in a new column instead of expanding them. |
| [Table.Group](https://trumpexcel.com/power-query/functions/table-group/) | Groups rows that have identical key values and allows you to aggregate data within each group. |
| Table.Join | Combines two tables based on matching key values, creating a wider table with columns from both. |
| Table.Keys | Returns information about which columns are defined as keys for the table. |
| Table.NestedJoin | Performs a join operation and puts the results in a new column instead of expanding them horizontally. |
| Table.ReplaceErrorValues | Finds error values in specific columns and replaces them with values you specify. |
| Table.ReplaceKeys | Changes which columns are defined as keys for the table. |
| Table.ReplaceRelationshipIdentity | Internal function for managing table relationships. Not meant for direct use. |
| Table.ReplaceValue | Finds specific values in your table and replaces them with new values. |
| Table.Split | Divides a large table into multiple smaller tables of a specified size. |
| Table.SplitColumn | Takes one column and splits it into multiple columns using a splitter function. |
| [Table.TransformColumns](https://trumpexcel.com/power-query/functions/table-transformcolumns/) | Applies functions to modify the values in one or more columns. |
| Table.TransformColumnTypes | Changes the data types of columns, with options for handling different cultural formats. |
| Table.TransformRows | Applies a function to transform each entire row of the table. |
| Table.Transpose | Flips your table so rows become columns and columns become rows. |

#### Membership

Functions that check for the presence or absence of specific data in tables.

| Function Name | What It Does |
| --- | --- |
| Table.Contains | Checks if a specific row (represented as a record) exists anywhere in your table. |
| Table.ContainsAll | Checks if all the rows you specify can be found in your table. |
| Table.ContainsAny | Checks if at least one of the rows you specify can be found in your table. |
| Table.Distinct | Removes duplicate rows from your table, keeping only unique rows. |
| Table.IsDistinct | Checks whether your table contains only unique rows (no duplicates). |
| Table.PositionOf | Finds the position (row number) where a specific row appears in your table. |
| Table.PositionOfAny | Finds the positions where any of several specified rows appear in your table. |
| Table.RemoveMatchingRows | Removes all rows that match the rows you specify. |
| Table.ReplaceMatchingRows | Finds specific rows in your table and replaces them with new rows you provide. |

#### Ordering

Functions that sort and rank table data.

| Function Name | What It Does |
| --- | --- |
| Table.AddRankColumn | Adds a column that shows the ranking of each row based on the values in other columns. |
| Table.Max | Returns the row with the highest values based on criteria you specify. |
| Table.MaxN | Returns multiple rows with the highest values, letting you specify how many you want. |
| Table.Min | Returns the row with the smallest values based on criteria you specify. |
| Table.MinN | Returns multiple rows with the smallest values, letting you specify how many you want. |
| Table.Sort | Arranges your table rows in ascending or descending order based on one or more columns. |

#### Other Table Functions

Utility functions for special table operations.

| Function Name | What It Does |
| --- | --- |
| Table.Buffer | Stores your table in memory to improve performance and protect it from changes during processing. |
| Table.StopFolding | Forces Power Query to process operations locally instead of pushing them to the data source, useful for troubleshooting. |

### Text Functions

Text functions in Power Query are essential tools for working with text data – from simple operations like extracting parts of text and changing case, to complex transformations like splitting, combining, and cleaning text values.

These functions help you manipulate, analyze, and format text data to meet your specific needs.

#### Information

Functions that provide details and metadata about text values.

| Function Name | What It Does |
| --- | --- |
| Text.InferNumberType | Analyzes text that contains numbers and figures out what specific number type it represents (like integer, decimal, etc.). Helpful for understanding data before converting it. |
| Text.Length | Counts how many characters are in your text, including spaces and special characters. |

#### Text Comparisons

Functions that convert between text and other data types, or create text representations.

| Function Name | What It Does |
| --- | --- |
| Character.FromNumber | Takes a number and converts it to its corresponding character (like 65 becomes “A”). |
| Character.ToNumber | Takes a single character and converts it to its numeric code (like “A” becomes 65). |
| Guid.From | Creates a properly formatted GUID (globally unique identifier) from various input values. |
| Json.FromValue | Converts any value into its JSON text representation, useful for data export or API interactions. |
| Text.From | Converts any type of value (numbers, dates, etc.) into text format. |
| Text.FromBinary | Converts binary data into readable text using a specific encoding method (like UTF-8). |
| Text.NewGuid | Generates a brand new, unique GUID as a text value. |
| Text.ToBinary | Converts text into binary data using a specific encoding method. |
| Text.ToList | Breaks down text into a list where each character becomes a separate item. |
| Value.FromText | Converts text back into its original data type (like turning “123” back into the number 123). |

#### Extraction

Functions that pull out specific parts or sections of text.

| Function Name | What It Does |
| --- | --- |
| Text.At | Gets the character at a specific position in your text (starting from position 0). |
| Text.Middle | Extracts a portion of text starting from a specific position and extending for a certain number of characters. |
| Text.Range | Similar to Text.Middle – extracts a specific number of characters starting from a position you specify. |
| Text.Start | Gets a specific number of characters from the beginning of your text. |
| Text.End | Gets a specific number of characters from the end of your text. |

#### Modification

Functions that change, add, or remove parts of text.

| Function Name | What It Does |
| --- | --- |
| Text.Insert | Adds new text into an existing text value at a specific position. |
| Text.Remove | Removes all instances of specific characters from your text. |
| Text.RemoveRange | Deletes a specific number of characters starting from a position you choose. |
| Text.Replace | Finds all occurrences of specific text and replaces them with new text. |
| Text.ReplaceRange | Replaces a specific section of text (defined by position and length) with new text. |
| Text.Select | Keeps only the characters you specify and removes everything else from your text. |

#### Membership

Functions that check whether text contains specific content or patterns.

| Function Name | What It Does |
| --- | --- |
| [Text.Contains](https://trumpexcel.com/power-query/functions/text-contains/) | Checks if your text contains a specific substring anywhere within it. Returns true or false. |
| Text.EndsWith | Checks if your text ends with a specific substring. Useful for file extensions or suffixes. |
| Text.PositionOf | Finds the first position where a specific substring appears in your text (returns -1 if not found). |
| Text.PositionOfAny | Finds the first position where any of several characters appear in your text (returns -1 if none are found). |
| Text.StartsWith | Checks if your text begins with a specific substring. Great for prefixes or identifying patterns. |

#### Transformations

Functions that modify text format, structure, or appearance.

| Function Name | What It Does |
| --- | --- |
| Text.AfterDelimiter | Returns everything that comes after a specific delimiter character or text. |
| Text.BeforeDelimiter | Returns everything that comes before a specific delimiter character or text. |
| Text.BetweenDelimiters | Extracts text that appears between two specific delimiters (like getting text between parentheses). |
| Text.Clean | Removes unprintable characters (like control characters) that might cause display issues. |
| [Text.Combine](https://trumpexcel.com/power-query/functions/text-combine/) | Joins multiple text values together with a separator you specify (like combining words with commas). |
| Text.Lower | Converts all letters in your text to lowercase. |
| Text.PadEnd | Adds characters (usually spaces) to the end of your text to make it a specific length. |
| Text.PadStart | Adds characters (usually spaces) to the beginning of your text to make it a specific length. |
| Text.Proper | Capitalizes the first letter of each word (like title case formatting). |
| Text.Repeat | Creates new text by repeating your original text a specified number of times. |
| Text.Reverse | Flips your text backwards so the last character becomes first. |
| Text.Split | Breaks text into a list of pieces using a specific delimiter (like splitting a sentence by spaces). |
| Text.SplitAny | Breaks text into pieces using any of several possible delimiters you specify. |
| Text.Trim | Removes unwanted characters (usually spaces) from both the beginning and end of your text. |
| Text.TrimEnd | Removes unwanted characters from just the end of your text. |
| Text.TrimStart | Removes unwanted characters from just the beginning of your text. |
| Text.Upper | Converts all letters in your text to uppercase. |

### Time Functions

Time functions in Power Query are specialized tools for working with time values – allowing you to create, extract, manipulate, and format time data. These functions help you work with hours, minutes, and seconds, whether you’re parsing time from text, extracting specific time components, or converting between different time formats.

| Function Name | What It Does |
| --- | --- |
| Time.EndOfHour | Takes a time value and returns the end of that hour (like 2:59:59 PM if you input any time during the 2 PM hour). |
| Time.From | Converts various types of values into proper time format. Works with text, numbers, or other data types that represent time. |
| Time.FromText | Converts text that represents time into an actual time value. Handles different time formats including local time, UTC, and custom formats you specify. |
| Time.Hour | Extracts just the hour component from a datetime or time value (like getting “14” from “2:30:45 PM”). |
| Time.Minute | Extracts just the minute component from a datetime or time value (like getting “30” from “2:30:45 PM”). |
| Time.Second | Extracts just the second component from a datetime or time value (like getting “45” from “2:30:45 PM”). |
| Time.StartOfHour | Takes a time value and returns the start of that hour (like 2:00:00 PM if you input any time during the 2 PM hour). |
| Time.ToRecord | Converts a time value into a record structure that breaks down the time into separate fields for hour, minute, and second. |
| Time.ToText | Converts a time value into text format, allowing you to specify how you want the time displayed as text. |
| #time | Creates a time value from individual hour, minute, and second numbers (like making 2:30:45 PM from the numbers 14, 30, and 45). |

### Type Functions

Type functions in Power Query are advanced tools for working with data types themselves – allowing you to examine, create, modify, and manipulate type definitions.

These functions are primarily used in advanced scenarios like building custom connectors, creating dynamic schemas, or performing meta-programming tasks where you need to work with the structure and constraints of data types.

| Function Name | What It Does |
| --- | --- |
| Type.AddTableKey | Adds key information to a table type definition, specifying which columns serve as unique identifiers for the table. |
| Type.ClosedRecord | Takes a record type and makes it “closed,” meaning it won’t accept any additional fields beyond those already defined. If it’s already closed, returns the same type. |
| Type.Facets | Returns the additional constraints and metadata (called facets) that are attached to a type, like precision for numbers or length limits for text. |
| Type.ForFunction | Creates a function type definition that specifies what parameter types the function accepts and what type it returns. |
| Type.ForRecord | Creates a record type definition from a description of the fields it should contain. |
| Type.FunctionParameters | Examines a function type and returns information about its parameters – their names and what types they expect. |
| Type.FunctionRequiredParameters | Tells you the minimum number of parameters you must provide when calling a function of this type. |
| Type.FunctionReturn | Looks at a function type and tells you what type of value the function returns. |
| Type.Is | Checks whether values of one type can always be used where another type is expected – essentially testing type compatibility. |
| Type.IsNullable | Checks whether a type allows null values or requires actual data. Returns true if nulls are allowed, false if not. |
| Type.IsOpenRecord | Checks whether a record type is “open” (can accept additional fields) or “closed” (only accepts predefined fields). |
| Type.ListItem | Takes a list type and tells you what type of items the list contains (like getting “text” from a “list of text” type). |
| Type.NonNullable | Takes a type that allows nulls and converts it to a version that doesn’t allow nulls. |
| Type.OpenRecord | Takes a record type and makes it “open,” meaning it can accept additional fields beyond those already defined. If it’s already open, returns the same type. |
| Type.RecordFields | Examines a record type and returns detailed information about each field, including the field’s type and whether it’s optional. |
| Type.ReplaceFacets | Changes the constraints and metadata (facets) attached to a type, like modifying precision or length limits. |
| Type.ReplaceTableKeys | Changes which columns are defined as keys in a table type definition. |
| Type.TableColumn | Gets the type definition for a specific column in a table type. |
| Type.TableKeys | Returns information about which columns are defined as keys in a table type. |
| Type.TableRow | Gets the record type that represents a single row in a table type (showing what fields each row contains). |
| Type.TableSchema | Returns a table that describes the structure of a table type, showing all columns and their properties. |
| Type.Union | Combines multiple types into a single type that can accept values from any of the original types. |

### URI Functions

Uri functions in Power Query are specialized tools for working with web addresses and URLs.

These functions help you build, combine, parse, and properly format URIs and query strings – essential when working with web APIs, constructing dynamic URLs, or extracting information from web addresses.

| Function Name | What It Does |
| --- | --- |
| Uri.BuildQueryString | Takes a record with field names and values and converts it into a proper URL query string (like turning \[name=”John”, age=25\] into “name=John&age=25”). |
| Uri.Combine | Intelligently combines a base URL with a relative path to create a complete, properly formatted web address. |
| Uri.EscapeDataString | Encodes special characters in text so they can be safely used in URLs (like converting spaces to %20 and other characters that aren’t allowed in web addresses). |
| Uri.Parts | Takes a complete URL and breaks it down into its individual components like scheme, host, path, query parameters, etc., returning them as a record. |

### Value Functions

Value functions in Power Query are fundamental tools that work with any type of data value – allowing you to evaluate, compare, perform operations, and manipulate values regardless of their specific data type.

These functions provide core operations like arithmetic, type checking, metadata handling, and value comparison that form the foundation of many data transformations.

#### Core Value Functions

General functions for evaluating and working with values.

| Function Name | What It Does |
| --- | --- |
| Value.Alternates | Provides alternative ways to execute a query, allowing Power Query to choose the most efficient approach. Advanced optimization function. |
| Value.Compare | Compares two values and returns -1 if the first is smaller, 0 if they’re equal, or 1 if the first is larger. |
| Value.Equals | Checks if two values are exactly the same, returning true or false. |
| Value.Expression | Returns the underlying code structure (AST) that represents how a value was created. Advanced meta-programming function. |
| Value.VersionIdentity | Gets the version identifier for a value, useful for tracking data lineage and changes. |
| Value.Versions | Returns a navigation table showing all available versions of a value, helpful for version control scenarios. |
| Value.NativeQuery | Executes a query written in the target system’s native language (like SQL) against a data source. |
| Value.NullableEquals | Similar to Value.Equals, but handles null values more gracefully – can return true, false, or null. |
| Value.Optimize | Takes a query and returns an optimized version if possible, otherwise returns the original query unchanged. |
| Value.Type | Tells you what data type a value is (like text, number, date, etc.). |

#### Arithmetic Operations

Functions for performing mathematical calculations on values.

| Function Name | What It Does |
| --- | --- |
| Value.Add | Adds two values together. Works with numbers, dates, times, and other compatible types. |
| Value.Divide | Divides the first value by the second value. |
| Value.Multiply | Multiplies two values together. |
| Value.Subtract | Subtracts the second value from the first value. |

#### Parameter Types

Functions for working with data types and type compatibility.

| Function Name | What It Does |
| --- | --- |
| Value.As | Converts a value to a specified type if possible, or returns an error if the conversion can’t be done. |
| Value.Is | Checks whether a value is compatible with a specific data type, returning true or false. |
| Value.ReplaceType | Changes the type information attached to a value without changing the actual value. |

#### Internal Functions

These functions are used internally by Power Query and are not intended for direct use in your queries.

| Function Name | What It Does |
| --- | --- |
| Action.WithErrorContext | Internal function for error handling. Not for direct use. |
| DirectQueryCapabilities.From | Internal function for DirectQuery operations. Not for direct use. |
| Embedded.Value | Accesses values within embedded mashup scenarios. Internal use only. |
| Excel.ShapeTable | Internal function for Excel-specific table operations. Not for direct use. |
| Module.Versions | Returns version information for the current module and its dependencies. Internal use. |
| Progress.DataSourceProgress | Internal function for tracking data source progress. Not for direct use. |
| SqlExpression.SchemaFrom | Internal function for SQL expression schema handling. Not for direct use. |
| SqlExpression.ToExpression | Internal function for SQL expression conversion. Not for direct use. |
| Value.Firewall | Internal function for security and access control. Not for direct use. |
| Value.ViewError | Internal function for handling view-related errors. Not for direct use. |
| Value.ViewFunction | Internal function for view operations. Not for direct use. |
| Variable.Value | Internal function for variable handling. Not for direct use. |

#### Metadata

Functions for working with metadata attached to values.

| Function Name | What It Does |
| --- | --- |
| Value.Metadata | Retrieves the metadata record attached to a value, which contains additional information about the value. |
| Value.RemoveMetadata | Strips away all metadata from a value, returning just the clean value without any attached information. |
| Value.ReplaceMetadata | Replaces the existing metadata on a value with new metadata you provide. |

#### Lineage

Functions for tracking data lineage and dependencies (primarily for internal use).

| Function Name | What It Does |
| --- | --- |
| Graph.Nodes | Internal function for working with dependency graphs. Not for direct use. |
| Value.Lineage | Internal function for tracking data lineage. Not for direct use. |
| Value.Traits | Internal function for managing value traits and characteristics. Not for direct use. |

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK