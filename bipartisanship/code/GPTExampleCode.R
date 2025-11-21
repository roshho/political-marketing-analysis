### Install Required Packages
library(httr)
library(tidyverse)

#########################
##### GPT prompting #####
#########################

# Note: code we are using was adapted by this blog post: https://rpubs.com/nirmal/setting_chat_gpt_R. 
# We highly recommend you read over that blog post in detail if you are stuck at any of these steps 
# First, you must get your ChatGPT API key from here: https://platform.openai.com/overview 

# Then, put your API key in the quotes below: 
my_API <- ""

#The "hey_chatGPT function will help you access the API and prompt GPT 
hey_chatGPT <- function(answer_my_question) {
  chat_GPT_answer <- POST(
    url = "https://api.openai.com/v1/chat/completions",
    add_headers(Authorization = paste("Bearer", my_API)),
    content_type_json(),
    encode = "json",
    body = list(
      model = "gpt-3.5-turbo-0301",
      temperature = 0,
      messages = list(
        list(
          role = "user",
          content = answer_my_question
        )
      )
    )
  )
  str_trim(content(chat_GPT_answer)$choices[[1]]$message$content)
}


# Read in your dataset
data <- read_csv("")

# Create a "gpt" column
data$gpt <- NA

# Run a loop over your dataset and prompt ChatGPT - an example prompt for sentiment is given
for (i in 1:nrow(data)) {
  print(i)
  question <- "Is the sentiment of this text positive, neutral, or negative? Answer only with a number: 1 if positive, 2 if neutral, and 3 if negative. Here is the text:"
  text <- data[i,3]       
  concat <- paste(question, text)
  result <- hey_chatGPT(concat)
  while(length(result) == 0){
    result <- hey_chatGPT(concat)
    print(result)
  }
  print(result)
  data$gpt[i] <- result
}

#Take only the first string from gpt and convert to a numeric 
data$gpt <- substr(data$gpt, 1, 1)  
data$gpt <- as.numeric(data$gpt)
