# Power BI Blog: Performance Analyzer

**Source:** https://sumproduct.com/blog/power-bi-blog-performance-analyzer/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Performance Analyzer

*   May 29, 2019

Power BI Blog: Performance Analyzer
===================================

Power BI Blog: Performance Analyzer
===================================

30 May 2019

_Welcome back to this week’s Power BI blog series! This week, we’re going to look at a new feature called Performance Analyzer._

Have you ever experienced lag when changing slicers or just interacting with your Power BI dashboard? We certainly have. Hopefully those days are numbered as there is a new feature in Power BI called Performance Analyzer.

To enable the Performance Analyzer head over to the View tab in Power BI and tick the “Performance Analyzer” check box:

![](<Base64-Image-Removed>)

When we first enable the Performance Analyzer we are greeted with an empty pane:

![](<Base64-Image-Removed>)

We will have to click on ‘Start recording’ to see how our report loads. Once we start recording Power BI will analyse the time it takes for any query such as changing a page or refreshing visuals will populate the pane with new information.

Each visual will have different steps logged underneath it, and each step will have the corresponding time it took to load.

![](<Base64-Image-Removed>)

To check on an individual visualization’s performance, we can mouse over the target visualization and click on the ‘Refresh this visual’ option:

![](<Base64-Image-Removed>)

We can click on an individual log entry to expand it to three different sections: DAX query, Visual display, and Other.

Each section represents a different component of the query:

*   The DAX query is the amount of time it took to run the query
*   Visual display is the length of time Power BI took to render the visual on screen
*   Other, is the time spent on preparing queries, and or waiting for other visuals or queries to complete in the background.

![](<Base64-Image-Removed>)

For more advanced users, you can elect to ‘Copy query’ and paste it onto a clipboard or other code interfaces to analyse it further:

![](<Base64-Image-Removed>)

We can also click on the ‘Export’ option to export all of the query information into a JSON file for analysis using other tools.

![](<Base64-Image-Removed>)

Hopefully this tool opens up avenues for troubleshooting when your query takes too long to load!

That’s it for this week tune in next time for more Power BI. See you then!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-performance-analyzer/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-performance-analyzer/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-performance-analyzer/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-performance-analyzer/#0)

[](https://sumproduct.com/blog/power-bi-blog-performance-analyzer/#0 "close")

top