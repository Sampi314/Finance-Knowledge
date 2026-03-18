# Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table – Part 2

**Source:** https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table-part-2/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table – Part 2

*   July 8, 2019

Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table – Part 2
===========================================================================================================

Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table – Part 2
===========================================================================================================

9 July 2019

_Welcome back to our Power Pivot blog. Today, we show you how use set up slicers to dynamically segregate text data based on text inputs._

Last week we showed you how to group text columns with new categories dynamically using an input table. This week, let’s expand on that concept.

Imagine we have the following data table, noting that this screenshot is not exhaustive:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-399.jpg)

We would like to be able to group the Product IDs by a new category. These categories are detailed in the following table:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-411.jpg)

In summary, if the Product ID text contains ‘Shoe’ the new column will display ‘Footwear’, and if the text contains ‘Jeans’ the new column will return with ‘Pants’, _etc._

How do we do this? Well, from our last blog, we used the following single column lookup table:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-387.jpg)

This time we can alter our lookup table and have two columns, one column for the Lookup value and the other for the category name we wish to return:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-360.jpg)

After loading both tables into Power Pivot, we create a calculated column with the following code:

\=CONCATENATEX(

            ‘LookupTable’,

                    IF(

                           SEARCH(

                                   FIRSTNONBLANK(                                                                                                                     ‘LookupTable'\[Lookup\],

                                                 1

                                                 ),

                                 ‘DataTable'\[Product Type\],

                                 ,

                                 9999

                                 )

                      <> 9999,

                      ‘LookupTable'\[Category\],

                      “”

                      )

           )

This code is very similar to the code we used last week, with one key difference. Instead of returning with the **‘LookupTable'\[Lookup\]**, we change it to **‘LookupTable'\[Category\]**. This way, the column will be populated with the new category that we wish to assign to each row:

![](<Base64-Image-Removed>)

We will also have to create a **Sales** column that multiplies the **Price** by the **Quantity**:

**\=’DataTable'\[Price\]\*’DataTable'\[Quantity\]**

![](<Base64-Image-Removed>)

We can now create the following PivotChart:

![](<Base64-Image-Removed>)

The next step is to create a Slicer for our new **Category** column:

![](<Base64-Image-Removed>)

We can now filter our graph to display different categories of our data!

The best part is that if we wish to change the categories or lookup values all we have to do is change the values in our lookup table, refresh the links in Power Pivot and our chart will update accordingly.

For example, updating our lookup table to:

![](<Base64-Image-Removed>)

and refreshing the links in Power Pivot, our PivotChart will be updated as follows:

![](<Base64-Image-Removed>)

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table-part-2/#0)

[](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table-part-2/#0 "close")

top