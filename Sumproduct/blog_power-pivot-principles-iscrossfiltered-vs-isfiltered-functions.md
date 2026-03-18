# Power Pivot Principles: ISCROSSFILTERED vs ISFILTERED Functions

**Source:** https://sumproduct.com/blog/power-pivot-principles-iscrossfiltered-vs-isfiltered-functions/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: ISCROSSFILTERED vs ISFILTERED Functions

*   July 27, 2020

Power Pivot Principles: ISCROSSFILTERED vs ISFILTERED Functions
===============================================================

Power Pivot Principles: ISCROSSFILTERED vs ISFILTERED Functions
===============================================================

28 July 2020

_Welcome back to the Power Pivot Principles blog. This week, we will talk about the difference between the **ISCROSSFILTERED** and the **ISFILTERED** functions in DAX._

A while ago, we wrote about the **[ISFILTERED](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-properly-calculating-weighted-totals-with-the-isfiltered-function)
** function. Now, we think it’s also worth mentioning the **ISCROSSFILTERED** function.

To recap, the **ISFILTERED** function has the following syntax:

**ISFILTERED(columnName)**

This returns a TRUE value when the **columnName** parameter is filtered in the PivotTable (by definition, all simple, non-total rows and columns in a PivotTable are filtered by a given context). If there is no filter applied to the **columnName**, the function will return with FALSE.

Similarly, the **ISCROSSFILTERED** returns TRUE when the column has a filter because of automatic propagation of another filter and not because of a filter applied directly to it. This function has the following syntax:

**ISCROSSFILTERED(columnName)**

The difference between the two functions is that a column is said to be **cross-filtered** when a filter applied to another column in the same table or in a related table affects **columnName** by filtering it. A column is said to be **filtered** directly when the filter or filters apply over the column, where the **ISFILTERED** function will return TRUE.

To prevent confusing you, let’s demonstrate with an example. Consider that we have **Sales** data by stores and different products already loaded to the Power Pivot Data Model:

![](<Base64-Image-Removed>)

We also have another table of ‘**Store Key**‘ and **Branch** data loaded into the Data Model:

![](<Base64-Image-Removed>)

In the Diagram view, we define the relationship between the two tables, by connecting the ‘**Store Key**‘ fields in the two tables:

![](<Base64-Image-Removed>)

Next, we will create two measures:

*   ‘**ISFILTERED Store**‘:

**\=ISFILTERED(Sales\[Store Key\])**

*   ‘**ISCROSSFILTERED Store’**:

**\=ISCROSSFILETED(‘Store\_Branch\_Key'\[Branch\])**

Going back to Excel, we will create a PivotTable and a **Branch** slicer:

![](<Base64-Image-Removed>)

Initially, the ‘**ISFILTERED Store**‘ returns all values as TRUE because it has the direct filter on it, which basically is the ‘**Store Key’** that we put on the table. It is going row by row, giving us the unique value of these. Notice that the ‘**Grand Total**‘ value of ‘**ISFILTERED Store**‘ column is FALSE. Meanwhile, we haven’t selected anything on the **Branch** slicer, so all values return FALSE.

Now, we select a value on the slicer:

![](<Base64-Image-Removed>)

The ‘**ISCROSSFILTERED Store**‘ column returns all TRUE values, including the ‘**Grand Total**‘. This happens based on the relationship between ‘**Store Key**‘ of the two tables, in this case, the ‘Store Key’ is being filtered by its related field in a different table, which is regarded as the indirect filter.

Clear as mud?

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-iscrossfiltered-vs-isfiltered-functions/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-iscrossfiltered-vs-isfiltered-functions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-iscrossfiltered-vs-isfiltered-functions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-iscrossfiltered-vs-isfiltered-functions/#0)

[](https://sumproduct.com/blog/power-pivot-principles-iscrossfiltered-vs-isfiltered-functions/#0 "close")

top