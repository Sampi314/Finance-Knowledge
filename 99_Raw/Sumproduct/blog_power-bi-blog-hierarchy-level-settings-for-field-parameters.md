# Power BI Blog: Hierarchy Level Settings for Field Parameters

**Source:** https://sumproduct.com/blog/power-bi-blog-hierarchy-level-settings-for-field-parameters/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Hierarchy Level Settings for Field Parameters

*   February 26, 2026

Power BI Blog: Hierarchy Level Settings for Field Parameters
============================================================

_Welcome back to this week’s edition of the Power BI blog series._  _This week, we look at a useful change for field parameters._

In July 2025, field parameters became Generally Available, improving how Matrices remember their expanded or collapsed state when the field parameter selection changes.  Previously, many users found it confusing that a Matrix would fully collapse whenever a field parameter value changed.  However, since the update, some users have shared that they preferred the earlier behaviour because it felt more familiar and better suited for their workflows.

To address this, Power BI has now added a new report-level setting that lets you restore the pre-July 2025 behaviour for field parameters’ expansion and collapse of hierarchy levels.  By default, hierarchy levels remain persistent, but you can switch off this feature for a report using the ‘Persist hierarchy level’ setting.  You may find this setting as follows:

*   in Power BI Desktop, navigate to **Options and settings -> Options -> Current File -> Report settings -> Field Parameters -> Persist hierarchy level**
*   in Fabric, navigate to the Report settings and find ‘Persist hierarchy level’ under the ‘Field parameter’ options.

To illustrate the difference, consider a Matrix showing a field parameter called **Product Group** and a column called **Year** on the rows, displaying **Total sales**.  The field parameter allows selection of category, class, colour or any combination.

In the following example, **Category** is selected and the categories are expanded, so you can see values broken down by **Year**:

![](<Base64-Image-Removed>)

Now, when you change the field parameter from **Category** to **Class**, what happens depends upon the ‘Persist hierarchy level’ setting.  If it’s on, the Matrix visual remains expanded, keeping the **Year** column visible:

![](<Base64-Image-Removed>)

If it’s off, the Matrix collapses and displays only values for **Class**:

![](<Base64-Image-Removed>)

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
 If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

*   [Log in](https://sumproduct.com/blog/power-bi-blog-hierarchy-level-settings-for-field-parameters/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-hierarchy-level-settings-for-field-parameters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-hierarchy-level-settings-for-field-parameters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-hierarchy-level-settings-for-field-parameters/#0)

[](https://sumproduct.com/blog/power-bi-blog-hierarchy-level-settings-for-field-parameters/#0 "close")

top