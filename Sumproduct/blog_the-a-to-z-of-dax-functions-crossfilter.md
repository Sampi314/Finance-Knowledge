# The A to Z of DAX Functions – CROSSFILTER

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossfilter/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CROSSFILTER

*   November 22, 2022

The A to Z of DAX Functions – CROSSFILTER
=========================================

Power Pivot Principles: The A to Z of DAX Functions – CROSSFILTER
=================================================================

22 November 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CROSSFILTER**._

**_The CROSSFILTER function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/1831ce4eefa9daaa9fa1a6482e867e21.jpg)

The **CROSSFILTER** function specifies the cross-filtering direction to be used in a calculation for a relationship that exists between two columns.

The function does not return any value. It may only be used in functions that define filter as an argument such as **CALCULATE** and **CALCULATETABLE** _etc_. It sets the cross-filtering direction for the indicated relationship and uses existing relationships in the model, identifying relationships by their ending point columns. It is an especially useful and smart technique that applies the filter through the relationships in the many-to-one direction when necessary.

The **CROSSFILTER** function uses the following syntax to operate:

**CROSSFILTER**(**columnName1**, **columnName2**, **direction**)

where:

*   **columnName1** represents the name of an existing column, using standard DAX syntax and fully qualified, that usually represents the many sides of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument cannot be an expression

*   **columnName2** is the name of an existing column, using standard DAX syntax and fully qualified, that usually represents the one side or lookup side of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument also cannot be an expression

*   **direction** is the cross-filter direction to be specified. The value can be one of the following:  
    o **OneWay:** filters on the one side or the lookup side of a relationship filter the other side. This option cannot be used with a one-to-one relationship . You should not use this option on a many-to-many relationship because it is unclear which side is the lookup side; you should use **OneWay\_LeftFiltersRight** or **OneWay\_RightFiltersLeft**_(below)_ instead  
    o **OneWay\_LeftFiltersRight:** filters on the side of **columnName1** filter the side of **columnName2**. This option cannot be used with a one-to-one or many-to-one relationship  
    o **OneWay\_RightFiltersLeft:** filters on the side of **columnName2** filter the side of **columnName1**. This option cannot be used with a one-to-one or many-to-one relationship  
    o for **One:** do note the differences between Power Pivot and Power BI requirements  
    o **Both:** filters on either side filter the other  
    o **None**: no cross-filtering occurs along this relationship.

For an example, consider the data tables, **DimSales**, **DimShop** and **DimProduct**, shown below:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

They have the following relationships:

![](<Base64-Image-Removed>)

The relationships shown with arrows indicate that **DimProduct** can filter **DimSales** and **DimShop** can also filter **DimSales**. If we want to count the distinct value of products sold (_i.e._ the number of different types of products actually sold) in each shop, we use a measure **Distinct Count of Product** to calculate the unique value of **Product ID** as shown below:

![](<Base64-Image-Removed>)

If we further create a PivotTable base on this measure and see if the PivotTable can filter the distinct count base the filter of **Shop Name**. The result would be:

![](<Base64-Image-Removed>)

The total count of **Distinct Count of Product** is five (5) for all shops, which is not correct. If we take a closer look at the data of **Shop A**, we can see that there are only two products, **Apple** and **Avocado**, which are sold in this shop, not five. The reason for this error is that **DimShop** cannot filter the **DimProduct** on an indirect one-to-many relationship.

One available solution for this case is to use the **CROSSFILTER** function to specify a direction for the relationship to be used between the **DimShop** and **DimProduct** tables. We can create the measure **Distinct Count** in the **DimSales** table as shown below:

![](<Base64-Image-Removed>)

In this measure, we use **CALCULATE** to evaluate the expression we create before and use **CROSSFILTER** to establish the bidirection between **DimSales** and **DimProduct**. Then when we add the measure to the PivotTable created before, the results would become:

![](<Base64-Image-Removed>)

The new measure correctly calculates the Product ID sold for reach shop. If we add **Product Name** as an additional selection criterion in the PivotTable, this would produce the following:

![](<Base64-Image-Removed>)

From the PivotTable, we can clearly identify that for **Shop A**, only **Apple** and **Avocado** are sold, and the distinct count of the product is correctly calculated.

More may be found on **CROSSFILTER**here: [https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-crossfilter](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-crossfilter)
.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossfilter/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossfilter/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossfilter/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossfilter/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-crossfilter/#0 "close")

top