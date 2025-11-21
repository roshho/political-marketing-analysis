# Prompt
## Prompt 1 (hussein)
```
Prompt:

You are going to see a list of Tweets from US politicians, and the politicians' political party. Your task is to figure out whether each tweet is consistent or goes against the party of the politician. For example, a Democrat who is calling for additional funding for border security would be an example of a Tweet going against the party. But, a Democrat calling for more immigration or a Republican calling for greater border security would be an example of a Tweet consistent with the party. 

For each Tweet, give a label. The label can take on the following values: 

    0: The Tweet aligns with the party's stance. 
    1: The Tweet goes against the party's stance. 

For each tweet, provide the classification label (0, 1, or 2) and a brief explanation for your choice.
Examples:

    Tweet: "We must ensure healthcare is affordable for every American. Access to healthcare is a right, not a privilege."
    Party: Democrat
    Classification: 0
    Explanation: The tweet aligns with the Democratic Party's focus on expanding healthcare access.

    Tweet: "Gun control laws are unconstitutional. We must uphold the Second Amendment."
    Party: Democrat
    Classification: 1
    Explanation: The sentiment does not align with the Democratic Party's typical stance on gun control.

    Tweet: "Wishing everyone a safe and happy Fourth of July!"
    Party: Republican
    Classification: 2
    Explanation: The tweet is neutral and not related to party values.

Now, analyze and classify the following tweet:

Tweet: [Insert tweet text here]
Party: [Insert party label here]
```

## Prompt 2
```
Prompt:

Analyze the sentiment and context of the following tweet. Based on the sentiment and its alignment with the associated political party's values, classify the tweet into one of the following categories:

    0: The sentiment aligns with the values and stance of the political party.
    1: The sentiment does not align with the values and stance of the political party.
    2: The sentiment is neutral or irrelevant to the party's values (e.g., holiday greetings, personal announcements).

For each tweet, provide the classification label (0, 1, or 2) and a brief explanation for your choice.
Examples:

    Tweet: "We must ensure healthcare is affordable for every American. Access to healthcare is a right, not a privilege."
    Party: Democrat
    Classification: 0
    Explanation: The tweet aligns with the Democratic Party's focus on expanding healthcare access.

    Tweet: "Gun control laws are unconstitutional. We must uphold the Second Amendment."
    Party: Democrat
    Classification: 1
    Explanation: The sentiment does not align with the Democratic Party's typical stance on gun control.

    Tweet: "Wishing everyone a safe and happy Fourth of July!"
    Party: Republican
    Classification: 2
    Explanation: The tweet is neutral and not related to party values.

Now, analyze and classify the following tweet:

Tweet: [Insert tweet text here]
Party: [Insert party label here]
```

## Prompt 3 (generated 1)
```
Analyze the sentiment and context of the following tweet. Based on the tweet's stance on specific policy areas or its alignment with key terms associated with the identified political party, classify the tweet into one of the following categories:

    0: The tweet aligns with the values and stance of the political party.
    1: The tweet does not align with the values and stance of the political party.
    2: The tweet is neutral or irrelevant to the party's values (e.g., holiday greetings, general statements, or unrelated topics).

Criteria for Party Alignment:

    Democratic Party (DEM):
        Policies: Support for affordable healthcare, climate action, reproductive rights, gun control, student loan forgiveness, renewable energy, and social equity.
        Keywords: "affordable care," "Medicare," "climate change," "gun safety," "choice," "women's rights," "renewable energy," "student loans," "equity," "progress."
        Contradictions: Advocacy against healthcare reform, pro-life stances, or strong support for Second Amendment rights.

    Republican Party (REP):
        Policies: Advocacy for tax cuts, pro-life policies, Second Amendment rights, border security, energy independence, and traditional family values.
        Keywords: "lower taxes," "pro-life," "Second Amendment," "border security," "energy independence," "religious freedom," "economic growth," "patriotism."
        Contradictions: Advocacy for gun control, strong support for renewable energy mandates, or pro-choice stances.

Considerations for Neutrality:

    Tweets about holidays, celebrations, personal achievements, or non-political topics are typically neutral unless tied explicitly to party values.

Objective:

Identify whether the sentiment aligns with the party’s general principles based on the identified key themes, policy areas, and contradictions.
```

## Prompt 4 (generated 2)
```
Analyze the sentiment and context of the following tweet. Based on the tweet's stance on specific policy areas or its alignment with key terms associated with the identified political party, classify the tweet into one of the following categories:

    0: The tweet aligns with the values and stance of the political party.
    1: The tweet does not align with the values and stance of the political party.
    2: The tweet is neutral or irrelevant to the party's values (e.g., holiday greetings, general statements, or unrelated topics).

Criteria for Party Alignment:

    Democratic Party (DEM):
        Policies: Support for affordable healthcare, climate action, reproductive rights, gun control, student loan forgiveness, renewable energy, and social equity.
        Keywords: "affordable care," "Medicare," "climate change," "gun safety," "choice," "women's rights," "renewable energy," "student loans," "equity," "progress."
        Contradictions: Advocacy against healthcare reform, pro-life stances, or strong support for Second Amendment rights.

    Republican Party (REP):
        Policies: Advocacy for tax cuts, pro-life policies, Second Amendment rights, border security, energy independence, and traditional family values.
        Keywords: "lower taxes," "pro-life," "Second Amendment," "border security," "energy independence," "religious freedom," "economic growth," "patriotism."
        Contradictions: Advocacy for gun control, strong support for renewable energy mandates, or pro-choice stances.

Considerations for Neutrality:

    Tweets about holidays, celebrations, personal achievements, or non-political topics are typically neutral unless tied explicitly to party values.

Objective:

Identify whether the sentiment aligns with the party’s general principles based on the identified key themes, policy areas, and contradictions.
```

## Prompt 5
```
The following set of tweets are from American politicians and I want to analyses the sentiment of the tweets their tweets align with the party (which will be labeled 0), if it doesn't align with the party (which will be labeled 1), and if it's irrelevant to party values (e.g. promotion to vote or celebration of holiday, to be labeled as 2). I will provide examples of each:
        
Example of not aligning with party values (1 index): republican politician: "victory     building workers  amp  the  have reached a tentative agreement that achieves historic wins for the union   s membership in what will be the first post pandemic contract between the two sides               nlive at        for more details"

This example is 1 because republicans tend to support free market, thus would be against unionization. This tweets indicates support for unionization, thus doesn't align with republican party values. 


Example of aligning with party values (0 index): republican politician: "in less than a month  joe biden and congressional democrats forced blue collar workers to give  17 500 to college graduates making  75 000 so they can buy a tesla and pay off their student loans "

This is an example of 0 because republicans support free market, against government intervention and want to prevent inflation. Biden's proposition to pay off student loans would be a big government intervention and cause large debt accumulation. 
```

## Prompt 6
```
I'm going to feed you a few tweets from American politicians with their party identity and tweet. I want you to assign 1 if the tweet doesn't align with the their party values 0 if the tweet aligns with their party ethos and 2 if its irrelevant to party values. 


Example of not aligning with party values (1 index): republican politician:     victory     building workers  amp  the  have reached a tentative agreement that achieves historic wins for the union   s membership in what will be the first post pandemic contract between the two sides               nlive at        for more details          


Example of aligning with party values (0 index): republican politician: in less than a month  joe biden and congressional democrats forced blue collar workers to give  17 500 to college graduates making  75 000 so they can buy a tesla and pay off their student loans 


Example of irrelevant (2 index): texas is a great state  but we have to fight for it  and to do that  we need every voice to be heard this november so our leadership in texas actually reflects who we really are   n nregister to vote today by visiting   texas is a great state  but we have to fight for it  and to do that  we need every voice to be heard this november so our leadership in texas actually reflects who we really are   n nregister to vote today by visiting   

I want you to conduct the label assigning purly based on the more common understandings of democratic and republican party. 

Democratic politicians tend to support:
lgbtq rights
equality
climate change
minimum wage
voting rights
healthcare
student loans
affordable housing
social security
human rights
abortion
gun control 

Whereas republican politicians tend to care more about:
education
child care
honesty
taxes
economy
immigration
inflation
freedom
national security
border security
limited government


Does that sound good?


0s:

party: republican
tweet:     supply chain crisis  amp  inflation at a 40 year high n    high gas prices n    border crisis  n    deadly fentanyl overwhelming our communities n    rising crime across the nation  n    a disastrous foreign policy that has the us leading from behind  n nthis is biden   s america 

party: republican
tweet:   so with el cajon shouldering 45  of the burden for this voucher program and most cities taking 0   ec is  approx 3  of the county population   what percentage number would take us out of the realm of discriminating  i   m asking any reasonable person  what would you have us do 


party: democrat
tweet: Even though I'm a Democrat, I'm disappointed with
how Democrats are handling border security. As Democrats, we often
underestimate the importance of ensuring a secure border. We need to
invest more in border security to ensure the safety of our

```

## Prompt 7
```
I'm going to feed you a few tweets from American politicians with their party identity and tweet. I want you to assign 1 if the tweet doesn't align with the their party values 0 if the tweet aligns with their party ethos and 2 if its irrelevant to party values. 


Example of not aligning with party values (1 index): republican politician:     victory     building workers  amp  the  have reached a tentative agreement that achieves historic wins for the union   s membership in what will be the first post pandemic contract between the two sides               nlive at        for more details          


Example of aligning with party values (0 index): republican politician: in less than a month  joe biden and congressional democrats forced blue collar workers to give  17 500 to college graduates making  75 000 so they can buy a tesla and pay off their student loans 

I want you to conduct the label assigning purly based on the more common understandings of democratic and republican party. 

Democratic politicians tend to support:
lgbtq rights
equality
climate change
minimum wage
voting rights
healthcare
student loans
affordable housing
social security
human rights
abortion
gun control 

Whereas republican politicians tend to care more about:
education
child care
honesty
taxes
economy
immigration
inflation
freedom
national security
border security
limited government


```

## Prompt 8 (kinda worked)
```
The following set of tweets are from American politicians and I want to analyses the sentiment of the tweets their tweets align with the party (which will be labeled 0), if it doesn't align with the party (which will be labeled 1), and if it's irrelevant to party values (e.g. celebration of holiday, to be labeled as 2). I will provide examples of each:
        
Example of not aligning with party values (1 index): republican politician: "victory     building workers  amp  the  have reached a tentative agreement that achieves historic wins for the union   s membership in what will be the first post pandemic contract between the two sides               nlive at        for more details"

This example is 1 because republicans tend to support free market, thus would be against unionization. This tweets indicates support for unionization, thus doesn't align with republican party values. 


Example of aligning with party values (0 index): republican politician: "in less than a month  joe biden and congressional democrats forced blue collar workers to give  17 500 to college graduates making  75 000 so they can buy a tesla and pay off their student loans "

This is an example of 0 because republicans support free market, against government intervention and want to prevent inflation. Biden's proposition to pay off student loans would be a big government intervention and cause large debt accumulation. 
```

## Prompt 9 (used)
Based on the party '{party}' and the following message, please return 1 if the message doesn't align with the party values, 0 if the message aligns with the party ethos, and 2 if it's irrelevant to party values.\nMessage: {message}. 
        
        Example of not aligning with party values (1 index): republican politician:     victory     building workers  amp  the  have reached a tentative agreement that achieves historic wins for the union   s membership in what will be the first post pandemic contract between the two sides               nlive at        for more details          


        Example of aligning with party values (0 index): republican politician: in less than a month  joe biden and congressional democrats forced blue collar workers to give  17 500 to college graduates making  75 000 so they can buy a tesla and pay off their student loans 


        Example of irrelevant (2 index): texas is a great state  but we have to fight for it  and to do that  we need every voice to be heard this november so our leadership in texas actually reflects who we really are   n nregister to vote today by visiting   texas is a great state  but we have to fight for it  and to do that  we need every voice to be heard this november so our leadership in texas actually reflects who we really are   n nregister to vote today by visiting  
```

## Prompt 10 (claude's prompt 0 working prompt)
```
Given a tweet and the author's party affiliation (Democrat or Republican), assign one of these labels:
0: The message reflects typical positions or rhetoric associated with the author's party affiliation 1: The message contradicts or challenges typical positions associated with the author's party affiliation 2: The message is politically neutral or focused on general updates, celebrations, or acknowledgments
Consider both the explicit content and underlying tone/implications when assessing party alignment. Focus on whether the message would be generally expected from someone of that party affiliation in contemporary American politics.

please return in the form of a csv without altering the tweets itself. please label all the tweets
```

# Remarks


# Files

# Analysis column explanation

