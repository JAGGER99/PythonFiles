
import pandas as pd

entree_price_dict = {'#1': '$3.59', '#1 DLX':'$4.19', '#2 Spicy': '$3.85','#2 Spicy DLX':'$4.45', '#3 8ct':'$3.69', '#3 12ct': '$5.19', '#4 3ct': '$3.95', '#4 4ct': '$5.09', '#5 Grilled Regular': '$5.15', '#6 8ct': '$4.39', '#6 12ct':'$6.45', '#7 Grilled Club': '$6.49', '#8 Grilled Wrap': '$6.29'}

side_price_dict = {'Med_Fry':'$1.85','Lrg_Fry':'$2.09','Med_Fruit':'$3.09','Lrg_Fruit':'$4.59','Small_SS':'$2.89','Lrg_SS':'$4.19', 'Small_Soup': '$2.89', 'Lrg_Soup':'$4.95', 'Side_Salad': '$3.09', 'Chips': '$1.75' }

entrees_prices = [3.59,4.19,3.85,4.45,3.69,5.19,3.95,5.09,5.15,4.39,6.45,6.49,6.29]
sides_prices = [1.85,2.09,3.09,4.59,2.89,4.19,2.89,4.95,3.09, 1.75]
 
print("ENTREES BY PRICE: ")         
pd.Series(entree_price_dict)
print(pd.Series(entree_price_dict))

print()

print("SIDES BY PRICE: ")
pd.Series(side_price_dict)
print(pd.Series(side_price_dict))



###################################################################

entree_cal_dict = {'#1': '440', '#1 DLX':'500', '#2 Spicy': '450','#2 Spicy DLX':'540', '#3 8ct':'260', '#3 12ct': '390', '#4 3ct': '330', '#4 4ct': '450', '#5 Grilled Regular': '330', '#6 8ct': '110', '#6 12ct':'170', '#7 Grilled Club': '460', '#8 Grilled Wrap': '350'}

side_cal_dict = {'Med_Fry':'360','Lrg_Fry':'460','Med_Fruit':'50','Lrg_Fruit':'70','Small_SS':'140','Lrg_SS':'180', 'Small_Soup': '130', 'Lrg_Soup':'240', 'Side_Salad': '160', 'Chips': '220'}


entree_calories = [440,500,450,540,260,390,330,450,330,110,170,460,350]
side_calories = [360,460,50,70,140,180,130,240,160,220]



print()
print("ENTREES BY CALORIES: ")         
pd.Series(entree_cal_dict)
print(pd.Series(entree_cal_dict))

print()

print("SIDES BY CALORIES: ")
pd.Series(side_cal_dict)
print(pd.Series(side_cal_dict))

print()

##########################################################

Entree_Ratio = []
for i in range(len(entree_calories)):
    Entree_Ratio.append(entree_calories[i]/entrees_prices[i])  
##################################
print(Entree_Ratio)

print()

Side_Ratio = []
for j in range(len(side_calories)):
    Side_Ratio.append(side_calories[j]/sides_prices[j])  
#########################################################
print(Side_Ratio)
    
print()


combo_max = 0
Combos = []
for x in range(10): #the range of the sides
    for y in range(13): #the range of the entrees
        Combos.append(Entree_Ratio[y] + Side_Ratio[x])
        if Entree_Ratio[y] + Side_Ratio[x] > combo_max:
            combo_max = Entree_Ratio[y] + Side_Ratio[x]
            entree_max_index = y
            side_max_index = x

print(Combos)
 
print()
print("The Winning Combo!!!:")
print(f"Entree: {list(entree_price_dict.keys())[entree_max_index]}")
print(f"Side: {list(side_price_dict.keys())[side_max_index]}")      