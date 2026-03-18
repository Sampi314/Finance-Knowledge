# Power Pivot Principles: Generating a List of Measure Descriptions

**Source:** https://sumproduct.com/blog/power-pivot-principles-generating-a-list-of-measure-descriptions/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Generating a List of Measure Descriptions

*   December 13, 2021

Power Pivot Principles: Generating a List of Measure Descriptions
=================================================================

Power Pivot Principles: Generating a List of Measure Descriptions
=================================================================

14 December 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll talk about how to generate a list of measure or column descriptions using DMV queries._

Sometimes, you may have a long list of complex measures with some descriptions and want to generate that list to easily refer to when you need. Measure descriptions are not obviously visible as you need to go into each measure’s Edit window or ‘Measure Description’ window within Power Pivot to check.

In this example, I randomly created a Sales table for a year as a source to pull into Power Pivot, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-96.jpg)

To see a measure description, we need to access the ‘Manage Measures’ window. To do this, go to **Power Pivot tab -> Measures -> Manage Measures…**

![](https://sumproduct.com/wp-content/uploads/2025/05/b6eec1a4a079fff23b8f21b62aff5df0-5.jpg)

For example, I have a simple measure called **Total Sales** below. In order to see the description, you need to select it and click Edit.

![](https://sumproduct.com/wp-content/uploads/2025/05/d57efd7322982f2ff72cf19ec5ea62c3-4.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/86fbab870c293f438ecf9c26e1368380-5.jpg)

If you have more than 10 measures, it is very time consuming to click into every single measure to see their descriptions or just simply copy DAX formulae. Instead, we will show you a trick to access the whole list of measure details. This feature is hidden so we need to follow the steps below to trigger it. We assume that you have already had at least a table and a measure in Power Pivot.

Firstly, go to **Data -> Existing Connections -> Tables tab** and double-click on one of the tables under your workbook name with a table symbol at the front (not the one with ‘Data Model’ in the name).

![](https://sumproduct.com/wp-content/uploads/2025/05/f0ca9f16442052b9b099c942d1c60283-2.jpg)

This ‘Import Data’ dialog will appear. Select ‘New worksheet’ and then click ‘OK’.

![](<Base64-Image-Removed>)

A table from Power Pivot will be put on a new sheet as below. Then, right-click on a cell within the new table and go to **Table -> Edit DAX…**

![](<Base64-Image-Removed>)

The following ‘Edit DAX’ dialog will appear, where you should change ‘Command Type:’ to ‘DAX’.

![](<Base64-Image-Removed>)

Then, you are able to enter any [DMV](https://docs.microsoft.com/en-us/analysis-services/instances/use-dynamic-management-views-dmvs-to-monitor-analysis-services?view=asallproducts-allversions)
 query into the Expression box to ask it to generate the data that you want. DMV query syntax is similar to a SQL SELECT statement.

So as to generate a list of measure details, please use the query below.

SELECT

measure\_name, \[description\], expression

FROM $system.mdschema\_measures

WHERE measure\_aggregator = 0

Your new table will change into a measure table as follows. You can now see both measure descriptions and DAX formulas under the same table.

![](<Base64-Image-Removed>)

If you create a new measure, the table above will be updated automatically. For example, I created a test measure below.

![](<Base64-Image-Removed>)

After you click ‘OK’, the measure table will be updated as below.

![](<Base64-Image-Removed>)

Similar to DAX measures, you can also generate a table including descriptions of all columns in Power Pivot using the DMV query below.

SELECT

hierarchy\_name as \[Column Name\], \[description\]

FROM $system.mdschema\_hierarchies

WHERE cube\_name=’model’

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-generating-a-list-of-measure-descriptions/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-generating-a-list-of-measure-descriptions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-generating-a-list-of-measure-descriptions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-generating-a-list-of-measure-descriptions/#0)

[](https://sumproduct.com/blog/power-pivot-principles-generating-a-list-of-measure-descriptions/#0 "close")

top