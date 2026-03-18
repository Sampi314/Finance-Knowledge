# 350 Excel Functions | Exceljet

**Source:** https://exceljet.net/functions

---

[Skip to main content](https://exceljet.net/functions#main-content)

[](https://exceljet.net/functions#)

350 Excel Functions
===================

Over 350 built-in functions, with examples and videos.  VLOOKUP, XLOOKUP, INDEX & MATCH, FILTER, RANK, SUMPRODUCT, AVERAGE, COUNTIFS, SUMIFS, UNIQUE, SORT, TEXTSPLIT, SEQUENCE, FIND, DATE, and more. See also [500 Formulas](https://exceljet.net/formulas)
, [101 Functions](https://exceljet.net/articles/101-excel-functions)
, and [New Excel Functions](https://exceljet.net/new-excel-functions)
.

### Jump to Category

*   [Logical](https://exceljet.net/functions#Logical)
    
*   [Date and time](https://exceljet.net/functions#Date-and-time)
    
*   [Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)
    
*   [Text](https://exceljet.net/functions#Text)
    
*   [Dynamic array](https://exceljet.net/functions#Dynamic-array)
    
*   [Engineering](https://exceljet.net/functions#Engineering)
    
*   [Financial](https://exceljet.net/functions#Financial)
    
*   [Information](https://exceljet.net/functions#Information)
    
*   [Math](https://exceljet.net/functions#Math)
    
*   [Trigonometry](https://exceljet.net/functions#Trigonometry)
    
*   [Statistical](https://exceljet.net/functions#Statistical)
    
*   [Web](https://exceljet.net/functions#Web)
    
*   [Database](https://exceljet.net/functions#Database)
    

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Logical)
Logical
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [AND](https://exceljet.net/functions/and-function) | Excel 2003 | Test multiple conditions at the same time | logical1 logical2 ... |
| [FALSE](https://exceljet.net/functions/false-function) | Excel 2003 | Generate the logical value FALSE |     |
| [IF](https://exceljet.net/functions/if-function) | Excel 2003 | Test for a specific condition | logical\_test value\_if\_true value\_if\_false |
| [IFERROR](https://exceljet.net/functions/iferror-function) | Excel 2007 | Trap and handle errors | value value\_if\_error |
| [IFNA](https://exceljet.net/functions/ifna-function) | Excel 2013 | Trap and handle #N/A errors | value value\_if\_na |
| [IFS](https://exceljet.net/functions/ifs-function) | Excel 2019 | Test multiple conditions, return first true | test1 value1 test2, value2 ... |
| [NOT](https://exceljet.net/functions/not-function) | Excel 2003 | Reverse arguments or results | logical |
| [OR](https://exceljet.net/functions/or-function) | Excel 2003 | Test multiple conditions at the same time | logical1 logical2 ... |
| [SWITCH](https://exceljet.net/functions/switch-function) | Excel 2019 | Match multiple values, return first match | expression val1/result1 val2/result2 ... default |
| [TRUE](https://exceljet.net/functions/true-function) | Excel 2003 | Generate the logical value TRUE |     |
| [XOR](https://exceljet.net/functions/xor-function) | Excel 2013 | Perform exclusive OR | logical1 logical2 ... |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Date-and-time)
Date and time
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [DATE](https://exceljet.net/functions/date-function) | Excel 2003 | Create a date with year, month, and day | year month day |
| [DATEDIF](https://exceljet.net/functions/datedif-function) | Excel 2003 | Get days, months, or years between two dates | start\_date end\_date unit |
| [DATEVALUE](https://exceljet.net/functions/datevalue-function) | Excel 2003 | Convert a date in text format to a valid date | date\_text |
| [DAY](https://exceljet.net/functions/day-function) | Excel 2003 | Get the day of month from a date | date |
| [DAYS](https://exceljet.net/functions/days-function) | Excel 2013 | Count days between dates | end\_date start\_date |
| [DAYS360](https://exceljet.net/functions/days360-function) | Excel 2003 | Get days between 2 dates in a 360-day year | start\_date end\_date method |
| [EDATE](https://exceljet.net/functions/edate-function) | Excel 2003 | Get date n months in future or past | start\_date months |
| [EOMONTH](https://exceljet.net/functions/eomonth-function) | Excel 2003 | Get last day of month n months in future or past | start\_date months |
| [HOUR](https://exceljet.net/functions/hour-function) | Excel 2003 | Get the hour as a number (0-23) from a Time | serial\_number |
| [ISOWEEKNUM](https://exceljet.net/functions/isoweeknum-function) | Excel 2013 | Get ISO week number for a given date | date |
| [MINUTE](https://exceljet.net/functions/minute-function) | Excel 2003 | Get minute as a number (0-59) from time | serial\_number |
| [MONTH](https://exceljet.net/functions/month-function) | Excel 2003 | Get month as a number (1-12) from a date | date |
| [NETWORKDAYS](https://exceljet.net/functions/networkdays-function) | Excel 2003 | Get the number of working days between two dates | start\_date end\_date holidays |
| [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function) | Excel 2010 | Get work days between two dates | start\_date end\_date weekend holidays |
| [NOW](https://exceljet.net/functions/now-function) | Excel 2003 | Get the current date and time |     |
| [SECOND](https://exceljet.net/functions/second-function) | Excel 2003 | Get the Second as a number (0-59) from a Time | serial\_number |
| [TIME](https://exceljet.net/functions/time-function) | Excel 2003 | Create a valid time with hours, minutes, and seconds | hour minute second |
| [TIMEVALUE](https://exceljet.net/functions/timevalue-function) | Excel 2003 | Get a valid time from a text string | time\_text |
| [TODAY](https://exceljet.net/functions/today-function) | Excel 2003 | Get the current date |     |
| [WEEKDAY](https://exceljet.net/functions/weekday-function) | Excel 2003 | Get the day of the week as a number | serial\_number return\_type |
| [WEEKNUM](https://exceljet.net/functions/weeknum-function) | Excel 2003 | Get the week number for a given date | serial\_num return\_type |
| [WORKDAY](https://exceljet.net/functions/workday-function) | Excel 2003 | Get a date n working days in the future or past | start\_date days holidays |
| [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function) | Excel 2010 | Get a date n working days in the future or past | start\_date days weekend holidays |
| [YEAR](https://exceljet.net/functions/year-function) | Excel 2003 | Get the year from a date | date |
| [YEARFRAC](https://exceljet.net/functions/yearfrac-function) | Excel 2003 | Get the fraction of a year between two dates | start\_date end\_date basis |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Lookup-and-reference)
Lookup and reference
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [ADDRESS](https://exceljet.net/functions/address-function) | Excel 2003 | Create a cell address from a row and column number | row\_num col\_num abs\_num a1 sheet |
| [AREAS](https://exceljet.net/functions/areas-function) | Excel 2003 | Get the number of areas in a reference. | reference |
| [CHOOSE](https://exceljet.net/functions/choose-function) | Excel 2003 | Get a value from a list based on position | index\_num value1 value2 ... |
| [COLUMN](https://exceljet.net/functions/column-function) | Excel 2003 | Get the column number of a reference. | reference |
| [COLUMNS](https://exceljet.net/functions/columns-function) | Excel 2003 | Get the number of columns in an array or reference. | array |
| [FIELDVALUE](https://exceljet.net/functions/fieldvalue-function) | Excel 365 | Extract field value from a data type | value field\_name |
| [FORMULATEXT](https://exceljet.net/functions/formulatext-function) | Excel 2013 | Get the formula in a cell | reference |
| [GETPIVOTDATA](https://exceljet.net/functions/getpivotdata-function) | Excel 2003 | Retrieve data from a pivot table in a formula | data\_field pivot\_table field1, item1 ... |
| [HLOOKUP](https://exceljet.net/functions/hlookup-function) | Excel 2003 | Look up a value in a table arranged horizontally | lookup\_value table\_array row\_index range\_lookup |
| [HYPERLINK](https://exceljet.net/functions/hyperlink-function) | Excel 2003 | Create a clickable link. | link\_location friendly\_name |
| [INDEX](https://exceljet.net/functions/index-function) | Excel 2003 | Get a value in a list or table based on location | array row\_num col\_num area\_num |
| [INDIRECT](https://exceljet.net/functions/indirect-function) | Excel 2003 | Create a reference from text | ref\_text a1 |
| [LOOKUP](https://exceljet.net/functions/lookup-function) | Excel 2003 | Look up a value in a one-column range | lookup\_value lookup\_vector result\_vector |
| [MATCH](https://exceljet.net/functions/match-function) | Excel 2003 | Get the position of an item in an array | lookup\_value lookup\_array match\_type |
| [OFFSET](https://exceljet.net/functions/offset-function) | Excel 2003 | Create a reference offset from given starting point | reference rows cols height width |
| [ROW](https://exceljet.net/functions/row-function) | Excel 2003 | Get the row number of a reference | reference |
| [ROWS](https://exceljet.net/functions/rows-function) | Excel 2003 | Get the number of rows in an array or reference. | array |
| [TRANSPOSE](https://exceljet.net/functions/transpose-function) | Excel 2003 | Flip the orientation of a range of cells | array |
| [VLOOKUP](https://exceljet.net/functions/vlookup-function) | Excel 2003 | Look up and retrieve a value in a table | lookup\_value table\_array column\_index\_num range\_lookup |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Text)
Text
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [CHAR](https://exceljet.net/functions/char-function) | Excel 2003 | Get a character from a number | number |
| [CLEAN](https://exceljet.net/functions/clean-function) | Excel 2003 | Strip non-printable characters from text | text |
| [CODE](https://exceljet.net/functions/code-function) | Excel 2003 | Get the code for a character | text |
| [CONCAT](https://exceljet.net/functions/concat-function) | Excel 2019 | Join text values without delimiter | text1 text2 ... |
| [CONCATENATE](https://exceljet.net/functions/concatenate-function) | Excel 2003 | Join text together | text1 text2 text3 ... |
| [DOLLAR](https://exceljet.net/functions/dollar-function) | Excel 2003 | Convert a number to text in currency format | number decimals |
| [EXACT](https://exceljet.net/functions/exact-function) | Excel 2003 | Compare two text strings | text1 text2 |
| [FIND](https://exceljet.net/functions/find-function) | Excel 2003 | Get the position of one text string inside another | find\_text within\_text start\_num |
| [FIXED](https://exceljet.net/functions/fixed-function) | Excel 2003 | Format number as text with fixed decimals | number decimals no\_commas |
| [LEFT](https://exceljet.net/functions/left-function) | Excel 2003 | Extract text from the left of a string | text num\_chars |
| [LEN](https://exceljet.net/functions/len-function) | Excel 2003 | Get the length of text. | text |
| [LOWER](https://exceljet.net/functions/lower-function) | Excel 2003 | Convert text to lower case | text |
| [MID](https://exceljet.net/functions/mid-function) | Excel 2003 | Extract text from inside a string | text start\_num num\_chars |
| [NUMBERVALUE](https://exceljet.net/functions/numbervalue-function) | Excel 2013 | Convert text to number with custom separators | text decimal\_separator group\_separator |
| [PROPER](https://exceljet.net/functions/proper-function) | Excel 2003 | Capitalize the first letter in each word | text |
| [REPLACE](https://exceljet.net/functions/replace-function) | Excel 2003 | Replace text based on location | old\_text start\_num num\_chars new\_text |
| [REPT](https://exceljet.net/functions/rept-function) | Excel 2003 | Repeat text as specified | text number\_times |
| [RIGHT](https://exceljet.net/functions/right-function) | Excel 2003 | Extract text from the right of a string | text num\_chars |
| [SEARCH](https://exceljet.net/functions/search-function) | Excel 2003 | Get the location of substring in a string | find\_text within\_text start\_num |
| [SUBSTITUTE](https://exceljet.net/functions/substitute-function) | Excel 2003 | Replace text based on content | text old\_text new\_text instance\_num |
| [TEXT](https://exceljet.net/functions/text-function) | Excel 2003 | Convert a number to text with a number format | value format\_text |
| [TEXTJOIN](https://exceljet.net/functions/textjoin-function) | Excel 2019 | Join text values with a delimiter | delimiter ignore\_empty text1 text2 ... |
| [TRIM](https://exceljet.net/functions/trim-function) | Excel 2003 | Remove extra spaces from text | text |
| [UNICHAR](https://exceljet.net/functions/unichar-function) | Excel 2013 | Get Unicode character by number | number |
| [UNICODE](https://exceljet.net/functions/unicode-function) | Excel 2013 | Get number from Unicode character | text |
| [UPPER](https://exceljet.net/functions/upper-function) | Excel 2003 | Convert text to upper case | text |
| [VALUE](https://exceljet.net/functions/value-function) | Excel 2003 | Convert text to a number | text |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Dynamic-array)
Dynamic array
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [ARRAYTOTEXT](https://exceljet.net/functions/arraytotext-function) | Excel 2021 | Converts array or range to a text string | array format |
| [BYCOL](https://exceljet.net/functions/bycol-function) | Excel 2024 | Apply function to column | array lambda |
| [BYROW](https://exceljet.net/functions/byrow-function) | Excel 2024 | Apply function to row | array function |
| [CHOOSECOLS](https://exceljet.net/functions/choosecols-function) | Excel 2024 | Return specific columns from an array | array col\_num1 col\_num2 ... |
| [CHOOSEROWS](https://exceljet.net/functions/chooserows-function) | Excel 2024 | Return specific rows from an array | array row\_num1 row\_num2 ... |
| [DETECTLANGUAGE](https://exceljet.net/functions/detectlanguage-function) | Excel 365 | Detect the language of a given text string | text |
| [DROP](https://exceljet.net/functions/drop-function) | Excel 2024 | Remove portion of an array | array rows col |
| [EXPAND](https://exceljet.net/functions/expand-function) | Excel 2024 | Expand array by adding rows or columns | array rows columns pad\_with |
| [FILTER](https://exceljet.net/functions/filter-function) | Excel 2021 | Filter range with given criteria | array include if\_empty |
| [GROUPBY](https://exceljet.net/functions/groupby-function) | Excel 365 | Summarize data by grouping rows | row\_fields values function field\_headers total\_depth sort\_order filter\_array field\_relationship |
| [HSTACK](https://exceljet.net/functions/hstack-function) | Excel 2024 | Combine ranges or arrays horizontally | array1 array2 ... |
| [IMAGE](https://exceljet.net/functions/image-function) | Excel 2024 | Retrieve image to Excel from the Internet | source alt\_text sizing height width |
| [ISOMITTED](https://exceljet.net/functions/isomitted-function) | Excel 2024 | Check for optional arguments in LAMBDAs | argument |
| [LAMBDA](https://exceljet.net/functions/lambda-function) | Excel 2024 | Create custom function | parameter ... calculation |
| [LET](https://exceljet.net/functions/let-function) | Excel 2021 | Assign variables inside formula | name1 value1 name2/value2 ... result |
| [MAKEARRAY](https://exceljet.net/functions/makearray-function) | Excel 2024 | Create array with calculated values | rows columns function |
| [MAP](https://exceljet.net/functions/map-function) | Excel 2024 | Map array to custom function | array1 array2 ... lambda |
| [PERCENTOF](https://exceljet.net/functions/percentof-function) | Excel 365 | Return a subset of data as a percentage of all data | data\_subset all\_data |
| [PIVOTBY](https://exceljet.net/functions/pivotby-function) | Excel 365 | Summarize data by grouping rows and columns | row\_fields col\_fields values function field\_headers row\_total\_depth row\_sort\_order col\_total\_depth col\_sort\_order filter\_array relative\_to |
| [RANDARRAY](https://exceljet.net/functions/randarray-function) | Excel 2021 | Get array of random numbers | rows columns min max integer |
| [REDUCE](https://exceljet.net/functions/reduce-function) | Excel 2024 | Reduce an array | initial\_value array function |
| [REGEXEXTRACT](https://exceljet.net/functions/regexextract-function) | Excel 365 | Extract text with regex pattern | text pattern return\_mode case\_sensitivity |
| [REGEXREPLACE](https://exceljet.net/functions/regexreplace-function) | Excel 365 | Replace text with a regex pattern | text pattern replacement occurrence case\_sensitivity |
| [REGEXTEST](https://exceljet.net/functions/regextest-function) | Excel 365 | Test a value for a specific pattern of text | text pattern case\_sensitivity |
| [SCAN](https://exceljet.net/functions/scan-function) | Excel 2024 | Scan array and return intermediate results | initial\_value array function |
| [SEQUENCE](https://exceljet.net/functions/sequence-function) | Excel 2021 | Get array of list of sequential numbers | rows columns start step |
| [SORT](https://exceljet.net/functions/sort-function) | Excel 2021 | Sorts range or array | array sort\_index sort\_order by\_col |
| [SORTBY](https://exceljet.net/functions/sortby-function) | Excel 2021 | Sorts range or array by column | array by\_array sort\_order array/order ... |
| [STOCKHISTORY](https://exceljet.net/functions/stockhistory-function) | Excel 365 | Retrieve stock price information | stock start\_date end\_date interval headers properties ... |
| [TAKE](https://exceljet.net/functions/take-function) | Excel 2024 | Get a subset of an array | array rows col |
| [TEXTAFTER](https://exceljet.net/functions/textafter-function) | Excel 2024 | Extract text after a delimiter | text delimiter instance\_num match\_mode match\_end if\_not\_found |
| [TEXTBEFORE](https://exceljet.net/functions/textbefore-function) | Excel 2024 | Extract text before a delimiter | text delimiter instance\_num match\_mode match\_end if\_not\_found |
| [TEXTSPLIT](https://exceljet.net/functions/textsplit-function) | Excel 2024 | Split a text string with a delimiter | text col\_delimiter row\_delimiter ignore\_empty match\_mode pad\_with |
| [TOCOL](https://exceljet.net/functions/tocol-function) | Excel 2024 | Transform array to single column | array ignore scan\_by\_column |
| [TOROW](https://exceljet.net/functions/torow-function) | Excel 2024 | Transform array to single row | array ignore scan\_by\_column |
| [TRANSLATE](https://exceljet.net/functions/translate-function) | Excel 365 | Translate text from one language to another | text source\_language target\_language |
| [TRIMRANGE](https://exceljet.net/functions/trimrange-function) | Excel 365 | Remove empty rows and columns from a range | range trim\_rows trim\_columns |
| [UNIQUE](https://exceljet.net/functions/unique-function) | Excel 2021 | Extract unique values from range | array by\_col exactly\_once |
| [VALUETOTEXT](https://exceljet.net/functions/valuetotext-function) | Excel 2021 | Converts a value to a text string | value format |
| [VSTACK](https://exceljet.net/functions/vstack-function) | Excel 2024 | Combine ranges or arrays vertically | array1 array2 ... |
| [WRAPCOLS](https://exceljet.net/functions/wrapcols-function) | Excel 2024 | Wrap array into columns | vector wrap\_count pad\_with |
| [WRAPROWS](https://exceljet.net/functions/wraprows-function) | Excel 2024 | Wrap array into rows | vector wrap\_count pad\_with |
| [XLOOKUP](https://exceljet.net/functions/xlookup-function) | Excel 2021 | Look up values in range or array | lookup lookup\_array return\_array if\_not\_found match\_mode search\_mode |
| [XMATCH](https://exceljet.net/functions/xmatch-function) | Excel 2021 | Get the position of an item in a list or table | lookup\_value lookup\_array match\_mode search\_mode |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Engineering)
Engineering
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [BIN2DEC](https://exceljet.net/functions/bin2dec-function) | Excel 2003 | Converts a binary number to decimal | number |
| [BIN2HEX](https://exceljet.net/functions/bin2hex-function) | Excel 2003 | Converts a binary number to hexadecimal | number places |
| [BIN2OCT](https://exceljet.net/functions/bin2oct-function) | Excel 2003 | Converts a binary number to octal | number places |
| [BITAND](https://exceljet.net/functions/bitand-function) | Excel 2013 | Returns a 'Bitwise And' of two numbers | number1 number2 |
| [BITLSHIFT](https://exceljet.net/functions/bitlshift-function) | Excel 2013 | Returns a number shifted left by some number of bits | number shift\_amount |
| [BITOR](https://exceljet.net/functions/bitor-function) | Excel 2013 | Returns a 'Bitwise Or' of two numbers | number1 number2 |
| [BITRSHIFT](https://exceljet.net/functions/bitrshift-function) | Excel 2013 | Returns a number shifted right by some number of bits | number shift\_amount |
| [BITXOR](https://exceljet.net/functions/bitxor-function) | Excel 2013 | Returns a 'Bitwise Xor' of two numbers | number1 number2 |
| [COMPLEX](https://exceljet.net/functions/complex-function) | Excel 2003 | Get the string representation of a complex number | real\_num i\_num suffix |
| [CONVERT](https://exceljet.net/functions/convert-function) | Excel 2003 | Convert measurement units | number from\_unit to\_unit |
| [DEC2BIN](https://exceljet.net/functions/dec2bin-function) | Excel 2003 | Converts a decimal number to binary | number places |
| [DEC2HEX](https://exceljet.net/functions/dec2hex-function) | Excel 2003 | Converts a decimal number to hexadecimal | number places |
| [DEC2OCT](https://exceljet.net/functions/dec2oct-function) | Excel 2003 | Converts a decimal number to octal | number places |
| [DELTA](https://exceljet.net/functions/delta-function) | Excel 2003 | Test two values are equal | number1 number2 |
| [HEX2BIN](https://exceljet.net/functions/hex2bin-function) | Excel 2003 | Converts a hexadecimal number to binary | number places |
| [HEX2DEC](https://exceljet.net/functions/hex2dec-function) | Excel 2003 | Converts a hexadecimal number to decimal | number |
| [HEX2OCT](https://exceljet.net/functions/hex2oct-function) | Excel 2003 | Converts a hexadecimal number to octal | number places |
| [IMABS](https://exceljet.net/functions/imabs-function) | Excel 2003 | Get the absolute value of a complex number | inumber |
| [IMAGINARY](https://exceljet.net/functions/imaginary-function) | Excel 2003 | Get the imaginary part of a complex number | inumber |
| [IMARGUMENT](https://exceljet.net/functions/imargument-function) | Excel 2003 | Get the angle of a complex number | inumber |
| [IMCONJUGATE](https://exceljet.net/functions/imconjugate-function) | Excel 2003 | Get the complex conjugate of a complex number | inumber |
| [IMCOS](https://exceljet.net/functions/imcos-function) | Excel 2003 | Get cosine of complex number. | complex\_num |
| [IMCOSH](https://exceljet.net/functions/imcosh-function) | Excel 2013 | Get hyperbolic cosine of complex number | complex\_num |
| [IMCOT](https://exceljet.net/functions/imcot-function) | Excel 2013 | Get cotangent of complex number. | complex\_num |
| [IMCSC](https://exceljet.net/functions/imcsc-function) | Excel 2013 | Get cosecant of complex number | complex\_num |
| [IMCSCH](https://exceljet.net/functions/imcsch-function) | Excel 2013 | Get hyperbolic cosecant of complex number | complex\_num |
| [IMDIV](https://exceljet.net/functions/imdiv-function) | Excel 2003 | Get quotient of two complex numbers. | complex\_num1 complex\_num2 |
| [IMEXP](https://exceljet.net/functions/imexp-function) | Excel 2003 | Get exponential of complex number. | complex\_num |
| [IMLN](https://exceljet.net/functions/imln-function) | Excel 2003 | Get natural log complex number | complex\_num |
| [IMLOG10](https://exceljet.net/functions/imlog10-function) | Excel 2003 | Returns the base-10 logarithm of a complex number. | complex\_num |
| [IMLOG2](https://exceljet.net/functions/imlog2-function) | Excel 2003 | Get base-2 log of a complex number. | complex\_num |
| [IMPOWER](https://exceljet.net/functions/impower-function) | Excel 2003 | Raise complex number to given power | inumber number |
| [IMPRODUCT](https://exceljet.net/functions/improduct-function) | Excel 2003 | Get product of complex numbers | inumber1 inumber2 ... |
| [IMREAL](https://exceljet.net/functions/imreal-function) | Excel 2003 | Get real part of a complex number | inumber |
| [IMSEC](https://exceljet.net/functions/imsec-function) | Excel 2013 | Get secant of complex number | complex\_num |
| [IMSECH](https://exceljet.net/functions/imsech-function) | Excel 2013 | Get hyperbolic secant of a complex number | complex\_num |
| [IMSIN](https://exceljet.net/functions/imsin-function) | Excel 2003 | Get sine of complex number. | complex\_num |
| [IMSINH](https://exceljet.net/functions/imsinh-function) | Excel 2013 | Get hyperbolic sine of the complex number. | complex\_num |
| [IMSQRT](https://exceljet.net/functions/imsqrt-function) | Excel 2003 | Get square root of a complex number | inumber |
| [IMSUB](https://exceljet.net/functions/imsub-function) | Excel 2003 | Get difference between two complex numbers | inumber1 inumber2 |
| [IMSUM](https://exceljet.net/functions/imsum-function) | Excel 2003 | Get sum of complex numbers | inumber1 inumber2 ... |
| [IMTAN](https://exceljet.net/functions/imtan-function) | Excel 2013 | Get the tangent of a complex number. | complex\_num |
| [OCT2BIN](https://exceljet.net/functions/oct2bin-function) | Excel 2003 | Convert octal number to binary | number places |
| [OCT2DEC](https://exceljet.net/functions/oct2dec-function) | Excel 2003 | Converts an octal number to its decimal equivalent | number |
| [OCT2HEX](https://exceljet.net/functions/oct2hex-function) | Excel 2003 | Converts an octal number to its hexadecimal equivalent | number places |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Financial)
Financial
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [ACCRINT](https://exceljet.net/functions/accrint-function) | Excel 2003 | Get accrued interest periodic | id fd sd rate par freq basis calc |
| [ACCRINTM](https://exceljet.net/functions/accrintm-function) | Excel 2003 | Get accrued interest at maturity | id sd rate par basis |
| [AMORDEGRC](https://exceljet.net/functions/amordegrc-function) | Excel 2003 | Depreciation for accounting period coefficient | cost purchase first salvage period rate basis |
| [AMORLINC](https://exceljet.net/functions/amorlinc-function) | Excel 2003 | Depreciation for accounting period | cost purchase first salvage period rate basis |
| [COUPDAYBS](https://exceljet.net/functions/coupdaybs-function) | Excel 2003 | Get days from coupon period to settlement date | settlement maturity frequency basis |
| [COUPDAYS](https://exceljet.net/functions/coupdays-function) | Excel 2003 | Get days in coupon period incl settlement date | settlement maturity frequency basis |
| [COUPDAYSNC](https://exceljet.net/functions/coupdaysnc-function) | Excel 2003 | Get days from settlement date to next coupon date | settlement maturity frequency basis |
| [COUPNCD](https://exceljet.net/functions/coupncd-function) | Excel 2003 | Get next coupon date after settlement date | settlement maturity frequency basis |
| [COUPNUM](https://exceljet.net/functions/coupnum-function) | Excel 2003 | Get number of coupons payable | settlement maturity frequency basis |
| [COUPPCD](https://exceljet.net/functions/couppcd-function) | Excel 2003 | Get previous coupon date before settlement date | settlement maturity frequency basis |
| [CUMIPMT](https://exceljet.net/functions/cumipmt-function) | Excel 2003 | Get cumulative interest paid on a loan | rate nper pv start\_period end\_period type |
| [CUMPRINC](https://exceljet.net/functions/cumprinc-function) | Excel 2003 | Get cumulative principal paid on a loan | rate nper pv start\_period end\_period type |
| [DB](https://exceljet.net/functions/db-function) | Excel 2003 | Depreciation - fixed-declining balance | cost salvage life period month |
| [DDB](https://exceljet.net/functions/ddb-function) | Excel 2003 | Depreciation - double-declining | cost salvage life period factor |
| [DISC](https://exceljet.net/functions/disc-function) | Excel 2003 | Get discount rate for a security | settlement maturity pr redemption basis |
| [DOLLARDE](https://exceljet.net/functions/dollarde-function) | Excel 2003 | Convert dollar price as fraction to decimal | fractional\_dollar fraction |
| [DOLLARFR](https://exceljet.net/functions/dollarfr-function) | Excel 2003 | Convert price to fractional notation | decimal\_dollar fraction |
| [DURATION](https://exceljet.net/functions/duration-function) | Excel 2003 | Get annual duration with periodic interest | settlement maturity coupon yld freq basis |
| [EFFECT](https://exceljet.net/functions/effect-function) | Excel 2003 | Get effective annual interest rate | nominal\_rate npery |
| [FV](https://exceljet.net/functions/fv-function) | Excel 2003 | Get the future value of an investment | rate nper pmt pv type |
| [FVSCHEDULE](https://exceljet.net/functions/fvschedule-function) | Excel 2003 | Get future value of principal compound interest | principal schedule |
| [INTRATE](https://exceljet.net/functions/intrate-function) | Excel 2003 | Get interest rate for fully invested security | settlement maturity investment redemption basis |
| [IPMT](https://exceljet.net/functions/ipmt-function) | Excel 2003 | Get interest in given period | rate per nper pv fv type |
| [IRR](https://exceljet.net/functions/irr-function) | Excel 2003 | Calculate internal rate of return | values guess |
| [ISPMT](https://exceljet.net/functions/ispmt-function) | Excel 2003 | Get interest paid for specific period | rate per nper pv |
| [MDURATION](https://exceljet.net/functions/mduration-function) | Excel 2003 | Get Macauley modified duration par value of $100 | settlement maturity coupon yld freq basis |
| [MIRR](https://exceljet.net/functions/mirr-function) | Excel 2003 | Calculate modified internal rate of return | values finance\_rate reinvest\_rate |
| [NOMINAL](https://exceljet.net/functions/nominal-function) | Excel 2003 | Get annual nominal interest rate | effect\_rate npery |
| [NPER](https://exceljet.net/functions/nper-function) | Excel 2003 | Get number of periods for loan or investment | rate pmt pv fv type |
| [NPV](https://exceljet.net/functions/npv-function) | Excel 2003 | Calculate net present value | rate value1 value2 ... |
| [ODDFPRICE](https://exceljet.net/functions/oddfprice-function) | Excel 2003 | Get price per $100 odd first period | sd md id fd rate yld redem freq basis |
| [ODDFYIELD](https://exceljet.net/functions/oddfyield-function) | Excel 2003 | Get yield security with odd first period | sd md id fd rate pr redem freq basis |
| [ODDLPRICE](https://exceljet.net/functions/oddlprice-function) | Excel 2003 | Get price per $100 face value with odd last period | sd md id rate yld redem freq basis |
| [ODDLYIELD](https://exceljet.net/functions/oddlyield-function) | Excel 2003 | Get yield of security with odd last period | sd md ld rate pr redem freq basis |
| [PDURATION](https://exceljet.net/functions/pduration-function) | Excel 2013 | Get periods required to reach given value | rate pv fv |
| [PMT](https://exceljet.net/functions/pmt-function) | Excel 2003 | Get the periodic payment for a loan | rate nper pv fv type |
| [PPMT](https://exceljet.net/functions/ppmt-function) | Excel 2003 | Get principal payment in given period | rate per nper pv fv type |
| [PRICE](https://exceljet.net/functions/price-function) | Excel 2003 | Get price per $100 face value - periodic interest | sd md rate yld redemption frequency basis |
| [PRICEDISC](https://exceljet.net/functions/pricedisc-function) | Excel 2003 | Get price per $100 discounted security | sd md discount redemption basis |
| [PRICEMAT](https://exceljet.net/functions/pricemat-function) | Excel 2003 | Get price per $100 interest at maturity | sd md id rate yld basis |
| [PV](https://exceljet.net/functions/pv-function) | Excel 2003 | Get the present value of an investment | rate nper pmt fv type |
| [RATE](https://exceljet.net/functions/rate-function) | Excel 2003 | Get the interest rate per period of an annuity | nper pmt pv fv type guess |
| [RECEIVED](https://exceljet.net/functions/received-function) | Excel 2003 | Get amount received at maturity | settlement maturity investment discount basis |
| [RRI](https://exceljet.net/functions/rri-function) | Excel 2013 | Get equivalent interest rate for growth | nper pv fv |
| [SLN](https://exceljet.net/functions/sln-function) | Excel 2003 | Depreciation - straight-line | cost salvage life |
| [SYD](https://exceljet.net/functions/syd-function) | Excel 2003 | Depreciation - sum-of-years | cost salvage life period |
| [TBILLEQ](https://exceljet.net/functions/tbilleq-function) | Excel 2003 | Get bond-equivalent yield for a Treasury bill | settlement maturity discount |
| [TBILLPRICE](https://exceljet.net/functions/tbillprice-function) | Excel 2003 | Get price per $100 Treasury bill | settlement maturity discount |
| [TBILLYIELD](https://exceljet.net/functions/tbillyield-function) | Excel 2003 | Get yield for a Treasury bill | settlement maturity price |
| [VDB](https://exceljet.net/functions/vdb-function) | Excel 2003 | Depreciation - double-declining variable | cost salvage life start end factor no\_switch |
| [XIRR](https://exceljet.net/functions/xirr-function) | Excel 2003 | Calculate internal rate of return for irregular cash flows | values dates guess |
| [XNPV](https://exceljet.net/functions/xnpv-function) | Excel 2003 | Calculate net present value for irregular cash flows | rate values dates |
| [YIELD](https://exceljet.net/functions/yield-function) | Excel 2003 | Get yield for security that pays periodic interest | sd md rate pr redemption frequency basis |
| [YIELDDISC](https://exceljet.net/functions/yielddisc-function) | Excel 2003 | Get annual yield for discounted security | sd md pr redemption basis |
| [YIELDMAT](https://exceljet.net/functions/yieldmat-function) | Excel 2003 | Get annual yield of security interest at maturity | sd md id rate pr basis |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Information)
Information
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [CELL](https://exceljet.net/functions/cell-function) | Excel 2003 | Get information about a cell | info\_type reference |
| [ERROR.TYPE](https://exceljet.net/functions/errortype-function) | Excel 2003 | Test for a specific error value | error\_val |
| [INFO](https://exceljet.net/functions/info-function) | Excel 2003 | Get information about current environment | type\_text |
| [ISBLANK](https://exceljet.net/functions/isblank-function) | Excel 2003 | Test if a cell is empty | value |
| [ISERR](https://exceljet.net/functions/iserr-function) | Excel 2003 | Test for any error but #N/A | value |
| [ISERROR](https://exceljet.net/functions/iserror-function) | Excel 2003 | Test for any error | value |
| [ISEVEN](https://exceljet.net/functions/iseven-function) | Excel 2003 | Test if a value is even | value |
| [ISFORMULA](https://exceljet.net/functions/isformula-function) | Excel 2013 | Test if cell contains a formula | reference |
| [ISLOGICAL](https://exceljet.net/functions/islogical-function) | Excel 2003 | Test if a value is logical | value |
| [ISNA](https://exceljet.net/functions/isna-function) | Excel 2003 | Test for the #N/A error | value |
| [ISNONTEXT](https://exceljet.net/functions/isnontext-function) | Excel 2003 | Test for a non-text value | value |
| [ISNUMBER](https://exceljet.net/functions/isnumber-function) | Excel 2003 | Test for numeric value | value |
| [ISODD](https://exceljet.net/functions/isodd-function) | Excel 2003 | Test if a value is odd | value |
| [ISREF](https://exceljet.net/functions/isref-function) | Excel 2003 | Test for a reference | value |
| [ISTEXT](https://exceljet.net/functions/istext-function) | Excel 2003 | Test for a text value | value |
| [N](https://exceljet.net/functions/n-function) | Excel 2003 | Convert a value to a number | value |
| [NA](https://exceljet.net/functions/na-function) | Excel 2003 | Create an #N/A error |     |
| [SHEET](https://exceljet.net/functions/sheet-function) | Excel 2013 | Get sheet index number | value |
| [SHEETS](https://exceljet.net/functions/sheets-function) | Excel 2013 | Get number of sheets in a reference | reference |
| [T](https://exceljet.net/functions/t-function) | Excel 2003 | Filter text values only | value |
| [TYPE](https://exceljet.net/functions/type-function) | Excel 2003 | Get the type of value in a cell | value |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Math)
Math
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [ABS](https://exceljet.net/functions/abs-function) | Excel 2003 | Find the absolute value of a number | number |
| [AGGREGATE](https://exceljet.net/functions/aggregate-function) | Excel 2010 | Return aggregate calculation | function\_num options ref1 ref2 ... |
| [ARABIC](https://exceljet.net/functions/arabic-function) | Excel 2013 | Converts a Roman numerals to an Arabic numerals | roman\_text |
| [BASE](https://exceljet.net/functions/base-function) | Excel 2013 | Convert number to another base. | number radix min\_length |
| [CEILING](https://exceljet.net/functions/ceiling-function) | Excel 2003 | Round a number up to nearest multiple | number significance |
| [CEILING.MATH](https://exceljet.net/functions/ceiling.math-function) | Excel 2013 | Round a number up to nearest multiple | number significance mode |
| [CEILING.PRECISE](https://exceljet.net/functions/ceiling.precise-function) | Excel 2010 | Round a number up to nearest multiple | number significance |
| [COMBIN](https://exceljet.net/functions/combin-function) | Excel 2003 | Get number of combinations without repetitions | number number\_chosen |
| [COMBINA](https://exceljet.net/functions/combina-function) | Excel 2013 | Get number of combinations with repetitions | number number\_chosen |
| [DECIMAL](https://exceljet.net/functions/decimal-function) | Excel 2013 | Convert a number in a different base to a decimal number | number radix |
| [EVEN](https://exceljet.net/functions/even-function) | Excel 2003 | Round a number up to the next even integer | number |
| [EXP](https://exceljet.net/functions/exp-function) | Excel 2003 | Find the value of e raised to the power of a number | number |
| [FACT](https://exceljet.net/functions/fact-function) | Excel 2003 | Find the factorial of a number | number |
| [FACTDOUBLE](https://exceljet.net/functions/factdouble-function) | Excel 2003 | Get double factorial of a number | number |
| [FLOOR](https://exceljet.net/functions/floor-function) | Excel 2003 | Round a number down to the nearest specified multiple | number significance |
| [FLOOR.MATH](https://exceljet.net/functions/floor.math-function) | Excel 2013 | Round number down to nearest multiple | number significance mode |
| [FLOOR.PRECISE](https://exceljet.net/functions/floor.precise-function) | Excel 2010 | Round number down to nearest multiple | number significance |
| [GCD](https://exceljet.net/functions/gcd-function) | Excel 2003 | Get the greatest common divisor of numbers | number1 number2 ... |
| [INT](https://exceljet.net/functions/int-function) | Excel 2003 | Get the integer part of a number by rounding down | number |
| [LCM](https://exceljet.net/functions/lcm-function) | Excel 2003 | Get the least common multiple of numbers | number1 number2 ... |
| [LN](https://exceljet.net/functions/ln-function) | Excel 2003 | Get the natural logarithm of a number | number |
| [LOG](https://exceljet.net/functions/log-function) | Excel 2003 | Get the logarithm of a number | number base |
| [LOG10](https://exceljet.net/functions/log10-function) | Excel 2003 | Get the base-10 logarithm of a number | number |
| [MDETERM](https://exceljet.net/functions/mdeterm-function) | Excel 2003 | Get matrix determinant of given array | array |
| [MINVERSE](https://exceljet.net/functions/minverse-function) | Excel 2003 | Get inverse matrix of array | array |
| [MMULT](https://exceljet.net/functions/mmult-function) | Excel 2003 | Perform matrix multiplication | array1 array2 |
| [MOD](https://exceljet.net/functions/mod-function) | Excel 2003 | Get the remainder from division | number divisor |
| [MROUND](https://exceljet.net/functions/mround-function) | Excel 2003 | Round a number to the nearest specified multiple | number significance |
| [MULTINOMIAL](https://exceljet.net/functions/multinomial-function) | Excel 2003 | Calculate the multinomial coefficient for a list of numbers | number1 number2 ... |
| [MUNIT](https://exceljet.net/functions/munit-function) | Excel 2013 | Return unit matrix for a given dimension | dimension |
| [ODD](https://exceljet.net/functions/odd-function) | Excel 2003 | Round a number up to the next odd integer | number |
| [PI](https://exceljet.net/functions/pi-function) | Excel 2003 | Get the value of π |     |
| [POWER](https://exceljet.net/functions/power-function) | Excel 2003 | Raise a number to a power | number power |
| [PRODUCT](https://exceljet.net/functions/product-function) | Excel 2003 | Get the product of supplied numbers | number1 number2 ... |
| [QUOTIENT](https://exceljet.net/functions/quotient-function) | Excel 2003 | Returns the quotient without a remainder. | numerator denominator |
| [RAND](https://exceljet.net/functions/rand-function) | Excel 2003 | Get a random number between 0 and 1 |     |
| [RANDBETWEEN](https://exceljet.net/functions/randbetween-function) | Excel 2003 | Get a random integer between two values | bottom top |
| [ROMAN](https://exceljet.net/functions/roman-function) | Excel 2003 | Converts numbers to Roman numerals | number form |
| [ROUND](https://exceljet.net/functions/round-function) | Excel 2003 | Round a number to a given number of digits | number num\_digits |
| [ROUNDDOWN](https://exceljet.net/functions/rounddown-function) | Excel 2003 | Round down to given number of digits | number num\_digits |
| [ROUNDUP](https://exceljet.net/functions/roundup-function) | Excel 2003 | Round a number up to a given number of digits | number num\_digits |
| [SIGN](https://exceljet.net/functions/sign-function) | Excel 2003 | Get the sign of a number | number |
| [SQRT](https://exceljet.net/functions/sqrt-function) | Excel 2003 | Find the positive square root of a number | number |
| [SQRTPI](https://exceljet.net/functions/sqrtpi-function) | Excel 2003 | Get the square root of (number × π) | number |
| [SUBTOTAL](https://exceljet.net/functions/subtotal-function) | Excel 2003 | Get a subtotal in a list or database | function\_num ref1 ref2 ... |
| [SUM](https://exceljet.net/functions/sum-function) | Excel 2003 | Add numbers together | number1 number2 number3 ... |
| [SUMIF](https://exceljet.net/functions/sumif-function) | Excel 2003 | Sum cells in a range that meet criteria | range criteria sum\_range |
| [SUMIFS](https://exceljet.net/functions/sumifs-function) | Excel 2007 | Sum cells in a range that meet criteria | sum\_range range1 criteria1 range2 criteria2 ... |
| [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function) | Excel 2003 | Multiply, then sum arrays | array1 array2 ... |
| [SUMSQ](https://exceljet.net/functions/sumsq-function) | Excel 2003 | Get sum of squares of supplied values | number1 number2 ... |
| [SUMX2MY2](https://exceljet.net/functions/sumx2my2-function) | Excel 2003 | Sum of difference of squares in two arrays | array\_x array\_y |
| [SUMX2PY2](https://exceljet.net/functions/sumx2py2-function) | Excel 2003 | Get sum of squares in two arrays | array\_x array\_y |
| [SUMXMY2](https://exceljet.net/functions/sumxmy2-function) | Excel 2003 | Sum of squares of differences in two arrays | array\_x array\_y |
| [TRUNC](https://exceljet.net/functions/trunc-function) | Excel 2003 | Truncate a number to a given precision | number num\_digits |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Trigonometry)
Trigonometry
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [ACOS](https://exceljet.net/functions/acos-function) | Excel 2003 | Get the inverse cosine of a value, in radians. | number |
| [ACOSH](https://exceljet.net/functions/acosh-function) | Excel 2003 | Get inverse hyperbolic cosine number. | number |
| [ACOT](https://exceljet.net/functions/acot-function) | Excel 2013 | Get arccotangent of a number. | number |
| [ACOTH](https://exceljet.net/functions/acoth-function) | Excel 2013 | Get the inverse hyperbolic cotangent of a number | number |
| [ASIN](https://exceljet.net/functions/asin-function) | Excel 2003 | Return the inverse sine of a value in radians. | number |
| [ASINH](https://exceljet.net/functions/asinh-function) | Excel 2003 | Get inverse hyperbolic sine of number. | number |
| [ATAN](https://exceljet.net/functions/atan-function) | Excel 2003 | Get arctangent of a number | number |
| [ATAN2](https://exceljet.net/functions/atan2-function) | Excel 2003 | Get arctangent from x- and y-coordinates | x\_num y\_num |
| [ATANH](https://exceljet.net/functions/atanh-function) | Excel 2003 | Get inverse hyperbolic tangent of number | number |
| [COS](https://exceljet.net/functions/cos-function) | Excel 2003 | Get the cosine of an angle provided in radians. | number |
| [COSH](https://exceljet.net/functions/cosh-function) | Excel 2003 | Get hyperbolic cosine of a number | number |
| [COT](https://exceljet.net/functions/cot-function) | Excel 2013 | Get the cotangent of an angle. | number |
| [COTH](https://exceljet.net/functions/coth-function) | Excel 2013 | Get the hyperbolic cotangent of an angle | number |
| [CSC](https://exceljet.net/functions/csc-function) | Excel 2013 | Get cosecant of an angle | number |
| [CSCH](https://exceljet.net/functions/csch-function) | Excel 2013 | Get hyperbolic cosecant of an angle. | number |
| [DEGREES](https://exceljet.net/functions/degrees-function) | Excel 2003 | Converts radians to degrees | angle |
| [RADIANS](https://exceljet.net/functions/radians-function) | Excel 2003 | Converts degrees into radians | angle |
| [SEC](https://exceljet.net/functions/sec-function) | Excel 2013 | Get secant of an angle | number |
| [SECH](https://exceljet.net/functions/sech-function) | Excel 2013 | Get hyperbolic secant of an angle | number |
| [SIN](https://exceljet.net/functions/sin-function) | Excel 2003 | Get the sine of an angle provided in radians. | number |
| [SINH](https://exceljet.net/functions/sinh-function) | Excel 2003 | Get hyperbolic sine of a number. | number |
| [TAN](https://exceljet.net/functions/tan-function) | Excel 2003 | Get the tangent of an angle | number |
| [TANH](https://exceljet.net/functions/tanh-function) | Excel 2003 | Get hyperbolic tangent of a number. | number |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Statistical)
Statistical
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [AVEDEV](https://exceljet.net/functions/avedev-function) | Excel 2003 | Get sum of squared deviations | number1 number2 ... |
| [AVERAGE](https://exceljet.net/functions/average-function) | Excel 2003 | Get the average of a group of numbers | number1 number2 ... |
| [AVERAGEA](https://exceljet.net/functions/averagea-function) | Excel 2003 | Get the average of a group of numbers and text | value1 value2 ... |
| [AVERAGEIF](https://exceljet.net/functions/averageif-function) | Excel 2007 | Get the average of numbers that meet criteria. | range criteria average\_range |
| [AVERAGEIFS](https://exceljet.net/functions/averageifs-function) | Excel 2007 | Average cells that match multiple criteria | avg\_rng range1 criteria1 range2 criteria2 ... |
| [BINOM.DIST](https://exceljet.net/functions/binom.dist-function) | Excel 2010 | Get binomial distribution probability | number\_s trials probability\_s cumulative |
| [BINOMDIST](https://exceljet.net/functions/binomdist-function) | Excel 2003 | Get binomial distribution probability | number\_s trials probability\_s cumulative |
| [CORREL](https://exceljet.net/functions/correl-function) | Excel 2003 | Get correlation coefficient between two data sets | array1 array2 |
| [COUNT](https://exceljet.net/functions/count-function) | Excel 2003 | Count numbers | value1 value2 ... |
| [COUNTA](https://exceljet.net/functions/counta-function) | Excel 2003 | Count the number of non-blank cells | value1 value2 ... |
| [COUNTBLANK](https://exceljet.net/functions/countblank-function) | Excel 2003 | Count cells that are blank | range |
| [COUNTIF](https://exceljet.net/functions/countif-function) | Excel 2003 | Count cells that match criteria | range criteria |
| [COUNTIFS](https://exceljet.net/functions/countifs-function) | Excel 2007 | Count cells that match multiple criteria | range1 criteria1 range2 criteria2 ... |
| [COVAR](https://exceljet.net/functions/covar-function) | Excel 2003 | Get the population covariance between two arrays. | array1 array2 |
| [COVARIANCE.P](https://exceljet.net/functions/covariance.p-function) | Excel 2010 | Get the population covariance between paired data | array1 array2 |
| [COVARIANCE.S](https://exceljet.net/functions/covariance.s-function) | Excel 2010 | Get the sample covariance between paired data | array1 array2 |
| [DEVSQ](https://exceljet.net/functions/devsq-function) | Excel 2003 | Get sum of squared deviations | number1 number2 ... |
| [EXPON.DIST](https://exceljet.net/functions/expon.dist-function) | Excel 2010 | Get the PDF or CDF of the exponential distribution. | x lambda cumulative |
| [EXPONDIST](https://exceljet.net/functions/expondist-function) | Excel 2003 | Get the PDF or CDF of the exponential distribution. | x lambda cumulative |
| [FORECAST](https://exceljet.net/functions/forecast-function) | Excel 2003 | Predict value along a linear trend | x known\_ys known\_xs |
| [FORECAST.ETS](https://exceljet.net/functions/forecast.ets-function) | Excel 2016 | Predict value with a seasonal trend | target\_date values timeline seasonality data\_completion aggregation |
| [FORECAST.ETS.CONFINT](https://exceljet.net/functions/forecast.ets.confint-function) | Excel 2016 | Get confidence interval for forecast value at given date | target\_date values timeline confidence\_level seasonality data\_completion aggregation |
| [FORECAST.ETS.SEASONALITY](https://exceljet.net/functions/forecast.ets.seasonality-function) | Excel 2016 | Get length of the seasonal pattern | values timeline data\_completion aggregation |
| [FORECAST.ETS.STAT](https://exceljet.net/functions/forecast.ets.stat-function) | Excel 2016 | Get statistical value related to forecasting | values timeline statistic\_type seasonality data\_completion aggregation |
| [FORECAST.LINEAR](https://exceljet.net/functions/forecast.linear-function) | Excel 2016 | Predict value along a linear trend | x known\_ys known\_xs |
| [FREQUENCY](https://exceljet.net/functions/frequency-function) | Excel 2003 | Get the frequency of values in a data set | data\_array bins\_array |
| [GAMMA](https://exceljet.net/functions/gamma-function) | Excel 2013 | Extends factorial calculations to decimal numbers | number |
| [GAMMA.DIST](https://exceljet.net/functions/gamma.dist-function) | Excel 2010 | Get the PDF or CDF of the gamma distribution | x alpha beta cumulative |
| [GAMMA.INV](https://exceljet.net/functions/gamma.inv-function) | Excel 2010 | Get inverse of gamma cumulative distribution | probability alpha beta |
| [GAMMADIST](https://exceljet.net/functions/gammadist-function) | Excel 2003 | Get the PDF or CDF of the gamma distribution | x alpha beta cumulative |
| [GAMMAINV](https://exceljet.net/functions/gammainv-function) | Excel 2003 | Get inverse of the gamma cumulative distribution | probability alpha beta |
| [GAMMALN](https://exceljet.net/functions/gammaln-function) | Excel 2003 | Calculate the natural logarithm of the gamma function. | x   |
| [GAMMALN.PRECISE](https://exceljet.net/functions/gammaln.precise-function) | Excel 2010 | To calculate the natural logarithm of the gamma function. | x   |
| [GEOMEAN](https://exceljet.net/functions/geomean-function) | Excel 2003 | Calculate geometric mean | number1 number2 ... |
| [GROWTH](https://exceljet.net/functions/growth-function) | Excel 2003 | Forecast exponential growth by fitting an exponential curve to existing data and predicts values. | known\_y known\_x new\_x const |
| [HARMEAN](https://exceljet.net/functions/harmean-function) | Excel 2003 | Calculate harmonic mean | number1 number2 ... |
| [INTERCEPT](https://exceljet.net/functions/intercept-function) | Excel 2003 | Get intercept of linear regression line | known\_ys known\_xs |
| [LARGE](https://exceljet.net/functions/large-function) | Excel 2003 | Get nth largest value | array k |
| [LINEST](https://exceljet.net/functions/linest-function) | Excel 2003 | Get parameters of linear trend | known\_ys known\_xs const stats |
| [MAX](https://exceljet.net/functions/max-function) | Excel 2003 | Get the largest value | number1 number2 ... |
| [MAXA](https://exceljet.net/functions/maxa-function) | Excel 2003 | Return largest value. | value1 value2 ... |
| [MAXIFS](https://exceljet.net/functions/maxifs-function) | Excel 2019 | Get maximum value with criteria | max\_range range1 criteria1 range2 criteria2 ... |
| [MEDIAN](https://exceljet.net/functions/median-function) | Excel 2003 | Get the median of a group of numbers | number1 number2 ... |
| [MIN](https://exceljet.net/functions/min-function) | Excel 2003 | Get the smallest value. | number1 number2 ... |
| [MINA](https://exceljet.net/functions/mina-function) | Excel 2003 | Return smallest value. | value1 value2 ... |
| [MINIFS](https://exceljet.net/functions/minifs-function) | Excel 2019 | Get minimum value with criteria | min\_range range1 criteria1 range2 criteria2 ... |
| [MODE](https://exceljet.net/functions/mode-function) | Excel 2003 | Get most frequently occurring number | number1 number2 ... |
| [MODE.MULT](https://exceljet.net/functions/mode.mult-function) | Excel 2010 | Get most frequently occurring numbers | number1 number2 ... |
| [MODE.SNGL](https://exceljet.net/functions/mode.sngl-function) | Excel 2010 | Get most frequently occurring number | number1 number2 ... |
| [NORM.DIST](https://exceljet.net/functions/norm.dist-function) | Excel 2010 | Get values and areas for the normal distribution | x mean standard\_dev cumulative |
| [NORM.INV](https://exceljet.net/functions/norm.inv-function) | Excel 2010 | Get the inverse of normal cumulative distribution | probability mean standard\_dev |
| [NORM.S.DIST](https://exceljet.net/functions/norm.s.dist-function) | Excel 2010 | Get the standard normal CDF and PDF. | z cumulative |
| [NORM.S.INV](https://exceljet.net/functions/norm.s.inv-function) | Excel 2010 | Get inverse of the standard normal cumulative distribution | probability |
| [NORMSDIST](https://exceljet.net/functions/normsdist-function) | Excel 2003 | Calculate the standard normal cumulative distribution function (CDF) for a given z-score. | z   |
| [NORMSINV](https://exceljet.net/functions/normsinv-function) | Excel 2003 | Calculate the inverse of the standard normal cumulative distribution function (CDF) for a given probability. | probability |
| [PEARSON](https://exceljet.net/functions/pearson-function) | Excel 2003 | To measure the strength and direction of the linear relationship between two variables. | array1 array2 |
| [PERCENTILE](https://exceljet.net/functions/percentile-function) | Excel 2003 | Get kth percentile | array k |
| [PERCENTILE.EXC](https://exceljet.net/functions/percentile.exc-function) | Excel 2010 | Get kth percentile | array k |
| [PERCENTILE.INC](https://exceljet.net/functions/percentile.inc-function) | Excel 2010 | Get kth percentile | array k |
| [PERCENTRANK](https://exceljet.net/functions/percentrank-function) | Excel 2003 | Get percentile rank, inclusive | array x significance |
| [PERCENTRANK.EXC](https://exceljet.net/functions/percentrank.exc-function) | Excel 2010 | Get percentile rank, exclusive | array x significance |
| [PERCENTRANK.INC](https://exceljet.net/functions/percentrank.inc-function) | Excel 2010 | Get percentile rank, inclusive | array x significance |
| [PERMUT](https://exceljet.net/functions/permut-function) | Excel 2003 | Get number of permutations without repetitions | number number\_chosen |
| [PERMUTATIONA](https://exceljet.net/functions/permutationa-function) | Excel 2013 | Get number of permutations with repetitions | number number\_chosen |
| [PHI](https://exceljet.net/functions/phi-function) | Excel 2013 | Get value of the density function for standard normal distribution | x   |
| [PROB](https://exceljet.net/functions/prob-function) | Excel 2003 | Calculate the probability that values in a range fall within specified limits. | x\_range prob\_range lower\_limit upper\_limit |
| [QUARTILE](https://exceljet.net/functions/quartile-function) | Excel 2003 | Get the quartile in a data set | array quart |
| [QUARTILE.EXC](https://exceljet.net/functions/quartile.exc-function) | Excel 2010 | Get the quartile in a data set | array quart |
| [QUARTILE.INC](https://exceljet.net/functions/quartile.inc-function) | Excel 2010 | Get the quartile in a data set | array quart |
| [RANK](https://exceljet.net/functions/rank-function) | Excel 2003 | Rank a number against a range of numbers | number ref order |
| [RANK.AVG](https://exceljet.net/functions/rank.avg-function) | Excel 2010 | Rank a number against a range of numbers | number ref order |
| [RANK.EQ](https://exceljet.net/functions/rank.eq-function) | Excel 2010 | Rank a number against a range of numbers | number ref order |
| [SKEW](https://exceljet.net/functions/skew-function) | Excel 2003 | Get skewness of a distribution | number1 number2 ... |
| [SKEW.P](https://exceljet.net/functions/skew.p-function) | Excel 2013 | Get skewness of a distribution based on population | number1 number2 ... |
| [SLOPE](https://exceljet.net/functions/slope-function) | Excel 2003 | Get slope of linear regression line | known\_ys known\_xs |
| [SMALL](https://exceljet.net/functions/small-function) | Excel 2003 | Get nth smallest value | array k |
| [STANDARDIZE](https://exceljet.net/functions/standardize-function) | Excel 2003 | Calculate a normalized value (z-score) | x mean standard\_dev |
| [STDEV](https://exceljet.net/functions/stdev-function) | Excel 2003 | Get the standard deviation in a sample | number1 number2 ... |
| [STDEV.P](https://exceljet.net/functions/stdev.p-function) | Excel 2010 | Get standard deviation of population | number1 number2 ... |
| [STDEV.S](https://exceljet.net/functions/stdev.s-function) | Excel 2010 | Get the standard deviation in a sample | number1 number2 ... |
| [STDEVA](https://exceljet.net/functions/stdeva-function) | Excel 2003 | Get standard deviation in a sample | number1 number2 ... |
| [STDEVP](https://exceljet.net/functions/stdevp-function) | Excel 2003 | Get standard deviation of population | number1 number2 ... |
| [STDEVPA](https://exceljet.net/functions/stdevpa-function) | Excel 2003 | Get standard deviation for a population | number1 number2 ... |
| [TRIMMEAN](https://exceljet.net/functions/trimmean-function) | Excel 2003 | Calculate mean excluding outliers | array percent |
| [VAR](https://exceljet.net/functions/var-function) | Excel 2003 | Get variation of a sample | number1 number2 ... |
| [VAR.P](https://exceljet.net/functions/var.p-function) | Excel 2010 | Get variation of population | number1 number2 ... |
| [VAR.S](https://exceljet.net/functions/var.s-function) | Excel 2010 | Get variation of a sample | number1 number2 ... |
| [VARA](https://exceljet.net/functions/vara-function) | Excel 2003 | Get variation of a sample | number1 number2 ... |
| [VARP](https://exceljet.net/functions/varp-function) | Excel 2003 | Get variation of a population | number1 number2 ... |
| [VARPA](https://exceljet.net/functions/varpa-function) | Excel 2003 | Get variation of a population | number1 number2 ... |
| [WEIBULL](https://exceljet.net/functions/weibull-function) | Excel 2003 | Get the PDF or CDF of the Weibull distribution. | x alpha beta cumulative |
| [WEIBULL.DIST](https://exceljet.net/functions/weibull.dist-function) | Excel 2010 | Get the PDF or CDF of the Weibull distribution. | x alpha beta cumulative |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Web)
Web
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [ENCODEURL](https://exceljet.net/functions/encodeurl-function) | Excel 2013 | Get URL-encoded string | text |
| [FILTERXML](https://exceljet.net/functions/filterxml-function) | Excel 2013 | Get data from XML with Xpath | xml xpath |
| [WEBSERVICE](https://exceljet.net/functions/webservice-function) | Excel 2013 | Get data from a web service | url |

|     |     |     |     |
| --- | --- | --- | --- |[#](https://exceljet.net/functions#Database)
Database
| Function | Version | Purpose | Arguments |
| --- | --- | --- | --- |
| [DAVERAGE](https://exceljet.net/functions/daverage-function) | Excel 2003 | Get average from matching records | database field criteria |
| [DCOUNT](https://exceljet.net/functions/dcount-function) | Excel 2003 | Count matching records in a database | database field criteria |
| [DCOUNTA](https://exceljet.net/functions/dcounta-function) | Excel 2003 | Count matching records in a database | database field criteria |
| [DGET](https://exceljet.net/functions/dget-function) | Excel 2003 | Get value from matching record | database field criteria |
| [DMAX](https://exceljet.net/functions/dmax-function) | Excel 2003 | Get max from matching records | database field criteria |
| [DMIN](https://exceljet.net/functions/dmin-function) | Excel 2003 | Get min from matching records | database field criteria |
| [DPRODUCT](https://exceljet.net/functions/dproduct-function) | Excel 2003 | Get product from matching records | database field criteria |
| [DSTDEV](https://exceljet.net/functions/dstdev-function) | Excel 2003 | Get standard deviation of sample in matching records | database field criteria |
| [DSTDEVP](https://exceljet.net/functions/dstdevp-function) | Excel 2003 | Get standard deviation of population in matching records | database field criteria |
| [DSUM](https://exceljet.net/functions/dsum-function) | Excel 2003 | Get sum from matching records | database field criteria |
| [DVAR](https://exceljet.net/functions/dvar-function) | Excel 2003 | Get sample variance for matching records | database field criteria |
| [DVARP](https://exceljet.net/functions/dvarp-function) | Excel 2003 | Get population variance for matching records | database field criteria |

[Back to Top](https://exceljet.net/functions#skip-link)

[![Cover art for 101 Excel Functions You Should Know](https://exceljet.net/sites/default/files/images/blocks/101-excel-functions.webp)](https://exceljet.net/resources/101-excel-functions-pdf)

Download 100+ Important Excel Functions
---------------------------------------

[Get PDF Guide](https://exceljet.net/resources/101-excel-functions-pdf)

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)