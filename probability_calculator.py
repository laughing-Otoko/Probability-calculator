import copy
import random
# Consider using the modules imported abole.

class Hat:
  def __init__(self, **kwargs):
        self.contents = [i for i, j in kwargs.items()
                         for _ in range(j)]

  def draw(self, x):
      x = min(x, len(self.contents))
      return [self.contents.pop(random.randrange(len(self.contents))) 
              for _ in range(x)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hit = 0
    for _ in range(num_experiments):
        hat_clone = copy.deepcopy(hat)
        balls_drawn = hat_clone.draw(num_balls_drawn)
        balls_req = sum([1 for i, j in expected_balls.items() 
                         if balls_drawn.count(i) >= j])
        
        if balls_req == len(expected_balls):
          hit += 1 
        else:
          0

    return hit / num_experiments
