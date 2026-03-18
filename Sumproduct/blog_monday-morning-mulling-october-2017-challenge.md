# Monday Morning Mulling: October 2017 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-october-2017-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: October 2017 Challenge

*   October 29, 2017

Monday Morning Mulling: October 2017 Challenge
==============================================

Monday Morning Mulling: October 2017 Challenge
==============================================

30 October 2017

Last Friday, we proposed one of the most puzzling challenges that we’ve had encountered so far. To dynamically pull data from this [Hockey site](http://www.quanthockey.com/khl/seasons/2017-18-khl-players-stats.html)
 using Power Query. The solution will be broken down into four parts. You are welcome to skip right to the end and copy our code, but it is worth knowing how all of the segments fit together too – especially if you encounter a similar problem.

**_Part 1: Manual Retrieval of Data_**

Before we move on to our proposed solution, we should first cover how to manually import data from the hockey statistics site. Do note that this method does not yield the complete list; this will be detailed later on. Without further ado, on to this rather manual method…

To manually import the data from this hockey statistics site http://www.quanthockey.com/khl/seasons/2017-18-khl-players-stats.html using Power Query, first open Excel then navigate to the ‘Data’ tab and click on the ‘New Query’ option, then select the ‘Other Sources’ option followed by ‘Web’, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/8535bc6b1dc65d316de47fb3a2ee32bf.jpg)

A dialog box will appear, allowing us to insert the URL. Next, click ‘OK’ (ground breaking stuff I know):

![](https://sumproduct.com/wp-content/uploads/2025/05/59d7eca6415bab59c9903c793cdd58d8.jpg)

The ‘Navigator’ dialog box will appear, allowing us to select exactly which table to pull data from. At this point all looks good, however we should name the table, so click on ‘Edit’:

![](https://sumproduct.com/wp-content/uploads/2025/05/7e4e50d017dcd19c6850b6fdfa06d718.jpg)

In the Query Editor dialog box, we should give our query a friendly name, let’s say ‘Hockey Data’, then select ‘Close & Load’:

![](https://sumproduct.com/wp-content/uploads/2025/05/4e5e1e95bdf2e1cde30b594993b438bf.jpg)

All seems to have worked well, however upon closer inspection, we can see that Power Query was only able to retrieve the first 50 entries.

![](https://sumproduct.com/wp-content/uploads/2025/05/39e460ad5281a89a1c4a83700497961c.jpg)

This is because Power Query retrieves data based on the URL, and in this case our Power Query friendly hockey statistics website displays data using JavaScript. Hang on, how does all this make any sense? Let’s stop speaking in nerd! Let me explain…

This website uses JavaScript code to dynamically refresh the list of players on one page, this enables the webpage to dynamically refresh the player list in one page, without changing the webpages’ URL. Additionally, we also do not know how many pages of data this website has.

Therefore, to summarise, we have three key issues:

1.  We are unable to manually pull data from the website
2.  We do not know how many pages of data the website has (and this may change over time)
3.  The webpage does not change its URL when a new page of data is displayed.

Not to worry, we do have a work around all of these things but let’s deal with one issue at a time.

You can find a worked solution of this part [here](https://sumproduct.com/assets/blog-pictures/2017/final-friday/oct-17/final-friday-fix---part-1-worked-solution.xlsx)
.

**_Part 2: Custom Functions_**

Turning to the first issue identified, it’s been noted that we are unable to manually retrieve all of the data just by importing it into Power Query.

The proposed solution, provided by Reza Rad is to utilise custom functions in Power Query. A custom function is a query that is run by other queries, those of you who know JavaScript, it is similar to what is known as an Object Method. The benefit of having a custom function is that we can repeat the same number of steps applied to the data set.

Let’s work through a simple example to illustrate a custom function’s utility. For instance, we wish to retrieve the gross earnings of all of the movies were released in that year, along with their current rank and their studio. It does not matter which year we wish to begin with, so for this example we shall begin with 2017. I am going to use the link [http://www.boxofficemojo.com/yearly/chart/?yr=2017&p=.htm](http://www.boxofficemojo.com/yearly/chart/?yr=2017&p=.htm)
 for this illustration.

To launch Power Query / Get & Transform, launch Excel (we are using Excel 2016 here), head to the Data tab and select ‘New Query’:

![](<Base64-Image-Removed>)

Use the default options, paste in the URL and click ‘OK’.

![](<Base64-Image-Removed>)

A dialog box will appear, prompting the selection of the table. We select ‘Table 1’ and then click on ‘Edit’.

![](<Base64-Image-Removed>)

Now that we have the Query Editor window open we can define our parameter. Parameters are needed for custom functions to work.

![](<Base64-Image-Removed>)

We create a simple parameter, set the name to ‘Year’ type to ‘text’ and the initial value to 2017:

![](<Base64-Image-Removed>)

We can now add a custom column to ‘Table 1’, click on ‘Table 1’, then on the ‘Add Column’ tab and then ‘Custom Column’:

![](<Base64-Image-Removed>)

We give the custom column a name ‘Year’ and make it equal to the parameter ‘Year’.

![](<Base64-Image-Removed>)

Be sure to change the custom column’s data type to ‘Text’ too:

![](<Base64-Image-Removed>)

The next step is to integrate our Parameter into the URL. Integrating the Parameter into the URL allows us to dynamically change the URL, ultimately altering the source of the data base on the desired year.

With ‘Table 1’ selected, we click on the setting icon for the ‘Source’ step in the ‘Applied Steps’ section:

![](<Base64-Image-Removed>)

Now let’s select the ‘Advanced’ option. Identify the part of the URL that has the date, and enter the parameter in its place. We should also include the last element of the URL after the ‘Year’ parameter. We do this by ‘Adding Parts’ to the URL and some copy and paste work.

Once that is done click ‘OK’:

![](<Base64-Image-Removed>)

We now have to convert the query into a function. Right click on the ‘Table 1’ query then select ‘Create Function…’:

![](<Base64-Image-Removed>)

Name the function ‘GetMovies’ then click ‘OK’.

![](<Base64-Image-Removed>)

There is now a group folder containing the original ‘Table 1’ query, the Year 2017 parameter, and the ‘GetMovies’ function.

![](<Base64-Image-Removed>)

We have created a copy of the Table 1 query and called it ‘GetMovies’, from now on every time we call on ‘GetMovies’, Power Query will perform the same tasks in that order.

For simplicity, we will create a simple generator. We will use the **List.Numbers** function to create our generator. To do this, simply create a new query by navigating to the ‘Data’ tab, ‘New Query, ‘From Other Sources’ and choose ‘Blank Query’. Then enter the following formula in the formula bar:

**\=List.Numbers(2002,16)**

and hit **ENTER**.

![](<Base64-Image-Removed>)

Convert the list into a table using the ‘To Table’ option located in the ‘Convert’ group as shown:

![](<Base64-Image-Removed>)

The default conversion settings will suffice. Lastly, change the data type to ‘Text’.

![](<Base64-Image-Removed>)

With the ‘Query1’ query selected, invoke a custom function by going to the ‘Add Column’ tab and select the ‘Invoke Custom Function’ in the ‘General’ group:

![](<Base64-Image-Removed>)

Name the new column to ‘GetMovieData’, select the **GetMovies** function and click ‘OK’:

![](<Base64-Image-Removed>)

A new column will be added:

![](<Base64-Image-Removed>)

Clicking on each individual Table will reveal the movie data for its corresponding year! Let’s check out 2006 for example:

![](<Base64-Image-Removed>)

There are some limitations however:

*   Editing the **M** script of the function will cause the function and query to collapse
*   Custom functions cannot be scheduled to update in Power BI.

Having reviewed the above, click on the ‘Expand’ option as shown:

![](<Base64-Image-Removed>)

Reveals this compiled table with the top 100 movies of each year:

![](<Base64-Image-Removed>)

The data still needs some cleaning up however, you can learn how to do that by reading our Power Query blog [here](https://www.sumproduct.com/thought/power-query-blog-series)
.

So this deals with manual importation of the data. However, what about the page number issue? That’s next, but first you might want to review a worked solution of this part [here](https://sumproduct.com/assets/blog-pictures/2017/final-friday/oct-17/final-friday-fix---part-2-worked-solution.xlsx)
.

**_Part 3: Unknown Number of Pages_**

The solution to this problem was produced by a combined effort of Matt Mason, his blog post can be found [here and here](https://www.mattmasson.com/2014/11/iterating-over-an-unknown-number-of-pages-in-power-query/)
.

Matt Mason’s method (from 2014) adopts a brute force method where it instructs Power Query to run through pages 1 to 10,000 and stop when Power Query runs into an error or a ‘null’ value. He points out that if this method is used together with a third-party software such as Fiddler (more on Fiddler later), Power Query will be found trying to evaluate all 10,000 pages. Furthermore, if you try Matt’s method now with the newest version of Power Query, you will receive an error claiming that you do not have access to the database. We need to modify!

This is where Miguel comes in and adjusts the code a little so that it does not adopt the brute force method anymore as well as fix the permissions bug in Power Query.

Building up from Matt Mason’s model, we will only utilise his **GetData** function. Open Power Query from Excel and let’s convert Matt’s **GetData** query into a function:

![](<Base64-Image-Removed>)

Now we create a whole new Query, using a ‘Blank Query’. The first line of code to be entered is the **List.Generate** function:

**\=List.Generate( ()=>**

The ()=> function nomenclature essentially says that we will define a function with no parameter.

![](<Base64-Image-Removed>)

The next line is:

**\[Result= try GetData(1) otherwise null, Page = 1\],**

This line uses Matt’s original function; however, it throws in an error check. Essentially, try to **GetData**: if it returns an error, return ‘null’ in Page 1:

![](<Base64-Image-Removed>)

The next line:

**each \[Result\] <> null,**

specifies a condition, where the result cannot be null or perform this function as long as the Result is not equal to null.

![](<Base64-Image-Removed>)

The next line increments the page to page 2:

**each \[Result = try GetData(\[Page\]+1) otherwise null, Page = \[Page\]+1\],**

![](<Base64-Image-Removed>)

The last line in this function instructs Power Query to display the **Result** field:

**each \[Result\])**

Once we hit **ENTER**, we will see the list of tables:

![](<Base64-Image-Removed>)

This is all of the different pages pulled of the domestic gross of 2016 from the Box Office Mojo website. Notice that Power Query does not try to evaluate 10,000 pages!

Now we go through the table and define each column’s data type. While this is still a list, we can transform this into a table and expand the data:

![](<Base64-Image-Removed>)

Once the table has been transformed we can expand the table:

![](<Base64-Image-Removed>)

The expanded table should look something like this.

![](<Base64-Image-Removed>)

Closing and loading will not result in an error but instead all of the movie data from the year of 2016 from the Box Office Mojo website:

![](<Base64-Image-Removed>)

You can find a worked solution of this part [here](https://sumproduct.com/assets/blog-pictures/2017/final-friday/oct-17/final-friday-fix---part-3-worked-solution.xlsx)
. Now that we have dealt with the page number issue, we can now move on to the final bit…

**_Part 4: Fiddling with the URL, Fiddle(r) with the URL_**

Head over to Telerik’s software [page](https://www.telerik.com/fiddler)
 to download Fiddler, don’t worry it will only install Malware so that we can track all of your activities on your computer… When Windows has finished installing Fiddler, open it and the page should look something like this:

![](<Base64-Image-Removed>)

As the prompt “Please select a single Web Session to impact” suggests we will open a window in a Chrome, you can actually use any web browser – we are just using Chrome for this example.

Go ahead and navigate to the Hockey statistics website again (url: [http://www.quanthockey.com/khl/seasons/2017-18-khl-players-stats.html](http://www.quanthockey.com/khl/seasons/2017-18-khl-players-stats.html)
) and we will start to see some interesting things appear on Fiddler:

![](<Base64-Image-Removed>)

Fiddler takes the source of the URL and displays is it here. Let’s see what happens when we try page 2 of the Hockey Stats. Fiddler now returns with an alternate URL:

![](<Base64-Image-Removed>)

It seems to have been broken down into Seasons, and potentially pages? Let’s copy it and save it on to an Excel spreadsheet to aid us in discovering any patterns. Right click the line of URL and select ‘Copy just URL’.

![](<Base64-Image-Removed>)

After repeating the process, a couple of times, we spot a pattern. Fiddler is able to retrieve the URL and break it down into pages! This is great news, we can finally use this to work with Power Query!

![](<Base64-Image-Removed>)

Now for the final part where we combine everything together.

The first step is to create a new query in Power Query and create a new parameter:

![](<Base64-Image-Removed>)

Name the parameter **PageNumber**, set it to a ‘Decimal Number’ type, and give it a current value of 1:

![](<Base64-Image-Removed>)

Now create a new ‘Blank Query’ and paste the original code from Matt Mason into the formula bar:

**Source = Web.Page(Web.Contents(“http://boxofficemojo.com/yearly/chart/?page=” & Number.ToText(page) & “&view=releasedate&view2=domestic&yr=2013&p=.htm”)),**

Then modify it using the new URL provided from Fiddler:

**\=Web.Page(Web.Contents(“http://www.quanthockey.com/scripts/AjaxPaginate.php?cat=Season&pos=Players&SS=2017-18&af=0&nat=2017-18&st=reg&sort=P&so=DESC&page=2&league=KHL&lang=en&rnd=167379793&dt=1”))**

We also have to include the **PageNumber** parameter and the **Text.From** Power Query function to ensure that it is inserted into the URL as a text format. The following code should replace the page number (in case you were wondering, the ampersand symbols mean concatenate):

**\=**“**&Text.From(PageNumber)&”**

yielding this:

**\=Web.Page(Web.Contents(“http://www.quanthockey.com/scripts/AjaxPaginate.php?cat=Season&pos=Players&SS=2017-18&af=0&nat=2017-18&st=reg&sort=P&so=DESC&page=”&Text.From(PageNumber)&”&league=KHL&lang=en&rnd=276273473&dt=1”))**

![](<Base64-Image-Removed>)

As you can see, the **PageNumber** parameter has been linked into the URL. Hit **ENTER** and Power Query will return with a condensed table, the next step is to select the top right ‘Table’ option:

![](<Base64-Image-Removed>)

This will expand the table resulting in a table that only imports data from the first page, or the first 50 records:

![](<Base64-Image-Removed>)

Create a new blank query and copy this code in. It is a modified version of Matt’s **GetData** function for our purpose:

**\= (PageNumber as number) => let**

        **Source = Web.Page(Web.Contents(“http://www.quanthockey.com/scripts/AjaxPaginate.php?cat=Season&pos=Players&SS=2017-18&af=0&nat=2017-18&st=reg&sort=P&so=DESC&page=”&Text.From(PageNumber)&”&league=KHL&lang=en&rnd=276273473&dt=1”)),**

        **Data0 = Source{0}\[Data\],**

        **#”Changed Type” = Table.TransformColumnTypes(Data0,{{“Rk”, Int64.Type}, {“”, type text}, {“Name”, type text}, {“Age”, Int64.Type}, {“Pos”, type text}, {“GP”, Int64.Type}, {“G”, Int64.Type}, {“A”, Int64.Type}, {“P”, Int64.Type}, {“PIM”, Int64.Type}, {“+/-“, Int64.Type}, {“PPG”, Int64.Type}, {“SHG”, Int64.Type}, {“GWG”, Int64.Type}, {“G/GP”, type number}, {“A/GP”, type number}, {“P/GP”, type number}})**

    **in**

        **#”Changed Type”**

The second section of code simply changes the data types accordingly for each column so that you don’t have to do it!

Hit **ENTER** and rename the function to **PageData**:

![](<Base64-Image-Removed>)

Now to incorporate Miguel’s method, create another blank query and copy this code in:

**\= List.Generate( ()=>**

 **\[Result= try PageData(1) otherwise null, Page = 1\],**

    **each \[Result\] <> null,**

    **each \[Result=  try PageData(Page) otherwise null, Page = \[Page\] +1\],**

    **each \[Result\])**

Hit **ENTER** and change the name of the Query to **AllData**:

![](<Base64-Image-Removed>)

This time there are no modifications needed in the code! Time to convert this list into a table.

![](<Base64-Image-Removed>)

Once Power Query has converted it into a table, we can expand the table:

![](<Base64-Image-Removed>)

Expanding the table should yield this result, where Power Query is able to compile the entire list of Hockey players, not just the first 50:

![](<Base64-Image-Removed>)

We can now proceed to ‘Close & Load’.

![](<Base64-Image-Removed>)

There you have it, all 829 Hockey Player stats (as at the time of writing) in one worksheet!

![](<Base64-Image-Removed>)

Until Microsoft introduces a new built in feature to circumvent all this nasty coding we will just have to suck it up and go through this entire process! Hopefully, you have found this useful, and if you have a better solution please do let us know at [contact@sumproduct.com](mailto:contact@sumproduct.com)
.

We would like to thank [Reza](http://radacad.com/)
, [Miguel Escobar](https://www.youtube.com/watch?v=vhr4w5G8bRA)
, Matt Mason, and Simon Sabin for all contributing to this solution. More next month.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-october-2017-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-october-2017-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-october-2017-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-october-2017-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-october-2017-challenge/#0 "close")

top