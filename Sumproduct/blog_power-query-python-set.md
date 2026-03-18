# Power Query: Python Set

**Source:** https://sumproduct.com/blog/power-query-python-set/

---

[Home](https://sumproduct.com/)

\> Power Query: Python Set

*   October 15, 2019

Power Query: Python Set
=======================

Power Query: Python Set
=======================

16 October 2019

_Welcome to our Power Query blog. Today, I look at how to set up and use Python in Power BI._

[Last time](https://sumproduct.com/blog/power-query-python-ready/)
, I installed and set up Python ready for Power BI to use. Naturally, I’d also like to be able to use Python in ‘Get & Transform’ from Excel, but for now this is not yet available, so I’ll look at how to use Python in Power BI.

In the ‘Options’ tab, I found the Python sub screen:

![](<Base64-Image-Removed>)

I set up the IDE to point to the location of my Visual Studio Code.

![](<Base64-Image-Removed>)

I am ready to use Python as my source. Back on the ‘Home’ tab, I look at the options available from the ‘Get Data’ tab.

![](<Base64-Image-Removed>)

I can limit the amount of data options available by selecting ‘Other’.

![](<Base64-Image-Removed>)

I have the option ‘Python Script’, and hovering over this gives me more information ‘Run a Python script on a local Python installation to import data frames’. I choose this option.

![](<Base64-Image-Removed>)

I can enter a Python script here – I will use the same standard Microsoft example that I used last time.

import pandas as pd

data = \[\[‘Alex’,10\],\[‘Bob’,12\],\[‘Clarke’,13\]\]

df = pd.DataFrame(data,columns=\[‘Name’,’Age’\],dtype=float)

print (df)

![](<Base64-Image-Removed>)

I click ‘OK’ to run the script. There is a slight pause whilst the connections are secured and the script is run, and then the ‘Navigator Pane’ appears.

![](<Base64-Image-Removed>)

I can select the table icon to see what data has been imported.

![](<Base64-Image-Removed>)

The data appears as expected. I choose to ‘Transform Data’.

![](<Base64-Image-Removed>)

My data is in the Power Query editor ready to be transformed. Once I am happy, I use ‘Close & Apply’ to make my data available.

![](<Base64-Image-Removed>)

I can now go back to my Power BI Desktop report canvas and select this data.

![](<Base64-Image-Removed>)

Next time, I will look at how to use Python to filter some of the data provided by my imaginary salespeople.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-python-set/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-python-set/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-python-set/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-python-set/#0)

[](https://sumproduct.com/blog/power-query-python-set/#0 "close")

top