# Power Query: Workbook Parameter Table Example Part 2

**Source:** https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Workbook Parameter Table Example Part 2

*   October 8, 2025

Power Query: Workbook Parameter Table Example Part 2
====================================================

_Welcome to our Power Query blog.  This week, I continue with the example by importing a large dataset and preparing it for filtering._

During training, attendees often ask how to use parameters to make their Power Query reports more flexible.  I recently looked at this in two \[2\] blog collections: [Workbook Parameter Tip](https://sumproduct.com/uncategorized/power-query-workbook-parameter-tip/)
 and [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
.  My fictional salespeople can take some well-earned leave since I will be applying the same method to a much larger dataset.  I will show how I can quickly create the same Parameters query in a new workbook and use it to access specific information.  I will be using car data I have extracted from the Kaggle website.  There are 241,205 rows.

![](https://sumproduct.com/wp-content/uploads/2025/10/image-21.png)

Some of the filters required have been entered on the Outputs sheet:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-22.png)

[Last time](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/)
, I converted this into the Table I need for the **fnGetParameter** method I used in the [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
 series.

![](https://sumproduct.com/wp-content/uploads/2025/10/image-23.png)

I copied the function from the workbook I used in the [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
 series to the current workbook.

![](https://sumproduct.com/wp-content/uploads/2025/10/image-24.png)

I am now ready to import the car sales data.  I select any single cell in the **Car\_Sales** Table, and right-click to ‘Get Data from Table/Range’.  This extracts the data to a query called **Car\_Sales**:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-25.png)

Note the green dots at the top of the query.  Since I have a large amount of data, each step will take some time to process.  I can create a subset of my query by choosing to keep the top 100 rows.  This will allow me to create the other steps more quickly.  I will remove this subset step at the end.  Before I do this, I remove the ‘Changed Type’ step, as it is currently analysing the first 1,000 rows to check the type (hence the green dots).  I can apply this step in a moment when I have less rows to deal with.  In the Home tab, I select ‘Reduce Rows’:

![](<Base64-Image-Removed>)

I choose to ‘Keep Rows’ and then to ‘Keep Top Rows’.  I could have chosen to keep the bottom rows or a range of rows if that gave me a more representative subset of the data, but this option works well for the car sales data.  A dialog appears, allowing me to specify how many rows I wish to keep:

![](<Base64-Image-Removed>)

Having chosen 100 rows, I click OK.  The dataset is now much easier to deal with.

![](<Base64-Image-Removed>)

Since I will be filtering my data using the **fnGetParameter** function, I need the correct data types for the columns, particularly the **Date** column.  If I try to compare type ‘Any’ with a date parameter, I will get errors.  I select all columns by clicking in any column heading and using **CTRL** + **A**.  On the Transform tab, I choose ‘Detect Data Type’:

![](<Base64-Image-Removed>)

The data is ready for the filters to be applied.

![](<Base64-Image-Removed>)

Next time, I will filter the data by creating placeholders before replacing these with the parameters.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/#0)

[](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/#0 "close")

top