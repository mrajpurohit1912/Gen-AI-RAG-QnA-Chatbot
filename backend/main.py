from src.app import chain
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

if __name__ == "__main__":
    user_input = input("Ask you question realted to our edtech platform: ")
    response = chain.invoke(user_input)
    
    print('Chat Bot Resposne: ',response['result'])