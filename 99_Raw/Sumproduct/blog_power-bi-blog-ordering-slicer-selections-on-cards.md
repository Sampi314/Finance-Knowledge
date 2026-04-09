# Power BI Blog: Ordering Slicer Selections on Cards

**Source:** https://sumproduct.com/blog/power-bi-blog-ordering-slicer-selections-on-cards/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Ordering Slicer Selections on Cards

*   September 30, 2020

Power BI Blog: Ordering Slicer Selections on Cards
==================================================

Power BI Blog: Ordering Slicer Selections on Cards
==================================================

1 October 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to order slicer selections that are displayed in a card in Power BI._

This week we are going to pick up where we left off [two weeks ago](https://sumproduct.com/blog/power-bi-blog-displaying-multiple-slicer-selections-on-cards/)
. As a recap, we created a measure that can display multiple countries on a card based upon slicer selection:

**List of Countries =**

    **CONCATENATEX(**

        **VALUES(Geography\[Country\]),**

        **Geography\[Country\],**

        **“, “**

    **)**

The measure returns with the following results when displayed on a card visualisation:

![](<Base64-Image-Removed>)

Taking a closer look at our title card, ‘Germany, France, United Kingdom’ doesn’t seem to be displayed in any particular order.

What if we want to order the countries by alphabetical order?

The **CONCATENATEX** function actually accepts order parameters:

**CONCATENATEX(table, expression, \[delimiter\], \[OrderBy\_Expression1\], \[Order1\], …)**

Let me explain the parameters:

*   The **OrderBy\_Expression1** parameter is optional, but it is the field or expression used to order the table
*   The **Order1** parameter accepts either **ASC** or **DESC**, for ascending or descending, respectively.

Now with the fourth and fifth parameters in mind, we can make the following adjustments to the measure:

**List of countries alphabetical =**

    **CONCATENATEX(**

        **VALUES(Geography\[Country\]),**

        **Geography\[Country\],**

        **“, “,**

        **Geography\[Country\],**

        **ASC**

    **)**

In the new measure, we have placed **Geography\[Country\]** as the **OrderBy\_Expression1**, which means we want to order the results by that field. We then have **ASC** as the **Order1** parameter, which means that we want the countries to be order in ascending order.

![](<Base64-Image-Removed>)

As you can see, the countries are now order in alphabetical order.

We can even order the countries by an expression, let’s try ordering them by the **\[Total Sales\]**

**List of countries ordered by total sales =**

    **CONCATENATEX(**

        **VALUES(Geography\[Country\]),**

        **Geography\[Country\],**

        **“, “,**

        **\[Total Sales\],**

        **DESC**

    **)** 

![](<Base64-Image-Removed>)

That’s it for this week! Come back next week for more on Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-ordering-slicer-selections-on-cards/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-ordering-slicer-selections-on-cards/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-ordering-slicer-selections-on-cards/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-ordering-slicer-selections-on-cards/#0)

[](https://sumproduct.com/blog/power-bi-blog-ordering-slicer-selections-on-cards/#0 "close")

top