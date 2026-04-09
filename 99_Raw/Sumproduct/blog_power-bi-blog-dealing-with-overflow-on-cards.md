# Power BI Blog: Dealing with Overflow on Cards

**Source:** https://sumproduct.com/blog/power-bi-blog-dealing-with-overflow-on-cards/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dealing with Overflow on Cards

*   October 7, 2020

Power BI Blog: Dealing with Overflow on Cards
=============================================

Power BI Blog: Dealing with Overflow on Cards
=============================================

8 October 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to deal with an overflow of slicer selections on card visualisations._

This week, we are going to pick up where we left off [last week](https://sumproduct.com/blog/power-bi-blog-ordering-slicer-selections-on-cards/)
. As a recap, we created a measure that orders the countries by the **Total Sales** expression:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-129-1.jpg)

But what if the user selects more countries than the card can display neatly?

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-119-1.jpg)

Judging from the current size of the card, it looks like it can comfortably display three countries. Therefore, we will limit the total number of countries to show in this card to three countries.

Before we create a measure that will do that, let’s take a look at the measure that is being displayed on the card presently:

**List of countries ordered by total sales =**

    **CONCATENATEX(**

        **VALUES(Geography\[Country\]),**

        **Geography\[Country\],**

        **“, “,**

        **\[Total Sales\],**

        **DESC**

    **)**

It works fine on its own, however we want the measure to return with a different result when more than three countries are selected. In this case, we should use an **IF** function to distinguish between two actions when a criterion is met.

The measure that I have written might seem a little complicated. I have split the measure up into two halves in an attempt break it down to explain it.

The first ‘half’ of the measure is as follows:

**IF(**

    **DISTINCTCOUNT(**

        **Geography\[Country\]) <= 3,**

            **CONCATENATEX(**

                **Values(Geography\[Country\]),**

                **Geography\[Country\],**

                **“, “,**

                **\[Total Sales\],**

                **DESC**

            **),**

It reads, if the distinct count of the **Country** field in the **Geography** table is less than or equal to three (3), then evaluate using the **CONCATENATEX** function.

In this scenario, we use the **DISTINCTCOUNT** to determine the total number of selections made in the **Country** slicer. With the following selection,

![](<Base64-Image-Removed>)

it will evaluate to four (4).

Now, for the other ‘half’ of the measure, that will be evaluated when the total number of countries selected in the slicer is strictly greater than three (3).

    **CONCATENATE(**

        **CONCATENATEX(**

        **TOPN(**

            **3,**

            **Values(Geography\[Country\])**

            **),**

        **Geography\[Country\],**

        **“, “,**

        **\[Total Sales\],**

        **DESC**

        **),**

    **“, etc…”**

    **)**

Here we use the **TOPN** function to determine the total number of countries to be concatenated. You can read more about the **TOPN** function [here](https://sumproduct.com/blog/power-bi-blog-summarising-the-top-two-countries-in-a-dataset/)
.

Moving up a level in the measure, we then have a similar layout for the **CONCATENATEX** function where:

*   the table is determined from the **TOPN** function
*   the expression is **Geography\[Country\]**
*   the delimiter is “, “
*   the **orderby\_expression** is **\[Total Sales\]**
*   the order is set to **DESC** or descending.

Moving one more level up in the measure, we have to nest the **CONCATENATEX** function with a **CONCATENATE** function to include an “, _etc_…” at the end of the string.

When we put both parts of the measure together we get this:

List of Countries Overflow =

**IF(**

    **DISTINCTCOUNT(**

        **Geography\[Country\]) <= 3,**

            **CONCATENATEX(**

                **Values(Geography\[Country\]),**

                **Geography\[Country\],**

                **“, “,**

                **\[Total Sales\],**

                **DESC**

            **),**

    **CONCATENATE(**

        **CONCATENATEX(**

        **TOPN(**

            **3,**

            **Values(Geography\[Country\])**

            **),**

        **Geography\[Country\],**

        **“, “,**

        **\[Total Sales\],**

        **DESC**

        **),**

    **“, etc…”**

    **)**

**)**

Placing this measure onto a card visualisation should get this result:

![](<Base64-Image-Removed>)

There we have it, how to manage overflow in cards displaying slicer selections.

That’s it for this week! Come back next week for more on Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dealing-with-overflow-on-cards/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dealing-with-overflow-on-cards/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dealing-with-overflow-on-cards/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dealing-with-overflow-on-cards/#0)

[](https://sumproduct.com/blog/power-bi-blog-dealing-with-overflow-on-cards/#0 "close")

top