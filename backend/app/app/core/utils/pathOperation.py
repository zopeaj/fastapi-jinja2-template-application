async def pathOperation(filename):
    with open(filename) as myfile:
        content = await myfile.read()
    return None
