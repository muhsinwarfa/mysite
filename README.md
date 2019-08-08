#Simpletwitter

Link: https://meawesometwitterapp.herokuapp.com/

This project's aim is to create twitter from scratch using django 

There are only three tables that the database will have User,tweet,follower.

Whenever a user A tweets, it gets inserted into the "Tweet" table and is_tweet field is set to 1. Now when user B opens the app
, the system fetches all users who B follows from the "Follower" table. For all those user_ids who B follows, fetch all their tweets
from the "Tweet" table and then join and sort them based on the "time_posted" field.

Whenever user B, retweets a tweet the retweet_count field in the "Tweet" table for the corresponding tweet gets incremented by 1.
Similarly for "Reply". 

Both Reply and Retweet we need to set is_reply and is_retweet flag in "Tweet" table respectively.

In the tweet details page, all replies and retweets are fetched from the "Tweet" table, for the corresponding tweet id.
The field 'original_tweet_id' is the field which is used to search for the replies and retweets.

Since each reply and a retweet is a row in itself in the table, fetch all rows corresponding to original_tweet_id = <current tweet id>.

Replies to replies can similarly be found out based on 'original_tweet_id' field.
