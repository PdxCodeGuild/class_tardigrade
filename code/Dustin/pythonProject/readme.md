# TARDIGRADE TRADER
> making small trades for big gains.

## Project Overview

Buying and selling Crypto currency app. I will be building the app using the Crypto Compare API [Crypto Compare](https://min-api.cryptocompare.com/). The idea is to have a user be able to log in to their account, choose what Crypto they are interested in and set both a "sell price" and a "but price." Then the app will track the crypto with the API and when it hits eith price it sends a text message, with  [Twilio](https://www.twilio.com/) to the users phone telling them it has hit the price of the specified Crypto. The user should also be able to text back to the program telling it a specific buy or sale amount, **in USD,** and the app will make the purchase or sell. 

## Features

Anyone interested in Crypto know that you must be able to keep track of buying and selling of your crypto. Because **small changes can lead to large gains.** Most crypto traders cannot afford to watch the market with a keen eye all day while living their life. **This APP will do it for you!**

# You Will be able to
- Pick the crypto youre interested in.
- Set a sell price.
- Set a buy price.
- Set up text notifications.
- Tell Tardigrade Trader how much to purchase or sell.
<!-- not considered part of my MVP, may not be able to purchase or sell -->
- The app will display the current price for the Crypto when you are setting prices.

# Other features include
- Set when you want to be notified. 
- Set how often you want to recieve a messege.
- Secure login.
- Link the app to your trader account to make purchases and sells.
<!-- not entirley sure how this would work, using other apps so may not be possible -->


## Data Model

Data we will need to capture.
- User login credentials.
- Phone number.
- User preferences.
- Banking details or Crypto trader account info.
- Crypto currenceys and prices.
<!-- must find a way to keep that information secure -->

##  Schedule
# Week 1:
- [ ] Set up Crypto Compare and Twilio with DJango. 
- [ ] Get and account that will just send a text when crypto hits prices
- [ ] User interface must display current prices of crypto when setting price ranges.
# Week 2:
- [ ] Build mutiple user functionality. 
- [ ] Secure user information <!-- Do not want anyone to be able to see confidential information-->
- [ ] Build user customization/setting profile. <!-- if some hits the sell price the likley dont want to see a text every minute until the price moves out of the sell price range. They also could want it to send only during certain time of the day. -->
# Week 3: 
- [ ] Styling! <!-- until this point its all going to look pretty ugly/basic-->
- [ ] Implement buying and selling options. <!-- not entirely sure how to do this yet, could use the program to navagae on their browser to use their own crypto acoount such as robin hood to make purchases and sells. not sure on legality and security on that though.-->
- [ ] **Secure banking and/crypto account information.** <!-- again just want to be extrea carefull when dealing with banking details, maybe it needs a higher lever of security when dealing with bank information-->
- [ ] Hosting and deployment.

## Setting up MVP
> What is the minimum to get the project running.

# Essential features
- User login.
- Picking specific Crypto and price ranges.
- Text messege when in price ranges.
- User infromation security.

# Really-great-to-haves
- Display prices when setting up preferences.
- Multiple user functionality.
- Deployment and hosting. <!-- I want this to be something that runs remotley and continuely not just until a text is sent.>

# Really-great-to-haves
- Ability to make sells and purchases.
- Text back functionality, something like ***"okay"*** to acknowlege the messege or ***"pause"*** get it to stop sending for 24 hours.
- link to Crypto accounts e.g. [Robin Hood] (https://robinhood.com/us/en/about/crypto/?utm_source=google&utm_campaign=13049048289&utm_content=crypto_119464199422&utm_term=520679377612__robinhood%20crypto&gclid=Cj0KCQiAxoiQBhCRARIsAPsvo-xb3T9Hx5Qqy0jLE1Jjt5lHQ9-4VBqb9ki5cl3U7sEQNb6rdOh_zcwaAiRzEALw_wcB)