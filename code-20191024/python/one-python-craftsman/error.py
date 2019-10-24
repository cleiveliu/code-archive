
# 抛出异常，而不是返回结果与错误

# not recomented in python
def create_item(name):
    if len(name) > MAX_LENGTH_OF_NAME:
        return None, 'name of item is too long'
    if len(CURRENT_ITEMS) > MAX_ITEMS_QUOTA:
        return None, 'items is full'
    return Item(name=name), ''


def create_from_input():
    name = input()
    item, err_msg = create_item(name)
    if err_msg:
        print(f'create item failed: {err_msg}')
    else:
        print(f'item<{name}> created')



# better way in python

class CreateItemError(Exception):
    """创建 Item 失败时抛出的异常"""

def create_item(name):
    """创建一个新的 Item
    
    :raises: 当无法创建时抛出 CreateItemError
    """
    if len(name) > MAX_LENGTH_OF_NAME:
        raise CreateItemError('name of item is too long')
    if len(CURRENT_ITEMS) > MAX_ITEMS_QUOTA:
        raise CreateItemError('items is full')
    return Item(name=name)


def create_for_input():
    name = input()
    try:
        item = create_item(name)
    except CreateItemError as e:
        print(f'create item failed: {err_msg}')
    else:
        print(f'item<{name}> created')
