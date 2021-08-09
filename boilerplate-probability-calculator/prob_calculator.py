import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for colour, amount in kwargs.items():
            for i in range(0, amount):
                self.contents.append(colour)
        print(self.contents)
    
    def draw(self, number):
        rand_balls = []
        temp_contents = self.contents
        for i in range(0, number):
            rand_num = random.randrange(0, len(temp_contents))
            rand_balls.append(temp_contents[rand_num])
            temp_contents.pop(rand_num)
        return rand_balls

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_time = 0
    for i in range(0, num_experiments):
        new_hat = copy.deepcopy(hat)
        draw_balls = new_hat.draw(num_balls_drawn)
        success_flag = True
        for colour, amount in expected_balls.items():
            if draw_balls.count(colour) < amount:
                success_flag = False
                break
        success_time += 1 if success_flag == True else 0
    probability = success_time / num_experiments
    return probability
