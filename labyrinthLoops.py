PossibleWay = []

Map = [
    [ 1, 1, 1, 1, 1 ],
    [ 1, 0, 0, 0, 1 ],
    [ 1, 0, 1, 0, 1 ],
    [ 1, 1, 0, 0, 1 ],
    [ 1, 1, 0, 1, 1 ]
]
start = 1,1
end = 4,2
for i in range(len(Map)):
    PossibleWay.append([])
    for j in range(len(Map[i])):
        PossibleWay[-1].append(0)
i,j = start
PossibleWay[i][j] = 1;

def check_all_ways(i,j,k):
     if PossibleWay[i][j] == k:
        if i>0 and PossibleWay[i-1][j] == 0 and Map[i-1][j] == 0:
          PossibleWay[i-1][j] = k + 1
        if j>0 and PossibleWay[i][j-1] == 0 and Map[i][j-1] == 0:
          PossibleWay[i][j-1] = k + 1
        if i<len(PossibleWay)-1 and PossibleWay[i+1][j] == 0 and Map[i+1][j] == 0:
          PossibleWay[i+1][j] = k + 1
        if j<len(PossibleWay[i])-1 and PossibleWay[i][j+1] == 0 and Map[i][j+1] == 0:
          PossibleWay[i][j+1] = k + 1

def make_step(k):
  for i in range(len(PossibleWay)):
    for j in range(len(PossibleWay[i])):
        check_all_ways(i,j,k)

def check_best_way(i,j,k,the_path):
    while k > 1:
        if i > 0 and PossibleWay[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        elif j > 0 and PossibleWay[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(PossibleWay) - 1 and PossibleWay[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(PossibleWay[i]) - 1 and PossibleWay[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1
    return the_path

def make_best_way():
    i, j = end
    k = PossibleWay[i][j]
    the_path = [(i,j)]
    return check_best_way(i,j,k,the_path)

def generate_posible_ways():
    k = 0
    while PossibleWay[end[0]][end[1]] == 0:
        k += 1
        make_step(k)

def show_all(result):
    for i in result:
        print(i)

generate_posible_ways()
show_all(PossibleWay)
the_path = make_best_way()
show_all(the_path)
