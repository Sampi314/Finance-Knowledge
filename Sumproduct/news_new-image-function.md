# New IMAGE Function

**Source:** https://sumproduct.com/news/new-image-function/

---

[Home](https://sumproduct.com/)

\> New IMAGE Function

*   August 31, 2022

New IMAGE Function
==================

New IMAGE Function
==================

31 August 2022

In the September update, Excel released the new Image function. Your images can now be part of a worksheet in pretty much any version of Excel (either for the web, or some Insiders Beta variant), instead of floating on top of the cells. You may move and resize cells, sort and filter, and work with images within an Excel table. This improvement unlocks and facilitates many new scenarios, such as tracking inventories, creating employee dashboards or building games and brackets – something I know you are all especially keen to do!

The **IMAGE** function inserts images into cells from a source location, along with alternative text. Its syntax is as follows:

**IMAGE(source, \[alt\_text\], \[sizing\], \[height\], \[width\])**

The arguments are as follows:

*   **source** is required, and represents the URL path of the image file, using an _https_ protocol (it should be noted that supported file formats include BMP, JPG, JPEG, GIF, TIFF, PNG, ICO and WEBP). Upon tinkering, cell references within the workbook appear to be recognised too
*   **alt\_text** is the first optional argument. This is the alternative text that describes the image (for accessibility purposes)
*   **sizing** is also an optional parameter and specifies the image dimensions. There are several possible values:

o **0:** fit the image in the cell and maintain its aspect ratio (default)

o **1:** fill the cell with the image and ignore its aspect ratio

o **2:** maintain the original image size, which may exceed the cell boundary

o **3:** customise the image size by using the **height** and **width** arguments _(see below)_

*   **height** and **width** are optional arguments. These define the height and width respectively of the image only when using **sizing** option 3 _(see above)_.

**_Examples_**

You may insert a sphere into a cell by typing

**\=IMAGE(“https://support.content.office.net/en-us/media/2d9e717a-0077-438f-8e5e-f85a1305d4ad.jpg”,  
“Sphere”)**

![](<Base64-Image-Removed>)

Alternatively, you may insert a cylinder into a cell as follows:

*   Copy and paste the following URL into cell **B1**:

[https://support.content.office.net/en-us/media/35aecc53-b3c1-4895-8a7d-554716941806.jpg](https://support.content.office.net/en-us/media/35aecc53-b3c1-4895-8a7d-554716941806.jpg)

*   Type “Cylinder” in cell **B2**
*   Enter the formula **\=IMAGE(B1,B2,0)** in cell **A3** and press the **ENTER** key.

![](<Base64-Image-Removed>)

**_Known issues_**

These include:

*   if the URL to the image file you are using is pointing to a site that requires authentication, the image will not render
*   zooming in and out with images in cells may distort the images
*   moving between platforms (for example, Windows and Mac) may result in irregular image rendering.

The **IMAGE** function is available to Insiders running the following Beta Channel builds:

*   **Windows:** Version 2209 (Build 15608.10000) or later
*   **Mac:** Version 16.65 (Build 22080701) or later
*   **iOS:** Version 2.65 (Build 22080701) or later
*   **Android:** 16.0.15608.10000 or later.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/new-image-function/#0)
    
*   [Register](https://sumproduct.com/news/new-image-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/new-image-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/new-image-function/#0)

[](https://sumproduct.com/news/new-image-function/#0 "close")

top