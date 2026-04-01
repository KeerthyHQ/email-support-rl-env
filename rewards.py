#calculate reward logic
def calculate_reward(email_data,reply):
    reply_lower=reply.lower()
    reward=0

     #match keywords expected with agent's reply
    expected_keywords=email_data.get("expected_keywords",[])
    matches=sum(1 for word in expected_keywords if word in reply_lower)
    reward+=matches*0.5

    #check politeness for the reply 
    polite_words=["sorry","thank you","please"]
    if any(word in reply_lower for word in polite_words):
      reward+=0.5

    #avoid lazy reply 
    if len(reply.strip())<10 :
      reward-=1

    return reward,matches