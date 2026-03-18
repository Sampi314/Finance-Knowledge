# Power Query: Riveting Results Part 2

**Source:** https://sumproduct.com/blog/power-query-riveting-results-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Riveting Results Part 2

*   December 21, 2021

Power Query: Riveting Results Part 2
====================================

Power Query: Riveting Results Part 2
====================================

22 December 2021

_Welcome to our Power Query blog. This week, I create parameters for last week’s example._

My salespeople are still taking a break. We will keep looking at those exam results from [last week](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
:

![](<Base64-Image-Removed>)

I will be grading the results, and I will be using this example to explore parameters. [Last time](https://sumproduct.com/blog/power-query-riveting-results-part-1/)
, I created a column to grade the results:

![](<Base64-Image-Removed>)

I am now ready to create some parameters to calculate the grades. To begin with, I will enter these parameters from the ‘Manage Parameter’ option on the Home tab:

![](<Base64-Image-Removed>)

I opt to create a ‘New Parameter’. This brings up a dialog:

![](<Base64-Image-Removed>)

I am going to enter a parameter for each grade. I call my first parameter **P\_Grade\_9**:

![](<Base64-Image-Removed>)

The ‘**P\_**‘ is to indicate it is a **p**arameter. This will make it easy to spot in the list of queries. I also enter a description. When I choose the Type, there is no option for percentage, so I make it a ‘Decimal Number’ instead.

![](<Base64-Image-Removed>)

For now, I will allow ‘Any value’. I will be revisiting the ‘Suggested Values’ dropdown for this example later.

![](<Base64-Image-Removed>)

To complete this parameter, I enter a ‘Current Value’ of 90. If I were to click ‘OK’ at this point, the parameter would be created, and I would automatically exit the dialog:

![](<Base64-Image-Removed>)

I can see the parameter in the Queries panel. If the parameter is selected, then I can edit the ‘Current Value’ if I wish. The ‘Current Value’ also appears next to the parameter in brackets ‘(90)’ so that I can always see what it is set to in the Queries panel.

If I want to create multiple parameters, then I can stay in the ‘Manage Parameter’ dialog by clicking ‘New’ instead of ‘OK’ when I have finished each parameter:

![](<Base64-Image-Removed>)

Note that since my parameters are similar, I can also copy and paste or create Duplicates:

![](<Base64-Image-Removed>)

This is fine, as long as I remember to change the name, description and ‘Current Value’.

Do not create a ‘Reference’. This would return the ‘Current Value’ of the parameter:

![](<Base64-Image-Removed>)

The icon next to **P\_Grade\_8 (2)** indicates a number. Note also that the ‘**(2)’** in this case is created because there is already a **P\_Grade\_8** and is not the value!

I now have all my parameters ready for the next step:

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-riveting-results-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-riveting-results-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-riveting-results-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-riveting-results-part-2/#0)

[](https://sumproduct.com/blog/power-query-riveting-results-part-2/#0 "close")

top