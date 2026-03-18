# Power Query: Flat Out

**Source:** https://sumproduct.com/blog/power-query-flat-out/

---

[Home](https://sumproduct.com/)

\> Power Query: Flat Out

*   March 30, 2021

Power Query: Flat Out
=====================

Power Query: Flat Out
=====================

31 March 2021

_Welcome to our Power Query blog. This week, I look at ways to improve the memory usage of a query involving flat files._

have a query which is running slowly. For the purposes of this blog, the queries are assumed to be coming from flat files which are not subject to query folding. If you have no idea what query folding is, don’t worry – more on query folding in a future blog!

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-226.jpg)

This week, I will look at a couple of ways to improve the memory used processing the query in the Power Query engine. Next time, I will also look at how to speed up loading this query to the Data Model in Power BI Desktop.

There are two areas of this query which are greedy when it comes to memory. The first is right at the beginning, in the first step:

**Source = Table.NestedJoin(ACCT\_Order\_Charges,**

                                    **{“Item\_Key”},**

                                    **Items,**

                                    **{“Item\_Key”},**

                                     **“NewColumn”,**

                                    **JoinKind.LeftOuter)**

I am merging two queries to get this query. I covered how to improve table merges in [Power Query: Merging Matters](https://sumproduct.com/blog/power-query-merging-matters/)
. I can add a **Table.Buffer()** step to store a joined table in memory. Although I normally start with the source step, this is not a rule, so I can add a step before it in the Advanced Editor:

**BufferedTable = Table.Buffer(Items)**

I can then refer to this instead of the table **Items** in the join:

**Source = Table.NestedJoin(ACCT\_Order\_Charges,**

                                    **{“Item\_Key”},**

                                    **BufferedTable,**

                                    **{“Item\_Key”},**

                                    **“NewColumn”,**

                                    **JoinKind.LeftOuter)**

![](<Base64-Image-Removed>)

This should improve the merge. The next area I can improve is the Added Custom step.

**\= Table.AddColumn(#”Added Index”, “Running Total”, each List.Sum(List.Range(#”Added Index”\[Amount\],0,\[Index\])))**

This is reading all the values in a list and adding them up. I describe this process and using **List.Buffer()** to speed things up in [Power Query: Keep on Running](https://sumproduct.com/blog/power-query-keep-on-running/)
. Instead of using **#”Added Index”\[Amount\]**, I can buffer this value. I insert a step before **Added Custom** (though it can be after it, Power Query doesn’t care!).

**BufferedValues = List.Buffer(#”Added Index”\[Amount\])**

I must also refer to this in **Added Custom**:

**\= Table.AddColumn(#”Added Index”, “Running Total”, each List.Sum(List.Range BufferedValues,0,\[Index\])))**

![](<Base64-Image-Removed>)

_Next time, I will consider how to make this query more efficient when loading to the Data Model in Power BI Desktop._

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-flat-out/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-flat-out/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-flat-out/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-flat-out/#0)

[](https://sumproduct.com/blog/power-query-flat-out/#0 "close")

top