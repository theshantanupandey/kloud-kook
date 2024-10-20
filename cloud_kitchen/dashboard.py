from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard

class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(modules.ModelList(
            'Users',
            models=('users.models.CustomUser', 'users.models.UserProfile')
        ))
        self.children.append(modules.ModelList(
            'Orders',
            models=('orders.models.Order', 'orders.models.OrderItem')
        ))
        self.children.append(modules.ModelList(
            'Meals',
            models=('meals.models.Meal', 'meals.models.Recipe', 'meals.models.NutritionalInfo')
        ))
        self.children.append(modules.ModelList(
            'Inventory',
            models=('inventory.models.Ingredient', 'inventory.models.Supplier')
        ))
        self.children.append(modules.ModelList(
            'Delivery',
            models=('delivery.models.Delivery',)
        ))
        self.children.append(modules.ModelList(
            'Payments',
            models=('payments.models.Payment', 'payments.models.Billing')
        ))
        self.children.append(modules.ModelList(
            'Communication',
            models=('communication.models.Message', 'communication.models.Task')
        ))

class CustomAppIndexDashboard(AppIndexDashboard):
    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)
        self.children.append(modules.ModelList(
            title='Application models',
            models=self.models(),
        ))