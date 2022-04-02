# Spotify Tinder

## Inspiration
In the past I have run into a conundrum where I get bored of my own playlists from listening to the songs too much. This has lead me to try the discover weekly playlist. However, this is a substandard fix as I only like a few of the songs which is not enough to build an entire playlist. Me and my friends have quite a similar music taste though and I often end up asking for their playlists so I can listen to them myself and try something different. Once I told my group mates this problem, we thought to ourselves "Surely we can combine both of our musics tastes and most listened to songs in order to build a playlist which we can both enjoy".

## What it does
It's a web application. When you first open the application you are greeted with a login page which lets you and your friends enter their spotify account details. This then gives us access to the data about their account. We then use spotify api to get data about their most listened to songs and artists. We use this data to calculate a compatibility score which we show on a panel in the centre of the screen. Their is also a button we use to create a fusion playlist which essentially makes use of you and your friends top 50 songs and music tastes to create a playlist for both of you. It then adds this playlist to your spotify account where you will be able to find it.

## How we built it
We built the back-end in python using and we built the front end in CSS, HTML and Java script. 

## How we did the data analysis

### The data
We get the most listened to songs from both of the users. Each of these songs has a multitude of attributes scored from 0-1 which we get from the spotify API. We deemed the following attributes most important: danceability, energy, acousticness, valence, tempo. We also store the attributes of each of the songs. We then go through all of the songs in the top 50 and compare each of the songs in the top 50 in order to get a score from 0-1 which states how similar the songs are (compatibility). We then store the maximum compatibility score. 

### How we calculate the compatibility score

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for Untitled
