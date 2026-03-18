# Power BI Blog: Refreshing Time on Power BI Service – Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-refreshing-time-on-power-bi-service-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Refreshing Time on Power BI Service – Part 1

*   May 15, 2024

Power BI Blog: Refreshing Time on Power BI Service – Part 1
===========================================================

Power BI Blog: Refreshing Time on Power BI Service – Part 1
===========================================================

16 May 2024

_Welcome to our Power BI blogs. Over the next two weeks, we will show you how to manage time-refreshing on Power BI Service._

When you manage dashboards on Power BI Service and try to refresh anything involving Date/Time values, you will discover that Power BI Service uses Coordinated Universal Time (UTC) instead of your local time. You might work around this by manually adding on the necessary time-zone adjustments (_e.g._ UTC+8 for Beijing) in your visual measures or in the Power Query **M** code, but it can get messy where daylight saving is relevant.

In the following example, we prepared two Date/Time variables, one with a measure, **\=NOW()**, and one with an **M** function, **\=DateTime.LocalNow()**.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-5-1.jpg)

They are matching our local Sydney date and time on Power BI Desktop, but once we publish the report to Power BI Service,

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-6-1.jpg)

we go back ten \[10\] hours in time and have the standard UTC now.

We will demonstrate a couple of methods to tackle the problem, and also how to manage daylight saving.

**_Obtain Date and Time from a Web API_**

It’s not rocket science that if we get data from _SydneyTime.com_ we will obtain the local time for Sydney. A drawback is that it can cost extra time to obtain web-based data. Also, robustness of the data source needs to be considered.

For this example, we will use [WorldTimeAPI.org](https://worldtimeapi.org/)
. When we enter the URL

[https://worldtimeapi.org/api/timezone/Australia/sydney](https://worldtimeapi.org/api/timezone/Australia/sydney)

in Power BI to Get Data From Web,

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-5-1.jpg)

Power BI will use the **M** function combination **Json.Document(Web.Contents())** to return a _record_.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-5-1.jpg)

Drilling down **datetime** provides as a single text value.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-3-1.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-1-1.jpg)

Then we can convert it to a table, rename it and change the data type to Date/Time/Timezone.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-1-1.jpg)![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-1-1.jpg)

The text string obtained from [WorldTimeAPI.org](https://worldtimeapi.org/)
 can’t be changed to Date/Time type directly, so we need the above step. However, this action also introduces time zone information back into the data and we’ll need to remove that. We can use the **DateTimeZone.RemoveZone()** function:

**WipeTimeZone =  
Table.TransformColumns(#”Changed Type”,  
{{“Date Time Web”, each DateTimeZone.RemoveZone(\_)}})**

After that, we can change the data type to Date/Time:

![](<Base64-Image-Removed>)

It should be noted that this Date/Time value will be refreshed every time Power Query is refreshed (by calling the API), no matter we are using Power BI Desktop or Power BI Service.

![](<Base64-Image-Removed>)

That’s it for this week. Next week we will show you an alternative approach using Power Query **M** functions. Please stay tuned. For more thoughts and insights, please visit [https://www.sumproduct.com](https://www.sumproduct.com/)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-refreshing-time-on-power-bi-service-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-refreshing-time-on-power-bi-service-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-refreshing-time-on-power-bi-service-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-refreshing-time-on-power-bi-service-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-refreshing-time-on-power-bi-service-part-1/#0 "close")

top