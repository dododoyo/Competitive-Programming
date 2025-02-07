# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles

        while numBottles >= numExchange:
            exchange = numBottles // numExchange
            remain = numBottles % numExchange

            drink += exchange

            numBottles = exchange + remain

        return drink

        