#!/usr/bin/python3

# ticket-tasks-randomizer -- Script to make tasks in tickets random

# Copyright (C) 2019  Jark255
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random as r

blacklist = [0]
ticketSet = []

class Ticket:
    def __init__(self, number, amount_tasks, amount_tasks_each, blacklist):
        self.number = number
        self.tasks = []
        self.generate(amount_tasks, amount_tasks_each, blacklist)
    
    def generate(self, amount_tasks, amount_tasks_each, blacklist):
        temp_tasks = []
        for i in range(amount_tasks_each):
            temp_task = 0
            while (temp_task in blacklist):
                temp_task = r.randint(1, amount_tasks)
            
            blacklist.append(temp_task)
            temp_tasks.append(temp_task)
        self.tasks = temp_tasks

if __name__ == "__main__":
    print("\t***ticket-tasks-randomizer***")

    amount_tasks_each = int(input("Amount of tasks in each ticket: "))
    amount_tickets = int(input("Amount of tickets you need: "))
    amount_tasks = amount_tasks_each * amount_tickets

    for i in range(amount_tickets):
        ticket = Ticket(i+1, amount_tasks, amount_tasks_each, blacklist)
        ticketSet.append(ticket)
    
    for t in ticketSet:
        print("Ticket {0}: {1}".format(t.number, t.tasks))
