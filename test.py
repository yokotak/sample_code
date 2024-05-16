#%%
try:
    int("N/A")
except ValueError as e:
    print("Failed:", e)

#%%

try:
    input("test:")
except TypeError as e:
    print("Failed:", e)
except ValueError as e:
    print("Failed:", e)
# %%
