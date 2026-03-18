# Power Query: Powerless Pivot

**Source:** https://sumproduct.com/blog/power-query-powerless-pivot/

---

[Home](https://sumproduct.com/)

\> Power Query: Powerless Pivot

*   December 19, 2017

Power Query: Powerless Pivot
============================

Power Query: Powerless Pivot
============================

20 December 2017

_Welcome to our Power Query blog. This week I look at PivotTables._

Back in [Power Query: Relationship Goals](https://sumproduct.com/blog/power-query-relationship-goals/)
, I focused on how well Power Query and Power Pivot work together. Power Query is not exclusive to Power Pivot though, as it may be used with ordinary PivotTables. There is a good reason for doing this too, which I will reveal at the end. Talk about cliff-hangers, eh?

I start with data that I have copied (not uploaded using Power Query) from my **_Items_** table, just to provide some typical data that I might like to put in a PivotTable.

![](<Base64-Image-Removed>)

All the data has been copied and pasted so that there are no formulae. From another blank workbook, I use Power Query to connect to this workbook. In my new workbook, on the ‘Data’ tab I choose ‘New Query’ and select ‘From File’ and then ‘From Workbook’ on the dropdown.

![](<Base64-Image-Removed>)

I select my original workbook.

![](<Base64-Image-Removed>)

I don’t want to load my data, I just want to make a connection to it, so I choose the ‘Load To’ option.

![](<Base64-Image-Removed>)

I choose ‘Only Create Connection’ – I want the connection to be available when I create my PivotTable, but I don’t need to load the data to the workbook. To create the PivotTable, I go to the ‘Insert’ tab and in the ‘Tables’ section I choose ‘PivotTable’:

![](<Base64-Image-Removed>)

I select the ‘Use an external data source’ option and choose my connection.

![](<Base64-Image-Removed>)

My connection is at the top ‘Query – Sheet1’, so I open this, and create a simple PivotTable as shown below.

![](<Base64-Image-Removed>)

So, what is the advantage of using Power Query? Well, for today’s example, my data file was huge – over a million rows. This is how each step has been stored:

*   step 1 is the data in the workbook
*   step 2 is my connection only query and the data shown as a PivotTable.

![](<Base64-Image-Removed>)

So using Power Query is one way to reduce the size of the PivotTable workbook. There are other ways, but Power Query will also allow me to clean and transform my data prior to creating my PivotTable.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-powerless-pivot/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-powerless-pivot/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-powerless-pivot/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-powerless-pivot/#0)

[](https://sumproduct.com/blog/power-query-powerless-pivot/#0 "close")

top