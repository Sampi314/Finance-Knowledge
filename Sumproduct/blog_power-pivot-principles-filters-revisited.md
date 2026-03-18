# Power Pivot Principles: Filters Revisited

**Source:** https://sumproduct.com/blog/power-pivot-principles-filters-revisited/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Filters Revisited

*   August 20, 2018

Power Pivot Principles: Filters Revisited
=========================================

Power Pivot Principles: Filters Revisited
=========================================

21 August 2018

_Welcome back to our Power Pivot blog. Today, we discuss another way to use Filters in Power Pivot._

In a previous blog, [Power Pivot Principles: Filters](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-filters)
, we discussed how to use Filters in a PivotTable created with Power Pivot. This week, we will discuss how to incorporate filters directly into the measures we create in Power Pivot.

We begin with creating a new table with the following values:

![](<Base64-Image-Removed>)

Remember to name the table ‘MinListPrice’. We will then add this table to our Data Model. After adding it to our Data Model we can create a new measure called ‘MinAmount’ with the following formula:

**\=Min(MinListPrice\[MinListPrice\])**

![](<Base64-Image-Removed>)

Our next move is to create another measure called **_Sales Above Selected Unit List Price_**, where the formula should be:

**\=CALCULATE(\[Sales\],FILTER (Sales\[UnitPrice\]>=\[MinAmount\]))**

![](<Base64-Image-Removed>)

Note that this formula wouldn’t work without using the **FILTER** function. This is because the calculation has to be performed on a record by record basis, rather than in aggregate, as **CALCULATE** usually works. This requires you to filter records, _i.e._ use the **FILTER** function.

Insert a slicer for MinListPrice and add the **_Sales Above Min Amount_** into the ‘Values’ area of the PivotTable.

![](<Base64-Image-Removed>)

Selecting different price points in the slicer will highlight the amount of Sales made where the unit price is above the minimum price point.

![](<Base64-Image-Removed>)

Interesting? We can apply the greater than or even the equals to operator to this filter.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-filters-revisited/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-filters-revisited/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-filters-revisited/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-filters-revisited/#0)

[](https://sumproduct.com/blog/power-pivot-principles-filters-revisited/#0 "close")

top