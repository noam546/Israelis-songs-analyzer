# DH2022---Noam-and-Ofek

1. Our research question is -
How feminine adjectives changed in Israeli songs during the last 5 decades (1970 - 2020) with the change in women's state in society.

2. Background - Choosing the topic of our project was influenced by questions and wonders in our conversations about Israeli women state. We were intrested to figure out how the women's state in Israel is reflected in Israeli songs through the last few decades. We found ourselves wondering through the eyes of Israeli music, and lyrics, and then a question poped up in our minds - is the politicly correct era changed also the way women are described in Israeli music? And that was it. 
We think that former adjectives like "בחורה מבית טוב, אישה קטנה, ילדה רכה" and more would identify women in the past rather than in the current decade songs, also, the main adjectices in earlier decade would be related mostly to outside beauty rather than the actual character.
We believe that the "Me Too" movement influenced much on the women state in the world, and obviously in Israel too. 
The "me too" movement is a movement thay was established in 2006. As part of the world's women perception, the movement burst into our lives in October 2017, after the Harry Weinstein sexual harrasment case. 
Since the movement establishment, women's state in the world was much improved, and there is zero tolerence policy to objectifying statements and songs regarding women. 
The movement was established in an important decade where more voices against homophobia, recasim, antisemitisem were heard, and the expression "Politicly Correct" came to life. 
This expression is also used in spoken Hebrew, when it is no longer okay to use words, or statements that can hurt or discriminate some communities or parts of the society.
Since the awareness of such words and expressions was much improved, some songs that were written in the past are no longer legitimate, and some expressions, adjectices that are describing women are no longer in use.
For example, the Israeli song - "בחורה מבית טוב צריכה להיות יפה ולשתוק הרבה" is an expression that is hard to assume that can be in use of latest songs, since it's not politicly correct to identify the meaning of women in such way that makes her "smaller". 
On the other we know some songs today that can objectify women, so we assume that the politicly correct era has not caused to a complete vanish of such expressions from the Israeli songs lyrics.
We want to examine if this phenomenon was decreased in the last decades. 

3. Work Plan - 
As part of the project we want to use the next tools:

Spotipy – Spotify API for Python. 
Israeli songs lyrics DB - Lyrics.co.il
Dicta - a tool to identify the feminine adjectives in the lyrics. 
Some visualization tool to make our results clear to understand - word clouds, Voyant.

4. Our Goal - 
Creating a tool that analyzes the women's imagery in Israeli music through the years. 
We want to display our results in an informative, clear way through קריאה משולבת (רחוקה וקרובה). 
We would like to create a graph that shows the change in the use of an adjective through out the years. For example, "אישה טובה" may appear 10 times in the 70's songs in contrast to 5 times in the 2000's. 
Another way we would like to display our results would be a word cloud that shows the word that was in use the most in bigger font than the words that were less in use. 
In addition, another goal is to explain the results in our words, and to compare the result to our previous assumption, i.e, is the use in offensive, objectyfing expressions regarding women has decreased through out the years. 

5. Our conclusion - 
After trying to use the Lyrics.co.il local DB, we understood that the songs there are not enough, so we wrote an API to use the "shironet" website and scrape the lyrics of the songs from their website. 
There is a trade off between these two solutions, since using the API we wrote will decrease the run time since there are many requests to the "Shironet" server, and also, a network connection is needed. On the other hand, for our research we had to use a large DB to have accurate, reliable results, so we decided to go with the Shironet API we wrote. We decied to keep both solutions in our code, so that a user can decide which solition fits better to his/hers needs. 

To sum up - We learned a lot from our project. Not only technical skills which will be in use in the future, but also we experienced a real research from it's beginning until the end. We had an interseting topic that combined our love to music and also a personal connection to Hebrew language with our technical skills that we gained through our degree these last few years. 
We experienced with HTML, API's and libraries from Python, which were very new to us, we got to write an API (!), and also learned about the Hebrew language, Israeli music, and the changes that the last generation is bringing with it, through music. We used skills from the erliear lessons with Yael - used "חצי מובנה" data, and also "מובנה" data, also experienced "עיבוד שפה טבעית", which is literly the combination between the computers world, and human language thriugh the Dicta tool.
We are grateful for this project and the experience it brought to us, very interesing and teaching. 
Thank you Yael! 

7. Bibiliography - 
* https://spotipy.readthedocs.io/en/2.19.0/
* https://shironet.mako.co.il/
* Lyrics.co.il DB that Yael sent us
* Wix.com for the website - https://ofek031096.wixsite.com/website
* https://voyant-tools.org/
*canva graphs

*A link to our website - https://ofek031096.wixsite.com/website
