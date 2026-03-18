# Power Query: Power Query Online – Part 13

**Source:** https://sumproduct.com/blog/power-query-power-query-online-part-13/

---

[Home](https://sumproduct.com/)

\> Power Query: Power Query Online – Part 13

*   October 31, 2023

Power Query: Power Query Online – Part 13
=========================================

Power Query: Power Query Online – Part 13
=========================================

1 November 2023

_Welcome to our Power Query blog. Today, I am looking at the features on the Diagram view that allow me to analyse relationships._

In the current series, I am looking at Power Query Online, which I have accessed from Power Apps:

![](https://sumproduct.com/wp-content/uploads/2025/05/69cec0c23d66df22e507784e62806251.jpg)

[Last week](https://sumproduct.com/blog/power-query-power-query-online-part-12/)
, I checked out some of the options on the right-click menu on Diagram view:

![](https://sumproduct.com/wp-content/uploads/2025/05/b1d83e37a5ad17ac9cd1d112129795e1.jpg)

This time, I will look at the other information pertaining to related queries. I showed [last week](https://sumproduct.com/blog/power-query-power-query-online-part-12/)
 that I could choose to highlight related queries as a default:

![](https://sumproduct.com/wp-content/uploads/2025/05/c8ac6f4fc76d0669e3148227a12d29cc.jpg)

If I hover over the node in **Addresses**, I can see the type of relationships from the perspective of **Addresses**:

![](https://sumproduct.com/wp-content/uploads/2025/05/5f08d0f825768fc37fad1070e0f98ee3.jpg)

I can see ‘Direct dependent queries’, which in this case is **Customer full addresses**, and ‘Indirect dependent queries’, which in this case is **Customers with full addresses**, because **Customers with full addresses** is directly dependent upon **Customer full addresses**.

The default highlighting is from the perspective query with the node filled; however, I do not need to select a different node to see the relationships from another query’s perspective – I can just hover over the appropriate node.

![](https://sumproduct.com/wp-content/uploads/2025/05/588b3b9904b9b6f596fc73672fce84ee.jpg)

If I hover over the left-hand node on **Customer full addresses**, I can see which queries are referenced by **Customer full addresses**. In this case, there are only ‘Direct referenced queries’ since **Addresses** and **Customer\_Addresses** came from the data source. I can only see highlighting from the perspective of the query with the filled node, and only one query may have a filled node.

![](https://sumproduct.com/wp-content/uploads/2025/05/6cfcd513a40b3ede5c4ab3f80b11c0d1.jpg)

From the perspective of **Customers with full addresses**, there are ‘Direct referenced queries’ which were merged to create this query, and also ‘Indirect reference queries’ which were used to create the queries that are merged to create this query.

Note that selecting a node will change the perspective of the query highlighting, but not change the query selected. The highlighted outline of **Addresses** indicates that it is the selected query, and this is why the steps from that query appear in the ‘Query settings’ pane.

![](<Base64-Image-Removed>)

I can also choose another query from a reference or dependency list to change both to the perspective of that query, and also select that query. Below, I have chosen **Customers with full addresses** from the ‘Indirect dependent queries’ list for **Customer\_Addresses**:

![](<Base64-Image-Removed>)

Finally, I can also toggle query highlighting to on or off using the icon currently visible on the selected query, and also on the query with the node selected:

![](<Base64-Image-Removed>)

If the highlighting icon is currently highlighted, the relationship highlighting is turned off. If it is not already highlighted from the perspective of the current query, it is turned on for that query. Although it is not shown by default, this icon is available when I hover over any query with relationships (in the next image I am hovering over **Customers with addresses**):

![](<Base64-Image-Removed>)

It is not possible for me to highlight **Products** or **Product Categories** in this way, as no relationships exist for either of them.

This brings my current series on Power Query Online to a close. I hope it will not be too long before the same interface is available in Power Query Desktop. In the meantime, I will revisit some Power Query Desktop topics that have been improved since I last covered them…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-power-query-online-part-13/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-power-query-online-part-13/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-power-query-online-part-13/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-power-query-online-part-13/#0)

[](https://sumproduct.com/blog/power-query-power-query-online-part-13/#0 "close")

top