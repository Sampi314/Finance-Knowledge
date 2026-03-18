# Power BI Blog: Floor Plan

**Source:** https://sumproduct.com/blog/power-bi-blog-floor-plan/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Floor Plan

*   July 24, 2019

Power BI Blog: Floor Plan
=========================

Power BI Blog: Floor Plan
=========================

25 July 2019

_Welcome back to this week’s Power BI blog series. This week, we are as far removed from financial modelling as we’ll ever be: we’re going to create a floor plan._

Let’s assume you manage an exhibition centre and you are planning for an upcoming exhibition. You have a floor plan of the centre and you want to see which are the most visited areas so that you can set their hire rates. With the traffic data in hand, you can do it with a standard Bar Chart. However, what if you want to check the spatial correlation between each area or if you want to explain the fact that the areas nearer the entrance are the most visited ones?

Synoptic Panel designed by OKViz is the tool for this kind of analysis and presentation. This is a custom visual for Power BI that allows you to present one or more images (called maps, but not necessarily geographical maps), assigning a meaning to arbitrary parts of them (called areas). Synoptic Panel allows you to highlight and colour these areas dynamically and display several information over them.

Synoptic Panel accepts and displays SVG files only, but you can transform your PNG, JPG or JPEG files using their [Synoptic Designer](https://synoptic.design/)
, or you can choose one from their library:

![](<Base64-Image-Removed>)

Luckily, I found a ‘Generic Store’ model which suits my need. I want to edit a few points on the graphic so I click on my selection and choose ‘Edit in Designer’:

![](<Base64-Image-Removed>)

In here, I am able to add, remove or rename my areas to match my data.

![](<Base64-Image-Removed>)

Upon completing my changes, I select ‘Export to Power BI’, in the pop-up dialog. Then, I right-click on my floor plan and choose ‘Save Image as’ in order to give it a name to store in my local directory.

![](<Base64-Image-Removed>)

In Power BI, I first load my data which tracks traffic by floor areas. It’s worth noting that the area name in my design should match exactly the area name in my data.

![](<Base64-Image-Removed>)

Then, in Power BI, I import ‘Synoptic Panel by OKViz’ from ‘Marketplace’:

![](<Base64-Image-Removed>)

In Report view, I drag ‘Area’ to ‘Category’ field and ‘Traffic’ to ‘Measure’ field:

![](<Base64-Image-Removed>)

There is one more step I need to do before my visual gets displayed: importing my map. In the visual area, I click ‘Local maps’:

![](<Base64-Image-Removed>)

I navigate to the SVG file, which I saved from the design page earlier, and open it in Power BI:

![](<Base64-Image-Removed>)

My initial visual would look like this:

![](<Base64-Image-Removed>)

There are common areas with no data of traffic, which are shown black on the floor plan. Hence, I go to Format mode and under ‘General’, I switch ‘Unmatched areas’ to Off.

![](<Base64-Image-Removed>)

Now, my visual will look cleaner. However, colour visuals are uniform, from which I am not able to tell the difference in traffic among areas:

![](<Base64-Image-Removed>)

To solve this, I go to Format mode. Under ‘States’ I turn it On, and I put ‘>=’ to ‘Comparison’ box, where I will rank my data into different levels of traffic:

![](<Base64-Image-Removed>)

Dragging down, I enter traffic levels and select State’s colour, with the darker the colour, the more crowded the area:

![](<Base64-Image-Removed>)

To make it more transparent, I go to ‘Data labels’, turn it On and let it display ‘Data value’ in the ‘Middle’ of each area:

![](<Base64-Image-Removed>)

Last but not least, I format the title for my visual under ‘Title’ options:

![](<Base64-Image-Removed>)

Finally, I have a floor plan ready for a sales pitch!

![](<Base64-Image-Removed>)

That’s it for this week, check back next week for more Power BI tips.

In the meantime, please remember we offer training in Power BI which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-floor-plan/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-floor-plan/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-floor-plan/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-floor-plan/#0)

[](https://sumproduct.com/blog/power-bi-blog-floor-plan/#0 "close")

top