# New Translation Functions in Excel

**Source:** https://sumproduct.com/news/new-translation-functions-in-excel/

---

[Home](https://sumproduct.com/)

\> New Translation Functions in Excel

*   July 1, 2024

New Translation Functions in Excel
==================================

New Translation Functions in Excel
==================================

1 July 2024

There are two new Preview functions coming to Excel. Be careful using these: their signature and results may change substantially before being broadly released, based upon feedback from those fortunate enough to be able to access them. Therefore, we strongly recommend you do not rely on these functions in important workbooks until they are Generally Available.

The two new translation functions out in Preview now are **TRANSLATE** and **DETECTLANGUAGE**.

Microsoft is introducing these two new functions to simplify and automate translations directly within your spreadsheet:

*   **TRANSLATE:** a function that translates a text from one language to another
*   **DETECTLANGUAGE:** a function that detects the language of the specified text.

**TRANSLATE**

**TRANSLATE** takes text you provide and translates it from one language to another using Microsoft Translation Services. Currently, there are 133 languages supported – including two variations of Klingon!!

At the time of writing, these are:

1.  Afrikaans
2.  Albanian
3.  Amharic
4.  Arabic
5.  Armenian
6.  Assamese
7.  Azerbaijani (Latin)
8.  Bangla
9.  Bashkir
10.  Basque
11.  Bhojpuri
12.  Bodo
13.  Bosnian (Latin)
14.  Bulgarian
15.  Cantonese (Traditional)
16.  Catalan
17.  Chinese (Literary)
18.  Chinese Simplified
19.  Chinese Traditional
20.  chiShona
21.  Croatian
22.  Czech
23.  Danish
24.  Dari
25.  Divehi
26.  Dogri
27.  Dutch
28.  English
29.  Estonian
30.  Faroese
31.  Fijian
32.  Filipino
33.  Finnish
34.  French
35.  French (Canada)
36.  Galician
37.  Georgian
38.  German
39.  Greek
40.  Gujarati
41.  Haitian Creole
42.  Hausa
43.  Hebrew
44.  Hindi
45.  Hmong Daw (Latin)
46.  Hungarian
47.  Icelandic
48.  Igbo
49.  Indonesian
50.  Inuinnaqtun
51.  Inuktitut
52.  Inuktitut (Latin)
53.  Irish
54.  Italian
55.  Japanese
56.  Kannada
57.  Kashmiri
58.  Kazakh
59.  Khmer
60.  Kinyarwanda
61.  Klingon
62.  Klingon (plqaD)
63.  Konkani
64.  Korean
65.  Kurdish (Central)
66.  Kurdish (Northern)
67.  Kyrgyz (Cyrillic)
68.  Lao
69.  Latvian
70.  Lithuanian
71.  Lingala
72.  Lower Sorbian
73.  Luganda
74.  Macedonian
75.  Maithili
76.  Malagasy
77.  Malay (Latin)
78.  Malayalam
79.  Maltese
80.  Maori
81.  Marathi
82.  Mongolian (Cyrillic)
83.  Mongolian (Traditional)
84.  Myanmar
85.  Nepali
86.  Norwegian
87.  Nyanja
88.  Odia
89.  Pashto
90.  Persian
91.  Polish
92.  Portuguese (Brazil)
93.  Portuguese (Portugal)
94.  Punjabi
95.  Queretaro Otomi
96.  Romanian
97.  Rundi
98.  Russian
99.  Samoan (Latin)
100.  Serbian (Cyrillic)
101.  Serbian (Latin)
102.  Sesotho
103.  Sesotho sa Leboa
104.  Setswana
105.  Sindhi
106.  Sinhala
107.  Slovak
108.  Slovenian
109.  Somali (Arabic)
110.  Spanish
111.  Swahili (Latin)
112.  Swedish
113.  Tahitian
114.  Tamil
115.  Tatar (Latin)
116.  Telugu
117.  Thai
118.  Tibetan
119.  Tigrinya
120.  Tongan
121.  Turkish
122.  Turkmen (Latin)
123.  Ukrainian
124.  Upper Sorbian
125.  Urdu
126.  Uyghur (Arabic)
127.  Uzbek (Latin)
128.  Vietnamese
129.  Welsh
130.  Xhosa
131.  Yoruba
132.  Yucatec Maya
133.  Zulu.

As mentioned above, the **TRANSLATE** function allows you to translate text from one language to another in Microsoft Excel by using Microsoft Translation Services. The full signature is:

**TRANSLATE(text,  
\[source\_language\], \[target\_language\])**

This function has the following arguments:

*   **text:** the **text** to translate. This value should either be enclosed in quotation marks or be a reference to a cell containing the appropriate **text**

*   **source\_language (optional):** the language code of the source language (_e.g_. “en” for English or “es” for Spanish). If not specified, the language will be automatically detected based upon the **text** provided. Auto-detection is supported for most languages. It is recommended to specify the language if known, especially for shorter texts

*   **target\_language (optional):** the language code of the target language (_e.g._ “en” for English or “es” for Spanish). If not specified, the system language will be used as the target language.

The supported languages and their respective language codes are as follows:

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

Suppose you have the following text in cell **A1**: “Hello, World!” and you want to translate it to Spanish. You can use the **TRANSLATE** function as follows:

**\=TRANSLATE(A1,  
“en”, “es”)**

In this example, the source language is English (en) and the target language is Spanish (es). The translated text, “Hola mundo!” will be displayed in the cell where you entered the formula.

Alternatively, you may just type the text in, _viz._

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

Common errors include the following:

*   **Text Too Long:** you have too many characters in a cell. Reduce your cell size and try again
*   **Error in Value:** you have a non-text value in your cell. The function only accepts a text argument
*   **Invalid Language:** you have entered an invalid language code or one not presently supported (see above)
*   **Request Throttled:** you have exceeded your daily quota of the translation function (now that is interesting, but we are not quite sure what that means at the time of writing).

**DETECTLANGUAGE**

**DETECTLANGAUGE** detects the language of text you provide using the Microsoft Translation Services and returns the language code. The full signature is:

**DETECTLANGUAGE(text)**

The function has the following arguments:

*   **text:** the **text** or reference to cells containing **text** to evaluate.

The supported languages and their respective language codes are as above.

Suppose you have the following text in cell **A1**: “Hola mundo!” and you want to find out what the language of the text is. You can use the **DETECTLANGUAGE** function as follows:

**\=DETECTLANGUAGE(A1)**

This will return the detected language for the text in cell **A1**. The language code “es” for Spanish will be displayed in the cell where you entered the formula.

Alternatively, you may just type the text in, _viz._

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

Common errors include the following:

*   **Text Too Long:** you have too many characters in a cell. Reduce your cell size and try again
*   **Error in Value:** you have a non-text value in your cell. The function only accepts a text argument
*   **Invalid Language:** you have entered an invalid language code or one not presently supported (see above)
*   **Request Throttled:** you have exceeded your daily quota of the translation function.

These functions are currently available to _some_ Beta Channel users running:

*   Windows: Version 2407 (Build 16.0.17808.20000) or later
*   Mac: 16.87 (Build 24062430) or later.

We say “some” as we haven’t access _yet_.

As always, we’ll be providing details in our August newsletter. Please remember we have virtual / online training in Excel which you can find out more about [here](https://www.sumproduct.com/courses/excel-tips-tricks)
. If you are not already a subscriber, why not sign up at the bottom of any [SumProduct](https://www.sumproduct.com/)
 web page?

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/new-translation-functions-in-excel/#0)
    
*   [Register](https://sumproduct.com/news/new-translation-functions-in-excel/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/new-translation-functions-in-excel/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/new-translation-functions-in-excel/#0)

[](https://sumproduct.com/news/new-translation-functions-in-excel/#0 "close")

top