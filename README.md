# Live Committee Signups
A live display of the number of new members for each committee.
The signup process is carried out using Google Forms.

[Demo](https://rawcdn.githack.com/StudieverenigingSTORM/live-committee-signups/585b88ade035cce42c0741eb86028c67ebad214c/index.html)

# Components
* Google Apps Script (`api.gs`)
* Static web frontend (`index.html`)

# Local Testing  
Run a local static HTTP server using `python3 -m http.server 8080`.
The data is fetched from the file `mock-api.json`.

# Deployment
1. Create a signup form (Google Form and Google Sheet)
2. Make changes in `api.gs` according to comments and deploy API as Google Apps Script
3. Set up the API url and color mapping in `index.html`
4. Deploy the file as a static site 
