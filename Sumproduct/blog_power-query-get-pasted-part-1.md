# Power Query: Get Pasted – Part 1

**Source:** https://sumproduct.com/blog/power-query-get-pasted-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Get Pasted – Part 1

*   October 18, 2022

Power Query: Get Pasted – Part 1
================================

Power Query: Get Pasted – Part 1
================================

19 October 2022

_Welcome to our Power Query blog. This week, we present an alternative approach to a one-off data grab from the web._

Today, I venture into Power BI. The task is to get a list of presenters, languages and times from the recent Excel Virtually Global 2022 event. This data is not going to change; the event is over.

Since the data is on the web, I could start with the ‘Get Data’ dropdown on the Home tab:

![](<Base64-Image-Removed>)

Here, I locate the Web option:

![](<Base64-Image-Removed>)

The URL comes from the website page :

![](<Base64-Image-Removed>)

I enter this URL into the ‘From Web’ dialog:

![](<Base64-Image-Removed>)

I am prompted for the connection criteria; I choose to ‘Use anonymous access for this Web content’.

![](<Base64-Image-Removed>)

Then I wait for Power BI to connect:

![](<Base64-Image-Removed>)

When the Navigator dialog appears, I can see there is a table, so I select this and choose to ‘Transform Data’:

![](<Base64-Image-Removed>)

However, this does not give me the data I need:

![](<Base64-Image-Removed>)

As this is not something I am planning to refresh, since the event has now ended, I can approach this another way. I delete the query **Table 1**.

In the Power Query editor, I locate the ‘Enter Data’ button on the Home tab:

![](<Base64-Image-Removed>)

This presents me with a new blank table:

![](<Base64-Image-Removed>)

I go back to the website and copy the data from the table:

![](<Base64-Image-Removed>)

I can then paste the data into the ‘Create Table’ dialog:

![](<Base64-Image-Removed>)

The data is all in one column, but at least I now have the presenter names, languages and times.

Next time, I will transform this data.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-get-pasted-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-get-pasted-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-get-pasted-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-get-pasted-part-1/#0)

[](https://sumproduct.com/blog/power-query-get-pasted-part-1/#0 "close")

top