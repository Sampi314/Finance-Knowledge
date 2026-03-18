# Power BI Blog: Summarising the Top N Number of Cities in a Dataset

**Source:** https://sumproduct.com/blog/power-bi-blog-summarising-the-top-n-number-of-cities-in-a-dataset/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Summarising the Top N Number of Cities in a Dataset

*   September 9, 2020

Power BI Blog: Summarising the Top N Number of Cities in a Dataset
==================================================================

Power BI Blog: Summarising the Top N Number of Cities in a Dataset
==================================================================

10 September 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to parameterise the summarisation of the top number of Cities in a dataset._

A while ago we talked about the [TOPN](https://sumproduct.com/blog/power-bi-blog-summarising-the-top-two-countries-in-a-dataset/)
 function, and we used it to summarise the top two countries in a dataset. This week, we want to look at summarising the top cities in the same dataset, where we can flex the number we wish to select.

The DAX code for the measure that will summarise the top two (2) cities in our dataset is:

Sales of Top 2 Cities =

CALCULATE(\[Total Sales\],

TOPN(2,

Values(Geography\[City\]),

\[Total Sales\],

DESC

)

)

If we want to summarise more than just the top two cities we can change the ‘2’ in the measure to a greater number, _say_ ‘3’.

Sales of Top 3 Cities =

CALCULATE(\[Total Sales\],

TOPN(3,

Values(Geography\[City\]),

\[Total Sales\],

DESC

)

)

![](<Base64-Image-Removed>)

But what if your end user is fickle and wants to be able to change the number of cities to summarise on the fly? We can parameterise the selection by using a disconnected table, meaning this table should have no relationships with the other tables in our dataset. You can read more about disconnected tables [here](https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/)
.

We can create the following table in Excel and load it into Power BI:

![](<Base64-Image-Removed>)

Now that we have the **Selection** table loaded into Power BI we can create a measure to pull out the number of cities that we want to summarise by.

Selection = IF(ISFILTERED(Selection\[Selection\]),MAX(Selection\[Selection\]),1)

If you have read the blog on [disconnected tables](https://sumproduct.com/blog/power-pivot-principles-disconnected-tables-and-exchange-rates/)
, we used a simple **MAX** approach there. However, I prefer to use an **ISFILTERED** condition. This is so that I can delineate which value to use in the scenario where no selection has been made.

The next step is to create a slicer for the selection.

![](<Base64-Image-Removed>)

Now we can add the **Selection** measure to our **Sales of Top 3 Cities** measure to parameterise it.

Sales of Top Selected Cities =

CALCULATE(\[Total Sales\],

TOPN(\[Selection\],

Values(Geography\[City\]),

\[Total Sales\],

DESC

)  
)

Our report should now look like this:

![](<Base64-Image-Removed>)

We can select a number and Power BI will update the calculations accordingly and return with the updated sales of the top **N** number of cities!

![](<Base64-Image-Removed>)

That’s it for this week, come back next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-summarising-the-top-n-number-of-cities-in-a-dataset/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-summarising-the-top-n-number-of-cities-in-a-dataset/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-summarising-the-top-n-number-of-cities-in-a-dataset/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-summarising-the-top-n-number-of-cities-in-a-dataset/#0)

[](https://sumproduct.com/blog/power-bi-blog-summarising-the-top-n-number-of-cities-in-a-dataset/#0 "close")

top