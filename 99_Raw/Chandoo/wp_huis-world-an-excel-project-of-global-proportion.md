# Chandoo.org, Hui's, World, Excel, Chart, Advanced, Animated, Globe

**Source:** https://chandoo.org/wp/huis-world-an-excel-project-of-global-proportion

---

*   [3D Maps (non Power Maps)](https://chandoo.org/wp/category/3d-maps-non-power-maps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Hui’s World ! – An Excel Project of Global Scale.
=================================================

*   Last updated on December 1, 2018

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Following the completion of my [3D Dancing Pendulum](https://chandoo.org/wp/3d-dancing-pendulums/)
 in 2011 I have had three follow up Excel projects in mind.

This post explores the first of them, **Hui’s World**.

**Hui’s World is an animated Excel Chart which displays the Earth and key features.  
**

[https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World-Rot-Full.mp4](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World-Rot-Full.mp4)

Hui’s World consists on an Excel chart comprising 111 series containing 2,775 data points. The 111 series are supported by 380 Named Formula. The rotation is driven by 10 lines of VBA code.

Hui’s World displays the following items:

*   The planar projection of the World as a Sphere with a select number of countries/continents;
*   The lines of Latitude and Longitude, International Date Line and Greenwich datum line (Prime meridian) and Arctic/Antarctic circles;
*   Major cities throughout the world;
*   The location of all the Chandoo.org Excel Ninja’s;
*   The States boundaries and State Capital cities in Australia;
*   Labels of Latitude, Longitude and Key Global points and optionally;
*   A User Defined Location (Marker and Label)

The globe can be rotated manually or animated with user control of the speed and direction of the rotation.

Many of the above items can be toggled to be displayed or be hidden, even as the globe turns using toggle buttons.

The Country boundaries, Cities and Lines of Longitude can be shown as if the earth is transparent or they can be hidden as they pass around the back of the earth from your view point.

There are a number of predefined views for major countries/continents and other features.

This post will look at how Hui’s World was constructed.

It will not be focusing on the math behind model, but that will be mentioned from time to time where it is important.

**Apology**: In simplifying the world to 2,775 points, compromises have been made. So if your Country, City etc is missing, simplified or merged to your neighboring countries I apologize in advance.

### Download

If you want to download Hui’s World click here: [Download Hui’s World](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World.xlsm)
; [Download Hui’s World Pre Excel 2007](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World.xls)

If you want to download the Helper File click here: [Download Hui’s World Helper File](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World-Support-Data.xlsm)

* * *

Coordinate System
-----------------

Hui’s World uses an Excel Scatter Chart as the basis of the Chart.

Excel scatter charts do not understand latitudes and longitudes, they only understand a standard orthogonal x & y grid. As such we need to convert the data into the system that Excel understands.

Excel performs the trigonometry functions according to the Anti-clockwise rule.

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Positive-angles.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Positive-angles.png)

The World uses a similar coordinate system where the base or 0 Azimuth is the Greenwich time line. All Azimuth values are taken from here.

![](<Base64-Image-Removed>)

As such we can use the Latitude and Longitudes for the locations and apply some math to work out where things should be plotted.

As such we need to determine the Location of each point of each data item and how it will be plotted on a 2D X/Y plane. I have assumed that we will look at the globe from a point level with the equator.

* * *

Data
----

Data was required for the location of all the elements required to be displayed. Data for the project was sourced from freely available sources.

This includes:

| Data | Source |
| --- | --- |
| Countries | [https://www.naturalearthdata.com/](https://www.naturalearthdata.com/) |
|     | [http://thematicmapping.org/downloads/world\_borders.php](http://thematicmapping.org/downloads/world_borders.php) |
| Cities | [https://www.worldatlas.com/travelaids/citysearch.html](https://www.worldatlas.com/travelaids/citysearch.html) |
| Circles of the Earth | [https://en.wikipedia.org/wiki/Circle\_of\_latitude](https://en.wikipedia.org/wiki/Circle_of_latitude) |
| Date Line | [https://ithoughthecamewithyou.com/post/international-date-line-longitude-latitude-coordinates](https://ithoughthecamewithyou.com/post/international-date-line-longitude-latitude-coordinates) |

Even though the Country data is Low Resolution, the original file still contained 26,264 points.

Before I even started I knew that I would have to simplify this data set, if for no other reason than moving twenty thousand points in an Excel chart would have speed implications.

As a Mining Engineer I have access to a number of mining / GIS related software tools.

I used one of these, to allow me to import the various GIS files, edit the files and save the edited data out as a CSV file type.

I could have also used any CAD style program just as simply.

* * *

### World Coordinates

The World Country Co-ordinates file was a CSV File containing the Latitude and Longitude coordinates and Names for all the worlds countries.

As a CSV File I imported it into a mine planning package as X & Y values.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW001.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW001.png)

Next I manually digitised around the key countries and continents I wanted to display. Whilst digitising I snapped to points to ensure a basic level of geographical accuracy.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW002.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW002.png)

This resulted in a simpler file that now only contained 1,400 points.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW003.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW003.png)

The new simpler file was written out as a CSV file.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW007.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW007.png)

Most CAD package could have been used to perform this.

In fact a number of Free Online websites also offer SHP to CSV file conversion

eg: [https://mygeodata.cloud/converter/shp-to-csv](https://mygeodata.cloud/converter/shp-to-csv)

Working with the Latitudes and Longitudes in an X/Y Display system results in the file being displayed in an Equirectangular projection, with exaggerated distances in the Lower and Higher Latitudes. ie: Greenland isn’t that large. In this case that doesn’t matter as the resultant file is saved in Latitudes and Longitudes and it is the Latitudes and Longitudes that are read into Excel and then converted to X/Y values on a Spherical projection where they appear in the correct locations.

### Australian Coordinates

I repeated the process for Australia and included the states. This took the source file with 108,000 data points down to a manageable 210 data points.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW004.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW004.png)
 [![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW005.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW005.png)

This data was also written out as a CSV file.

These CSV File contained columns of Line ID, Latitudes, Longitudes and sometimes other data.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW007.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW007.png)

ie: ID 1 in the first column above is Western Australia and ID 2 is Northern Territory etc

### International Time Line and Major Cities

I used a similar process to that described above downloading a set of co-ordinates for the International Date Line as well as Major Cities of the world.

### Chandoo.org Ninja Location Data

The Chandoo.org Ninja locations was sourced from Chandoo.org and the Cities coordinates manually sourced from [World Atlas.com](http://https//www.worldatlas.com/travelaids/citysearch.html)
 and saved in Excel.

* * *

Import and Standardisation of Data
----------------------------------

The text files above were imported into Excel as Comma Delimitered Text Files and cleaned up.

Header and Footer lines were removed, Segment break lines were cleared and The Names were shifted to the First Column.

Next was to standardise the data.

The GIS data downloaded came in a number of formats. Most typically Longitudes are expressed in terms of Degrees East (positive) and Degrees West (negative) from the Prime Meridian.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW008.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW008.png)

For the purposes of use in Excel it was simpler to simply have the Longitudes expressed as degrees of a circle ie: starting at 0 deg at the Prime Meridian and extending to 360 deg. I choose to use East as Positive as I am used to having Perth as +115 Deg in my day job.

This was done using a helper column where required.

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW010.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW010.png)

Eg: **E3**: =360+D3

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW011.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW011.png)

Similarily with Latitudes, some data was sourced where zero degrees was North pole and 180 deg was the South pole.

See Column B below

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW012.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW012.png)

The data was standardised to have Zero degrees at the equator with positive 90 Deg at the North Pole and –90 Deg at the South Pole.

![](<Base64-Image-Removed>)

Once again helper cells were used if required to transform the data to this format.

Note the Formula in **C1043**: =90-B1043

![](<Base64-Image-Removed>)

Any system of locations could have been used. I just choose to use what I am familiar with. With other coordinate systems the math would need to be set up accordingly.

* * *

Use of Named Formula
--------------------

To add animation to the system we will need to have the following data sets

*   Original data, Latitudes and Longitudes
*   Transformation data, Details of the required view azimuth
*   Transformed data, The transformed data after the Transformation data is applied to the Original data.
*   Projected data, The Projection of the transformed data onto a 2D viewing plane

Once we have the projected data we can plot the data.

By changing the transformation data above and recalculating the worksheet, the chart will update and give the user the impression of animation.

But for this to work smoothly it needs to be fast.

One of the main skills I learned from completing \[sic\] the Excel Hero Academy was the benefit of using Named Formula. Named Formula store data in arrays that are stored in Memory. As such they don’t need to access the Excel grid and so performance is significantly improved.

But as I already have point data for 25 countries, 7 Australian States, 36 Lines of Longitude and 17 lines of Latitude, Cities of the World, Australian Capital Cities and the Chandoo.org Ninjas, and need between 4 and 5 sets of data for each plotted line, resulting in a total of 374 Named Formula, I could see that if I wasn’t organised and methodical this could become a real mess.

What was needed was a Named Formula Naming Convention.

* * *

Named Formula Naming Convention
-------------------------------

To plot a line on a Scatter Chart within Excel we need to obtain the X & Y coordinates for each point along the line.

The data we have imported is a series of Latitude and Longitudes for each point.

Each line on the chart will be a Chart Series and will be made up of an array of x and an array of y values

Each Array of x and y values will be derived from the appropriate Latitudes and Longitudes. And each series may need a list (array) of values for annotation, eg: City names.

The following naming convention was setup and used for the project

Data type\_Name\_Type of data

Hence

**Data Types** used:

Countries,           **C**

Cities,                  **Cit**

Ninja’s                 **Nin**

Latitude Line,   **Lat**

Long Lines,        **Lon**

Other Lines         **o**              Other data

Variables             **v**              Used to store variables to interact between the user controls, VBA and the Named Formula

Boolean               **b**             Boolean switches to toggle controls on/off

**Names** used:

Africa, Japan, etc

**Type of Data**:

Latitude               Lat

Longitude            Lon

X Value                 x

Y Value                 y

Names                  Nam

A Separator of an \_ (underscore) was used to separate the fields

**Example**:

Countries:

C\_Africa\_Lat

C\_Africa\_Lon

C\_Africa\_X

C\_Africa\_Y

Cities:

Cit\_CoW\_Lat

Cit\_CoW\_Lon

Cit\_CoW\_X

Cit\_CoW\_Y

Cit\_CoW\_Nam

Lines of Latitude

Lat\_010N\_Lat

Lat\_010N\_Lon

Lat\_010N\_x

Lat\_010N\_y

Lat\_010S\_Lat

Lat\_010S\_Lon

Lat\_010S\_x

Lat\_010S\_y

Lines of Longitude

Lon\_010\_Lat

Lon\_010\_Lon

Lon\_010\_x

Lon\_010\_y

The benefits of using a Naming Convention like this is that in the Name Manager with Excel the Names are grouped and sorted according to there names. As such it simplifies the editing of formula.

* * *

Transforming the Data
---------------------

We can transform the data from Latitudes and Longitudes to X & Y values using some simple math.

Pic

X \= COS(RADIANS(C\_Alaska\_Lat))\*Sin(RADIANS(C\_Alaska\_Lon + View\_Az))

Y = SIN(RADIANS(C\_Alaska\_Lat))

So using Alaska as an example

The following formulas were added next to the top of the data set

![](<Base64-Image-Removed>)

You will notice in the above formula that we need to have a Named Formula setup to store and access the Latitudes and Longitudes for each data set.

Once again to allow for maximum performance it was chosen that the Latitudes and Longitudes would be stored as Named Formula, rather than being accessed directly from Excel ranges.

Using Alaska as an example

**C\_Alaska\_Lat**      \={55.122;57.643;59.151;58.655;60.555;62.417;63.869;65.189;66.448;68.351;70.307;71.163;69.968;69.642;60.307;60.899;57.604;54.941;51.213;55.122}

**C\_Alaska\_Lon**     \={196.677;202.293;203.221;198.887;194.575;195.364;199.223;193.038;198.399;193.172;198.058;204.413;215.048;218.997;219.004;212.925;207.849;200.566;180.895;196.677}

* * *

Named Formula
-------------

### Setup the Named Formula

We can see above that we need to establish at least 4 Named formula and sometimes 5 for each item we wish to plot.

The fifth Named Formula will hold the City Names etc for annotation, where required.

Using Alaska as an example 8 formula were added adjacent to the Country data

These allow for the following constructions

[![](https://chandoo.org/wp/wp-content/uploads/2018/09/HW020.png)](https://chandoo.org/wp/wp-content/uploads/2018/09/HW020.png)

Column A contains the name of our country, in this case Alaska

Column B contains a line identifier that is an artifact from the CAD processing. It has been maintained so that countries could be separated and identified

Column C & D are the Latitudes and Longitudes of the points which were digitised for Alaska

Column E Is the corrected Longitudes of the points which were digitised for Alaska going from 0 to 360 deg

Column G is a list of Named Formula names. Each is constructed suing a formula.

**G3**:         C\_Alaska\_Lat     \=”C\_”&A3&”\_lat”

**G4**:         C\_Alaska\_Lon    \=”C\_”&A3&”\_lon”

**G5**:         C\_Alaska\_x         \=”C\_”&A3&”\_x”

**G6**:         C\_Alaska\_y         \=”C\_”&A3&”\_y”

Column H is a series of formula that will setup the formula for the Named Formula

**H3**:        \=”={“&Concat(C3:C22,”;”)&”}”

\={55.122;57.643;59.151;58.655;60.555;62.417;63.869;65.189;66.448;68.351;70.307;71.163;69.968;69.642;60.307;60.899;57.604;54.941;51.213;55.122}

**H4**:        \=”={“&Concat(E3:E22,”;”)&”}”

\={196.677;202.293;203.221;198.887;194.575;195.364;199.223;193.038;198.399;193.172;198.058;204.413;215.048;218.997;219.004;212.925;207.849;200.566;180.895;196.677}

**H5**:        \=”=COS(RADIANS(“&G3&”))\*COS(RADIANS(“&G4&” + v\_View\_Az))”

\=COS(RADIANS(C\_Alaska\_lat))\*COS(RADIANS(C\_Alaska\_lon + v\_View\_Az))

**H6**:        \=”=SIN(RADIANS(“&G3&”))”

\=SIN(RADIANS(C\_Alaska\_lat))

The Formula in **Columns G & H** are setup to return a Text String, that replicates the formula required for the Name Manager.

The formula in Cells **H3** and **H4** use a User Defined Function, **Concat()**, to append the Latitude and Longitude values into a string with ; as a separator and appropriate ={ and } leading and trailing brackets.

I modified the Concat UDF to allow an optional Surrounding character ” as well as to skip over blank cells.

This change allowed Names to be stored as strings and also allowed large ranges to be uploaded at once

Eg:

\={test1;test2;test3} is not permitted as a Named Formula formula unless test1, test 2 and test3 are existing Named Formula

\={“test1”;”test2”;”test3”} is permitted, as test1 is a Text string.

**H5** & **H6** setup formula to return the X & Y values for each of the Points defining Alaska. Note that these formulas make use of the Named Formula in **H3** and **H4** above them. They also refer to a Named Formula **v\_View\_Az**. We haven’t set this up yet, but don’t worry about that yet. It simply contains the viewing azimuth of the view that the user wants to see the globe from, ie: How far to rotate the data so that it looks like the globe has turned.

### The Concat() UDF

The use of Concat() UDF was described in a previous post at: [Concat](https://chandoo.org/wp/how-to-add-a-range-of-cells-in-excel-concat/)

### Load Named Formula

Finally we need to load these new named formula into the Name Manager

We could do this manually, by selecting each range and ….

No, no no

In one of my previous posts I describe a technique to load named Formula from the worksheet. It is described in:  [Automating Repetitive Tasks](https://chandoo.org/wp/automating-repetitive-tasks/)

The Automating Repetitive Tasks post above also describes the use of a small pieces of VBA Code which will allow these named formula to be uploaded quickly. This code is supplied included in the **Hui’s World** model.

For Alaska Select **G3:G6**

**![](<Base64-Image-Removed>)**

Execute a VBA Macro by using **Alt+F8**

 **![](<Base64-Image-Removed>)**

Select **aa\_Load\_Named\_Ranges** and press **Ok**. The **aa\_** prefix was simply added to the macro’s name so that it appears at the top of the Module List and is hence easier to find. So easy that you don’t need to select it, simply press **Enter**. This will be discussed in the section **Formula Updates**.

The 4 Named Formula selected were just created or updated if they previously existed.

Each Named Formula contains the formula comprised of the text to the right of it in Column H

Now just repeat this for the other Countries, Cities and other details.

Or setup all the countries and other data and upload them all in once step.

The **aa\_Load\_Named\_Ranges** module skips blank lines, so you can setup a whole block of these adjacent to each set of data and then upload the entire lot by selecting say **G1:G2000**, then running the **aa\_Load\_Named\_Ranges** module described above.

* * *

Adding Series to the Chart
--------------------------

Once the Named Formula for the Countries, Cities and Date Lines we can add a chart and upload each Country as a series

Select a single cell then got the **Insert** Tab and click on the **Scatter Chart** Icon,

Select any of the Scatter Charts as we will be formatting the Chart’s series later on.

![](<Base64-Image-Removed>)

Take note of the Charts Name

![](<Base64-Image-Removed>)

Each series requires a Name, a Range for X values and a Range for Y Values.

![](<Base64-Image-Removed>)

These are usually entered via the Add Series Dialog shown above.

However as we will require some x & y series to be added it is a lot easier to use some VBA to add the series.

For Alaska we have the Name: **Alaska**, with the X Series: **C\_Alaska\_x** and Y Series: **C\_Alaska\_y**

Again we can do this manually for each of the data sets or we can set this up and then use a small VBA snippet to add all the series to the chart in one go.

To achieve this I will use another code from the Automation post, **Add\_Cht\_Series**

To run this I setup 3 formulas for each series, then copied these down and relink the ranges for the other series

Using Alaska as the example

**I10**:           \=”=”””&A3&””””

**J10**:           \=”=Globe!”&G5

**K10**:          =“=Globe!”&G6

Setup a list of Country names, with adjacent x & Y values named Formula names

Note they are offset from columns **G** & **H** to avoid being uploaded as Named Formula

![](<Base64-Image-Removed>)

You can add other formula for the other ranges below eg: USA and Canada etc

Then Select the First column and run the **Add\_Cht\_Series** macro by pressing **Alt+F8** the select **Add\_Cht\_Series** and press **Run**.

![](<Base64-Image-Removed>)

The Add\_Cht\_Series code will select every cell in the first column and add a New Series to the Chart based on the Values in the 3 Columns I, J & K.

* * *

Lines of Longitude
------------------

Lines of Longitude are the vertical lines or Great Circle Lines that extend North & South from the North Pole to the South Pole.

For each line we know the Longitude it will have as it is a fixed Longitude or Azimuth from the Prime Meridian.

eg: The Longitude +120 Deg is  North South line passing through Western Australia.

Pic

We know that it extends from -90 Deg to +-90 Deg.

So we can use a Named Formula to calculate the Latitudes and the Longitude for the line.

Because the Latitudes of the lines of Longitude are know and are the same for each line of Longitude I setup a Named Formula \_t2

**\_t2**:  \={-90;-80;-70;-60;-50;-40;-30;-20;-10;0;10;20;30;40;50;60;70;80;90}

This named formula of Latitudes can be used for all the lines of Longitude.

We don’t need to store the Longitude for each line as it is fixed

We can directly calculate the X & Y values for each line of Longitude

The X Value is calculated by:

**Lon\_030\_x**: \=COS(RADIANS(\_t2))\*SIN(RADIANS(360-30 + v\_View\_Az))

This is setup as before for all lines of Longitude and uploaded to the Name manager as described before

The Y Value is calculated by:

**\_y2**: \=SIN(RADIANS(\_t2))

The \_y2 Named Formula is then used for all the Lines of Longitude.

That is there is no Named Formula **Lon\_010\_y**, **Lon\_020\_y**, **Lon\_030\_y** etc, as they are all the same **\_y2.**

* * *

Lines of Latitude
-----------------

Lines of Latitude are the horizontal lines that are parallel to the Equator and points on the lines are the same distance from the North or South poles.

For each line we know the Latitude it will have as it is a fixed Latitude or Bearing North or South of the equator.

eg: The Latitude 30 Deg south or -30 Degrees is the East West line passing just north of Perth Western Australia.

Pic

The important part to realise here is that we could easily setup a Named Formula for the Latitude and Longitude for these lines.

Lat\_010S\_Lat:  \={-10;-10;-10 … -10;-10;-10}

Lat\_010S\_Lon: \={0;10;20;30;40 …. 340;350;360} or  =(ROW(OFFSET($A$1,,,37,1))-1)\*10  

and then calculate the X & Y values for each circle.

But there is an easier way.

Because I haven’t implemented vertical tilting of the earth yet, the lines of Latitude will always be straight and extend from one side of the globe to the other.

Knowing this I can cheat and simply workout the starting and finishing x & y coordinates for each line

This is done using the following formula:

**Lat\_S010\_x**:   \={-1;1}\*SIN(RADIANS(100))

\={-0.98; 0.98}

This formula calculates the Sin of the Angle 100 and then multiplies it by the array {-1;1}

In this example this creates the X values of -0.98 and 0.98

Similarily we know the Latitude of the Line of Latitude and so we can use that to calculate the Y Values for each line

Note here that we use the Multiplication array of {1;1}

**Lon\_S010\_y**:   ={1;1}\*COS(RADIANS(100))

\={0.17; 0.17}

In this example this creates the X values of 0.17 and 0.17

Excel then plots these two points as a Flat Line at -10 Deg South, extending from -0.98 to +0.98.

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Line-of-Lat.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Line-of-Lat.png)

Note that we haven’t stored an array of Latitudes and Longitudes saving both a Named Formula and saving calculations

### Circles of Latitude

The same technique described for the Lines of Latitude was applied to the Arctic and Antarctic Circles as well as the Tropic of Cancer and the Tropic of Capricorn lines

The Arctic Circle is located at: North 66.50 Deg, The Antarctic circle is located at South 66.55 Deg.

The Tropic of Cancer is located at: North 23.5Deg, The Tropic of Capricorn is located at South 26.43 Deg.

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Circles-of-Latitude.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Circles-of-Latitude.png)

* * *

Hidden Lines
------------

One of the first issues that arose during construction of the model is that data was being displayed in its normal projection but also in the negative projection as the various objects traveled around the back of the globe as the globe rotated.

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/wohiddenlines.jpg)](https://chandoo.org/wp/wp-content/uploads/2018/10/wohiddenlines.jpg)

Technically this is what would be seen if the Earth was made of Glass.

But this isn’t what we are used to seeing.

I have used two techniques for solving this

### Simple Objects

For simple objects like Lines of Longitude, Markers and Annotation etc, the easiest way was to check the location of the object and if it was behind the earth, simply add a large number so that it plots outside the Plot area for the chart.

As the chart extends from -1 to +1 in both x and y directions, it was as simple as adding a large number say 5 to the data

This is simple and works well with minimal overheads.

It works well in that it shifts the entire object off the Charts’ Plot area.

Eg:

The basic formula for the Lines of Longitude at 210 Deg East:

\=COS(RADIANS(\_t2))\*SIN(RADIANS(360-210 +v\_View\_Az))

The adjusted formula to allow Hidden Line removal:

\=COS(RADIANS(\_t2))\*SIN(RADIANS(360-210 +v\_View\_Az)) \+ 5 \* AND((AND(IF(210<v\_View\_Min,210+360,210) > v\_View\_Max, IF(210<v\_View\_Min,210+360,210)<(v\_View\_Min+360))), b\_View\_Hidden)

The Red part of the formula above is what checks the location of the line of Longitude and if it should be hidden shifts the location off the chart’s plot area (+5). It also incorporates the logic to enable the Toggling on/off of Hidden Lines, using the b\_View\_Hidden name.

Despite being complex, the logic is fairly simple, and it is great for lines of Longitude and for controlling the location of the the various annotations on the chart.

But because of this it can’t be used for when a country or continent starts to move behind the globe. Ideally we want to just hide the bits of the countries as they go off the view plan of the earth, not the whole country.

### Complex Objects

For more complex objects like Countries a number of techniques were investigated, including:

The use of VBA to hide line segments was considered, but that would mean checking every line segment every time the chart is updated. If the segment was behind the Globe, then the fill color of the line could be set to None.

This was dismissed as potentially adding too much overhead to the chart.

The next technique was to plot every line segment as a series of 2 points. Doing this would mean that I could use the same technique that was used for simple objects and simply plot them outside the charts plot area. The downside here was with 1,275 data points there would be 2,550 named formula and 2,550 chart series.

No, there was a better way.

I have been having some conversations with Peter Bartholomew, Peter is well know for his innovative uses of Named Formula.

Peter is a former Senior Fellow at QinetiQ and is internationally known for his research in the area of the optimal design of aeronautics structures, having published over 80 papers. Peter has interests in data management and graphic design that are evident in his use of Excel to capture and convey information. He has made a particular specialty of the programmatic use of shapes in Excel to create diagrams as controls and also moderates a leading Excel Group on LinkedIn. Peter can been seen trolling around the Excel communities at the [Linkedin Excel Hero Group](https://www.linkedin.com/groups/3843467/)
 and here at the [Chandoo.org Forums](https://chandoo.org/forum/)
 amongst others.

Peter suggested changing the x Value of the data for all points behind the earth so that they plot on the boundary of the globe. Then plotting a Black or White circle in front of the earth circumference so that the edge lines were hidden. The good thing about this technique is that only the X Values need to be checked and altered, cutting down processing effort.

Peter then also gave me the formula to implement this:

So using Africa as an example

Original Formula:         =COS(RADIANS(C\_Africa\_Lat))\*SIN(RADIANS(C\_Africa\_Lon+v\_View\_Az))

Hidden Line Formula:   \=IF(COS(RADIANS(C\_Africa\_Lon+v\_View\_Az))>0, COS(RADIANS(C\_Africa\_Lat)) \* SIN(RADIANS(C\_Africa\_Lon+v\_View\_Az)), IF(b\_View\_Hidden, COS(RADIANS(C\_Africa\_Lat)) \* SIGN(SIN(RADIANS(INDEX(C\_Africa\_Lon,1)+v\_View\_Az))), COS(RADIANS(C\_Africa\_Lat)) \* SIN(RADIANS(C\_Africa\_Lon+v\_View\_Az))))

I owe a huge gratitude of thanks to Peter for this assistance on this as it took the visuals from being great to being stunning.

You can see the hidden edges of the countries from behind the globe on the same view as the image above. The Areas of the countries resting on the edge of the globe are highlighted below.

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/whiddenlines.jpg)](https://chandoo.org/wp/wp-content/uploads/2018/10/whiddenlines.jpg)

* * *

**User Defined Locations**
--------------------------

As nice as the display of the world maybe, the project couldn’t cater for every location on the planet.

So I added the ability to display a user selected point from a predefined list or to add a user defined location for a specific point.

I setup 4 predefined locations, Ayers Rock, Great Barrier Reef, Grand Canyons & Pyramids of Cheops.

These are user selectable from a Drop Down menu

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/UDL1.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/UDL1.png)

or by choosing User Defined, the user can define there own location

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/UDL2.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/UDL2.png)

This allows the user to enter the Coordinates and Name for a single point which is then plotted.

In the example above we can see that the Amazon Rain Forest has been plotted at the correct location of -3.8 deg South and 297.5 Deg East.

The User Defined Location is setup using 5 Named Formula:

o\_UDL\_Lat:   \=IF($P$31=”User Defined”,P32,INDEX(o\_UDL\_Latlist,MATCH($P$31,o\_UDL\_NamList,0)))

o\_UDL\_Lon:  \=IF($P$31=”User Defined”,$P$33,INDEX(o\_UDL\_LonList,MATCH($P$31,o\_UDL\_NamList,0)))

o\_UDL\_Nam: \=IF($P$31=”User Defined”,$P$34,INDEX(o\_UDL\_NamList,MATCH($P$31,o\_UDL\_NamList,0)))

o\_UDL\_x:       \=IF(LEN(o\_UDL\_Lat)=0, 2, COS(RADIANS(o\_UDL\_Lat))\*SIN(RADIANS(o\_UDL\_Lon+v\_View\_Az)))

o\_UDL\_y:       =IF(LEN(o\_UDL\_Lon)=0, 2, SIN(RADIANS(o\_UDL\_Lat)))

The Names controlling the Predefined locations are:

o\_UDL\_LatList: \={-25.345,-18.3,36.1,29.98}

o\_UDL\_LonList: ={131.035,147.7,247.89,31.13}

o\_UDL\_NamList: \={“Ayres Rock”,”Great Barrier Reef”,”Grand Canyon”,”Pyramids”}

These contain the locations and Names of the 4 predefined locations.

If **None** is selected as a Predefined location then the User Defined Location is not plotted.

Note the formula has been adjusted so that if the Latitude or longitude cells are blank the data point is plotted off the charts plot area, .

* * *

Annotation
----------

Annotation of the model has been handled in exactly the same way as the countries has been described above except that for the annotation the Series in the Chart have no line, Markers are enabled and set differently for each data type and Data Labels have been used to annotate the points values eg: City Names etc.

In the example below I have set the Australian/NZ Capitals charts series line to be Red instead of None

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/annotate1.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/annotate1.png)

* * *

Formula Updates
---------------

You can see by the shear number of Named Formula that the management of them was a critical aspect of the construction of Hui’s World.

However it was a lot simpler than you may imagine.

I use a technique where the formulas are developed on the worksheet and uploaded into the Name Manager.

Let me demonstrate with two examples

#### Countries

The basic formula for the conversion of the Lat and Long arrays to X & Y for each country are shown by

x value:  \=COS(RADIANS(C\_Africa\_Lat))\*SIN(RADIANS(C\_Africa\_Lon+v\_View\_Az))

y value:  \=SIN(RADIANS(C\_Africa\_Lat))

These two names have to be made for every country

So I setup a list of the 46 countries

Next to the list I added formula to develop both the Named Formula’s Name as well as the Function for the named Formula

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/auto1.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/auto1.png)

Once these formulas are setup I simply select the column of Named Formula Names and run the macro **aa\_Load\_Named\_Ranges**

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Auto2.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Auto2.png)

Using this technique allows very rapid prototyping of new formula

The corresponding X Value formula for the countries is

x value:  \=COS(RADIANS(C\_Africa\_Lat))\*SIN(RADIANS(C\_Africa\_Lon+v\_View\_Az))

This is applied to the list of countries using

\=”COS(RADIANS(C\_“&E368&”\_Lat))\*SIN(RADIANS(C\_“&E368&”\_Lon+v\_View\_Az))”

The x Values formula to allow Hidden lines is

\=COS(RADIANS(C\_Africa\_Lon+v\_View\_Az))>0 COS(RADIANS(C\_Africa\_Lat))\*SIN(RADIANS(C\_Africa\_Lon+v\_View\_Az)) b\_View\_Hidden COS(RADIANS(C\_Africa\_Lat))\*SIGN(SIN(RADIANS(INDEX(C\_Africa\_Lon,1)+v\_View\_Az))) COS(RADIANS(C\_Africa\_Lat)) C\_Africa\_Lon+v\_View\_Az

But using this technique a formula of

\=”=IF(COS(RADIANS(C\_“&E368&”\_Lon+v\_View\_Az))>0,COS(RADIANS(C\_“&E368&”\_Lat))\*SIN(RADIANS(C\_“&E368&”\_Lon+v\_View\_Az)),IF(b\_View\_Hidden,COS(RADIANS(C\_“&E368&”\_Lat))\*SIGN(SIN(RADIANS(INDEX(C\_“&E368&”\_Lon,1)+v\_View\_Az))),COS(RADIANS(C\_“&E368&”\_Lat))\*SIN(RADIANS(C\_“&E368&”\_Lon+v\_View\_Az))))”

is developed once and then applied to the list of countyries

#### Lines of Longitude

Similarily for the X Values for the Lines of Longitude

The formula including allowance for hidden line removal is:

\=COS(RADIANS(\_t2))\*COS(RADIANS(MOD(v\_View\_Az+10,360)))+5\*AND(10>MOD(v\_View\_Max,360),10<MOD(v\_View\_Min,360),b\_View\_Hidden)

In this case a list of 10 to 360 was used

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Auto3.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Auto3.png)

The Named Formula Name and Named Formula Formula were setup as shown above.

Then the entire range was loaded in one pass into the Name Manager using **aa\_Load\_Named\_Formula**

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Auto4.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Auto4.png)

* * *

Controls
--------

A number of controls were included in the model.

These controls allow the following functionality

#### Animation

**View Point Slider** – Allows the rotation of the earth to the desired view point.

This is a simple slider control linked to a Named cell **v\_View\_Az\_Entry**

**Animate/Stop** – Start rotation of the model and once started stops the model

This is a control button and is linked to the Macro: **StartStop**

**<<** / **\>>** – Change direction button

This is a control button and is linked to the Macro: **Change\_Direction**

**Reset** – Reset button. Resets the model to the starting conditions

This is a control button and is linked to the Macro: **Reset**

**Rotation speed** – Allows the change of rotation speed and direction from -10 degrees per step to +10 degrees per step

This is a Spin Control and is connected a a Named Cell: **v\_Rotate\_Speed\_Link**

#### Predefined Views

Six predefined views have been established for viewing the model from preset locations. This includes Australia, the Americas, India, Africa/Europe, The Pacific and Greenwich Time Line (The Prime Meridian).

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Predefined-views2.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Predefined-views2.png)

Each button is a Shaped linked to a macro that rotates the model from the current view point to a pre-defined view point for that position.

example:

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/GotoAustralia.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/GotoAustralia.png)

All code is available in the model, by pressing **Alt+F11**.

#### Feature Display

Check box controls were added to enable or disable the visualization of 7 sets of data.

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Controls1.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Controls1.png)

Each checkbox is connected to a Named Cell on the worksheet.

These names are then available for use in the various formula to hide or view data as appropriate.

* * *

Animation
---------

Animation is achieved by use of a small piece of VBA code that simply adds a value, the rotation speed, **v\_Rotate\_Speed**, to the View Azimuth **v\_View\_Az\_Entry**.

If the new view azimuth is greater than 360 it subtracts 360 degrees from the new view azimuth

If the new view azimuth is less than 0 it adds 360 degrees to the new view azimuth

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Macro1.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Macro1.png)

All code is available in the model by pressing **Alt+F11** to enter the Visual Basic Editor.

The modularisation of the code and use of worksheet cells to store key variables allows for interactive control of the model whilst it is running

that is you can press any of the controls eg: **<<**, **\>>** or the Speed change spinner while the model is running and they will have an immediate effect on the model.

* * *

Chart Background
----------------

The background of the chart was originally set to White and then Black.

However as I regularly use Google Earth, I though of replicating the stars that rotate as the globe rotates behind the Earth in Google Earth, but without the rotation. I was already sick of Rotation by this point.

To achieve this I setup a view in Google Earth that had an appealing background

Then simply took a Screen shot of the Google Earth screen

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Google-Earth1.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Google-Earth1.png)

I then added a Grey Circle to cover the view if the earth, so that only the Background was visible.[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Google-Earth2.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Google-Earth2.png)

This image was loaded as the background to the Chart Area.

This involved a bit of fiddling to get it the right size and centered but I think the impact is much better.

* * *

Future Development
------------------

**Zooming:** It would not be hard to add the ability to zoom in/out on areas of the chart.

**User Defined Data:** Similar to the Point Input it would be easy to add the ability for a user to add a line or number of lines of data including annotation.

**Earth Tilt:** The Earth doesn’t rotate on a vertical axis. The earths rotational axis is tilted about 23.5 deg and is constantly changing. The ability to alter the tilt was considered and then put into the version 2 basket.

ps: I already have a working version of Hui’s World with Axis tilt and will release it quite soon.

[![](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World-2.png)](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World-2.png)

Note the countries are rotating about a 23 deg tilted axis, I haven’t updated the Latitudes or Longitudes as yet.

**Speed Improvements:** I have considered saving the Latitudes and Longitudes in arrays of Radians instead of Degrees. ie: Pre-process the Degrees into Radians before uploading them. This would remove the need to convert the Latitudes and Longitudes to radians on the fly. The downside is that it makes checking and editting formula much more difficult.

* * *

Download
--------

If you want to download Hui’s World click here: [Download Hui’s World](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World.xlsm)
; [Download Hui’s World Pre-Excel 2007](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World.xls)

If you want to download the Helper File click here: [Download Hui’s World Helper File.](https://chandoo.org/wp/wp-content/uploads/2018/10/Huis-World-Support-Data.xlsm)

* * *

Other and Future Animated Excel Posts
-------------------------------------

My previous animated chart is: [3D Dancing Pendulums](https://chandoo.org/wp/3d-dancing-pendulums/)

I have two more advanced chart projects in mind and both are way beyond this project in scope…

The first is at a proof of concept stage and works. The second is still bouncing around in my head.

If you have any ideas or suggestions for similar projects please let me know in the comments below:

* * *

Final Comments
--------------

This project has been on my bucket list for several years. Probably since Keyhole developed what is now Google Earth.

Most of that time was spent on spreadsheet/data design thoughts. The actual implementation time was just under 20 Hours spread over about 3 months. In fact it has taken about twice as long to write this post as it did to develop the model.

I’m quite proud of how it has turned out I would love to hear your thoughts and comments about this model in the comments below.

And a final Thanx to **Peter Bartholomew** for his assistance with the Hidden Line logic.

**Why did I do it? Because they said it couldn’t be done.**

If you have suggestions for other Excel models please also leave them as a comment below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [27 Comments](https://chandoo.org/wp/huis-world-an-excel-project-of-global-proportion/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/huis-world-an-excel-project-of-global-proportion/#respond)
    
*   Tagged under [Advanced Chart](https://chandoo.org/wp/tag/advanced-chart/)
    , [Animated Chart](https://chandoo.org/wp/tag/animated-chart/)
    , [chart](https://chandoo.org/wp/tag/chart/)
    , [Earth](https://chandoo.org/wp/tag/earth/)
    , [Globe](https://chandoo.org/wp/tag/globe/)
    
*   Category: [3D Maps (non Power Maps)](https://chandoo.org/wp/category/3d-maps-non-power-maps/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousLeave entitlement vs. usage analysis with Power Query](https://chandoo.org/wp/entitlement-vs-usage-power-query/)

[NextQuick tip: Make a list of numbers (or dates) in Power Query easilyNext](https://chandoo.org/wp/quick-tip-make-a-list-of-numbers-or-dates-in-power-query-easily/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

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
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/huis-world-an-excel-project-of-global-proportion/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/huis-world-an-excel-project-of-global-proportion/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/huis-world-an-excel-project-of-global-proportion/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ