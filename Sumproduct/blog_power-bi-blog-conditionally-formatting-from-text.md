# Power BI Blog: Conditionally Formatting from Text

**Source:** https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-from-text/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Conditionally Formatting from Text

*   June 17, 2020

Power BI Blog: Conditionally Formatting from Text
=================================================

Power BI Blog: Conditionally Formatting from Text
=================================================

18 June 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to apply conditional formatting to field values, based upon rules derived from text._

Imagine that we have superiors who have requested to see our field values colour coded as text values in Power BI. However, looking at the conditional formatting options in Power BI there does not seem to be any straightforward way to apply logical conditional formatting based upon text values:

![](<Base64-Image-Removed>)

Let us see what we can do here. We will be using the following dataset for this example:

![](<Base64-Image-Removed>)

From here, we may create the following Matrix visualisation in Power BI:

![](<Base64-Image-Removed>)

Our commander wants to see this data colour coded based upon the military division _(say)_. How do we go about that? Well, we can create a measure called **ColourCode** (the name of this measure does not matter, you can pick any name you want), which looks at the text values and assigns a number to it, _viz._

ColourCode =

VAR Division = SELECTEDVALUE(FoodRations\[Division\])

RETURN

SWITCH(TRUE(),

Division = “Air Force”, 1,

Division = “Infantry”, 2,

Division = “Navy”, 3)

In our measure, we use a variable or **VAR** and the **SWITCH** function to lookup the **Division**, and then assign a value to that division. With that measure created, we can then click on the visualisation and select the Format tab, located below the Visualisations pane, to click on ‘Conditional formatting’:

![](<Base64-Image-Removed>)

The default conditional format is set to a colour scale, which is not what we want. Let’s click on the ‘Advanced controls’ option instead.

![](<Base64-Image-Removed>)

From here, we want to make the following changes:

1.  Change ‘Format by’ to Rules
2.  Change ‘Based on field’ to **ColourCode** (the measure we created earlier)
3.  Add two new rules
4.  Change ‘If value’ in each rule to **is**
5.  Toggle the input type for each rule to **Number**
6.  Apply the corresponding colour to each number 1 to 3 (this depends on the **ColourCode** measure that we created earlier)
7.  Finally assign the corresponding colour.

For our example, we have selected light blue for ‘Air Force’, green for Infantry, and navy blue for Navy (how original).

![](<Base64-Image-Removed>)

Our visualisation should look like this now:

![](<Base64-Image-Removed>)

There we have it, how to apply colour coding to fields based upon text information!

That’s it for this week, come back next week for more on Power BI.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-from-text/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-from-text/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-from-text/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-from-text/#0)

[](https://sumproduct.com/blog/power-bi-blog-conditionally-formatting-from-text/#0 "close")

top