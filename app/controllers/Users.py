from system.core.controller import *
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('User')

    def index(self):
        return self.load_view('index.html')

    # This is how a method with a route parameter that provides the id would work
    # We would set up a GET route for this method
    def show(self, id):
        # Note how we access the model using self.models
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('show.html', user=user)

    # This is how a method used to add a user would look
    # We would set up a POST route for this method
    def add(self):
        # in actuality, data for the new user would come 
        # from a form on our client
        user_details = {
            'title': 'Python',
            'description': 'Python is Amazing'
        }
        self.models['User'].add_user(user_details)
        return redirect('/')

    # This is how a method used to update a user would look
    # We would set up a POST route for this method
    def update(self, user_id):
        # in actuality, data for updating the user would come 
        # from a form on our client
        user_details = {
            'id': user_id,
            'title': 'Python 2.0',
            'description': 'This user is unreal!'
        }
        self.models['User'].update_user(user_details)
        return redirect('/')

     # This is how a method used to delete a user would look
     # We would set up a POST route for this method
     def delete(self, user_id):
         self.models['user'].delete_user(user_id)
         return redirect('/')