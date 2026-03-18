# Power Pivot Principles: Using the ALLNOBLANKROW Function to Calculate The Percentage of Total

**Source:** https://sumproduct.com/blog/power-pivot-principles-using-the-allnoblankrow-function-to-calculate-the-percentage-of-total/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Using the ALLNOBLANKROW Function to Calculate The Percentage of Total

*   October 12, 2020

Power Pivot Principles: Using the ALLNOBLANKROW Function to Calculate The Percentage of Total
=============================================================================================

Power Pivot Principles: Using the ALLNOBLANKROW Function to Calculate The Percentage of Total
=============================================================================================

13 October 2020

_Welcome back to the Power Pivot Principles blog. This week, we consider how to calculate the percentage of a total using the ALLNOBLANKROW._

[Last week](https://www.sumproduct.com/)
, we introduced the **ALLNOBLANKROW** function which returns all the rows except for the blank rows in a table, or all the values in a column, ignoring any filters that may have been applied. From the previous sample dataset let’s revisit **Store\_ID**, which lists five store IDs and their respective names,

![](<Base64-Image-Removed>)

and the **Car\_Sales\_Count** table which records the sales of car by **Date**, **Store ID** and **Sales Person**.

![](<Base64-Image-Removed>)

The above two tables are already loaded into the Power Pivot Data Model and a relationship was previously set up between them, by connecting the **Store ID** fields in the two tables, _viz._

![](<Base64-Image-Removed>)

We counted rows using the [**A**](https://www.sumproduct.com/)
**[LLNOBLANKROW](https://www.sumproduct.com/)
**, **[ALL](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-all)
**, **[VALUES](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-values-function)
** and **[DISTINCT](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-function)
**functions when there is a blank row in the PivotTable:

![](<Base64-Image-Removed>)

Now, we want to see the share of **Sales** by store. We create a measure by nesting the **DISTINCT** and **ALLNOBLANKROW** functions inside the **COUNTROWS** function, _viz._

**% #Store Distinct:= DIVIDE(COUNTROWS(DISTINCT(Car\_Sales\_Count)), COUNTROWS(ALLNOBLANKROW(Car\_Sales\_Count)))**

![](<Base64-Image-Removed>)

The formula works well, but we can try making it shorter by using the **VALUES** and **ALL** functions instead:

**% #Store Values:= DIVIDE(COUNTROWS(VALUES(Car\_Sales\_Count)), COUNTROWS(ALL(Car\_Sales\_Count)))**

This measure returns the same results:

![](<Base64-Image-Removed>)

Still, the **% #Store Values** measure is not the shortest (which mean most efficient!) way to get the result. We can trim it down by keeping the **ALL** function in the denominator and nesting no other function inside the **COUNTROWS** function in the numerator:

**% #Store:= DIVIDE(COUNTROWS(Car\_Sales\_Count),COUNTROWS(ALL(Car\_Sales\_Count)))**

We get the same results in three different measures:

![](<Base64-Image-Removed>)

As always, simplicity is best!

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-using-the-allnoblankrow-function-to-calculate-the-percentage-of-total/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-using-the-allnoblankrow-function-to-calculate-the-percentage-of-total/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-using-the-allnoblankrow-function-to-calculate-the-percentage-of-total/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-using-the-allnoblankrow-function-to-calculate-the-percentage-of-total/#0)

[](https://sumproduct.com/blog/power-pivot-principles-using-the-allnoblankrow-function-to-calculate-the-percentage-of-total/#0 "close")

top