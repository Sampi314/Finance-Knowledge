# Power Pivot Principles: Using USERELATIONSHIP to Activate an Inactive Relationship

**Source:** https://sumproduct.com/blog/power-pivot-principles-using-userelationship-to-activate-an-inactive-relationship/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Using USERELATIONSHIP to Activate an Inactive Relationship

*   March 30, 2020

Power Pivot Principles: Using USERELATIONSHIP to Activate an Inactive Relationship
==================================================================================

Power Pivot Principles: Using USERELATIONSHIP to Activate an Inactive Relationship
==================================================================================

31 March 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a method of creating a virtual relationship in Power Pivot._

In Power Pivot, a physical relationship connects two tables through an equivalence over a single column. The purpose of a relationship in a Tabular model is to filter through specific attributes between two different tables. The engine automatically propagates the filter context in a query in terms of the active filter direction. An inactive relationship is ignored, but can be manipulated by certain DAX functions. This week, we are going to talk about the DAX function **USERELATIONSHIP**.

This function specifies an existing relationship to be used in the evaluation of a DAX expression. The relationship is defined by naming, as arguments, the two columns that serve as endpoints. It has the following syntax to operate:

**USERELATIONSHIP (ColumnName1, ColumnName2)**

where:

*   **ColumnName1** represents the foreign (or primary) key of the relationship
*   **ColumnName2** represents the primary (or foreign) key of the relationship.

It should be noted that the function returns no value. It only enables the indicated relationship for the duration of the calculation.

Let’s look at a simple example. Suppose we have following two tables, **Calendar** and **Sales** (neither displayed in full):

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-245-1.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-242-1.jpg)

They have the following relationship:

![](<Base64-Image-Removed>)

In this case, the active relationship is setup between the field ‘**Order Date’** in the **Sales** table and the field **Date** in **Calendar** table. Another relationship, which is inactive, is setup between the field ‘**Ship Date**‘ in **Sales** table and the field **Date** in **Calendar** table. Typically, only one active relationship works in data modelling, however, we can use **USERELATIONSHIP** to make the inactive function active in a logic way.

We write the DAX syntax as following:

![](<Base64-Image-Removed>)

**\=CALCULATE(SUM(Sales\[SalesAmount\]),USERELATIONSHIP(Sales\[Ship Date\],’Calendar'\[Date\]))**

In the measure above, we use the **CALCULATE** function to filter on the relationship established between ‘**Ship Date**‘ in **Sales** and **Date** in **Calendar**. **USERELATIONSHIP** does not return any value, it only enables the inactive relationship to be active between the **Sales** and **Calendar** tables.

Then, we export the result as a PivotTable and use **Year** as the row and **OrderDateSales** and **ShipDateSales** as fields, with the following result:

![](<Base64-Image-Removed>)

As indicated by the PivotTable, the **OrderDateSales** shows the result of sales amount in accordance with the direct relationship and the **ShipDateSales** shows the result of the inactive relationship. The total sales value remains the same for both fields.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog/power-pivot-principles-using-userelationship-to-activate-an-inactive-relationship/?id=152)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-using-userelationship-to-activate-an-inactive-relationship/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-using-userelationship-to-activate-an-inactive-relationship/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-using-userelationship-to-activate-an-inactive-relationship/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-using-userelationship-to-activate-an-inactive-relationship/#0)

[](https://sumproduct.com/blog/power-pivot-principles-using-userelationship-to-activate-an-inactive-relationship/#0 "close")

top