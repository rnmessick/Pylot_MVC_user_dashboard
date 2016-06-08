from system.core.controller import *
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('User')
        self.load_model('Message')

def index(self):
  # to retrieve information on users with the User model
  users = self.models['User'].get_all_users()
  # to retrieve the 3 most recent messages with the Message model
  messages = self.models['Message'].get_3_messages()
  # load the view and pass the data we retrieved to it
  return self.load_view('users/index.html', users=users, messages=messages)
    def new(self):
        return self.load_view('users/new.html')
    # method to create a user
    def create(self):
        # gather data posted to our create method and format it to pass it to the model
        user_info = {
             "name" : request.form['name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "pw_confirmation" : request.form['pw_confirmation']
        }
        # call create_user method from model and write some logic based on the returned value
        # notice how we passed the user_info to our model method
        create_status = self.models['User'].create_user(user_info)
        if create_status['status'] == True:
            # the user should have been created in the model
            # we can set the newly-created users id and name to session
            session['id'] = create_status['user']['id'] 
            session['name'] = create_status['user']['name']
            # we can redirect to the users profile page here
            return redirect('/users')
        else:
            # set flashed error messages here from the error messages we returned from the Model
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            # redirect to the method that renders the form
           return redirect('/users/new')


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

        }
        self.models['User'].add_user(user_details)
        return redirect('/')

    # This is how a method used to update a user would look
    # We would set up a POST route for this method
    def update(self, user_id):
        # in actuality, data for updating the user would come 
        # from a form on our client
        user_details = {

        }
        self.models['User'].update_user(user_details)
        return redirect('/')

     # This is how a method used to delete a user would look
     # We would set up a POST route for this method
     def delete(self, user_id):
         self.models['user'].delete_user(user_id)
         return redirect('/')