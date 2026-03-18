# Power BI Blog: Restaurant Selector

**Source:** https://sumproduct.com/blog/power-bi-blog-restaurant-selector/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Restaurant Selector

*   May 22, 2019

Power BI Blog: Restaurant Selector
==================================

Power BI Blog: Restaurant Selector
==================================

23 May 2019

_Welcome back to this week’s Power BI blog series! This week, we’re going to look at cleaning up the data we brought in last week from ‘New web table from inference’._

Last week we brought in 4 different tables of data from the TripAdvisor webpage, you can read more about that blog [here](https://sumproduct.com/blog/power-bi-blog-new-web-table-from-inference/)
.

The four different tables don’t help much on their own other than making relieving us of having to scroll through the webpage to look at restaurants.

Let’s see if we can combine them together to make something more of it.

The first step we are going to take here is to rename Table 2 to ‘Restaurants’ and the column headers:

![](<Base64-Image-Removed>)

The next step is to merge two tables based on the restaurant name so that we can see how far each restaurant is from us:

![](<Base64-Image-Removed>)

Next, we have to filter out rows with _null_ values and remove duplicate entries in our table:

![](<Base64-Image-Removed>)

We now have to split the ‘Table 1.Column4’ column by delimiter so that we can have a number value for the distance. Don’t forget to give the new columns appropriate names!

![](<Base64-Image-Removed>)

Close & Apply, and the next step is to create several simple visualisations. A table with the Restaurant Name, Pricing, District. A clustered bar chart displaying the Distance (km) by Restaurant Name. A slicer to help filter the distances and another slicer for the Prices.

![](<Base64-Image-Removed>)

We can now sort the restaurants by ascending prices, and Power BI will filter the results based on our price tolerance level and how far we are willing to travel!

Hopefully building something like this will help you decide where to go to eat next time you’re having trouble!

Tune in next time for more Power BI. See you then!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-restaurant-selector/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-restaurant-selector/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-restaurant-selector/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-restaurant-selector/#0)

[](https://sumproduct.com/blog/power-bi-blog-restaurant-selector/#0 "close")

top