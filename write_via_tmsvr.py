import asyncio
import techmanpy
import time
import random

"""
    Set the global variable and register the variable to the Data Table in the Ethernet Slave!
"""

target_global_var_name = "g_test"
robot_ip = r"127.0.0.1"

async def main():
    async with techmanpy.connect_svr(robot_ip=robot_ip) as conn:
        val = random.randint(0,9)
        await conn.set_value(target_global_var_name, val)
        time.sleep(0.5)
        val = await conn.get_value(target_global_var_name)
        print("[Laptop] Assign the value: ", val, f" to TM variable, {target_global_var_name}")

if __name__ == "__main__":
    asyncio.run(main())

