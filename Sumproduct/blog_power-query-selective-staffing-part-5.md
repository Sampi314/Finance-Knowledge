# Power Query: Selective Staffing Part 5

**Source:** https://sumproduct.com/blog/power-query-selective-staffing-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Selective Staffing Part 5

*   November 23, 2021

Power Query: Selective Staffing Part 5
======================================

Power Query: Selective Staffing Part 5
======================================

24 November 2021

_Welcome to our Power Query blog. This week, I revisit my second inclusion example to show a solution that excludes data._

I have looked at two examples over the last few weeks where I included data based on a list of values. [Last week](https://sumproduct.com/blog/power-query-selective-staffing-part-4/)
, I revisited my first example to see how I would have excluded the data instead. This time I will revisit my second example:

In [Power Query: Selective Staffing Part 3](https://sumproduct.com/blog/power-query-selective-staffing-part-3/)
 , I had a table of quote data for each of my salespeople, and a list of salespeople that I wished to view quote details for:

![](<Base64-Image-Removed>)

I used **M List()** functionality, which I will revisit shortly, to achieve the result:

![](<Base64-Image-Removed>)

I am considering the situation where I want to exclude salespeople instead. The new Excel Tables are **Sales\_Quotes\_Exclude** and **Quote\_Selection\_Exclude**:

![](<Base64-Image-Removed>)

I need to create a List Query which will contain the excluded salespeople. Since the column name has changed, the quickest way to do this is by extracting the data from the Excel Table **Quote\_Selection\_Exclude** using ‘From Table/Range’ from the ‘Get & Transform’ section of the Data tab:

![](<Base64-Image-Removed>)

I then choose to ‘Convert to List’ from the Transform tab:

![](<Base64-Image-Removed>)

The **M** code I used for the last example can be viewed in the Advanced Editor for the query **Staff\_Quotes**.

![](<Base64-Image-Removed>)

I create a duplicate of **Staff\_Quotes**, which I will call **Staff\_Quotes Exclude**.

![](<Base64-Image-Removed>)

I need to change the Source step to point at the new Excel Table **Staff\_Quotes\_Exclude** instead of **Staff\_Quotes**. I change the **M** code from this:

**\= Excel.CurrentWorkbook(){\[Name=”Staff\_Quotes”\]}\[Content\]**

to this:

**\= Excel.CurrentWorkbook(){\[Name=”Staff\_Quotes\_Exclude”\]}\[Content\]**

Having changed the code, I look at it further in the Advanced Editor:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Staff\_Quotes\_Exclude”\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Salesperson “, type text}, {“Quote Number”, Int64.Type}, {“Success Rate”, Percentage.Type}, {“Profit”, type number}}),**

    **// Only keep rows if the name is on the Quote\_Selection list**

    **#”Keep Included Rows” = Table.SelectRows(#”Changed Type”, each List.ContainsAny(Record.ToList(\_), Quote\_Selection))**

**in**

    **#”Keep Included Rows”**

I need to change the line

    **#”Keep Included Rows” = Table.SelectRows(#”Changed Type”, each List.ContainsAny(Record.ToList(\_), Quote\_Selection))**

to reverse the logic and use **Quote\_Selection\_Exclude** instead of **Quote\_Selection**. I also rename the line to reflect its new purpose:

    **#”Remove Excluded Rows” = Table.SelectRows(#”Changed Type”, each not List.ContainsAny(Record.ToList(\_), Quote\_Selection\_Exclude))**

This means that the final ‘**in**‘ step should also refer to the new name for the step

**in**

    **#”Remove Excluded Rows”**

I should also update the comments to reflect the new functionality:

   **// now exclude anything that matches the list**

When I click Done, the lines that are not excluded are shown:

![](<Base64-Image-Removed>)

The information for the ‘Remove Excluded Rows’ step reflects the current functionality:

![](<Base64-Image-Removed>)

There is often more than one method to achieve the same results, and I will look at another approach I could have used for this example, which I will show next week.

Come back next time for more ways to use Power Query

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-selective-staffing-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-selective-staffing-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-selective-staffing-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-selective-staffing-part-5/#0)

[](https://sumproduct.com/blog/power-query-selective-staffing-part-5/#0 "close")

top