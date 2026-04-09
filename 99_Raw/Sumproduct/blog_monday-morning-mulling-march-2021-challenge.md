# Monday Morning Mulling: March 2021 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-march-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: March 2021 Challenge

*   March 28, 2021

Monday Morning Mulling: March 2021 Challenge
============================================

Monday Morning Mulling: March 2021 Challenge
============================================

29 March 2021

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The challenge this month was to create a line in a Matrix visualisation in Power BI. This should be performed only using the tools within Power BI, but not by drawing a Shape in the report.

**_The Challenge_**

In Power BI there is a visualisation called the Matrix visualisation. We can use it to display numerical values over several time periods:

![](<Base64-Image-Removed>)

Each line item is a measure. The challenge here was to make the **Gross Profit** measure stand out more by inserting lines into the Matrix visualisation like so:

![](<Base64-Image-Removed>)

We did not simply draw a line on top of the visualisation. We can expand the visualisation by breaking the **Total COGS** measure down to **Direct Labour** and **Direct Materials**:

![](<Base64-Image-Removed>)

The lines move _automatically._

**_Suggested Solution_**

The first step here is to create a new measure, in this case we are going to enter the following DAX code into the measure formula bar:

**\* = ” “**

We use the asterisk in this example, because when shown on a visualisation, the Asterisk defaults to a blank space. That’s a nice trick to know. For example, if we place the newly created Asterisk measure in between the **Total COGS** and the **Gross Profit** measure we get the following result:

![](<Base64-Image-Removed>)

Looking at the visualisation it is currently a grey line. We can change that by navigating to the Format tab, and expanding the ‘Field formatting’ section:

![](<Base64-Image-Removed>)

From here, we change the formatting of the asterisk (**\***) measure, with the trick being to change the ‘Background color’ to black:

![](<Base64-Image-Removed>)

The next step is to toggle the ‘Apply to header’ option to On.

![](<Base64-Image-Removed>)

To add the line below the **Gross Profit** measure, we simply add another Asterisk measure below the **Gross Profit** measure in the Values area:

![](<Base64-Image-Removed>)

That is how we did it. How did you fare?

_The Final Friday Fix will return on Friday 30th April 2021 with a new Challenge. In the meantime, have a great April fools and please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-march-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-march-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-march-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-march-2021-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-march-2021-challenge/#0 "close")

top