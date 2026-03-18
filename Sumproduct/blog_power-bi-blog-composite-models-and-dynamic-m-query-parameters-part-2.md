# Power BI Blog: Composite Models and Dynamic M Query Parameters Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Composite Models and Dynamic M Query Parameters Part 2

*   August 17, 2022

Power BI Blog: Composite Models and Dynamic M Query Parameters Part 2
=====================================================================

Power BI Blog: Composite Models and Dynamic M Query Parameters Part 2
=====================================================================

18 August 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we link the **M** parameters to tables and reference them in a slicer._

Microsoft have added support recently for Power BI datasets added that have Dynamic **M** Query Parameters defined. Now, we may create a composite model on such datasets to enrich or extend them. With Dynamic **M** Query Parameters, we can let report viewers use filters or slicers to set values for an **M** query parameter.

[Last time](https://www.sumproduct.com/blog/article/power-bi-tips/composite-models-and-dynamic-m-query-parameters-part-1)
, we created parameters and amended an **M** query to reference the parameters:

![](<Base64-Image-Removed>)

This week, we will create a table with a column that provides the possible values available for that parameter. This will allow the parameters to be dynamically set based on filter selection. In this example, we want our **StartTime** parameter and **EndTime** parameter to be dynamic. Since these parameters require a Date/Time parameter, we want to generate date inputs that may be used to set the date for the parameter. We start by creating a new table in Power BI:

![](<Base64-Image-Removed>)

Here’s the **DAX** to create the first table for the values for **StartTime** parameter:

**StartDateTable  
\= CALENDAR (DATE(2016,1,1), DATE(2016,12,31))**

![](<Base64-Image-Removed>)

This is the **DAX** for the second table created for the values for **EndTime** parameter:

**EndDateTable  
\= CALENDAR (DATE(2016,1,1), DATE(2016,12,31))**

![](<Base64-Image-Removed>)

We use a different column name that is not in a table. Otherwise, if names are duplicated, the selected value will be applied as a filter to the query.

Now that the tables with the **Date** field have been created, we can bind each field to a parameter. Binding the field to a parameter essentially means that as the selected value for the field changes, the value will get passed to the parameter and update the query where the parameter is referenced. Therefore, to bind field, we go to the Modeling _(sic)_ tab, select the newly created field, and then go to the Advanced properties (noting that the column ‘Data Type’ should match with the **M** parameter type):

![](<Base64-Image-Removed>)

We select the dropdown under ‘Bind to parameter’ and select the parameter that we want to bind to the field:

![](<Base64-Image-Removed>)

Since this example is for a single-select value (setting the parameter to a single value), we want to keep Multi-select set to No, which is the default:

![](<Base64-Image-Removed>)

If we were creating an example that required multi-selection (passing multi-values to a single parameter), then we would toggle the switch to Yes and ensure that our **M** query was set up properly to accept multiple values in the **M** query. Here’s an example for **RepoNameParameter**, which allows for multiple values:

![](<Base64-Image-Removed>)

We repeat these steps for other fields to bind to other parameters:

![](<Base64-Image-Removed>)

Finally, we can reference this field in a slicer or as a filter:

![](<Base64-Image-Removed>)

If the mapped column is set to No for Multi-select, we either use a single select mode in the slicer or use a single select in the Filter card.

There are additional steps if we want end users to be able to use the ‘Select all’ option in the Slicer or Filter card, which we will look at next time.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-2/#0 "close")

top