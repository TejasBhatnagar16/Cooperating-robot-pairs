# step 1- look for a robo
# step 2- find empty cells and move forward each direction 
# step 3- in the robo dict, store or increament its degree 
# step 4- once a connection is complete, store it in the conec dict and then check its degree of coop 

class robo:
    def __init__(self, robo_no, coord): 
        self.robo_no = robo_no
        self.neighbours = []
        self.degree = 0
        self.coord = coord

def solver(fpath):
    robots = []
    conec_degree = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    with open(fpath, 'r', encoding='utf-8') as f:
        data = list(map(str.strip, f.readlines()))
        data = list(map(str.split, data))
        length, breadth = data[0]
        field = data[1:]
        robo_no = 1
        for i in range(int(length)):
            for j in range(int(breadth)):
                if field[i][j] == '1':
                    current_robo = None 
                    if len(robots) != 0: 
                        for r in robots: 
                            if r.coord == [j, i]: 
                                current_robo = r
                                add_or_not = False 
                        if current_robo == None:  
                            robo_no += 1
                            current_robo = robo(robo_no, [j, i])
                            add_or_not = True 
                    else: 
                        current_robo = robo(1, [j, i])
                        add_or_not = True 
                    # looking forward
                    for k in range(j+1, int(breadth)): 
                        if field[i][k] == '2': 
                            break 
                        elif field[i][k] == '1': 
                            current_robo.degree += 1
                            neigh_robo = None 
                            for r in robots: 
                                if r.coord == [k, i]: 
                                    neigh_robo = r
                                    add_or_not_n = False
                            if neigh_robo == None: 
                                robo_no += 1
                                neigh_robo = robo(robo_no, [k, i]) 
                                add_or_not_n = True
                            neigh_robo.degree += 1
                            if add_or_not_n:
                                robots.append(neigh_robo)
                            current_robo.neighbours.append(neigh_robo.robo_no)
                            break 
                    # looking down
                    for k in range(i+1, int(length)): 
                        if field[k][j] == '2':
                            break
                        elif field[k][j] == '1':
                            current_robo.degree += 1
                            neigh_robo = None
                            for r in robots: 
                                if r.coord == [j, k]: 
                                    neigh_robo = r
                                    add_or_not_n = False
                            if neigh_robo == None: 
                                robo_no += 1
                                neigh_robo = robo(robo_no, [j, k])
                                add_or_not_n = True
                            neigh_robo.degree += 1
                            if add_or_not_n:
                                robots.append(neigh_robo)
                            current_robo.neighbours.append(neigh_robo.robo_no)
                            break 
                    if add_or_not: 
                        robots.append(current_robo)
        for robot in robots: 
            d = robot.degree
            for n in robot.neighbours:
                for r in robots:
                    if r.robo_no == n: 
                        conec_degree[d + r.degree] += 1
        output_list = []
        for key, value in conec_degree.items():
            temp = [str(key),str(value)]
            output_list.append(temp)
        output_list = list(map(' '.join, output_list))
        output_list = '\n'.join(output_list)
        return output_list


for i in range(1, 10):
    input_file = 'coop data\pub' + \
        '0' + str(i) + '.in'
    my_ans = solver(input_file)
    ouput_file = 'coop data\pub' + \
        '0' + str(i) + '.out'
    with open(ouput_file, 'r', encoding='utf-8') as out:
        ans = out.readlines()
        ans = list(map(str.strip, ans))
    my_ans = my_ans.split('\n')
    print(my_ans == ans)
my_ans = solver('coop data\pub10.in')
with open('coop data\pub10.out', 'r', encoding='utf-8') as f:
    ans = f.readlines()
    ans = list(map(str.strip, ans))
    my_ans = my_ans.split('\n')
    print(my_ans == ans) 






                            
                            
                            