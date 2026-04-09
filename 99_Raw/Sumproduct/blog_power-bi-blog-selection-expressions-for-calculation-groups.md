# Power BI Blog: Selection Expressions for Calculation Groups

**Source:** https://sumproduct.com/blog/power-bi-blog-selection-expressions-for-calculation-groups/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Selection Expressions for Calculation Groups

*   May 1, 2024

Power BI Blog: Selection Expressions for Calculation Groups
===========================================================

Power BI Blog: Selection Expressions for Calculation Groups
===========================================================

2 May 2024

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at how selection expressions – and their behaviour in particular – is changing for calculation groups._

![](<Base64-Image-Removed>)

Calculation Groups in Power BI allow you to apply a single calculation across multiple measures without the need to create additional calculated columns or measures. This not only saves time but also enhances the manageability of your data model.

These have now become more powerful. Microsoft has recently introduced into Preview revised selection expressions for calculation groups, which allow you to influence what happens in case the user makes multiple selections for a single calculation group or does not make a selection at all. This provides not only a better way to perform error handling, it also opens interesting scenarios that provide some good default behaviours, _e.g._ automatic currency conversion. Selection expressions are optionally defined on a calculation group and consist of an expression and an optional dynamic format expression.

This new capability comes with an extra benefit of potential performance improvements when evaluating complex calculation group items.

To define and manage selection expressions for calculation groups, you can leverage the same tools you use today to work with calculation groups. On a calculation group you will be able to specify the following selection expressions both consisting of the Expression itself and a **FormatStringDefinition**:

*   **multipleOrEmptySelectionExpression:** this expression has a default value of **SELECTEDMEASURE()** and will be returned if the user selects multiple calculation items on the same calculation group or if a conflict between the user’s selections and the filter context occurs
*   **noSelectionExpression:** this expression has a default value of **SELECTEDMEASURE()** and will be returned if the user did not select any items on the calculation group.

Here’s an overview of the type of selection compared to the current behaviour that was shipped before this Preview, and the new behaviour both when the expression is defined on the calculation group and when it’s not. The items in bold are where the new action differs from the previous approach.

![](<Base64-Image-Removed>)

To illustrate, here are some examples.

**_Multiple or Empty Selections_**

If the user makes multiple selections on the same calculation group, the current behaviour is to return the same result as if the user did not make any selections. In this Preview, you can specify a **multipleOrEmptySelectionExpression** on the calculation group. If you did, then we evaluate that expression and related dynamic format string and return its result. You can for example use this to inform the user about what is being filtered:

EVALUATE

{

CALCULATE (

\[MyMeasure\],

‘MyCalcGroup'\[Name\] = “item1” || ‘MyCalcGroup'\[Name\] =  
“item2”

)

}

— multipleOrEmptySelectionExpression on MyCalcGroup:

IF(ISFILTERED ( ‘MyCalcGroup’ ),”Filters: “”&

*   [Log in](https://sumproduct.com/blog/power-bi-blog-selection-expressions-for-calculation-groups/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-selection-expressions-for-calculation-groups/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-selection-expressions-for-calculation-groups/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-selection-expressions-for-calculation-groups/#0)

[](https://sumproduct.com/blog/power-bi-blog-selection-expressions-for-calculation-groups/#0 "close")

top