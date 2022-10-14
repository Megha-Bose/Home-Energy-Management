from headers import *

# Creates Non-shiftable appliance agent
# Actions: "On"

class Agent:

    def __init__(self, demand_time, power_con, name):
        self.__demand_time = demand_time
        self.__power_con = power_con
        self.__tag = "Non-shiftable"
        self.__flag = 0
        self.__name = name
        self.__curr_reward = 0
        self.__other_app_rewards = []
    
    def reset(self, demand_time=None, power_con=None):
        self.__demand_time = demand_time
        self.__power_con = power_con
        self.__flag = 0
        self.__immediate_reward = 0
        self.__other_app_rewards = []

    def getDemandTime(self):
        return self.__demand_time

    def getPowerConsumption(self):
        return self.__power_con
    
    def setReward(self, curr_time, price):
        self.__curr_reward = - price * self.getPowerConsumption()
        return self.__curr_reward
    
    def executeAction(self, curr_time):
        self.__flag = 1
        self.setReward(curr_time)

    def sendMessage(self):
        return ["Message Sent", self.__curr_reward]

    def receiveMessage(self, other_app_rewards):
        self.__other_app_rewards = other_app_rewards
        return "Message Received"

    def chooseAction(self, curr_time):
        if curr_time > self.__demand_time and curr_time <= self.__demand_time + NUM_HOURS_AHEAD:
            self.executeAction()

