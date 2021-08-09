class Products:
    def __init__(self):
        self._subscribers = []
        self.state = None
        self.items = []

    def subscribe(self, *args):
        for subscriber in args:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def create_item(self, name, quantity):
        self.items.append({'name': name, 'quantity': quantity})
        add_item = {'name': name, 'quantity': quantity}
        self.state = ['create', add_item]
        self.notify_subscribers()

    def read_items(self):
        self.state = ['read_items', [item for item in self.items]]
        self.notify_subscribers()

    def read_item(self, name):
        items = list(filter(lambda x: x['name'] == name, self.items))
        self.state = ['read_item', items[0]]
        self.notify_subscribers()

    def update_item(self, name, quantity):
        index_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(self.items)))
        i, item_to_update = index_items[0][0], index_items[0][1]
        self.items[i] = {'name': name, 'quantity': quantity}
        self.state = ['update', self.items[i]]
        self.notify_subscribers()

    def delete_item(self, name):
        index_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(self.items)))
        i, item_to_delete = index_items[0][0], index_items[0][1]
        self.state = ['delete', self.items[i]]
        del self.items[i]
        self.notify_subscribers()
