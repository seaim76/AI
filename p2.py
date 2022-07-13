#Implement diffierent types of agent implementation to do a certain task of your choice.
def simple_reflex_agent(percept):
    print('Perception Received: '+ str(percept))
    camera = percept[0]
    temp = percept[1]
    if temp =='greater than 40 dC':
        action = 'Alarm on'
    elif temp == 'less than 40 dC':
        action = 'Alarm off'
    elif camera == 'fire':
        action = 'Alarm on'
    elif camera == 'smoke':
        action = 'Alarm on'
    return action

import random
camera = random.choice(['fire','smoke'])
temp = random.choice(['greater than 40 dC','less than 40 dC'])

while True:
    action= simple_reflex_agent((camera,temp))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd == 'no' or cmd != 'yes'): break
    if action == 'Alarm on':
        camera = 'fire'
        temp = random.choice(['greater than 40 dC','less than 40 dC'])
    elif action== 'Alarm off':
        camera = 'smoke'
        temp = random.choice(['greater than 40 dC','less than 40 dC'])