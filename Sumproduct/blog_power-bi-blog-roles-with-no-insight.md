# Power BI Blog: Roles with no Insight

**Source:** https://sumproduct.com/blog/power-bi-blog-roles-with-no-insight/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Roles with no Insight

*   February 16, 2022

Power BI Blog: Roles with no Insight
====================================

Power BI Blog: Roles with no Insight
====================================

17 February 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at an issue which can occur when publishing a dashboard._

Imagine we have the following dashboard we wish to publish to Power BI Service:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-64-1.jpg)

The option to Publish is on the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-87.jpg)

Selecting this option allows us to choose which Workspace we want to publish to Power BI Service. For more information on different forms of Power BI see blog ‘[Power BI Tips: Which Power BI should I use?](https://www.sumproduct.com/blog/article/power-bi-tips/which-power-bi-should-i-use)
‘

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-65.jpg)

When we have selected to publish to ‘My workspace’, the processing takes place:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-59.jpg)

Once the process is completed, the dialog makes some options available:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-49.jpg)

The ‘Get Quick Insights’ option is appealing, so we choose that:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-41.jpg)

However, three hours later, nothing has happened… What went wrong?

The answer is in our original dashboard. If we go to the Modelling tab, we can ‘Manage Roles’:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-38.jpg)

It turns out we have set up an ‘Australian manager’ role:

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-28.jpg)

If we choose ‘View as’, we can view the data as anyone using Power BI Services with this role would see the dashboard:

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-24.jpg)

Whilst setting up Row Level Security (RLS) is a useful aspect of Power BI (see more on this in [Power BI: Row Level Security](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-row-level-security)
), it prevents Quick Insights from working. The reason for this is that Quick Insights are not currently configured to limit the insights to only consider the data that a particular role is allowed to view.

We can remove the Roles from the ‘Manage Roles’ dialog:

![](<Base64-Image-Removed>)

Once the Roles are removed, we publish again, and this time the Quick Insights do appear:

![](<Base64-Image-Removed>)

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-roles-with-no-insight/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-roles-with-no-insight/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-roles-with-no-insight/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-roles-with-no-insight/#0)

[](https://sumproduct.com/blog/power-bi-blog-roles-with-no-insight/#0 "close")

top