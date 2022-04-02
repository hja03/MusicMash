# Spotify Tinder

## Inspiration
In the past I have run into a conundrum where I get bored of my own playlists from listening to the songs too much. This has lead me to try the discover weekly playlist. However, this is a substandard fix as I only like a few of the songs which is not enough to build an entire playlist. Me and my friends have quite a similar music taste though and I often end up asking for their playlists so I can listen to them myself and try something different. Once I told my group mates this problem, we thought to ourselves "Surely we can combine both of our musics tastes and most listened to songs in order to build a playlist which we can both enjoy".

## What it does
It's a web application. When you first open the application you are greeted with a login page which lets you and your friends enter their spotify account details. This then gives us access to the data about their account. We then use spotify api to get data about their most listened to songs and artists. We use this data to calculate a compatibility score which we show on a panel in the centre of the screen. Their is also a button we use to create a fusion playlist which essentially makes use of you and your friends top 50 songs and music tastes to create a playlist for both of you. It then adds this playlist to your spotify account where you will be able to find it.

## How we built it
We built the back-end in python using and we built the front end in CSS, HTML and Java script. 

## How we did the data analysis

### The data
We get the most listened to songs from both of the users. Each of these songs has a multitude of attributes scored from 0-1 which we get from the spotify API. We deemed the following attributes most important: danceability, energy, acousticness, valence, tempo. We also store the genre of each of the songs.

### How we calculate the compatibility score
Explanation in graphical form. We plot all of the songs in a 5D graph with the axis being danceability, energy, acouticness, valence and tempo. We then go through all of the songs in one of the users top 50 and find the minimum distance on the 5D graph to one of the other users top 50 songs. We calculate this Euclidean distance using vectors and pythagoras theorem. This will give a number from 0-1. We then times this number by 100 and this is then displayed as the number as the compatibility number on the website.

I have drawn a 2D representation of the graph below
!(2d representation.PNG)

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for Untitled


## How we used to do the compatibility score