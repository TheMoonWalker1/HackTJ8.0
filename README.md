# I'm ~~cravin'~~ carvin' tech 😉

## Inspiration
**For both safety and convenience**, it is _crucial_ to know important details about your car. Sometimes, however, it is easy to misplace or forget this information, or even get misinformed by online sources. For this reason, we created a website that conveniently retrieves data from your car's `VIN`, which is analogous to a fingerprint. 

## What it does
Our web-application retrieves information about your car through the `VIN` number, located on the passenger side door of your car. With this, you can quickly browse through specifications, that might take you a while to find otherwise.

![Building a Wall](https://media4.giphy.com/media/pO6VirqF04cgEUVbzS/giphy.gif)

## How we built it
The front-end and the backend of the website are heavily reliant on the framework Django provides. The information displayed on the front-end was made to be dynamic depending on the `VIN` inputted using the Jinja and Django template engines, while the styling and animations were made using `CSS` and `JS`. We created `models` and `forms` in the backend, which were used to conveniently cache information, as well as save/transmit data to wherever it is needed. We used the [NHTSA API](https://vpic.nhtsa.dot.gov/api/), [Edmund's API](https://developer.edmunds.com/api-documentation/vehicle/), and [VIN Decoder](https://vindecoder.eu/api?gclid=Cj0KCQjwmcWDBhCOARIsALgJ2QdHXtF4PEFn6gHuZuJ-0xraisUM-IijuOEx2lzNT0q6dblKIUBJJUgaAqlLEALw_wcB) in the backend to retrieve information about the car based on the `VIN` provided. 

## Challenges we ran into
*The main challenges we ran into* were finding a _reliable_ and _up-to-date_ API, and being able to correctly set up our site on Praneeth's _personal hosting server_. During our hunt for an API, we had trouble finding one that was free, provided the necessary information, and didn't restrict the rate limit of our post requests. We initially didn't think that this part would take a good portion of the time during the hackathon, so we didn't allocate much time to it. Looking back, we should have split up the jobs to make them more productive and efficient. Our next challenge was setting up the site on Praneeth's server: which included using an Alpine Docker image, running the server with `gunicorn`, creating workers to handle the workload, creating a valid SSL certificate in order for the website to have `https://`, and setting up the DNS connections. This was an extreme time struggle for us, especially because Praneeth has never deployed a dynamic website on his server.

![Arrow Thingy](https://miro.medium.com/max/2880/1*MNYR2dHTNxRt91EVH_bf0Q.gif)

## Accomplishments that we're proud of
The entire experience that we had while coding, debugging, and learning during this hackathon was something that we don't experience every day. We all learned important information about web design and automotive vehicles, from implementing `django-rest-framework` to what a `VIN` number is used and stands for. With the information we learned, we were able to build a simple-looking yet complex website that is optimized for time and information.

## What we learned
As would anybody learning something new, we naturally ran into problems. From simple font changes to program-breaking bugs, we experienced it all and learned valuable lessons from it. With perseverance and patience, we were able to successfully complete this project on time.  During this adventure, we learned how to make a simple and clean web design using `JS` and `CSS`, and also learned how websites communicate with `APIs`, Backends, and other websites in order to show our users the most up-to-date information. Most importantly, we learned how a website works and is deployed by implementing a series of pipelines using Jenkins, configuring docker images, and using `celery` workers. 

## What's next for VIN-tech
Continuing on our idea of providing the most important information about your car at the instant you want it, we would like to create a neural network that analyzes the correspondence between the number of years the car has been in use, the number of miles driven, and the market value of that car. We would also like to gain information about the likely hood of a car breaking down, as well as retrieving information (such as news) about the specific car model. With this, we can truly achieve our goal of being the one-stop-shop for any type of car information. 

![Party Blob](https://media.tenor.com/images/2327dde5f42ddd867d2db0aad09ae2dc/tenor.gif)
