# Live Committee Signups
A live display of the number of new members for each committee.
The signup process is carried out using Google Forms.

[[Demo](https://raw.githack.com/StudieverenigingSTORM/live-committee-signups/main/index.html)]

## Components
* Google Apps Script (`api.gs`)
* Frontend Electron app 

## Local Testing  
Run a local static HTTP server using `python3 -m http.server 8080`.
The data is fetched from the file `mock-api.json`.

## Deployment
1. Create a signup form (Google Form and Google Sheet).
2. Make changes in `api.gs` according to comments and deploy API as Google Apps Script.
3. Set up the API url and color mapping in `index.html`.
4. Install Electron dependencies with `npm install`.
5. Run Electron app (run with `npm start` and toggle fullscreen with F11).

