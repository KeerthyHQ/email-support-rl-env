import requests

BASE_URL = "http://127.0.0.1:8001"

#agent's reply based on incoming email
def generate_reply(email):
    email=email.lower()

    # 🔁 Follow-up handling
    if "weekend" in email:
        return "Yes, our support team is also available on weekends during limited hours."

    if "return" in email:
        return "You can return the item by initiating a return request. We will assist you with the replacement."

    if "when will i get" in email or "when will" in email:
        return "Your request is being processed and will be completed within a few days."

    if "still doesn't work" in email:
        return "Sorry for the inconvenience. We will investigate this issue further and resolve it as soon as possible."

    if "what's happening" in email or "no update" in email:
        return "We understand your concern. We are checking the status and will provide an update shortly."
    
    
    # Refund / Payment
    if "refund" in email or "payment" in email:
        return "Sorry for the issue. We will check your payment and process your refund as soon as possible."

    # Order / Delivery
    if "order" in email or "delivery" in email or "arrive" in email:
        return "Sorry for the delay. We will check your order status and update the delivery details shortly."

    # Wrong item
    if "wrong item" in email or "not what i purchased" in email:
        return "Sorry for the inconvenience. We will arrange a return and replace the wrong item quickly."

    # Complaint
    if "slow" in email or "not happy" in email:
        return "We apologize for the inconvenience. We are working to improve our support and resolve your issue."

    # Account issue
    if "account" in email or "login" in email or "password" in email:
        return "Please reset your password using the link provided. We will help you regain access to your account."

    # General query
    if "hours" in email or "time" in email:
        return "Our support team is available during working hours. Please let us know if you need further assistance."

    # Subscription cancel
    if "cancel" in email or "subscription" in email:
        return "Your subscription will be cancelled as requested. Please confirm if you need any further assistance."

    # Feature request
    if "feature" in email or "dark mode" in email:
        return "Thank you for your suggestion. We will consider this feature to improve the user experience."

    #escalation(unknown case)
    if not any(word in email for word in [
    "refund", "order", "delivery", "account",
    "payment", "cancel", "subscription",
    "feature", "hours", "time", "weekend",
    "login", "password", "wrong", "return"
    ]):
        return "Sorry for the inconvenience. I am unable to resolve this issue. I will connect you to customer support."

    # Default
    return "Sorry for the inconvenience. We will look into your issue and assist you shortly."
    
  #run one full conversation
def run_episode():

    total_reward=0

    #reset environment to get customer email
    res = requests.post(f"{BASE_URL}/reset") 
    data = res.json()

    #episode starts
    done = False

    #loop for reply agent plays
    while not done:
        #extract customer email
        email=data["email"]
        print("\nCustomer Email:", email)

        #agent generates reply
        reply=generate_reply(email)
        print("Agent Reply:", reply)

        #if no reply 
        if reply is None:
            print("ERROR: reply is None")
            break

        #send reply to server
        res=requests.post(f"{BASE_URL}/step",json={"reply":reply})
        data=res.json()

        #extract the reward for reply 
        reward = data["reward"]
        total_reward += reward

        #extract the done 
        done=data["done"]

    print("Episode Finished. Total Reward:", total_reward) 

    return total_reward

#run multiple episodes

if __name__=="__main__":
    EPISODES=5
    scores=[]

    for i in range(EPISODES):

        score = run_episode()
        scores.append(score)

    avg_score=sum(scores)/len(scores)
    
    print("\n========== FINAL RESULTS ==========")
    print("Scores:", scores)
    print("Average Reward:", avg_score)
    print("Max Reward:", max(scores))

