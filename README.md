# MLOps-project-real-estate

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
>* Price Analysis : Comparing every listing with the local market and classifying in three categories : Good Deal, Fair Price, and Premium
>* Developer's Choice : Finding listings perfect for developers and investors, offering lots of ready-to-build land
>* Market Velocity : Measuring the speed of transactions in each location

>[!TIP]
>**How to run this code: **  
>* **Prerequesites :** Having Python installed, having a code editor (like VSCode)  
>* Make sure to download the dataset (in a .txt format) from https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres and add it IN A FOLDER "DATA" ON YOUR COMPUTER
>* On the top-right of this repo, click on the green button "<> Code" and copy the URL
>* Open VSCode and paste the URL
>* Run app.py.
>* When it finished running, paste this into the terminal : "streamlit run app.py". 
>* Click on the link that appeared. It should be in this format : http://192.168.1.11:8501. 



## MLOps and Maintenance

We need to update the data every year. In order to do that we plan on using a script that will download the data from the official website, checking for differences in format (number of rows and names/number of columns) and re-process it. Once the new data is validated, we will update the app, keeping the old data for this intermediate stage.

Errors will need to be monitored and fixed. We plan on using a dashboard to monitor the app and alert us if there are any errors. We aim at looking for logging errors and if fraud detection flags are showing any FP (a legitimate cheap listing flagged as fraud) or FN (a fraudulent listing not flagged as fraud). We also aim at looking for performance metrics like page load time, etc.

We follow a canary deployment strategy. We will first deploy the new version of the app to a limited set of users, monitoring for issues before a wider rollout. If needed we can roll back to the previous stable releases marked with git tags.

We aim at updating the requirements.txt file with the new dependencies for every new version of the app. Having pinned versions of dependencies matters for reproducibility of the repo. A potential next step would be to use Docker to containerize the app and make it easier to deploy and manage.



## Future of this project
Do users like this app? 

Potential other features : here we'll write about the maintenance if hypothetically this project was published online and used by other people. 
ex: anticipate what these users would need, statistics, latency, etc

also hypothetically if we update this website, how would current version compare with old version. 

>[!NOTE]
>**Limitations:** here we write about the limitations of this project, mainly : data is not updated often, data sparsity (many null values), no latitude / longitude 

## More information

For more information about how this project was built, please click [here](./MOREINFO.md). 








