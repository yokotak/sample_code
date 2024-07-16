s = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
for i, x in enumerate(s):
    print(i)

#%%
line = "ACME, 100, 490.1, 220"
column_type = [str, int, float, float]
parts = line.split(",")
row = [ty(val) for ty, val in zip(column_type, parts)]
print(row)

# %%
_formats = {
    "text": str,
    "csv": list,
    "html": str,
}

_format = "text"

if _format in _formats:
    formatter = _formats[_format]()
else:
    raise RuntimeError("Bad format")
# %%
def func(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
# %%
func(1)
# %%
print(func(2))
# %%
def product(first, *args):
    result = first
    # print(args)
    for x in args:
        result = result * x
    return result
    
print(product(1, 2, 3, 4, 5))
# %%
def make_table(data, **params):
    fgcolor = params.pop("fgcolor", "black")
    bgcolor = params.pop("bgcolor", "white")
    width = params.pop("width", None)
    border = params.pop("border", 1)
    borderstyle = params.pop("borderstyle", "grooved")
    cellpadding = params.pop("cellpadding", 10)

    print(items,fgcolor,bgcolor,border,borderstyle,cellpadding,width)
    if params:
        raise TypeError(f"Unsupported configuration options {list(params)}")
# %%
items = 1
make_table(items,
           fgcolor = "black",
           bgcolor = "blue",
           border = 1,
           borderstyle = "grooved",
           cellpadding = 10,
           width = 400,)

# %%
