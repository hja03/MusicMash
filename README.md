# MusicMash
Have you ever wanted to see how compatible you and your friends music tastes are?
Music Mash will tell you your compatibility score and even build a playlist combining both of your music tastes.

### Inspiration
In the past, I have run into a conundrum where I get bored with my playlists from listening to the songs too much. This has led me to try the "Discover Weekly" playlist. However, this is a substandard fix as I only like a few of the songs, which is not enough to build an entire playlist. My friends and I have quite a similar music taste though, and I often end up asking for their playlists so I can listen to them myself and try something different. Once I told my group mates this problem, we thought to ourselves: "Surely we can combine both of our music tastes and most listened to songs in order to build a playlist which we can both enjoy".

### What it does
It's a revolutionary web application. When you first open the application, you are greeted with a login page which lets you and your friends enter their Spotify account details. This then gives us access to the data about their account. We then use Spotify API to get data about their most listened to songs and artists. We use this data to calculate a compatibility score, which we show on a panel in the centre of the screen. There is also a button which creates a fusion playlist, which essentially uses a combination of inputs including your friend's top 50 songs and music tastes to create a playlist for both of you. It then adds this playlist to your Spotify account, where you will be able to find it.

### How we built it
We built the back-end in Python using Flask, and we built the front end in HTML, CSS, and JavaScript.

### How we did the data analysis
**The data**
We get the most listened to songs from both of the users. Each of these songs has a multitude of attributes scored from 0-1 which we get from the Spotify API. We deemed the following attributes most important: danceability, energy, acousticness, valence, tempo. We also store the genre of each of the songs. We also analysed the genres and joined them together using more general genres to increase the accuracy of our calculations.

**How we calculate the compatibility score**
Explanation in graphical form. We plot all the songs in 5D space with the axis being danceability, energy, acouticness, valence and tempo. We  then go through all the songs in one of the user's top 50 and find the minimum distance on the 5D graph to one of the other user's top 50 songs.

We find the average danceability, energy, acousticness, valence, tempo of all the top 50 songs for both of the users. Plot this on the 5D graph and find the Euclidean distance between the average points of the two users. We then work out which genres match for each of the songs. 
After this we we workout all the genres which both users listen to and then the number of songs in these genres. Then we use a weighted sum of the 5D Euclidean distance and the matching-genre songs proportion. This gives us a number between 0-1 which we times by 100 to get the percentage shown on the panel.

I have drawn a 2D representation of how we calculated the Euclidean distance:
![](https://github.com/hja03/TopHackersAndShaggers/blob/main/2d%20representation.PNG)

### Challenges we ran into
Our app is currently in development so Spotify makes us manually authorize users and we would need clearance from Spotify to change this.
We found it very difficult to agree on a catchy name to brand our project. Eventually we agreed on MusicMash but it was a long process

### Accomplishments that we're proud of
The main goal of this project was to help people connect though discovering shared interests and exploring new music together. We feel the fusion playlists combing 2 peoples tastes offer a unique opportunity to explore new sounds with another and the fascinating stats presented create great experience with friends.

### What we learned
We learnt how the Spotify API worked, got used to how git hub works and using it within the IDE and How to effectively work as a team (delegating tasks and creating a fun and productive work environment).