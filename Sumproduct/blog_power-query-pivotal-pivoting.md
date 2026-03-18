# Power Query: Pivotal Pivoting

**Source:** https://sumproduct.com/blog/power-query-pivotal-pivoting/

---

[Home](https://sumproduct.com/)

\> Power Query: Pivotal Pivoting

*   August 15, 2017

Power Query: Pivotal Pivoting
=============================

Power Query: Pivotal Pivoting
=============================

16 August 2017

_Welcome to our Power Query blog. Today I look at pivoting a column._

Power Query’s ability to efficiently transform data is amply demonstrated by features which allow me to pivot (and unpivot) data at the touch of a button. I begin as usual with my data in an Excel worksheet.

![](<Base64-Image-Removed>)

In the ‘POWER QUERY’ tab, in the ‘Excel Data’ section, I choose to extract my data ‘From Table/Range’:

![](<Base64-Image-Removed>)

My data appears in a new query, which I have called ‘Pivot Column’. In the ‘Transform’ tab, there is a section which groups together the transformations which can be applied to ‘Any Column’. I am interested in the ‘Pivot Column’ option.

![](<Base64-Image-Removed>)

‘Pivot Column’ is available as long as I haven’t selected multiple columns. I can either select a column before using ‘Pivot Column’ or it will assume I want to use the first column in my query. I select **_expense code_**.

![](<Base64-Image-Removed>)

The ‘Pivot Column’ feature will remove my selected column and add columns to my table that contain an aggregate value for each unique value in that column. This is quite a concept to describe in one sentence, and it best demonstrated by an example!

I have provided the names of the column (**_expense code_**), but I also need to specify what data will be aggregated, and the function associated with the aggregation. The data column will also be removed from my query when the new columns are added. I will be using the **_amount_** column as my data, which I have decided to sum _viz._

![](<Base64-Image-Removed>)

As soon as I pick **_amount,_** power query recognises that I have chosen datatype currency, and defaults to ‘Sum’. The other options for my datatype are shown above. If I had chosen a text column, then the options would be different, as shown below:

![](<Base64-Image-Removed>)

Returning to my **_amount_** column, there is also an option ‘Don’t Aggregate’. This would return a grid which only has values when that particular expense code is populated, as shown below:

![](<Base64-Image-Removed>)

It didn’t work too well when I had two consecutive food amounts, but the other amounts are shown. I am more interested to try aggregating by using the ‘Sum’ option, so I delete this step and return to my ‘Pivot Column’ screen and try again…

![](<Base64-Image-Removed>)

This time my data is all populated as expected. I have already reordered my columns so that I can see who incurred what expense and on what date and I can tidy it up further by removing the nulls by using the ‘Replace Values’ facility.

Having demonstrated how easy it is to pivot columns, another nice feature to show is how easy it is to unpivot them again. If I select my new columns and choose to ‘Unpivot’ them using the option from within the ‘Any Column’ section in the ‘Transform’ tab, I get this:

![](<Base64-Image-Removed>)

My expense code (**Attribute**) and my amount (**Value**) have been reinstated!

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-pivotal-pivoting/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-pivotal-pivoting/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-pivotal-pivoting/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-pivotal-pivoting/#0)

[](https://sumproduct.com/blog/power-query-pivotal-pivoting/#0 "close")

top