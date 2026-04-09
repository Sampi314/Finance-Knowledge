# Power Query: Building Bridges

**Source:** https://sumproduct.com/blog/power-query-building-bridges/

---

[Home](https://sumproduct.com/)

\> Power Query: Building Bridges

*   November 6, 2018

Power Query: Building Bridges
=============================

Power Query: Building Bridges
=============================

7 November 2018

_Welcome to our Power Query blog. This week, I look at creating a bridge table._

Today I am going to look at how to construct and use a bridge table. This does not mean I’ve taken up playing cards; this kind of bridge table can also be called an intermediate table, and it allows me to create a ‘many to many’ join.

In [P](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-if-you-cant-tell-them-apart-join-them)
[ower Query: If You Can’t Tell Them Apart, Join Them](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-if-you-cant-tell-them-apart-join-them)
, I looked at using different types of joins in order to see what was missing from two similar looking tables.

![](<Base64-Image-Removed>)

The previous screen shows the data I used (now in Excel 2016), and the join options available. Whilst I can happily merge these queries in Power Query, once I upload their product to the data model, I encounter problems joining my two queries if they have duplicate entries, as I will show.

In order to look at ‘many to many’ joins in the data model and how to achieve them with Power Query, I am going to create two simple subsets of this data.

![](<Base64-Image-Removed>)

I create queries for each of these tables by using the ‘From Table’ option on the ‘Get and Transform’ section of the ‘Data’ tab. I create the queries as ‘Connection Only’ and add them to the Data Model. This can be done at any time by right-clicking on the query and choosing ‘Load to’:

![](<Base64-Image-Removed>)

I then merge the queries.

![](<Base64-Image-Removed>)

I choose the ‘Full Outer’ join, which should include all rows from both.

![](<Base64-Image-Removed>)

My first table rows are shown, and I can expand the final column to see the data from the second table.

![](<Base64-Image-Removed>)

I have all 15 rows.

Now I am going to check what happens when I link **Table\_One** to **Table\_Two** in the Data Model. This will involve a small excursion into Power Pivot! (For more on the interaction between Power Query and Power Pivot, please refer to see [Power Query: (Data) Model Building](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-data-model-build)
 and [Power Query: Models Have Relationship Issues Too](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-models-have-relationship-issues-too)
.)

![](<Base64-Image-Removed>)

In the ‘Power Pivot’ tab, I can select to ‘Manage’ the Data Model.

![](<Base64-Image-Removed>)

In the Power Pivot window, if I choose the ‘Design’ tab, I can ‘Manage Relationships’, _viz_.

![](<Base64-Image-Removed>)

When I try to link **Table\_One** to **Table\_Two** I get the message that it is a ‘many to many’ relationship, and therefore is not currently supported. I need to create a **bridge table** between **Table\_One** and **Table\_Two** so that I can join them. My bridge table will contain unique entries of all the data in **Table\_One** and **Table\_Two**, so I can build it from my merged table, currently called **Merge4**.

![](<Base64-Image-Removed>)

I rename my table **Bridge\_table**. I need to clean it up, as I only need a list of unique full names. I delete all the other columns by selecting the **_FULL\_NAME_** column and choosing to ‘Remove Other Columns’.

![](<Base64-Image-Removed>)

This gives me one column, and right-clicking again, I can select to ‘Remove Duplicates’.

![](<Base64-Image-Removed>)

I now have a unique list of names which I can use as a bridge table. Back in the Power Pivot window, I link **Table\_One** to **Bridge\_table**.

![](<Base64-Image-Removed>)

This is fine as it is a ‘many to one’ relationship.

![](<Base64-Image-Removed>)

I also create a relationship between **Bridge\_table** and **Table\_Two**. This is a ‘one to many’ relationship.

![](<Base64-Image-Removed>)

Looking at the ‘Diagram View’ from the ‘Home’ tab in my PowerPivot window, I can see that the two tables are now connected via the bridge table. Slicing or filtering on this intermediate, bridge table will affect both dependent tables. This is a common technique employed in relational databases and if you have never encountered this before, once you start using this technique you’ll wonder how you ever got by without it.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-building-bridges/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-building-bridges/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-building-bridges/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-building-bridges/#0)

[](https://sumproduct.com/blog/power-query-building-bridges/#0 "close")

top