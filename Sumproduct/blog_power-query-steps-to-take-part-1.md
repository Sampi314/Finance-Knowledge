# Power Query: Steps to Take – Part 1

**Source:** https://sumproduct.com/blog/power-query-steps-to-take-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Steps to Take – Part 1

*   September 13, 2022

Power Query: Steps to Take – Part 1
===================================

Power Query: Steps to Take – Part 1
===================================

14 September 2022

_Welcome to our Power Query blog. This week, I am going to look at a worked example._

The tent business has a new administrative assistant, who used to work in the United States. George has provided some information, but it’s not yet in a format I can use:

![](https://sumproduct.com/wp-content/uploads/2025/05/c5f70e541a6d6d94619988dfd1ef1277.jpg)

I start in the usual way, by choosing ‘From Table/Range’ in the ‘Get & Transform’ section of the Data tab. This gives me my initial query:

![](https://sumproduct.com/wp-content/uploads/2025/05/ce77107e734550084e8b5df2ab0ccfd8.jpg)

There are of course many ways I can transform this data, but I will begin by establishing a link so that I can keep track of which rows relate to each other. I commence by right-clicking on **Column1**, and choosing to ‘Replace Values’:

![](https://sumproduct.com/wp-content/uploads/2025/05/4160ebbf34f7cbc074f0dff0f49506fc.jpg)

The phrase ‘salespeople available’ is no use to me, so I replace this value with _null_.

![](https://sumproduct.com/wp-content/uploads/2025/05/b8ee94c0fb50de98008062033f92d90e.jpg)

I can now choose ‘Fill’ and then ‘Down’ from the right-click menu for **Column1**.

![](https://sumproduct.com/wp-content/uploads/2025/05/b37c0551e6c2e3c039bf0ae9975edda1.jpg)

My rows are now linked by month; I rename the column **Month** for clarity.

![](https://sumproduct.com/wp-content/uploads/2025/05/682362cf52a353d584f4c8b9847ef287.jpg)

I rename this query **Base**. I then make a Reference copy of **Base**.

![](https://sumproduct.com/wp-content/uploads/2025/05/2c8d72a7c526e1f4eac191dbfe01762e.jpg)

I call this query **Quantities**. I only want the rows pertaining to quantities. I would like to use text filters, but to do this I need to change the data type of **week 1** to Text:

![](https://sumproduct.com/wp-content/uploads/2025/05/99c760b5be9deb733e5a507293deab4e.jpg)

If I click on the filter arrow next to the title, I can use the ‘Does Not Contain’ filter:

![](https://sumproduct.com/wp-content/uploads/2025/05/97f290309442c3e0c52eeb9c2553f03f.jpg)

I select those rows that don’t contain a forward slash (**/**).

![](https://sumproduct.com/wp-content/uploads/2025/05/f5d3744b5f0d0df5cf769666b8f61387.jpg)

This gives me the rows pertaining to quantity only.

![](<Base64-Image-Removed>)

Next time, I will create another query for the date information.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-steps-to-take-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-steps-to-take-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-steps-to-take-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-steps-to-take-part-1/#0)

[](https://sumproduct.com/blog/power-query-steps-to-take-part-1/#0 "close")

top