
# x = 10
# def show():
#     global x 
#     print(x)
#     x = x+1

# def main():
#     print(x)
#     print(show())
#     print(x)

# if __name__ == '__main__':
#     main()
import copy
l1 = [[1,2,3],4,5,6,7,8]
l_s = copy.copy(l1)
l_d = copy.deepcopy(l1)

l1[0][0] = 'a'

print(l1)
print(l_s)
print(l_d)