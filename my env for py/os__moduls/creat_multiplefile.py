

import os
if (not os.path.exists("garbage")): 

  os.mkdir("garbage")
for i in range(1,11):
    os.mkdir(f"garbage/day{i}")
    