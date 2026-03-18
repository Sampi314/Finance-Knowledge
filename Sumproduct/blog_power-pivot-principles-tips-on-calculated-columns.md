# Power Pivot Principles: Tips on Calculated Columns

**Source:** https://sumproduct.com/blog/power-pivot-principles-tips-on-calculated-columns/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Tips on Calculated Columns

*   October 15, 2018

Power Pivot Principles: Tips on Calculated Columns
==================================================

Power Pivot Principles: Tips on Calculated Columns
==================================================

16 October 2018

_Welcome back to our Power Pivot blog. Today, we discuss some tips and best practices you should keep in mind when working with Calculated Columns._

**Creating Calculated Columns**

When creating new calculated columns, they are automatically added to the far right of other columns in a table.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-550.jpg)

Their positions are not permanent though, we can rearrange the Calculated Columns after we have created them:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-572.jpg)

**Naming Calculated Columns**

New Calculated Columns are assigned the default name of ‘Calculated Column 1’, ‘Calculated Column 2’, etc. Therefore, we should always give calculated columns a unique name within each table. Otherwise using them in [measures](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-measures-and-aggregations)
 or other calculated columns may lead to calculation issues.

**Unique Names**

Always give a unique name to a calculated column immediately after creating it. If we rename the calculated column after using it in other calculated columns or measures we may also have to update any formulas that relied on the initial calculated column.

Calculated columns can possess the same name as measures, however doing so may result in potential calculation errors down the road. We strongly recommend to avoid assigning the same name to a calculated column and a measure.

**Fully Qualified Column References**

When referring to calculated columns in other calculated columns or measures we should always use the ‘fully qualified column reference’. What is that you may ask? A ‘fully qualified column reference’ includes the table name followed by the column name in square brackets. For example, the fully qualified column reference for the ‘Standard Cost’ column in the ‘Product SubCategory’ table is:

![](<Base64-Image-Removed>)

This is so that we can clearly distinguish between Calculated Columns, Columns and Measures in our formulas.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-tips-on-calculated-columns/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-tips-on-calculated-columns/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-tips-on-calculated-columns/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-tips-on-calculated-columns/#0)

[](https://sumproduct.com/blog/power-pivot-principles-tips-on-calculated-columns/#0 "close")

top