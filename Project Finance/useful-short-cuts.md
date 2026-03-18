# Useful Short-Cuts, Creating Your Own Short-Cuts, Macros

**Source:** https://edbodmer.com/useful-short-cuts

---

This page includes a review of useful short-cut keys in excel.  There are a few short-cuts that can be helpful are the subject of this page. I also show you how to make you own formatting short-cuts and a basic goal seek macro. A lot of the excel short-cuts are pretty useless and you can use the menu or the mouse just as fast and over-doing short-cuts because of some silly rule is not a good idea. You can go to google and find a list of short-cuts that probably has more than a thousand short-cuts (I have not bothered to go and check). I use just a few short cuts that I think are effective. Some short-cuts are old — for example ALT E, I, S and ALT E, L; and ALT, E, M; ALT, M, D; ALT, E,k which come from an old version of excel. These can be very helpful when used together with the SHIFT, CNLT, R macro. I have put the short-cut keys that I like in the file name Short-cuts.xlsx which is attached below and I have put them in the generic macro file. I also demonstrate a simple technique to make your own short-cut keys with a macro.

Sometimes after I teach a class, participants tell me that they will not be able to remember any of the short-cut keys I show them one day after the class is finished.  The basic objective of the discussion on this page and the associated videos is to demonstrate just a few key short-cut keys that can really help you and that perhaps you can remember.

Some of the pages on this website will hopefully make you think about deep philosophical issues associated with cost of capital in Africa and measuring real risks. This page has no deep risk measurement issues.  It is like a cookbook. I have created the files and videos below so people who take my classes can remember some of the short-cuts.

Explanation of Useful Short-cuts
--------------------------------

Some short-cuts are easy and really help and are worth a tiny investment in practicing. But like a lot of other things in life, you can take things to the extreme and over-use the short-cuts. So I have tried to discuss a few selected few of the short-cuts are really helpful.

Helpful short-cuts include ALT, E,I, S (Everybody Is Stupid, Egyptian Intelligence Service, Elvis Is Sleeping) that works really well with the SHIFT,CNTL,R macro explained in the Generic Macro page. Other helpful short-cuts include ALT,E,M to move sheets around, ALT,E,L to delete a sheet, ALT E,S to paste special and SHIFT, ALT, right arrow and SHIFT, ALT, left arrow, The best short-cut may by the F11 key to make a graph and the ALT, F1 key to put the graph on the current page. To or delete a row or a column, the SHIFT, SPACE and the SHIFT CNTL keys combined with SHIFT,CNTL, + and SHIFT,CNTL,- can be helpful. All of these short-cuts are directly from excel and not associated with any of the files that I have made (i.e. Generic Macros”). Other useful macros create a new sheet, CNTL, N and format cells, SHIFT, CNTL, 1 to 7. One of the new short-cut keys is good for quickly freezing the panes and then un-freezing — ALT, W, F, F.

The video below walks you through these and other short-cut keys in the context of a credit analysis model and the files listed below are used in the videos. In the file named Project and Corporate Credit Example I have listed some of the short-cuts that I think are really helpful. The Project and Corporate Finance Example also is the file that is associated with the video is available for download in the next section.

A few of the short-cut keys that are discussed in the video are shown below.  Please note that I am not one of these crazy people who are so proud of themselves for not ever using the mouse.  I just follow the laziness principle.  When you can be lazier by using the mouse, please use the mouse and do not try to show off with your short-cut prowess. This is really irritating.

![](https://edbodmer.com/wp-content/uploads/2018/04/Corporate-and-Project-3.jpg)

Files for Practicing and Finding Short-Cuts
-------------------------------------------

The files that you can download below are discussed in the video and hopefully may be helpful for thinking about finance as well.  The first file that you may want to download is the file I was working on a file named project and corporate credit when I made the video above.  This file contrasts the cash flow focus in project finance with DSCR, LLCR and PLCR with the re-financing risk in corporate finance. The second file just has a list of short-cuts.  These were published in excel’s help a long time ago.  I have taken this old list (that does not seem to be available any more) and hilighted short-cuts that I find useful.

**[Simple Credit Simulation Used to Demonstrate Short-cut Keys in Excel](https://edbodmer.com/wp-content/uploads/2018/04/Project-and-Corprate-Finance-Credit-Example.xlsx)
 [Excel File with List of Short-cut Keys that May Be Helpful with Hilights on Some Effective Short-Cuts](https://edbodmer.com/wp-content/uploads/2018/04/Short-Cuts.xlsx)
**

![](https://edbodmer.com/wp-content/uploads/2021/02/image-1.png)

Video for Creating your Own Short-Cuts (Don’t Move After Turning on the Macro)
------------------------------------------------------------------------------

Some short-cut keys that would be really good are not included in excel. These may be short-cut keys to format your currency, to underline groups really fast or to put extra decimals in cells formatted as a percent. I have seen some people include all sorts of add-ins in their excel menu with scads of short-cut keys and other functions. I hope you agree that this is not very necessary. Instead, you can make you own customised short-cut keys. Then you will know what is going on and you will not cede control of your excel to anybody else.

The video below demonstrates how you can make your own macros. There is only one big rule here. Please place your cursor on the cell to be formatted and do not move it before you are finished recording the macro.

The file that is used in the video is a file that contains some excel techniques that I used when teaching a budgeting class. The file and the video include a lot more than just making your own short-cut key to create an underline.

**[File that Includes Some Tips for Budget Analysis in Excel with Explanation on How to Create Your Own Short-cut](https://edbodmer.com/wp-content/uploads/2018/04/Budget.xlsb)
**

Creating a Comment Box that Allows you to Turn On and Turn Off Comments
-----------------------------------------------------------------------

You can create a little box that allows you to turn-on and turn-off comments for your spreadsheet.  To do this, the first step is to paint a check-box and name a cell somewhere in your workbook that contains TRUE or FALSE.  The cell name with TRUE or FALSE will drive the turning-on or turning-off of the comments.  Once you have the check box, follow the process below.

1.  In the cell link for the check-box, point to the cell with the TRUE/FALSE and make sure either the range name is used or the sheet name is included.
2.  Create a macro that is attached to the check box.  This could be created directly from the check box by pressing the new option
3.  Use and IF THEN statement in the VBA, where you can press IF Range(“comment”) then application.showcomments= TRUE.
4.  Include the ability to turn off the comments as well by adding a statement like application.showcomments = false at the top of the code.
5.  Make the Checkbox look fancy

Other Miscellaneous Excel Examples

**[Excel File with Financal Database for U.S. Electric Utility Companies Incuding Financial Statements, Valuation Ratios etc.](https://edbodmer.com/wp-content/uploads/2019/06/1.-Financial-Download-Utilities-2019.xlsb)
**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2307&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9584&rand=0.7714547282395269)