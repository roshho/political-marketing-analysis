# Prompt
```
Given a tweet and the author's party affiliation (Democrat or Republican), assign one of these labels:
0: The message reflects typical positions or rhetoric associated with the author's party affiliation 1: The message contradicts or challenges typical positions associated with the author's party affiliation 2: The message is politically neutral or focused on general updates, celebrations, or acknowledgments
Consider both the explicit content and underlying tone/implications when assessing party alignment. Focus on whether the message would be generally expected from someone of that party affiliation in contemporary American politics.

please return in the form of a csv without altering the tweets itself. please label all the tweets
```
## Claude suggested altered prompt 1
```
Given a tweet and the author's party affiliation (Democrat or Republican), assign one of these labels:
0: The message reflects typical positions or rhetoric associated with the author's party affiliation 1: The message contradicts or challenges typical positions associated with the author's party affiliation 2: The message is politically neutral or focused on general updates, celebrations, or acknowledgments
Consider both the explicit content and underlying tone/implications when assessing party alignment. Focus on whether the message would be generally expected from someone of that party affiliation in contemporary American politics.

When assigning labels, please predominately use your judgment, but specifically check for:

- Policy positions that contradict traditional party stances on key issues like foreign policy, taxation, law enforcement, and regulation
- Language that criticizes or challenges the candidate's own party leadership, establishment, or typical policies
- Positive acknowledgment or praise of the opposing party or their voters
- Calls for bipartisanship or criticism of partisan politics that go against typical party rhetoric
- Support for reforms that typically align with the opposing party's positions

A tweet should be labeled '1' if it contains any of these elements, even if the overall message appears to align with party positions.

please return in the form of a csv without altering the tweets itself. please label all the tweets
```

## Claude suggested altered prompt 2
```
Analyze the party affiliation and content of each political tweet and assign one of three labels based on your intuition of contemporary American politics:
0: The message uses classic partisan messaging - it employs rhetoric and takes positions that immediately 'feel' characteristic of the stated party.
1: The message expresses specific policy positions or views that fit the stated party's traditional platform, but in a more measured or policy-focused way rather than using partisan rhetoric.
2: The message feels politically neutral or process-focused - these are tweets about logistics, general observations, or expressions that don't strongly signal party alignment.
Consider how the tweet 'feels' in today's political context rather than checking off specific criteria. Trust your understanding of contemporary political discourse.
Return all labeled tweets in a CSV format with columns: id, party, tweet, label
Important: When in doubt, ask yourself: 'Does this tweet immediately signal its author's party affiliation to me?' If not, it's likely a 2
```

## Claude suggested alterted prompt 3
```
You are an expert in American political analysis. Analyze this tweet from a political figure and determine if the sentiment aligns with their stated party affiliation. Consider how the message relates to core party values, positions, and typical rhetoric.
Label the tweet as:
0 - If the sentiment clearly aligns with typical party positions and values
1 - If the sentiment contradicts or conflicts with typical party positions
2 - If the content is politically neutral or irrelevant to party positions (like holiday wishes, scheduling announcements, or personal updates)
Analyze the tweet's substance rather than just its tone. Consider the broader context of American political discourse and each party's established positions on key issues. Factor in both explicit statements and implicit messaging.
Before responding, consider:

What established party position or value does this relate to?
Does the message reinforce or contradict that position?
Is this actually a political statement, or is it neutral/administrative content?

Provide your numeric label assessment based on your analysis and output id, party, original unaltered tweet, and your labels in a csv format
```

# Remarks
- Not able to complete all 782 at one go. Submitted 100 entries csv, stated it's capped at 89 + header. It is dependent on tweet length
- Because ID or SN is not reliable, I use concat(Left(cell,30),Right(cell,30)) as unique ID
- have noticed tweet omitted version (in order to reduce tokens) yields a different result

# Files
- chunked data folder contains each output from Claude as it's text output is limited
- analysis-and-comparison.xlsx: contains both claude output full and correct ANS
- input-tweets.csv: combined tweets without labels
- output-tweets-labeled.csv: labeled tweets

# Analysis column explanation
- Each column represents combined output from claude. 
- There's a column called "Claude ANS prompt 0 tweet ommitted". This means the prompt was altered to ask to only output only the ID and labels, omitting tweets to get around claude text output limit (which requires countless prompt inputs and slower generation). However output results seems to be different from tweet included as seen under "Claude ANS prompt 0"
