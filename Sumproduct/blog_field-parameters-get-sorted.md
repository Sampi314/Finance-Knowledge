# Power BI Blog: Field Parameters Get Sorted

**Source:** https://sumproduct.com/blog/field-parameters-get-sorted/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Field Parameters Get Sorted

*   June 12, 2025

Power BI Blog: Field Parameters Get Sorted
==========================================

_Welcome back to this week’s edition of the Power BI blog series.  This week we look at sorting field parameter visuals._

Field parameters have proved to be a great way to provide flexibility in reports.  However, there have been issues.  One of the problems has to do with how changes in the field selected by the field parameter resets the sorting of a visual.  Microsoft has recently resolved this by persisting in the sorting even if you change the field selected by the field parameter.

For instance, a visual can use a field parameter to display ‘Total Sales’ based upon the selected field.  In this example, the selected field is Category.  Notice that we have sorted the visual by Category ascending:

![](<Base64-Image-Removed>)

Now let’s switch the field parameter to Class instead of Category.  You can compare and contrast the old and new behaviour as follows:

![](<Base64-Image-Removed>)

As soon as you switch the field selected by the field parameter to something else (in our example Class), the sort order of the visual would change and your visual would be sorted by ‘Total Sales’ descending (which is the default sort order for this type of visual).  Starting with this update, that is no longer the case, and the sort order will persist and the visual is still sorted by the field selected by the field parameter even after it is switched.

This is one of the key improvements to field parameters.  More updates are to follow, apparently.  We look forward to them with interest.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.      

*   [Log in](https://sumproduct.com/blog/field-parameters-get-sorted/#0)
    
*   [Register](https://sumproduct.com/blog/field-parameters-get-sorted/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/field-parameters-get-sorted/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/field-parameters-get-sorted/#0)

[](https://sumproduct.com/blog/field-parameters-get-sorted/#0 "close")

top