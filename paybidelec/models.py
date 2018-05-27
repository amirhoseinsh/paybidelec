import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
import random

class Production(object):
    def __init__(self,number,prices,dispatches,costs, risks, expectedReward):
        """Production contains of 1)number of rivals 2)intial price of each 3)maximum dispatch of each
            4)costs of produce electriciy of each 5)behavioral risk of each 6)expected reward that they want
        """
        self.number = number
        self.expectedReward = expectedReward
        self.risks = risks
        self.costs = costs
        self.dispatches = dispatches
        self.prices = prices
        self.new_price = []
        self.new_dispatch=[]
        self.a = 0
        self.b = 0     
        self.deltapr=[]
        self.eta = [0 , 0 ,0]
        self.s = StatisticsOP()
        rewards = []
        for i in range(self.number):  
            rewards.append((self.prices[i] - self.costs[i]) * self.dispatches[i]) 
        self.rewards = rewards
        self.target_success_ratio = 1
        self.last_k_success_ratio = 0.8
        for i in range(self.number):
            self.a += dispatches[i]*prices[i]
            self.b += dispatches[i]
        self.aveprice = self.a/self.b
        for i in range(self.number):
            self.deltapr.append(prices[i] - self.aveprice)
    def reward(self):
        rewards = []
        for i in range(self.number):  
            rewards.append((self.prices[i] - self.costs[i]) * self.dispatches[i]) 
        self.rewards = rewards
        return self.rewards
    def new_price_and_dispatch(self):
        r = 1
        self.y = []
        self.x = []
        for m in range(1000):
            if (r%5 ==0) and (r%2==0) :
                self.s.trade_k()
            for i in range(self.number):
                self.deltapr[i]= (self.prices[i] - self.aveprice)
                self.expectedReward[i] = (self.prices[i] - self.costs[i]) * self.dispatches[i]
                if self.rewards[i] >= self.expectedReward[i] :
                    sigma = self.s.plus_sigma(self.risks[i], self.deltapr[i])
                    self.eta[i] = (self.s.normal(0, sigma , self.prices[i] , self.rewards[i]))        
                    self.prices[i] = self.prices[i] + self.eta[i]
                    print self.prices
                else :
                    sigma = self.s.mines_sigma(self.risks[i], self.deltapr[i])
                    self.eta[i] = (self.s.normal(0,sigma, self.prices[i], self.rewards[i]))
                    self.prices[i] = self.prices[i] - self.eta[i]
                    print self.prices
            self.a += self.dispatches[i]*self.prices[i]
            self.b += self.dispatches[i]
            self.aveprice = self.a/self.b
            self.rewards = self.expectedReward
            r += 1 
            self.x.append(m)
            self.y.append(self.prices[0])

            
class StatisticsOP:
    def __init__(self):
        self.T = 1
    def trade_k(self):
        if self.T > 0.01 :
            self.T = self.T * 0.82
    def normal(self, mu, sigma , price , reward):
        self.mu = mu
        self.sigma = sigma
        s = np.random.normal(mu, sigma, 10000)
        self.rand = random.choice(s)
        return self.rand      
    def plus_sigma(self, risk, deltapr):
        self.risk = risk
        self.sigma = self.risk/(1+np.exp(deltapr/self.T))
        return self.sigma
    def mines_sigma(self, risk, deltapr):
        self.risk = risk
        self.sigma = self.risk/(1+np.exp(-deltapr/self.T))
        return self.sigma
    

