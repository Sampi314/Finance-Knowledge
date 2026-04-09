# The IMAGE function

**Source:** https://www.fullstackmodeller.com/blog/image-function-excel

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/The%20IMAGE%20function%20-%20Insert%20Pictures%20in%20Cells.png)

The IMAGE function - Insert Pictures in Cells
=============================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Mar 3, 2023 1:30:00 PM

Microsoft announce exciting new IMAGE function

_Announced by Microsoft on 21st February 2023_

In this latest article in our Future of Excel series, we look at the new IMAGE function.

Ever wished you could bring an image directly into a cell in your Excel spreadsheet via a formula rather than manually inserting it? Well, now you can! 

So how does it work?
--------------------

The image is imported and sized using the new IMAGE function:

  
**\=IMAGE(source, \[alt\_text\], \[sizing\], \[height\], \[width\])**

*   **_Source_****:** The URL path, using an "https" protocol, of the picture file. _Supported file formats include BMP, JPG/JPEG, GIF, TIFF, PNG, ICO, and WEBP._ 
*   **_alt\_text_****:** A description of the picture for accessibility. 
*   **_sizing_****:** The picture dimensions. There are several possible values: 
    *   0: Fit the picture in the cell and maintain its aspect ratio. 
    *   1: Fill the cell with the picture and ignore its aspect ratio. 
    *   2: Maintain the original picture size, which may exceed the cell boundary. 
    *   3: Customize the picture size by using the _height_ and _width_ arguments. 
*   _**height and width:** Only a_pplicable when sizing option 3 is selected, define the height and width of the picture.  

### Here's a simple example

I would like to bring the Full Stack Modeller logo below into my model.

![Full Stack Modular Feature Images](https://www.fullstackmodeller.com/hs-fs/hubfs/Full%20Stack%20Modular%20Feature%20Images.webp?width=738&height=552&name=Full%20Stack%20Modular%20Feature%20Images.webp)

The logo is stored here:

[https://www.fullstackmodeller.com/hubfs/Full%20Stack%20Modular%20Feature%20Images.webp](https://www.fullstackmodeller.com/hubfs/Full%20Stack%20Modular%20Feature%20Images.webp)

The formula to bring this image into my Excel spreadsheet with an Alt Text of "Full Stack Modeller" and a sizing of 200 by 300 is:

\=IMAGE("https://www.fullstackmodeller.com/hubfs/Full%20Stack%20Modular%20Feature%20Images.webp", "Full Stack Modeller", 3, 200, 300)

![IMAGE Function](https://www.fullstackmodeller.com/hs-fs/hubfs/IMAGE%20Function.gif?width=3036&height=1014&name=IMAGE%20Function.gif)

### My thoughts

This is a very helpful new feature from Microsoft. The ability brings images straight into a workbook via a formula will undoubtedly prove useful to anyone who regularly works with images in their spreadsheets.  

It is a shame that you can only bring images in from HTTPS addresses rather than from a local drive, or from within the model itself. Hopefully, this will be added to the IMAGE function in the near future.

### Release date

The feature is currently available in the 365 version of Excel.

Our Future of Excel series  

-----------------------------

This series of articles focuses on new features recently released or soon to be released in Excel. See the announcement from the [Microsoft Tech Community](https://techcommunity.microsoft.com/t5/excel-blog/insert-pictures-in-cells-with-the-image-function/ba-p/3748692)
 team.

See other articles in our Future of Excel series [here](https://www.fullstackmodeller.com/blog/future-of-excel)
. 

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fimage-function-excel)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fimage-function-excel)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fimage-function-excel)
    

![Award_Winning](https://www.fullstackmodeller.com/hubfs/badge.jpg)

Become a Modelling Pro
----------------------

Join us and we'll unlock your full potential.

Our award-winning training programme, and exclusive global community, will guide you on your way to Excel, Financial Modelling, data visualisation & analytics mastery.

[Join as an Individual](https://www.fullstackmodeller.com/full-stack-membership)
 [Register Your Team](https://www.fullstackmodeller.com/team-training)

Latest Blogs
------------

*   [New Year, New You?](https://www.fullstackmodeller.com/blog/full-stack-modeller-new-year-new-you)
    
*   [New Import Functions](https://www.fullstackmodeller.com/blog/excel-importtext-importcsv)
    
*   [Best Practice Confessions & Terminology Overload](https://www.fullstackmodeller.com/blog/unpivot-episode-40-full-stack-modeller)
    
*   [Excel Meetup Groups](https://www.fullstackmodeller.com/blog/excel-meetup-groups)
    
*   [New Features and Common Data Problems](https://www.fullstackmodeller.com/blog/unpviot-episode-39)
    
*   [More AI Hype and Traps to avoid when modelling](https://www.fullstackmodeller.com/blog/unpviot-episode-38)
    
*   [The Excel World Championship Song](https://www.fullstackmodeller.com/blog/excel-world-championship-song)
    
*   [The Advanced Financial Modeler Certificate from FMI](https://www.fullstackmodeller.com/blog/advanced-financial-modeler)
    
*   [The history of Microsoft Excel](https://www.fullstackmodeller.com/blog/history-of-excel)
    
*   [My main learning from the FMI AFM exam](https://www.fullstackmodeller.com/blog/financial-modeling-institute-fmi-afm-learnings)
    

#### Subscribe to our monthly modelling newsletter