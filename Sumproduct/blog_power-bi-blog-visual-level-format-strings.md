# Power BI Blog: Visual Level Format Strings

**Source:** https://sumproduct.com/blog/power-bi-blog-visual-level-format-strings/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Visual Level Format Strings

*   September 18, 2024

Power BI Blog: Visual Level Format Strings
==========================================

Power BI Blog: Visual Level Format Strings
==========================================

19 September 2024

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at one of the latest features in Preview, visual level format strings._

Visual level format strings provide you with more options to configure formatting in Power BI. Originally built for visual calculations, the core ability that visual-level format strings provide is the ability to format visual calculations. Since visual calculations are not in the model, you could not format them, unless you were using them in data labels or in specific parts of the new card and new slicer visuals. With visual level format strings, you can.

![](https://sumproduct.com/wp-content/uploads/2025/05/dcb0a1d33b09ad6ddd10df72c7246c92-1.jpg)

However, visual level format strings are useful even without using visual calculations. With the introduction of visual-level format strings, Power BI now has three \[3\] levels for format strings:

1.  **Model.** You can set a format string for columns and measures in the model. Anywhere you use that column or measure the format string will be applied, unless it’s overridden by a visual or element level format string
2.  **Visual.** This is the update. You may set format strings on any column, measure or visual calculation that is on your visual, even if they already had a format string. In that case, the model level format string will be overridden, and the visual level format string is used
3.  **Element.** You can set a format string for data labels and for specific elements of the new card and the new slicer visuals. This level will be expanded to include much more in the future. Any format string you set here will override the format string set on the visual and model level.

These levels are hierarchical, with the model level being the lowest level and the element level the highest. A format string defined on a column, measure or visual calculation on a higher-level override what was defined on a lower level.

Since visual calculations are not in the model, they cannot have a format string set on the model level but can on the visual or element level. Measures and columns can have format strings on all three levels:

![](<Base64-Image-Removed>)

The image below summarizes this and shows that higher level format strings override lower-level format strings:

![](<Base64-Image-Removed>)

Let’s look at an example using a measure.

Assume we have a **Profit** measure in our model, which is set to a decimal number format. To do this, you might have set the formatting for this measure using the Ribbon:

![](<Base64-Image-Removed>)

Alternatively, you could have made the same selections in the Properties pane for the measure in the Model view or entered the following custom formatting code:

![](<Base64-Image-Removed>)

If you put this measure on a visual it now returns a decimal number, as expected:

![](<Base64-Image-Removed>)

However, on a particular visual you want that measure to be formatted as a whole number. You can now do that by setting the format code on the visual level by opening the Format pane for that visual and the Data format options found there under General:

![](<Base64-Image-Removed>)

Now that same measure shows as a whole number, but just on that visual:

![](<Base64-Image-Removed>)

Further, you might want to use a scientific notation for that measure but only in the data label on a particular visual. No problem; you set the format code on the data label for that measure:

![](<Base64-Image-Removed>)

Now, the total shows in scientific notation, but only in the data label and not in other places (such as the ToolTip as shown below). Notice how the element level format is used in the data label but the visual or model level format string is still used for the other elements in the same visual.

![](<Base64-Image-Removed>)

For visual calculations the same principle applies but of course without the model level. For example, if you have a visual calculation that returns a percentage, you can now format it as such using the ‘Data Format’ options in the General on the visual in the Format pane:

![](<Base64-Image-Removed>)

The ability to set visual level format strings makes it much easier to get the exact formatting you need for your visualisations. However, this is only the first iteration of the visual level format strings. Microsoft is planning to add the settings you’re used to for the model level format strings to the visual level soon.

Since visual level format strings are introduced as part of the visual calculations Preview, you will need to turn on the visual calculations Preview to use them. To do that, go to **Options and Settings -> Options -> Preview features**. Select ‘Visual calculations’ and then OK. Visual calculations and visual level format strings are enabled after Power BI Desktop is restarted.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-visual-level-format-strings/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-visual-level-format-strings/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-visual-level-format-strings/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-visual-level-format-strings/#0)

[](https://sumproduct.com/blog/power-bi-blog-visual-level-format-strings/#0 "close")

top