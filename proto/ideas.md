

### Some ideas

We are working out the best song in a playlist via pairwise comparisons
 
* If the playlist has a number of songs $n$ that is not $2^k$ then the draw will be unbalanced.
    * We find the correct draw for the first round by doing:
        *  $b = \lceil\log_2{n}\rceil$
        * output size $o=2^{b-1}$
        * number of comparisons is $c=n-o$
        * number of byes is $s=n-2c$
    * This will guaruntee that the following rounds will always have a $n=2^k$ number of songs
* Maybe we should employ a metric to choose wisely which songs get byes - they should be strong candidates
    * Heuristic like the top $s$ most listened to songs in the playlist. By user if possible, else maybe in total on spotify.
* We should remember somewhere what comparisons have been made.
    * There are systems like Elo that could be used to rank over multiple playlists without needing so many comparisons by performing just pairwise comparisions within playlists
        * Might need some extra comparisons if not many songs shared between playlists