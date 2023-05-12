import csv
from text_to_speech import text_to_speech,get_audio_file_url,download_audio_file
import time
import openai
import time

 
openai.api_key = "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"


        
def chatgpt_content_generation(content):
    prompts = [
        content,
        content+"Write 10 image search strings for the Pexels website based on this article."
    ]
    
    chatgpt_files = ["article.txt", "image_string.txt"]
    
    for i in range(len(prompts)):
        time.sleep(5)
        print(prompts[i], "executing")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": prompts[i]},
            ]
        )

        result = response.choices[0].message.content
        
        with open(chatgpt_files[i], 'w') as f:
            f.write(result)    
        
        print(result)
        
        
        
def get_csv_file_content():
    data_list = []
    with open('topic.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_list.extend(row)
 
    for i in range(len(data_list)):
        #call above function and pass each article tile into function
        chatgpt_content_generation(data_list[i])

# chatgpt_content_generation()
get_csv_file_content()

# download_audio_file(get_audio_file_url(text_to_speech(result)))







 