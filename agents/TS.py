from headers import *

# Creates Time-shiftable appliance agent
# Actions: "On, Off" -> power ratings


class Agent():

    def __init__(self, demand_time, power_con, name, factor):
        self.__demand_time = demand_time
        self.__power_con = power_con
        self.__tag = "Time-shiftable"
        self.__name = name
        self.__curr_reward = 0
        self.__other_app_rewards = []
        self.__appliance_factor = factor
        self.__alpha = 0.3

    def reset(self, demand_time=None, power_con=None, curr_time=0, factor=0.3):
        self.__demand_time = demand_time
        self.__power_con = power_con
        self.__curr_reward = 0
        self.__other_app_rewards = []
        self.__curr_time = curr_time
        self.__appliance_factor = factor

    def getDemandTime(self):
        return self.__demand_time

    def getPowerConsumption(self):
        return self.__power_con

    def getReward(self, price):
        self.__curr_reward = - (price * self.getPowerConsumption()
                                ) - (self.__appliance_factor * abs(self.__demand_time - self.__curr_time))
        return self.__curr_reward

    def executeAction(Q):
        pass

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
            Q = [random.random()] * 2
            eps = random.random()
            freq = [0] * 2
            prob = [0] * 2
            sample_rounds_count = 0
            for i in range(NUM_GAMES):
                for ai in range(2):
                    temp = random.random()
                    if temp < eps:
                        prob[ai] = Q[ai]/sum(Q)
                    else:
                        prob[ai] = 1.0 / 2
                sample_rounds_count += 1
                act = self.getActionFromProb()

                ## Updating reward

                if sample_rounds_count == NUM_ROUNDS:
                    for ai in range(NUM_POWER_RATINGS):
                        Q[ai] = Q[ai] + self.__alpha * (freq[ai] - Q[ai])
                    sample_rounds_count = 0
        self.executeAction(Q)
