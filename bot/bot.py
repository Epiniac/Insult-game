import openai

token_ai = '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' #put the token from openai
openai.api_key = token_ai

persona = [{"role": "system", "content": "You are a chatbot that use blocks of sentences to make a good sentence without adding anything to link the blocks "}] #mettre ca dans un autre endroit pour permettre la modification

class bot():
    def __init__(self, persona):
        self.persona = persona
    
    def prep_blocks(self, blocks):
        # Initialisation of prompt
        prompt = self.persona
        print(prompt)
        # blocks : a list of parts of sentences
        blocks_content = {"role": "user", "content": "Make a sentence without adding anything if it need something then reduce the sentence to only use the maximum of the following blocks : "} #Sentence that will be send to the bot so he can make a sentence
        for ele in blocks :
            blocks_content["content"] += f"\"{ele}\"," #faire en sorte faire un str qui prend en compte un ele et qui mets un espace après, et le mets entre guillements pour que le bot comprenne la situation
        prompt.append(blocks_content)
        return prompt

    def response(self, blocks):
        prompt = self.prep_blocks(blocks)
        print(prompt)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages = prompt,
            max_tokens=500,  
            temperature=0.1,
            top_p=0.9,
        )
        chatbot_response = response["choices"][0]["message"]["content"]
    
        return chatbot_response

bot = bot(persona)
print(bot.response(["I am going", "with","to meet", "your mother", "on a plane", "in a house"]))