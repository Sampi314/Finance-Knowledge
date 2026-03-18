# Power BI Blog: Creating Dynamic Slicers using Field Parameters

**Source:** https://sumproduct.com/blog/power-bi-blog-creating-dynamic-slicers-using-field-parameters/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Creating Dynamic Slicers using Field Parameters

*   January 25, 2023

Power BI Blog: Creating Dynamic Slicers using Field Parameters
==============================================================

Power BI Blog: Creating Dynamic Slicers using Field Parameters
==============================================================

26 January 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at how to create dynamic slicers using field parameters._

[Recently](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-field-parameters)
, Microsoft released a public Preview of field parameters, which allowed end-users to dynamically change the measures and dimensions being analysed within a report. The initial release supported scenarios where Slicers or Filter cards could control which fields would be used in different visuals:

![](<Base64-Image-Removed>)

However, it did not support the ability for slicers to control the fields used in other slicers, also referred to as dynamic slicers. Microsoft has now removed this limitation, and you can now parameterise your slicers to support your dynamic filtering scenarios.

For example, in the report below we have three slicers: a measure picker, a dimension picker, and a dynamic slicer for filtering values. When you change the selected field for the dimension picker, not only will the main visual update but also the dynamic slicer will update as well to show the values of the selected dimension, which may be used for filtering.

![](<Base64-Image-Removed>)

Microsoft has now enabled the field parameters Preview feature by default, so you do not have to manually turn on the Preview feature in the options menu. To create a dynamic slicer using field parameter, you will need to start by adding a field parameter to a slicer. This is the slicer that we will use as the field / dimension picker for the dynamic slicer:

![](<Base64-Image-Removed>)

Next, you might want to duplicate the slicer using copy and paste. This slicer will become the dynamic slicer used for filtering values:

![](<Base64-Image-Removed>)

With the second slicer selected, you may launch the field input context menu (right-click menu) and select ‘Show values of the selected field’:

![](<Base64-Image-Removed>)

Now you have a dynamic slicer!

![](<Base64-Image-Removed>)

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-creating-dynamic-slicers-using-field-parameters/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-creating-dynamic-slicers-using-field-parameters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-creating-dynamic-slicers-using-field-parameters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-creating-dynamic-slicers-using-field-parameters/#0)

[](https://sumproduct.com/blog/power-bi-blog-creating-dynamic-slicers-using-field-parameters/#0 "close")

top