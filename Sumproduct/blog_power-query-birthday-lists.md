# Power Query: Birthday Lists

**Source:** https://sumproduct.com/blog/power-query-birthday-lists/

---

[Home](https://sumproduct.com/)

\> Power Query: Birthday Lists

*   November 14, 2017

Power Query: Birthday Lists
===========================

Power Query: Birthday Lists
===========================

15 November 2017

_Welcome to our Power Query blog. Since I have reached the milestone of my 50th issue, I have covered a whole list of Power Query features. Talking of lists… (it’s an ellipsis, get it?)_

I will start with a nice simple example – in a new query, I will create a list of consecutive numbers.

![](<Base64-Image-Removed>)

Curly brackets (or braces) **{ }** indicate that a list is enclosed. For whole numbers, I can define a range by giving my start and end points and separate them by an ellipsis of two dots .. to indicate that the intervening numbers should be included. Therefore, I may specify a list from 1 to 10 by entering

            **= {1..10}**

in the formula bar.

![](<Base64-Image-Removed>)

Numbers are not the only list I can create with this format; I can create a list of consecutive letters. Since letters are text, they must be surrounded by speech marks **” “**.

![](<Base64-Image-Removed>)

Using ellipsis with characters is limited to single characters though, so although I can create this list

**\= {“0”..”9″}**

![](<Base64-Image-Removed>)

I am not allowed to create this

**\= {“1”..”10″}**

![](<Base64-Image-Removed>)

I have to specify the whole list instead

**\= {“1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “10”)**

![](<Base64-Image-Removed>)

Therefore, lists with ellipses are more useful for numbers – what if I want to create a list of dates without typing them out? In this case I can’t just type the number for today as 15/11/17 or even 151117, as this is not how Power Query will recognise it – however I can use the serial number of the date. In order to get a date in serial number format, I can use the **Number.From** function.

Number.From(**value** as any, optional **culture** as nullable text) as nullable number

My **value** is **#date** and I need to give my date as year, month and day separated by commas. So, for today it would be:

**\= Number.From(#date(2017,11,15))**

I create a list of the dates (in serial number format) until the end of November:

![](<Base64-Image-Removed>)

If I want the dates to look like dates, then I need more formatting options open to me. Having created my list, if I want to transform data or merge with other tables, then I need to convert my list to a table, which is easy to do, as the options for lists are automatically displayed when I create my list.

![](<Base64-Image-Removed>)

As I have created a very simple list I can take the defaults and create my table. In the ‘Transform’ tab, I can choose to convert my ‘Data Type’ to ‘Date’ (I could also do this from the ‘Home’ tab):

![](<Base64-Image-Removed>)

Thus, I have my list of dates in a recognisable format.

![](<Base64-Image-Removed>)

There are other ways to get a list of dates (without using the ellipsis). The **List.Dates** function allows more flexibility:

List.Dates(**start** as date, **count** as number, **step** as duration) as list

I am going to create my list again from a blank query, using this function.

**\=List.Dates(#date(2017,11,15), 16, #duration(1,0,0,0))**

Now, since this function is more flexible, it looks more complicated. I have specified my start date as before, then I need to specify how many list entries I want and finally, what the difference is between each entry. Since I can also use this function for ‘datetimes’ the duration can be hours, minutes etc. I choose to increment by one day at a time.

That sounds complicated: if only there was some way to remind me what to enter for the **List.Dates** function…

![](<Base64-Image-Removed>)

Now this is useful. Power Query has recognised what I am trying to do when I enter **List.Dates**, and I can enter the parameters one at a time.

![](<Base64-Image-Removed>)

I enter my parameters (I enter 1 as the step or increment as I’m assuming one day is the default).

![](<Base64-Image-Removed>)

The advantage this way, is that my dates are created in a recognisable format so I can see they are all there. There are some other interesting (well for me anyway) uses of the **List** functionality. I can list numbers, without using an ellipsis, and by specifying the interval:

List.Numbers(**start** as number, **count** as number, **optional increment** as nullable number) as { Number }  

This function is very flexible too, so it looks complicated. I create a list with the following formula

**\= List.Numbers(3, 16, 3)**

So, I am expecting my list to start at three, have 16 entries and have an interval or increment of three. As before, I don’t have to remember how to use the parameters, I can just enter **List.Numbers**:

![](<Base64-Image-Removed>)

So now I am expecting to see my three times table:

![](<Base64-Image-Removed>)

I don’t have to stick to whole numbers; if I choose different parameters I can have a list of decimals:

![](<Base64-Image-Removed>)

This time I expect to see my 0.3 times table.

![](<Base64-Image-Removed>)

If for some reason I want to see my list in reverse, I can do this with the…

List.Reverse(**list** as list) as list

The **list** can be created using any of the methods used so far, so I can create

**\= List.Reverse({1..15})**

![](<Base64-Image-Removed>)

Or I can reverse my three times table:

![](<Base64-Image-Removed>)

Finally (for now), I can create a repeating list of numbers, with **List.Repeat**.

List.Repeat(**list** as list**, count** as number) as list 

This repeats any list as many times as I want. Therefore, I can repeat the first three entries of my three times table.

**\= List.Repeat(List.Numbers(3,3,3),3)**

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-birthday-lists/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-birthday-lists/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-birthday-lists/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-birthday-lists/#0)

[](https://sumproduct.com/blog/power-query-birthday-lists/#0 "close")

top