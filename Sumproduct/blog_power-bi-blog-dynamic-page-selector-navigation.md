# Power BI Blog: Dynamic Page Selector Navigation

**Source:** https://sumproduct.com/blog/power-bi-blog-dynamic-page-selector-navigation/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dynamic Page Selector Navigation

*   July 22, 2020

Power BI Blog: Dynamic Page Selector Navigation
===============================================

Power BI Blog: Dynamic Page Selector Navigation
===============================================

23 July 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to create a dynamic page selector for your reports._

Last week, we looked at creating button navigators for our end users to navigate through our report pages.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-176-scaled-1.jpg)

This involved creating unique buttons on each page and manually assigning where each button would take you. This would be easy on a report with four pages, but it would soon get rather tedious on reports with eight or more pages.

Lucky for us there is another way to do this.

Assume for this example that we have the following report consisting of six pages for six different countries.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-164-1.jpg)

As you would imagine, creating buttons for all six pages would prove to be rather tedious. To create an alternative way to navigate through the report, we must create a table with the names of all the different pages in our report. In this example, I have chosen to create the table in Excel. Of course, you can create the table from any source you wish. Please note that the **CountryName** table has to contain the exact names of each page, otherwise the selection will not work using this method.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-158-1.jpg)

Once that is done, load the table into Power BI. We now have a **CountryName** table:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-140-1.jpg)

The trick here is to create a slicer that contains the **CountryName** field.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-119-1.jpg)

I have removed the Slicer Heading and elected to give the slicer the fitting Title of ‘**Page Selector**‘.

Be sure to toggle ‘Single Select’ to On, and I have also changed the slicer to a drop-down list to keep it compact.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-99-1.jpg)

The drop-down slicer alone is not able navigate through the pages of the report. The slicer serves as a selection tool for the user to pick the page they want to navigate to. We will need a widget of some sort for the user to click, so that Power BI will know when the user has made their selection and is ready to navigate to the selected page.

I decided to use the arrow icon as my widget. After creating the image, select it and navigate to the Action area in the Visualizations panel. Toggle ‘On’ for the Action option, then select ‘Page navigation’ as Type.

![](<Base64-Image-Removed>)

Then click on the ‘**fx**‘ button next to the Destination input field. This will bring up the Destination dialog box. Here, we will select the ‘**First Country Name**‘ field for the ‘Based on field’ option and ‘First’ for Summarization.

![](<Base64-Image-Removed>)

Position the arrow (or widget) appropriately close to the ‘Page Selector’ and copy the set onto every page in the report.

Now users will be able to select which page they wish to navigate to, click on the arrow and Power BI will navigate to the selected page!

![](<Base64-Image-Removed>)

That’s it for this week, come back next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dynamic-page-selector-navigation/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dynamic-page-selector-navigation/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dynamic-page-selector-navigation/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dynamic-page-selector-navigation/#0)

[](https://sumproduct.com/blog/power-bi-blog-dynamic-page-selector-navigation/#0 "close")

top