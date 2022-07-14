# Live Committee Signups
A live display of the number of new members for each committee.
The signup process is carried out using Google Forms.

[Demo](https://rawcdn.githack.com/StudieverenigingSTORM/live-committee-signups/585b88ade035cce42c0741eb86028c67ebad214c/index.html)

# Components
* Google Apps Script (`api.gs`)
* Static web frontend (`index.html`, `style.css`)

# Local Testing  
Run a local static HTTP server using `python3 -m http.server 8080`.
The data is fetched from the file `mock-api.json`.
