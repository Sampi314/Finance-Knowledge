# Power Pivot Principles: Introducing the Function CROSSFILTER

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-crossfilter/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the Function CROSSFILTER

*   March 2, 2020

Power Pivot Principles: Introducing the Function CROSSFILTER
============================================================

Power Pivot Principles: Introducing the Function CROSSFILTER
============================================================

3 March 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a new DAX function, CROSSFILTER._

Power Pivot does not support bidirectional relationships, so it is not always so convenient for users to synchronise slicers for different fields. However, the bidirectional filter can be achieved by the DAX function **CROSSFILTER**. This DAX expression specifies the cross-filtering direction to be used in a calculation for a relationship that exists between two columns and it returns no value; the function only sets the cross-filtering direction for the indicated relationship, for the duration of the query.

It has following syntax to operate:

**CROSSFILTER(columnName1, columnName2, direction)**

where:

*   **<columnName1>** is the name of an existing column, using standard DAX syntax and fully qualified, that usually represents the many side of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument cannot be an expression
*   **<columnName2>** is the name of an existing column, using standard DAX syntax and fully qualified, that usually represents the one side or lookup side of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument cannot be an expression
*   **<direction>** is the parameter for the cross-filter direction to be used. This must be one of the following:

1\. **None** – no cross-filtering occurs along this relationship

2\. **One** – filters on the one or lookup side of the side of the relationship filter the many side

3\. **Both** – filters on either side filter the other.

Let’s look at one simple example. Consider the following four (4) tables of **Calendar**, **Sales**, **Product** and **Customer** (not displayed in full):

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-263.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-264-1.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-249-1.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-223-1.jpg)

The tables have a relationship map as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/3ac5370f9f4398a131d56efd88b67702-2.jpg)

From this map, we can see that **Customer** filters through **Sales** and this One-to-Many pattern applies to **Calendar** and **Product** as well. If we want to use **Customer** to filter **Product**, the physical relationship will not allow this filter to work. However, we can use **CROSSFILTER** to establish bidirectional relationship between **Sales** table and **Product** table. In our case, we want to calculate the total count of product name sold for specific customer and we use the following measures.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-171-1.jpg)

**\=COUNT(‘Product'\[Product Key\])**

The first measure calculates the total numbers of product based on the field ‘**Product Key**‘.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-146-1.jpg)

**\=CALCULATE(\[CountofProduct\],CROSSFILTER(‘Product'\[Product Key\],Sales\[Product Key\],Both))**

The second measure calculates the first measure based on the filter that using **CROSSFILTER**. In the filter section, we use the **Both** parameter to establish the bidirectional relationship between **Product** table and **Sales** table based on the field ‘**Product Key**‘. Next, we export the DAX expression to a PivotTable based upon the fields of two measures.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-118-1.jpg)

The result table should be:

![](<Base64-Image-Removed>)

For customer A, the filed **CountofProduct** shows the result of three (3), indicating products A, B and C are all sold. However, according to the field **CountofProductFilter**, only one product (product A) is sold for customer A. The reason for this difference is that the first measure is based upon unidirectional relationship and it returns the total count of product name. **Customer** cannot filter through **Product**. The second measure correctly calculates the count of product names for customer A since we use bidirectional filter in our DAX expression and **Customer** can filter through **Product**.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-crossfilter/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-crossfilter/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-crossfilter/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-crossfilter/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-function-crossfilter/#0 "close")

top