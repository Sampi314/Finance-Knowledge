# Power Query: Project Population – Part 9

**Source:** https://sumproduct.com/blog/power-query-project-population-part-9/

---

[Home](https://sumproduct.com/)

\> Power Query: Project Population – Part 9

*   June 20, 2023

Power Query: Project Population – Part 9
========================================

Power Query: Project Population – Part 9
========================================

21 June 2023

_Welcome to our Power Query blog. This week, I continue combining my queries from a public data source._

I have found some information on population growth provided by The World Bank, which I am using as an example of how to transform real-life data.

![](<Base64-Image-Removed>)

I have been transforming the data, and [last week](https://sumproduct.com/blog/power-query-project-population-part-8/)
, I used ‘Merge Queries’ to combine the data from **Country** and **Country-Series**.

![](<Base64-Image-Removed>)

I’d like to take a closer look at the Source step for this query (the first item in the ‘APPLIED STEPS’ section).

![](<Base64-Image-Removed>)

The **M** code is:

**\= Table.NestedJoin(Country, {“Country Code”},  
#”Country-Series”, {“CountryCode”},  
“Country-Series”, JoinKind.LeftOuter)**

The **M** function used here is **Table.NestedJoin()**. This is the default join method, but I can use a more efficient one. I can use **Table.Join()** instead:

**\= Table.Join(Country, {“Country Code”},  
#”Country-Series”, {“CountryCode”}, JoinKind.LeftOuter)**

At first glance, this appears to have had the same effect.

![](<Base64-Image-Removed>)

However, notice that the code no longer specifies the name of the output column. If I look at the column created,

![](<Base64-Image-Removed>)

I already have the **Data Sources** column; this means that the ‘Expanded Country-Series’ step is now redundant:

![](<Base64-Image-Removed>)

I should delete this step since I have merged the data from **Country** and **Country-Series** with one \[1\] step.

![](<Base64-Image-Removed>)

I would use the **Table.Join()** method over the **Table.NestedJoin()** method when I want to merge most of the columns from both tables, otherwise I would simply be adding columns to delete them again.

Note that in order to use **Table.Join()**, there should be no common column names, otherwise an error would be encountered. This doesn’t mean that I can’t use **Table.Join()** if there are shared column names. I looked at a way of dealing with this in [Joining the dots](https://sumproduct.com/blog/power-query-joining-the-dots/)
.

That’s it for this time; next time, I will move on to the **Data** query…

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-project-population-part-9/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-project-population-part-9/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-project-population-part-9/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-project-population-part-9/#0)

[](https://sumproduct.com/blog/power-query-project-population-part-9/#0 "close")

top