# Power BI Blog: Composite Models and Dynamic M Query Parameters Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Composite Models and Dynamic M Query Parameters Part 1

*   August 10, 2022

Power BI Blog: Composite Models and Dynamic M Query Parameters Part 1
=====================================================================

Power BI Blog: Composite Models and Dynamic M Query Parameters Part 1
=====================================================================

11 August 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we create Dynamic **M** Query Parameters and reference them in an **M** query._

Microsoft have added support recently for Power BI datasets added that have Dynamic **M** Query Parameters defined. Now, we may create a composite model on such datasets to enrich or extend them. With Dynamic **M** Query Parameters, we can let report viewers use filters or slicers to set values for an **M** query parameter.

With Dynamic **M** Query Parameters, model developers can let report viewers use filters or slicers to set the value(s) for an **M** Query Parameter, which can be especially useful for query performance optimisations. With Dynamic **M** Query Parameters, model authors have more control over how filter selections get incorporated into DirectQuery source queries.

When builders understand the intended semantics of their filters, they often know how to write efficient queries against their data source, and can thus ensure filter selections get incorporated into source queries at the right point to achieve their intended results with improved performance.

As a prerequisite for this feature, we must have a valid **M** Query Parameter created and referred in one or more Direct Query tables.

**Example**

In Power BI Desktop, we select **Home -> Transform data- > Transform data** to open the Power Query Editor. Then, we select ‘New Parameters’ under the ‘Manage Parameters’ button in the Ribbon.

![](<Base64-Image-Removed>)

We fill out the following information about the parameter:

![](<Base64-Image-Removed>)

If we have more parameters to add, we can simply click ‘New’:

![](<Base64-Image-Removed>)

Once we’ve created our parameters, we can reference them in the **M** query. To modify the **M** query, we open the Advanced Editor, having selected the query that we want to modify:

![](<Base64-Image-Removed>)

Then, reference the parameters in the **M** query, highlighted in yellow _(below)_:

![](<Base64-Image-Removed>)

Now that we have created the parameters and referenced them in the **M** query, we need to create a table with a column that provides the possible values available for that parameter. This will allow it such that the parameters are dynamically set based on filter selection. In this example, we want our **StartTime** parameter and **EndTime** parameter to be dynamic. Since these parameters require a Date/Time parameter, we want to generate date inputs that may be used to set the date for the parameter.

That’s where we will pick this up next week.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-composite-models-and-dynamic-m-query-parameters-part-1/#0 "close")

top