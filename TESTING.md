# Testing


## PEP8 Standard Linters
### Expected
The code is expected to pass without any major issues highlighted.
### Test
flake8 & pylint was used throughout the development to check compliance.
### Result
There were a number of issues that cropped up throughout development, but there were able to be corrected easily going along. The vast majority of these were warnings about "lines too long".
![IDE Problems Section](assets/readme-images/pep8.png)
At the end of the project the only errors showing were those related to the `env.py` file that cound't be helped due to the nature of it.


## WC3 Markup Validation 
### Expected
The site is expected to pass validation with no errors.
### Test
I supplied the Live Heroku address of the site to [The WC3 Markup Validation Service](https://validator.w3.org/) and ran the test.
### Result
![HTML Validation Errors](assets/readme-images/html-validation-errors.png)
There were numerous errors, all relating the the use of paragraph elements *within* span elements.
### Fix
I added in the missing spaces where they were needed, I also deleted one of the sections that was producing the warning as it was not needed. After re-running the test with the updated markup, only one warning remained, I opted not to add a heading to this section because of how it would have affected the design.


## Jigsaw CSS Validation
### Expected
The site is expected to pass validation with no errors.
### Test
I supplied the GitHub Pages address of the site to [The WC3 CSS Validation Service](https://jigsaw.w3.org/css-validator/) and ran the test.
### Result
The CSS passed with no errors.


## Responsiveness
### Expected
Throughout the different sections the design should remain well laid out regardless of the device size
### Test
Using Google Developer Tools I changed to each device available to see how the lawy out looked, as well as using the "responsive" layout and changing the shape and size of the viewport with the drag handles. I did this repeatedly during the development process and again at the end.
### Result
Throughout development, on occasion I discovered elements that were not displaying how I thought they ought to be, for example appearing off the screen or out of alignment with other elements. However, by the end I was satisfied that the elements were all appearing in a satisfactory position / proportion.
### Fix
As and when issues were spotted I amended styles for the elements to ensure that everything fit and flowed. Where necessary I added media queries for different device sizes or orientation.


## Functionality
### Expected
Interactive elements should result in the expected or at least not an undesirable way when interacted with.
### Test
Through testing of interactive elements was conducted throughout the development process with many repeaded "playthroughs" of the game to check the the outcomes were consistently as expected throughout and at the end. I moved from screen to screen in each and every conbination an order that I could think of. I played the game, chosing every option and every conbination to get each of the 6 outcomes. Likewise with the options controls for sound and localStorage deletion.
### Result
Not always did things respond in the way they should be, at those times I returned to the code and would problem solve whatever issue had been recently introduced. However, but the end all issues were resolved and everythng functioned as indended.
### Fix
Frequent reajustments to code througout development.

## Peformance
### Expected
The site should load quickly.
### Test
Using Lighthouse from Chrome Developer tools, I ran a report.
### Result
The report flagged up 4 main issues impacting loading speed.
1. The linked Google Fonts needing to load before being abel to render the rest of the document.
2. Image file sizes.
3. Code that has not been minified.
4. Code that was not used (primarily from jQuery)
### Fix
I updated the images used from JPEGs to WebP files,reducing their filezise in half form ~200KB to ~100KB thereby increading the load speed.
I replaced the jQuery that I was using with the minimised verison of it, also speeding up the load time.
### Unresolved
Unfortunatley I do want to use the fonts that I am getting from Google Fonts, so it is still there slowing things up slightly.
I only used a small amount of jQuery when compared to the entire library, it miht be possible to strip out the parts of the library that I am not using, but that is not something I'm currently confident to carry out without causing issue at the moment.## Functionality
### Expected
Interactive elements should result in the expected or at least not an undesirable way when interacted with.
### Test
Thorough testing of interactive elements was conducted throughout the development process with many repeated "playthroughs" of the game to check the outcomes were consistently as expected throughout and at the end. I moved from screen to screen in each and every combination in and order that I could think of. I played the game, choosing every option and every combination to get each of the 6 outcomes. Likewise with the options controls for sound and localStorage deletion.
### Result
Not always did things respond in the way they should be, at those times I returned to the code and would problem solve whatever issue had been recently introduced. However, in the end all issues were resolved and everything functioned as intended.
### Fix
Frequent adjustments to code throughout development.
 
## Performance
### Expected
The site should load quickly.
### Test
Using Lighthouse from Chrome Developer tools, I ran a report.
### Result
The report flagged up 4 main issues impacting loading speed.
1. The linked Google Fonts needing to load before being able to render the rest of the document.
2. Image file sizes.
3. Code that has not been minified.
4. Code that was not used (primarily from jQuery)
### Fix
I updated the images used from JPEGs to WebP files,reducing their filezise in half from ~200KB to ~100KB thereby increasing the load speed.
I replaced the jQuery that I was using with the minimised version of it, also speeding up the load time.
### Unresolved
Unfortunately I do want to use the fonts that I am getting from Google Fonts, so it is still there slowing things up slightly.
I only used a small amount of jQuery when compared to the entire library, it might be possible to strip out the parts of the library that I am not using, but that is not something I'm currently confident to carry out without causing issues at the moment.
 
 
## Accessibility
### Expected
The site should not have any major accessibility issues as shown by accessibility tests.
### Test
Using Lighthouse from Chrome Developer tools, I ran a report.
### Result
There was an issue raised that heading tags were being skipped, as I had an `<h1>` followed by an `<h4>` 
### Fix
I initially tried to fix this by changing the `<h4>` to an `<h3>` thinking this would resolve the problem as I had `<h2>` elements elsewhere on the page, however it did not, so I changed the `<h4>` into a `<p>` instead and adjusted it's styles to match what I had previously.
 
 
## SEO
### Expected
No major issues to show from SEO report.
### Test
Using Lighthouse from Chrome Developer tools, I ran a report.
### Result
It showed that the SEO could be impacted by a lack of a description meta tag.
### Fix
I added in a description meta tag and re-ran the report and the issue no longer showed.
 
## Useability
### Expected
That users should be able to use the site and play the game as intended.
### Test
Throughout development, I had my partner attempt to play the game while I watched and listened to their feedback.
### Result
Throughout development they explained to me the parts that they would like to be different in some way that they felt would improve the experience for them.
### Fix
I implemented changes and added functionality and features along the development path based on the feedback I received.