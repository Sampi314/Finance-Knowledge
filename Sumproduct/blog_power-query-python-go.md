# Power Query: Python Go

**Source:** https://sumproduct.com/blog/power-query-python-go/

---

[Home](https://sumproduct.com/)

\> Power Query: Python Go

*   October 22, 2019

Power Query: Python Go
======================

Power Query: Python Go
======================

23 October 2019

_Welcome to our Power Query blog. Today, I look at how use Python to filter data in Power Query._

[Last time](https://sumproduct.com/blog/power-query-python-set/)
, I showed how Python can be used to bring data into Power BI. Since I can’t yet use Python in ‘Get & Transform’ from Excel, I will look at how to use Python in Power BI Power Query to filter data. I’ve also included a warning of what not to do if I want to use a Python script.

To start, I would like to analyse some of the expense data from my imaginary salespeople.

![](<Base64-Image-Removed>)

I opt to extract the data from an Excel workbook, where I can get expense data for three of my salespeople. I opt to ‘Transform Data’ so that I can manipulate my data with Power Query.

![](<Base64-Image-Removed>)

I will append my queries and tidy up the data.

![](<Base64-Image-Removed>)

I concatenate my expense data.

![](<Base64-Image-Removed>)

Now I just need to tidy my data.

![](<Base64-Image-Removed>)

I have decided I want to see expenses that are greater than 30. I could do this using the filter on amount, but for this example, I will use Python instead.

![](<Base64-Image-Removed>)

There is an option to ‘Run Python Script’ on the ‘Transform’ tab. The description of this option is ‘Use Python to transform and shape your data. Python needs to be installed for you to add a Python script’.

The Python code for this would be:

**import pandas as pd**

**dataset\_filtered = dataset.query(‘Amount > 30’)**

![](<Base64-Image-Removed>)

The results are not quite what I am looking for!

![](<Base64-Image-Removed>)

The error says:

**Formula.Firewall: Query ‘python\_data’ (step ‘Run Python script’) references other queries or steps, so it may not directly access a data source. Please rebuild this data combination.**

This is actually a Power Query error, and nothing to do with Python. The message is confusing, and it’s down to having the append earlier in the process. Normally, when this error is encountered in Power Query, it is possible to move the offending steps to another query, but in this case, even if I put all the other steps in another query and use that as a source for the ‘Run Python script’ step, I get the same error. At the moment, I can’t use a Python script on appended data.

I’ll avoid the append altogether in this example, by bringing in the merged data from an Excel workbook:

![](<Base64-Image-Removed>)

I enter my Python script again and create the step. This time I get a message about privacy:

![](<Base64-Image-Removed>)

I need to set the data sources to Public so that Python and Power BI will work together.

![](<Base64-Image-Removed>)

Once I’ve set the levels, I can continue.

![](<Base64-Image-Removed>)

I need to give permission for the script to run.

![](<Base64-Image-Removed>)

I only have to give permission once for each new script I run.

![](<Base64-Image-Removed>)

I have two rows, once for ‘dataset’ and one for ‘dataset\_filtered’. I click on ‘dataset\_filtered’.

![](<Base64-Image-Removed>)

I can see all the expenses that are more than 30.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-python-go/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-python-go/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-python-go/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-python-go/#0)

[](https://sumproduct.com/blog/power-query-python-go/#0 "close")

top