Spec
======

We would like to make a social network that displays media usage of a user.

This social network shall include the following details in V1:

- Only login through Facebook. This will simplify the process of obtaining a profile picture,
    and may be a good step towards identifying potential first things to list within the app.
    - login permissions to look for:
        - profile picture
        - friends
        - interests
- There shall be several categories, including tv shows, movies, books, and video games.
    - should only start with two
        - tv shows/movies are most simple
    - need to look up different available apis for typeaheads of each media
        - equivalent of spotify for music
        - could use wikipedia
        - imdb
        - rotten tomatoes
        - metacritic
    - could make rating system mandatory or optional
        - mandatory or nonexistant seems preferrable for design sake
        - maybe use emoji scale or some alternative to 1-10 or 1-5 stars?

- layout
    - items to focus on
        - user
            - name
            - profile picture
            - profile pic click shows stats
        - list of things to follow
        - some carousel/tab style system for different media
        - some carousel/tab style system for watched/to watch
            - could just be two columns for desktop
            - should prev column include time checked off?
                - would be different for prev/upcoming
            - should prev column be faded/gray?
        - queue style system
        - other user connections
        - other similar users
        - ads (not initially, maybe bottom of screen)
    - font, style
        - entertainment, but clean and modern
        - still social network
    - colors
        - three color maximum, two colors preferred
        - should be something entertainment-y
        - would like to incorporate purple
- interactions
    - user profile pic click flip
        - show stats/time last visit/number of items/connections
    - click on an item flip (tv show/movie)
        - see other friends who have also picked it
        - see other people who have also picked it and rated it highly
        - have a page for each item?
        - show wikipedia information
        - be able to add to your own lists (especially upcoming!)
    - tab system for different media
        - fade to left/right
            - needs to be smooth!
        - maybe use material style tabs?
    - editing list
        - edit button or hold to toggle?
        - should probably do hold to rearrange
            - could also make a part of the cell holdable
        - delete should probably be a little x somewhere
    - need some other "cool" animations using jquery
- 
