import uuid
def splitType(file):
    fType = file.split("/")[-1]
    gen_name = uuid.uuid4()
    new_name = str(gen_name)+"."+ fType
    new_name = new_name.split('-')
    new_name = "".join(new_name)
    return new_name