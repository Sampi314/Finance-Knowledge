# Power Query: Options for Table Groups

**Source:** https://sumproduct.com/blog/power-query-options-for-table-groups/

---

[Home](https://sumproduct.com/)

\> Power Query: Options for Table Groups

*   December 22, 2020

Power Query: Options for Table Groups
=====================================

Power Query: Options for Table Groups
=====================================

23 December 2020

Welcome to our Power Query blog. This week, I look closer at Table.Group(), which I used last week.

This is the data that I used in [last week’s blog](https://sumproduct.com/blog/power-query-divided-groups/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-85-1.jpg)

I used the **GroupKind** parameter (deliberately with a capital ‘**G**‘) on the **M** code function **Table.Group()**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-73-1.jpg)

The **M** code I used for this was:

**\= Table.Group(#”Changed Type”, {“Verified”}, {{“GroupedData”, each \_, type table \[Date=nullable datetime, Income=nullable number, Department=nullable text, Verified=nullable text\]}}, GroupKind.Local)**

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-65-1.jpg)

This has worked, giving me separate groups for each range of dates corresponding to a change in value on **Verified_._** Also note, that if I don’t want to sort my data, it’s more efficient to set **GroupKind** to local, as it doesn’t sort the data.

Going back to the definitions in the help pages for **Table.Group()**:

**Table.Group(table** as table, **key** as any, **aggregatedColumns** as list, optional **groupKind** as nullable number, optional **comparer** as nullable function**)** as table

This groups the rows of **table** by the values in the specified column, **key**, for each row. For each group, a record is constructed containing the key columns (and their values) along with any aggregated columns specified by **aggregatedColumns**. Note that if multiple keys match the **comparer**, different keys may be returned. This function cannot guarantee to return a fixed order of rows. Optionally, groupKind and comparer may also be specified.

I have looked at the first optional parameter, **groupKind**, but there is also a **comparer** parameter that I may specify.

The **comparer** value can be:

*   **Comparer.Equals****:** returns a logical value based on the equality check over the two given values
*   **Comparer.FromCulture****:** returns a **comparer** function, given the culture and a logical value for case sensitivity for the comparison. The default value for **ignoreCase** is false. The values for **culture** are well known text representations of locales used in the .NET framework
*   **Comparer.Ordinal****:** returns a **comparer** function, which uses Ordinal rules to compare values
*   **Comparer.OrdinalIgnoreCase****:** returns a case-insensitive **comparer** function, which uses Ordinal rules to compare the provided values **x** and **y**
*   **Culture.Current****:** returns the current culture of the system.

I am going to modify my data slightly to show how this may be useful.

![](<Base64-Image-Removed>)

This time, I have separate groups for YES and Yes, which is not helpful. I am going to use **Comparer.OrdinalIgnoreCase** to just give me one group for yes / Yes / YES and one for no / No / NO.

![](<Base64-Image-Removed>)

When I enter my changed step, I can see the difference:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.Group(#”Changed Type”, {“Verified”}, {{“GroupedData”, each \_, type table \[Date=nullable datetime, Income=nullable number, Department=nullable text, Verified=nullable text\]}},1, Comparer.OrdinalIgnoreCase)**

Note that this only works with **GroupKind** global, since there needs to be a sort where the case is ignored.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-options-for-table-groups/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-options-for-table-groups/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-options-for-table-groups/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-options-for-table-groups/#0)

[](https://sumproduct.com/blog/power-query-options-for-table-groups/#0 "close")

top