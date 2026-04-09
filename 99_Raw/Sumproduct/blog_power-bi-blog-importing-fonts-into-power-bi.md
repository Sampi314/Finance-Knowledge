# Power BI Blog: Importing Fonts into Power BI

**Source:** https://sumproduct.com/blog/power-bi-blog-importing-fonts-into-power-bi/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Importing Fonts into Power BI

*   August 5, 2020

Power BI Blog: Importing Fonts into Power BI
============================================

Power BI Blog: Importing Fonts into Power BI
============================================

6 August 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to import fonts into Power BI._

Let’s look a simple dashboard that we’ve created in a [previous blog](https://sumproduct.com/blog/power-bi-blog-custom-button-page-navigation/)
:

![](<Base64-Image-Removed>)

Imagine that the users that we are creating this dashboard for requested that we change the font in the report to Roboto. Sure, no problem. Let’s just click on a visualisation and navigate to the **Title** option and change the font family.

![](<Base64-Image-Removed>)

To our horror, Roboto is not one of the default fonts that is included in Power BI:

![](<Base64-Image-Removed>)

No worries, we can also change the default font used in this report in the theme, maybe that will yield better results.

Navigate to the **View** tab on the Ribbon, click on the drop-down option for Themes. Then select the ‘Customize current theme’ option:

![](<Base64-Image-Removed>)

The ‘Customize theme’ dialog box will appear allowing us to select a ‘Font Family’

![](<Base64-Image-Removed>)

Bad news, the font Roboto is not here either, so what can we do? Well, we could try and force it by importing a theme with the font specified in the **JSON** file (the file format that Power BI reads to import themes).

The first step is to create a theme, we do this by clicking the ‘Save current theme’ option:

![](<Base64-Image-Removed>)

Save the theme, then use Windows Explorer to find where you saved the theme. Power BI would have saved the file as a **.json** file.

Navigate to the **JSON** file’s location, open it with notepad, or any other text editing or code editing software available:

![](<Base64-Image-Removed>)

Now we add the following code to it:

**,”visualStyles”:{“\*”:{“\*”:{“\*”:\[{“fontSize”:12,”fontFamily”:”Roboto”,”color”:{“solid”:{}}}\]}}}**

Note that this goes inside the brackets so the final code looks like this:

**{“name”:”Roboto”,**

**“visualStyles”:{“\*”:{“\*”:{“\*”:\[{“fontSize”:12,”fontFamily”:”Roboto”,”color”:{“solid”:{}}}\]}}}}**

![](<Base64-Image-Removed>)

Save the file. Go back to Power BI and back to the themes drop-down menu. This time, we select ‘Browse for themes’:

![](<Base64-Image-Removed>)

Using Windows Explorer select the **.json** file that we have just edited and open it. Power BI will load the theme and hopefully we should see this message appear:

![](<Base64-Image-Removed>)

The fonts should now have been changed to Roboto!

We can confirm this by repeating the very first step, clicking on a visualisation then going to the **Title** area and selecting the ‘Font Family’ drop-down:

![](<Base64-Image-Removed>)

That’s it for this week, come back next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-importing-fonts-into-power-bi/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-importing-fonts-into-power-bi/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-importing-fonts-into-power-bi/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-importing-fonts-into-power-bi/#0)

[](https://sumproduct.com/blog/power-bi-blog-importing-fonts-into-power-bi/#0 "close")

top