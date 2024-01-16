This is a small project I did while learning how to use APIs and data mining using BS4. 

The script creates a Spotify playlist containing the Billboard top 100 for a selected week for the date provided (Your birthday week for example).

**Note: I use dotenv for environment variables.**

# Tutorial:

First you need to get your Spotify API token:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and log in with your Spotify account credentials.

2. Click the "Create an App" button and follow the prompts to create a new app. Give your app a name and description, and choose a relevant category.

3. Once you've created your app, you'll be taken to the app dashboard. Click on the "Edit Settings" button and add a redirect URI under the "Redirect URIs" section. This can be any valid URL, such as `http://localhost:8888/callback`.

4. Save your changes and go back to the app dashboard. You should now see your app's client ID and client secret. These are the credentials you'll use to authenticate your app with the Spotify API.

5. Now run [token_gen.py](token_gen.py) it will generate a URL, paste it in a browser it will redirect you to a different URL, copy it and paste it into CLI and press enter, you should receive your token as an output. 

Now add the API token as an environment variable, or you can just add it directly to [main.py](main.py) and run it, input the date, it will collect the top hot 100 for that week and put it into a Spotify playlist after choosing a name for it. 

