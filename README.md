# Vesta

![picture of a house](./images/building.jpeg)

**Welcome to Vesta : Léonie Willecomme and Tommaso Conti's final project for the MLOps class (DSBA M2).**

<p align="center">
  <img src="images/vesta.png" width="200" />
</p>

>[!IMPORTANT]
>**Executive Summary:** Vesta is built to assist people in purchasing a home or investing in real estate. Our platform uses the dataset "Demandes de Valeurs Foncières" of 2024 into an interface capable of analyzing price, location, and detecting fraudulent listings.
> Our mission at Vesta is providing users with a reliable foundation for their property acquisition.

>[!NOTE]
>**Our added value:** Going beyond traditional real estate platforms, Vesta analyzes every listing to assist decision-making : 
>* Fraud Detection : Detecting abnormally low prices or dataset errors (for example a studio listed as having 4 beds)
>* Price Analysis : Comparing every listing with the local market and classifying in three categories : Good Price, Fair Price, and High Price
>* Developer's Choice : Finding listings perfect for developers and investors, offering lots of ready-to-build land
>* Market Velocity : Measuring the speed of transactions in each location

>[!TIP]
>**How to run this code:**  
>* **Prerequesites :** Having Python installed, having a code editor (like VSCode)  
>* Make sure to download the dataset (in a .txt format) from https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres and add it IN A FOLDER "DATA" ON YOUR COMPUTER
>* On the top-right of this repo, click on the green button "<> Code" and copy the URL
>* Open VSCode and paste the URL
>* Open a terminal run this command : "pip install -r requirements.txt"
>* When it finished running, paste this into the terminal : "streamlit run app.py". 
>* Click on the link that appeared. It should be in this format : http://192.168.1.11:8501. 



## MLOps and Maintenance

We need to update the data every year. In order to do that we plan on using a script that will download the data from the official website, checking for differences in format (number of rows and names/number of columns) and re-process it. Once the new data is validated, we will update the app, keeping the old data for this intermediate stage.

>* **If I am the maintainer:** I run the update script every year (when a new dataset comes out). I also check that the format of the dataset is the same (no new column / variable). Then I update the app.
>* **If I am the user:** While the maintainer is validating the new data, I can continue using this website normally.

Errors will need to be monitored and fixed. We plan on using a dashboard to monitor the app and alert us if there are any errors. We aim at looking for logging errors and if fraud detection flags are showing any FP (a legitimate cheap listing flagged as fraud) or FN (a fraudulent listing not flagged as fraud). We also aim at looking for performance metrics like page load time, etc.

>* **If I am the maintainer:** I check the dashboard daily to see False Positive or False Negative alerts for listings, and I investigate them. On the dashboard, I can also see for every city the scores for every listing, so I can also monitor errors for other features.
>* **If I am the user:** Using a little button in the corner of each listing, I can report a listing if I think it was wrongly flagged as a scam, or if it was given a score that I think is wrong (ex: developer's choice for a house with a tiny garden).

We follow a canary deployment strategy. We will first deploy the new version of the app to a limited set of users, monitoring for issues before a wider rollout. If needed we can roll back to the previous stable releases marked with git tags.

>* **If I am the maintainer:** When I just built a new feature (ex: a new score for listings), i make it available to only 10% of users. If I see that the logs show some crashes or some slow performance, I roll back to the previous stable version.
>* **If I am the user:** If I am in the selected 10%, I get to try out new features early. If the performance is not good (slow, lots of bugs), the maintainer will be notified and it will be resolved quickly (the system will go back to the previous version that didn't have bugs).

We aim at updating the requirements.txt file with the new dependencies for every new version of the app. Having pinned versions of dependencies matters for reproducibility of the repo. A potential next step would be to use Docker to containerize the app and make it easier to deploy and manage.

>* **If I am the maintainer (short-term):** Every time I use a new library I update requirements.txt (so that everyone in the team can understand the project more easily).
>* **If I am the maintainer (medium-term):** I start using Docker.

Lastly, it is important to note that using the DVF dataset here (and the scenario we explained about updating the data every year) wouldn't work for a true real-estate startup. We would need the updated data every time a listing is posted (using web scrapers or real-time APIs).

## Limitations

The main limitation of this project is that the data is updated only once a year, so prices could be outdated. The dataset also doesn't include latitude/longitude, which would be useful for more precise analysis or to show listings on a map. The dataset is also quite sparse, with many null values.

Other limitations of our own features include the thresholds of the fraud detection (since they might not be optimal for rural areas) and that the market velocity treats all zip codes equally, even though some are very small.



## Future of this project

We want to collect user data to improve the app and gauge user satisfaction. We could collect data such as clicks on listings, time spent on page, etc. 
New features will need to be implemented to expand our current offering. Users might want to be able to save their favourite listings, filter by price or surface, and be notified when a good deal appears. 

We can also improve our current features by tuning the thresholds, by using more advanced ML models, and by giving a score instead of a label. 

We would use A/B testing to compare the new version of the features with the old version and analyze user behavior and satisfaction with statistical tests. The same concept can be applied to compare a new version of the app with the old version.

Finally, a geocoder (a service that converts addresses into coordinates) could be used to show listings on a map.


## More information

For more information about how this project was built, please click [here](./MOREINFO.md). 








