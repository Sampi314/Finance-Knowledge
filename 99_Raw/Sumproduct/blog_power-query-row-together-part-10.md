# Power Query: Row Together Part 10

**Source:** https://sumproduct.com/blog/power-query-row-together-part-10/

---

[Home](https://sumproduct.com/)

\> Power Query: Row Together Part 10

*   August 27, 2025

Power Query: Row Together Part 10
=================================

_Welcome to our Power Query blog.  This week, I look at a new row challenge._

Over the last few weeks, I have been looking at row challenges.  This week, I am going to look at a new challenge.  To solve it, I will use a similar approach to [last week](https://sumproduct.com/blog/power-query-row-together-part-9)
.  I have itinerary data for my salespeople for next year.

![](https://sumproduct.com/wp-content/uploads/2025/08/image-50.png)

This time, I would like to take the row data and organise it into columns:

![](https://sumproduct.com/wp-content/uploads/2025/08/image-51.png)

I start by extracting the **Itinerary** Table into Power Query by right-clicking in the Table and choosing ‘Get Data from Table / Range’:

![](https://sumproduct.com/wp-content/uploads/2025/08/image-52.png)

I remove the ‘Changed Type’ step as I will be applying this at the end.  Then, I split the **Itinerary** column by delimiter by selecting it and selecting the appropriate option from the right-click menu:

![](https://sumproduct.com/wp-content/uploads/2025/08/image-53.png)

Note that the default option is not correct for this example:

![](https://sumproduct.com/wp-content/uploads/2025/08/image-54.png)

Since the first typical delimiter character the algorithms have come across is the forward slash (**/**), this has been identified as the appropriate place to split the data.  I change the custom option to a comma and a space (‘**,** ‘) and split the column:

![](https://sumproduct.com/wp-content/uploads/2025/08/image-55.png)

The column is split, and I have another ‘Changed Type’ step which I also delete.  You will recall from [last week](https://sumproduct.com/blog/power-query-row-together-part-9)
 that I should avoid using the column names in steps.  For this example, I have three \[3\] itinerary columns, but this could vary.  I used the same method I used to avoid naming the columns [last week](https://sumproduct.com/blog/power-query-row-together-part-9)
.  I select the **Salesperson** column, right-click and choose ‘Unpivot Other Columns’:

![](https://sumproduct.com/wp-content/uploads/2025/08/image-56.png)

I now have the itinerary data in two \[2\] columns:

![](<Base64-Image-Removed>)

I delete the **Attribute** column and split the **Value** column.  I need to consider not only the current data, but also future values.  If I split by a space (‘ ‘), then if I have location names with more than one word (for example ‘Milton Keynes’ ), I would encounter problems.  Since I expect the date to be in a consistent format, I split by the number of characters instead:

![](<Base64-Image-Removed>)

This splits the column correctly:

![](<Base64-Image-Removed>)

I remove the ‘Changed Type’ step as it only applies to the new columns and rename **Value.1** to **Date** and **Value.2** to **Location**.  I select all the columns and choose to ‘Detect Data Type’ from the Transform tab:

![](<Base64-Image-Removed>)

The query is now ready to be uploaded to the workbook:

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-row-together-part-10/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-row-together-part-10/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-row-together-part-10/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-row-together-part-10/#0)

[](https://sumproduct.com/blog/power-query-row-together-part-10/#0 "close")

top