# Power BI Blog: Dynamic Headers

**Source:** https://sumproduct.com/blog/power-bi-blog-dynamic-headers/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dynamic Headers

*   June 16, 2021

Power BI Blog: Dynamic Headers
==============================

Power BI Blog: Dynamic Headers
==============================

17 June 2021

Welcome back to this week’s edition of the Power BI blog series. This week, we will look at dynamic titles, and how to create titles with multiple linked values.

In the past, we have looked at how to create a dynamic heading based on a [slicer selection](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dynamic-headings-based-on-slicer-selection)
. In today’s article, we’re going to see how we can add multiple selected items to a heading.

In today’s example, we’re going to create a simple chart that looks at Sales broken down by specified countries. We have a slicer that we can use to filter our data.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-177.jpg)

Now, we want to create a heading. If we were to use the code that we had previously, we would just end up with the first non-blank value, which is Australia in this case:

**IF(  
**  
**ISFILTERED(CountryList\[EnglishCountryRegionName\]),**

**“Selected Country: ” & FIRSTNONBLANK(CountryList\[EnglishCountryRegionName\],1),**

**“No Country Selected”**

**)**

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-234.jpg)

This clearly isn’t going to work – FIRSTNONBLANK effectively aggregates our three selected options, but only chooses the first of the list. Instead, we need to use an aggregation that combines our results. We can use CONCATENATEX to do this:

**List of Countries = CONCATENATEX(CountryList,CountryList\[EnglishCountryRegionName\],” / “)**

![](<Base64-Image-Removed>)

CONCATENATEX gives us the ability to create a string by combing values together. Importantly, it also allows us to specify the delimiter that we want to insert between the different values. We also have the ability to specify a sort order – by default, it will use alphabetical order of the values we’re using, but we can link it back to other measures, such as our Total Sales measure:

**List of Countries = CONCATENATEX(CountryList,CountryList\[EnglishCountryRegionName\],” / “,\[Total Sales\],DESC)**

All we need to do now is drop the result into a Card visual, pop in the measure, and line up our results:

![](<Base64-Image-Removed>)

There we go – a neat way to display multiple options from a Slicer.

In the meantime, please remember we offer training in Power BI which you can find out more about here. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dynamic-headers/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dynamic-headers/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dynamic-headers/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dynamic-headers/#0)

[](https://sumproduct.com/blog/power-bi-blog-dynamic-headers/#0 "close")

top