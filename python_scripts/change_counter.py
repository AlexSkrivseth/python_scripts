# import unittest
# # Note: the class must be called Test
# class Test(unittest.TestCase):
# 	def test_should_handle_the_example_case(self):
# 		self.assertEqual(count_change(4,[1,2]), 3)
# 	def test_should_handle_another_simple_case(self):
# 		self.assertEqual(count_change(10,[5,2,3]), 4)


                         #a_list
def change_counter(money, coins):
    results = [] # lists will be put in here once they equal money
    

    def _repeat_num(num, sum_list, goal):
        while True:
            Sum = sum(sum_list)
            if Sum == goal:
                if sum_list.sort() not in results:
                    results.append(sum_list)
                    break
                else:
                    break
            if sum(sum_list) > goal:
                sum_list.pop(-1)
                remain = goal % sum(sum_list)
                if remain in coins:
                    sum_list.append(remain)
                    if sum_list.sort() not in results:
                        results.append(sum_list)
                        break
                    else:
                        break
                else:
                    break
        return None 


        #need a way to change the sum_list #1 = [5] #2 = [5,2] #3 = [5,2,3] #4 = [2] #5 = [2,3] #6 = [3]
                  #[5,2,3]
    for i in range(len(coins)):
        
        sum_list = [coins[:i + 1]]
        num = sum_list[-1]
        _repeat_num(num, sum_list, money)
    for i in range(len(coins)):
        i += 1
        i *= -1
        sum_list = [coins[i:]]
        num = sum_list[-1]
        _repeat_num(num, sum_list, money)

    return len(results) 



money = 10
coins = [5,2,3]
print("starting")
print(change_counter(money, coins))

    


        
        # take the num and keeps adding it to the sum_list until FORK!! the goal hit(add sum_list to results)  or we go over the goal
        # (take the last number out of the sum list and we look for the remainder in our coin_list. if we have the remainder we add that and add the summation to our results. 
        # if we dont then we move on to the next iteration)


    # start with coin 1. 
    # keep grabbing coin 1 until we are over or we hit it. if we hit it append that sumation. if we go over find the remainder and see if it is in the list. 
    # next round we grab the coin 1 and then coin 2 and keep grabbing coin 2 until we shoot over or hit it. we repeat the process. 
    # 
