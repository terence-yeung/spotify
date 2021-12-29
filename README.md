<h1 align="center">Automated Custom Playlists with Spotify Web API</h1>

<p>
The motivation behind this project was to be able to quickly make a playlist for a certain mood or occasion without having to manually find suitable songs and add them one by one which can be very time-consuming. I have also found Spotify's default recommendations (at the bottom of the playlist) to be quite hit-and-miss and not always aligned with what I was looking for. This was a good opportunity to take advantage of the Spotify Web API to automatically create a playlist based on custom defined parameters.
  
The program first creates an empty playlist with a name and description of my choice. Then, songs are recommended based on 'seed tracks' that I specify so Spotify can find songs similar to those. Furthermore, the API allows you to specify song attributes that the recommendations will have which is extremely helpful. In this example, I was building a playlist for a New Year's Eve gathering, so I was able to set attributes such as the minimum 'danceability', energy and valence (happiness) to ensure that only lively songs are included.
  
The playlist also updates to contain different songs each time the program is executed (since recommendations are made at random). Alternatively, the code can easily be changed with small adjustments to create an entirely new playlist with a different name, with different song attributes for a different occasion, if desired.
  
I have found this to be an effective way to put together a custom playlist containing great recommendations in a very short amount of time! Please feel free to check out the full code and generated playlist below.
</p>

## Links

- [Full Code](https://github.com/terence-yeung/spotify/blob/main/spotify.py)
- [Spotify Playlist](https://open.spotify.com/playlist/4XTaR3MbyKvr6FwJgtv3kS?si=0f39e2b14fb340d5)


## Future Updates

- [ ] Allow more than 100 songs to be added to the playlist at one time

## Author

**Terence Yeung**

- [GitHub Profile](https://github.com/terence-yeung "Terence Yeung")
- [Email](mailto:terenceyeung0@gmail.com?subject=Hi "Hi!")
- [LinkedIn](https://www.linkedin.com/in/terence-yeung/)

## Support

Contributions, issues, and feature requests are welcome!
