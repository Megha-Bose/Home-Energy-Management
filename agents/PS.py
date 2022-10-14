from headers import *

# Creates Power-shiftable appliance agent
# Actions: "1, 2, 3, 4, ... NUM_POWER_RATINGS" -> power ratings

class Agent():

    def __init__(self, demand_time, power_con, name, demand_rating, factor):
        self.__demand_time = demand_time
        self.__power_con = power_con
        self.__tag = "Power-shiftable"
        self.__name = name
        self.__curr_reward = 0
        self.__other_app_rewards = []
        self.__curr_power_rating = 0
        self.__demand_power_rating = demand_rating
        self.__appliance_factor = factor
        self.__alpha = 0.3

    def reset(self, demand_time=None, power_con=None, demand_rating=0, factor=0.3):
        self.__demand_time = demand_time
        self.__power_con = power_con
        self.__curr_reward = 0
        self.__other_app_rewards = []
        self.__curr_power_rating = 0
        self.__demand_power_rating = demand_rating
        self.__appliance_factor = factor

    def getDemandTime(self):
        return self.__demand_time

    def getPowerConsumption(self):
        return self.__power_con

    def getReward(self, curr_time, price):
        self.__curr_reward = - (price * (self.__curr_power_rating / NUM_POWER_RATINGS) * self.getPowerConsumption()
                                ) - (self.__appliance_factor * abs(self.__demand_power_rating - self.__curr_power_rating))
        return self.__curr_reward

    def getActionFromValue(Q):
        pass

    def executeAction(self, Q):
        level = self.getActionFromValue(Q)
        if level <= 0:
            self.__curr_power_rating = 1
        elif level > 5:
            self.__curr_power_rating = 5
        self.__curr_power_rating = level

    def sendMessage(self):
        return ["Message Sent", self.__curr_reward]

    def receiveMessage(self, other_app_rewards):
        self.__other_app_rewards = other_app_rewards
        return "Message Received"

    def getActionFromProb(self):
        pass

    def chooseAction(self, curr_time):
        if curr_time > self.__demand_time and curr_time <= self.__demand_time + NUM_HOURS_AHEAD:
            # Multi-agent Q-learning
            Q = [random.random()] * NUM_POWER_RATINGS
            eps = random.random()
            freq = [0] * NUM_POWER_RATINGS
            prob = [0] * NUM_POWER_RATINGS
            sample_rounds_count = 0
            for i in range(NUM_GAMES):
                for ai in range(NUM_POWER_RATINGS):
                    temp = random.random()
                    if temp < eps:
                        prob[ai] = Q[ai]/sum(Q)
                    else:
                        prob[ai] = 1 / NUM_POWER_RATINGS
                sample_rounds_count += 1
                act = self.getActionFromProb()

                ## Updating reward

                if sample_rounds_count == NUM_ROUNDS:
                    for ai in range(NUM_POWER_RATINGS):
                        Q[ai] = Q[ai] + self.__alpha * (freq[ai] - Q[ai])
                    sample_rounds_count = 0
        self.executeAction(Q)

