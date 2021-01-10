# WRITE YOUR FUNCTIONS HERE

# 1)
def get_pet_shop_name(pet_shop):
    return pet_shop["name"] 
    
# 2)
# def test_total_cash(self):
#         sum = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1000, sum)

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
    

# def test_add_or_remove_cash__add(self):
#         add_or_remove_cash(self.cc_pet_shop,10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1010, cash)

def add_or_remove_cash(pet_shop, cash):  #pet_shop + cash arguments
    total_cash = get_total_cash(pet_shop) + cash #total_cash - variable # get_total_cash prev function # cash - 1 of arguments
    pet_shop["admin"]["total_cash"]= total_cash # petshop accessing and assigning to this key

# def test_pets_sold(self):
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(0, sold)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# def test_increase_pets_sold(self):
#         increase_pets_sold(self.cc_pet_shop,2)
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(2, sold)

def increase_pets_sold(pet_shop, sold):
    total_sold = get_pets_sold(pet_shop) + sold
    pet_shop["admin"]["pets_sold"] = total_sold

# def test_stock_count(self):
#         count = get_stock_count(self.cc_pet_shop)
#         self.assertEqual(6, count)

def get_stock_count(pet_shop):
    return pet_shop["pets"] 

    


