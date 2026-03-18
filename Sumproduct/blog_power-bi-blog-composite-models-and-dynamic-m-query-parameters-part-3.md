# Power BI Blog: Composite Models and Dynamic M Query Parameters Part 3

**Source:** https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-3/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Composite Models and Dynamic M Query Parameters Part 3

*   August 24, 2022

Power BI Blog: Composite Models and Dynamic M Query Parameters Part 3
=====================================================================

Power BI Blog: Composite Models and Dynamic M Query Parameters Part 3
=====================================================================

25 August 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we conclude our series by looking at how to use a ‘Select all’ option in the slicer referencing **M** parameters._

Microsoft have added support recently for Power BI datasets added that have Dynamic **M** Query Parameters defined. Now, we may create a composite model on such datasets to enrich or extend them. With Dynamic **M** Query Parameters, we can let report viewers use filters or slicers to set values for an **M** query parameter.

[In Part 1](https://www.sumproduct.com/blog/article/power-bi-tips/composite-models-and-dynamic-m-query-parameters-part-1)
, we created parameters and amended an **M** query to reference the parameters:

![](<Base64-Image-Removed>)

[Last time](https://www.sumproduct.com/blog/article/power-bi-tips/composite-models-and-dynamic-m-query-parameters-part-2)
, we created a new table for each parameter, linked them up and referenced them in a slicer:

![](<Base64-Image-Removed>)

There are additional steps if we want end users to be able to use the ‘Select all’ option in the Slicer or Filter card, which we will look at this week.

Consider the following scenario. Within the Model tab of Power BI Desktop, let’s have a field called **Country** (list of countries) that is bound to an **M** parameter called **countryNameMParameter**:

![](<Base64-Image-Removed>)

Notice that this parameter is enabled for Multi-select but not enabled for ‘Select all’. When we enable the ‘Select all’ toggle, we’ll see an enabled input called ‘Select all’ value:

![](<Base64-Image-Removed>)

The ‘Select all’ value is used to refer to the ‘Select all’ option in the **M** query. This value is passed to parameter as a list that contains the value we defined for ‘Select all’. Therefore, when we are defining this value or using the default value, we need to make sure that this value is unique and does not exist in the field bound to the parameter. Once we have set the value or used the default value for ‘Select all’, we need to update the **M** query to account for this ‘Select all’ value.

![](<Base64-Image-Removed>)

To edit the **M** query, we launch the Power Query Editor using the ‘Transform Data’ button on the Home tab, and then select ‘Advanced Editor’ in the Query section:

![](<Base64-Image-Removed>)

In the Advanced Editor, we need to add a Boolean expression that will evaluate to TRUE if the parameter is enabled for Multi-select and contains the ‘Select all’ value (else return FALSE). For our example that would look like this:

![](<Base64-Image-Removed>)

Next, we will need to incorporate the result of this ‘Select all’ Boolean expression into the source query. For our example, we have a Boolean query parameter in the source query called **includeAllCountries** that is set to the result of the Boolean expression from the previous step. We then use this parameter in a filter clause in the query, such that FALSE for the Boolean will filter to the selected country name(s) and a TRUE would effectively apply no filter:

![](<Base64-Image-Removed>)

For reference here is the full query employed:

**let**

    **selectedcountryNames = if  
Type.Is(Value.Type(countryNameMParameter), List.Type) then**

      **Text.Combine({“‘”,  
Text.Combine(countryNameMParameter, “‘,'”) , “‘”})**

    **else**

      **Text.Combine({“‘”  
, countryNameMParameter , “‘”}),**

    **selectAllCountries = if  
Type.Is(Value.Type(countryNameMParameter), List.Type) then**

     **List.Contains(countryNameMParameter, “\_\_SelectAll\_\_”)**

    **else**

      **false,**

    **KustoParametersDeclareQuery =  
Text.Combine({“declare query\_parameters(“,**

                                 **“startTimep:datetime = datetime(“,  
DateTime.ToText(StartTimeMParameter, “yyyy-MM-dd hh:mm”), “),  
” ,**

                                **“endTimep:datetime = datetime(“,  
DateTime.ToText(EndTimeMParameter, “yyyy-MM-dd hh:mm:ss”), “),  
“,**  

                                 **“includeAllCountries:  
bool = “, Logical.ToText(selectAllCountries) ,”,”,**

                                **“countryNames: dynamic = dynamic(\[“, selectedcountryNames,  \
“\]));” }),**

   **ActualQueryWithKustoParameters  
\=**

                                **“Covid19**

                                **|  
where includeAllCountries or Country in(countryNames)**

                                **|  
where Timestamp > startTimep and Timestamp < endTimep**

                                **|  
summarize sum(Confirmed) by Country, bin(Timestamp, 30d)”,**

    **finalQuery =  
Text.Combine({KustoParametersDeclareQuery, ActualQueryWithKustoParameters}),**

    **Source =  
AzureDataExplorer.Contents(“help”, “samples”, finalQuery,  
\[MaxRows=null, MaxSize=null, NoTruncate=null, AdditionalSetStatements=null\]),**

    **#”Renamed Columns” =  
Table.RenameColumns(Source,{{“Timestamp”, “Date”},  
{“sum\_Confirmed”, “Confirmed Cases”}})**

**in**

    **#”Renamed Columns”**

Once we have updated the **M** query to account for this new ‘Select all’ value, we can use the ‘Select all’ function in slicers or filters:

![](<Base64-Image-Removed>)

When we allow report readers to dynamically set the values for the **M** query parameters, they may be able to access additional data or trigger modifications to the source system using injection attacks, depending upon how the parameters are referenced in the **M** query and what values are passed to that parameter.

For example, let’s say we have a parameterised query **Products**:

**Products**

**| where Category == \[Parameter inserted here\] & HasReleased == ‘True’**

 **| project ReleaseDate, Name,  
Category, Region“\`**

We may have no issues with a friendly user who passes an appropriate value for the parameter, for example, _Games_:

**| where Category == ‘Games’ & HasReleased == ‘True’**

However, an attacker may be able to pass a value that modifies the query to get access to more data, for example, _‘Games’ //_:

**Products**

**| where Category == ‘Games’// & HasReleased == ‘True’**

**| project ReleaseDate, Name, Category, Region**

In this example, the attacker can get access to information on games that have not been released yet by changing part of the query into a comment.

To mitigate the security risk, it’s best to avoid string concatenation of **M** parameter values within the query. Instead, consume those parameter values in **M** operations that fold to the source query, so that the **M** engine and connector construct the final query. Alternatively, if available, make use of a parameter passing mechanism built-in to the source query language and connectors. For example, Azure Data Explorer has built-in query parameter capabilities that are designed to protect against injection attacks.

As examples:

*   Example using **M** query’s filtering operations:

**Table.SelectRows(Source, (r) =&gt; r\[Columns\]  
\= Parameter)**

*   Example declaring the parameter in the source query (or passing the parameter value as an input to a source query function):

**declare query\_parameters (Name of Parameter : Type  
of Parameter);**

There are some considerations and limitations to consider when using dynamic **M** query parameters:

*   a single parameter cannot be bound to multiple fields nor vice-versa
*   aggregations are not supported with the feature
*   Row Level Security (RLS) is not supported with the feature
*   parameter names cannot be reserved words in **DAX** nor contain spaces. Appending ‘Parameter to the end of the parameter name can help avoid this limitation

if the parameter is Date/Time data type, cast it within the **M** query as

**DateTime.Date(<YourDateParameter>)**

*   if using **SQL** sources, there is a confirmation dialog every time the parameter value changes. This is due to a security setting: ‘Require user approval for new native database queries’. This setting can be switched off in the Security tab of the Options dialog in Power BI Desktop
*   the following are unsupported out-of-box parameter types:

o Any

o Duration

o True/False

o Binary

*   unsupported filters:

o Relative time slicer or filter

o Relative date

o Hierarchy slicer

o Multi-field include filter

o Exclude filter / Not filters

o Cross-highlighting

o Drill-down filter

o Cross drill filter

o Top **N** filter

*   Unsupported operations:

o And

o Contains

o Less than

o Greater than

o Starts with

o Does not start with

o Is not

o Does not contain

o Is blank

o Is not blank.

This concludes our series on composite models and dynamic **M** parameters.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-3/#0)

[](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-3/#0 "close")

top