# Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table

**Source:** https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table

*   July 1, 2019

Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table
==================================================================================================

Power Pivot Principles: Grouping Text Columns with New Categories Dynamically using an Input Table
==================================================================================================

2 July 2019

_Welcome back to our Power Pivot blog. Today, we discuss how to use an input Table to group text columns into new categories_

This week, we want to look up the following values: Glove, Shoe, Belt _(say)_, in a column, but these values may change.For this example, we are going to use the following text column:

![](<Base64-Image-Removed>)

What we want to do is create a column that will highlight if any one of the three values from the Lookup table are present in the Product Type column. For example, if the Product Type value is “Leather Gloves”, we would want the column to recognise that that value had “Glove” in it. If the Product Type value is “Business Shoes”, then we would want the column to recognise “Shoe”, and so on.

We have already done something similar to this in previous blogs, one involving switching between numbers and text values here and another involving the **SEARCH** and **SWITCH** functions to look through text values here.

They both involve creating a new column based on data in reference column. However, the difference here is that those two previously outlined methods are not dynamic. The end user would have to manually go into the formula for the calculated column and rewrite the formula, should the criteria change.

This time, we will have the flexibility of redefining the lookup criteria with an external table. To begin we will use the following lookup Table:

![](<Base64-Image-Removed>)

(OK, so we haven’t chosen “Belt” here, but you get the picture!)

The first DAX code we are going to write is:

\=SEARCH**(**

                FIRSTNONBLANK(

                                ‘LookupTable'\[Lookup\],

                                1

                                ),

                ‘Combined Example'\[Product Type\],

                ,

                9999

**)**

![](<Base64-Image-Removed>)

This DAX code uses the **SEARCH** and**FIRSTNONBLANK** functions, we have used the value ‘9999’ as the value to return if not found as it is extremely unlikely that we would find a text value we are looking for in the 9,999th character position. The column is only able to detect the first value in our lookup table ‘Gloves’, since we are using the **FIRSTNONBLANK** function. We need the function to iterate for each value of the lookup table.

We are going to have to use the **CONCATENATEX** function to force the function to iterate for each row:

\=CONCATENATEX(

                ‘LookupTable’,

                                                SEARCH(

                                                                FIRSTNONBLANK(

                                                                                                ‘LookupTable'\[Lookup\],

                                                                                                1

                                                                                                ),

                                                                ‘Combined Example'\[Product Type\],

                                                                ,

                                                                9999

                                                                )

                )

![](<Base64-Image-Removed>)

The **CONCATENATEX** function iterates the function to look for each value in the lookup table, Glove and Shoe.

This method enables the column to highlight when a cell value contains both Glove or Shoe. This is highlighted on the 10th row, it finds ‘Glove’ at the first character position, hence 1, and it finds ‘Shoe’ on the 11th character position, hence 11, resulting in ‘111’.

The final step is to use the **IF** function so that the function would return with the text value rather than the character position:

\=CONCATENATEX(

                ‘LookupTable’,

                                IF(

                                                SEARCH(

                                                                                FIRSTNONBLANK(

                                                                                                                ‘LookupTable'\[Lookup\],

                                                                                                                1

                                                                                                                ),

                                                                ‘Combined Example'\[Product Type\],

                                                                ,

                                                                9999

                                                                )

                                <> 9999,

                                ‘LookupTable'\[Lookup\],

                                “”

                                )

                )

![](<Base64-Image-Removed>)

The **IF** function checks if the number returned does not equal 9,999 and returns with the lookup table value.

Now we can add ‘Belt’ as criteria into the Lookup table and have the calculated column update automatically.

![](<Base64-Image-Removed>)

Updating the Lookup table and refreshing the connection will yield:

![](<Base64-Image-Removed>)

With our new column we can set up slicers to dynamically segregate our data based on text inputs. However, we’ll have more on that next week.

That’s it for this week, join us next week for more Power Pivot.

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table/#0)

[](https://sumproduct.com/blog/power-pivot-principles-grouping-text-columns-with-new-categories-dynamically-using-an-input-table/#0 "close")

top