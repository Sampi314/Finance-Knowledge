# Making a slick on/off switch using Excel & little bit of VBA [case study] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/on-off-switch-in-excel-vba

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Making a slick on/off switch using Excel & little bit of VBA \[case study\]
===========================================================================

*   Last updated on December 6, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_I have a confession to make._

I am not sure how to describe this new thing I made in Excel / VBA. So first take a look at it.

![On off swtich linked to a chart - Made with Excel & VBA - Demo](https://img.chandoo.org/c/on-off-switch-interactive-chart-demo.gif)

### Inspiration for the on/off switch

As you know, there is a form control in Excel that behaves like on/off switch. It is called [check box](http://chandoo.org/wp/2011/03/30/form-controls/#check-box)
. Although they are easy to use, check boxes are not very slick. So I though, why not make an on/off switch like the ones we see in our iPhones / tablets. And the rest is what you see.

### How to make this on/off switch using Excel & VBA

1.  Create an on/off switch using drawing tools in Excel insert ribbon. I used a rounded rectangle for outer container and small circle for switch.
2.  Select the circle, name it using namebox (top-left in formula bar). I called mine as btnToggle.
3.  Write a macro that takes care of the switch behavior. The macro looks like this:
    1.  Change a cell value to true or false based on the switch position.
    2.  Move the btnToggle from left edge to right edge (or reverse) in a loop.
    3.  Change switch color to GREEN or dark black based on its position.
4.  Use the linked to cell value to make changes to your charts / dashboards / formulas as needed.
5.  That is all!

### Video tutorial – On/off switch using Excel & VBA

To make you even more awesome, I made a short video tutorial explaining the whole thing. Watch it below:

Note: This video shows another example of on/off switch (not the chart one you see above), but equally awesome.

Alternative ways to watch this video – on our [YouTube Channel](http://youtu.be/lzwDxGapdu8)
 or [Facebook Fan Page](https://www.facebook.com/photo.php?v=571674399571085)
.

### Download Example Workbook

[**Click here to download the example workbook**](https://img.chandoo.org/c/holiday-sale.xlsm)
. Play with it to understand this concept better. Examine the moveBtn2() macro to learn more.

### Do you like the on/off switch concept?

I had fun making this. It looks great and makes my workbook attractive. But I find one nagging problem with it. _You have to set up multiple macros if you want several of them in a workbook._ Of course there is a work around. With a little bit of clever programming we can make one macro that can talk to all on/off switches and update their individual linked cells. We will save it for another day.

**What about you?** Do you like the on/off switch concept? How are you planning to use it? Go ahead and tell me in comments.

### Learn more about VBA from these examples

If you like the on/off switch example, you are going to love these other examples.

*   [3D Dancing pendulums simulated in VBA](http://chandoo.org/wp/2011/07/06/3d-dancing-pendulums/)
    
*   [Clocks ant timers using Excel & VBA](http://chandoo.org/wp/2012/07/05/masterchef-style-clock-in-excel/)
    
*   [A replacement for scrollbar control – picture calendar case study](http://chandoo.org/wp/2012/01/02/picture-calendar-template/)
    
*   [More VBA examples](http://chandoo.org/wp/excel-vba/examples/)
     (40+)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

*   [30 Comments](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/on-off-switch-in-excel-vba/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [animation](https://chandoo.org/wp/tag/animation/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [products](https://chandoo.org/wp/tag/products/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousHoliday Sale is on, Save upto $50 on your favorite Excel courses](https://chandoo.org/wp/2013-holiday-sale-is-on/)

[NextCreating Triangular Plots using ExcelNext](https://chandoo.org/wp/creating-triangular-plots-using-excel/)

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introducing-advanced-excel-training-v1.png)](https://chandoo.org/wp/excel-school-program/)

Chandoo is an awesome teacher

__________ Rated 5 out of 5

_– Jason_

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Complete Introduction to Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

### 30 Responses to “Making a slick on/off switch using Excel & little bit of VBA \[case study\]”

1.  ![](https://secure.gravatar.com/avatar/13c54046f56abd0675dab5340e650f46706ca98677bb07e97be682fadcdb4dac?s=64&d=mm&r=g) Pete says:
    
    [December 5, 2013 at 11:16 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459677)
    
    Now that is one slick trick! I can use this in many of the dashboard that I am building. Thanks Chandoo!
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459677)
    
2.  ![](https://secure.gravatar.com/avatar/f5f332a190aa911c412230d63bfae4fced864c832f478118a4d9d7e6954fb80b?s=64&d=mm&r=g) Khushnood Viccaji says:
    
    [December 5, 2013 at 11:21 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459678)
    
    I have only this to say 🙂  
    [http://www.youtube.com/watch?v=1zj418rKTqU](http://www.youtube.com/watch?v=1zj418rKTqU)
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459678)
    
3.  ![](https://secure.gravatar.com/avatar/e50cd3b131e08ebe76d868240a47445341929dc8ed4b2fb793d95eb7e9577e55?s=64&d=mm&r=g) Ninad Pradhan says:
    
    [December 5, 2013 at 5:30 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459684)
    
    Neat. very neat. Thanks.
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459684)
    
4.  ![](https://secure.gravatar.com/avatar/b88f13a79ab51b5747e940a05398d27cc0cc4d2875c41b07165ec0d8c01c9dab?s=64&d=mm&r=g) Hamy says:
    
    [December 5, 2013 at 6:25 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459685)
    
    I am not sure if this is done, but websites like make avail so many nice codes and tips, that needs to be reviewed more than once. I have tried storing them in programs such as Treepad, OneNote but its has not been very effective.. May be you can write a blog making your point and allowing people to comment on a best way to catalog these codes
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459685)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [December 6, 2013 at 4:15 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459693)
        
        I usually rely on browser bookmarks to save my favorite pieces code / technique.
        
        [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459693)
        
    *   ![](https://secure.gravatar.com/avatar/f5f332a190aa911c412230d63bfae4fced864c832f478118a4d9d7e6954fb80b?s=64&d=mm&r=g) Khushnood Viccaji says:
        
        [December 6, 2013 at 5:19 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459702)
        
        I have a whole bunch of xls and bas files saved in a separate folder, with all the sample code and Excel features that can be used for various purposes.  
        These files are named in as detailed manner as possible using keywords to indicate the feature or purpose of the code.
        
        After that, whenever I need to use some code or feature, I use a small but powerful filename search utility, 'Everything' from [http://www.voidtools.com](http://www.voidtools.com/)
        , to locate the required file.
        
        E.g. in another thread I had asked Chandoo about how to get the color index for conditionally formatted cells in a UDF.  
        I have now saved the details in a file named "CELLS\_Color Index Conditional Formatting CF Colors Chip Pearson.bas" for future use.
        
        [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459702)
        
5.  ![](https://secure.gravatar.com/avatar/409717731b3a3a666910bd77f8a40feb0c86c5cd53fbaa2c5755cad7773868d8?s=64&d=mm&r=g) Gene says:
    
    [December 5, 2013 at 6:49 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459686)
    
    how do you define the moveBy variable?
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459686)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [December 6, 2013 at 4:14 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459692)
        
        I started macro recorder and moved a drawing shape by using left arrow key. The increment left value was 0.75. That is how I arrived at the value for moveby.
        
        [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459692)
        
6.  ![](https://secure.gravatar.com/avatar/ed4bf8fb3409ece33de5212089d26b299d08ebb0313443228c516ea46778609e?s=64&d=mm&r=g) Darin Myers says:
    
    [December 5, 2013 at 8:20 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459689)
    
    Had an idea to add a fade effect to the example workbook for a smoother transition. (Code Below) There are a few other improvements I have in mind to improve the abstraction and re-usability of the control, but this was just a quick and fun addition.
    
    Also, I have the same question as Gene: how did you determine the moveby value. Was it a mathematical solution or more experimental?
    
    '''BEGIN CODE'''
    
    Option Explicit
    
    Sub moveBtn2()  
    Dim objToggle As Shape 'Toggle Button  
    Dim objHide As Shape 'Rectangle to hide content  
    Dim CellLink As Range 'Provide a cell link that can be used in formulas
    
    Dim moveBy As Double  
    Dim transBy As Double  
    Dim i As Long  
    Dim iSteps As Long
    
    Const ON\_COLOR As Long = 5287936 'Green RGB(0, 176, 80)  
    Const OFF\_COLOR As Long = 2171169 'Black RGB(33, 33, 33)
    
    Set objToggle = ActiveSheet.Shapes("btnToggle")  
    Set objHide = ActiveSheet.Shapes("shpHideSale")  
    Set CellLink = ActiveSheet.Range("F3")
    
    iSteps = 25  
    moveBy = 0.75  
    transBy = 1 / iSteps
    
    If objToggle.Fill.ForeColor.RGB = OFF\_COLOR Then 'Turn On  
    CellLink = True  
    objToggle.Fill.ForeColor.RGB = ON\_COLOR  
    Else 'Turn Off  
    CellLink = False  
    moveBy = -1 \* moveBy  
    transBy = -1 \* transBy  
    objToggle.Fill.ForeColor.RGB = OFF\_COLOR 'Black  
    End If
    
    For i = 1 To iSteps  
    objToggle.IncrementLeft moveBy  
    objHide.Fill.Transparency = objHide.Fill.Transparency + transBy  
    DoEvents  
    Next i
    
    objHide.Visible = Not (objHide.Fill.Transparency = 1)
    
    End Sub
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459689)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [December 6, 2013 at 1:48 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459690)
        
        Good idea.. 🙂
        
        [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459690)
        
7.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
     says:
    
    [December 6, 2013 at 4:16 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459694)
    
    Thanks all for the love. I am glad you like this 🙂
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459694)
    
8.  ![](https://secure.gravatar.com/avatar/d309cae04fc971e84a19db159ccc2dfa78b7a1949564de62d999cbebc5e7cf62?s=64&d=mm&r=g) vishwanath says:
    
    [December 6, 2013 at 10:46 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459698)
    
    Hi ,
    
    I am not able to get the "Hand symbol" to the cursor , when i click on the Round circle it will just SELECT and goes to design mode
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459698)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [December 6, 2013 at 11:06 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459700)
        
        The macro is attached to the outer rounded rectangle. try clicking on that.
        
        [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459700)
        
9.  ![](https://secure.gravatar.com/avatar/de95c2a6327c0745bd1a9a6c039403d22db3259b6e956566ea3f4650665f35bb?s=64&d=mm&r=g) [Oz](http://www.datascopic.net/)
     says:
    
    [December 8, 2013 at 11:17 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459719)
    
    Thanks for this. I'm playing with this and have the ball traveling in a square. One thing doesn't make sense:
    
    What is the relationship between moveBy and increment?  
    Moving either one of the variables changes the distance the ball travels. I thought i would only impact speed but it does impact the distance.
    
    What's going on?
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459719)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [December 11, 2013 at 3:05 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459748)
        
        There is no way (well, almost) to control the speed. It just depends on how fast your Excel is. The moveBy tells Excel how many pixels to move each time the line runs.
        
        [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459748)
        
        *   ![](https://secure.gravatar.com/avatar/de95c2a6327c0745bd1a9a6c039403d22db3259b6e956566ea3f4650665f35bb?s=64&d=mm&r=g) [Oz](http://www.datascopic.net/)
             says:
            
            [December 11, 2013 at 4:58 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459753)
            
            Right. I was able to find out that the moveBy says how far to move. the i say how many times to move. that was the mystery for me.
            
            [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459753)
            
            *   ![](https://secure.gravatar.com/avatar/5531ce95e6b14c68d0cdd567f3338c8a15fc05c23ad8665c65998e418eff51aa?s=64&d=mm&r=g) Test says:
                
                [December 12, 2013 at 12:59 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459764)
                
                Try adding timedelay
                
                Application.Wait Now + TimeSerial(0, 0, 1)
                
                It worked for me  
                With ActiveSheet.Shapes.Range(Array("btnToggle"))  
                For i = 1 To 25  
                .IncrementLeft moveBy  
                Application.Wait Now + TimeSerial(0, 0, 1)  
                DoEvents  
                Next i  
                End With  
                After some code as well if you are moving the object then it should work  
                Move the object code  
                Task Code  
                Move  
                Code  
                Move  
                end
                
                [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459764)
                
10.  [TechNet Blogs](http://blogs.technet.com/b/southasiamvp/archive/2013/12/10/blog-posts-of-the-week-1st-7th-december-2013.aspx)
     says:
    
    [December 10, 2013 at 9:59 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459740)
    
    \[…\] Making a slick on/off switch using Excel & little bit of VBA \[…\]
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459740)
    
11.  ![](https://secure.gravatar.com/avatar/d5dccf46af83988df0aa771b86e576ae83274b676303b9ad5b6b5f9e6a02a1d1?s=64&d=mm&r=g) Amzo says:
    
    [December 13, 2013 at 9:11 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459770)
    
    Chandoo,  
    Please teach us how to construct the ACME inc Chart. I have attempted but with no success 🙁
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459770)
    
12.  ![](https://secure.gravatar.com/avatar/d5dccf46af83988df0aa771b86e576ae83274b676303b9ad5b6b5f9e6a02a1d1?s=64&d=mm&r=g) Amzo says:
    
    [December 13, 2013 at 9:11 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459771)
    
    Chandoo,  
    Please teach us how to construct the ACME inc Chart. I have attempted but with no success 🙁
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-459771)
    
13.  ![](https://secure.gravatar.com/avatar/cc098dbf2d95a6d0331e3dec4fdfc74dc21e48968407f613f1126aa8fd657c42?s=64&d=mm&r=g) [Randy](http://www.excel-4-business.com/)
     says:
    
    [December 19, 2013 at 6:52 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-460400)
    
    This works great in 2010 and above but i get a Run Time error on the ".IncrementLeft moveBy" line in 2007. Many of my clients still use older versions of Excel. Any ideas?  
    Thanks so much for the great articles and info.
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-460400)
    
14.  ![](https://secure.gravatar.com/avatar/cc098dbf2d95a6d0331e3dec4fdfc74dc21e48968407f613f1126aa8fd657c42?s=64&d=mm&r=g) [Randy](http://www.excel-4-business.com/)
     says:
    
    [December 19, 2013 at 7:11 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-460401)
    
    Ahhh.. Works in 2007 when the sheet is unprotected, but the bug only appears when protection sheet is on because the btnToggle shape is locked. So either unlocking this shape, or unprotecting and reprotecting the sheet in the VBA code will solve this bug. (In case anyone else ran into this issue)  
    Thanks for the great button. I will be using it
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-460401)
    
15.  ![](https://secure.gravatar.com/avatar/cc098dbf2d95a6d0331e3dec4fdfc74dc21e48968407f613f1126aa8fd657c42?s=64&d=mm&r=g) [Randy](http://www.excel-4-business.com/)
     says:
    
    [December 19, 2013 at 7:18 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-460402)
    
    (last comment)  
    Also for a smother, slower action, you can try this:  
    If ActiveSheet.Shapes.Range(Array("shpHideSale")).Visible Then  
    moveBy = -0.095  
    With ActiveSheet.Shapes.Range(Array("btnToggle")).Fill  
    .ForeColor.RGB = RGB(33, 33, 33)  
    End With  
    Else  
    moveBy = 0.095  
    With ActiveSheet.Shapes.Range(Array("btnToggle")).Fill  
    .ForeColor.RGB = RGB(0, 176, 80)  
    End With  
    End If
    
    With ActiveSheet.Shapes.Range(Array("btnToggle"))  
    For i = 1 To 200  
    .IncrementLeft moveBy  
    DoEvents  
    Next i  
    End With
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-460402)
    
16.  ![](https://secure.gravatar.com/avatar/d75b2dded123620d1ff6dfa9b7a458edb6eaa3f87950e3daa6570cc253e0163b?s=64&d=mm&r=g) John Hackwood says:
    
    [March 8, 2014 at 9:32 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-473029)
    
    Hamy  
    I long struggled with your question on the storage of tips and code and accessing them. I couldn't find the one answer so I came up with a 3 prong approach....
    
    1) I use Excel as a flat database with columns & dropdowns defining the broadest grouping say VBA, Formulas, Excel Application, Pivot Tables eg "VBA", then the next column broad grouping eg "Copying Ranges" , then another eg "within the same workbook" and then the detail of the tip plus links if any plus a comment box for long entries. Autofilter and Ctrl+F find allows fairly good access. Perhaps there are other tools but if you are an Excel believer you have to make this work and make it a project in itself that you tinker with over time. I tried MindMaps and MS Notes in the past but it gets all too hard as the topic is just too big.  
    2) I save more complex tips or articles with illustrations as web archive files in structured windows folders - then search these with Windows or maybe there are better tools like Ultrasearch  
    3) Use MZ Tools to save VBA code snippets - this is a double up for me as these snippets are also in my Excel file usually in a comment box associated with a topic but I reserve the code I put into MZ Tools (fantastic tool for VBA it really is) as the standard I use for a particular situation.
    
    Hope this makes sense....if there are better approaches out there I am all ears.  
    Cheers  
    John Hackwood
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-473029)
    
17.  ![](https://secure.gravatar.com/avatar/c86ad1a76d05c7a95abb47bd24ebb40c01526cacfb56c453c0d17268e6751f26?s=64&d=mm&r=g) Dhiraj says:
    
    [March 23, 2014 at 3:50 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-475419)
    
    Hi Chandoo,
    
    As much as I love going through your new Excel templates and tutorials, I feel that your instructions are almost always incomplete. It is may be because I am a novice and will take some time to get a hang of it. I know you are trying to make everyone awesome in Excel but you seem to be targeting on the advanced users.
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-475419)
    
18.  ![](https://secure.gravatar.com/avatar/06f1553c9066b69d4ee545a1550c8773b0986cea6feec2811bb0b826f47a65d4?s=64&d=mm&r=g) Matt says:
    
    [February 20, 2015 at 12:15 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-916863)
    
    Hi Chandoo,
    
    Thanks so much for this toggle switch idea! I have used it a bunch of times and it works great.. the one problem I find though is that if you are zoomed in or out on your spreadsheet, then the button breaks and ends up out of wack.. any way you can think of addressing this?
    
    Thanks again!
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-916863)
    
19.  ![](https://secure.gravatar.com/avatar/c053b4274c08d78fe6c5b2af0cb781a9c98cfa123f2e16f1f075f86afbc05c3e?s=64&d=mm&r=g) Suvadip says:
    
    [December 18, 2015 at 2:38 am](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1107648)
    
    This is very cool! Just borrowed the idea for one of my work. Wanted to say thanks!
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1107648)
    
20.  ![](https://secure.gravatar.com/avatar/e17acae5ea00991570a9b376ab07818d51d592f47dc13f58479c2f123dcb96c5?s=64&d=mm&r=g) Don says:
    
    [October 4, 2016 at 7:47 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1303680)
    
    Chandoo,  
    I use these slide buttons all the time. They work so much better than any activeX control. And they look much better too!
    
    However, I have a question. I want to write code that checks the buttons (I have 30 of them on the same worksheet) to see if they are on or off. If they are on, turn them off (on is green, off is black), but if they are off, leave them off and ignore that button. How can I do that?
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1303680)
    
21.  ![](https://secure.gravatar.com/avatar/cb9aab5120db8a635e6855e1772e2a04d9afca63886e65da3b0c8af8ce192977?s=64&d=mm&r=g) Jose says:
    
    [December 8, 2019 at 12:19 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1719802)
    
    Could I get to download the graph example, which is displayed in the beginning?  
    regards
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1719802)
    
22.  ![](https://secure.gravatar.com/avatar/b9594dc27de4cdf58ce2946f6b91276524b5af0b1686e7d005eeefc81388cd16?s=64&d=mm&r=g) Jo says:
    
    [January 25, 2020 at 4:45 pm](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1732684)
    
    Could I get to download the graph example which is displayed in the beginning?  
    Thanks
    
    [Reply](https://chandoo.org/wp/on-off-switch-in-excel-vba/#comment-1732684)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/on-off-switch-in-excel-vba/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ