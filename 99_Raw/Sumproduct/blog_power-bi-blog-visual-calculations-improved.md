# Power BI Blog: Visual Calculations Improved

**Source:** https://sumproduct.com/blog/power-bi-blog-visual-calculations-improved/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Visual Calculations Improved

*   January 8, 2025

Power BI Blog: Visual Calculations Improved
===========================================

Power BI Blog: Visual Calculations Improved
===========================================

9 January 2025

_Welcome back to this week’s edition of the Power BI blog series. This week, we review recent updates to visual calculations._

**_Combination (“Combo”) Charts are now supported_**

You can now use visual calculations in Combo charts, such as the Line and Clustered Column chart, just like you could in the other chart types. For example, here is a visual calculation returning the moving average over three quarters:

![](<Base64-Image-Removed>)

The visual calculation used here on the Line **y**\-axis is:

**ThreeQuarterMovingAverage = MOVINGAVERAGE(\[Sales Amount\], 3)**

**_Field Parameters are now supported_**

Power BI has now enabled the use of visual calculations with field parameters. You may add a visual calculation to a visual that contains a field parameter and vice versa.

Field parameters may be used to quickly switch around what is shown in a visual. For example, you can create a field parameter to enable your users to decide which attributes of a dimension to show. In this example, a field parameter called **Product Attribute** can be used to determine what the ‘Percent of grand total’ visual calculation returns:

![](<Base64-Image-Removed>)

The Percent of grand total visual calculation is defined using the template as:

**Percent of grand total = DIVIDE(\[Sales Amount\], COLLAPSEALL(\[Sales  \
Amount\], ROWS))**

Since the Percent of grand total visual calculation used here refers to **ROWS** as its axis, it will update and reflect the correct values when another product attribute is picked:

![](<Base64-Image-Removed>)

**_Faster way to add a templated visual calculation_**

You may now add a templated visual calculation with fewer clicks by clicking on the bottom part of the ‘New visual calculation’ Ribbon button to see a menu that includes the templates. Clicking on a template will open the visual calculation mode, where you may fill in the template and add your visual calculation.

![](<Base64-Image-Removed>)

If you want to create a new visual calculation without using a template, either select the top part of the ‘New visual calculation’ button or choose ‘Custom’ from the ‘Visual calculation’ template menu shown above.

That’s it for this week. In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-visual-calculations-improved/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-visual-calculations-improved/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-visual-calculations-improved/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-visual-calculations-improved/#0)

[](https://sumproduct.com/blog/power-bi-blog-visual-calculations-improved/#0 "close")

top