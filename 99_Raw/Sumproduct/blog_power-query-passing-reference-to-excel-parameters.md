# Power Query: Passing (Reference to) Excel Parameters

**Source:** https://sumproduct.com/blog/power-query-passing-reference-to-excel-parameters/

---

[Home](https://sumproduct.com/)

\> Power Query: Passing (Reference to) Excel Parameters

*   February 27, 2018

Power Query: Passing (Reference to) Excel Parameters
====================================================

Power Query: Passing (Reference to) Excel Parameters
====================================================

28 February 2018

_Welcome to our Power Query blog. This week, I take a look at how to pass Excel data as a parameter in Power Query._

I am going to look at a simple scenario where I use a parameter in Power Query which is populated from a cell in my Excel workbook.

Below, I have a spreadsheet with charge data pertaining to items in my fictitious inventory:

![](<Base64-Image-Removed>)

My plan is to create a query from ‘Charges’ data, and pass a parameter from the ‘Items’ sheet.

![](<Base64-Image-Removed>)

I am not claiming that this is the most efficient approach for this particular scenario, but it will serve to show the method!

I create the parameter first, so that it is ready to add to my main ‘Charges’ query. Since my cell is already in a table of items data, trying to create a new query from the ‘Data’ tab by choosing ‘From Table’ in the ‘Get and Transform’ section will assume I want the whole table. I can circumvent this issue by using the method I used in [Power Query: Returning to Referencing Ranges](https://sumproduct.com/blog/power-query-returning-to-referencing-ranges/)
. If I give my prospective parameter a range name, then I can locate it easily in my workbook. I name my cell ‘Parameter\_Range’ and create a new blank workbook from the ‘Other sources’ option of the ‘New Query’ dropdown, _viz._

![](<Base64-Image-Removed>)

In my new blank query, I enter the following **M** function:

**Excel.CurrentWorkbook(){\[Name=”Parameter\_Range”\]}\[Content\]{0}\[Column1\]**

which will extract the value from the cell. I rename my new query ‘**Item\_Parameter**‘ and save it as a ‘Connection Only’ query.

![](<Base64-Image-Removed>)

Now I need to create a query on ‘Charges’ which will select charges that match a particular item. I will do this using the GUI options available. I create a new query ‘From Table’ whilst in my ‘Charges’ sheet:

![](<Base64-Image-Removed>)

I can then choose to filter on **_Description_**:

![](<Base64-Image-Removed>)

It doesn’t matter which description I pick at this stage – I am simply getting Power Query to create the step for me.

![](<Base64-Image-Removed>)

Now I have the step, instead of picking those charges that are pertaining to ’10 x 4 metre marquee’ I want to use my parameter instead. If I expand the ‘Queries’ pane to the left of the screen, I can make sure I have the correct name.

![](<Base64-Image-Removed>)

I then select the tick icon (left of the formula bar) to change the step to use my parameter.

![](<Base64-Image-Removed>)

The correct data is shown. I can update the parameter (by changing the cell or editing the named range) in my Excel worksheet and refresh the query to change the data that is selected. I try this by changing ‘**Item\_Parameter**‘ to point at the next item description.

![](<Base64-Image-Removed>)

Before I refresh my query, the original data appears:

![](<Base64-Image-Removed>)

Once I refresh my query, the new parameter value is used.

![](<Base64-Image-Removed>)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-passing-reference-to-excel-parameters/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-passing-reference-to-excel-parameters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-passing-reference-to-excel-parameters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-passing-reference-to-excel-parameters/#0)

[](https://sumproduct.com/blog/power-query-passing-reference-to-excel-parameters/#0 "close")

top