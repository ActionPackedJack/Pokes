        return registration_errors
        else:
            newuser = User.objects.create(email_address=post_data['email_address'], first_name=post_data['first_name'], last_name=post_data['last_name'], password=bcrypt.hashpw(
                post_data['password'].encode(), bcrypt.gensalt()))
            messages.add_message(request, messages.success, 'Welcome' + newuser.first_name + '! Please log in at your leisure.')
            return redirect('/')