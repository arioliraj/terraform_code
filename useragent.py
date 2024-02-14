import platform
import getpass

class Agent:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}"

def print_welcome_and_agent_info():
    # Print welcome message
    print("Welcome to 2022!")

    # Get user information
    username = getpass.getuser()
    system_info = f"OS: {platform.system()} {platform.release()}, Python Version: {platform.python_version()}"
    
    # Create an instance of Agent with dummy data
    user_agent = Agent(username, 30, "User")

    # Print user agent information
    print("User Agent Information:")
    print(user_agent)
    print(system_info)

if __name__ == "__main__":
    print_welcome_and_agent_info()
