# Power BI Blog: Select All Operation Now Supported for Dynamic M Query Parameters

**Source:** https://sumproduct.com/blog/power-bi-blog-select-all-operation-now-supported-for-dynamic-m-query-parameters/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Select All Operation Now Supported for Dynamic M Query Parameters

*   July 7, 2021

Power BI Blog: Select All Operation Now Supported for Dynamic M Query Parameters
================================================================================

Power BI Blog: Select All Operation Now Supported for Dynamic M Query Parameters
================================================================================

8 July 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we will look at the ‘Select all’ Preview feature._

As a general rule, we don’t tend to go through Preview features in this [blog series](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
 – but we thought this one might be the exception that proves the rule.

Back in October last year, Microsoft released a Preview of Dynamic **M** Query Parameters that allowed report viewers to use filters or slicers to set the value(s) for an **M** Query Parameter, which can be especially useful for query performance optimisations. Previously, Dynamic **M** Query Parameters did not support the ‘Select all’ operation, requiring end-users to individually select each value if they wanted to see the data for all values. Now, in this release, support has finally been added for the ‘Select all’ operation, so that with a single-click users may select all values for the query parameter.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-167.jpg)

As a prerequisite, you’ll need to enable and setup Dynamic **M** Query Parameters. Once you have the feature enabled and setup a Dynamic **M** Query Parameter, you may now begin the setup process to support ‘Select all’.

For example, within the Model tab of Power BI Desktop, imagine you have a field called Country (list of countries) that is bound to an **M** parameter called c**ountryNameMParameter**:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-220.jpg)

You’ll also notice that this parameter is enabled for Multi-select but not enabled for ‘Select all’. When you enable the ‘Select all’ toggle, you will then see an enabled input called ‘Select all value’:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-178.jpg)

The Select all value (which defaults to ‘\_\_SelectAll\_\_’) is used to refer to the ‘Select all’ option in the **M** Query. This value is passed to parameter as a list that contains the value you defined for ‘Select all’. Therefore, when you are defining this value or using the default value, you will need to make sure that this value is unique and does not exist in the field bound to the parameter.

Once you have set the value or used the default value for ‘Select all’, you will then need to update the **M** Query to account for this ‘Select all’ value.

![](<Base64-Image-Removed>)

To edit the **M** Query, you will need first launch the Power Query Editor and then select the Advanced Editor in the Query section:

![](<Base64-Image-Removed>)

In the Advanced Editor, you will need to add a Boolean expression that will evaluate to TRUE if the parameter is enabled for Multi-select and contains the ‘Select all’ value (else return FALSE). For our example, that would look like this:

![](<Base64-Image-Removed>)

Next, you will need to incorporate the result of this ‘Select all’ Boolean expression into the source query. For our example, there is a Boolean query parameter in the source query called ‘includeAllCountries’ that is set to the result of the Boolean expression from the previous step. You may then use this parameter in a filter clause in the query, such that FALSE for the Boolean will filter to the selected country name(s) and TRUE would effectively apply no filter:

![](<Base64-Image-Removed>)

For reference, here is the full query used in this example:

**let**

**selectedcountryNames = if Type.Is(Value.Type(countryNameMParameter), List.Type) then**

**Text.Combine({“‘”, Text.Combine(countryNameMParameter, “‘,'”) , “‘”})**

**else**

**Text.Combine({“‘” , countryNameMParameter , “‘”}),**

**selectAllCountries = if Type.Is(Value.Type(countryNameMParameter), List.Type) then**

**List.Contains(countryNameMParameter, “\_\_SelectAll\_\_”)**

**else**

**false,**

**KustoParametersDeclareQuery = Text.Combine({“declare query\_parameters(“,**

**“startTimep:datetime = datetime(“, DateTime.ToText(StartTimeMParameter, “yyyy-MM-dd hh:mm”), “), ” ,**

**“endTimep:datetime = datetime(“, DateTime.ToText(EndTimeMParameter, “yyyy-MM-dd hh:mm:ss”), “), “,**

**“includeAllCountries: bool = “, Logical.ToText(selectAllCountries) ,”,”,**

**“countryNames: dynamic = dynamic(\[“, selectedcountryNames, “\]));” }),**

**ActualQueryWithKustoParameters =**

**“Covid19**

**| where includeAllCountries or Country in(countryNames)**

**| where Timestamp > startTimep and Timestamp < endTimep**

**| summarize sum(Confirmed) by Country, bin(Timestamp, 30d)”,**

**finalQuery = Text.Combine({KustoParametersDeclareQuery, ActualQueryWithKustoParameters}),**

**Source = AzureDataExplorer.Contents(“help”, “samples”, finalQuery, \[MaxRows=null, MaxSize=null, NoTruncate=null, AdditionalSetStatements=null\]),**

**#”Renamed Columns” = Table.RenameColumns(Source,{{“Timestamp”, “Date”}, {“sum\_Confirmed”, “Confirmed Cases”}})**

**in**

**#”Renamed Columns”**

Once you have updated your **M** Query to account for this new ‘Select all’ value, you can now use the ‘Select all’ function in slicers or filters:

![](<Base64-Image-Removed>)

Note that Dynamic **M** Query parameters do not support ‘Exclude / Not in’ filters. Therefore, selecting a value after ‘Select all’ has been pressed will not deselect that value and produce an unsupported exclude filter. Instead, this scenario produces an Include / In filter for that selected value.

That’s it for this week!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-select-all-operation-now-supported-for-dynamic-m-query-parameters/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-select-all-operation-now-supported-for-dynamic-m-query-parameters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-select-all-operation-now-supported-for-dynamic-m-query-parameters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-select-all-operation-now-supported-for-dynamic-m-query-parameters/#0)

[](https://sumproduct.com/blog/power-bi-blog-select-all-operation-now-supported-for-dynamic-m-query-parameters/#0 "close")

top