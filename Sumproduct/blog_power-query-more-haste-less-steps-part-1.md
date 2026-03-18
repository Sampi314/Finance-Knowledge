# Power Query: More Haste Less Steps Part 1

**Source:** https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: More Haste Less Steps Part 1

*   April 19, 2022

Power Query: More Haste Less Steps Part 1
=========================================

Power Query: More Haste Less Steps Part 1
=========================================

20 April 2022

_Welcome to our Power Query blog. This week, I look a query with too many steps._

I have created a **Dates** query:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-40-1.jpg)

I have deliberately gone the long way round to create this query! Ignoring the first three \[3\] steps, it has taken me twelve \[12\] steps to achieve my goal.

The first task was to create a **Month Name** column with a short month name. This takes up six \[6\] steps. First, I duplicate the Date Column, creating a ‘Duplicated Column’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-54-1.jpg)

Then I use the Date transformation on the Transform tab to convert the new column to hold the ‘Name of Month’, creating an ‘Extracted Month Name’ step.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-40-1.jpg)

Next, I used ‘Split Column’ on the Transform tab to split the column ‘By Positions’, creating a ‘Split Column by Position’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-35-1.jpg)

This automatically generated a ‘Changed Type1’ step. I then had to delete the unwanted column, creating a ‘Removed Column’ step and rename the one I wanted to keep to ‘month’, creating a ‘Renamed Column1’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-27-1.jpg)

I then took another five \[5\] steps to create a ‘Quarter’ column. I duplicated the Date column again (Duplicated Column1) and used the Date transformation again, this time to get the Quarter, creating a ‘Calculated Quarter’ step.

I then decided I wanted to have a ‘Q’ in front of it, so I converted the column to data type text using the dropdown from the data type icon, creating a ‘Changed Type2’ step:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-22-1.jpg)

I then added a ‘Custom Column’ from the Home tab to add the ‘Q’ (‘Added Custom’):

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-19-1.jpg)

Then I deleted the **Date – Copy** column which held the original quarter value (‘Removed Column1’) and decided to rename the **month** column to ‘Month Name’ (‘Renamed Column2’).

![](<Base64-Image-Removed>)

Next time I’ll have a look at how this number of steps may be reduced whilst still using the User Interface (UI). How many steps do you think I will need?

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/#0)

[](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-1/#0 "close")

top