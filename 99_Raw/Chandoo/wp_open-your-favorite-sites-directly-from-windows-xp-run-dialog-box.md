# Open your favorite sites directly from Windows XP run dialog box » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box

---

Open your favorite sites directly from Windows XP run dialog box
================================================================

[hacks](https://chandoo.org/wp/category/hacks/)
 , [ideas](https://chandoo.org/wp/category/ideas/)
 , [technology](https://chandoo.org/wp/category/computer/)
 - 7 comments

  

![how to use windows xp run dialog as search box](https://chandoo.org/wp/wp-content/uploads/2008/05/use_run_as_search_box.png "use_run_as_search_box")

After seeing DI’s [Open Your Favorite Websites Directly from Windows Vista Start](menuhttp://www.labnol.org/software/tutorials/search-open-websites-from-windows-vista-start-menu/3110/)
 post, I thought why not use Windows XP Run dialog box as a search box. So here is a simple trick that can enable you to open your favorite sites directly from XP’s run dialog box.

Using this trick **you can type _“g bbc”_ to directly open BBC website** in firefox / IE.

First step is to **create a batch file** with the following text:

_**For Firefox users:**_  
`"C:\Program Files\Mozilla Firefox\firefox.exe" "http://www.google.com/search?btnI=I'm+Feeling+Lucky&q=%1"`

_**For IE users:**_  
`"C:\Program Files\Internet Explorer\IEXPLORE.EXE" "http://www.google.com/search?btnI=I'm+Feeling+Lucky&q=%1"`

Save the file anywhere (preferably in _C:\\Program Files_) with a name “g.bat”. The above one line of code essentially starts Firefox or IE and requests Google to fetch your favorite site using “I am feeling lucky” feature. The “%1” towards end tells windows to get the first parameter followed by “g” and passes it to Google.

Before you can use this you just need to modify your environment variables. For this:

1\. Right click on “my computer” and select properties  
2\. In the dialog box go to “advanced” tab and click on “environment variables” button  
[![using_xp_run_as_search2](https://chandoo.org/wp/wp-content/uploads/2008/05/using_xp_run_as_search2.png "using_xp_run_as_search2")](https://chandoo.org/wp/wp-content/uploads/2008/05/using_xp_run_as_search2.png)
  
3\. Select “path” from system variables and click “edit” button  
![using_xp_run_as_search3](https://chandoo.org/wp/wp-content/uploads/2008/05/using_xp_run_as_search3.png "using_xp_run_as_search3")  
4\. Append “;C:\\Program files” (if you have saved the batch file in some other directory mention that path here) to the path in the end (dont forget the ; before C: )  
![using_xp_run_as_search1](https://chandoo.org/wp/wp-content/uploads/2008/05/using_xp_run_as_search1.gif "using_xp_run_as_search1")  
5\. Click OK all the way back.

Now you can use run dialog box as Google search bar with “I am feeling lucky”, You can use the same trick to do searches on ebay, amazon, imdb, yahoo or wikipedia or anything else.

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [batch files](https://chandoo.org/wp/tag/batch-files/)<br>, [hacks](https://chandoo.org/wp/tag/hacks/)<br>, [howto](https://chandoo.org/wp/tag/howto/)<br>, [ideas](https://chandoo.org/wp/tag/ideas/)<br>, [productivity](https://chandoo.org/wp/tag/productivity/)<br>, [technology](https://chandoo.org/wp/tag/technology/)<br>, [tips](https://chandoo.org/wp/tag/tips/)<br>, [tricks](https://chandoo.org/wp/tag/tricks/)<br>, [windows](https://chandoo.org/wp/tag/windows/)<br>, [xp](https://chandoo.org/wp/tag/xp/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 7 Responses to “Open your favorite sites directly from Windows XP run dialog box”

1.  ![](https://secure.gravatar.com/avatar/4222b715898cbf103bf4ee79c153e658c970cf6d4b302ee88c17ca0d869413cb?s=64&d=mm&r=g) [Hypnos\`](http://blog.dsignbeyond.com/)
     says:
    
    [May 4, 2008 at 7:25 pm](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7398)
    
    Thanks. I think I'd prefer to fire up a firefox/safari and just search using the in-built google bar.
    
    Aren't you using the macbook?
    
    [Reply](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7398)
    
2.  ![](https://secure.gravatar.com/avatar/1afbe640e3b0b597c8e602dd9629b6858a8cb5dc0dd33356ff3532acf2b931d1?s=64&d=mm&r=g) [Sukhbinder Singh](http://my-aesi.blogspot.com/)
     says:
    
    [May 5, 2008 at 9:51 am](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7465)
    
    Great tip? But instead of doing the environment variable thing. Just copy the g.bat that is the batch file in windows folder and you can run is without any other issue.
    
    Thanks by the way. keep up the good work
    
    [Reply](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7465)
    
3.  ![](https://secure.gravatar.com/avatar/73bba53c4bf59e0a3ef8a894209b28ac19a8850424f15a0747cc4ba20e498cd3?s=64&d=mm&r=g) [Nikhil Narayanan](http://blog.nikhil.co.in/)
     says:
    
    [May 5, 2008 at 10:10 am](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7468)
    
    Hi Chandoo  
    Cool tip man!  
    Thanks..  
    What abt a batch file for opening 10 of my fav sites in one go on Mozilla..?
    
    \-Nikhil
    
    [Reply](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7468)
    
4.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/)
     says:
    
    [May 5, 2008 at 3:31 pm](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7505)
    
    @Hypnos - oh yeah, you always have that option, btw, I use PC @ office, so ended up experimenting this...
    
    @Sukhbinder Singh - welcome to PHD 🙂 We can always copy the batch file to system folders, often access to the folder may be limited based on user levels, thats why I mentioned program files or something like that. But good idea there 🙂
    
    @Nikhil ... oh sure, it would be the same way, just write 10 lines in the batch file instead of one and it works, alternatively if you are using firefox, you can change your options to load a bunch of bookmarks on start up.
    
    [Reply](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-7505)
    
5.  ![](https://secure.gravatar.com/avatar/83705007f372b89edfafa1724dccf049539050aed33826ebac6d00888e8f0f72?s=64&d=mm&r=g) [Club ReM](http://www.clubrem.es/)
     says:
    
    [May 14, 2008 at 9:37 am](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-8587)
    
    Hola
    
    Mi nombre es Javier Polo Pérez y soy Ingeniero, y desde hace varios años me dedico a la Informática de Gestión. He desarrollado varias soluciones informáticas que en el Mundo Hispano han obtenido una buena acogida debido a sus prestaciones y fácil manejo, muchos ya las conocerán sus nombres son: Clinicas @Clinic @OdontoClinic @PsicoClinic @PodoClinic @FisioClinic Inmobiliarias InmoServer Facturacion ProServer @GesPYME Comunidades AdmiCom Veterinarias @VetGes Promocion GesProm Prevencion PrevGes Almacen @GeSTOCK Personal @GesRRHH Turismo @GesTUR
    
    Me gustaría comentar que tras un año de pelea con Windows Vista intentando adaptar mis programas a dicho sistema operativo, lo cual he conseguido con mucho esfuerzo, finalmente he vuelto con mi Windosw XP, por tanto si lo que desean es un sistema operativo estable que no de ni un solo problema lo recomiendo.
    
    Si desean ver mi trabajo y descargarse mis programas en forma gratuita pueden acceder a la web del Club ReM su dirección es [http://www.clubrem.es](http://www.clubrem.es/)
     o en [http://www.e-rem.net](http://www.e-rem.net/)
    
    Un Saludo
    
    Javier Polo
    
    [Reply](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-8587)
    
6.  ![](https://secure.gravatar.com/avatar/939dddd2a9ccc48d27637c7bb060ee470f3d9399e614521394c5af3c47dcbe27?s=64&d=mm&r=g) Chris says:
    
    [May 20, 2008 at 6:09 pm](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-9221)
    
    Hi,  
    I love this idea, what I would really like is to add this to the right click of a folder, e.g. look up movie names in imdb. By making a shortcut of your batch file in the "send to" menu it will pass to %1 but it passes the complete path.  
    Do you know of any way to pass just the folder name?
    
    Cheers.  
    C.
    
    [Reply](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-9221)
    
7.  ![](https://secure.gravatar.com/avatar/5bd8d34a7ee04914e769003f03040ad03292827577ea8b4301974120ad2db5cf?s=64&d=mm&r=g) Pamela says:
    
    [July 25, 2011 at 9:08 pm](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-207568)
    
    This is great. I've used it to open the [https://www.epls.gov/epls/search.do](https://www.epls.gov/epls/search.do)
    . I have to do the same search on multiple occasions. How do I figure out what and how to pass the variables to the website then perform the search?
    
    [Reply](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#comment-207568)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/open-your-favorite-sites-directly-from-windows-xp-run-dialog-box/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [7 Most innovative software job titles](https://chandoo.org/wp/7-most-innovative-software-job-titles/) | [on vlookup()](https://chandoo.org/wp/on-vlookup/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)