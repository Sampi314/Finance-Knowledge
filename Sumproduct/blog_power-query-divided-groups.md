# Power Query: Divided Groups

**Source:** https://sumproduct.com/blog/power-query-divided-groups/

---

[Home](https://sumproduct.com/)

\> Power Query: Divided Groups

*   December 15, 2020

Power Query: Divided Groups
===========================

Power Query: Divided Groups
===========================

16 December 2020

_Welcome to our Power Query blog. This week, I look at how to group into changes of value._

Just for a change, I have some tent data.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-89-1.jpg)

I want to return the start and end dates of each section of data which has not been verified. I start by extracting my data to Power Query using ‘From Data’ on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-77-1.jpg)

I am going to try and use the ‘Group By’ functionality on the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-70-1.jpg)

I am grouping on **Verified**.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-62-1.jpg)

The problem is, this only creates two groups, one for Yes and one for No – I can see the No row contains data from both date ranges. If I look at the **M** code generated for this step I get:

**\= Table.Group(#”Changed Type”, {“Verified”}, {{“GroupedData”, each \_, type table \[Date=nullable datetime, Income=nullable number, Department=nullable text, Verified=nullable text\]}})**

This uses the **M** function **Table.Group()**:

**Table.Group(table** as table, **key** as any, **aggregatedColumns** as list, optional **groupKind** as nullable number, optional **comparer** as nullable function**)** as table.

This groups the rows of **table** by the values in the specified column, **key,** for each row. For each group, a record is constructed containing the key columns (and their values) along with any aggregated columns specified by **aggregatedColumns**. Note that if multiple keys match the comparer, different keys may be returned. This function cannot guarantee to return a fixed order of rows. Optionally, **groupKind** and **comparer** may also be specified.

The key to solving my issue, is to use the **groupKind** parameter (next week I will look at the other optional parameter, **comparer**). There is nothing to describe the options for the **groupKind** parameter currently in the **Table.Group()** section, but according to [github.com](http://www.github.com/)
, there used to be! They helpfully reproduced what used to be there, which has apparently disappeared when documentation was moved.

A group can be local (**groupKind.Local**) or global (**groupKind.Global**):

*   A **local** group is formed from a consecutive sequence of rows from an input table with the same key value
*   A **global** group is formed from all rows in an input table with the same key value
*   Multiple local groups may be produced with the same key value but only a single global group is produced for a given key value
*   The default **groupKind** value is **groupKind.Global**.

So, in fact the default **groupKind.Global** is pulling all the values together into one row, which, in this case, is not what I want.

I am going to amend my data to use **groupKind.Local**:

![](<Base64-Image-Removed>)

The **M** code is now:

**\= Table.Group(#”Changed Type”, {“Verified”}, {{“GroupedData”, each \_, type table \[Date=nullable datetime, Income=nullable number, Department=nullable text, Verified=nullable text\]}}, GroupKind.Local)**

\[Note in the **M** code **GroupKind.Local** also starts with a capital letter.\]

I enter my changed step.

![](<Base64-Image-Removed>)

This has worked, giving me separate groups for each range of dates corresponding to a change in value on **Verified**. I can now add start and end columns by extracting the minimum and maximum date value from table **GroupedRows**.

![](<Base64-Image-Removed>)

This gives me the record corresponding to the start date.

![](<Base64-Image-Removed>)

I can then extract the date.

![](<Base64-Image-Removed>)

I only want the date, so I expand this.

![](<Base64-Image-Removed>)

The default is to call the column **Date**, I can amend this step to call it ‘Start Date’.

![](<Base64-Image-Removed>)

I now carry out the same sequence of steps to get to the ‘End Date’.

![](<Base64-Image-Removed>)

I now have the start and end date for each range of dates that have been verified (or not verified).

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-divided-groups/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-divided-groups/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-divided-groups/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-divided-groups/#0)

[](https://sumproduct.com/blog/power-query-divided-groups/#0 "close")

top