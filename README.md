# Spotify Tinder

## Inspiration
In the past, I have run into a conundrum where I get bored with my playlists from listening to the songs too much. This has led me to try the "Discover Weekly" playlist. However, this is a substandard fix as I only like a few of the songs, which is not enough to build an entire playlist. My friends and I have quite a similar music taste though, and I often end up asking for their playlists so I can listen to them myself and try something different. Once I told my group mates this problem, we thought to ourselves: "Surely we can combine both of our musics tastes and most listened to songs in order to build a playlist which we can both enjoy".

## What it does
It's a revolutionary web application. When you first open the application, you are greeted with a login page which lets you and your friends enter their Spotify account details. This then gives us access to the data about their account. We then use Spotify API to get data about their most listened to songs and artists. We use this data to calculate a compatibility score, which we show on a panel in the centre of the screen. There is also a button which creates a fusion playlist, which essentially uses a combination of inputs including your friend's top 50 songs and music tastes to create a playlist for both of you. It then adds this playlist to your Spotify account, where you will be able to find it.

## How we built it
We built the back-end in Python using Flask, and we built the front end in HTML, CSS, and JavaScript. 

## How we did the data analysis
### The data
We get the most listened to songs from both of the users. Each of these songs has a multitude of attributes scored from 0-1 which we get from the Spotify API. We deemed the following attributes most important: danceability, energy, acousticness, valence, tempo. We also store the genre of each of the songs.

### How we calculate the compatibility score
Explanation in graphical form. We plot all the songs in 5D space with the axis being danceability, energy, acouticness, valence and tempo. We then go through all the songs in one of the user's top 50 and find the minimum distance on the 5D graph to one of the other user's top 50 songs. We also calculate this Euclidean distance using vectors and Pythagoras' theorem. This will give a number from 0-1. We then times this number by 100 and this is then displayed as the number as the compatibility number on the website.

I have drawn a 2D representation of what the euclidian distance is:
![](https://github.com/hja03/TopHackersAndShaggers/blob/main/2d%20representation.PNG)

## Challenges we ran into
Our app is currently in development so spotify makes us manually authorize users and we would need clearance from spotify to change this.
Coming up with a name.

## Accomplishments that we're proud of
It works!!!!!

## What we learned
We learnt how the spotify API worked, got used to how git hub works and using it within the IDE and How to effictevly work as a team (delegating tasks and creating a fun and productive work environment).

## What's next for Untitled


## How we used to do the compatibility score


