# Power BI Blog: Row Level Security

**Source:** https://sumproduct.com/blog/power-bi-blog-row-level-security/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Row Level Security

*   December 19, 2018

Power BI Blog: Row Level Security
=================================

Power BI Blog: Row Level Security
=================================

20 December 2018

Welcome to the last Power BI article of the year! This week, we’re going to look at Row Level Security, as a topic that has come up quite a bit in recent enquiries.

Row Level Security is exactly that – it’s a security setting that can be applied to individuals that restricts what data they have access to at the row level. Essentially, you can specify rules (e.g. Country = “Australia”) that filter the data that a user can see in their reports.

To set it up, go to the Modelling tab and find the Manage Roles button:

![](<Base64-Image-Removed>)

And from here, we can create a role that might be applied to our dataset:

![](<Base64-Image-Removed>)

By following the prompts, we can add a filter:

\[EnglishCountryRegionName\] = “Australia”

… that will restrict what “Australian Managers” can see to only those rows that match the filter criteria; that is, relate to the country in question.

Once we save and publish this data, we can go into the Power BI service to share our dataset to the Australian Managers. Under your workspace, go to Datasets, click on the ellipses and browse to Security:

![](<Base64-Image-Removed>)

This will then give you the ability to see who is restricted in this role, and to add members to specific roles.

![](<Base64-Image-Removed>)

That’s it for this year – nearly 50 blogs later and we’re still going strong! See you in 2019 with more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-row-level-security/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-row-level-security/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-row-level-security/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-row-level-security/#0)

[](https://sumproduct.com/blog/power-bi-blog-row-level-security/#0 "close")

top