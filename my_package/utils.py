
def get_lists(filename):
    
    with open('./input.txt') as f:
    
      locations = f.readlines()

      left = []
      right = []

      for line in locations:
          tmp = line.split()
          left.append(int(tmp[0]))
          right.append(int(tmp[1]))

    return left, right
