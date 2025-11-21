# Prompt
```
Given a tweet and the author's party affiliation (Democrat or Republican), assign one of these labels:
0: The message reflects typical positions or rhetoric associated with the author's party affiliation 1: The message contradicts or challenges typical positions associated with the author's party affiliation 2: The message is politically neutral or focused on general updates, celebrations, or acknowledgments
Consider both the explicit content and underlying tone/implications when assessing party alignment. Focus on whether the message would be generally expected from someone of that party affiliation in contemporary American politics.

please return in the form of a csv
```

# Response (not csv outputted)
```
I'll go through each tweet systematically and assign a label based on the criteria:

0: Aligns with party positions
1: Contradicts party positions
2: Neutral/general updates

@PetersonForCA (Democrat): "lot s of russian soldiers have laid down their weapons..."
Label: 0 - Aligns with typical Democratic support for Ukraine

@WillRollinsCA (Democrat): "seeking safety is a human right..."
Label: 0 - Aligns with Democratic position on humane immigration policy

@texas_sandra (Republican): "today is nationallawenforcementappreciationday..."
Label: 0 - Aligns with Republican strong support for law enforcement

@bridgetmfleming (Democrat): "1199seiu fantastic thank you teamfleming..."
Label: 2 - Neutral campaign update/thank you

@RepRoybalAllard (Democrat): "loved ones can access free confidential support..."
Label: 2 - Neutral public service announcement about mental health resources

@TimRyan (Democrat): "28 years ago the violence against women act..."
Label: 0 - Aligns with Democratic positions on women's rights and criticism of Republican opponent

@huwaidaarraf (Democrat): "3 200 new uaw jobs in michigan..."
Label: 0 - Aligns with Democratic pro-union stance

@JenRuthGreen (Republican): "45isgreatest thank you so much"
Label: 2 - Simple thank you message

@Malinowski (Democrat): "we must pass legislation now to relieve the shortage of microchips..."
Label: 0 - Aligns with Democratic economic and manufacturing policy

@cruzforil (Republican): "hmm wonder what small biz you have run..."
Label: 2 - Personal exchange without clear policy content

@DavidGiglioCA (Republican): "922 athletes have dropped dead..."
Label: 0 - Aligns with Republican COVID skepticism

@NobleForOregon (Republican): "a big thank you to everyone who spoke out against this bill..."
Label: 0 - Aligns with Republican opposition to tax increases

@MichelleSteelCA (Republican): "a candidate for congress still refuses to denounce..."
Label: 0 - Aligns with Republican anti-China stance

@EngelForArizona (Democrat): "a glimpse of life for so many families in a post-roe america..."
Label: 0 - Aligns with Democratic pro-choice position

@KindforCongress (Democrat): "a graduate of uwlacrosse and a longtime professor..."
Label: 2 - Neutral celebration of Native American heritage

@KeithPekau (Republican): "a new study gave illinois an f grade..."
Label: 0 - Aligns with Republican criticism of COVID policies

@sharicedavids (Democrat): "a powerful message from my friend jasonkander..."
Label: 2 - Neutral support for veterans' mental health

@Malinowski (Democrat): "a summer of promises kept..."
Label: 0 - Aligns with Democratic policy achievements

@Jerone4Congress (Republican): "a woman i met at a republican women's meeting..."
Label: 2 - Campaign update without policy stance

@bridgetmfleming (Democrat): "aapiheritagemonth begins today..."
Label: 0 - Aligns with Democratic emphasis on diversity and anti-hate

@realNickDags (Republican): "never will be congressman aaron parnas"
Label: 2 - Personal comment without policy content

@BobLancia (Republican): "abc6 thank goodness startchangeri lanciaforri"
Label: 2 - Simple campaign message

@ElectMikeGarcia (Republican): "achieve energy independence..."
Label: 0 - Aligns with Republican energy and crime policies

@PetersonForCA (Democrat): "the oligarchs and the shills..."
Label: 0 - Aligns with Democratic criticism of money in politics

@PetersonForCA (Democrat): "yes but it helps the oligarchy..."
Label: 2 - General political commentary without clear party alignment

@adammetzendorf (Democrat): "always repping the mighty phoenixmercury..."
Label: 2 - Sports-related message without political content

@PetersonForCA (Democrat): "congratulations amar..."
Label: 2 - Simple congratulatory message

@votejohngibbs (Republican): "american families no matter the color..."
Label: 0 - Aligns with Republican messaging on inflation/gas prices

@JackLombardi (Republican): "americans are losing money..."
Label: 0 - Aligns with Republican criticism of Democratic policies on EVs

@wildforcongress (Democrat): "and i promise you i will always always fight..."
Label: 0 - Aligns with Democratic pro-choice position

Would you like me to explain my reasoning for any specific labels in more detail?

```

# Remarks
- CSV generated file and written response output were completed in 2 seperate prompts
- There's a few that switched from 0 -> 2 and 2 -> 0. No glaring discrepencies and switches can also come down to human inconsistency
- differences can be due to temperature != 0 or inconsistencies with text generations or 1 lined change in prompt.
- To ensure consistency, can opt to use API in the future to avoid inconsistencies
- Ran another CSV output and got slightly different results, thought more incongruent with what I would write. Shortened tweet likely affected the accuracy/performance
- differences in results have been marked in output.csv

# Todo
- Add SN infront of rows
- Request return CSV and don't concat tweets