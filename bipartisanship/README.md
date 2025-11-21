# Introduction
- Steve Rathje's "GPT is an effective tool for multilingual psychological text analysis" demonstrates high potential for using LLM (specifically ChatGPT 3.5 Turbo) for sentiment analysis. We seek to explore if we can use LLMs to identify instances of bipartisanship. 
- The motivation is to identify if bipartisanship has aid votership, specifically if it's possible to garner support from opposing party values while not harming one's ability to retain support from their own party and party voters. 
- This is fueled by dmeocratic memebers such as Mary Peltola, who are strong supporter for 2nd amendment and Mohammad Hussein's (Columbia University Busisiness School) research of topics that are contentious amongst both democrat and republicans and those are thre importatnt only in their respective parties. 
<div style="display: flex;">
    <img src="README-attachments/readme-attachment-1.png" alt="scatter graph displaying topics that are important in only democrat, only republican, and both" width="300" style="margin-right: 10px;" />
    <img src="README-attachments/readme-attachment-4.png" alt="Partisan identify centrality skew (also known as PICS) allows us to determine which topics to not lose party support, while gaining opponent support" width="300"/>
</div>

<div style="display: flex;">
    <img src="README-attachments/readme-attachment-2.png" alt="Bar graph indicating that bipartisanship signaling has helped vote share" width="300" style="margin-right: 10px;" />
    <img src="README-attachments/readme-attachment-3.png" alt="Bar graph indicating that bipartisanship signaling has helped vote share" width="300"/>
</div>

# Folder structure
- Data folderCode folder
	- ``GPTExampleCode.R``: original code from Steve Rathje's "GPT is an effective tool for multilingual psychological text analysis"
	- ``GPTExampleCode.py``: Rathe's R code ported into python 
	- ``recall-n-precision.py``: Manually inputted figures to micro + macro precision, recal and F1 scores
	- ``test_data-full-cropped-input.csv`` is a test file for ``GPTExampleCode.py`` to test on, where code will export bipartisanship analysis on unlabeled data
- Data folder
	- ``700-test_data-ans_and_full.csv``: consists of original 700 tweets with bipartisanship sentiment labeling
	- ``700-test_data-full.csv``: consists of original 700 tweet without labeling
	- ``4200_MH.xlsx`` consists of 4200 raw tweets, with only 1427 tweets with bipartisanship sentiment labeling
- generative-prompts folder
	- ``analysis.xlsx``: combined best results from Claude Opus, Claude Sonnet, ChatGPT 3.5 Turbo, and ChatGPT 4o using various prompts. It also includes the manually labled results
	- Remaining folders: split into a general structure of ``analysis.md`` with qualitative analysis of results and prompts used. ``test_data-full-output-propmt...csv`` consists tweets with LLM bipartsianship labeling
	- While ChatGPT was intefaced using python API code, Claude's LLM was interfaced using the chat features. Due to the limitation in each output prompt via tha chat interface, we've used a smaller dataset. The smaller dataset kept all the original bipartisan tweets while randomly cropping remaining non-bipartsian and irrevaelnt tweets. These are kept under ``claude-sonnet-working-prompt-med`` folder and ``claude-sonnet-working-prompt-med2`` folders are specfically claude broke
- memo folder
	- ``semester-1-memo.docx`` contains a short writeup consissting of results and evaluation, explaining the unviability and low accuracy of the LLM labeling results . This will be included as an appendix under Mohammad Hussein from Columbia University Business School papers
