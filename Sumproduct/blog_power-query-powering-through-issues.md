# Power Query: Powering Through Issues

**Source:** https://sumproduct.com/blog/power-query-powering-through-issues/

---

[Home](https://sumproduct.com/)

\> Power Query: Powering Through Issues

*   November 21, 2017

Power Query: Powering Through Issues
====================================

Power Query: Powering Through Issues
====================================

22 November 2017

_Welcome to our Power Query blog. This week I look at some of the issues that can come up when using Power Query, and how to resolve them._

Sometimes, I am happily working away in Power Query when I hit a problem. Features are not there when I need them, something I’m _sure_ should have worked doesn’t. The examples I feature here do not form an exhaustive list, but these are some of the issues that I have encountered.

**Where is the Power Query Tab?**

Thankfully, now eradicated by the inclusion of Power Query as the ‘Get and Transform’ section in the Excel 2016 menus, users of earlier versions of Excel can sometimes find that the Power Query (or the louder POWER QUERY) tab has disappeared. This has happened to me (too?) many times, and to date, it hasn’t led to me losing any of my data. The steps to get it back are listed on the Microsoft help pages (a good indicator of how often it happens!). According to Microsoft, it is usually caused by the Excel COM add-in failing to load – for me this can happen after Excel encounters an error and has to close and re-open.

The steps to solve it are as follows.

From the Excel workbook, I click the ‘File’ (or ‘FILE’ if you like Excel 2013 SHOUTING at you) tab. On the File menu, I select ‘Options’, which displays the ‘Excel Options’ screen. At the bottom of this screen there is a ‘Manage’ section as shown below; I choose ‘COM Add-ins’:

![](https://sumproduct.com/wp-content/uploads/2025/05/808c699d2334780a1ea8ea39d986060b.jpg)

I click ‘Go’ to see if Power Query is on the list (see later for what to do if it isn’t).

![](https://sumproduct.com/wp-content/uploads/2025/05/156094a2e276208cc0038337eaa43e84.jpg)

Once I check the box next to ‘Microsoft Power Query for Excel’, I click ‘OK’ and I should see the ‘POWER QUERY’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/3b6624f905bd39db9362eadc807538c7.jpg)

Success, ‘POWER QUERY’ is back, and any queries will be accessible.

Of course, as with any problem to do with computers, the simplest solution can be to ‘switch it off and on again’, which I recommend before trawling though help online to find the answer! If the Add-in is missing from the COM Add-ins list and a reboot has been tried, then upload Power Query again from the Microsoft website. Instructions for this are in [Power Query: Installing and Updating](https://sumproduct.com/blog/power-query-installing-and-updating/)
.

**Where are my queries?**

This one is much easier – in Excel 2016 there is a setting on the ‘Data’ tab in the ‘Get and Transform’ section to show any queries in the workbook (in previous versions of Excel, look for ‘Show Pane’ in the ‘Power Query’ tab):

![](<Base64-Image-Removed>)

**Where is my Formula Bar?**

In the Query editor, there is a ‘View’ tab, which will allow some formatting options, including hiding the Formula Bar – if it is missing, make sure this box is checked.

![](<Base64-Image-Removed>)

**Why didn’t that merge work?**

Sometimes, it is easy to get so engrossed in getting to the next step that I don’t pay attention to making sure the current step is correct. I came across this one whilst working on [Power Query: If You Can’t Tell Them Apart, Join Them](https://sumproduct.com/blog/power-query-if-you-cant-tell-them-apart-join-them/)
. I was trying to apply an inner join to my merge and I had the following screen:

![](<Base64-Image-Removed>)

I couldn’t choose ‘OK’. And this is where I deviated from where I should have gone. I decided to refresh my data using the refresh icons next to each table:

![](<Base64-Image-Removed>)

And now my ‘OK’ button is available, so as I am focussed on getting to my result, I click on it:

![](<Base64-Image-Removed>)

Well it says it’s merged, but it looks like my first table. And it is, because I missed a step on my merge screen:

![](<Base64-Image-Removed>)

I didn’t select any matching columns to link my tables! But because I refreshed, I managed to bypass the security to make sure at least one linked column is selected. If I pick **_FULL\_NAME_** in each table, and click ‘OK’, the results look at little better:

![](<Base64-Image-Removed>)

Ideally, the screen should have checks to stop me from clicking ‘OK’, even if I refresh, but I was able to bypass the security. If I get unexpected results using any of the Power Query functionality, then it is worth going through what I have done step by step to see if it all makes sense. Merging tables with no instructions on how to join them does not make sense.

**Why didn’t that formula work?**

I have had this many times. I have entered a formula in the Advanced Editor, and it just doesn’t work, even though it looks right (sometime even when it tells me ‘No syntax errors have been detected’!). There are a couple of ways to cause this. The easiest one to replicate here is by copying lines of **M** language from a different type of editor. Especially one with internal formatting (and escape sequences). Word in particular has a different format for speech marks \[**“**\], which will not work in the advanced editor. In the screen below I have copied the last line from Word, and received the error message ‘Invalid Literal’:

**#”Invoked Custom Function”**

![](<Base64-Image-Removed>)

To correct it, I need to delete the speech marks in the last line and type them in from the editor.

![](<Base64-Image-Removed>)

And then the editor is happy. Not all errors are easy to spot – sometimes I can end up with a line that looks fine, but is not acceptable. The screen below looks okay – no syntax errors, so I must have created the code correctly, yes?

![](<Base64-Image-Removed>)

Well… actually, no!

The syntax checker is happy, but in the editor, the names of objects are not checked:

![](<Base64-Image-Removed>)

I had an extra space in ‘ Invoked Custom Function’ so it wasn’t recognised. When I have a line of code which doesn’t pass the syntax or further checks and I am fairly sure I have the right functions and objects, then I usually try deleting and retyping that line – **M** language is not only case sensitive, but it does not like escape characters or other fonts.

_\[Editorial note: Liam Bastick would like to add to the observations on **M** code: he advises would-be coders to image that **M** was written by your ex. And your ex hates you…\]_

Come back next time for more ways to use Power Query!

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-powering-through-issues/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-powering-through-issues/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-powering-through-issues/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-powering-through-issues/#0)

[](https://sumproduct.com/blog/power-query-powering-through-issues/#0 "close")

top