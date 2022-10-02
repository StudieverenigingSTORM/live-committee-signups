# Live Committee Signups
A live display of the number of new members for each committee.
The signup process is carried out using Google Forms.

[Demo](https://rawcdn.githack.com/StudieverenigingSTORM/live-committee-signups/9e8381d759407487a50312a835a6bdb3f30b92b0/index.html)

## Components
* Google Apps Script (`api.gs`)
* Static web frontend (`index.html`)  
**Note!** Since CORS is annoying, you need to run first close chrome and run it with `chrome --disable-web-security --user-data-dir=<some temp dir>` to get this to work.
* **Alternative:** Python 3 app (`app.py`, dependencies are installed with `pip install -r requirements.txt`)

## Local Testing  
Run a local static HTTP server using `python3 -m http.server 8080`.
The data is fetched from the file `mock-api.json`.

## Deployment
1. Create a signup form (Google Form and Google Sheet)
2. Make changes in `api.gs` according to comments and deploy API as Google Apps Script
3. Set up the API url and color mapping in `index.html`
4. Deploy the file as a static site 
